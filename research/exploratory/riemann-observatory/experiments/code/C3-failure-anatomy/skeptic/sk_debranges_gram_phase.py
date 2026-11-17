#!/usr/bin/env python3
"""Skeptic: reduce the de Branges zero condition -Xi'(g_n) Im xi(3/2+i g_n) >= 0 to a Gram-type phase condition.
Identity: arg xi(3/2+it) = theta(t) + c(t) + arg zeta(3/2+it), with c(t) -> 5pi/4 (mod 2pi) by Stirling.
Since sign Xi'(g_n) alternates, the condition reads  sin(theta(g_n) + 5pi/4 + arg zeta(3/2+i g_n)) * s_n >= 0
for a fixed alternating sign s_n.  We report: max |c(g_n) - 5pi/4| (mod 2pi), and the failure rate binned by
the Gram offset u_n = theta(g_n)/pi - n (Gram's law ~ u_n in [-1,0)).  mpmath, NUMERICAL-NONRIGOROUS.
Usage: python3 sk_debranges_gram_phase.py K TSV out.json"""
import sys, json, mpmath as mp
mp.mp.dps = 25
K = int(sys.argv[1]); path = sys.argv[2]; out = sys.argv[3]
def xi(s): return s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
maxdev = 0; rows = []
for line in open(path):
    n, m = line.split()[:2]; n = int(n)
    if n > K: break
    g = mp.mpf(m)
    rho = mp.mpc(0.5, g)
    a = rho*(rho-1)*mp.pi**(-rho/2)*mp.gamma(rho/2)*mp.zeta(rho, derivative=1)
    b = xi(1+rho)
    fail = (-mp.re(a*b) < 0)
    th = mp.siegeltheta(g); az = mp.arg(mp.zeta(mp.mpc(1.5, g)))
    c = (mp.arg(b) - th - az - 5*mp.pi/4)
    c = float((c + mp.pi) % (2*mp.pi) - mp.pi)
    maxdev = max(maxdev, abs(c)) if n >= 10 else maxdev
    u = float(th/mp.pi - n)
    rows.append((n, bool(fail), u, float(az)))
fails = [r for r in rows if r[1]]
# failure rate by Gram offset bins
bins = {}
for n, f, u, az in rows:
    k = round(u - 0.5*0, 1)
    key = "%.1f" % (mp.floor(u*4)/4)
    bins.setdefault(key, [0, 0]); bins[key][0] += 1; bins[key][1] += int(f)
res = {"K": K, "num_fail": len(fails), "max_|c-5pi/4|_n>=10": maxdev,
       "fail_rate_by_gram_offset_quarter_bins": {k: [v[0], v[1], round(v[1]/v[0], 3)] for k, v in sorted(bins.items(), key=lambda kv: float(kv[0]))}}
json.dump(res, open(out, "w"), indent=1); print(json.dumps(res, indent=1))
