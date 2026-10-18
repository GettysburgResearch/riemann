"""FLOATING_RECONNAISSANCE of complete primitive-ratio coefficients.

The printed tail values use binary64 and are NOT directed enclosures. The
analytic infinite-tail formula is proved in the paper. No zero-free or RH
claim follows from these finite observations.
"""
import argparse
import json
import math
import time
from pathlib import Path

import numpy as np


def beta_sieve(n):
    flags = np.ones(n + 1, dtype=np.bool_)
    flags[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            flags[p*p::p] = False
    beta = np.ones(n + 1, dtype=np.float64)
    for pv in np.flatnonzero(flags):
        p = int(pv)
        beta[p::p] *= -(p*p - 1)/(p + 2)
    beta[1:] /= np.arange(1, n + 1)
    beta[0] = 0
    return beta


def explore(limit, max_small):
    start = time.monotonic()
    beta = beta_sieve(limit)
    rr = np.arange(1, limit + 1, dtype=np.int64)
    logs = np.log(rr)
    base = beta[1:]/np.sqrt(rr)
    accum = 1.0
    records = []
    for s in range(1, max_small + 1):
        right = rr[s:]
        mask = np.gcd(right, s) == 1
        weights = np.exp(-(logs[s:] - math.log(s))**2/8)
        inner = float(np.dot(base[s:][mask], weights[mask]))
        accum += 2*float(beta[s])/math.sqrt(s)*inner
        tail = 2*math.exp(.5)*math.sqrt(2*math.pi)*math.fsum(
            abs(float(beta[j]))*math.erfc((math.log(limit/j)-2)/math.sqrt(8))
            for j in range(1, s+1)
        )
        if s <= 12 or s & (s-1) == 0 or s == max_small:
            rec = {'small_cutoff': s, 'ratio_limit': limit,
                   'finite_coefficient': accum, 'analytic_tail_float': tail}
            records.append(rec)
            print(json.dumps(rec), flush=True)
    return {'arithmetic': 'FLOATING_RECONNAISSANCE',
            'not_a_directed_enclosure': True, 'records': records,
            'elapsed_seconds': time.monotonic()-start}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit', type=int, default=2_000_000)
    parser.add_argument('--small', type=int, default=128)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if not 1 <= args.small <= args.limit:
        raise ValueError('Require 1 <= small <= limit.')
    result = explore(args.limit, args.small)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
