#!/usr/bin/env python3
from __future__ import annotations

from bisect import bisect_left, bisect_right
from fractions import Fraction
from functools import lru_cache
from math import isqrt, prod
import json
from pathlib import Path


PRIMES79 = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
    37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
)
P79 = prod(PRIMES79)
SCALE = 10**24


def bounded_divisors(limit: int) -> list[tuple[int, int]]:
    values: list[tuple[int, int]] = [(1, 1)]
    for prime in PRIMES79:
        values += [
            (divisor * prime, -mu)
            for divisor, mu in values
            if divisor * prime <= limit
        ]
    values.sort()
    return values


DIVISORS = bounded_divisors(4104)
DIVISORS_82 = [item for item in DIVISORS if item[0] <= 82]
THRESHOLDS = [
    divisor for divisor, mu in DIVISORS
    if mu == -1 and divisor < 4096
]


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [prime for prime in range(83, limit + 1) if sieve[prime]]


ROUGH_PRIMES = prime_sieve(4103)


@lru_cache(None)
def sqrt_fraction_scaled(value: Fraction) -> tuple[int, int]:
    scaled_square = (
        value.numerator * SCALE * SCALE // value.denominator
    )
    lower = isqrt(scaled_square)
    while (
        (lower + 1) * (lower + 1) * value.denominator
        <= value.numerator * SCALE * SCALE
    ):
        lower += 1
    while (
        lower * lower * value.denominator
        > value.numerator * SCALE * SCALE
    ):
        lower -= 1

    exact = (
        lower * lower * value.denominator
        == value.numerator * SCALE * SCALE
    )
    return lower, lower if exact else lower + 1


@lru_cache(None)
def sqrt_integer_scaled(integer: int) -> tuple[int, int]:
    return sqrt_fraction_scaled(Fraction(integer))


@lru_cache(None)
def reciprocal_sqrt_integer_scaled(integer: int) -> tuple[int, int]:
    scaled_square = SCALE * SCALE // integer
    lower = isqrt(scaled_square)
    while (lower + 1) * (lower + 1) * integer <= SCALE * SCALE:
        lower += 1
    while lower * lower * integer > SCALE * SCALE:
        lower -= 1

    exact = lower * lower * integer == SCALE * SCALE
    return lower, lower if exact else lower + 1


def scale_interval(
    scalar: int,
    lower: int,
    upper: int,
) -> tuple[int, int]:
    if scalar >= 0:
        return scalar * lower, scalar * upper
    return scalar * upper, scalar * lower


def multiply_intervals(
    left_lower: int,
    left_upper: int,
    right_lower: int,
    right_upper: int,
) -> tuple[int, int]:
    values = (
        left_lower * right_lower,
        left_lower * right_upper,
        left_upper * right_lower,
        left_upper * right_upper,
    )
    return min(values), max(values)


def build_threshold_data() -> dict[
    int,
    tuple[list[int], list[int], list[int], list[int]],
]:
    result: dict[
        int,
        tuple[list[int], list[int], list[int], list[int]],
    ] = {}

    for threshold in THRESHOLDS:
        selected = [
            (divisor, mu)
            for divisor, mu in DIVISORS
            if (
                (mu == 1 and divisor <= threshold + 8)
                or (mu == -1 and divisor <= threshold)
            )
        ]

        divisors: list[int] = []
        reciprocal_prefix = [0]
        radical_lower_prefix = [0]
        radical_upper_prefix = [0]

        for divisor, mu in selected:
            divisors.append(divisor)
            reciprocal_prefix.append(
                reciprocal_prefix[-1] + mu * (P79 // divisor)
            )

            inverse_lower, inverse_upper = (
                reciprocal_sqrt_integer_scaled(divisor)
            )
            if mu > 0:
                radical_lower_prefix.append(
                    radical_lower_prefix[-1] + inverse_lower
                )
                radical_upper_prefix.append(
                    radical_upper_prefix[-1] + inverse_upper
                )
            else:
                radical_lower_prefix.append(
                    radical_lower_prefix[-1] - inverse_upper
                )
                radical_upper_prefix.append(
                    radical_upper_prefix[-1] - inverse_lower
                )

        result[threshold] = (
            divisors,
            reciprocal_prefix,
            radical_lower_prefix,
            radical_upper_prefix,
        )

    return result


THRESHOLD_DATA = build_threshold_data()


def prefix(
    threshold: int,
    cutoff: Fraction,
    include_cutoff: bool,
) -> tuple[int, int, int]:
    divisors, reciprocal, radical_lower, radical_upper = (
        THRESHOLD_DATA[threshold]
    )
    index = (
        bisect_right(divisors, cutoff)
        if include_cutoff
        else bisect_left(divisors, cutoff)
    )
    return reciprocal[index], radical_lower[index], radical_upper[index]


def hall_state_lowers(
    threshold: int,
    prime: int,
    y: Fraction,
    include_child: bool,
    include_parent: bool,
) -> tuple[int, int]:
    """Return lower numerators for H_4 and H_5.

    The common denominator is SCALE^2 * P79.
    """
    y_sqrt_lower, y_sqrt_upper = sqrt_fraction_scaled(y)
    p_sqrt_lower, p_sqrt_upper = sqrt_integer_scaled(prime)
    p_inverse_lower, p_inverse_upper = (
        reciprocal_sqrt_integer_scaled(prime)
    )

    parent_a, parent_b_lower, parent_b_upper = prefix(
        threshold,
        Fraction(prime) * y,
        include_parent,
    )
    child_a, child_b_lower, child_b_upper = prefix(
        threshold,
        y,
        include_child,
    )

    parent_slope_lower, parent_slope_upper = scale_interval(
        parent_a,
        p_sqrt_lower,
        p_sqrt_upper,
    )
    child_slope_lower, child_slope_upper = scale_interval(
        child_a,
        p_inverse_lower,
        p_inverse_upper,
    )
    slope_lower = parent_slope_lower - child_slope_upper
    slope_upper = parent_slope_upper - child_slope_lower

    weighted_slope_lower, _weighted_slope_upper = multiply_intervals(
        y_sqrt_lower,
        y_sqrt_upper,
        slope_lower,
        slope_upper,
    )

    constant_lower = -3 * parent_b_upper * SCALE * P79
    inverse_child_lower, _inverse_child_upper = multiply_intervals(
        p_inverse_lower,
        p_inverse_upper,
        child_b_lower,
        child_b_upper,
    )
    constant_lower += 3 * inverse_child_lower * P79

    return (
        4 * weighted_slope_lower + constant_lower,
        5 * weighted_slope_lower + constant_lower,
    )


def child_state_lowers(
    threshold: int,
    y: Fraction,
    include_child: bool,
) -> tuple[int, int]:
    """Return lower numerators for child target/score margins.

    The common denominator is SCALE * P79.
    """
    y_sqrt_lower, y_sqrt_upper = sqrt_fraction_scaled(y)
    child_a, child_b_lower, child_b_upper = prefix(
        threshold,
        y,
        include_child,
    )
    weighted_lower, _weighted_upper = scale_interval(
        child_a,
        y_sqrt_lower,
        y_sqrt_upper,
    )
    constant_lower = -3 * child_b_upper * P79
    return (
        4 * weighted_lower + constant_lower,
        5 * weighted_lower + constant_lower,
    )


CHILD_POINTS = sorted(
    {Fraction(1), Fraction(83)}
    | {
        Fraction(divisor)
        for divisor, _mu in DIVISORS_82
        if 1 < divisor < 83
    }
)


def positive_parent_activations(threshold: int) -> list[int]:
    return [
        divisor
        for divisor, mu in DIVISORS
        if mu == 1 and threshold < divisor <= threshold + 8
    ]


def prime_cases(threshold: int) -> tuple[list[int], int]:
    tail_boundary = max(83, threshold + 8)
    finite_primes = [
        prime for prime in ROUGH_PRIMES if prime < tail_boundary
    ]
    return finite_primes, tail_boundary


def real_breakpoints(threshold: int, prime: int) -> list[Fraction]:
    lower = max(Fraction(1), Fraction(threshold, prime))
    points = {lower, Fraction(83)}

    for point in CHILD_POINTS:
        if lower < point < 83:
            points.add(point)

    for activation in positive_parent_activations(threshold):
        point = Fraction(activation, prime)
        if lower < point < 83:
            points.add(point)

    return sorted(points)


def certify_child_margins() -> dict[str, object]:
    denominator = SCALE * P79
    target_minimum: tuple[int, tuple[object, ...]] | None = None
    score_minimum: tuple[int, tuple[object, ...]] | None = None
    checks = 0

    for threshold in THRESHOLDS:
        full_a = THRESHOLD_DATA[threshold][1][-1]
        assert full_a > 0

        for index, y in enumerate(CHILD_POINTS):
            if y < 83:
                target_lower, score_lower = child_state_lowers(
                    threshold, y, True
                )
                checks += 2
                assert target_lower > 0
                assert score_lower > 0
                if target_minimum is None or target_lower < target_minimum[0]:
                    target_minimum = (
                        target_lower,
                        (threshold, str(y), "right"),
                    )
                if score_minimum is None or score_lower < score_minimum[0]:
                    score_minimum = (
                        score_lower,
                        (threshold, str(y), "right"),
                    )

            if index > 0:
                target_lower, score_lower = child_state_lowers(
                    threshold, y, False
                )
                checks += 2
                assert target_lower > 0
                assert score_lower > 0
                if target_minimum is None or target_lower < target_minimum[0]:
                    target_minimum = (
                        target_lower,
                        (threshold, str(y), "left"),
                    )
                if score_minimum is None or score_lower < score_minimum[0]:
                    score_minimum = (
                        score_lower,
                        (threshold, str(y), "left"),
                    )

    assert target_minimum is not None
    assert score_minimum is not None
    assert target_minimum[0] >= denominator

    return {
        "directed_checks": checks,
        "minimum_target_lower": str(
            Fraction(target_minimum[0], denominator)
        ),
        "minimum_target_location": list(target_minimum[1]),
        "minimum_score_lower": str(
            Fraction(score_minimum[0], denominator)
        ),
        "minimum_score_location": list(score_minimum[1]),
    }


def certify_causal_hall() -> dict[str, object]:
    denominator = SCALE * SCALE * P79
    assert denominator % 4 == 0
    target_gate = 7 * denominator // 4
    score_gate = 3 * denominator // 2

    target_minimum: tuple[int, tuple[object, ...]] | None = None
    score_minimum: tuple[int, tuple[object, ...]] | None = None
    checks = 0
    cases = 0
    breakpoint_count = 0

    for threshold in THRESHOLDS:
        finite_primes, tail_boundary = prime_cases(threshold)

        for prime in finite_primes + [tail_boundary]:
            cases += 1
            points = real_breakpoints(threshold, prime)
            breakpoint_count += len(points)

            for index, y in enumerate(points):
                if y < 83:
                    target_lower, score_lower = hall_state_lowers(
                        threshold,
                        prime,
                        y,
                        True,
                        True,
                    )
                    checks += 2
                    assert target_lower > target_gate, (
                        "right target",
                        threshold,
                        prime,
                        y,
                    )
                    assert score_lower > score_gate, (
                        "right score",
                        threshold,
                        prime,
                        y,
                    )
                    if target_minimum is None or target_lower < target_minimum[0]:
                        target_minimum = (
                            target_lower,
                            (threshold, prime, str(y), "right"),
                        )
                    if score_minimum is None or score_lower < score_minimum[0]:
                        score_minimum = (
                            score_lower,
                            (threshold, prime, str(y), "right"),
                        )

                if index > 0:
                    target_lower, score_lower = hall_state_lowers(
                        threshold,
                        prime,
                        y,
                        False,
                        False,
                    )
                    checks += 2
                    assert target_lower > target_gate, (
                        "left target",
                        threshold,
                        prime,
                        y,
                    )
                    assert score_lower > score_gate, (
                        "left score",
                        threshold,
                        prime,
                        y,
                    )
                    if target_minimum is None or target_lower < target_minimum[0]:
                        target_minimum = (
                            target_lower,
                            (threshold, prime, str(y), "left"),
                        )
                    if score_minimum is None or score_lower < score_minimum[0]:
                        score_minimum = (
                            score_lower,
                            (threshold, prime, str(y), "left"),
                        )

    assert target_minimum is not None
    assert score_minimum is not None

    return {
        "finite_prime_plus_tail_cases": cases,
        "real_breakpoints": breakpoint_count,
        "directed_checks": checks,
        "minimum_target_lower": str(
            Fraction(target_minimum[0], denominator)
        ),
        "minimum_target_lower_decimal": (
            f"{float(Fraction(target_minimum[0], denominator)):.15f}"
        ),
        "minimum_target_location": list(target_minimum[1]),
        "minimum_score_lower": str(
            Fraction(score_minimum[0], denominator)
        ),
        "minimum_score_lower_decimal": (
            f"{float(Fraction(score_minimum[0], denominator)):.15f}"
        ),
        "minimum_score_location": list(score_minimum[1]),
        "target_margin_certified_above": "7/4",
        "score_margin_certified_above": "3/2",
    }


def main() -> None:
    child = certify_child_margins()
    hall = certify_causal_hall()

    assert len(THRESHOLDS) == 385
    assert hall["finite_prime_plus_tail_cases"] == 91090
    assert child["directed_checks"] == 78540
    assert hall["directed_checks"] == 18102064

    result = {
        "classification": "PASS_P79_CAUSAL_LOW_PREFIX_HALL",
        "thresholds": len(THRESHOLDS),
        "child": child,
        "hall": hall,
        "complete_directed_inequalities": (
            child["directed_checks"] + hall["directed_checks"]
        ),
        "scope": (
            "Exact fixed-denominator interval proof of the true causal P79 "
            "low-prefix target and declared-score Hall margins for every prime "
            "p>=83, every real 1<=y<83, and every active mu=-1 threshold "
            "t<4096. Finite primes below full parent support are enumerated; "
            "the infinite full-support tail is reduced by an exact monotonicity "
            "argument. The replay does not export a source-labelled Hall flow, "
            "prove LRPT, or prove RH."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
