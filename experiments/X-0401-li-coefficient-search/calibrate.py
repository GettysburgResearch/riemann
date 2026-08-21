#!/usr/bin/env python3
"""High-precision, non-interval calibration of two Li-coefficient formulas."""
from __future__ import annotations
import argparse, json, platform, sys, time
from math import comb
from pathlib import Path
import mpmath as mp


def eta_constants(max_index: int) -> list[mp.mpf]:
    c = [mp.mpf(0)] * (max_index + 2)
    c[0] = mp.mpf(1)
    for k in range(1, max_index + 2):
        c[k] = (-1) ** (k - 1) * mp.stieltjes(k - 1) / mp.factorial(k - 1)
    eta = [mp.mpf(0)] * (max_index + 1)
    for m in range(max_index + 1):
        value = (m + 1) * c[m + 1]
        for j in range(1, m + 1):
            value -= c[j] * eta[m - j]
        eta[m] = value
    return eta


def li_via_eta(n_max: int) -> list[mp.mpf]:
    eta = eta_constants(n_max - 1)
    a1 = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
    values = []
    for n in range(1, n_max + 1):
        value = n * a1
        for k in range(2, n + 1):
            local = ((-1) ** (k + 1) + eta[k - 1]
                     + (-1) ** k * (1 - mp.power(2, -k)) * mp.zeta(k))
            value += comb(n, k) * local
        values.append(value)
    return values


def dlogxi(s: mp.mpc) -> mp.mpc:
    return (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2 + mp.zeta(s, derivative=1) / mp.zeta(s))


def li_via_cauchy(n_max: int, radius: mp.mpf, samples: int) -> list[mp.mpf]:
    values = []
    sampled = []
    for j in range(samples):
        theta = 2 * mp.pi * j / samples
        z = radius * mp.e ** (1j * theta)
        s = 1 / (1 - z)
        sampled.append(s * s * dlogxi(s))
    for n in range(1, n_max + 1):
        fourier = mp.fsum(
            sampled[j] * mp.e ** (-2j * mp.pi * j * (n - 1) / samples)
            for j in range(samples)
        ) / samples
        values.append(mp.re(fourier) / radius ** (n - 1))
    return values


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('--n-max', type=int, default=50)
    p.add_argument('--dps', type=int, default=100)
    p.add_argument('--radius', default='0.5')
    p.add_argument('--samples', type=int, default=256)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    mp.mp.dps = args.dps
    t0 = time.time(); a = li_via_eta(args.n_max); eta_seconds = time.time()-t0
    t0 = time.time(); b = li_via_cauchy(args.n_max, mp.mpf(args.radius), args.samples); cauchy_seconds=time.time()-t0
    diffs = [abs(x-y) for x,y in zip(a,b)]
    checkpoints = sorted(set([1,2,3,4,5,10,20,30,40,50,args.n_max]))
    checkpoints = [n for n in checkpoints if n <= args.n_max]
    result = {
        'method_a': 'Stieltjes-to-eta recurrence',
        'method_b': 'direct high-precision Cauchy extraction of xi logarithmic derivative',
        'classification': 'high-precision non-rigorous calibration',
        'n_max': args.n_max,
        'dps': args.dps,
        'radius': args.radius,
        'samples': args.samples,
        'eta_seconds': eta_seconds,
        'cauchy_seconds': cauchy_seconds,
        'max_abs_difference': mp.nstr(max(diffs), 30),
        'minimum_method_a': {'n': 1+min(range(args.n_max), key=lambda i:a[i]), 'value':mp.nstr(min(a),30)},
        'minimum_method_b': {'n': 1+min(range(args.n_max), key=lambda i:b[i]), 'value':mp.nstr(min(b),30)},
        'checkpoints': {str(n): {'eta':mp.nstr(a[n-1],40), 'cauchy':mp.nstr(b[n-1],40), 'abs_diff':mp.nstr(diffs[n-1],10)} for n in checkpoints},
        'environment': {'python':sys.version.split()[0], 'mpmath':mp.__version__, 'platform':platform.platform()},
    }
    text=json.dumps(result,indent=2,sort_keys=True)
    print(text)
    if args.output: args.output.write_text(text+'\n')

if __name__=='__main__': main()
