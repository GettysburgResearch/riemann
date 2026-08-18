#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import mpmath as mp

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]


def qstar(m: int) -> int:
    if m == 2: return 15
    if m == 3: return 6
    if m == 4: return 3
    return 6 if m >= 5 else 0


def H(x: mp.mpf, n: int) -> mp.mpf:
    if x <= n: return mp.mpf('0')
    return min(mp.log(4), mp.log(x/n))


def A(x: mp.mpf) -> mp.mpf:
    if x <= 2: return mp.mpf('0')
    return mp.fsum(qstar(m)/mp.sqrt(m)*H(x,m) for m in range(2, int(mp.floor(x))+1))


def divisors(limit: mp.mpf):
    out=[(1,1)]
    for p in PRIMES:
        out += [(d*p,-mu) for d,mu in list(out) if d*p <= limit]
    return out


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--output',default='results/counterexample_x184.json'); args=ap.parse_args()
    mp.mp.dps=100
    x=mp.mpf(184)
    F=mp.mpf('0'); M=mp.mpf('0')
    for d,mu in divisors(x/2):
        term=A(x/d)/mp.sqrt(d)
        F += mu*term
        M += term
    result={
        'classification':'PASS_X184_COUNTERCERTIFICATE',
        'x':'184',
        'F':mp.nstr(F,90),
        'M':mp.nstr(M,90),
        'F_over_M':mp.nstr(F/M,90),
        'F_minus_M_over_40':mp.nstr(F-M/40,90),
        '42F_minus_M':mp.nstr(42*F-M,90),
        'one_over_40_claim_holds': bool(F >= M/40),
        'one_over_42_repair_holds': bool(F >= M/42),
        'RH_established':False,
    }
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification']); print(result['F_over_M'])
    return 0

if __name__=='__main__': raise SystemExit(main())
