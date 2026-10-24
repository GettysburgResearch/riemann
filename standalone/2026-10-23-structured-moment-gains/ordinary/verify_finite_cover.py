#!/usr/bin/env python3
"""Exact finite algebra, not an analytic or zero-free theorem checker."""
from fractions import Fraction as F
from itertools import product
from math import prod
import json


def demand(value, label):
    if not value:
        raise RuntimeError(label)


def norm(mask, qs):
    return prod(q for i, q in enumerate(qs) if mask >> i & 1)


def monomial(mask, atom):
    return int(mask & atom == mask)


def centered(mask, atom, deltas):
    return prod((F((atom >> i) & 1) - d)
                for i, d in enumerate(deltas) if mask >> i & 1)


def mu(mask):
    return (-1) ** mask.bit_count()


def main():
    checks = 0
    # Enumerate the primitive projective representatives modulo p^2.
    # For split Gaussian primes the local ring is Z/p^2Z.
    for p in [5, 13, 17]:
        mod = p * p
        reps = [(1, t) for t in range(mod)] + [(p*t, 1) for t in range(p)]
        demand(len(reps) == p*p+p, "projective cardinality")
        demand(sum(c == 0 for c, b in reps) == 1, "distinguished incidence")
        primitive = [(c, b) for c in range(mod) for b in range(mod)
                     if c % p or b % p]
        actual = set()
        for c, b in primitive:
            if c % p:
                actual.add((1, b * pow(c, -1, mod) % mod))
            else:
                actual.add((c * pow(b, -1, mod) % mod, 1))
        demand(actual == set(reps), "all primitive rows represented")
        checks += 3

    # Distinct good Gaussian prime ideals may have the same norm.
    qs = [5, 5, 9, 13]
    deltas = [F(1, q*(q+1)) for q in qs]
    masks = list(range(1 << len(qs)))
    weights = {atom: prod(d if atom >> i & 1 else 1-d
                          for i, d in enumerate(deltas)) for atom in masks}
    demand(sum(weights.values()) == 1, "probability mass")
    checks += 1

    def inner(f, g):
        return sum(weights[a] * f(a) * g(a) for a in masks)

    for d in masks:
        for e in masks:
            gram = inner(lambda a: monomial(d, a), lambda a: monomial(e, a))
            target = prod(x for i, x in enumerate(deltas) if (d | e) >> i & 1)
            demand(gram == target, "primitive Gram kernel")
            got = inner(lambda a: centered(d, a, deltas),
                        lambda a: centered(e, a, deltas))
            expected = (prod(x*(1-x) for i, x in enumerate(deltas)
                             if d >> i & 1) if d == e else F(0))
            demand(got == expected, "orthogonal basis from atom enumeration")
            checks += 2

    rows = []
    for cutoff in [1, 4, 5, 8, 9, 13, 25, 45, 65, 117, 225, 325, 585, 2925]:
        active = [m for m in masks if norm(m, qs) <= cutoff]
        x0 = masks[-1]
        def sieve(atom):
            return sum(mu(m)*monomial(m, atom) for m in active)
        def full(atom):
            return int(atom == 0)
        def riesz(atom):
            return sum(F(centered(m, x0, deltas)*centered(m, atom, deltas)) /
                       prod(d*(1-d) for i, d in enumerate(deltas) if m >> i & 1)
                       for m in active)
        explicit = sum(prod(q*(q+1)-1 for i, q in enumerate(qs) if m >> i & 1)
                       for m in active)
        demand(inner(riesz, riesz) == explicit, "Riesz norm by atom enumeration")
        demand(riesz(x0) == explicit, "Riesz evaluation")
        for m in active:
            demand(inner(riesz, lambda a: monomial(m, a)) == 1,
                   "Riesz represents literal evaluation")
            checks += 1
        demand(sieve(x0) == sum(mu(m) for m in active), "literal Mobius evaluation")
        selected = [i for i, q in enumerate(qs) if q*q > cutoff and q <= cutoff]
        bad_atom = sum(1 << i for i in selected)
        demand(sieve(bad_atom) == 1-len(selected), "arbitrary coset exact prime count")
        sieve_sq = inner(sieve, sieve)
        bound = prod(1+3*d for d in deltas)
        demand(sieve_sq <= bound, "uniform sieve norm")
        tail_sq = inner(lambda a: full(a)-sieve(a),
                        lambda a: full(a)-sieve(a))
        demand(tail_sq <= F(96, cutoff), "uniform explicit tail bound")
        checks += 6
        rows.append({"R": cutoff, "dimension": len(active),
                     "evaluation_norm_squared": str(explicit),
                     "sieve_norm_squared": str(sieve_sq),
                     "tail_norm_squared": str(tail_sq)})

    # Independently multiply local formal power series: mu*h = a.
    for q in [5, 9, 13]:
        for z in [F(1, q), F(1, q+1), F(2, q)]:
            c = (1-F(1, q))/(1-z)
            hs = [F(1)] + [1-c]*5
            convolution = [hs[0]] + [hs[k]-hs[k-1] for k in range(1, 6)]
            demand(convolution == [1, -c, 0, 0, 0, 0], "cusp Euler convolution")
            checks += 1

    # Deliberately wrong Haar normalization and missing delta are rejected.
    q = 5
    d = F(1, q*(q+1))
    true_sq = inner(lambda a: monomial(1, a), lambda a: monomial(1, a))
    demand(true_sq != 1, "reject counting/Haar confusion")
    demand((1-d)/d != (1-d), "reject missing evaluation factor")
    checks += 2
    print(json.dumps({"arithmetic": "EXACT_RATIONAL", "checks": checks,
                      "analytic_certification": False,
                      "finite_prime_norms": qs, "rows": rows},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
