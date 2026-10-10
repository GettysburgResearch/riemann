#!/usr/bin/env python3
"""Generate figures/barrier_ladder.svg: where the quasi-RH methods stand (boundary sigma0)."""
from fractions import Fraction as F
import os
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
items = [  # (value, label, sublabel, category)
    (1.0, "1", "trivial: Euler product, Re s > 1", "res"),
    (float(F(47, 48)), "47/48", "Kintali, short proof (claimed)", "res"),
    (float(F(11, 12)), "11/12", "OpenAI Part I / Oct 5 mean square (claimed)", "res"),
    (0.875, "7/8", "OpenAI Part II (claimed); PR 910: 7/8 − 1/160000 conditional", "res"),
    (0.874957, "≈ 0.87496", "optimum of the 7/8 paper's own lemmas (PR 910 exact; model agrees)", "bar"),
    (float(F(167, 192)), "167/192", "zero-free rows at detector floor 51/100: any zero counting", "bar"),
    (float(F(13, 15)), "13/15", "pointwise barrier: perfect counts + energy + row-by-row GLH", "bar"),
    (float(F(5, 6)), "5/6", "cubic-theta probe floor under Cauchy–Schwarz", "bar"),
    (float(F(17, 24)), "17/24", "Oct 5 route + 4th moment of sextic Möbius family (PR 910); GL(3) shape", "route"),
    (float(F(2, 3)), "2/3", "any theta-type probe (heuristic parity rule)", "bar"),
    (float(F(23, 36)), "23/36", "Oct 5 route + 6th moment", "route"),
    (0.5, "1/2", "RH  ←  all 2k-th moments: 1/2 + 5/(12k)", "route"),
]
W, H = 980, 780
top, bot = 150, 720
x_axis = 150
def y_of(v): return top + (1.0 - v)/(0.5)*(bot - top)
color = {"res": BLUE, "bar": ORANGE, "route": AQUA}
def marker(cat, x, y):
    c = color[cat]
    if cat == "res":
        return f'<circle cx="{x}" cy="{y:.1f}" r="5.5" fill="{c}" stroke="{SURF}" stroke-width="2"/>'
    if cat == "bar":
        return (f'<rect x="{x-5.5}" y="{y-5.5:.1f}" width="11" height="11" fill="{c}" stroke="{SURF}" '
                f'stroke-width="2" transform="rotate(45 {x} {y:.1f})"/>')
    return f'<rect x="{x-5}" y="{y-5:.1f}" width="10" height="10" rx="2" fill="{c}" stroke="{SURF}" stroke-width="2"/>'
# label placement: greedy top-down with min spacing
labels = []
prev = -1e9
for v, a, b, c in items:
    ty = y_of(v)
    ly = max(ty, prev + 34)
    labels.append((v, a, b, c, ty, ly)); prev = ly
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H + 20}" viewBox="0 0 {W} {H + 20}" '
       f'font-family="Inter, Helvetica, Arial, sans-serif" role="img" aria-labelledby="t d">',
       f'<title id="t">Where the quasi-RH methods stand</title>',
       f'<desc id="d">Boundaries sigma0 for zero-free half-planes Re s &gt; sigma0, from trivial (1) to RH (1/2): '
       f'claimed results, barriers found in the October 2026 wave, and conditional routes.</desc>',
       f'<rect width="100%" height="100%" fill="{SURF}"/>',
       f'<text x="40" y="44" font-size="22" font-weight="600" fill="{INK}">Where the quasi-RH methods stand</text>',
       f'<text x="40" y="70" font-size="14" fill="{INK2}">Boundary σ₀ of a zero-free half-plane Re s &gt; σ₀ (lower is better; RH is σ₀ = 1/2). '
       f'External claims are unreviewed.</text>']
# legend
for (cat, name), (lx, ly) in zip([("res", "claimed / imported result"),
                  ("bar", "barrier for a stated architecture (this wave unless noted)"),
                  ("route", "conditional route (needs an unproved moment)")], [(40, 96), (300, 96), (40, 118)]):
    out.append(marker(cat, lx + 6, ly))
    out.append(f'<text x="{lx + 18}" y="{ly + 5}" font-size="13" fill="{INK2}">{name}</text>')
# axis
out.append(f'<line x1="{x_axis}" y1="{top}" x2="{x_axis}" y2="{bot}" stroke="{INK2}" stroke-width="1"/>')
for t in [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]:
    y = y_of(t)
    out.append(f'<line x1="{x_axis - 6}" y1="{y:.1f}" x2="{x_axis}" y2="{y:.1f}" stroke="{INK2}" stroke-width="1"/>')
    out.append(f'<text x="{x_axis - 12}" y="{y + 4:.1f}" font-size="12" text-anchor="end" fill="{INK2}">{t:.1f}</text>')
out.append(f'<text x="{x_axis - 60}" y="{(top+bot)/2:.0f}" font-size="13" fill="{INK2}" '
           f'transform="rotate(-90 {x_axis - 60} {(top+bot)/2:.0f})" text-anchor="middle">σ₀</text>')
# critical-line band label
out.append(f'<line x1="{x_axis}" y1="{y_of(0.5):.1f}" x2="{W - 40}" y2="{y_of(0.5):.1f}" stroke="{GRID}" stroke-width="1" stroke-dasharray="3 4"/>')
lab_x = 330
offs = {"≈ 0.87496": 16, "167/192": 32, "13/15": 48}
for v, a, b, c, ty, ly in labels:
    mx = x_axis + offs.get(a, 0)
    if mx != x_axis:
        out.append(f'<line x1="{x_axis}" y1="{ty:.1f}" x2="{mx}" y2="{ty:.1f}" stroke="{GRID}" stroke-width="1"/>')
    out.append(f'<path d="M{mx + 8} {ty:.1f} L{lab_x - 120} {ty:.1f} L{lab_x - 100} {ly:.1f} L{lab_x - 8} {ly:.1f}" '
               f'fill="none" stroke="{GRID}" stroke-width="1.5"/>')
    out.append(marker(c, mx, ty))
    out.append(f'<text x="{lab_x - 92}" y="{ly + 5:.1f}" font-size="14" font-weight="600" fill="{INK}">{a}</text>')
    out.append(f'<text x="{lab_x}" y="{ly + 5:.1f}" font-size="13" fill="{INK2}">{b}</text>')
out.append('</svg>')
path = os.path.join(os.path.dirname(__file__), '..', 'figures', 'barrier_ladder.svg')
open(path, 'w').write("\n".join(out))
print("wrote", os.path.abspath(path))
