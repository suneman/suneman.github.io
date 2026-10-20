# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Regenerate the inline maps on /directions.

Two maps, same recipe: pull buildings, roads, rail and greenery from the
OpenStreetMap API, draw them as a theme-aware inline SVG (every colour is one
of the site's CSS custom properties, so dark mode is free), and splice the
result into src/content/pages/20140910_directions.md between marker comments.

  dtu  DTU Lyngby Campus: the light rail through campus and the walk from the
       Akademivej stop to Building 321.        <!-- dirmap:start/end -->
  ku   CSS (Kommunehospitalet) in Copenhagen: the walk from Nørreport to the
       left gate of Building 1, drawn with Øster Farimagsgade horizontal, like KU's
       own campus map.                          <!-- kumap:start/end -->

    uv run branding/build-directions-map.py            # rewrite both maps
    uv run branding/build-directions-map.py ku         # just one
    uv run branding/build-directions-map.py --stdout   # print instead of splicing

Stop and door coordinates are hard-coded from OSM because the map API tiles
don't carry route relations; update them if anything moves, which it won't.
"""
import json
import math
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

PAGE = Path(__file__).resolve().parent.parent / "src/content/pages/20140910_directions.md"
UA = {"User-Agent": "sunelehmann.com directions map (sljo@dtu.dk)"}
MAJOR = {"primary", "secondary", "tertiary", "primary_link", "secondary_link", "tertiary_link"}
MINOR = {"residential", "unclassified", "service", "living_street", "pedestrian"}
PATH = {"footway", "path", "cycleway", "steps", "track", "corridor"}
MOTORWAY = {"motorway", "motorway_link", "trunk", "trunk_link"}
WALKABLE = MAJOR | MINOR | PATH


# ----------------------------------------------------------------- geometry
class Frame:
    """Local metres around an origin, optionally rotated; SVG y points down."""

    def __init__(self, lat0, lon0, rot_deg=0.0):
        self.lat0, self.lon0 = lat0, lon0
        self.kx, self.ky = math.cos(math.radians(lat0)) * 111320, 111320
        self.c, self.s = math.cos(math.radians(rot_deg)), math.sin(math.radians(rot_deg))
        self.rot = rot_deg

    def xy(self, lat, lon):
        x, y = (lon - self.lon0) * self.kx, (lat - self.lat0) * self.ky
        return (x * self.c - y * self.s, x * self.s + y * self.c)


def S(p):
    return f"{p[0]:.0f},{-p[1]:.0f}"


def P(pts):
    return " ".join(("M" if i == 0 else "L") + S(p) for i, p in enumerate(pts))


def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    a, b = pts[0], pts[-1]
    if math.dist(a, b) < 1e-9:  # closed ring: split at the point farthest from the start
        idx = max(range(1, len(pts) - 1), key=lambda i: math.dist(a, pts[i]))
        return rdp(pts[: idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy) or 1e-9
    dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        p = pts[i]
        dist = abs(dy * p[0] - dx * p[1] + b[0] * a[1] - b[1] * a[0]) / L
        if dist > dmax:
            dmax, idx = dist, i
    if dmax > eps:
        return rdp(pts[: idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [a, b]


def length(pts):
    return sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))


# --------------------------------------------------------------------- OSM
def fetch(tiles):
    """OSM API map tiles -> (ways, nodes). ways = [(tags, node_ids, [(lat, lon)])]."""
    nodes, ways, relations = {}, {}, {}
    for bbox in tiles:
        url = f"https://api.openstreetmap.org/api/0.6/map?bbox={bbox}"
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180) as r:
            root = ET.fromstring(r.read())
        for n in root.iter("node"):
            nodes[n.get("id")] = (float(n.get("lat")), float(n.get("lon")))
        for w in root.iter("way"):
            ways[w.get("id")] = ({t.get("k"): t.get("v") for t in w.findall("tag")},
                                 [nd.get("ref") for nd in w.findall("nd")])
        print(f"  fetched {bbox}: {len(nodes)} nodes, {len(ways)} ways", file=sys.stderr)
        for rel in root.iter("relation"):
            tags = {t.get("k"): t.get("v") for t in rel.findall("tag")}
            if tags.get("type") != "multipolygon":
                continue
            members = [m.get("ref") for m in rel.findall("member") if m.get("type") == "way"]
            relations[rel.get("id")] = (tags, members)
    out = [(t, refs, [nodes[r] for r in refs if r in nodes]) for t, refs in ways.values()]
    # a multipolygon's outer and inner rings become one way each, with the relation's tags;
    # the SVG fill rule (evenodd) turns inner rings into holes
    for tags, members in relations.values():
        for ring in assemble_rings([ways[m][1] for m in members if m in ways]):
            out.append((tags, ring, [nodes[r] for r in ring if r in nodes]))
    return [w for w in out if len(w[2]) >= 2], nodes


def assemble_rings(segments):
    """Join way segments end to end into closed rings of node ids."""
    segs = [list(s) for s in segments if len(s) >= 2]
    rings = []
    while segs:
        ring = segs.pop()
        while ring[0] != ring[-1]:
            for i, s in enumerate(segs):
                if s[0] == ring[-1]:
                    ring += s[1:]
                elif s[-1] == ring[-1]:
                    ring += s[-2::-1]
                elif s[-1] == ring[0]:
                    ring = s[:-1] + ring
                elif s[0] == ring[0]:
                    ring = s[::-1][:-1] + ring
                else:
                    continue
                segs.pop(i)
                break
            else:
                break  # open chain; draw it anyway
        rings.append(ring)
    return rings


def walk_route(ways, nodes, frame, src, dst):
    """Shortest pedestrian path (Dijkstra) between two local points; returns local pts."""
    import heapq
    pos = {k: frame.xy(*v) for k, v in nodes.items()}
    adj = {}
    for t, refs, _ in ways:
        underground = t.get("tunnel") or t.get("indoor") or str(t.get("layer", "")).startswith("-") or str(t.get("level", "")).startswith("-")
        if t.get("highway") in WALKABLE and t.get("foot") != "no" and t.get("access") not in ("private", "no") and not underground:
            for a, b in zip(refs, refs[1:]):
                if a in pos and b in pos:
                    w = math.dist(pos[a], pos[b])
                    adj.setdefault(a, []).append((b, w))
                    adj.setdefault(b, []).append((a, w))
    near = lambda p: min(adj, key=lambda n: math.dist(pos[n], p))
    s, d = near(src), near(dst)
    dist, prev, pq = {s: 0}, {}, [(0, s)]
    while pq:
        dd, u = heapq.heappop(pq)
        if u == d:
            break
        if dd > dist[u]:
            continue
        for v, w in adj[u]:
            if dd + w < dist.get(v, 1e18):
                dist[v], prev[v] = dd + w, u
                heapq.heappush(pq, (dd + w, v))
    if d not in prev:
        sys.exit("no walking route found")
    path = [d]
    while path[-1] != s:
        path.append(prev[path[-1]])
    return [pos[n] for n in path[::-1]]


# --------------------------------------------------------------------- SVG
STYLE = """
.{cls}{{width:100%;height:auto;display:block;margin:1.5em 0;font-family:Inter,system-ui,sans-serif}}
.{cls} .paper{{fill:var(--surface-card,#f1f0ea)}}
.{cls} .green{{fill:var(--accent-olive,#7e8d20);fill-opacity:.12}}
.{cls} .water{{fill:var(--accent-teal,#107078);fill-opacity:.16}}
.{cls} .bld{{fill:var(--bg,#fbfbf8);stroke:var(--fg-muted,#666);stroke-width:.8;stroke-opacity:.6}}
.{cls} .area-hi{{fill:var(--accent-sienna,#b8451e);fill-opacity:.07;stroke:var(--accent-sienna,#b8451e);stroke-width:1;stroke-dasharray:6 5;stroke-opacity:.6}}
.{cls} .rd{{fill:none;stroke:var(--fg-muted,#666);stroke-linecap:round;stroke-linejoin:round}}
.{cls} .rd-mw{{stroke-width:7;stroke-opacity:.22}}
.{cls} .rd-major{{stroke-width:4.5;stroke-opacity:.3}}
.{cls} .rd-minor{{stroke-width:2.5;stroke-opacity:.25}}
.{cls} .rd-path{{stroke-width:1;stroke-opacity:.22}}
.{cls} .rail{{fill:none;stroke:var(--accent-oxblood,#992c44);stroke-width:3;stroke-opacity:.5;stroke-dasharray:14 6}}
.{cls} .tram{{fill:none;stroke:var(--accent-olive,#7e8d20);stroke-width:6;stroke-linecap:round;stroke-linejoin:round}}
.{cls} .tram-core{{fill:none;stroke:var(--bg,#fbfbf8);stroke-width:1.5;stroke-dasharray:9 9;stroke-opacity:.9}}
.{cls} .walk{{fill:none;stroke:var(--accent-sienna,#b8451e);stroke-width:9;stroke-dasharray:12 10;stroke-linecap:round;stroke-linejoin:round}}
.{cls} .stop{{fill:var(--bg,#fbfbf8);stroke:var(--accent-olive,#7e8d20);stroke-width:4}}
.{cls} .stop-here{{stroke:var(--accent-sienna,#b8451e)}}
.{cls} .stn{{fill:var(--bg,#fbfbf8);stroke:var(--accent-oxblood,#992c44);stroke-width:4}}
.{cls} .b321{{fill:var(--accent-sienna,#b8451e);stroke:none}}
.{cls} .pin{{fill:var(--accent-sienna,#b8451e)}}
.{cls} .bus{{fill:var(--accent-oxblood,#992c44)}}
.{cls} text{{fill:var(--fg,#0e0e10);font-size:17px}}
.{cls} .lbl-stop{{font-weight:600;font-size:19px}}
.{cls} .lbl-stop tspan.sub{{font-weight:400;font-size:15px;fill:var(--fg-muted,#666)}}
.{cls} .lbl-road{{font-size:15px;fill:var(--fg-muted,#666);letter-spacing:.06em}}
.{cls} .lbl-here{{font-weight:600;font-size:19px;fill:var(--accent-sienna,#b8451e)}}
.{cls} .lbl-muted{{fill:var(--fg-muted,#666);font-size:15px}}
.{cls} .lbl-area{{fill:var(--accent-olive,#7e8d20);font-size:15px;font-style:italic;letter-spacing:.04em}}
.{cls} .halo{{stroke:var(--surface-card,#f1f0ea);stroke-width:5;stroke-linejoin:round;paint-order:stroke}}
.{cls} .scale{{stroke:var(--fg,#0e0e10);stroke-width:2}}
.{cls} .arrow{{fill:var(--fg,#0e0e10)}}
@media (max-width:600px){{
  .{cls} text{{font-size:24px}} .{cls} .lbl-stop{{font-size:26px}} .{cls} .lbl-stop tspan.sub{{font-size:20px}}
  .{cls} .lbl-road{{font-size:21px}} .{cls} .lbl-here{{font-size:26px}} .{cls} .lbl-muted{{font-size:21px}} .{cls} .lbl-area{{font-size:21px}}
}}
"""


class Canvas:
    """Collects base layers for one map and renders the SVG skeleton."""

    def __init__(self, cls, frame, extent, ways, road_names, title, desc):
        self.cls, self.frame, self.title, self.desc = cls, frame, title, desc
        self.X0, self.X1, self.Y0, self.Y1 = extent
        self.bld, self.green, self.water, self.rail, self.tram = [], [], [], [], []
        self.roads = {"major": [], "minor": [], "path": [], "mw": []}
        self.named = {}
        for t, _, ll in ways:
            pts = [frame.xy(*p) for p in ll]
            if not self.clip(pts, 60):
                continue
            if t.get("building"):
                self.bld.append(P(rdp(pts, 0.8)) + "Z")
            elif t.get("leisure") in ("garden", "park") or t.get("landuse") in ("grass", "cemetery") or t.get("natural") == "wood":
                self.green.append(P(rdp(pts, 1.5)) + "Z")
            elif t.get("natural") == "water":
                self.water.append(P(rdp(pts, 1.5)) + "Z")
            elif t.get("railway") == "light_rail" and t.get("name") == "Hovedstadens Letbane":
                self.tram.append(rdp(self.clip(pts, 120), 1.0))
            elif t.get("railway") in ("rail", "light_rail", "subway") and t.get("tunnel") != "yes" and t.get("service") is None:
                cp = self.clip(pts, 60)
                if len(cp) > 1:
                    self.rail.append(P(rdp(cp, 1.5)))
            elif t.get("highway"):
                h, cp = t["highway"], self.clip(pts)
                if len(cp) < 2:
                    continue
                pth = P(rdp(cp, 1.5))
                if h in MOTORWAY:
                    self.roads["mw"].append(pth)
                elif h in MAJOR:
                    self.roads["major"].append(pth)
                elif h in MINOR:
                    self.roads["minor"].append(pth)
                elif h in PATH and length(cp) >= 20:
                    self.roads["path"].append(pth)
                n = t.get("name")
                if n in road_names and h not in PATH and length(cp) > self.named.get(n, (0,))[0]:
                    self.named[n] = (length(cp), cp)

    def clip(self, pts, pad=40):
        return [p for p in pts if self.X0 - pad < p[0] < self.X1 + pad and self.Y0 - pad < p[1] < self.Y1 + pad]

    def road_label(self, name, pid, off, dy):
        if name not in self.named:
            print(f"  no road named {name!r} in extent", file=sys.stderr)
            return "", ""
        _, pts = self.named[name]
        if pts[0][0] > pts[-1][0]:
            pts = pts[::-1]  # left to right, so the text reads upright
        return (f'<path id="{pid}" d="{P(rdp(pts, 1.0))}" fill="none"/>',
                f'<text class="lbl-road" dy="{dy}"><textPath href="#{pid}" startOffset="{off}">{name}</textPath></text>')

    def scale_bar(self, metres, corner="sw"):
        sx, sy = (self.X0 + 30 if corner == "sw" else self.X1 - 30 - metres), -self.Y0 - 30
        return (f'<line class="scale" x1="{sx}" y1="{sy}" x2="{sx+metres}" y2="{sy}"/><line class="scale" x1="{sx}" y1="{sy-6}" x2="{sx}" y2="{sy+6}"/>'
                f'<line class="scale" x1="{sx+metres}" y1="{sy-6}" x2="{sx+metres}" y2="{sy+6}"/><text class="lbl-muted" x="{sx+metres/2:.0f}" y="{sy-10}" text-anchor="middle">{metres} m</text>')

    def north(self, corner="se"):
        nx = self.X1 - 40 if corner[1] == "e" else self.X0 + 40
        ny = -self.Y0 - 70 if corner[0] == "s" else -self.Y1 + 60
        return (f'<g transform="rotate({-self.frame.rot} {nx} {ny})"><path class="arrow" d="M{nx},{ny-26} L{nx-9},{ny+6} L{nx},{ny-2} L{nx+9},{ny+6} Z"/>'
                f'<text x="{nx}" y="{ny+24}" text-anchor="middle" class="lbl-muted">N</text></g>')

    def render(self, defs, body, under=()):
        W, H = self.X1 - self.X0, self.Y1 - self.Y0
        r = self.roads
        return (f'<svg class="{self.cls}" xmlns="http://www.w3.org/2000/svg" viewBox="{self.X0} {-self.Y1} {W} {H}" role="img" aria-labelledby="{self.cls}-title {self.cls}-desc">\n'
                f'<title id="{self.cls}-title">{self.title}</title>\n<desc id="{self.cls}-desc">{self.desc}</desc>\n'
                f'<style>{STYLE.format(cls=self.cls)}</style>\n<defs>{defs}</defs>\n'
                f'<rect class="paper" x="{self.X0}" y="{-self.Y1}" width="{W}" height="{H}" rx="6"/>\n'
                f'<path class="green" fill-rule="evenodd" d="{" ".join(self.green)}"/>\n<path class="water" d="{" ".join(self.water)}"/>\n' + "\n".join(under) + "\n"
                f'<g class="roads"><path class="rd rd-path" d="{" ".join(r["path"])}"/><path class="rd rd-minor" d="{" ".join(r["minor"])}"/>'
                f'<path class="rd rd-major" d="{" ".join(r["major"])}"/><path class="rd rd-mw" d="{" ".join(r["mw"])}"/></g>\n'
                f'<path class="rail" d="{" ".join(self.rail)}"/>\n<path class="bld" fill-rule="evenodd" d="{" ".join(self.bld)}"/>\n'
                + "\n".join(body) + "\n</svg>\n")


# --------------------------------------------------------------------- DTU
def build_dtu():
    tiles = ["12.511,55.7785,12.5215,55.7845", "12.5215,55.7785,12.532,55.7845",
             "12.511,55.7845,12.5215,55.7905", "12.5215,55.7845,12.532,55.7905"]
    frame = Frame(55.785, 12.52)
    ways, nodes = fetch(tiles)
    cv = Canvas("dirmap", frame, (-270, 700, -620, 330), ways,
                {"Anker Engelunds Vej", "Akademivej", "Lundtoftegårdsvej", "Helsingørmotorvejen"},
                "Map of DTU Lyngby Campus with the light rail and the walk to Building 321",
                "The light rail enters campus from the south along Lundtoftegårdsvej, runs west along Akademivej, north up Koppels Allé and east along Anker Engelunds Vej before leaving towards Rævehøjvej and Lundtofte. From the Akademivej stop it is about 450 metres north on foot to Building 321.")
    cv.rail = []  # no heavy rail in frame worth showing
    b321 = next((P([frame.xy(*p) for p in ll]) + "Z" for t, _, ll in ways if t.get("building") and t.get("ref") == "321"), None)
    if not cv.tram or b321 is None:
        sys.exit("OSM data is missing the light rail or Building 321; refusing to write a broken map")
    tram_path = " ".join(P(seg) for seg in cv.tram if len(seg) > 1)
    inside = [p for seg in cv.tram for p in seg if cv.X0 < p[0] < cv.X1 and cv.Y0 < p[1] < cv.Y1]
    t_south, t_north = min(inside, key=lambda p: p[1]), max(inside, key=lambda p: p[1])

    def tram_x_at(y):
        for seg in cv.tram:
            for a, b in zip(seg, seg[1:]):
                lo, hi = sorted((a, b), key=lambda p: p[1])
                if lo[1] <= y <= hi[1] and -130 < lo[0] < 70 and -130 < hi[0] < 70 and hi[1] - lo[1] > 50:
                    return lo[0] + (hi[0] - lo[0]) * (y - lo[1]) / (hi[1] - lo[1])
        sys.exit(f"could not place the walking route at y={y}")

    ak, aev, rv = frame.xy(55.78022, 12.51948), frame.xy(55.78554, 12.52263), frame.xy(55.78719, 12.52829)
    bus = [frame.xy(55.78715, 12.52708), frame.xy(55.78758, 12.52983)]
    walk = [ak, (ak[0] - 20, ak[1] + 14), (-105, -508)] + [(tram_x_at(y) - 15, y) for y in (-470, -400, -300, -200, -140)] + [(-22, -140)]
    print(f"  walk {length(walk):.0f} m", file=sys.stderr)
    defs, body = "", [f'<path class="b321" d="{b321}"/>', f'<path class="tram" d="{tram_path}"/>', f'<path class="tram-core" d="{tram_path}"/>',
                      f'<path class="walk" d="{P(rdp(walk, 1.0))}"/>']
    for name, pid, off, dy in [("Anker Engelunds Vej", "lp-aev", "62%", -9), ("Akademivej", "lp-ak", "30%", -9),
                               ("Lundtoftegårdsvej", "lp-lg", "55%", -9), ("Helsingørmotorvejen", "lp-mw", "72%", -10)]:
        d, t = cv.road_label(name, pid, off, dy)
        defs += d
        body.append(t)
    body += [f'<circle class="stop stop-here" cx="{ak[0]:.0f}" cy="{-ak[1]:.0f}" r="9"/>',
             f'<circle class="stop" cx="{aev[0]:.0f}" cy="{-aev[1]:.0f}" r="9"/>',
             f'<circle class="stop" cx="{rv[0]:.0f}" cy="{-rv[1]:.0f}" r="9"/>']
    body += [f'<rect class="bus" x="{b[0]-6:.0f}" y="{-b[1]-6:.0f}" width="12" height="12" rx="2"/>' for b in bus]
    body += [f'<text class="lbl-stop halo" x="{ak[0]+16:.0f}" y="{-ak[1]+28:.0f}">Akademivej (DTU) <tspan class="sub">get off here</tspan></text>',
             f'<text class="lbl-stop halo" x="{aev[0]-16:.0f}" y="{-aev[1]-18:.0f}" text-anchor="end">Anker Engelunds Vej (DTU)</text>',
             f'<text class="lbl-stop halo" x="{rv[0]-16:.0f}" y="{-rv[1]-16:.0f}" text-anchor="end">Rævehøjvej</text>',
             f'<text class="lbl-muted halo" x="{bus[1][0]:.0f}" y="{-bus[1][1]+24:.0f}" text-anchor="middle">bus 150S</text>',
             '<text class="lbl-here halo" x="-78" y="136" text-anchor="end">Building 321</text>',
             '<text class="lbl-muted halo" x="-78" y="156" text-anchor="end">my office, 2nd floor</text>',
             f'<text class="lbl-muted halo" x="{t_south[0]+16:.0f}" y="{-t_south[1]-4:.0f}">to Lyngby St. ↓</text>',
             f'<text class="lbl-muted halo" x="{t_north[0]-16:.0f}" y="{-t_north[1]+22:.0f}" text-anchor="end">↑ to Lundtofte</text>',
             cv.scale_bar(200), cv.north()]
    return cv.render(defs, body)


# ---------------------------------------------------------------------- KU
def build_ku():
    tiles = ["12.565,55.682,12.573,55.6875", "12.573,55.682,12.581,55.6875",
             "12.565,55.6875,12.573,55.692", "12.573,55.6875,12.581,55.692"]
    # rotated 45 degrees clockwise so Øster Farimagsgade runs left to right and CSS faces down, as on KU's own map
    frame = Frame(55.686, 12.571, rot_deg=-45)
    ways, nodes = fetch(tiles)
    cv = Canvas("kumap", frame, (-270, 250, -300, 250), ways,
                {"Øster Farimagsgade", "Nørre Farimagsgade", "Gothersgade", "Frederiksborggade", "Nørre Voldgade", "Øster Voldgade"},
                "Map of the walk from Nørreport to CSS, the old Kommunehospitalet, on Øster Farimagsgade",
                "From Nørreport station, walk up Gothersgade along the Botanical Garden fence to Øster Farimagsgade. CSS is the red-brick hospital complex straight ahead across the crossing, opposite the Botanical Garden. Turn right along Øster Farimagsgade, enter the front garden at number 5 and go in through the left gate of Building 1, under the dome; the office is one building to the left, Building 7.")
    norreport = frame.xy(55.68385, 12.57276)   # the S-train platforms under Nørre Voldgade; the metro is next door
    gate = frame.xy(55.68693, 12.57100)        # the main gate, Øster Farimagsgade 5, straight out from the dome
    dome = frame.xy(55.68722, 12.57052)        # Building 1, under the dome
    door = dome                                # the left gate of Building 1 is just left of the dome: same spot at this scale
    corner = frame.xy(55.68458, 12.57355)      # OSM node 3627218951: Gothersgade meets Øster Voldgade, the Gothersgade end of the station
    goth = frame.xy(55.68570, 12.56926)        # OSM node 9865771105: Gothersgade meets Øster Farimagsgade (don't eyeball this one: 2026-10-20 it sat 55 m off, and the walk cut through the garden)
    # The KU walk is drawn by hand, not with Dijkstra. Gothersgade is dead straight, and OSM's footway graph
    # is no help here: it would send the walk down a service road 40 m off the street, and past Gothersgade
    # the pavement is disconnected, so the search tours the Botanical Garden. (Until 2026-10-20 a waypoint
    # sent the walk west along Frederiksborggade and back up Nørre Farimagsgade: 140 m longer, for no reason.)
    ux, uy = goth[0] - corner[0], goth[1] - corner[1]
    n = math.hypot(ux, uy)
    px, py = uy / n * 9, -ux / n * 9                  # 9 m to the Botanical Garden side: the pavement along the fence
    assert px > 0, "pavement offset should point towards the garden (+x)"
    kerb = goth[1] + 10                               # Øster Farimagsgade's CSS-side pavement at the crossing
    walk = [norreport, (corner[0] + px, norreport[1]), (corner[0] + px, corner[1] + py), (goth[0] + px, goth[1] + py - 8), (goth[0] + px, kerb),
            (gate[0], gate[1] - 4), gate, (gate[0] + 1, dome[1] - 10), door]
    print(f"  walk {length(walk):.0f} m; nørreport {norreport[0]:.0f},{norreport[1]:.0f} door {door[0]:.0f},{door[1]:.0f} dome {dome[0]:.0f},{dome[1]:.0f}", file=sys.stderr)
    css = next((P(rdp([frame.xy(*p) for p in ll], 1.0)) + "Z" for t, _, ll in ways
                if t.get("amenity") == "university" and "Sundhed og Samfund" in t.get("name", "")), None)
    under = [f'<path class="area-hi" d="{css}"/>'] if css else []

    def along(name, a, b, side=14, frac=0.5):
        """Street name set along the walk between local points a and b, offset to one side."""
        ang = math.degrees(math.atan2(-(b[1] - a[1]), b[0] - a[0]))  # SVG angle (y down)
        mx, my = a[0] + (b[0] - a[0]) * frac, -(a[1] + (b[1] - a[1]) * frac)
        if ang > 90 or ang < -90:
            ang += 180
        nx, ny = -math.sin(math.radians(ang)) * side, math.cos(math.radians(ang)) * side  # perpendicular, in SVG coords
        return f'<text class="lbl-road" x="{mx - nx:.0f}" y="{my - ny:.0f}" text-anchor="middle" transform="rotate({ang:.1f} {mx - nx:.0f} {my - ny:.0f})">{name}</text>'

    # the walk's long straight leg carries the street name that textPath would put off-canvas
    defs, body = "", [f'<path class="walk" d="{P(rdp(walk, 1.0))}"/>',
                      along("Gothersgade", corner, goth, -16, 0.5)]
    for name, pid, off, dy in [("Øster Farimagsgade", "kp-of", "42%", -9), ("Nørre Voldgade", "kp-nv", "14%", 20)]:
        d, t = cv.road_label(name, pid, off, dy)
        defs += d
        body.append(t)
    gx, gy = frame.xy(55.6868, 12.5735)   # Botanical Garden label
    body += [f'<circle class="stn" cx="{norreport[0]:.0f}" cy="{-norreport[1]:.0f}" r="9"/>',
             f'<text class="lbl-stop halo" x="{norreport[0]-16:.0f}" y="{-norreport[1]+7:.0f}" text-anchor="end">Nørreport</text>',
             f'<text class="lbl-stop halo" x="{norreport[0]+16:.0f}" y="{-norreport[1]+22:.0f}"><tspan class="sub">S-train and metro</tspan></text>',
             f'<circle class="pin" cx="{door[0]:.0f}" cy="{-door[1]:.0f}" r="8"/>',
             f'<text class="lbl-here halo" x="{door[0]-18:.0f}" y="{-door[1]-16:.0f}" text-anchor="end">Enter here</text>',
             f'<text class="lbl-muted halo" x="{door[0]-18:.0f}" y="{-door[1]+4:.0f}" text-anchor="end">Left gate of Building 1, then up to 7.2.48</text>',
             f'<text class="lbl-muted halo" x="{cv.X1-10}" y="{-dome[1]-56:.0f}" text-anchor="end">the dome: Building 1, SODAS</text>',
             f'<text class="lbl-area halo" x="{gx:.0f}" y="{-gy:.0f}" text-anchor="middle">Botanical Garden</text>',
             f'<text class="lbl-area halo" x="{dome[0]-130:.0f}" y="{-dome[1]-100:.0f}" text-anchor="middle">CSS (Kommunehospitalet)</text>',
             cv.scale_bar(100, "se"), cv.north("nw")]
    return cv.render(defs, body, under)
    return cv.render(defs, body)


MAPS = {"dtu": (build_dtu, "dirmap"), "ku": (build_ku, "kumap")}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    which = args or list(MAPS)
    text = PAGE.read_text()
    for key in which:
        build, marker = MAPS[key]
        print(f"{key}:", file=sys.stderr)
        svg = build()
        print(f"  svg {len(svg.encode()) / 1024:.0f} KB", file=sys.stderr)
        if "--stdout" in sys.argv:
            sys.stdout.write(svg)
            continue
        text, n = re.subn(rf"(<!-- {marker}:start -->\n).*?(<!-- {marker}:end -->)", lambda m: m.group(1) + svg + m.group(2), text, flags=re.S)
        if n != 1:
            sys.exit(f"expected one {marker} marker pair in {PAGE}, found {n}")
    if "--stdout" not in sys.argv:
        PAGE.write_text(text)
        print(f"wrote {PAGE}", file=sys.stderr)


if __name__ == "__main__":
    main()
