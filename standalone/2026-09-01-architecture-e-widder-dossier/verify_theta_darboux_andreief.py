#!/usr/bin/env python3
"""Exact bounded checks for the theta--Darboux/Andreief gate.

The script uses only Python's standard library and exact rational arithmetic.
It verifies coefficient-lowering algebra, finite total-positivity controls,
formal self-adjointness against a Gaussian test source, and finite
Cauchy--Binet/Andreief algebra.  It does not prove the infinite theta-source
factorization, the weighted sign gate, the all-order E--Widder inequality, or
RH.
"""

from __future__ import annotations

import math
from fractions import Fraction
from itertools import combinations
from math import factorial
from typing import Sequence


def trim(coefficients: Sequence[Fraction]) -> list[Fraction]:
    result = list(coefficients)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_add(
    left: Sequence[Fraction],
    right: Sequence[Fraction],
) -> list[Fraction]:
    size = max(len(left), len(right))
    result = [Fraction(0)] * size
    for index in range(size):
        result[index] = (
            left[index] if index < len(left) else 0
        ) + (
            right[index] if index < len(right) else 0
        )
    return trim(result)


def poly_scale(
    scale: int | Fraction,
    coefficients: Sequence[Fraction],
) -> list[Fraction]:
    factor = Fraction(scale)
    return trim([factor * coefficient for coefficient in coefficients])


def poly_mul(
    left: Sequence[Fraction],
    right: Sequence[Fraction],
) -> list[Fraction]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            result[i + j] += first * second
    return trim(result)


def poly_derivative(
    coefficients: Sequence[Fraction],
    order: int = 1,
) -> list[Fraction]:
    if order < 0:
        raise ValueError("derivative order must be nonnegative")
    result = list(coefficients)
    for _ in range(order):
        if len(result) <= 1:
            return [Fraction(0)]
        result = [Fraction(index) * result[index] for index in range(1, len(result))]
    return trim(result)


def poly_eval(coefficients: Sequence[Fraction], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def lowering_operator(coefficients: Sequence[Fraction]) -> list[Fraction]:
    """Apply L = d^2/dtau^2 - 1/4 to a polynomial."""

    return poly_add(
        poly_derivative(coefficients, 2),
        poly_scale(Fraction(-1, 4), coefficients),
    )


def coefficient_polynomial(n: int, cutoff: int) -> list[Fraction]:
    """Truncate b_n(tau) after the tau^(2*cutoff) term."""

    if n < 0:
        return [Fraction(0)]
    if cutoff < n:
        return [Fraction(0)]
    result = [Fraction(0)] * (2 * cutoff + 1)
    for m in range(n, cutoff + 1):
        result[2 * m] = Fraction(
            math.comb(m, n),
            4 ** (m - n) * factorial(2 * m),
        )
    return trim(result)


def determinant(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    work = [list(map(Fraction, row)) for row in matrix]
    result = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for index in range(column, size):
            work[column][index] /= pivot_value
        for row in range(column + 1, size):
            factor = work[row][column]
            if factor == 0:
                continue
            for index in range(column, size):
                work[row][index] -= factor * work[column][index]
    return result


def check_lowering_coefficients() -> int:
    checks = 0
    for cutoff in range(4, 12):
        for n in range(cutoff + 1):
            left = lowering_operator(coefficient_polynomial(n, cutoff))
            right = coefficient_polynomial(n - 1, cutoff - 1)
            # The only truncation remainder occurs at degree 2*cutoff.
            for degree in range(2 * cutoff - 1):
                left_value = left[degree] if degree < len(left) else 0
                right_value = right[degree] if degree < len(right) else 0
                if left_value != right_value:
                    raise AssertionError(
                        ("lowering", cutoff, n, degree, left_value, right_value)
                    )
                checks += 1
    return checks


def check_pascal_minors() -> int:
    row_sets = [
        (0, 1),
        (1, 3),
        (2, 5),
        (0, 2, 5),
        (1, 3, 4),
        (0, 2, 4, 6),
    ]
    column_sets = [
        (0, 1),
        (0, 2),
        (1, 3),
        (0, 1, 2),
        (0, 2, 3),
        (0, 1, 3, 5),
    ]
    checks = 0
    for rows, columns in zip(row_sets, column_sets, strict=True):
        matrix = [
            [
                Fraction(math.comb(m, n), 4 ** (m - n)) if m >= n else 0
                for n in columns
            ]
            for m in rows
        ]
        value = determinant(matrix)
        if value < 0:
            raise AssertionError(("pascal_minor", rows, columns, value))
        checks += 1
    return checks


def check_composition_minors() -> int:
    tau_sets = [
        (Fraction(1, 5), Fraction(2, 3)),
        (Fraction(1, 4), Fraction(3, 4), Fraction(5, 3)),
        (Fraction(1, 7), Fraction(1, 2), Fraction(4, 3), Fraction(7, 3)),
    ]
    index_sets = [
        (0, 2),
        (0, 1, 3),
        (0, 1, 3, 5),
    ]
    checks = 0
    for taus, indices in zip(tau_sets, index_sets, strict=True):
        exponential_matrix = [
            [tau ** (2 * m) / factorial(2 * m) for m in indices]
            for tau in taus
        ]
        if determinant(exponential_matrix) <= 0:
            raise AssertionError(("generalized_vandermonde", taus, indices))
        checks += 1

        cutoff = max(indices) + 8
        coefficient_matrix = [
            [
                poly_eval(coefficient_polynomial(n, cutoff), tau)
                for n in indices
            ]
            for tau in taus
        ]
        if determinant(coefficient_matrix) <= 0:
            raise AssertionError(("coefficient_kernel", taus, indices))
        checks += 1
    return checks


def gaussian_ladder_operator(coefficients: Sequence[Fraction]) -> list[Fraction]:
    """If f=P(tau)e^(-tau^2), return the polynomial for Lf."""

    tau = [Fraction(0), Fraction(1)]
    tau_squared = [Fraction(0), Fraction(0), Fraction(1)]
    return poly_add(
        poly_add(
            poly_derivative(coefficients, 2),
            poly_scale(-4, poly_mul(tau, poly_derivative(coefficients))),
        ),
        poly_mul(
            poly_add(poly_scale(4, tau_squared), [Fraction(-9, 4)]),
            coefficients,
        ),
    )


def gaussian_integral_coefficient(coefficients: Sequence[Fraction]) -> Fraction:
    """Return the coefficient of sqrt(pi) in int_R P(t)e^(-t^2) dt."""

    result = Fraction(0)
    for degree, coefficient in enumerate(coefficients):
        if degree % 2:
            continue
        half_degree = degree // 2
        result += coefficient * Fraction(
            factorial(2 * half_degree),
            4 ** half_degree * factorial(half_degree),
        )
    return result


def check_self_adjointness() -> int:
    checks = 0
    for cutoff in (5, 7, 9):
        for n in range(2, cutoff + 1):
            b_value = coefficient_polynomial(n, cutoff)
            for order in range(1, min(3, n) + 1):
                lowered_b = b_value
                source_polynomial = [Fraction(1)]
                for _ in range(order):
                    lowered_b = lowering_operator(lowered_b)
                    source_polynomial = gaussian_ladder_operator(source_polynomial)
                left = gaussian_integral_coefficient(lowered_b)
                right = gaussian_integral_coefficient(
                    poly_mul(source_polynomial, b_value)
                )
                if left != right:
                    raise AssertionError(
                        ("self_adjoint", cutoff, n, order, left, right)
                    )
                checks += 1
    return checks


def check_finite_andreief() -> int:
    nodes = [
        Fraction(1, 5),
        Fraction(1, 2),
        Fraction(4, 3),
        Fraction(2),
        Fraction(11, 4),
    ]
    weights = [
        Fraction(1),
        Fraction(2),
        Fraction(3, 2),
        Fraction(5, 3),
        Fraction(7, 4),
    ]
    cutoff = 12
    checks = 0
    for rank in (1, 2, 3):
        indices = [rank + offset for offset in range(rank)]
        source = [
            Fraction(2),
            Fraction(0),
            Fraction(3),
            Fraction(0),
            Fraction(1, 2),
            Fraction(0),
            Fraction(1, 7),
        ]
        source_ladder = [source]
        for _ in range(1, rank):
            source_ladder.append(lowering_operator(source_ladder[-1]))

        first = [
            [poly_eval(source_ladder[row], node) for node in nodes]
            for row in range(rank)
        ]
        second = [
            [
                poly_eval(coefficient_polynomial(indices[row], cutoff), node)
                for node in nodes
            ]
            for row in range(rank)
        ]
        composed = [
            [
                sum(
                    weights[index] * first[row][index] * second[column][index]
                    for index in range(len(nodes))
                )
                for column in range(rank)
            ]
            for row in range(rank)
        ]
        left = determinant(composed)

        right = Fraction(0)
        for subset in combinations(range(len(nodes)), rank):
            first_minor = determinant(
                [[first[row][index] for index in subset] for row in range(rank)]
            )
            second_minor = determinant(
                [[second[row][index] for index in subset] for row in range(rank)]
            )
            subset_weight = Fraction(1)
            for index in subset:
                subset_weight *= weights[index]
            right += first_minor * second_minor * subset_weight

        if left != right:
            raise AssertionError(("andreief", rank, left, right))
        checks += 1
    return checks


def main() -> None:
    counts = {
        "lowering_coefficients": check_lowering_coefficients(),
        "pascal_minors": check_pascal_minors(),
        "composition_minors": check_composition_minors(),
        "self_adjointness": check_self_adjointness(),
        "andreief": check_finite_andreief(),
    }
    print("PASS_THETA_DARBOUX_ANDREIEF_EXACT_CHECKS")
    for name, count in counts.items():
        print(f"{name}={count}")
    print(f"total={sum(counts.values())}")
    print("WEIGHTED_THETA_DARBOUX_SIGN_OPEN")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
