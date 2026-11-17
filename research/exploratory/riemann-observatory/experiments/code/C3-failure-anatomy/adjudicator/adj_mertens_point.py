#!/usr/bin/env python3
"""C3 adjudicator: exact values of the Mertens function M(x) at isolated large x.

Method (independent of both C3 sieves): mu sieved exactly up to U (numpy int8), then
    M(v) = 1 - sum_{d=2}^{v} M(floor(v/d))
evaluated with the usual two-range grouping (d <= sqrt v individually; d > sqrt v grouped by q = floor(v/d)),
memoised for v > U.  Exact integer arithmetic throughout (numpy int64 + Python int); no floating point
enters any value.  Purpose: check checklist item 13 / Hurst (2018) table entry M(7766842813) = 50286,
and spot values M(10^9) = -222 (both C3 sieves) and M(10^10).

Usage: python3 adj_mertens_point.py U x1,x2,... out.json
"""
import sys, json, time, math
import numpy as np

U = int(float(sys.argv[1])); xs = [int(float(x)) for x in sys.argv[2].split(',')]; out = sys.argv[3]
t0 = time.time()
mu = np.ones(U + 1, dtype=np.int8); mu[0] = 0
isp = np.ones(U + 1, dtype=bool); isp[:2] = False
for p in range(2, math.isqrt(U) + 1):
    if isp[p]: isp[p * p::p] = False
primes = np.nonzero(isp)[0]
for p in primes:
    p = int(p)
    mu[p::p] *= -1
    if p * p <= U: mu[p * p::p * p] = 0
Msmall = np.cumsum(mu, dtype=np.int64)
tsieve = time.time() - t0
assert Msmall[10] == -1 and Msmall[100] == 1 and Msmall[1000] == 2 and Msmall[10**4] == -23

memo = {}
def M(v):
    if v <= U: return int(Msmall[v])
    if v in memo: return memo[v]
    r = math.isqrt(v)
    total = 0
    # d in [2, r]: M(v//d) individually (large ones recurse)
    d = np.arange(2, r + 1, dtype=np.int64)
    q = v // d
    small = q <= U
    total += int(Msmall[q[small]].sum())
    for qq in q[~small].tolist(): total += M(int(qq))
    # d > r grouped by q = v//d, q in [1, v//(r+1)]
    qmax = v // (r + 1)
    qs = np.arange(1, qmax + 1, dtype=np.int64)
    cnt = v // qs - v // (qs + 1)
    total += int((Msmall[qs] * cnt).sum())
    val = 1 - total
    memo[v] = val
    return val

vals = {}
for x in xs:
    t1 = time.time(); vals[str(x)] = {"M": M(x), "q=M/sqrt(x)": M(x) / math.sqrt(x), "s": round(time.time() - t1, 2)}
    print(x, vals[str(x)], flush=True)
res = {"script": "adj_mertens_point.py", "U": U, "sieve_s": round(tsieve, 1), "values": vals,
       "versions": {"python": sys.version.split()[0], "numpy": np.__version__},
       "runtime_s": round(time.time() - t0, 1)}
json.dump(res, open(out, 'w'), indent=1)
