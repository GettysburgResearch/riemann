#!/usr/bin/env python3
"""SKEPTIC: NON-RIGOROUS screen for zeros of Z_{x^2+5y^2} with Re s > 1 below t = TMAX, using the truncated
Euler product R(s) = ((1-2^-s)/(1+2^-s)) prod_{p=3,7 mod 20, p<P} ((1-p^-s)/(1+p^-s))^2 (Z = zeta_K (1+R)),
on several sigma; prints the smallest local minima of |1+R| per sigma (candidates for Newton on full Z)."""
import sys, numpy as np, time
from sympy import primerange
TMAX = float(sys.argv[1]); P = int(sys.argv[2])
ps = np.array([p for p in primerange(3, P) if p % 20 in (3, 7)], float)
lp = np.log(ps)
t0 = time.time()
for sg in [1.003, 1.008, 1.015, 1.025]:
    cands = []
    for T0 in np.arange(0, TMAX, 2e4):
        t = np.arange(T0, min(T0 + 2e4, TMAX), 0.02)
        s = sg + 1j * t
        x = np.exp(-s * np.log(2.0)); logR = np.log((1 - x) / (1 + x))
        for p, l in zip(ps, lp):
            x = np.exp(-s * l)
            logR += 2 * np.log((1 - x) / (1 + x))
        v = np.abs(1 + np.exp(logR))
        loc = np.nonzero((v[1:-1] < 0.06) & (v[1:-1] <= v[:-2]) & (v[1:-1] <= v[2:]))[0] + 1
        cands += [(float(v[i]), float(t[i])) for i in loc]
    cands.sort()
    print(sg, len(cands), [(round(a, 4), round(b, 2)) for a, b in cands[:12]], round(time.time() - t0, 1), flush=True)
