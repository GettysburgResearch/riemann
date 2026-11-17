#!/usr/bin/env python3
"""SKEPTIC: NON-RIGOROUS replay of C2-06: min |f| (Davenport-Heilbronn) on sigma = 1 and 1.05 for 1<=t<=TMAX
(grid 0.04), plus Newton from the 10 smallest minima on sigma=1 to see where the nearby zeros are."""
import sys, numpy as np, flint
from flint import acb
import sk_dh
flint.ctx.prec = 53
TMAX = float(sys.argv[1])
t = np.arange(1.0, TMAX, 0.04)
for sg in (1.0,):
    v = np.array([abs(complex(sk_dh.f(acb(sg, x)))) for x in t])
    i = int(np.argmin(v))
    loc = np.nonzero((v[1:-1] <= v[:-2]) & (v[1:-1] <= v[2:]))[0] + 1
    best = sorted([(float(v[j]), float(t[j])) for j in loc])[:8]
    print(sg, 'min', float(v[i]), 'at t', float(t[i]), 'smallest minima', [(round(a, 4), round(b, 2)) for a, b in best], flush=True)
