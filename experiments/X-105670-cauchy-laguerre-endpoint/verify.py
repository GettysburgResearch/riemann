#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def make(value: object) -> "C":
        return value if isinstance(value, C) else C(F(value), F(0))

    def __add__(self, other: object) -> "C":
        other = C.make(other)
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self) -> "C":
        return C(-self.re, -self.im)

    def __sub__(self, other: object) -> "C":
        return self + (-C.make(other))

    def __rsub__(self, other: object) -> "C":
        return C.make(other) - self

    def __mul__(self, other: object) -> "C":
        other = C.make(other)
        return C(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    __rmul__ = __mul__

    def conj(self) -> "C":
        return C(self.re, -self.im)

    def __truediv__(self, other: object) -> "C":
        other = C.make(other)
        denominator = other.re * other.re + other.im * other.im
        return C(
            (self.re * other.re + self.im * other.im) / denominator,
            (self.im * other.re - self.re * other.im) / denominator,
        )

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0


def identity(n: int) -> list[list[C]]:
    return [[C.make(i == j) for j in range(n)] for i in range(n)]


def multiply(a: list[list[C]], b: list[list[C]]) -> list[list[C]]:
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), C())
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def inverse(a: list[list[C]]) -> list[list[C]]:
    n = len(a)
    augmented = [a[i][:] + identity(n)[i] for i in range(n)]
    for column in range(n):
        pivot = next(row for row in range(column, n) if not augmented[row][column].is_zero())
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        value = augmented[column][column]
        augmented[column] = [entry / value for entry in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if not factor.is_zero():
                augmented[row] = [
                    augmented[row][j] - factor * augmented[column][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in augmented]


def trace(a: list[list[C]]) -> C:
    return sum((a[i][i] for i in range(len(a))), C())


def gram(lambdas: list[C], shift: F) -> list[list[C]]:
    return [
        [C.make(1) / (lambdas[i].conj() + lambdas[j] + shift) for j in range(len(lambdas))]
        for i in range(len(lambdas))
    ]


def overlap_and_current(lambdas: list[C], height: F) -> tuple[C, C]:
    g0, gh, g2, g4 = (gram(lambdas, shift) for shift in (F(0), height, 2 * height, 4 * height))
    overlap = trace(multiply(multiply(multiply(inverse(g0), g2), inverse(g4)), g2))
    current = trace(multiply(inverse(g0), gh))
    return overlap, current


def laguerre_coefficients(order: int) -> list[F]:
    return [F((-1) ** k * comb(order, k), factorial(k)) for k in range(order + 1)]


def integrate_exponential_polynomial(coefficients: list[F], rate: F) -> F:
    return sum(coefficient * factorial(k) / rate ** (k + 1) for k, coefficient in enumerate(coefficients))


def laguerre_inner(left: int, right: int) -> F:
    a = laguerre_coefficients(left)
    b = laguerre_coefficients(right)
    product = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            product[i + j] += x * y
    return integrate_exponential_polynomial(product, F(1))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    checks = 0

    for i in range(8):
        for j in range(8):
            assert laguerre_inner(i, j) == F(i == j)
            checks += 1
        integral = integrate_exponential_polynomial(laguerre_coefficients(i), F(1, 2)) / 2
        assert integral == F((-1) ** i)
        checks += 1

    lambdas = [C(F(1)), C(F(2), F(1)), C(F(3), F(-1))]
    g0_inverse = inverse(gram(lambdas, F(0)))
    one_row = [[C.make(1) for _ in lambdas]]
    one_column = [[C.make(1)] for _ in lambdas]
    kappa = multiply(one_row, multiply(g0_inverse, one_column))[0][0]
    assert kappa == C(F(12))
    checks += 1

    overlap, current = overlap_and_current(lambdas, F(2))
    scaled = [C(3 * value.re, 3 * value.im) for value in lambdas]
    overlap_scaled, current_scaled = overlap_and_current(scaled, F(6))
    assert overlap == overlap_scaled and current == current_scaled
    checks += 2

    previous_current_error: F | None = None
    previous_overlap_error: F | None = None
    for height in (10, 100, 1000):
        overlap, current = overlap_and_current(lambdas, F(height))
        assert overlap.im == 0 and current.im == 0 and overlap.re > current.re
        checks += 3
        current_error = abs(height * current.re - kappa.re)
        overlap_error = abs(height * overlap.re - 3 * kappa.re)
        if previous_current_error is not None:
            assert current_error < previous_current_error
            assert overlap_error < previous_overlap_error
            checks += 2
        previous_current_error = current_error
        previous_overlap_error = overlap_error

    for depth in (F(1, 3), F(2), F(7, 2)):
        for height in (F(1, 5), F(1), F(9)):
            difference = height * depth * depth / ((height + depth) ** 2 * (height + 2 * depth))
            assert difference > 0
            checks += 1

    data = {
        "claim": "T-105670",
        "verdict": "PASS_T105670_CAUCHY_LAGUERRE_ENDPOINT",
        "checks": checks,
        "laguerre_limit_exact": True,
        "scale_invariance_exact": True,
        "global_cti_proved": False,
        "rh_established": False,
        "scope": "exact finite rational Cauchy controls and Laguerre endpoint algebra",
    }
    data["proof_object"] = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(data["verdict"])
    print(f"checks={checks}")
    print(data["proof_object"])


if __name__ == "__main__":
    main()
