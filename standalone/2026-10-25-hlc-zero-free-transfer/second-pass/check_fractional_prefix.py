#!/usr/bin/env python3
"""Exact rational checks of the growing-prime coefficient convolution.

This checks finite integer algebra. It does not check the imported family
moment estimate or infer an all-scale bound from computed values.
"""
from fractions import Fraction
import json
from math import comb


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def factor(n):
    ans = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            ans[p] = ans.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def divisors(n):
    ans = [1]
    for p, e in factor(n).items():
        ans = [d * p**j for d in ans for j in range(e + 1)]
    return ans


def squarefree(n):
    return all(e == 1 for e in factor(n).values())


def target(n, cutoff, z, anchor=Fraction(1)):
    ff = factor(n)
    if any(e > 1 for e in ff.values()):
        return Fraction(0)
    out = Fraction(1)
    for p in ff:
        out *= z if p <= cutoff else anchor
    return out


def correction(n, cutoff, z, anchor=Fraction(1)):
    out = Fraction(1)
    for p, e in factor(n).items():
        if p > cutoff:
            return Fraction(0)
        out *= (z - anchor) * (-anchor) ** (e - 1)
    return out


def anchor_coeff(n, anchor):
    ff = factor(n)
    if any(e > 1 for e in ff.values()):
        return Fraction(0)
    return anchor ** len(ff)


def main():
    limit = 800
    params = [Fraction(-1), Fraction(0), Fraction(1, 2),
              Fraction(1), Fraction(3, 2)]
    cutoffs = [2, 5, 11, 29]
    count = 0
    for anchor in [Fraction(1), Fraction(-1), Fraction(1, 2)]:
        for cutoff in cutoffs:
            for z in params:
                for n in range(1, limit + 1):
                    actual = sum((correction(d, cutoff, z, anchor)
                                  * anchor_coeff(n // d, anchor)
                                  for d in divisors(n)), Fraction(0))
                    expected = target(n, cutoff, z, anchor)
                    require(actual == expected,
                            f"convolution mismatch {anchor=} {cutoff=} {z=} {n=}")
                    count += 1

    # At a changed prime square, retaining b(p^2) is indispensable.
    p, z = 5, Fraction(-1)
    full = sum((correction(d, 5, z) * anchor_coeff(p*p // d, Fraction(1))
                for d in divisors(p*p)), Fraction(0))
    truncated = sum((correction(d, 5, z) * anchor_coeff(p*p // d, Fraction(1))
                     for d in divisors(p*p) if squarefree(d)), Fraction(0))
    require(full == 0 and truncated != 0, "prime-power negative control failed")

    # Verify local series products through degree 20 with exact rational values.
    local_count = 0
    for anchor in [Fraction(1), Fraction(-1), Fraction(1, 2)]:
        for z in params:
            coeff = [Fraction(1)] + [
                (z - anchor) * (-anchor)**(j-1) for j in range(1, 21)]
            product = [coeff[0]] + [coeff[j] + anchor * coeff[j-1]
                                     for j in range(1, 21)]
            require(product[1] == z and all(c == 0 for c in product[2:]),
                    "local Euler series mismatch")
            local_count += 1

    # Exact algebraic form of the feedback gap avoids floating square roots:
    # E(r)-baseline = 5/2 + 5r/3 - (10/sqrt(6))*sqrt(r).
    # Substituting r=3*t^2/2 yields (5/2)*(t-1)^2.
    for t in [Fraction(4, 5), Fraction(5, 6), Fraction(9, 10), Fraction(1)]:
        r = Fraction(3, 2) * t*t
        gap = Fraction(5, 2) + Fraction(5, 3)*r - 5*t
        require(gap == Fraction(5, 2)*(t-1)**2, "feedback gap identity failed")

    mark_cases = 0
    for cutoff in [5, 29]:
        for k in range(7):
            for n in range(1, limit + 1):
                omega = sum(p <= cutoff for p in factor(n))
                expected = comb(omega, k) if squarefree(n) and k <= omega else 0
                actual = 0
                for d in divisors(n):
                    ff = factor(d)
                    if len(ff) == k and all(p <= cutoff for p in ff):
                        actual += (-1)**(sum(ff.values()) - len(ff)) * squarefree(n // d)
                require(actual == expected,
                        f"binomial mark convolution mismatch {cutoff=} {k=} {n=}")
                mark_cases += 1
    print(json.dumps({
        "status": "pass", "arithmetic": "exact rational",
        "integer_convolution_cases": count,
        "local_series_cases": local_count,
        "local_series_degree": 20,
        "binomial_mark_convolution_cases": mark_cases,
        "negative_control": "dropping repeated-prime correction fails at n=25",
        "scope": "finite coefficient algebra only; no asymptotic moment verification"
    }, indent=2))


if __name__ == "__main__":
    main()
