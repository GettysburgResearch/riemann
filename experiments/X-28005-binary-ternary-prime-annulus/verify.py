#!/usr/bin/env python3
"""Exact replay for the binary–ternary pole-preserving prime annulus.

The checker uses integers and fractions.Fraction only. Formal logarithms are
vectors on prime generators. It verifies finite source, carry, commutator, and
continuum/discrete boundary algebra. It does not prove the local-energy estimate
or RH.
"""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for value in range(2, limit + 1):
        if not composite[value]:
            primes.append(value)
            mu[value] = -1
        for prime in primes:
            product = value * prime
            if product > limit:
                break
            composite[product] = True
            if value % prime == 0:
                mu[product] = 0
                break
            mu[product] = -mu[value]
    return mu


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def factorint(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    prime = 2
    while prime * prime <= value:
        while value % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            value //= prime
        prime = 3 if prime == 2 else prime + 2
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def divisors(value: int) -> list[int]:
    return [divisor for divisor in range(1, value + 1) if value % divisor == 0]


def source_values(limit: int) -> list[Fraction]:
    mu = mobius_sieve(limit)
    result = [Fraction(0) for _ in range(limit + 1)]
    for value in range(1, limit + 1):
        result[value] = Fraction(mu[value])
        if value % 2 == 0:
            result[value] -= Fraction(mu[value // 2])
        if value % 3 == 0:
            result[value] -= Fraction(mu[value // 3], 3)
        if value % 6 == 0:
            result[value] += Fraction(mu[value // 6], 3)
    return result


def inverse_coefficient(value: int) -> Fraction:
    exponent_two = valuation(value, 2)
    exponent_three = valuation(value, 3)
    return Fraction(exponent_two + 1) * sum(
        (Fraction(1, 3**index) for index in range(exponent_three + 1)),
        Fraction(0),
    )


def beta(parent: int, base: int) -> Fraction:
    if base > parent:
        return Fraction(0)
    quotient, remainder = divmod(parent, base)
    return Fraction(
        quotient * (base - 1 - remainder),
        parent + 1,
    )


def continuum_carry(parent: int, base: int) -> Fraction:
    quotient, remainder = divmod(parent, base)
    return Fraction(quotient * (base - remainder), parent)


def carry(parent: int, child: int, base: int) -> int:
    return (
        parent // base
        - child // base
        - (parent - child) // base
    )


def floor_profile(value: int) -> Fraction:
    return (
        (1 if value >= 1 else 0)
        - (1 if value >= 2 else 0)
        - Fraction(1 if value >= 3 else 0, 3)
        + Fraction(1 if value >= 6 else 0, 3)
    )


def add_vector(
    left: dict[int, Fraction],
    right: dict[int, Fraction],
    scale: Fraction = Fraction(1),
) -> dict[int, Fraction]:
    result: defaultdict[int, Fraction] = defaultdict(Fraction)
    result.update(left)
    for prime, coefficient in right.items():
        result[prime] += scale * coefficient
    return {
        prime: coefficient
        for prime, coefficient in result.items()
        if coefficient
    }


def scale_vector(
    vector: dict[int, Fraction],
    scale: Fraction,
) -> dict[int, Fraction]:
    return {
        prime: scale * coefficient
        for prime, coefficient in vector.items()
        if scale * coefficient
    }


def log_vector(value: int) -> dict[int, Fraction]:
    return {
        prime: Fraction(exponent)
        for prime, exponent in factorint(value).items()
    }


def subtract_vectors(
    left: dict[int, Fraction],
    right: dict[int, Fraction],
) -> dict[int, Fraction]:
    return add_vector(left, right, Fraction(-1))


def generalized_lambda(value: int) -> dict[int, Fraction]:
    factors = factorint(value)
    if len(factors) != 1:
        return {}
    prime, exponent = next(iter(factors.items()))
    if prime == 2:
        coefficient = Fraction(2)
    elif prime == 3:
        coefficient = Fraction(1) + Fraction(1, 3**exponent)
    else:
        coefficient = Fraction(1)
    return {prime: coefficient}


def ordinary_lambda(value: int) -> dict[int, Fraction]:
    factors = factorint(value)
    if len(factors) != 1:
        return {}
    prime = next(iter(factors))
    return {prime: Fraction(1)}


def ordinary_first_moment(endpoint: int) -> dict[int, Fraction]:
    result: dict[int, Fraction] = {}
    for value in range(1, endpoint + 1):
        result = add_vector(result, ordinary_lambda(value), Fraction(value))
    return result


def equal_vectors(
    left: dict[int, Fraction],
    right: dict[int, Fraction],
) -> bool:
    return {
        prime: coefficient for prime, coefficient in left.items() if coefficient
    } == {
        prime: coefficient for prime, coefficient in right.items() if coefficient
    }


def main() -> None:
    limit = 160
    source = source_values(limit)

    inverse_cases = 0
    for value in range(1, limit + 1):
        total = sum(
            (
                source[divisor]
                * inverse_coefficient(value // divisor)
                for divisor in divisors(value)
            ),
            Fraction(0),
        )
        assert total == (1 if value == 1 else 0), (value, total)
        inverse_cases += 1

    floor_cases = 0
    for value in range(0, limit + 1):
        total = sum(
            (
                source[index] * (value // index)
                for index in range(1, value + 1)
            ),
            Fraction(0),
        )
        assert total == floor_profile(value), (value, total)
        floor_cases += 1

    average_zero_cases = 0
    for parent in range(6, limit + 1):
        total = sum(
            (source[base] * beta(parent, base) for base in range(1, parent + 1)),
            Fraction(0),
        )
        assert total == 0, (parent, total)
        average_zero_cases += 1

    wavelet_cases = 0
    vanishing_cases = 0
    for scale in range(1, 9):
        for parent in range(1, min(limit, 25 * scale) + 1):
            binary = parent // 2
            ternary = (parent + 2) // 3
            for child in (binary, ternary):
                actual = sum(
                    (
                        source[index] * carry(parent, child, scale * index)
                        for index in range(1, parent // scale + 1)
                    ),
                    Fraction(0),
                )
                expected = (
                    floor_profile(parent // scale)
                    - floor_profile(child // scale)
                    - floor_profile((parent - child) // scale)
                )
                assert actual == expected, (scale, parent, child, actual)
                wavelet_cases += 1
            average = sum(
                (
                    source[index]
                    * Fraction(
                        carry(parent, binary, scale * index)
                        + carry(parent, ternary, scale * index),
                        2,
                    )
                    for index in range(1, parent // scale + 1)
                ),
                Fraction(0),
            )
            if parent >= 18 * scale - 2:
                assert average == 0
                vanishing_cases += 1

    generalized_cases = 0
    inverse_values = [Fraction(0) for _ in range(limit + 1)]
    for value in range(1, limit + 1):
        inverse_values[value] = inverse_coefficient(value)

    for value in range(1, limit + 1):
        actual: dict[int, Fraction] = {}
        for divisor in divisors(value):
            quotient = value // divisor
            for prime, exponent in factorint(quotient).items():
                actual = add_vector(
                    actual,
                    {prime: Fraction(exponent)},
                    source[divisor] * inverse_values[quotient],
                )
        expected = generalized_lambda(value)
        assert equal_vectors(actual, expected), (value, actual, expected)
        generalized_cases += 1

    top_annulus_cases = 0
    for endpoint in range(7, 101):
        endpoint_log = log_vector(endpoint)
        left: dict[int, Fraction] = {}
        for base in range(1, endpoint + 1):
            left = add_vector(
                left,
                subtract_vectors(endpoint_log, log_vector(base)),
                source[base] * continuum_carry(endpoint, base),
            )

        right: dict[int, Fraction] = {}
        for prime_power in range(1, endpoint + 1):
            if 2 * prime_power > endpoint:
                weight = Fraction(2 * prime_power - endpoint, endpoint)
            elif 3 * prime_power > endpoint:
                weight = Fraction(-2 * prime_power, endpoint)
            elif 6 * prime_power > endpoint:
                weight = Fraction(1, 3) - Fraction(
                    4 * prime_power,
                    endpoint,
                )
            else:
                weight = Fraction(0)
            right = add_vector(
                right,
                generalized_lambda(prime_power),
                weight,
            )
        assert equal_vectors(left, right), (endpoint, left, right)
        top_annulus_cases += 1

    boundary_cases = 0
    for endpoint in range(6, 101):
        endpoint_log = log_vector(endpoint)
        left: dict[int, Fraction] = {}
        for base in range(1, endpoint + 1):
            left = add_vector(
                left,
                subtract_vectors(endpoint_log, log_vector(base)),
                source[base]
                * (
                    continuum_carry(endpoint, base)
                    - beta(endpoint, base)
                ),
            )

        bracket = ordinary_first_moment(endpoint)
        bracket = add_vector(
            bracket,
            ordinary_first_moment(endpoint // 2),
            Fraction(-2),
        )
        bracket = add_vector(
            bracket,
            ordinary_first_moment(endpoint // 3),
            Fraction(-1),
        )
        bracket = add_vector(
            bracket,
            ordinary_first_moment(endpoint // 6),
            Fraction(2),
        )
        bracket = add_vector(bracket, {3: Fraction(1)}, Fraction(-1))
        right = scale_vector(
            bracket,
            Fraction(2, endpoint * (endpoint + 1)),
        )
        assert equal_vectors(left, right), (endpoint, left, right)
        boundary_cases += 1

    discrete_cases = 0
    for endpoint in range(6, 101):
        endpoint_log = log_vector(endpoint)
        left: dict[int, Fraction] = {}
        for base in range(1, endpoint + 1):
            left = add_vector(
                left,
                subtract_vectors(endpoint_log, log_vector(base)),
                source[base] * beta(endpoint, base),
            )

        right: dict[int, Fraction] = {}
        for scale in range(1, endpoint + 1):
            average_wavelet = sum(
                (
                    source[index] * beta(endpoint, scale * index)
                    for index in range(1, endpoint // scale + 1)
                ),
                Fraction(0),
            )
            right = add_vector(
                right,
                generalized_lambda(scale),
                average_wavelet,
            )
        assert equal_vectors(left, right), (endpoint, left, right)
        discrete_cases += 1

    results = {
        "schema": "X-28005-binary-ternary-prime-annulus-v1",
        "classification": "EXACT_RATIONAL_FORMAL_LOG_ALGEBRA",
        "checks": {
            "inverse_convolution_cases": inverse_cases,
            "floor_profile_cases": floor_cases,
            "average_zero_rows": average_zero_cases,
            "scaled_wavelet_cases": wavelet_cases,
            "factor18_vanishing_cases": vanishing_cases,
            "generalized_lambda_cases": generalized_cases,
            "top_annulus_formal_cases": top_annulus_cases,
            "continuum_discrete_boundary_cases": boundary_cases,
            "discrete_carry_source_cases": discrete_cases,
        },
        "does_not_prove": [
            "BT-PAE",
            "prime-annulus subexponential energy",
            "Riemann Hypothesis",
        ],
    }

    canonical = json.dumps(results, indent=2, sort_keys=True) + "\n"
    results["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(results, indent=2, sort_keys=True) + "\n"

    path = Path(__file__).with_name("results") / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
