#!/usr/bin/env python3
"""HEURISTIC onset estimate for failure of the PR 910 curve condition (random Euler product model).

Nothing here is a theorem about zeta.  Model:
  log|zeta(sigma0 + i t)|  ~  X = sum_p -log|1 - U_p p^{-sigma0}|,  U_p i.i.d. uniform on the circle,
  CGF K(lam) = log E e^{lam X} = sum_p log 2F1(lam/2, lam/2; 1; p^{-2 sigma0})   (exact for the model),
  tail size at the point:  |sum_{n>Y} mu(n) n^{-s}|  =  A * Y^{-delta} * |zeta|^{-theta}
      (A, theta are inputs; the float64 data in results/noise_floor_*.json suggest A ~ 0.2-1.8 and a
       bulk log-log slope theta ~ 0.7, while targeted small-prime resonance points show no clear
       decrease, theta ~ 0, in the range |zeta| <= 10).
Failure at a point needs |zeta * tail| >= 1/sqrt(8), i.e.
  log|zeta| >= V* = (log(0.3536/A) + c loglog Y) / (1 - theta),   using delta log Y = c loglog Y.
Tail probability by the Bahadur-Rao saddle point:  P(X >= V) ~ exp(K(l) - l V) / (l sqrt(2 pi K''(l))), K'(l) = V.
"Onset" = least T on a log grid with  log N_eff + log P(X >= V*) >= 0,  N_eff = T trials in [T, 2T].

Primes up to 10^7 are summed exactly (scipy hyp2f1 for p <= 10^4, a 4-term series above);
primes beyond 10^7 contribute (lam/2)^2 E_1((2 sigma0 - 1) log 10^7) (leading order).
"""
import argparse
import json
import math

import numpy as np
from scipy.special import hyp2f1, exp1


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.nonzero(s)[0].astype(np.float64)


PR = primes_upto(10 ** 7)
LP = np.log(PR)
SMALL = PR <= 1e4
PMAX = 1e7


def K(lam, sigma):
    a = lam / 2.0
    x = np.exp(-2 * sigma * LP)
    ks = np.sum(np.log(hyp2f1(a, a, 1.0, x[SMALL])))
    xb = x[~SMALL]
    c1 = a * a
    c2 = (a * (a + 1) / 2) ** 2
    c3 = (a * (a + 1) * (a + 2) / 6) ** 2
    c4 = (a * (a + 1) * (a + 2) * (a + 3) / 24) ** 2
    kb = np.sum(np.log1p(xb * (c1 + xb * (c2 + xb * (c3 + xb * c4)))))
    tail = a * a * exp1((2 * sigma - 1) * math.log(PMAX))
    return ks + kb + tail


def logP(V, sigma):
    """Bahadur-Rao estimate of log P(X >= V) (natural log)."""
    h = 1e-3
    lo, hi = 1e-3, 200.0
    dK = lambda l: (K(l + h, sigma) - K(l - h, sigma)) / (2 * h)
    if dK(lo) >= V:
        return 0.0, lo
    for _ in range(32):
        mid = 0.5 * (lo + hi)
        if dK(mid) < V:
            lo = mid
        else:
            hi = mid
    l = 0.5 * (lo + hi)
    K2 = (K(l + h, sigma) - 2 * K(l, sigma) + K(l - h, sigma)) / h ** 2
    return K(l, sigma) - l * V - math.log(l * math.sqrt(2 * math.pi * K2)), l


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cs', default='2,2.5,3')
    ap.add_argument('--As', default='0.3,1.0')
    ap.add_argument('--thetas', default='0,0.5,0.7')
    ap.add_argument('--log10T', default='10,20,30,40,60,80,100,150,200,300,500,700,1000,1500,2000,3000')
    a = ap.parse_args()
    grid = [float(v) for v in a.log10T.split(',')]
    out = []
    for c in [float(v) for v in a.cs.split(',')]:
        for A in [float(v) for v in a.As.split(',')]:
            for th in [float(v) for v in a.thetas.split(',')]:
                rows, onset = [], None
                for g in grid:
                    logT = g * math.log(10)
                    logY = logT + math.log(4)
                    sig = 0.5 + c * math.log(logY) / logY
                    if sig >= 1:
                        continue
                    V = (math.log(0.3536 / A) + c * math.log(logY)) / (1 - th)
                    lp, lam = logP(V, sig)
                    margin = logT + lp
                    rows.append(dict(log10T=g, sigma0=round(sig, 5), Vstar=round(V, 3),
                                     log10P=round(lp / math.log(10), 2), saddle_lambda=round(lam, 2),
                                     log10_expected_count=round(margin / math.log(10), 2)))
                    if onset is None and margin >= 0:
                        onset = g
                out.append(dict(c=c, A=A, theta=th, onset_log10T_on_grid=onset, rows=rows))
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
