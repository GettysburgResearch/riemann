#!/usr/bin/env python3
"""SKEPTIC: NON-RIGOROUS search for the LOWEST zeros of Z_{x^2+5y^2} with Re s > 1 (t <= TMAX):
numpy screen of |1+R| (truncated Euler product, primes < P) on sigma in 1.001..1.15, local minima below 0.15
-> Newton on the FULL Z (genus formula, flint) -> report zeros with Re > 1.  Usage: sk_ep_low.py TMAX P"""
import sys, numpy as np, flint
from flint import acb
from sympy import primerange
from sk_ep_probe import Z
flint.ctx.prec = 64
TMAX, P = float(sys.argv[1]), int(sys.argv[2])
ps = np.array([p for p in primerange(3, P) if p % 20 in (3, 7)], float)
t = np.arange(1.0, TMAX, 0.01)
cands = set()
for sg in np.arange(1.001, 1.15, 0.006):
    s = sg + 1j * t
    x = np.exp(-s * np.log(2.0)); logR = np.log((1 - x) / (1 + x))
    for p in ps:
        x = np.exp(-s * np.log(p)); logR += 2 * np.log((1 - x) / (1 + x))
    v = np.abs(1 + np.exp(logR))
    loc = np.nonzero((v[1:-1] < 0.15) & (v[1:-1] <= v[:-2]) & (v[1:-1] <= v[2:]))[0] + 1
    for i in loc:
        cands.add((round(float(t[i]), 1), round(float(sg), 3)))
print('n candidates', len(cands), flush=True)
found = []
for tc, sg in sorted(cands):
    z = complex(sg, tc)
    ok = False
    for _ in range(40):
        h = 1e-8
        f0 = complex(Z(acb(z.real, z.imag))); f1 = complex(Z(acb(z.real + h, z.imag)))
        st = f0 / ((f1 - f0) / h); z -= st
        if abs(st) < 1e-12: ok = True; break
        if abs(z.imag - tc) > 3: break
    if ok and z.real > 1 and all(abs(z - w) > 1e-6 for w in found):
        found.append(z); print('zero Re>1', z, flush=True)
print('done', sorted(found, key=lambda w: w.imag))
