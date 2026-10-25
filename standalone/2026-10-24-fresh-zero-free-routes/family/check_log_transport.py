#!/usr/bin/env python3
"""Exact finite coefficient checks, not an analytic zero-free certificate.

Formal monomials in log(prime) are used; no logarithms are rounded.
"""
import json
from collections import defaultdict
from itertools import combinations


def factor(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mobius(n):
    fs = factor(n)
    if any(e > 1 for e in fs.values()):
        return 0
    return (-1) ** len(fs)


def divisors(n):
    out = [1]
    for p, e in factor(n).items():
        out = [d * p**j for d in out for j in range(e + 1)]
    return out


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(*ps):
    out = defaultdict(int)
    for p in ps:
        for m, c in p.items():
            out[m] += c
    return clean(out)


def scale(p, c):
    return clean({m: c * a for m, a in p.items()})


def mul(a, b):
    out = defaultdict(int)
    for ma, ca in a.items():
        for mb, cb in b.items():
            out[tuple(sorted(ma + mb))] += ca * cb
    return clean(out)


def power(a, k):
    out = {(): 1}
    for _ in range(k):
        out = mul(out, a)
    return out


def logarithm(n):
    return {(p,): e for p, e in factor(n).items()}


def lambda_j(n, j):
    fs = factor(n)
    if len(fs) != 1:
        return {}
    p, e = next(iter(fs.items()))
    return {(p,) * (j + 1): e**j}


def convolution(a, b, n):
    return add(*(mul(a(d), b(n // d)) for d in divisors(n)))


def require_equal(a, b, context):
    if a != b:
        raise RuntimeError(f"Failed {context}: {a!r} != {b!r}")


def main():
    limit = 512
    lam = lambda n: lambda_j(n, 0)
    lam1 = lambda n: lambda_j(n, 1)
    lam2 = lambda n: lambda_j(n, 2)
    lam_sq = lambda n: convolution(lam, lam, n)
    lam_cube = lambda n: convolution(lam_sq, lam, n)
    lam_lam1 = lambda n: convolution(lam, lam1, n)
    kernels = [
        lambda n: scale(lam(n), -1),
        lambda n: add(lam_sq(n), scale(lam1(n), -1)),
        lambda n: add(scale(lam_cube(n), -1),
                      scale(lam_lam1(n), 3), scale(lam2(n), -1)),
    ]
    checked = 0
    for n in range(1, limit + 1):
        for k, kernel in enumerate(kernels, 1):
            expected = scale(power(logarithm(n), k), mobius(n))
            actual = add(*(scale(kernel(n // d), mobius(d))
                           for d in divisors(n)))
            require_equal(expected, actual, ("logarithmic", n, k))
            checked += 1

    # Independently test squarefree/rough splitting, including repeated primes.
    splitting = 0
    for cutoff in (2, 3, 5, 7, 11):
        for n in range(1, limit + 1):
            actual = 0
            for d in divisors(n):
                if any(p > cutoff for p in factor(d)):
                    continue
                if any(p <= cutoff for p in factor(n // d)):
                    continue
                actual += mobius(d) * mobius(n // d)
            require_equal(mobius(n), actual, ("rough split", n, cutoff))
            splitting += 1

    # A real completely multiplicative character with natural nonunit zeros.
    def psi(n):
        return (0, 1, -1, -1, 1)[n % 5]

    multiplicativity = 0
    nonunit = 0
    for n in range(1, limit + 1):
        for d in divisors(n):
            require_equal(psi(n), psi(d) * psi(n // d), ("character", n, d))
            multiplicativity += 1
            nonunit += psi(n) == 0

    # Explicit negative control: dropping the p^2 term must fail at n=p^2.
    rejected_prime_only = 0
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        n = p * p
        false_rhs = scale({(p,): 1}, -mobius(p))
        if false_rhs == scale(logarithm(n), mobius(n)):
            raise RuntimeError("Prime-only negative control was not rejected")
        require_equal(false_rhs, {(p,): 1}, ("prime-only sign", p))
        rejected_prime_only += 1

    print(json.dumps({
        "status": "PASS",
        "integer_limit": limit,
        "formal_logarithmic_coefficients": checked,
        "rough_splitting_coefficients": splitting,
        "zero_extended_character_products": multiplicativity,
        "nonunit_products_included": nonunit,
        "prime_only_mutations_rejected": rejected_prime_only,
        "scope": "Exact finite coefficient identities only; no analytic moment or zero-free certificate.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
