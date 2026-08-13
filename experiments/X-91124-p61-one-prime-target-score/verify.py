#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import prod
import json
from pathlib import Path

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
P61 = prod(PRIMES)


def squarefree_divisors_with_mu():
    values = [(1, 1)]
    for prime in PRIMES:
        values += [(d * prime, -mu) for d, mu in list(values)]
    return sorted(values)


def certify():
    divisors = squarefree_divisors_with_mu()
    assert len(divisors) == 2 ** len(PRIMES)

    prefix_numerator = 0
    maximum = None
    minimum_after_67 = None
    prefix_checks = 0

    for divisor, mu in divisors:
        prefix_numerator += mu * (P61 // divisor)
        prefix_checks += 1

        record = (prefix_numerator, divisor)
        if maximum is None or record[0] > maximum[0]:
            maximum = record
        if divisor >= 67 and (
            minimum_after_67 is None or record[0] < minimum_after_67[0]
        ):
            minimum_after_67 = record

    assert maximum == (P61, 1)
    assert minimum_after_67 == (1926272088479361233555, 70)

    minimum_fraction = Fraction(minimum_after_67[0], P61)
    reduced_minimum = Fraction(
        55036345385124606673,
        3351096610268770599522,
    )
    assert minimum_fraction == reduced_minimum
    assert minimum_fraction > Fraction(16423, 10**6)

    one_prime_gap = minimum_fraction - Fraction(1, 67)
    exact_gap = Fraction(
        336338530534578047569,
        224523472888007630167974,
    )
    assert one_prime_gap == exact_gap
    assert one_prime_gap > Fraction(1498, 10**6)

    # Affine interpolation of the a-channel forcing:
    # 4/3 = (2/3)*1 + (1/3)*2 and
    # 5/3 = (1/3)*1 + (2/3)*2.
    assert Fraction(4, 3) == Fraction(2, 3) + Fraction(2, 3)
    assert Fraction(5, 3) == Fraction(1, 3) + Fraction(4, 3)

    # L-91328 gives F_(a;p)>3/50 sqrt(x) at a=1,2.
    # The target and score are three times the affine values a=4/3,5/3.
    scalar_lower = 3 * Fraction(3, 50)
    assert scalar_lower == Fraction(9, 50)

    result = {
        "classification": "PASS_P61_ONE_PRIME_TARGET_SCORE_SURPLUS",
        "small_primes": PRIMES,
        "divisor_states": len(divisors),
        "product_P61": P61,
        "prefix_checks": prefix_checks,
        "global_prefix_maximum": {
            "numerator": str(maximum[0]),
            "activation_divisor": maximum[1],
            "value": "1",
        },
        "minimum_prefix_for_z_ge_67": {
            "common_numerator": str(minimum_after_67[0]),
            "activation_divisor": minimum_after_67[1],
            "reduced_fraction": str(minimum_fraction),
            "decimal": float(minimum_fraction),
        },
        "one_prime_first_moment_gap": {
            "fraction": str(one_prime_gap),
            "decimal": float(one_prime_gap),
            "certified_above": "1498/1000000",
        },
        "target_and_score_lower_coefficient": "9/50",
        "scope": (
            "Exact integer/Fraction arithmetic certifies every P61 divisor "
            "prefix, the uniform one-prime first-moment gap, and the affine "
            "target/score interpolation. Positivity of the endpoint forcings "
            "at a=1,2 is imported from the directed theorem L-91328. The "
            "finite Green-boundary row inequality and RH remain open."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    certify()
