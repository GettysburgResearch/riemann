#!/usr/bin/env python3
"""Exact finite checks for the spectral theta--Darboux variation theorem.

The checks use only Python's standard library and exact rational arithmetic.
They authenticate finite Cauchy--Binet, generalized-Vandermonde, coefficient
extraction, and bispectral operator identities.  They do not prove the
infinite analytic source theorem, the coefficient-resolved TDA sign, or RH.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from typing import Sequence


def trim(poly: Sequence[Fraction]) -> list[Fraction]:
    out = list(map(Fraction, poly))
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left: Sequence[Fraction], right: Sequence[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    out = [Fraction(0) for _ in range(size)]
    for i in range(size):
        out[i] = (
            left[i] if i < len(left) else 0
        ) + (
            right[i] if i < len(right) else 0
        )
    return trim(out)


def scale(value: Fraction | int, poly: Sequence[Fraction]) -> list[Fraction]:
    return trim([Fraction(value) * coefficient for coefficient in poly])


def multiply(
    left: Sequence[Fraction],
    right: Sequence[Fraction],
) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            out[i + j] += first * second
    return trim(out)


def derivative(poly: Sequence[Fraction]) -> list[Fraction]:
    if len(poly) <= 1:
        return [Fraction(0)]
    return trim([Fraction(i) * poly[i] for i in range(1, len(poly))])


def evaluate(poly: Sequence[Fraction], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def determinant(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    work = [list(map(Fraction, row)) for row in matrix]
    answer = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        pivot_value = work[column][column]
        answer *= pivot_value
        for index in range(column, size):
            work[column][index] /= pivot_value
        for row in range(column + 1, size):
            factor = work[row][column]
            if factor == 0:
                continue
            for index in range(column, size):
                work[row][index] -= factor * work[column][index]
    return answer


def coefficient(sequence: Sequence[Fraction], index: int) -> Fraction:
    if 0 <= index < len(sequence):
        return Fraction(sequence[index])
    return Fraction(0)


def check_spectral_cauchy_binet() -> int:
    """Check det[u_q^h_p X(u_q)] in its alternant coefficient expansion."""

    coefficient_panels = [
        [Fraction(1), Fraction(3, 2), Fraction(2, 3), Fraction(5, 7)],
        [Fraction(2), Fraction(1, 3), Fraction(7, 5), Fraction(4, 9), Fraction(1, 8)],
    ]
    exponent_panels = [
        (0, 1),
        (0, 2),
        (1, 3),
        (0, 1, 3),
    ]
    checks = 0
    for coefficients in coefficient_panels:
        degree = len(coefficients) - 1
        for exponents in exponent_panels:
            rank = len(exponents)
            nodes = tuple(Fraction(i + 1, rank + 2) for i in range(rank))
            values = [evaluate(coefficients, node) for node in nodes]
            left = determinant([
                [
                    nodes[column] ** exponents[row] * values[column]
                    for column in range(rank)
                ]
                for row in range(rank)
            ])
            right = Fraction(0)
            for spectral_exponents in combinations(
                range(degree + max(exponents) + 1),
                rank,
            ):
                toeplitz_coefficient = determinant([
                    [
                        coefficient(
                            coefficients,
                            spectral_exponents[column] - exponents[row],
                        )
                        for column in range(rank)
                    ]
                    for row in range(rank)
                ])
                alternant = determinant([
                    [
                        nodes[column] ** spectral_exponents[row]
                        for column in range(rank)
                    ]
                    for row in range(rank)
                ])
                right += toeplitz_coefficient * alternant
            if left != right:
                raise AssertionError(
                    ("spectral_cauchy_binet", coefficients, exponents, left, right)
                )
            checks += 1
    return checks


def check_generalized_vandermonde() -> int:
    panels = [
        ((Fraction(1, 7), Fraction(2, 5)), (0, 3)),
        ((Fraction(1, 9), Fraction(1, 2), Fraction(5, 4)), (0, 2, 5)),
        (
            (Fraction(1, 11), Fraction(2, 7), Fraction(4, 5), Fraction(3, 2)),
            (0, 1, 4, 7),
        ),
    ]
    checks = 0
    for nodes, exponents in panels:
        value = determinant([
            [nodes[column] ** exponents[row] for column in range(len(nodes))]
            for row in range(len(nodes))
        ])
        if value <= 0:
            raise AssertionError(("generalized_vandermonde", nodes, exponents, value))
        checks += 1
    return checks


def check_positive_spectral_not_coefficientwise() -> int:
    """Exact firewall: spectral positivity alone cannot extract Schur signs."""

    coefficients = [Fraction(1), Fraction(1), Fraction(2)]
    u1 = Fraction(1, 3)
    u2 = Fraction(5, 4)
    x1 = evaluate(coefficients, u1)
    x2 = evaluate(coefficients, u2)
    spectral = determinant([
        [x1, x2],
        [u1 * x1, u2 * x2],
    ])
    toeplitz = determinant([
        [coefficients[1], coefficients[2]],
        [coefficients[0], coefficients[1]],
    ])
    if spectral <= 0:
        raise AssertionError(("spectral_should_be_positive", spectral))
    if toeplitz != -1:
        raise AssertionError(("toeplitz_firewall", toeplitz))
    return 2


def mellin_generator(poly: Sequence[Fraction]) -> list[Fraction]:
    """Polynomial action of M=m*d/dm on g(m,tau)P(y), y proportional to m^2."""

    y = [Fraction(0), Fraction(1)]
    return scale(2, multiply(y, add(derivative(poly), scale(-1, poly))))


def tau_ladder(poly: Sequence[Fraction]) -> list[Fraction]:
    """Polynomial action of L_tau=D_tau^2-1/4 on gP."""

    first = mellin_generator(poly)
    return mellin_generator(add(first, poly))


def explicit_tau_ladder(poly: Sequence[Fraction]) -> list[Fraction]:
    """The expanded 4y^2 P''+(-8y^2+6y)P'+(4y^2-6y)P formula."""

    first = derivative(poly)
    second = derivative(first)
    return add(
        add(
            scale(4, multiply([0, 0, 1], second)),
            multiply([0, 6, -8], first),
        ),
        multiply([0, -6, 4], poly),
    )


def check_bispectral_casimir() -> int:
    panels = [
        [Fraction(1)],
        [Fraction(1), Fraction(2), Fraction(3)],
        [Fraction(3, 2), Fraction(-2), Fraction(5), Fraction(1)],
        [Fraction(-1, 7), Fraction(4, 3), Fraction(0), Fraction(9, 5)],
    ]
    checks = 0
    for poly in panels:
        via_mellin = tau_ladder(poly)
        via_tau = explicit_tau_ladder(poly)
        if via_mellin != via_tau:
            raise AssertionError(("bispectral_casimir", poly, via_mellin, via_tau))
        checks += 1
    return checks


def check_source_mode_ladder() -> int:
    """Check the first four mode polynomials P_h generated by the Casimir."""

    expected = [
        [1],
        [0, -6, 4],
        [0, -36, 164, -112, 16],
        [0, -216, 3784, -8456, 5168, -1056, 64],
    ]
    current = [Fraction(1)]
    checks = 0
    for target in expected:
        if current != list(map(Fraction, target)):
            raise AssertionError(("source_mode_ladder", current, target))
        checks += 1
        current = tau_ladder(current)
    return checks


def main() -> None:
    counts = {
        "spectral_cauchy_binet": check_spectral_cauchy_binet(),
        "generalized_vandermonde": check_generalized_vandermonde(),
        "spectral_extraction_firewall": check_positive_spectral_not_coefficientwise(),
        "bispectral_casimir": check_bispectral_casimir(),
        "source_mode_ladder": check_source_mode_ladder(),
    }
    print("PASS_SPECTRAL_WEIGHTED_VARIATION_EXACT_CHECKS")
    for name, count in counts.items():
        print(f"{name}={count}")
    print(f"total={sum(counts.values())}")
    print("COEFFICIENT_RESOLVED_TDA_SIGN_OPEN")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
