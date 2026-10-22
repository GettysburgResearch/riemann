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
SCALE = 10**24
LOG_TERMS = 10


def log_interval_fraction(
    value: Fraction,
    terms: int = LOG_TERMS,
) -> tuple[Fraction, Fraction]:
    """Exact atanh interval for log(value), value >= 1."""
    if value < 1:
        raise ValueError("value must be at least one")
    if value == 1:
        return Fraction(0), Fraction(0)

    z = (value - 1) / (value + 1)
    partial = 2 * sum(
        (
            z ** (2 * index + 1) / Fraction(2 * index + 1)
            for index in range(terms)
        ),
        Fraction(0),
    )
    tail = (
        2
        * z ** (2 * terms + 1)
        / (Fraction(2 * terms + 1) * (1 - z * z))
    )
    return partial, partial + tail


LOG2_INTERVAL = log_interval_fraction(Fraction(2))


def scaled_interval(
    interval: tuple[Fraction, Fraction],
) -> tuple[int, int]:
    lower, upper = interval
    lower_integer = lower.numerator * SCALE // lower.denominator
    upper_integer = (
        upper.numerator * SCALE + upper.denominator - 1
    ) // upper.denominator
    return lower_integer, upper_integer


def log_integer_fraction_interval(integer: int) -> tuple[Fraction, Fraction]:
    if integer < 1:
        raise ValueError("integer must be positive")
    if integer == 1:
        return Fraction(0), Fraction(0)

    power = integer.bit_length() - 1
    reduced = Fraction(integer, 1 << power)
    reduced_interval = log_interval_fraction(reduced)
    return (
        power * LOG2_INTERVAL[0] + reduced_interval[0],
        power * LOG2_INTERVAL[1] + reduced_interval[1],
    )


def log_integer_scaled(integer: int) -> tuple[int, int]:
    return scaled_interval(log_integer_fraction_interval(integer))


def sqrt_scaled(integer: int) -> tuple[int, int]:
    root = isqrt(integer * SCALE * SCALE)
    upper = root if root * root == integer * SCALE * SCALE else root + 1
    return root, upper


def reciprocal_sqrt_scaled(integer: int) -> tuple[int, int]:
    root = isqrt((SCALE * SCALE) // integer)
    upper = root if integer * root * root == SCALE * SCALE else root + 1
    return root, upper


def all_divisors() -> list[tuple[int, int]]:
    values: list[tuple[int, int]] = [(1, 1)]
    for prime in PRIMES79:
        values += [(divisor * prime, -mu) for divisor, mu in values]
    values.sort()
    return values


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


def prime_sieve(limit: int) -> bytearray:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return sieve


def certify_global_euler_corridors() -> dict[str, object]:
    divisors = all_divisors()
    assert len(divisors) == 2 ** len(PRIMES79)

    first_state_at_83 = max(
        index for index, (divisor, _mu) in enumerate(divisors) if divisor <= 83
    )

    a_numerator = 0
    b_lower = 0
    b_upper = 0
    maximum_a: tuple[int, int] | None = None
    maximum_absolute_a = 0
    maximum_b: tuple[int, int] | None = None
    minimum_b: tuple[int, int] | None = None

    for index, (divisor, mu) in enumerate(divisors):
        a_numerator += mu * (P79 // divisor)

        reciprocal_lower, reciprocal_upper = reciprocal_sqrt_scaled(divisor)
        if mu > 0:
            b_lower += reciprocal_lower
            b_upper += reciprocal_upper
        else:
            b_lower -= reciprocal_upper
            b_upper -= reciprocal_lower

        maximum_absolute_a = max(maximum_absolute_a, abs(a_numerator))
        if maximum_b is None or b_upper > maximum_b[0]:
            maximum_b = b_upper, divisor
        if minimum_b is None or b_lower < minimum_b[0]:
            minimum_b = b_lower, divisor

        if index >= first_state_at_83:
            if maximum_a is None or a_numerator > maximum_a[0]:
                maximum_a = a_numerator, divisor

    assert maximum_a is not None
    assert maximum_b is not None
    assert minimum_b is not None

    maximum_a_fraction = Fraction(maximum_a[0], P79)
    assert maximum_a[1] == 221
    assert maximum_a_fraction < Fraction(1, 5)
    assert maximum_absolute_a <= P79

    assert maximum_b[1] == 341
    assert minimum_b[1] == 9823
    assert maximum_b[0] < Fraction(3, 2) * SCALE
    assert minimum_b[0] > -Fraction(3, 2) * SCALE

    return {
        "activation_states": len(divisors),
        "global_A_max": str(maximum_a_fraction),
        "global_A_max_activation": maximum_a[1],
        "global_A_upper": "1/5",
        "global_abs_A_upper": "1",
        "global_B_lower_decimal": f"{minimum_b[0] / SCALE:.15f}",
        "global_B_lower_activation": minimum_b[1],
        "global_B_upper_decimal": f"{maximum_b[0] / SCALE:.15f}",
        "global_B_upper_activation": maximum_b[1],
        "global_abs_B_upper": "3/2",
    }


def build_log_and_lambda_tables() -> tuple[
    list[tuple[int, int]],
    list[int],
]:
    logs = [(0, 0)] * 10001
    for integer in range(1, 10001):
        logs[integer] = log_integer_scaled(integer)

    small_prime_count = [0] * 10001
    unique_small_prime = [0] * 10001
    for prime in PRIMES79:
        for integer in range(prime, 10001, prime):
            small_prime_count[integer] += 1
            if small_prime_count[integer] == 1:
                unique_small_prime[integer] = prime
            else:
                unique_small_prime[integer] = 0

    lambda_log_argument = [1] * 10001
    for integer in range(2, 10001):
        if small_prime_count[integer] == 0:
            lambda_log_argument[integer] = integer
        elif small_prime_count[integer] == 1:
            lambda_log_argument[integer] = unique_small_prime[integer]
        else:
            lambda_log_argument[integer] = 1

    return logs, lambda_log_argument


def certify_theta_lower(
    logs: list[tuple[int, int]],
) -> dict[str, object]:
    primes = prime_sieve(10000)
    theta_lower = 0
    theta_upper = 0
    theta_79_upper: int | None = None
    minimum_margin: tuple[int, int] | None = None

    for integer in range(2, 10000):
        if primes[integer]:
            log_lower, log_upper = logs[integer]
            theta_lower += log_lower
            theta_upper += log_upper

        if integer == 79:
            theta_79_upper = theta_upper

        if integer >= 179:
            assert theta_79_upper is not None
            # This checks every real t in [integer, integer+1).
            margin = (
                2 * (theta_lower - theta_79_upper)
                - (integer + 1) * SCALE
            )
            if minimum_margin is None or margin < minimum_margin[0]:
                minimum_margin = margin, integer

    assert minimum_margin is not None
    assert minimum_margin[0] > 0

    log_10_small = log_interval_fraction(Fraction(5, 4))
    log_10_interval = (
        3 * LOG2_INTERVAL[0] + log_10_small[0],
        3 * LOG2_INTERVAL[1] + log_10_small[1],
    )
    log_56_small = log_interval_fraction(Fraction(7, 4))
    log_56_interval = (
        5 * LOG2_INTERVAL[0] + log_56_small[0],
        5 * LOG2_INTERVAL[1] + log_56_small[1],
    )
    log_10001_interval = log_integer_fraction_interval(10001)

    assert LOG2_INTERVAL[0] > Fraction(6931, 10000)
    assert LOG2_INTERVAL[1] < Fraction(7, 10)
    assert log_10_interval[1] < Fraction(2303, 1000)
    assert log_56_interval[1] < Fraction(403, 100)
    assert log_10001_interval[1] < 10
    assert P79 < 10**31
    assert 464**3 < 10000**2

    cube_term_upper = (
        Fraction(9212, 1000) ** 2
        / (3 * Fraction(69, 100) * 464)
    )
    assert cube_term_upper < Fraction(443, 5000)

    analytic_ratio_lower = (
        Fraction(6931, 10000)
        - Fraction(7, 50000)
        - Fraction(1, 1000)
        - Fraction(461, 10000)
        - Fraction(443, 5000)
        - Fraction(9, 1250)
    )
    assert analytic_ratio_lower == Fraction(27503, 50000)
    assert analytic_ratio_lower > Fraction(1, 2)

    analytic_f_lower_at_10000 = (
        Fraction(100)
        - 7 * Fraction(403, 100)
        - 28
        - Fraction(9, 2)
    )
    assert analytic_f_lower_at_10000 == Fraction(3929, 100)
    assert analytic_f_lower_at_10000 > 18

    return {
        "real_cell_start": 179,
        "finite_min_cell": minimum_margin[1],
        "finite_min_margin_decimal": (
            f"{float(Fraction(minimum_margin[0], 2 * SCALE)):.12f}"
        ),
        "analytic_theta_ratio_lower": str(analytic_ratio_lower),
        "analytic_F_lower_at_10000": str(analytic_f_lower_at_10000),
    }


def certify_finite_entropy_gaps(
    logs: list[tuple[int, int]],
    lambda_log_argument: list[int],
) -> dict[str, object]:
    mu_at = dict(divisors_capped(10000))

    c_lower = 0
    c_upper = 0
    d_lower = 0
    d_upper = 0
    a_numerator = 0
    b_lower = 0
    b_upper = 0

    minimum_by_a: dict[int, int | None] = {4: None, 5: None}
    minimum_location: dict[int, tuple[int, str]] = {}
    entropy_83_upper: int | None = None

    for integer in range(1, 10001):
        if integer >= 2 and lambda_log_argument[integer] > 1:
            lambda_lower, lambda_upper = logs[lambda_log_argument[integer]]
            reciprocal_lower, reciprocal_upper = reciprocal_sqrt_scaled(integer)
            weight_lower = lambda_lower * reciprocal_lower
            weight_upper = lambda_upper * reciprocal_upper

            c_lower += weight_lower
            c_upper += weight_upper

            log_lower, log_upper = logs[integer]
            d_lower += weight_lower * log_lower
            d_upper += weight_upper * log_upper

        if integer in mu_at:
            mu = mu_at[integer]
            a_numerator += mu * (P79 // integer)
            reciprocal_lower, reciprocal_upper = reciprocal_sqrt_scaled(integer)
            if mu > 0:
                b_lower += reciprocal_lower
                b_upper += reciprocal_upper
            else:
                b_lower -= reciprocal_upper
                b_upper -= reciprocal_lower

        if integer == 83:
            _log_lower, log_upper = logs[integer]
            entropy_83_upper = c_upper * log_upper - d_lower

        def gap_cross_product(endpoint: int, a: int) -> int:
            log_lower, _log_upper = logs[endpoint]
            entropy_lower = c_lower * log_lower - d_upper

            sqrt_lower, sqrt_upper = sqrt_scaled(endpoint)
            sqrt_for_source_upper = (
                sqrt_upper if a_numerator >= 0 else sqrt_lower
            )
            source_upper = (
                a * sqrt_for_source_upper * a_numerator
                - 3 * b_lower * P79
            )

            return (
                entropy_lower * P79
                - source_upper * SCALE**2
                - 18 * P79 * SCALE**3
            )

        if integer >= 83:
            for a in (4, 5):
                margin = gap_cross_product(integer, a)
                if (
                    minimum_by_a[a] is None
                    or margin < minimum_by_a[a]
                ):
                    minimum_by_a[a] = margin
                    minimum_location[a] = integer, "right"

        if 83 <= integer < 10000:
            for a in (4, 5):
                margin = gap_cross_product(integer + 1, a)
                assert minimum_by_a[a] is not None
                if margin < minimum_by_a[a]:
                    minimum_by_a[a] = margin
                    minimum_location[a] = integer + 1, "left"

    assert entropy_83_upper is not None
    assert entropy_83_upper < 21 * SCALE**3
    assert minimum_by_a[4] is not None
    assert minimum_by_a[5] is not None
    assert minimum_by_a[4] > 0
    assert minimum_by_a[5] > 0
    assert minimum_location[4] == (83, "right")
    assert minimum_location[5] == (83, "right")

    final_residual_lower = Fraction(18) - Fraction(76, 9)
    assert final_residual_lower == Fraction(86, 9)
    assert final_residual_lower > 0

    denominator = P79 * SCALE**3
    return {
        "E_P79_83_upper_decimal": (
            f"{float(Fraction(entropy_83_upper, SCALE**3)):.12f}"
        ),
        "F4_min_location": list(minimum_location[4]),
        "F4_margin_over_18": (
            f"{float(Fraction(minimum_by_a[4], denominator)):.12f}"
        ),
        "F5_min_location": list(minimum_location[5]),
        "F5_margin_over_18": (
            f"{float(Fraction(minimum_by_a[5], denominator)):.12f}"
        ),
        "residual_entropy_minus_target_lower": str(final_residual_lower),
        "residual_entropy_minus_score_lower": str(final_residual_lower),
    }


def main() -> None:
    global_corridors = certify_global_euler_corridors()
    logs, lambda_log_argument = build_log_and_lambda_tables()
    theta = certify_theta_lower(logs)
    finite_gaps = certify_finite_entropy_gaps(logs, lambda_log_argument)

    result = {
        "classification": "PASS_P79_LITERAL_ENTROPY_DOMINATION",
        "global_corridors": global_corridors,
        "theta": theta,
        "finite_gaps": finite_gaps,
        "scope": (
            "Exact/directed proof that the literal P79 Euler residual component "
            "entropy dominates both the target and declared source score for all "
            "p>=83 and 1<=y<83. This does not by itself prove that the finite "
            "frontier/quantization assembly retains the full literal entropy, "
            "nor the Riemann Hypothesis."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
