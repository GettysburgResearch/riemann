#!/usr/bin/env python3
"""Exact finite replay for the omega_(2,3) hyperbola prefix bank.

Only Python's standard library and integer arithmetic are used.  This checker
authenticates finite convolution and delay-support algebra.  It does not prove
the physical bank upper estimate, BTEBC, or RH.
"""
from __future__ import annotations

import hashlib
import json
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


def inverse23(value: int) -> int:
    return (valuation(value, 2) + 1) * (valuation(value, 3) + 1)


def divisors(value: int) -> list[int]:
    return [divisor for divisor in range(1, value + 1) if value % divisor == 0]


def main() -> None:
    max_r = 256
    omega = omega23_values(max_r)

    coefficient_cases = 0
    strict_delay_pairs = 0

    for cutoff in range(2, max_r + 1):
        for coefficient in range(1, cutoff):
            total = sum(
                omega[divisor] * inverse23(coefficient // divisor)
                for divisor in divisors(coefficient)
            )
            assert total == (1 if coefficient == 1 else 0), (
                cutoff,
                coefficient,
                total,
            )
            coefficient_cases += 1

        for divisor in range(1, cutoff):
            for inverse_index in range(1, (cutoff - 1) // divisor + 1):
                assert divisor * inverse_index < cutoff
                strict_delay_pairs += 1

    mu = mobius_sieve(max_r)
    local_coefficients = [1, -2, 1]
    local_cases = 0
    for value in range(1, max_r + 1):
        exponent_two = valuation(value, 2)
        exponent_three = valuation(value, 3)
        odd_core = value // (2**exponent_two * 3**exponent_three)
        if exponent_two > 2 or exponent_three > 2:
            expected = 0
        else:
            expected = (
                local_coefficients[exponent_two]
                * local_coefficients[exponent_three]
                * mu[odd_core]
            )
        assert omega[value] == expected, (value, omega[value], expected)
        local_cases += 1

    max_abs = max(abs(value) for value in omega[1:])
    assert max_abs == 4

    # Removing the d=2 synthesis term destroys the coefficient m=2.
    mutation = sum(
        omega[divisor] * inverse23(2 // divisor)
        for divisor in divisors(2)
        if divisor != 2
    )
    assert mutation == 2

    results = {
        "schema": "X-28002-omega23-prefix-bank-v1",
        "classification": "EXACT_INTEGER_CONVOLUTION_ALGEBRA",
        "checks": {
            "hyperbola_coefficient_cases": coefficient_cases,
            "strict_delay_pair_cases": strict_delay_pairs,
            "local_euler_coefficient_cases": local_cases,
            "max_abs_omega23": max_abs,
            "delete_d2_mutation_coefficient_at_m2": mutation,
            "max_R": max_r,
        },
        "does_not_prove": [
            "BTEBC",
            "physical bank upper estimate",
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
