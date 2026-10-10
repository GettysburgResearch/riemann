#!/usr/bin/env python3
"""Noise-floor reconnaissance for the PR 910 curve condition (float64; NOT certified).

Reuses (imports, does not modify) Native / mobius_sieve / sigma0 / Y_of_T from pr910_height_scan.py.

At a point s = sigma + i t with Y = Y(t) = ceil(4(t+2)) it computes
  B_Y, G_Y                        (finite Dirichlet polynomials, as in the scan script)
  zeta(s)                         Euler-Maclaurin with N = Y and 3 Bernoulli corrections
                                  (|s|/(2 pi Y) <= 0.04, so the truncation is far below float64 noise
                                  at these heights; validated against mpmath in `validate`)
  tail  = 1/zeta - G_Y            (equals sum_{n>Y} mu(n) n^{-s} under RH; here only a DEFINITION)
  near  = sum_{Y/2 < n <= Y} mu(n) n^{-s}   (the near-cutoff block of G_Y)
and reports |zeta|, |G_Y|, |1/zeta|, |tail|, |zeta*tail|, |R_Y|, the scales Y^{-delta},
sqrt(6/pi^2) * Y^{-delta} / sqrt(2 delta), and |near|/|G_Y|.

Subcommands:
  validate   EM zeta vs mpmath at three moderate heights
  points     the large/small-|zeta| candidates already found in results/pr910_resonance_*.json
  random     uniform random heights, binned by |zeta| quantile (does the tail shrink at large values?)
"""
import argparse
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
from pr910_height_scan import Native, mobius_sieve, sigma0, Y_of_T  # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B2K = [1.0 / 6, -1.0 / 30, 1.0 / 42]


def zeta_em(sigma, t, Y, BY):
    """zeta(s) = sum_{n<=Y} n^-s - Y^-s/2 + Y^{1-s}/(s-1) + sum_k B_2k/(2k)! (s)_{2k-1} Y^{-s-2k+1}."""
    s = complex(sigma, t)
    lY = math.log(Y)
    z = BY - 0.5 * np.exp(-s * lY) + np.exp((1 - s) * lY) / (s - 1)
    poch = s
    for k, b in enumerate(B2K, start=1):
        if k > 1:
            poch *= (s + 2 * k - 3) * (s + 2 * k - 2)
        z += b / math.factorial(2 * k) * poch * np.exp((-s - 2 * k + 1) * lY)
    return z


def point(mu, Y, t, sigma, c=2.0):
    nat = Native(mu, Y)
    ev = nat.eval(sigma, [t])
    B, G, R = complex(ev['B'][0]), complex(ev['G'][0]), complex(ev['R'][0])
    z = complex(zeta_em(sigma, t, Y, B))
    tail = 1.0 / z - G
    n = np.arange(Y // 2 + 1, Y + 1)
    near = complex(np.sum(mu[n].astype(np.float64) * np.exp(-(sigma + 1j * t) * np.log(n))))
    L = math.log(Y)
    delta = sigma - 0.5
    floor0 = Y ** (-delta)
    floor1 = math.sqrt(6 / math.pi ** 2) * floor0 / math.sqrt(2 * delta)
    E = z - B
    return dict(Y=Y, t=round(t, 6), sigma=round(sigma, 6), on_curve=abs(sigma - sigma0(Y, c)) < 1e-12,
                abs_zeta=abs(z), abs_G=abs(G), abs_inv_zeta=abs(1 / z), abs_tail=abs(tail),
                abs_zeta_tail=abs(z * tail), abs_R=abs(R), abs_E_times_G=abs(E * G),
                Y_minus_delta=floor0, rms_floor=floor1, tail_over_Ymd=abs(tail) / floor0,
                tail_over_rmsfloor=abs(tail) / floor1, near_over_G=abs(near) / abs(G),
                abs_near=abs(near), G_over_inv_zeta=abs(G) * abs(z), logY=L)


def cmd_validate(args):
    import mpmath
    mpmath.mp.dps = 25
    mu = mobius_sieve(200000)
    out = []
    for t, sigma in [(2819.5, 0.9786839822973252), (30775.1, 0.7), (12345.6, 0.6)]:
        Y = Y_of_T(t)
        nat = Native(mu, Y)
        B = complex(nat.eval(sigma, [t])['B'][0])
        z = complex(zeta_em(sigma, t, Y, B))
        zm = complex(mpmath.zeta(mpmath.mpc(sigma, t)))
        out.append(dict(t=t, sigma=sigma, Y=Y, em=[z.real, z.imag], mp=[zm.real, zm.imag],
                        rel_err=abs(z - zm) / abs(zm)))
    print(json.dumps(out, indent=1))


def cmd_points(args):
    files = ['results/pr910_resonance_c2.json', 'results/pr910_resonance_c2_1e6.json',
             'results/pr910_resonance_sigma07.json', 'results/pr910_resonance_sigma075.json']
    pts = []
    for f in files:
        d = json.load(open(os.path.join(HERE, f)))
        for kind in ['large', 'small']:
            for r in d[kind][:args.k]:
                pts.append((kind, f.split('/')[-1], r['Y'], r['T'], r['sigma']))
    ymax = max(p[2] for p in pts)
    mu = mobius_sieve(ymax + 10)
    out = []
    for kind, f, Y, t, sigma in pts:
        r = point(mu, Y, t, sigma)
        r.update(kind=kind, source=f)
        out.append(r)
    print(json.dumps(out, indent=1))


def cmd_random(args):
    rng = np.random.default_rng(args.seed)
    ts = np.sort(rng.uniform(args.tlo, args.thi, args.n))
    mu = mobius_sieve(Y_of_T(args.thi) + 10)
    out = {}
    for sig in ['curve'] + [float(x) for x in args.sigmas.split(',') if x]:
        rows = []
        for t in ts:
            Y = Y_of_T(t)
            s = sigma0(Y) if sig == 'curve' else sig
            rows.append(point(mu, Y, float(t), s))
        z = np.array([r['abs_zeta'] for r in rows])
        q = np.quantile(z, [0.5, 0.9, 0.99])
        bins = [(0, q[0]), (q[0], q[1]), (q[1], q[2]), (q[2], np.inf)]
        summ = []
        for lo, hi in bins:
            sel = [r for r in rows if lo <= r['abs_zeta'] < hi]
            summ.append(dict(zeta_range=[float(lo), float(hi)], n=len(sel),
                             median_tail_over_Ymd=float(np.median([r['tail_over_Ymd'] for r in sel])),
                             median_tail_over_rmsfloor=float(np.median([r['tail_over_rmsfloor'] for r in sel])),
                             median_near_over_G=float(np.median([r['near_over_G'] for r in sel])),
                             median_G_times_zeta=float(np.median([r['G_over_inv_zeta'] for r in sel])),
                             max_zeta_tail=float(max(r['abs_zeta_tail'] for r in sel))))
        lz = np.log(z)
        lt = np.log([r['abs_tail'] for r in rows])
        slope = float(np.polyfit(lz, lt, 1)[0])
        out[str(sig)] = dict(bins=summ, slope_logtail_on_logzeta=slope,
                             max_abs_zeta=float(z.max()),
                             max_zeta_tail=float(max(r['abs_zeta_tail'] for r in rows)))
    print(json.dumps(dict(t_range=[args.tlo, args.thi], n=args.n, seed=args.seed, result=out), indent=1))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    sp.add_parser('validate')
    p = sp.add_parser('points'); p.add_argument('--k', type=int, default=6)
    r = sp.add_parser('random')
    r.add_argument('--tlo', type=float, default=20000.0); r.add_argument('--thi', type=float, default=100000.0)
    r.add_argument('--n', type=int, default=400); r.add_argument('--seed', type=int, default=20261010)
    r.add_argument('--sigmas', default='0.7')
    a = ap.parse_args()
    dict(validate=cmd_validate, points=cmd_points, random=cmd_random)[a.cmd](a)


if __name__ == '__main__':
    main()
