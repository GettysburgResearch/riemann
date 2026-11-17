#!/usr/bin/env python3
"""SKEPTIC: rigorous argument-principle certificates (sk_wind.py) for zeros of Z_{x^2+5y^2} with Re s > 1,
evaluated with genus formula zeta*L_-20 + L_-4*L_5 (characters rebuilt and checked in sk_ep_probe.py).
The zeros at t ~ 1.48e5, 2.73e5, 5.06e5 were NOT certified by the investigator (they appear only as
unpolished screen candidates in epstein_sigma_gt1_screen.log).
Usage: python3 sk_ep_cert.py OUTDIR re1 im1 [re2 im2 ...]"""
import sys, os, json, time, flint
from flint import acb, arb
from sk_ep_probe import Z
from sk_wind import winding
flint.ctx.prec = 80
out = []
a = sys.argv[2:]
for i in range(0, len(a), 2):
    x, y = float(a[i]), float(a[i + 1])
    h = min(1e-3, (x - 1) / 2)
    t0 = time.time()
    r = winding(Z, x - h, x + h, y - h, y + h, nseg=4, maxdepth=10)
    r.update(center=[x, y], halfwidth=h, sigma_lower_edge=x - h, runtime_s=round(time.time() - t0, 1))
    out.append(r)
    print(r, flush=True)
os.makedirs(sys.argv[1], exist_ok=True)
fn = os.path.join(sys.argv[1], 'sk_ep_cert.json')
old = json.load(open(fn)) if os.path.exists(fn) else []
json.dump(old + out, open(fn, 'w'), indent=1)
