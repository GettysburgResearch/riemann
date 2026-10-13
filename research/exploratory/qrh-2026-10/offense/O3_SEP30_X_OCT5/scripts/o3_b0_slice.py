#!/usr/bin/env python3
"""Repair R4 check: optimise the imported threshold_calculus model on the slice b = 0 (lx = ly), where
Prop. 15.2's P_a^{1/6} term is absent (P_a <= 1, additive sieve Lemma 6.2 gives Q/Y').  Floating point, finite."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts'))
import threshold_calculus as TC
from scipy.optimize import minimize
def obj(p):
    lx, ell = p; ly = lx
    if not TC.valid_geometry(lx, ly, ell): return 2.0
    s0 = TC.low_threshold(lx, ly, ell, nd=41)
    if s0 >= 11/12: return 1.5 + s0
    hs = TC.high_sup(lx, ly, ell, s0, 11/12, nde=41, nx=6, nd=5)[0]
    return s0 + 200*max(0.0, hs + 2e-5)
best = None
for st in [(0.5, 0.0), (0.45, 0.1), (17/48, 1/6), (0.4, 0.2)]:
    r = minimize(obj, st, method='Nelder-Mead', options=dict(xatol=1e-6, fatol=1e-8, maxiter=1500))
    if best is None or r.fun < best.fun: best = r
lx, ell = best.x
s0, hs = TC.closes(lx, lx, ell, 11/12, fine=True)
out = dict(sigma0=s0, lx=lx, ly=lx, ell=ell, high_sup=hs[0], arg=str(hs[1]))
print(out)
json.dump(out, open(os.path.join(os.path.dirname(__file__), '..', 'results', 'o3_b0_slice.json'), 'w'), indent=1)
