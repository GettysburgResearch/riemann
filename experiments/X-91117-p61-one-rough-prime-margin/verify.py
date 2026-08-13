#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import isqrt, prod
import json
from pathlib import Path

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
P = prod(PRIMES)
DEN = 10**50
FIRST_ROUGH = 67


def generate_divisors():
    values = [(1, 1)]
    for prime in PRIMES:
        values += [(d * prime, -sign) for d, sign in list(values)]
    return sorted(values)


def invsqrt_interval_num(value):
    if value == 1:
        return DEN, DEN
    lower = isqrt((DEN * DEN) // value)
    return lower, lower + 1


def maximum_product(lower_a, upper_a, lower_b, upper_b):
    return max(
        lower_a * lower_b,
        lower_a * upper_b,
        upper_a * lower_b,
        upper_a * upper_b,
    )


def certify_gate(channel, a_numerator, b_lower, b_upper, x, gate):
    inv_lower, inv_upper = invsqrt_interval_num(x)
    product_upper = maximum_product(
        b_lower, b_upper, inv_lower, inv_upper
    )
    return (
        channel * a_numerator * DEN * DEN
        - gate * P * DEN * DEN
        - P * product_upper
    )


def certify():
    divisors = generate_divisors()
    assert len(divisors) == 2**len(PRIMES)

    gates = {1: Fraction(3, 40), 2: Fraction(9, 100)}
    a_numerator = 0
    b_lower = 0
    b_upper = 0
    checks = 0
    minimum_margin = {1: None, 2: None}

    for index, (divisor, sign) in enumerate(divisors):
        a_numerator += sign * (P // divisor)
        lower, upper = invsqrt_interval_num(divisor)
        if sign == 1:
            b_lower += lower
            b_upper += upper
        else:
            b_lower -= upper
            b_upper -= lower

        right = divisors[index + 1][0] if index + 1 < len(divisors) else None
        start = max(divisor, FIRST_ROUGH)
        points = []

        if right is None:
            points.append(start)
        elif start < right:
            points.extend((start, right))

        for x in points:
            for channel in (1, 2):
                numerator = certify_gate(
                    channel,
                    a_numerator,
                    b_lower,
                    b_upper,
                    x,
                    gates[channel],
                )
                assert numerator > 0, (
                    index, divisor, right, x, channel, numerator
                )
                margin = Fraction(numerator, P * DEN * DEN)
                record = (margin, x, divisor, right)
                if (
                    minimum_margin[channel] is None
                    or record[0] < minimum_margin[channel][0]
                ):
                    minimum_margin[channel] = record
                checks += 1

        if right is None:
            for channel in (1, 2):
                assert Fraction(channel * a_numerator, P) > gates[channel]

    assert Fraction(3, 40) - Fraction(1, 67) > Fraction(3, 50)
    assert Fraction(9, 100) - Fraction(2, 67) > Fraction(3, 50)

    return {
        "classification": "PASS_P61_ONE_ROUGH_PRIME_MARGIN",
        "small_primes": PRIMES,
        "first_rough_prime": FIRST_ROUGH,
        "divisor_cells": len(divisors),
        "directed_endpoint_channel_checks": checks,
        "normalized_gates": {
            "reserve": "3/40",
            "equality": "9/100",
        },
        "minimum_gate_margins": {
            str(channel): {
                "lower": str(minimum_margin[channel][0]),
                "decimal": float(minimum_margin[channel][0]),
                "x": minimum_margin[channel][1],
                "cell_left": minimum_margin[channel][2],
                "cell_right": minimum_margin[channel][3],
            }
            for channel in (1, 2)
        },
        "one_rough_prime_margin": "3/50",
        "exact_margin_checks": [
            "3/40 - 1/67 > 3/50",
            "9/100 - 2/67 > 3/50",
        ],
        "scope": (
            "All forcing gates use exact integer/Fraction arithmetic and "
            "directed fixed-denominator inverse-square-root enclosures. "
            "The theorem concerns one new least rough prime per reset; it "
            "does not assert scalar tensorization over distinct rough primes."
        ),
    }


if __name__ == "__main__":
    result = certify()
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)
