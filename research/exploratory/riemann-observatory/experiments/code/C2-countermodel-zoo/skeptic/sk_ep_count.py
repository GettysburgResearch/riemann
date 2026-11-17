#!/usr/bin/env python3
"""SKEPTIC: rigorous completeness test for C2-09 (Z_{x^2+5y^2}, 1 <= t <= T), same logic as sk_dh_count.py:
N_box = zeros in [-0.7, 1.7] x [1, T] (rigorous argument principle, sk_wind.winding; contains all zeros with
1 <= t <= T because Z != 0 for sigma >= 1.17816 (C2-11, re-checked in sk_edges.py) and, by the functional
equation, for sigma <= -0.17816), versus certified sign changes of the real function Lambda_Q(1/2+it).
Usage: python3 sk_ep_count.py OUTDIR T"""
import sys, os, json, time
import flint
from flint import acb, arb
from sk_wind import winding
from sk_ep_probe import Z
flint.ctx.prec = 80


def Lam(s):
    return ((arb(20).sqrt() / (2 * arb.pi())).log() * s).exp() * s.gamma() * Z(s)


T = float(sys.argv[2])
t0 = time.time()
W = winding(Z, -0.7, 1.7, 1.0, T, nseg=300, maxdepth=16)
print('box', W, round(time.time() - t0, 1), flush=True)
signs, nunc, t = [], 0, 1.0
while t <= T:
    v = Lam(acb(0.5, t)).real
    if v > 0:
        signs.append(1)
    elif v < 0:
        signs.append(-1)
    else:
        nunc += 1
    t += 0.005
sc = sum(1 for a, b in zip(signs, signs[1:]) if a != b)
out = dict(T=T, box=[-0.7, 1.7, 1.0, T], winding=W, line_sign_changes=sc, uncertified=nunc,
           N_box_minus_line=(W['count'] - sc) if W.get('ok') else None, runtime_s=round(time.time() - t0, 1))
print(out, flush=True)
os.makedirs(sys.argv[1], exist_ok=True)
json.dump(out, open(os.path.join(sys.argv[1], f'sk_ep_count_T{int(T)}.json'), 'w'), indent=1)
