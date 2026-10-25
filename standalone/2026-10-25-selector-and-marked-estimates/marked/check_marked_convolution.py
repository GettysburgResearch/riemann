#!/usr/bin/env python3
"""Exact finite identities for the matched marked-count decomposition.

This verifies finite coefficient and finite smoothing identities only.
It does not verify a prime-number-theorem error, contour shift, growing-order
resonance, or new zero-free boundary.
"""
from fractions import Fraction
import json


def data(limit):
    least = [0] * (limit + 1)
    primes = []
    for n in range(2, limit + 1):
        if not least[n]:
            primes.append(n)
            for multiple in range(n, limit + 1, n):
                if not least[multiple]:
                    least[multiple] = n
    squarefree = [1] * (limit + 1)
    omega = [0] * (limit + 1)
    squarefree[0] = 0
    for n in range(2, limit + 1):
        value, last = n, 0
        while value > 1:
            p = least[value]
            value //= p
            if p == last:
                squarefree[n] = 0
            else:
                omega[n] += 1
            last = p
    return primes, squarefree, omega


def profile(x):
    # A rational compact finite test profile. Smoothness is not required for
    # the finite identities tested here; analytic theorems use C_c^infinity.
    if x <= 1 or x >= 2:
        return Fraction(0)
    return (x - 1)**4 * (2 - x)**4


def main():
    limit = 2048
    primes, sq, omega = data(limit)
    kappa = [Fraction(0) for _ in range(limit + 1)]
    correction = [Fraction(0) for _ in range(limit + 1)]
    prime_only = [Fraction(0) for _ in range(limit + 1)]
    powers = []
    for p in primes:
        q, exponent = p, 1
        prime_only[p] = 1
        while q <= limit:
            kappa[q] = Fraction(1, exponent)
            correction[q] = Fraction((-1)**(exponent - 1)) - kappa[q]
            powers.append((p, exponent, q))
            q *= p
            exponent += 1
    convolved = [Fraction(0) for _ in range(limit + 1)]
    incomplete = [Fraction(0) for _ in range(limit + 1)]
    for d in range(2, limit + 1):
        if kappa[d] or correction[d] or prime_only[d]:
            for m in range(1, limit // d + 1):
                convolved[d*m] += sq[m] * (kappa[d] + correction[d])
                incomplete[d*m] += sq[m] * prime_only[d]
    for n in range(1, limit + 1):
        if convolved[n] != sq[n] * omega[n]:
            raise RuntimeError(("coefficient identity failed", n))
    mutation_failures = [
        n for n in range(1, limit + 1)
        if incomplete[n] != sq[n]*omega[n]
    ]
    if 4 not in mutation_failures:
        raise RuntimeError("prime-only mutation was not rejected at 4")

    scales = [Fraction(1, 2), Fraction(3, 4), Fraction(1),
              Fraction(3, 2), Fraction(2), Fraction(5, 2)]
    scales += [Fraction(n) for n in (3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377)]
    receipts = []
    for X in scales:
        direct = sum(Fraction(sq[n]*omega[n])*profile(Fraction(n)/X)
                     for n in range(1, min(limit, int(2*X))+1))
        transformed = Fraction(0)
        punctured = Fraction(0)
        for p, exponent, q in powers:
            if q >= 2*X:
                continue
            S = sum(Fraction(sq[m])*profile(Fraction(m*q)/X)
                    for m in range(1, min(limit, int(2*X/q))+1))
            transformed += (kappa[q]+correction[q])*S
            if exponent == 1:
                punctured += sum(
                    Fraction(sq[m])*profile(Fraction(m*p)/X)
                    for m in range(1, min(limit, int(2*X/p))+1)
                    if m % p
                )
        if transformed != direct or punctured != direct:
            raise RuntimeError(("finite smoothing identity failed", str(X)))
        receipts.append({"X": str(X), "marked_sum_exact": str(direct)})

    result = {
        "status": "EXACT_FINITE_IDENTITIES_PASS",
        "scope": "Finite convolution identities, not analytic asymptotics",
        "coefficient_cases": limit,
        "prime_power_terms_retained": len(powers),
        "prime_only_mutation_failures": len(mutation_failures),
        "first_mutation_failure": mutation_failures[0],
        "finite_profile_cases": len(scales),
        "profile_note": "Rational compact C3 profile used only for finite identities",
        "profile_receipts": receipts,
        "analytic_error_estimate_verified": False,
        "growing_order_resonance_numerically_certified": False,
        "zero_free_boundary_certified": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
