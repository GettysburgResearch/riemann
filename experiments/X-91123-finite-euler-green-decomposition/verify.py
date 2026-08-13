#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import gcd
import json
from pathlib import Path


def divisors_with_mu(primes):
    values = [(1, 1)]
    for prime in primes:
        values += [(d * prime, -mu) for d, mu in list(values)]
    return sorted(values)


def direct_dictionary(primes, row, maximum):
    """Coefficient of each formal symbol ell_x(k)."""
    a = Fraction(row + 1, row - 1)
    b = -Fraction((row + 1) * (row - 2), row * (row - 1))
    c = Fraction(2, row * (row - 1))
    out = {k: Fraction(0) for k in range(1, maximum + 1)}

    for divisor, mu in divisors_with_mu(primes):
        if divisor * row <= maximum:
            out[divisor * row] += mu * a
        if divisor * (row + 1) <= maximum:
            out[divisor * (row + 1)] += mu * b
        first = divisor * (row + 2)
        if first <= maximum:
            for multiple in range(first, maximum + 1, divisor):
                out[multiple] += mu * c
    return out


def green_dictionary(primes, row, maximum):
    mu_map = dict(divisors_with_mu(primes))
    product = 1
    for prime in primes:
        product *= prime

    c = Fraction(2, row * (row - 1))
    left = Fraction(row + 2, row)
    out = {}
    for k in range(1, maximum + 1):
        coefficient = c if gcd(k, product) == 1 else Fraction(0)

        # The full rough tail includes every quotient m.  The actual component
        # row has zero coefficient for m<row, so these sectors must be removed.
        for m in range(1, row):
            if k % m == 0 and k // m in mu_map:
                coefficient -= c * mu_map[k // m]

        if k % row == 0 and k // row in mu_map:
            coefficient += left * mu_map[k // row]
        if k % (row + 1) == 0 and k // (row + 1) in mu_map:
            coefficient -= mu_map[k // (row + 1)]
        out[k] = coefficient
    return out


def adjoin_prime_dictionary(parent_dictionary, prime, maximum):
    """Formal identity E_(P union {p}) = E_P - p^-1/2 S_p E_P.

    The factor p^-1/2 turns ell_(x/p)(k) into ell_x(pk), so no radicals
    remain in the formal coefficient dictionary.
    """
    out = dict(parent_dictionary)
    for k, coefficient in parent_dictionary.items():
        if prime * k <= maximum:
            out[prime * k] = out.get(prime * k, Fraction(0)) - coefficient
    return out


def certify():
    checks = 0
    for primes in ([2, 3], [2, 3, 5], [2, 3, 5, 7]):
        for row in range(2, 13):
            maximum = 900
            direct = direct_dictionary(primes, row, maximum)
            green = green_dictionary(primes, row, maximum)
            assert direct == green, (primes, row)
            checks += maximum

            new_prime = 11 if 11 not in primes else 13
            direct_enlarged = direct_dictionary(
                list(primes) + [new_prime], row, maximum
            )
            renewed = adjoin_prime_dictionary(direct, new_prime, maximum)
            assert direct_enlarged == renewed, (primes, row, new_prime)
            checks += maximum

    # Coefficientwise positivity of the rough Green difference: parent rough
    # symbols at pk cancel the shifted child symbols; all other parent symbols
    # remain with coefficient one.
    for prime in (11, 13, 17):
        maximum = 2000
        parent = {
            k: Fraction(1)
            for k in range(1, maximum + 1)
            if gcd(k, 2 * 3 * 5 * 7) == 1
        }
        difference = dict(parent)
        for k, coefficient in parent.items():
            if prime * k <= maximum:
                difference[prime * k] = (
                    difference.get(prime * k, Fraction(0)) - coefficient
                )
        assert all(value >= 0 for value in difference.values())
        checks += len(difference)

    result = {
        "classification": "PASS_FINITE_EULER_GREEN_DECOMPOSITION",
        "formal_coefficient_checks": checks,
        "prime_sets": [[2, 3], [2, 3, 5], [2, 3, 5, 7]],
        "rows": "2..12",
        "scope": (
            "Exact Fraction arithmetic verifies the complete finite-boundary "
            "coefficient dictionary, the one-new-prime renewal identity, and "
            "coefficientwise positivity of the rough Green bulk. It does not "
            "certify the P_79 finite-boundary inequality or RH."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    certify()
