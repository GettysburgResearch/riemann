#!/usr/bin/env python3
"""Lane 3 independent implementation — frozen 61-smooth aggregate-licensed system.
Written from scratch (not imported from lane_repair). Direct-sum Q (no prefix tables)
for small x; used for: edge cases x in [2,67), jump signs at activations, tiny-x
degeneracies, integer sweep, and the x=1e6 frozen cross-check via prefix tables
validated against the direct sum.
"""
import numpy as np
from math import sqrt, log, fsum, floor

PR = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

def build_lattice():
    divs = [(1,1)]
    for p in PR:
        divs = divs + [(d*p, -mu) for d, mu in divs]
    divs.sort()
    return divs

LAT = build_lattice()
assert len(LAT) == 2**18

def gamma(j, m):
    if m < j: return 0.0
    if m == j: return (j+1)/(j-1)
    if m == j+1: return -((j+1)*(j-2))/(j*(j-1))
    return 2.0/(j*(j-1))

def Q_direct(Y, j):
    if Y < j: return 0.0
    M = int(floor(Y + 1e-12)) if abs(Y - round(Y)) < 1e-9 else int(floor(Y))
    if M > Y + 1e-12: M -= 1
    return fsum(gamma(j, m)/sqrt(m)*log(Y/m) for m in range(j, M+1))

def margins(x, Qfun=Q_direct, js=(2,3), return_fill=False):
    """All four margins at real x >= 2 on the frozen lattice. Greedy prefix fill."""
    act = [(d, mu) for d, mu in LAT if d <= x]
    evens = [d for d, mu in act if mu == 1]   # ascending
    odds  = [d for d, mu in act if mu == -1]
    T = {d: (4*sqrt(x/d) - 3)/sqrt(d) for d, mu in act}
    D = fsum(T[o] for o in odds)
    capE = fsum(T[e] for e in evens)
    TB = capE - D
    # greedy prefix fill (smallest evens first)
    c = {}
    rem = D
    for e in evens:
        take = min(T[e], rem)
        c[e] = take
        rem -= take
    assert rem <= 1e-9*max(1.0, D), f"greedy fill failed at x={x}: rem={rem}"
    out = dict(x=x, TB=TB, D=D, nE=len(evens), nO=len(odds))
    for j in js:
        me = fsum(c[e]*Qfun(x/e, j)/((4*sqrt(x/e)-3)*sqrt(e))*(4*sqrt(x/e)-3) for e in evens if x/e >= j)
        # simplify: c[e]*rho_j(e) with rho = Q/(4 sqrt(Y)-3); but write via theta*Q/sqrt(e):
        me = fsum(c[e]/T[e]*Qfun(x/e, j)/sqrt(e) for e in evens if x/e >= j)
        mo = fsum(Qfun(x/o, j)/sqrt(o) for o in odds if x/o >= j)
        out[f"m{j}"] = me - mo
    # score margin two ways: definition and closed form
    def s(d):
        z = sqrt(x/d)
        return (5*z - 3)/(4*z - 3)
    msc_def = fsum(T[o]*s(o) for o in odds) - fsum(c[e]*s(e) for e in evens)
    msc_cf = 0.75*(fsum(1/sqrt(o) for o in odds) - fsum(c[e]/T[e]/sqrt(e) for e in evens))
    out["m_sc"] = msc_def
    out["m_sc_closed"] = msc_cf
    if return_fill:
        out["theta"] = {e: c[e]/T[e] for e in evens}
    return out

def show(r, tag=""):
    print(f"{tag}x={r['x']:<14.9g} TB={r['TB']:+.9f}  m2={r['m2']:+.9f}  "
          f"m3={r['m3']:+.9f}  m_sc={r['m_sc']:+.9f} (closed {r['m_sc_closed']:+.9f})  "
          f"nE={r['nE']} nO={r['nO']}")

print("== 1. Degenerate endpoints ==")
for x in (2.0, 2.0000001, 2.5, 2.9999999, 3.0, 3.0000001, 3.5, 4.0, 4.9999999, 5.0, 5.5, 5.9999999, 6.0, 6.5):
    show(margins(x))

print("\n== 2. Jump signs at activations (x = d*(1-1e-9), d, for odd and even d) ==")
acts = [d for d, mu in LAT if 6 <= d <= 70]
mus = dict(LAT)
for d0 in acts:
    lo = margins(d0*(1 - 1e-9))
    hi = margins(float(d0))
    kind = "EVEN" if mus[d0] == 1 else "ODD "
    print(f"d={d0:<3d} ({kind}) jumps: dTB={hi['TB']-lo['TB']:+.6f} (pred {mus[d0]/sqrt(d0):+.6f})  "
          f"dm2={hi['m2']-lo['m2']:+.6f}  dm3={hi['m3']-lo['m3']:+.6f}  dm_sc={hi['m_sc']-lo['m_sc']:+.6f}")

print("\n== 3. Fine scan on [2, 67): minima of each margin over real x ==")
best = {k: (1e18, None) for k in ("TB", "m2", "m3", "m_sc")}
cells = [d for d, _ in LAT if d < 67] + [67]
for i in range(len(cells)-1):
    a, b = cells[i], cells[i+1]
    if b <= 2: continue
    a = max(a, 2)
    for t in np.linspace(0, 1, 41):
        xx = a + (b - a)*min(t, 1 - 1e-12)
        if xx < 2: continue
        r = margins(float(xx))
        for k in best:
            if r[k] < best[k][0]: best[k] = (r[k], xx)
print({k: (round(v, 9), round(w, 6)) for k, (v, w) in best.items()})

print("\n== 4. Integer sweep x = 2..2000 (frozen lattice), minima and any negatives ==")
neg = []
best = {k: (1e18, None) for k in ("TB", "m2", "m3", "m_sc")}
for xi in range(2, 2001):
    r = margins(float(xi))
    for k in best:
        if r[k] < best[k][0]: best[k] = (r[k], xi)
        if r[k] < -1e-12: neg.append((xi, k, r[k]))
print("minima:", {k: (round(v, 9), w) for k, (v, w) in best.items()})
print("negatives:", neg[:20] if neg else "NONE")

print("\n== 5. Left-limits at every activation d in [2, 2000] (worst case for margins) ==")
worst = {k: (1e18, None) for k in ("TB", "m2", "m3", "m_sc")}
for d0, mu0 in LAT:
    if d0 < 3 or d0 > 2000: continue
    r = margins(d0*(1 - 1e-9))
    for k in worst:
        if r[k] < worst[k][0]: worst[k] = (r[k], d0)
print("left-limit minima:", {k: (round(v, 9), w) for k, (v, w) in worst.items()})
