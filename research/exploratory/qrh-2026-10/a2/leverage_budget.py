#!/usr/bin/env python3
"""Leverage bookkeeping for LEVERAGE_FAMILIES.md (Sections 3-4).  EXACT rational arithmetic for
Parts D1-D3; Part C is an integer count over positive rational integers, used as a proxy for the
Z[omega] row lattice (only the exponents are compared).  Nothing here checks the analytic model
assumptions (the Poisson threshold, the GL(r) dual length q^r/X, an optimal large sieve).

D1  For a theta coefficient that is ONE normalized Gauss sum of order n (angle +-1/n), the order m of
    the row symbol whose single Poisson Gauss sum pairs with it to total angle 1/2 (the Moebius
    parity, Section 2) is the denominator of 1/2 - 1/n.
D2  Structural boundary sigma(m, r) = 1/2 + (1 - 1/m) max(1/2, 1 - 1/r): leverage c = 1 - 1/m,
    row threshold rho = max(1, 2 - 2/r) for a GL(r)-type reflection with dual length q^r/X and an
    optimal large sieve (the rows term of the large sieve alone forces rho >= 1).  Table for (n, r) with r = 2 and r = n - 1 (Kazhdan-Patterson unique-model range).
D3  All (m, r), 2 <= m <= 12, 1 <= r <= 6, with sigma(m, r) < 11/12.
C   Principal-row counts: product family (a, b) <= H with ab a cube; quotient family with a/b a
    cube or sixth power; single-variable cubes up to H^2.

Usage: python3 leverage_budget.py [HMAX=10**6] [OUT.json]       (about 10 s at HMAX = 10**6)"""
import json, math, sys
from fractions import Fraction as Fr
from collections import Counter

HMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
OUT = sys.argv[2] if len(sys.argv) > 2 else None
res = {}

def m_of_n(n):
    return (Fr(1, 2) - Fr(1, n)).denominator if n > 2 else None
def sigma(m, r):
    return Fr(1, 2) + (1 - Fr(1, m))*max(Fr(1, 2), 1 - Fr(1, r))
known = {  # status of the theta coefficient at primes, from the cited sources
    (3, 2): 'Patterson: tau(p) = cubic Gauss sum (explicit)',
    (3, 3): 'Proskurin/Bump-Hoffstein: tau(p,1) = 0',
    (4, 2): 'undetermined (non-unique model); Eckhardt-Patterson conj: tau(p)^2 ~ 2 g_4(p), angle 3/8',
    (4, 3): 'FG15: tau(p,1) = |p|^{-1/2} conj g_4(p) (unique model, c odd)',
    (2, 2): 'classical theta: tau(p) = 0',
}
D1 = []
for n in range(2, 13):
    m = m_of_n(n)
    rows = []
    for r in sorted({2, n - 1} - {1}):
        if m is None: rows.append({'r': r, 'sigma': None}); continue
        s = sigma(m, r)
        rows.append({'r': r, 'sigma': str(s), 'sigma_float': float(s), 'beats_11_12': s < Fr(11, 12),
                     'status': known.get((n, r), 'undetermined (n > 4 on GL(3), n > 3 on GL(2))'
                                         if r <= 3 else 'GL(r) cover, coefficients not used here')})
    D1.append({'n': n, 'm': m, 'c': str(1 - Fr(1, m)) if m else None, 'by_r': rows})
res['D1_D2'] = D1

D3 = []
for m in range(2, 13):
    for r in range(1, 7):
        s = sigma(m, r)
        if s < Fr(11, 12): D3.append({'m': m, 'r': r, 'sigma': str(s)})
res['D3_beats_11_12'] = D3

# ---- Part C: principal-row counts over positive integers (proxy)
spf = list(range(HMAX + 1))
for p in range(2, int(HMAX**0.5) + 1):
    if spf[p] == p:
        for k in range(p*p, HMAX + 1, p):
            if spf[k] == k: spf[k] = p
def cls(n, m):
    out = []
    while n > 1:
        p = spf[n]; e = 0
        while n % p == 0: n //= p; e += 1
        if e % m: out.append((p, e % m))
    return tuple(out)
def inv(k, m): return tuple((p, (-e) % m) for p, e in k)
C = []
H = 10**3
while H <= HMAX:
    c3 = Counter(cls(a, 3) for a in range(1, H + 1))
    c6 = Counter(cls(a, 6) for a in range(1, H + 1))
    prod3 = sum(v*c3.get(inv(k, 3), 0) for k, v in c3.items())
    quot3 = sum(v*v for v in c3.values()); quot6 = sum(v*v for v in c6.values())
    L = math.log(H)
    C.append({'H': H, 'family_size': H*H,
              'product_cubic_P': prod3, 'P/(H^(2/3) log^2 H)': prod3/(H**(2/3)*L*L),
              'log_P/log_F': math.log(prod3)/math.log(H*H),
              'single_cubes_upto_H2': int(round((H*H)**(1/3))),
              'quotient_cubic_P': quot3, 'quotient_cubic_P/H': quot3/H,
              'quotient_sextic_P': quot6, 'quotient_sextic_P/H': quot6/H})
    H *= 10
res['C_counts'] = C

print(json.dumps(res, indent=1))
if OUT:
    with open(OUT, 'w') as fh: json.dump(res, fh, indent=1)
