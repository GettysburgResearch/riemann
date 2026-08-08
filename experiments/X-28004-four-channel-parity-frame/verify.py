#!/usr/bin/env python3
"""Exact algebraic replay for the four-channel binary–ternary parity frame.

The checker uses Q(sqrt(2),sqrt(3)) and Fraction arithmetic only. It verifies
Bézout, tensor reconstruction, parity Hadamard, and twist-sum algebra. It does
not prove the physical upper estimate or RH.
"""
from __future__ import annotations

import hashlib
import json
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


def as_alg(value: object) -> Alg:
    if isinstance(value, Alg):
        return value
    return Alg(Fraction(value))


ZERO = Alg()
ONE = Alg(Fraction(1))
ROOT_TWO = Alg(root_two=Fraction(1))
ROOT_THREE = Alg(root_three=Fraction(1))


def poly_add(left: list[Alg], right: list[Alg]) -> list[Alg]:
    size = max(len(left), len(right))
    result = [ZERO for _ in range(size)]
    for index in range(size):
        result[index] = (
            left[index] if index < len(left) else ZERO
        ) + (
            right[index] if index < len(right) else ZERO
        )
    while len(result) > 1 and result[-1] == ZERO:
        result.pop()
    return result


def poly_multiply(left: list[Alg], right: list[Alg]) -> list[Alg]:
    result = [ZERO for _ in range(len(left) + len(right) - 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] = result[i + j] + left_value * right_value
    return result


def source_polynomial(root: Alg, sign: int) -> list[Alg]:
    signed_one = sign * ONE
    signed_root = sign * root
    return poly_multiply(
        [ONE, -signed_one],
        poly_multiply([ONE, -signed_one], [ONE, -signed_root]),
    )


def bezout_polynomials(prime: int) -> tuple[list[Alg], list[Alg], Alg]:
    if prime == 2:
        root = ROOT_TWO
        linear = Alg(Fraction(11, 4), root_two=Fraction(-3, 2))
        quadratic = Alg(Fraction(2), root_two=Fraction(-5, 4))
    elif prime == 3:
        root = ROOT_THREE
        linear = Alg(Fraction(7, 4), root_three=Fraction(-5, 8))
        quadratic = Alg(Fraction(9, 8), root_three=Fraction(-1, 2))
    else:
        raise ValueError("only primes 2 and 3 are used")
    plus = [Fraction(1, 2) * ONE, linear, quadratic]
    minus = [Fraction(1, 2) * ONE, -linear, quadratic]
    return plus, minus, root


def bivariate_add(
    left: dict[tuple[int, int], Alg],
    right: dict[tuple[int, int], Alg],
) -> dict[tuple[int, int], Alg]:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, ZERO) + coefficient
    return {
        exponent: coefficient
        for exponent, coefficient in result.items()
        if coefficient != ZERO
    }


def bivariate_product(
    left_x: list[Alg],
    right_y: list[Alg],
) -> dict[tuple[int, int], Alg]:
    return {
        (x_degree, y_degree): x_coefficient * y_coefficient
        for x_degree, x_coefficient in enumerate(left_x)
        for y_degree, y_coefficient in enumerate(right_y)
        if x_coefficient * y_coefficient != ZERO
    }


def main() -> None:
    one_variable_checks = 0
    data: dict[int, tuple[list[Alg], list[Alg], list[Alg], list[Alg]]] = {}
    for prime in (2, 3):
        plus_u, minus_u, root = bezout_polynomials(prime)
        plus_p = source_polynomial(root, 1)
        minus_p = source_polynomial(root, -1)
        result = poly_add(
            poly_multiply(plus_u, plus_p),
            poly_multiply(minus_u, minus_p),
        )
        assert result == [ONE], (prime, result)
        data[prime] = (plus_u, minus_u, plus_p, minus_p)
        one_variable_checks += 1

    tensor = {}
    for two_sign in (0, 1):
        for three_sign in (0, 1):
            two_u = data[2][two_sign]
            three_u = data[3][three_sign]
            two_p = data[2][two_sign + 2]
            three_p = data[3][three_sign + 2]
            channel = bivariate_product(
                poly_multiply(two_u, two_p),
                poly_multiply(three_u, three_p),
            )
            tensor = bivariate_add(tensor, channel)
    assert tensor == {(0, 0): ONE}, tensor

    hadamard_cases = 0
    for seed in range(1, 101):
        parity = {
            (a, b): [
                Fraction((seed + 3 * index + 5 * a + 7 * b) % 19 - 9,
                         seed + index + a + b + 1)
                for index in range(6)
            ]
            for a in (0, 1)
            for b in (0, 1)
        }
        channel_norm = Fraction(0)
        for epsilon in (1, -1):
            for eta in (1, -1):
                vector = [
                    sum(
                        Fraction(epsilon**a * eta**b)
                        * parity[(a, b)][index]
                        for a in (0, 1)
                        for b in (0, 1)
                    )
                    for index in range(6)
                ]
                channel_norm += sum(value * value for value in vector)
        parity_norm = 4 * sum(
            value * value
            for vector in parity.values()
            for value in vector
        )
        assert channel_norm == parity_norm
        hadamard_cases += 1

    twist_cases = 0
    for value in range(1, 501):
        exponent_two = 0
        exponent_three = 0
        reduced = value
        while reduced % 2 == 0:
            exponent_two += 1
            reduced //= 2
        while reduced % 3 == 0:
            exponent_three += 1
            reduced //= 3
        character_sum = sum(
            epsilon**exponent_two * eta**exponent_three
            for epsilon in (1, -1)
            for eta in (1, -1)
        )
        expected = (
            4
            if exponent_two % 2 == 0 and exponent_three % 2 == 0
            else 0
        )
        assert character_sum == expected
        twist_cases += 1

    results = {
        "schema": "X-28004-four-channel-parity-frame-v1",
        "classification": "EXACT_Q_SQRT2_SQRT3_POLYNOMIAL_ALGEBRA",
        "checks": {
            "one_variable_bezout_identities": one_variable_checks,
            "tensor_bezout_nonzero_coefficients": len(tensor),
            "hadamard_norm_cases": hadamard_cases,
            "forcing_twist_sum_cases": twist_cases,
        },
        "does_not_prove": [
            "four-channel physical upper estimate",
            "BTEBC",
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
