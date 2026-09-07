#!/usr/bin/env python3
"""Bounded algebra/interval controls only. No RH or entropy-growth gate.

All mathematical values are integers or fractions. log_bounds uses range
reduction and a convergent atanh series with its complete positive remainder.
Assertions are not used as acceptance conditions, so -O has the same behavior.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from itertools import product
import json
import math
from pathlib import Path
import sys


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def scale(c, a):
    c = Q(c)
    return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])


def sub(a, b):
    return add(a, scale(-1, b))


def square(a):
    return (Q(0) if a[0] <= 0 <= a[1] else min(a[0]**2, a[1]**2),
            max(a[0]**2, a[1]**2))


def log_bounds(r: Q, terms: int = 48):
    r = Q(r)
    require(r > 0, 'log requires a positive rational')
    k = 0
    while r >= 2:
        r /= 2
        k += 1
    while r < 1:
        r *= 2
        k -= 1
    def core(x):
        z = (x-1)/(x+1)
        total = 2*sum((z**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
        tail = 2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
        return (total, total+tail)
    return add(core(r), scale(k, core(Q(2))))


def isprime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))


def factors(n: int):
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0)+1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


def physical(m, n):
    return Q(min(m, n), max(m, n))


def independent(m, n):
    return Q(math.gcd(m, n)**2, m*n)


def positive_pivots(a):
    a = [row[:] for row in a]
    pivots = []
    for j in range(len(a)):
        pivot = a[j][j]
        require(pivot > 0, 'nonpositive Gram pivot')
        pivots.append(str(pivot))
        for i in range(j+1, len(a)):
            for k in range(i, len(a)):
                a[k][i] -= a[k][j]*a[i][j]/pivot
                a[i][k] = a[k][i]
    return pivots


def compute():
    groups = {}
    L = log_bounds(Q(2))
    require(Q(2,3) < L[0] and L[1] < Q(7,10), 'log2 bounds')
    require(log_bounds(Q(3,2))[1] < Q(1,2), 'log1.5')
    require(log_bounds(Q(16,5))[0] > 1, 'central lower constant')
    require(Q(1943,16000) < Q(1,8), 'prime2 modulus enclosure')
    require(Q(19,340) > Q(1,20), 'E2 lower margin')
    require(Q(7,5)**2 < 2 < Q(8,5)**2, 'sqrt2 brackets')
    require(Q(2,3)+Q(1,4)+Q(21,40) < Q(3,2), 'outer tail constant')
    # (a+a^2)/2 = 4+(5/2)sqrt2 < 8, and a/2 < 2.
    require(Q(5,2)*Q(8,5)+4 == 8, 'curvature constant')
    groups['rational_constant_controls'] = 8

    count = 0
    for r, q in product([Q(1,8), Q(1,4), Q(1,2), Q(1), Q(2), Q(4), Q(8)],
                        [Q(1,4), Q(1,2), Q(1), Q(2), Q(4)]):
        # u=(log r)/2, jump=(log q)/2.
        # log cosh Taylor remainder = log((1+rq)/(1+r))-r/(1+r)log q.
        rem = sub(log_bounds((1+r*q)/(1+r)), scale(r/(1+r), log_bounds(q)))
        upper = scale(Q(1,8), square(log_bounds(q)))
        if q == 1:
            require(rem == (0,0), 'zero jump')
        else:
            require(rem[0] > 0 and rem[1] < upper[0], 'convex jump bound')
        count += 1
    groups['convex_jump_interval_controls'] = count

    count = 0
    for r, c in product([Q(1,4), Q(1,2), Q(2,3), Q(7,10)],
                        [Q(-1), Q(-1,2), Q(0), Q(1,2), Q(1)]):
        j = scale(Q(-1,2), log_bounds(1-2*r*c+r*r))
        diff = sub(j, (r*c,r*c))
        require(max(abs(diff[0]), abs(diff[1])) < r*r/(2*(1-r)), 'power tail')
        require(max(abs(j[0]),abs(j[1])) < r/(1-r), 'full jump')
        count += 1
    groups['complete_log_jump_interval_controls'] = count

    count = 0
    for m, n in product(range(1,33), repeat=2):
        fm, fn = factors(m), factors(n)
        inv = Q(1)
        for p in set(fm) | set(fn):
            inv /= p**abs(fm.get(p,0)-fn.get(p,0))
        require(inv == independent(m,n), 'mixed product law')
        require(physical(m,n) >= inv, 'entry comparison')
        if m % n == 0 or n % m == 0:
            require(physical(m,n) == inv, 'one-sign moments')
        count += 1
    groups['exact_mixed_phase_pairs'] = count

    cov = (Q(2,3)+Q(1,6))/2-Q(1,2)*Q(1,3)
    require(cov == Q(1,4), 'actual prime covariance')
    diff = physical(2,3)-independent(2,3)
    require(diff == Q(1,2) and -diff*diff == Q(-1,4), 'indefinite difference')
    groups['prime_2_3_separators'] = 2

    psd = []
    packets = [[1,2,3,4,5], [2,3,5,7,11], [101,102,103,104]]
    for packet in packets:
        for kernel in [physical, independent]:
            psd.append(positive_pivots([[kernel(m,n) for n in packet] for m in packet]))
    groups['exact_positive_Gram_matrices'] = len(psd)

    count = 0
    for k in range(2,13):
        M = k**3
        ns = range(M+1,M+k+1)
        c = sum((physical(m,n) for m in ns for n in ns),Q(0))/k
        i = sum((independent(m,n) for m in ns for n in ns),Q(0))/k
        require(c >= Q(k,2) and i < 2, 'nonuniform upper comparison')
        count += 1
    for M in [2,3,10,100,1000]:
        c = 1-physical(M,M+1)
        i = 1-independent(M,M+1)
        require(c == Q(1,M+1) and i/c >= Q(M+1,2), 'reverse comparison')
        count += 1
    groups['comparison_growth_controls'] = count

    count = 0
    for X in [2,3,5,10,30,64,100,256]:
        p = sum((Q(1,n) for n in range(2,X+1) if isprime(n)),Q(0))
        lx = log_bounds(Q(X))
        upper_target_lo = 3*log_bounds(1+lx[0])[0]
        require(p < upper_target_lo, 'finite prime harmonic inequality')
        count += 1
    groups['finite_prime_harmonic_controls'] = count
    return {
        'schema': 'EFB26-bounded-controls-v1',
        'arithmetic': 'EXACT_RATIONAL_AND_DIRECTED_RATIONAL_LOG_INTERVALS',
        'RH_proved': False,
        'work_upper_bound_proved': False,
        'entropy_integral_evaluated': False,
        'groups': groups,
        'total_bounded_cases': sum(groups.values()),
        'covariance_prime_2_3': '1/4',
        'difference_determinant_prime_2_3': '-1/4',
        'positive_Gram_pivots': psd,
    }


def strict_json(text):
    def pairs(items):
        d = {}
        for k,v in items:
            if k in d:
                raise ValueError('duplicate JSON key')
            d[k] = v
        return d
    def nofloat(_):
        raise ValueError('floating JSON value disallowed')
    return json.loads(text, object_pairs_hook=pairs, parse_float=nofloat, parse_constant=nofloat)


def same_types(a,b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys()==b.keys() and all(same_types(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(same_types(x,y) for x,y in zip(a,b))
    return a==b


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', type=Path)
    args = parser.parse_args()
    data = compute()
    if args.check is not None:
        require(same_types(data,strict_json(args.check.read_text())), 'retained result differs')
    print(json.dumps(data,sort_keys=True,indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        raise SystemExit(1)
