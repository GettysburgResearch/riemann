#!/usr/bin/env python3
"""Exact algebraic replay for the critical binary–ternary source.

The coefficient ring is Q(sqrt(2),sqrt(3)).  The checker uses only Python's
standard library and exact Fraction arithmetic.  It proves finite algebra only,
not the compact-source energy theorem, BTEBC, or RH.
"""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


@dataclass(frozen=True)
class Alg:
    one: Fraction = Fraction(0)
    root_two: Fraction = Fraction(0)
    root_three: Fraction = Fraction(0)
    root_six: Fraction = Fraction(0)

    def __add__(self, other: object) -> "Alg":
        right = as_alg(other)
        return Alg(
            self.one + right.one,
            self.root_two + right.root_two,
            self.root_three + right.root_three,
            self.root_six + right.root_six,
        )

    __radd__ = __add__

    def __neg__(self) -> "Alg":
        return Alg(
            -self.one,
            -self.root_two,
            -self.root_three,
            -self.root_six,
        )

    def __sub__(self, other: object) -> "Alg":
        return self + (-as_alg(other))

    def __rsub__(self, other: object) -> "Alg":
        return as_alg(other) - self

    def __mul__(self, other: object) -> "Alg":
        right = as_alg(other)
        a, b, c, d = (
            self.one,
            self.root_two,
            self.root_three,
            self.root_six,
        )
        e, f, g, h = (
            right.one,
            right.root_two,
            right.root_three,
            right.root_six,
        )
        return Alg(
            a * e + 2 * b * f + 3 * c * g + 6 * d * h,
            a * f + b * e + 3 * c * h + 3 * d * g,
            a * g + c * e + 2 * b * h + 2 * d * f,
            a * h + d * e + b * g + c * f,
        )

    __rmul__ = __mul__

    def serial(self) -> list[str]:
        return [
            str(self.one),
            str(self.root_two),
            str(self.root_three),
            str(self.root_six),
        ]


def as_alg(value: object) -> Alg:
    if isinstance(value, Alg):
        return value
    return Alg(Fraction(value))


ZERO = Alg()
ONE = Alg(Fraction(1))
ROOT_TWO = Alg(root_two=Fraction(1))
ROOT_THREE = Alg(root_three=Fraction(1))


def power(value: Alg, exponent: int) -> Alg:
    result = ONE
    for _ in range(exponent):
        result = result * value
    return result


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


def factor_array(prime: int, coefficient: Alg, limit: int) -> list[Alg]:
    result = [ZERO for _ in range(limit + 1)]
    result[1] = ONE
    if prime <= limit:
        result[prime] = -coefficient
    return result


def convolve_arrays(arrays: list[list[Alg]], limit: int) -> list[Alg]:
    result = [ZERO for _ in range(limit + 1)]
    result[1] = ONE
    for array in arrays:
        updated = [ZERO for _ in range(limit + 1)]
        for left in range(1, limit + 1):
            if result[left] == ZERO:
                continue
            for right in range(1, limit // left + 1):
                if array[right] != ZERO:
                    updated[left * right] = (
                        updated[left * right]
                        + result[left] * array[right]
                    )
        result = updated
    return result


def inverse_coefficient(value: int) -> Alg:
    exponent_two = valuation(value, 2)
    exponent_three = valuation(value, 3)
    local_two = sum(
        (
            (exponent_two - index + 1) * power(ROOT_TWO, index)
            for index in range(exponent_two + 1)
        ),
        ZERO,
    )
    local_three = sum(
        (
            (exponent_three - index + 1) * power(ROOT_THREE, index)
            for index in range(exponent_three + 1)
        ),
        ZERO,
    )
    return local_two * local_three


def carry(parent: int, child: int, base: int) -> int:
    return (
        parent // base
        - child // base
        - (parent - child) // base
    )


def main() -> None:
    limit = 220
    mu = mobius_sieve(limit)
    mu_array = [ZERO for _ in range(limit + 1)]
    for value in range(1, limit + 1):
        mu_array[value] = as_alg(mu[value])

    sigma = convolve_arrays(
        [
            mu_array,
            factor_array(2, ONE, limit),
            factor_array(2, ROOT_TWO, limit),
            factor_array(3, ONE, limit),
            factor_array(3, ROOT_THREE, limit),
        ],
        limit,
    )

    finite_floor_source = convolve_arrays(
        [
            factor_array(2, ONE, limit),
            factor_array(2, ROOT_TWO, limit),
            factor_array(3, ONE, limit),
            factor_array(3, ROOT_THREE, limit),
        ],
        limit,
    )
    finite_support = [
        value
        for value in range(1, limit + 1)
        if finite_floor_source[value] != ZERO
    ]
    assert finite_support == [1, 2, 3, 4, 6, 9, 12, 18, 36]
    assert sum(
        (finite_floor_source[value] for value in finite_support),
        ZERO,
    ) == ZERO

    inverse_cases = 0
    for value in range(1, 201):
        total = sum(
            (
                sigma[divisor]
                * inverse_coefficient(value // divisor)
                for divisor in divisors(value)
            ),
            ZERO,
        )
        assert total == (ONE if value == 1 else ZERO), (value, total)
        inverse_cases += 1

    def floor_profile(value: int) -> Alg:
        return sum(
            (
                finite_floor_source[divisor]
                for divisor in finite_support
                if divisor <= value
            ),
            ZERO,
        )

    floor_cases = 0
    for value in range(0, 201):
        total = sum(
            (
                sigma[index] * (value // index)
                for index in range(1, value + 1)
            ),
            ZERO,
        )
        assert total == floor_profile(value), (value, total)
        if value >= 36:
            assert total == ZERO
        floor_cases += 1

    wavelet_cases = 0
    vanishing_cases = 0
    for scale in range(1, 5):
        for parent in range(1, min(limit, 120 * scale) + 1):
            binary = parent // 2
            ternary = (parent + 2) // 3
            actual = sum(
                (
                    sigma[index]
                    * Fraction(
                        carry(parent, binary, scale * index)
                        + carry(parent, ternary, scale * index),
                        2,
                    )
                    for index in range(1, parent // scale + 1)
                ),
                ZERO,
            )
            expected = Fraction(1, 2) * (
                floor_profile(parent // scale)
                - floor_profile(binary // scale)
                - floor_profile((parent - binary) // scale)
                + floor_profile(parent // scale)
                - floor_profile(ternary // scale)
                - floor_profile((parent - ternary) // scale)
            )
            assert actual == expected, (scale, parent, actual, expected)
            if parent >= 108 * scale - 2:
                assert actual == ZERO
                vanishing_cases += 1
            wavelet_cases += 1

    generalized_cases = 0
    inverse_values = [ZERO for _ in range(limit + 1)]
    for value in range(1, limit + 1):
        inverse_values[value] = inverse_coefficient(value)

    for value in range(1, 151):
        actual: defaultdict[int, Alg] = defaultdict(lambda: ZERO)
        for divisor in divisors(value):
            quotient = value // divisor
            for prime, exponent in factorint(quotient).items():
                actual[prime] = (
                    actual[prime]
                    + sigma[divisor]
                    * inverse_values[quotient]
                    * exponent
                )
        actual = {
            prime: coefficient
            for prime, coefficient in actual.items()
            if coefficient != ZERO
        }

        expected: dict[int, Alg] = {}
        factors = factorint(value)
        if len(factors) == 1:
            prime, exponent = next(iter(factors.items()))
            if prime == 2:
                expected[prime] = as_alg(2) + power(ROOT_TWO, exponent)
            elif prime == 3:
                expected[prime] = as_alg(2) + power(ROOT_THREE, exponent)
            else:
                expected[prime] = ONE
        assert actual == expected, (value, actual, expected)
        generalized_cases += 1

    results = {
        "schema": "X-28003-critical-binary-ternary-source-v1",
        "classification": "EXACT_Q_SQRT2_SQRT3_ALGEBRA",
        "checks": {
            "finite_floor_support": finite_support,
            "inverse_convolution_cases": inverse_cases,
            "floor_profile_cases": floor_cases,
            "scaled_carry_wavelet_cases": wavelet_cases,
            "factor108_vanishing_cases": vanishing_cases,
            "generalized_lambda_formal_cases": generalized_cases,
        },
        "does_not_prove": [
            "compact-source subexponential energy",
            "physical source-image transition theorem",
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
