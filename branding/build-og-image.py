# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Regenerate public/og-image.jpg, the 1200x630 card shown when a link to the site is shared.

    uv run branding/build-og-image.py [--seed N]

The card is the site in miniature, in its dark palette: a random geometric network coloured by
BFS shell in the six spectrum colours (same recipe as the homepage hero, without the force
layout), the wordmark in Fraunces, and the colour stripe along the bottom edge.

Drawn as a web page and photographed with headless Chrome, then converted to JPEG with sips
(macOS). Needs network access once, for Fraunces from Google Fonts. Set CHROME to override the
browser path. The colours below are copies of the dark tokens in BaseLayout.astro; if those
change, change them here and re-run.
"""
import argparse, os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "og-image.jpg"
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

HTML = r"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;1,9..144,400&display=block" rel="stylesheet">
<style>
:root{--bg:#0B1838;--text:#F3F1EA;--muted:#A9B0C4;
  --c0:#D85838;--c1:#E47A45;--c2:#EFC044;--c3:#9CB033;--c4:#3FA0A8;--c5:#B7405A}
html,body{margin:0;width:1200px;height:630px;overflow:hidden;background:var(--bg)}
#net{position:absolute;left:0;top:0}
.wm{position:absolute;left:64px;bottom:74px;font-family:Fraunces,serif;font-size:67px;line-height:1;
  font-variation-settings:"opsz" 72;color:var(--text);white-space:nowrap;letter-spacing:-0.01em}
.wm .m{color:var(--muted)} .wm i{color:var(--muted);font-style:italic}
.stripe{position:absolute;left:0;right:0;bottom:0;height:18px;background:linear-gradient(to right,
  var(--c0) 0 16.667%,var(--c1) 0 33.333%,var(--c2) 0 50%,var(--c3) 0 66.667%,var(--c4) 0 83.333%,var(--c5) 0)}
</style></head><body>
<svg id="net"></svg>
<div class="wm">Sune Lehmann<span class="m">:</span><i> Intermittent Updates</i></div>
<div class="stripe"></div>
<script>
const W=1200,H=410,N=120,pad=34;
let s=__SEED__;const rnd=()=>{s=(s*1664525+1013904223)%4294967296;return s/4294967296};
const A=(W-2*pad)*(H-2*pad), r=Math.sqrt(6.2*A/(N*Math.PI)), dmin=r*0.42;
function gen(){
  const P=[];let tries=0;
  while(P.length<N&&tries<20000){tries++;
    const x=pad+rnd()*(W-2*pad),y=pad+rnd()*(H-2*pad);
    if(P.every(p=>Math.hypot(p.x-x,p.y-y)>dmin))P.push({x,y})}
  const E=[];
  for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++)
    if(Math.hypot(P[i].x-P[j].x,P[i].y-P[j].y)<r)E.push([i,j]);
  const adj=P.map(()=>[]);E.forEach(([a,b])=>{adj[a].push(b);adj[b].push(a)});
  // epicentre: the node nearest the left edge's midpoint, so the shells run across the card
  let e=0,bd=1e9;P.forEach((p,i)=>{const d=Math.hypot(p.x-W*0.08,p.y-H*0.5);if(d<bd){bd=d;e=i}});
  const D=P.map(()=>-1);D[e]=0;const Q=[e];
  while(Q.length){const u=Q.shift();for(const w of adj[u])if(D[w]<0){D[w]=D[u]+1;Q.push(w)}}
  return {P,E,D,ok:D.every(d=>d>=0)}}
let g;for(let k=0;k<200;k++){g=gen();if(g.ok)break}   // redraw until the network is one piece
const svg=document.getElementById('net');svg.setAttribute('width',W);svg.setAttribute('height',H);
const col=d=>`var(--c${d%6})`;let h='';
g.E.forEach(([a,b])=>{h+=`<line x1="${g.P[a].x}" y1="${g.P[a].y}" x2="${g.P[b].x}" y2="${g.P[b].y}" stroke="${col(Math.min(g.D[a],g.D[b]))}" stroke-width="2.6" stroke-opacity=".75"/>`});
g.P.forEach((p,i)=>{h+=`<circle cx="${p.x}" cy="${p.y}" r="8.5" fill="${col(g.D[i])}" stroke="var(--bg)" stroke-width="2.5"/>`});
svg.innerHTML=h;
</script></body></html>
"""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--seed", type=int, default=7, help="network seed (default 7, the published card)")
    args = ap.parse_args()
    if not Path(CHROME).exists():
        sys.exit(f"Chrome not found at {CHROME}; set CHROME")
    with tempfile.TemporaryDirectory() as tmp:
        page, png = Path(tmp) / "og.html", Path(tmp) / "og.png"
        page.write_text(HTML.replace("__SEED__", str(args.seed)), encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--window-size=1200,630", "--virtual-time-budget=6000",
                        f"--screenshot={png}", page.as_uri()],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "92",
                        str(png), "--out", str(OUT)], check=True, stdout=subprocess.DEVNULL)
    print(f"wrote {OUT.relative_to(ROOT)} (seed {args.seed})")


if __name__ == "__main__":
    main()
