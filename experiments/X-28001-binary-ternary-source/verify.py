#!/usr/bin/env python3
"""Exact replay for the binary–ternary bottom-charge proposal.

Only Python's standard library is used.  The checker authenticates finite
algebra and exact counterexamples.  It does not prove BTEBC, the cofinal bottom
sign, physical transference, or RH.
"""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from math import comb, isqrt
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
    result = [1]
    for prime, exponent in factorint(value).items():
        result = [
            divisor * prime**power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return sorted(result)


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def carry(parent: int, child: int, base: int) -> int:
    return (
        parent // base
        - child // base
        - (parent - child) // base
    )


def producer(target: list[Fraction], endpoint: int) -> tuple[list[Fraction], list[Fraction]]:
    mu = mobius_sieve(endpoint)
    tail = [Fraction(0) for _ in range(endpoint + 2)]
    for multiple in range(1, endpoint + 1):
        for factor in range(1, endpoint // multiple + 1):
            if mu[factor]:
                tail[multiple] += mu[factor] * target[multiple * factor]

    divergence = [Fraction(0) for _ in range(endpoint + 2)]
    for node in range(1, endpoint + 1):
        divergence[node] = tail[node] - tail[node + 1]

    coefficient = [Fraction(0) for _ in range(endpoint + 2)]
    incoming = [Fraction(0) for _ in range(endpoint + 2)]
    for parent in range(endpoint, 1, -1):
        coefficient[parent] = divergence[parent] + incoming[parent]
        ternary = (parent + 2) // 3
        binary = parent // 2
        children = (
            ternary,
            parent - ternary,
            binary,
            parent - binary,
        )
        for child in children:
            if child >= 2:
                incoming[child] += coefficient[parent] / 2
    return coefficient, divergence


def b2_values(limit: int) -> list[int]:
    mu = mobius_sieve(limit)
    result = [0] * (limit + 1)
    for value in range(1, limit + 1):
        result[value] = mu[value]
        if value % 2 == 0:
            result[value] -= mu[value // 2]
    return result


def omega23_values(limit: int) -> list[int]:
    mu = mobius_sieve(limit)
    result = [0] * (limit + 1)
    for value in range(1, limit + 1):
        result[value] = mu[value]
        if value % 2 == 0:
            result[value] -= mu[value // 2]
        if value % 3 == 0:
            result[value] -= mu[value // 3]
        if value % 6 == 0:
            result[value] += mu[value // 6]
    return result


def box(value: int) -> int:
    return (
        (1 if value >= 1 else 0)
        - (1 if value >= 2 else 0)
        - (1 if value >= 3 else 0)
        + (1 if value >= 6 else 0)
    )


def check_abel_witnesses() -> dict[str, object]:
    output: dict[str, object] = {}
    witnesses = (
        (520, 3, 15, Fraction(-91, 256)),
        (3559, 4, 15, Fraction(-84_999_795, 2048)),
    )
    for endpoint, order, node, expected in witnesses:
        target = [Fraction(0) for _ in range(endpoint + 1)]
        for column in range(2, endpoint + 1):
            target[column] = comb(
                endpoint - column + order - 1,
                order - 1,
            )
        coefficient, _ = producer(target, endpoint)
        assert coefficient[node] == expected
        output[f"abel{order}"] = {
            "Q": endpoint,
            "n": node,
            "value": str(expected),
        }
    return output


def check_b2() -> dict[str, object]:
    limit = 100
    b2 = b2_values(limit)
    cases = 0
    for parent in range(2, limit + 1):
        for child in range(parent + 1):
            left = sum(
                b2[base] * carry(parent, child, base)
                for base in range(1, parent + 1)
            )
            right = -int(child == 1) - int(child == parent - 1)
            assert left == right
            cases += 1

    expected = {2: Fraction(-2), 3: Fraction(-1)}
    for parent in range(2, limit + 1):
        binary = parent // 2
        ternary = (parent + 2) // 3
        value = Fraction(
            sum(
                b2[base]
                * (
                    carry(parent, binary, base)
                    + carry(parent, ternary, base)
                )
                for base in range(1, parent + 1)
            ),
            2,
        )
        assert value == expected.get(parent, 0)

    synthetic_cases = 0
    for endpoint in (8, 12, 20, 30):
        local_b2 = b2_values(endpoint)
        for seed in range(5):
            target = [Fraction(0) for _ in range(endpoint + 1)]
            for column in range(2, endpoint + 1):
                target[column] = Fraction(
                    ((seed + 3) * column * column + 5 * column + 7) % 17 - 8,
                    column + seed + 1,
                )
            coefficient, _ = producer(target, endpoint)
            left = sum(
                local_b2[column] * target[column]
                for column in range(2, endpoint + 1)
            )
            right = -2 * coefficient[2] - coefficient[3]
            assert left == right
            synthetic_cases += 1

    return {
        "b2_two_contact_cases": cases,
        "b2_bottom_profile": {"2": "-2", "3": "-1"},
        "bottom_charge_synthetic_cases": synthetic_cases,
    }


def check_omega23() -> dict[str, object]:
    limit = 200
    omega = omega23_values(limit)

    for value in range(limit + 1):
        left = sum(
            omega[base] * (value // base)
            for base in range(1, value + 1)
        )
        assert left == box(value)

    wavelet_cases = 0
    for scale in range(1, 12):
        for parent in range(1, min(limit, 22 * scale) + 1):
            for child in range(parent + 1):
                left = sum(
                    omega[factor]
                    * carry(parent, child, scale * factor)
                    for factor in range(1, parent // scale + 1)
                )
                right = (
                    box(parent // scale)
                    - box(child // scale)
                    - box((parent - child) // scale)
                )
                assert left == right
                wavelet_cases += 1

    expected = {
        2: Fraction(-2),
        3: Fraction(-2),
        4: Fraction(-1),
        6: Fraction(3, 2),
        7: Fraction(2),
        8: Fraction(2),
        9: Fraction(3, 2),
        10: Fraction(3, 2),
        11: Fraction(1),
        12: Fraction(1, 2),
        13: Fraction(1, 2),
        14: Fraction(1, 2),
        15: Fraction(1, 2),
    }
    for parent in range(2, 80):
        binary = parent // 2
        ternary = (parent + 2) // 3
        value = Fraction(
            sum(
                omega[base]
                * (
                    carry(parent, binary, base)
                    + carry(parent, ternary, base)
                )
                for base in range(1, parent + 1)
            ),
            2,
        )
        assert value == expected.get(parent, 0)

    inverse_cases = 0
    for value in range(1, limit + 1):
        inverse = lambda n: (valuation(n, 2) + 1) * (valuation(n, 3) + 1)
        result = sum(
            omega[divisor] * inverse(value // divisor)
            for divisor in divisors(value)
        )
        assert result == (1 if value == 1 else 0)
        inverse_cases += 1

    generalized_cases = 0
    inverse_values = [0] * (limit + 1)
    for value in range(1, limit + 1):
        inverse_values[value] = (
            (valuation(value, 2) + 1)
            * (valuation(value, 3) + 1)
        )

    for value in range(1, limit + 1):
        actual: defaultdict[int, int] = defaultdict(int)
        for divisor in divisors(value):
            quotient = value // divisor
            for prime, exponent in factorint(quotient).items():
                actual[prime] += (
                    omega[divisor]
                    * inverse_values[quotient]
                    * exponent
                )

        expected_vector: defaultdict[int, int] = defaultdict(int)
        factors = factorint(value)
        if len(factors) == 1:
            prime = next(iter(factors))
            expected_vector[prime] += 1
            if prime in (2, 3):
                expected_vector[prime] += 1

        assert {
            prime: coefficient
            for prime, coefficient in actual.items()
            if coefficient
        } == {
            prime: coefficient
            for prime, coefficient in expected_vector.items()
            if coefficient
        }
        generalized_cases += 1

    return {
        "omega23_floor_cases": limit + 1,
        "omega23_wavelet_cases": wavelet_cases,
        "omega23_average_profile": {
            str(node): str(value)
            for node, value in expected.items()
        },
        "positive_inverse_cases": inverse_cases,
        "generalized_lambda_formal_cases": generalized_cases,
    }


def main() -> None:
    checks = {}
    checks.update(check_abel_witnesses())
    checks.update(check_b2())
    checks.update(check_omega23())

    results = {
        "schema": "X-28001-binary-ternary-source-v1",
        "classification": "EXACT_RATIONAL_AND_INTEGER_ALGEBRA",
        "checks": checks,
        "does_not_prove": [
            "BTEBC",
            "bottom-charge sign",
            "Riemann Hypothesis",
            "physical-normal-to-carry transference",
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
