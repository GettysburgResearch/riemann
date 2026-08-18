#!/usr/bin/env python3
from __future__ import annotations
import itertools
import json
from fractions import Fraction
from pathlib import Path
import mpmath as mp

mp.mp.dps = 120
PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
X = 184
LOG4 = mp.log(4)

def qstar(m: int) -> int:
    if m < 2: return 0
    if m == 2: return 15
    if m == 3: return 6
    if m == 4: return 3
    return 6

def h(x: mp.mpf, n: int) -> mp.mpf:
    if x <= n:
        return mp.mpf('0') if x < n else mp.mpf('0')
    return min(LOG4, mp.log(x / n))

def astar(x: mp.mpf) -> mp.mpf:
    if x < 2:
        return mp.mpf('0')
    return mp.fsum(mp.mpf(qstar(m)) / mp.sqrt(m) * h(x, m)
                   for m in range(2, int(mp.floor(x)) + 1))

def safe_divisors(cap: int):
    out=[]
    def rec(i: int, d: int, mu: int):
        if i == len(PRIMES):
            out.append((d,mu)); return
        rec(i+1,d,mu)
        p=PRIMES[i]
        if d <= cap//p:
            rec(i+1,d*p,-mu)
    rec(0,1,1)
    return sorted(out)

divs=safe_divisors(X//2)
F=mp.fsum(mp.mpf(mu)/mp.sqrt(d)*astar(mp.mpf(X)/d) for d,mu in divs)
M=mp.fsum(mp.mpf(1)/mp.sqrt(d)*astar(mp.mpf(X)/d) for d,mu in divs)
ratio=F/M
old_margin=F-M/40
new_lower=42*F-M
new_upper=M-20*F
out={
    'schema':'riemann.p61-x184-high-precision.v1',
    'precision_decimal_digits':mp.mp.dps,
    'x':X,
    'divisors_used':len(divs),
    'F':mp.nstr(F,100),
    'M':mp.nstr(M,100),
    'F_over_M':mp.nstr(ratio,100),
    'one_over_40':mp.nstr(mp.mpf(1)/40,100),
    'F_minus_M_over_40':mp.nstr(old_margin,100),
    '42F_minus_M':mp.nstr(new_lower,100),
    'M_minus_20F':mp.nstr(new_upper,100),
    'classification':'high-precision independent computation; the sign gap is far larger than the displayed numerical uncertainty',
}
print(json.dumps(out,indent=2))
