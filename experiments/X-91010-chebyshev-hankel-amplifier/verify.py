#!/usr/bin/env python3
"""Finite regression for the Chebyshev/Christoffel Hankel amplifier.

This script checks exact finite algebra and synthetic scaling laws only.
It does not evaluate zeta, prove the analytic parabolic-contour theorem,
or prove RH.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import mpmath as mp

mp.mp.dps = 80


def catalan(n: int) -> int:
    return math.comb(2 * n, n) // (n + 1)


def moment(k: int) -> Fraction:
    return Fraction(catalan(k + 1), 8 * (4**k))


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(max(len(a), len(b)))]
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return [c * value for value in a]


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def shifted_u_coefficients(max_degree: int) -> list[list[Fraction]]:
    rows = [[Fraction(1)]]
    if max_degree == 0:
        return rows
    rows.append([Fraction(-2), Fraction(4)])
    multiplier = [Fraction(-2), Fraction(4)]
    for _ in range(1, max_degree):
        rows.append(
            poly_add(poly_mul(multiplier, rows[-1]), poly_scale(rows[-2], Fraction(-1)))
        )
    return rows


def poly_eval(coefficients: Iterable[Fraction], x: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(list(coefficients)):
        value = value * x + coefficient
    return value


def q_moment(a: list[Fraction], b: list[Fraction]) -> Fraction:
    return sum(
        (ai * bj * moment(i + j) for i, ai in enumerate(a) for j, bj in enumerate(b)),
        Fraction(0),
    )


def matrix_inverse_fraction(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(matrix)
    augmented = [
        list(row) + [Fraction(int(i == j)) for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if augmented[row][column] != 0),
            None,
        )
        if pivot is None:
            raise AssertionError("singular exact matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [entry / pivot_value for entry in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][j] - factor * augmented[column][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in augmented]


def quadratic(matrix: list[list[Fraction]], vector: list[Fraction]) -> Fraction:
    return sum(
        (
            vector[i] * matrix[i][j] * vector[j]
            for i in range(len(vector))
            for j in range(len(vector))
        ),
        Fraction(0),
    )


def u_value(n: int, x: mp.mpf) -> mp.mpf:
    if n == 0:
        return mp.mpf(1)
    if n == 1:
        return 2 * x
    previous, current = mp.mpf(1), 2 * x
    for _ in range(1, n):
        previous, current = current, 2 * x * current - previous
    return current


def t_value(n: int, x: mp.mpf) -> mp.mpf:
    if n == 0:
        return mp.mpf(1)
    if n == 1:
        return x
    previous, current = mp.mpf(1), x
    for _ in range(1, n):
        previous, current = current, 2 * x * current - previous
    return current


def christoffel_sum(n: int, y: mp.mpf) -> mp.mpf:
    lam = 1 / (1 - y * y)
    x = 2 * lam - 1
    return 8 * sum(u_value(j, x) ** 2 for j in range(n + 1))


def christoffel_closed(n: int, y: mp.mpf) -> mp.mpf:
    alpha = 2 * mp.atanh(y)
    degree_count = n + 1
    return 4 / mp.sinh(alpha) ** 2 * (
        mp.sinh(degree_count * alpha)
        * mp.cosh((degree_count + 1) * alpha)
        / mp.sinh(alpha)
        - degree_count
    )


def first_detection_degree(log_ell: float, depth: float) -> int:
    ell = mp.e ** mp.mpf(log_ell)
    y = mp.mpf(depth)
    kappa = 4 * y * y / (1 - y * y) ** 3
    degree = 0
    while kappa * christoffel_sum(degree, y) <= ell:
        degree += 1
        if degree > 100000:
            raise AssertionError("synthetic detection search failed")
    return degree


def rational_x(b: mp.mpf, y: mp.mpf) -> mp.mpf:
    lam = 1 / (1 - y * y)
    return 2 * lam * (b - 1) / (b - lam) - 1


def build_report() -> dict:
    shifted = shifted_u_coefficients(12)

    exact_orthogonality_rows = []
    exact_orthogonality_ok = True
    for i in range(9):
        for j in range(9):
            value = q_moment(shifted[i], shifted[j])
            target = Fraction(1, 8) if i == j else Fraction(0)
            exact_orthogonality_ok &= value == target
            if i < 4 and j < 4:
                exact_orthogonality_rows.append(
                    {
                        "i": i,
                        "j": j,
                        "numerator": value.numerator,
                        "denominator": value.denominator,
                    }
                )

    inverse_rows = []
    inverse_ok = True
    y_exact = Fraction(1, 5)
    lam_exact = 1 / (1 - y_exact * y_exact)
    for degree in range(6):
        hankel = [
            [moment(i + j) for j in range(degree + 1)]
            for i in range(degree + 1)
        ]
        inverse = matrix_inverse_fraction(hankel)
        monomial_vector = [lam_exact**i for i in range(degree + 1)]
        inverse_value = quadratic(inverse, monomial_vector)
        kernel_value = 8 * sum(
            poly_eval(shifted[j], lam_exact) ** 2 for j in range(degree + 1)
        )
        inverse_ok &= inverse_value == kernel_value
        inverse_rows.append(
            {
                "degree": degree,
                "numerator": kernel_value.numerator,
                "denominator": kernel_value.denominator,
                "numeric": float(kernel_value),
            }
        )

    pair_polynomial = [
        Fraction(3, 2),
        Fraction(-2, 3),
        Fraction(5, 7),
        Fraction(1, 4),
    ]
    w_exact = 1 - y_exact * y_exact

    def pair_moment(k: int) -> Fraction:
        return -4 * y_exact * y_exact * w_exact ** (-k - 3)

    pair_lhs = sum(
        (
            pair_polynomial[i]
            * pair_polynomial[j]
            * pair_moment(i + j)
            for i in range(len(pair_polynomial))
            for j in range(len(pair_polynomial))
        ),
        Fraction(0),
    )
    pair_rhs = (
        -4
        * y_exact
        * y_exact
        * w_exact ** (-3)
        * poly_eval(pair_polynomial, 1 / w_exact) ** 2
    )
    pair_identity_ok = pair_lhs == pair_rhs

    closed_rows = []
    max_closed_error = mp.mpf(0)
    for depth in (mp.mpf("0.1"), mp.mpf("0.2"), mp.mpf("0.4"), mp.mpf("0.49")):
        for degree in (0, 1, 4, 10):
            direct = christoffel_sum(degree, depth)
            closed = christoffel_closed(degree, depth)
            error = abs(direct - closed)
            max_closed_error = max(max_closed_error, error)
            closed_rows.append(
                {
                    "depth": float(depth),
                    "degree": degree,
                    "direct": float(direct),
                    "closed": float(closed),
                    "absolute_error": float(error),
                }
            )

    detection_rows = []
    for depth in (0.1, 0.2, 0.4, 0.49):
        for log_ell in (20.0, 50.0, 100.0):
            degree = first_detection_degree(log_ell, depth)
            prediction = mp.mpf(log_ell) / (4 * mp.atanh(depth))
            detection_rows.append(
                {
                    "depth": depth,
                    "log_ell": log_ell,
                    "first_degree": degree,
                    "leading_prediction": float(prediction),
                    "ratio": float(degree / prediction),
                }
            )

    parabola_rows = []
    parabola_ok = True
    for degree in (4, 8, 16, 32, 64, 128, 256):
        delta = mp.mpf(1) / (degree + 4)
        c = mp.mpf("0.5") + delta
        rho = (1 + c) / (1 - c)
        exact = 3 + mp.mpf(8) / (degree + 2)
        ratio = rho ** (2 * degree) / (mp.mpf(9) ** degree)
        parabola_ok &= abs(rho - exact) < mp.mpf("1e-70")
        parabola_rows.append(
            {
                "degree": degree,
                "rho": float(rho),
                "rho_exact": float(exact),
                "rho_2n_over_9n": float(ratio),
            }
        )

    rational_rows = []
    rational_ok = True
    for depth in (0.1, 0.2, 0.4, 0.49):
        y = mp.mpf(depth)
        limit_alpha = 2 * mp.atanh(2 * y)
        previous = mp.mpf(0)
        for b in (mp.mpf("1.5"), mp.mpf("1.4"), mp.mpf("1.34")):
            if b <= 1 / (1 - y * y):
                continue
            x_value = rational_x(b, y)
            alpha = mp.acosh(x_value)
            rational_ok &= alpha > previous and alpha < limit_alpha
            previous = alpha

            max_support = mp.mpf(0)
            test_degree = 9
            for grid_index in range(401):
                lam = mp.mpf(grid_index) / 400
                z = lam * (b - 1) / (b - lam)
                value = abs(t_value(test_degree, 2 * z - 1))
                max_support = max(max_support, value)
            rational_ok &= max_support <= 1 + mp.mpf("1e-60")

            rational_rows.append(
                {
                    "depth": depth,
                    "b": float(b),
                    "x_target": float(x_value),
                    "alpha": float(alpha),
                    "boundary_limit_alpha": float(limit_alpha),
                    "support_sup_degree_9": float(max_support),
                }
            )

    constants = {
        "coefficient_edge": float(1 / mp.log(mp.mpf(4) / 3)),
        "hankel_edge": float(1 / (2 * mp.log(3))),
        "gain_ratio": float((2 * mp.log(3)) / mp.log(mp.mpf(4) / 3)),
    }

    gates = {
        "exact_shifted_chebyshev_orthogonality": exact_orthogonality_ok,
        "inverse_hankel_equals_christoffel": inverse_ok,
        "pair_rank_one_identity": pair_identity_ok,
        "closed_christoffel_formula": max_closed_error < mp.mpf("1e-65"),
        "parabolic_growth_constant_three": parabola_ok,
        "rational_safe_pole_accelerator": rational_ok,
        "edge_constants_ordered": constants["hankel_edge"] < constants["coefficient_edge"],
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    return {
        "status": "PASS_CHEBYSHEV_HANKEL_AMPLIFIER",
        "gates": gates,
        "constants": constants,
        "orthogonality": {
            "checked_degree": 8,
            "rows": exact_orthogonality_rows,
        },
        "inverse_hankel_christoffel": inverse_rows,
        "pair_identity": {
            "lhs_numerator": pair_lhs.numerator,
            "lhs_denominator": pair_lhs.denominator,
            "rhs_numerator": pair_rhs.numerator,
            "rhs_denominator": pair_rhs.denominator,
            "numeric": float(pair_lhs),
        },
        "christoffel_closed_form": {
            "max_absolute_error": float(max_closed_error),
            "rows": closed_rows,
        },
        "synthetic_detection": detection_rows,
        "parabolic_growth": parabola_rows,
        "rational_accelerator": rational_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    report = build_report()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
