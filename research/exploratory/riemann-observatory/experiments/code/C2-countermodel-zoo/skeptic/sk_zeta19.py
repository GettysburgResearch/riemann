#!/usr/bin/env python3
"""SKEPTIC replay of C2-22 (zeta_19 zero with Re > 1):
(1) NON-RIGOROUS Newton-step screen on sigma = 1, 0 < t <= TMAX: at grid points (dt = 0.05) compute
    delta = -F/F' and keep points whose Newton estimate 1+it+delta has |delta| < 0.08 and Re > 0.999;
    polish with Newton (complex128) and keep zeros with Re > 1 (catches zeros the |F|<0.03 threshold misses);
(2) RIGOROUS argument-principle certificate (sk_wind.winding, independent of zoo_common.krawczyk) on a
    square with left edge > 1 for each zero found (Arb).
Usage: python3 sk_zeta19.py OUTDIR TMAX"""
import sys, os, json, time
import numpy as np
import flint
from flint import acb, arb
from sk_wind import winding
N = 19
TMAX = float(sys.argv[2])
n = np.arange(1, N + 1); ln = np.log(n)
t0 = time.time()
cands = []
for T0 in np.arange(0, TMAX, 1e5):
    t = np.arange(T0, min(T0 + 1e5, TMAX), 0.05)
    F = np.zeros(t.size, complex); D = np.zeros(t.size, complex)
    for a, l in zip(1.0 / n, ln):
        e = a * np.exp(-1j * t * l)
        F += e; D -= l * e
    delta = -F / D
    sel = np.nonzero((np.abs(delta) < 0.08) & (delta.real > -0.02))[0]
    for i in sel:
        cands.append(complex(1.0, t[i]) + delta[i])
def Fz(z):
    e = np.exp(-z * ln); return e.sum(), -(ln * e).sum()
zeros = []
for z in cands:
    for _ in range(30):
        f, d = Fz(z); st = f / d; z -= st
        if abs(st) < 1e-13: break
    if abs(Fz(z)[0]) < 1e-8 and z.real > 1 and all(abs(z - w) > 1e-6 for w in zeros):
        zeros.append(z)
zeros.sort(key=lambda w: w.imag)
print('screen', len(cands), 'zeros Re>1:', zeros, round(time.time() - t0, 1), flush=True)
flint.ctx.prec = 128
logs = [acb(k).log() for k in range(1, N + 1)]
def F_acb(z):
    return sum(((-z * L).exp() for L in logs), acb(0))
certs = []
for z in zeros:
    h = min(1e-3, (z.real - 1) / 2)
    r = winding(F_acb, z.real - h, z.real + h, z.imag - h, z.imag + h, nseg=16, maxdepth=14)
    r.update(center=[z.real, z.imag], halfwidth=h, sigma_lower_edge=z.real - h)
    certs.append(r); print(r, flush=True)
out = dict(N=N, TMAX=TMAX, screen='Newton-step on sigma=1, dt=0.05', n_screen_points=len(cands),
           zeros_re_gt_1=[[w.real, w.imag] for w in zeros], certificates=certs, runtime_s=round(time.time() - t0, 1))
os.makedirs(sys.argv[1], exist_ok=True)
json.dump(out, open(os.path.join(sys.argv[1], 'sk_zeta19.json'), 'w'), indent=1)
