#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import isqrt, prod
import json
from pathlib import Path


PRIMES79 = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
    37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
)
P79 = prod(PRIMES79)
RADICAL_SCALE = 10**40

EXPECTED_A83 = Fraction(
    -1401629533229069216211617003,
    107254825578022430263302818471,
)
EXPECTED_GAP = Fraction(
    -223590076836035175208867029720,
    8902150522975861711854133933093,
)
EXPECTED_GLOBAL_MAX = Fraction(
    52541123207025505248824623351,
    292513160667333900718098595830,
)


def divisors_capped(cap: int) -> list[tuple[int, int]]:
    values: list[tuple[int, int]] = [(1, 1)]
    for prime in PRIMES79:
        values += [
            (divisor * prime, -mu)
            for divisor, mu in values
            if divisor * prime <= cap
        ]
    values.sort()
    return values


def all_divisors() -> list[tuple[int, int]]:
    values: list[tuple[int, int]] = [(1, 1)]
    for prime in PRIMES79:
        values += [(divisor * prime, -mu) for divisor, mu in values]
    values.sort()
    return values


def prefix_a(cap: int) -> Fraction:
    return sum(
        (Fraction(mu, divisor) for divisor, mu in divisors_capped(cap)),
        Fraction(0),
    )


def sqrt_interval(integer: int) -> tuple[Fraction, Fraction]:
    root = isqrt(integer * RADICAL_SCALE * RADICAL_SCALE)
    lower = Fraction(root, RADICAL_SCALE)
    upper = (
        lower
        if root * root == integer * RADICAL_SCALE * RADICAL_SCALE
        else Fraction(root + 1, RADICAL_SCALE)
    )
    return lower, upper


def reciprocal_sqrt_interval(integer: int) -> tuple[Fraction, Fraction]:
    lower, upper = sqrt_interval(integer)
    return Fraction(1, upper), Fraction(1, lower)


def add_interval(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    return left[0] + right[0], left[1] + right[1]


def scale_interval(
    scalar: Fraction,
    interval: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    if scalar >= 0:
        return scalar * interval[0], scalar * interval[1]
    return scalar * interval[1], scalar * interval[0]


def log_lower_atanh(value: Fraction, terms: int) -> Fraction:
    """Exact lower bound: log x = 2 sum z^(2k+1)/(2k+1), z=(x-1)/(x+1)."""
    if value < 1:
        raise ValueError("value must be at least one")
    if value == 1:
        return Fraction(0)
    z = (value - 1) / (value + 1)
    partial = sum(
        (z ** (2 * index + 1) / Fraction(2 * index + 1) for index in range(terms)),
        Fraction(0),
    )
    return 2 * partial


def certify_first_cell() -> dict[str, object]:
    divisors_83 = divisors_capped(83)
    a83 = sum(
        (Fraction(mu, divisor) for divisor, mu in divisors_83),
        Fraction(0),
    )
    assert len(divisors_83) == 51
    assert a83 == EXPECTED_A83
    assert a83 < 0

    gap = a83 - Fraction(1, 83)
    assert gap == EXPECTED_GAP
    assert gap < 0

    a105 = prefix_a(105)
    assert a105 > Fraction(1, 25)

    sqrt_83 = sqrt_interval(83)
    target = (Fraction(0), Fraction(0))
    for divisor, mu in divisors_83:
        atom = add_interval(
            scale_interval(Fraction(4, divisor), sqrt_83),
            scale_interval(Fraction(-3), reciprocal_sqrt_interval(divisor)),
        )
        target = add_interval(target, scale_interval(Fraction(mu), atom))

    # The terminal child target at y=1 equals one, scaled by 1/sqrt(83).
    target = add_interval(
        target,
        scale_interval(Fraction(-1), reciprocal_sqrt_interval(83)),
    )
    assert target[0] > 0
    assert target[1] < Fraction(1813, 1000)

    # Exact rational logarithmic lower bounds.
    log_2_lower = log_lower_atanh(Fraction(2), 4)
    log_83_over_64_lower = log_lower_atanh(Fraction(83, 64), 2)
    assert log_2_lower > Fraction(6931, 10000)
    assert log_83_over_64_lower > Fraction(2599, 10000)

    # log(83/2) = 5 log 2 + log(83/64).
    log_83_over_2_lower = (
        5 * Fraction(6931, 10000) + Fraction(2599, 10000)
    )

    # 1/sqrt(2) > 707/1000, certified by squaring.
    assert 2 * 707 * 707 < 1000 * 1000
    entropy_n2_lower = (
        Fraction(6931, 10000)
        * log_83_over_2_lower
        * Fraction(707, 1000)
    )
    assert entropy_n2_lower > Fraction(1825, 1000)
    assert entropy_n2_lower > target[1]

    return {
        "A_P79_83": str(a83),
        "A_P79_105": str(a105),
        "divisors_through_83": len(divisors_83),
        "entropy_n2_lower": str(entropy_n2_lower),
        "entropy_n2_lower_decimal": f"{float(entropy_n2_lower):.15f}",
        "score_minus_target_coefficient": str(gap),
        "score_minus_target_sign": "negative",
        "target_lower_decimal": f"{float(target[0]):.15f}",
        "target_upper_decimal": f"{float(target[1]):.15f}",
        "target_upper_lt": "1813/1000",
    }


def certify_global_prefix_upper() -> dict[str, object]:
    divisors = all_divisors()
    assert len(divisors) == 2 ** len(PRIMES79)

    numerator = 0
    maximum: tuple[int, int] | None = None
    for divisor, mu in divisors:
        numerator += mu * (P79 // divisor)
        if divisor >= 83 and (maximum is None or numerator > maximum[0]):
            maximum = numerator, divisor

    assert maximum is not None
    maximum_fraction = Fraction(maximum[0], P79)
    assert maximum[1] == 221
    assert maximum_fraction == EXPECTED_GLOBAL_MAX
    assert maximum_fraction < Fraction(1, 5)

    return {
        "activation_states": len(divisors),
        "global_A_P79_max": str(maximum_fraction),
        "global_A_P79_max_activation": maximum[1],
        "global_A_P79_upper": "1/5",
    }


def main() -> None:
    result = {
        "classification": "PASS_P79_FIRST_CELL_SCORE_REFUTATION_AND_ENTROPY_REPAIR",
        "first_cell": certify_first_cell(),
        "global_prefix": certify_global_prefix_upper(),
        "scope": (
            "Exact Fraction enumeration of the first P79 splice cell and every "
            "P79 reciprocal-prefix activation; directed rational radical bounds "
            "for the residual target; and exact atanh lower bounds showing that "
            "the single n=2 physical-entropy atom exceeds that target. The replay "
            "does not prove the all-parameter physical-score recurrence or RH."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
