#!/usr/bin/env python3
"""Exact finite checks of BL formulas; not an infinite analytic certificate."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
import math
import census as c

checks = Counter()


def need(ok, label):
    if not ok:
        raise RuntimeError(label)
    checks[label] += 1


def multiply(x, y):
    a, b = x
    d, e = y
    return a*d-b*e, a*e+b*d-b*e


def residue_key(u, selected):
    a, b = u
    return tuple((a+r*b) % p if r is not None else (a % p, b % p)
                 for q, p, r, table in selected)


def complete_averages():
    primes = c.prime_ideals(32)
    supports = ((), (0,), (0, 1), (0, 2), (0, 6))
    for support in supports:
        selected = [primes[j] for j in support]
        N = math.prod(p[0] for p in selected)
        reps = {}
        for a in range(N):
            for b in range(N):
                u = (a, b)
                reps.setdefault(residue_key(u, selected), u)
                if len(reps) == N:
                    break
            if len(reps) == N:
                break
        need(len(reps) == N, 'complete_CRT_residue_coverage')
        for exps in product(range(1, 7), repeat=len(support)):
            total = [0, 0]
            for u in reps.values():
                z = (1, 0)
                for e, prime in zip(exps, selected):
                    v = c.local_phase(u, prime)
                    if v == 6:
                        z = (0, 0)
                        break
                    z = multiply(z, c.ROOTS[(e*v) % 6])
                total[0] += z[0]
                total[1] += z[1]
            expected = math.prod(p[0]-1 for p in selected) if all(e == 6 for e in exps) else 0
            need(tuple(total) == (expected, 0), 'complete_sextic_average_with_masks')
            need(Q(expected, N) == (math.prod(Q(p[0]-1,p[0]) for p in selected)
                                   if all(e == 6 for e in exps) else 0), 'density_normalization')
        if selected:
            need(math.prod(p[0]-1 for p in selected) != N, 'reject_neutral_zero_erasure')


def dual_norms():
    for a, b in product(range(-4, 5), repeat=2):
        n = c.norm((a, b))
        if not n:
            continue
        for m, t in product(range(-3, 4), repeat=2):
            if m == t == 0:
                continue
            x = Q((a-b)*m-b*t, n)
            y = Q(b*m+a*t, n)
            squared = Q(4,3)*(x*x+x*y+y*y)
            need(n*squared == Q(4,3)*(m*m+m*t+t*t), 'ideal_dual_scaling')
            need(n*squared >= Q(4,3), 'dual_gap')
            need(n*squared > Q(1,64), 'fixed_support_pruning_at_H_equals_NQ')


def trim(p):
    while len(p)>1 and not p[-1]:
        p.pop()
    return p


def divrem(p, q):
    p = p[:]
    out = [0]*max(1, len(p)-len(q)+1)
    while len(p)>=len(q) and p != [0]:
        need(q[-1] == 1, 'monic_polynomial_division')
        j = len(p)-len(q)
        x = p[-1]
        out[j] = x
        for i,v in enumerate(q):
            p[j+i] -= x*v
        trim(p)
    return trim(out), trim(p)


def cyclotomics(limit):
    out = {}
    for n in range(1, limit+1):
        p = [-1]+[0]*(n-1)+[1]
        for d in range(1,n):
            if n%d == 0:
                p, r = divrem(p, out[d])
                need(r == [0], 'cyclotomic_exact_factorization')
        out[n] = p
    return out


def fejer_coset(L, q, a, degree, cyclo):
    # |sum_{j=0}^degree exp(2pi i j x/L)|^2: nonnegative by definition.
    p = [0]*L
    for x in range(a,L,q):
        for j in range(degree+1):
            for k in range(degree+1):
                p[((j-k)*x)%L] += 1
    return divrem(trim(p), cyclo[L])[1]


def finite_quadrature():
    cyclo = cyclotomics(48)
    for q in range(1,13):
        L=4*q
        for a in range(q):
            # Fourier degree 2 is below first residue-coset dual frequency 4.
            need(fejer_coset(L,q,a,2,cyclo) == [12], 'finite_bandlimited_coset_quadrature')
    x = fejer_coset(8,2,0,4,cyclo)
    y = fejer_coset(8,2,1,4,cyclo)
    need(x != y, 'reject_support_at_first_nonzero_frequency')


def main():
    complete_averages()
    dual_norms()
    finite_quadrature()
    print(json.dumps({'status':'PASS','checks':dict(sorted(checks.items())),
                      'total_predicates':sum(checks.values()),
                      'scope':'finite exact algebra; no numerical infinite Schwartz sum'},
                     sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
