# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Regenerate the inline campus map on /directions.

Pulls the DTU Lyngby campus (buildings, roads, the light rail) from the
OpenStreetMap API, draws it as a theme-aware inline SVG (all colours are the
site's CSS custom properties, so dark mode is free), and splices the result
into src/content/pages/20140910_directions.md between the
<!-- dirmap:start --> and <!-- dirmap:end --> markers.

    uv run branding/build-directions-map.py            # rewrite the page
    uv run branding/build-directions-map.py --stdout   # print the SVG instead

Stop coordinates are hard-coded from OSM (stop_position nodes of
Hovedstadens Letbane) because the map API tiles don't carry the route
relation; update them if the stops ever move, which they won't.
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
TILES = [  # four tiles keep each call under the OSM API's node limit
    "12.511,55.7785,12.5215,55.7845", "12.5215,55.7785,12.532,55.7845",
    "12.511,55.7845,12.5215,55.7905", "12.5215,55.7845,12.532,55.7905",
]
# local metres: x east, y north, origin at 55.785N 12.52E
LAT0, LON0 = 55.785, 12.52
KX, KY = math.cos(math.radians(LAT0)) * 111320, 111320
X0, X1, Y0, Y1 = -270, 700, -620, 330  # map extent in metres

STOPS = {  # light rail stop positions (OSM stop_position nodes)
    "Akademivej": (55.78022, 12.51948),
    "Anker Engelunds Vej": (55.78554, 12.52263),
    "Rævehøjvej": (55.78719, 12.52829),
}
BUS_150S = [(55.78715, 12.52708), (55.78758, 12.52983)]  # "Rævehøjvej, DTU" platforms on the motorway
B321 = (-22, -140)  # east end of Building 321, where the walk ends
MAJOR = {"primary", "secondary", "tertiary", "primary_link", "secondary_link", "tertiary_link"}
MINOR = {"residential", "unclassified", "service", "living_street", "pedestrian"}
PATH = {"footway", "path", "cycleway", "steps", "track", "corridor"}
MOTORWAY = {"motorway", "motorway_link", "trunk", "trunk_link"}


def xy(lat, lon):
    return ((lon - LON0) * KX, (lat - LAT0) * KY)


def S(p):
    return f"{p[0]:.0f},{-p[1]:.0f}"  # SVG y points down


def P(pts):
    return " ".join(("M" if i == 0 else "L") + S(p) for i, p in enumerate(pts))


def rdp(pts, eps):
    """Douglas-Peucker simplification."""
    if len(pts) < 3:
        return pts
    a, b = pts[0], pts[-1]
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


def clip(pts, pad=40):
    return [p for p in pts if X0 - pad < p[0] < X1 + pad and Y0 - pad < p[1] < Y1 + pad]


def length(pts):
    return sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))


def fetch_ways():
    nodes, ways = {}, {}
    for bbox in TILES:
        url = f"https://api.openstreetmap.org/api/0.6/map?bbox={bbox}"
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180) as r:
            root = ET.fromstring(r.read())
        for n in root.iter("node"):
            nodes[n.get("id")] = (float(n.get("lat")), float(n.get("lon")))
        for w in root.iter("way"):
            ways[w.get("id")] = (
                {t.get("k"): t.get("v") for t in w.findall("tag")},
                [nd.get("ref") for nd in w.findall("nd")],
            )
        print(f"fetched {bbox}: {len(nodes)} nodes, {len(ways)} ways", file=sys.stderr)
    out = []
    for tags, refs in ways.values():
        pts = [xy(*nodes[r]) for r in refs if r in nodes]
        if len(pts) >= 2:
            out.append((tags, pts))
    return out


def build_svg(ways):
    bld, tram, named, b321 = [], [], {}, None
    roads = {"major": [], "minor": [], "path": [], "mw": []}
    for t, pts in ways:
        if not clip(pts, 60):
            continue
        if t.get("building"):
            bld.append(P(rdp(pts, 0.8)) + "Z")
            if t.get("ref") == "321":
                b321 = P(pts) + "Z"
            continue
        if t.get("railway") == "light_rail" and t.get("name") == "Hovedstadens Letbane":
            tram.append(rdp(clip(pts, 120), 1.0))
            continue
        h = t.get("highway")
        if not h:
            continue
        cp = clip(pts)
        if len(cp) < 2:
            continue
        pth = P(rdp(cp, 1.5))
        if h in MOTORWAY:
            roads["mw"].append(pth)
        elif h in MAJOR:
            roads["major"].append(pth)
        elif h in MINOR:
            roads["minor"].append(pth)
        elif h in PATH and length(cp) >= 20:
            roads["path"].append(pth)
        n = t.get("name")
        if n in ("Anker Engelunds Vej", "Akademivej", "Lundtoftegårdsvej", "Helsingørmotorvejen") \
                and h not in PATH and length(pts) > named.get(n, (0,))[0]:
            named[n] = (length(pts), pts)
    if not tram or b321 is None:
        sys.exit("OSM data is missing the light rail or Building 321; refusing to write a broken map")

    tram_path = " ".join(P(seg) for seg in tram if len(seg) > 1)
    inside = [p for seg in tram for p in seg if X0 < p[0] < X1 and Y0 < p[1] < Y1]
    t_south, t_north = min(inside, key=lambda p: p[1]), max(inside, key=lambda p: p[1])

    def tram_x_at(y):
        """x of the Koppels Allé stretch of the tracks at a given y."""
        for seg in tram:
            for a, b in zip(seg, seg[1:]):
                lo, hi = sorted((a, b), key=lambda p: p[1])
                if lo[1] <= y <= hi[1] and -130 < lo[0] < 70 and -130 < hi[0] < 70 and hi[1] - lo[1] > 50:
                    return lo[0] + (hi[0] - lo[0]) * (y - lo[1]) / (hi[1] - lo[1])
        sys.exit(f"could not place the walking route at y={y}")

    # the walk: west along Akademivej to the bend, north up the west side of the tracks, then west to 321
    ak = xy(*STOPS["Akademivej"])
    walk = [ak, (ak[0] - 20, ak[1] + 14), (-105, -508)] + \
           [(tram_x_at(y) - 15, y) for y in (-470, -400, -300, -200, -140)] + [B321]
    walk_path = P(rdp(walk, 1.0))
    print(f"walk length {length(walk):.0f} m", file=sys.stderr)

    def road_label_path(name, pid):
        _, pts = named[name]
        if pts[0][0] > pts[-1][0]:
            pts = pts[::-1]  # left to right, so the text reads upright
        return f'<path id="{pid}" d="{P(rdp(pts, 1.0))}" fill="none"/>'

    road_labels = [(n, pid, off, dy) for n, pid, off, dy in [
        ("Anker Engelunds Vej", "lp-aev", "62%", -9), ("Akademivej", "lp-ak", "30%", -9),
        ("Lundtoftegårdsvej", "lp-lg", "55%", -9), ("Helsingørmotorvejen", "lp-mw", "72%", -10),
    ] if n in named]
    defs = "".join(road_label_path(n, pid) for n, pid, _, _ in road_labels)
    W, H = X1 - X0, Y1 - Y0
    aev, rv = xy(*STOPS["Anker Engelunds Vej"]), xy(*STOPS["Rævehøjvej"])
    bus = [xy(*b) for b in BUS_150S]

    o = [f'''<svg class="dirmap" xmlns="http://www.w3.org/2000/svg" viewBox="{X0} {-Y1} {W} {H}" role="img" aria-labelledby="dirmap-title dirmap-desc">
<title id="dirmap-title">Map of DTU Lyngby Campus with the light rail and the walk to Building 321</title>
<desc id="dirmap-desc">The light rail enters campus from the south along Lundtoftegårdsvej, runs west along Akademivej, north up Koppels Allé and east along Anker Engelunds Vej before leaving towards Rævehøjvej and Lundtofte. From the Akademivej stop it is about 450 metres north on foot to Building 321.</desc>
<style>
.dirmap{{width:100%;height:auto;display:block;margin:1.5em 0;font-family:Inter,system-ui,sans-serif}}
.dirmap .paper{{fill:var(--surface-card,#f1f0ea)}}
.dirmap .bld{{fill:var(--bg,#fbfbf8);stroke:var(--fg-muted,#666);stroke-width:.8;stroke-opacity:.6}}
.dirmap .rd{{fill:none;stroke:var(--fg-muted,#666);stroke-linecap:round;stroke-linejoin:round}}
.dirmap .rd-mw{{stroke-width:7;stroke-opacity:.22}}
.dirmap .rd-major{{stroke-width:4.5;stroke-opacity:.3}}
.dirmap .rd-minor{{stroke-width:2.5;stroke-opacity:.25}}
.dirmap .rd-path{{stroke-width:1;stroke-opacity:.22}}
.dirmap .tram{{fill:none;stroke:var(--accent-olive,#7e8d20);stroke-width:6;stroke-linecap:round;stroke-linejoin:round}}
.dirmap .tram-core{{fill:none;stroke:var(--bg,#fbfbf8);stroke-width:1.5;stroke-dasharray:9 9;stroke-opacity:.9}}
.dirmap .walk{{fill:none;stroke:var(--accent-sienna,#b8451e);stroke-width:6;stroke-dasharray:10 9;stroke-linecap:round;stroke-linejoin:round}}
.dirmap .stop{{fill:var(--bg,#fbfbf8);stroke:var(--accent-olive,#7e8d20);stroke-width:4}}
.dirmap .stop-here{{stroke:var(--accent-sienna,#b8451e)}}
.dirmap .b321{{fill:var(--accent-sienna,#b8451e);stroke:none}}
.dirmap .bus{{fill:var(--accent-oxblood,#992c44)}}
.dirmap text{{fill:var(--fg,#0e0e10);font-size:17px}}
.dirmap .lbl-stop{{font-weight:600;font-size:19px}}
.dirmap .lbl-stop tspan.sub{{font-weight:400;font-size:15px;fill:var(--fg-muted,#666)}}
.dirmap .lbl-road{{font-size:15px;fill:var(--fg-muted,#666);letter-spacing:.06em}}
.dirmap .lbl-here{{font-weight:600;font-size:19px;fill:var(--accent-sienna,#b8451e)}}
.dirmap .lbl-muted{{fill:var(--fg-muted,#666);font-size:15px}}
.dirmap .halo{{stroke:var(--surface-card,#f1f0ea);stroke-width:5;stroke-linejoin:round;paint-order:stroke}}
.dirmap .scale{{stroke:var(--fg,#0e0e10);stroke-width:2}}
.dirmap .arrow{{fill:var(--fg,#0e0e10)}}
@media (max-width:600px){{
  .dirmap text{{font-size:24px}} .dirmap .lbl-stop{{font-size:26px}} .dirmap .lbl-stop tspan.sub{{font-size:20px}}
  .dirmap .lbl-road{{font-size:21px}} .dirmap .lbl-here{{font-size:26px}} .dirmap .lbl-muted{{font-size:21px}}
}}
</style>
<defs>{defs}</defs>
<rect class="paper" x="{X0}" y="{-Y1}" width="{W}" height="{H}" rx="6"/>
<g class="roads">
<path class="rd rd-path" d="{" ".join(roads['path'])}"/>
<path class="rd rd-minor" d="{" ".join(roads['minor'])}"/>
<path class="rd rd-major" d="{" ".join(roads['major'])}"/>
<path class="rd rd-mw" d="{" ".join(roads['mw'])}"/>
</g>
<path class="bld" d="{" ".join(bld)}"/>
<path class="b321" d="{b321}"/>
<path class="tram" d="{tram_path}"/>
<path class="tram-core" d="{tram_path}"/>
<path class="walk" d="{walk_path}"/>
''']
    o.append(f'<circle class="stop stop-here" cx="{ak[0]:.0f}" cy="{-ak[1]:.0f}" r="9"/>')
    o.append(f'<circle class="stop" cx="{aev[0]:.0f}" cy="{-aev[1]:.0f}" r="9"/>')
    o.append(f'<circle class="stop" cx="{rv[0]:.0f}" cy="{-rv[1]:.0f}" r="9"/>')
    for b in bus:
        o.append(f'<rect class="bus" x="{b[0]-6:.0f}" y="{-b[1]-6:.0f}" width="12" height="12" rx="2"/>')
    o.append(f'<text class="lbl-stop halo" x="{ak[0]+16:.0f}" y="{-ak[1]+28:.0f}">Akademivej (DTU) <tspan class="sub">get off here</tspan></text>')
    o.append(f'<text class="lbl-stop halo" x="{aev[0]-16:.0f}" y="{-aev[1]-18:.0f}" text-anchor="end">Anker Engelunds Vej (DTU)</text>')
    o.append(f'<text class="lbl-stop halo" x="{rv[0]-16:.0f}" y="{-rv[1]-16:.0f}" text-anchor="end">Rævehøjvej</text>')
    o.append(f'<text class="lbl-muted halo" x="{bus[1][0]:.0f}" y="{-bus[1][1]+24:.0f}" text-anchor="middle">bus 150S</text>')
    o.append('<text class="lbl-here halo" x="-78" y="136" text-anchor="end">Building 321</text>')
    o.append('<text class="lbl-muted halo" x="-78" y="156" text-anchor="end">my office, 1st floor</text>')
    for _, pid, off, dy in road_labels:
        name = next(n for n, p, _, _ in road_labels if p == pid)
        o.append(f'<text class="lbl-road" dy="{dy}"><textPath href="#{pid}" startOffset="{off}">{name}</textPath></text>')
    o.append(f'<text class="lbl-muted halo" x="{t_south[0]+16:.0f}" y="{-t_south[1]-4:.0f}">to Lyngby St. ↓</text>')
    o.append(f'<text class="lbl-muted halo" x="{t_north[0]-16:.0f}" y="{-t_north[1]+22:.0f}" text-anchor="end">↑ to Lundtofte</text>')
    sx, sy = X0 + 30, -Y0 - 30
    o.append(f'<line class="scale" x1="{sx}" y1="{sy}" x2="{sx+200}" y2="{sy}"/><line class="scale" x1="{sx}" y1="{sy-6}" x2="{sx}" y2="{sy+6}"/>'
             f'<line class="scale" x1="{sx+200}" y1="{sy-6}" x2="{sx+200}" y2="{sy+6}"/><text class="lbl-muted" x="{sx+100}" y="{sy-10}" text-anchor="middle">200 m</text>')
    nx, ny = X1 - 40, -Y0 - 70
    o.append(f'<path class="arrow" d="M{nx},{ny-26} L{nx-9},{ny+6} L{nx},{ny-2} L{nx+9},{ny+6} Z"/><text x="{nx}" y="{ny+24}" text-anchor="middle" class="lbl-muted">N</text>')
    o.append("</svg>")
    return "\n".join(o) + "\n"


def main():
    svg = build_svg(fetch_ways())
    print(f"svg {len(svg.encode()) / 1024:.0f} KB", file=sys.stderr)
    if "--stdout" in sys.argv:
        sys.stdout.write(svg)
        return
    text = PAGE.read_text()
    new, n = re.subn(r"(<!-- dirmap:start -->\n).*?(<!-- dirmap:end -->)", lambda m: m.group(1) + svg + m.group(2), text, flags=re.S)
    if n != 1:
        sys.exit(f"expected one dirmap marker pair in {PAGE}, found {n}")
    PAGE.write_text(new)
    print(f"wrote {PAGE}", file=sys.stderr)


if __name__ == "__main__":
    main()
