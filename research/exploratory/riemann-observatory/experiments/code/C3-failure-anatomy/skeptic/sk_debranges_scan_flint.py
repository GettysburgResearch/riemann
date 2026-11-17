#!/usr/bin/env python3
"""Skeptic re-count of de Branges necessary-condition failures, K zeros, with a formula
different from the investigator's (closed form at a zero: xi'(rho) = rho(rho-1) pi^{-rho/2} Gamma(rho/2) zeta'(rho)),
zeta'(rho) from the Arb series of zeta alone, zeros from the certified TSV (n, mid, rad), Re rho = 1/2
(justified because RH is verified far beyond these heights).  Sign certified by Arb balls.
Also: mpmath spot check on a random sample (non-rigorous, different library).
Usage: python3 sk_debranges_scan_flint.py K TSV out.json"""
import sys, json, time, random
import flint, mpmath as mp
from flint import acb, arb, acb_series, ctx
ctx.prec = 128
K = int(sys.argv[1]); path = sys.argv[2]; out = sys.argv[3]
t0 = time.time()
PI = arb.pi()
zs = []
for line in open(path):
    n, m, r = line.split()[:3]
    if int(n) > K: break
    zs.append((int(n), m, r))
neg = []; und = []
for n, m, r in zs:
    rho = acb(arb("0.5"), arb(m, r))
    zp = acb_series.zeta(acb_series([rho, 1], prec=2)).coeffs()[1]
    xip = rho*(rho-1)*(-(rho/2)*acb(PI).log()).exp()*(rho/2).gamma()*zp
    s1 = 1+rho
    xi1 = s1*(s1-1)*(-(s1/2)*acb(PI).log()).exp()*(s1/2).gamma()*s1.zeta()
    q = -(xip*xi1).real
    if q < 0: neg.append(n)
    elif not (q > 0): und.append(n)
res = {"K": K, "num_negative": len(neg), "undetermined": und, "first": neg[:10], "prec": ctx.prec,
       "count_le_2000": sum(1 for x in neg if x <= 2000)}
# mpmath spot check
random.seed(12345)
mp.mp.dps = 25
sample = random.sample(range(2001, K+1), 150) if K > 2000 else []
negset = set(neg); mism = []
for n in sample:
    g = mp.mpf(zs[n-1][1]); rho = mp.mpc(0.5, g)
    a = rho*(rho-1)*mp.pi**(-rho/2)*mp.gamma(rho/2)*mp.zeta(rho, derivative=1)
    s1 = 1+rho; b = s1*(s1-1)*mp.pi**(-s1/2)*mp.gamma(s1/2)*mp.zeta(s1)
    if (-mp.re(a*b) < 0) != (n in negset): mism.append(n)
res["mpmath_spot_sample_size"] = len(sample); res["mpmath_spot_mismatches"] = mism
res["runtime_s"] = round(time.time()-t0, 1)
json.dump(res, open(out, "w"), indent=1); print(json.dumps(res))
