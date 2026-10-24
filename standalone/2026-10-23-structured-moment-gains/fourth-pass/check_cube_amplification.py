#!/usr/bin/env python3
"""Exact finite formal checks for the cube-amplification identity.

This checks a finite reciprocity model, not primitive Gauss sums or an
analytic estimate.  Arithmetic is exact in Z[omega], omega^2+omega+1=0.
The square-root norm factors are checked by their multiplicative identity;
the displayed sum is the equivalent unnormalized coefficient identity.
"""

from itertools import product
from math import prod
import json


ROOTS = ((1, 0), (0, 1), (-1, -1))
ZERO = (0, 0)
ONE = (1, 0)
NORMS = (7, 7, 13)
RAY = (1, 2, 1)
RECIPROCITY = ((0, 1, 2), (1, 0, 1), (2, 1, 0))
PRIME_GAUSS = (2, 1, 2)
SF = list(product((0, 1), repeat=3))


def demand(condition, message):
    if not condition:
        raise AssertionError(message)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]-a[1]*b[1]


def scale(a, n):
    return a[0]*n, a[1]*n


def norm(a):
    return prod(q**e for q, e in zip(NORMS, a))


def mobius(a):
    return 0 if max(a, default=0) > 1 else (-1)**sum(a)


def theta(a):
    return ROOTS[sum(e*t for e, t in zip(a, RAY)) % 3]


def gauss(a):
    exponent = sum(e*t for e, t in zip(a, PRIME_GAUSS))
    exponent -= sum(RECIPROCITY[i][j]*a[i]*a[j]
                    for i in range(3) for j in range(i+1, 3))
    return ROOTS[exponent % 3]


def conjugate_symbol(column, row):
    if any(a and b for a, b in zip(column, row)):
        return ZERO
    exponent = sum(RECIPROCITY[i][j]*column[i]*row[j]
                   for i in range(3) for j in range(3))
    return ROOTS[-exponent % 3]


def column_term(n, h, puncture):
    if any(n[i] and (puncture >> i) & 1 for i in range(3)):
        return ZERO
    return scale(mul(mul(theta(n), gauss(n)), conjugate_symbol(n, h)), mobius(n))


def main():
    multiplicativity_checks = 0
    for a in SF:
        for b in SF:
            if any(x and y for x, y in zip(a, b)):
                continue
            ab = tuple(x+y for x, y in zip(a, b))
            demand(gauss(ab) == mul(mul(gauss(a), gauss(b)), conjugate_symbol(b, a)),
                   "Gauss reciprocity factor")
            demand(norm(ab) == norm(a)*norm(b), "normalizing norm factors")
            multiplicativity_checks += 1

    # Arbitrary whole-index weights ensure the check is not an artifact of
    # a constant profile.  Equal norms of distinct primes are intentional.
    weight = {n: 3 + 2*n[0] - 5*n[1] + 7*n[2] + norm(n) % 11 for n in SF}
    amplification_checks = 0
    omitted_divisor_failures = 0
    fibre = {}
    for h in product(range(4), repeat=3):
        for c in product(range(3), repeat=3):
            divisors = [d for d in SF if all(not d[i] or c[i] for i in range(3))]
            for puncture in (0, 1, 3, 7):
                left = ZERO
                right = ZERO
                wrong = ZERO
                for n in SF:
                    left = add(left, scale(column_term(n, h, puncture), weight[n]))
                for d in divisors:
                    if any(d[i] and (puncture >> i) & 1 for i in range(3)):
                        continue
                    outer = scale(mul(mul(theta(d), gauss(d)),
                                      conjugate_symbol(d, h)), mobius(d))
                    k = tuple(h[i]+d[i]+3*c[i] for i in range(3))
                    wrong_k = tuple(h[i]+3*c[i] for i in range(3))
                    for n in SF:
                        dn = tuple(d[i]+n[i] for i in range(3))
                        if dn not in weight:
                            continue
                        right = add(right, scale(mul(outer, column_term(n, k, puncture)), weight[dn]))
                        wrong = add(wrong, scale(mul(outer, column_term(n, wrong_k, puncture)), weight[dn]))
                demand(left == right, "complete cube amplification with natural zeros")
                amplification_checks += 1
                omitted_divisor_failures += wrong != left
            for d in divisors:
                k = tuple(h[i]+d[i]+3*c[i] for i in range(3))
                fibre[k] = fibre.get(k, 0) + 1

    for k, multiplicity in fibre.items():
        demand(multiplicity <= prod(e+1 for e in k)**2,
               "divisor-square upper bound for the full h,d,c fibre")
    demand(omitted_divisor_failures > 0, "check detects the missing Gauss divisor")

    print(json.dumps({
        "arithmetic": "EXACT_INTEGER_Z_OMEGA_FORMAL_RECIPROCITY_MODEL",
        "primitive_gauss_certification": False,
        "analytic_certification": False,
        "formal_prime_norms": NORMS,
        "multiplicativity_checks": multiplicativity_checks,
        "amplification_checks": amplification_checks,
        "fibre_checks": len(fibre),
        "missing_divisor_rejections": omitted_divisor_failures,
        "scope": "Finite exact identity, zero masks, and fibre count; no asymptotic or zero-free claim"
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
