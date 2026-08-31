#!/usr/bin/env python3
"""Exact bounded checks for the Architecture-E Loewner addendum.

This module checks only rational divided-difference and discrete-Stieltjes
identities.  It does not evaluate Xi, zeta zeros, total positivity, or RH.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Callable

Q = Fraction


def fraction_text(value: Q) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def loewner_entry(
    h: Callable[[Q], Q],
    h_prime: Callable[[Q], Q],
    left: Q,
    right: Q,
) -> Q:
    if left == right:
        return h_prime(left)
    return (h(left) - h(right)) / (left - right)


def polynomial(coefficients: tuple[Q, ...]) -> tuple[Callable[[Q], Q], Callable[[Q], Q]]:
    def evaluate(value: Q) -> Q:
        total = Q(0)
        power = Q(1)
        for coefficient in coefficients:
            total += coefficient * power
            power *= value
        return total

    def derivative(value: Q) -> Q:
        total = Q(0)
        power = Q(1)
        for degree, coefficient in enumerate(coefficients[1:], start=1):
            total += degree * coefficient * power
            power *= value
        return total

    return evaluate, derivative


def check_loewner_difference() -> int:
    """Check H = L_(tp) - D_x L_p D_x, including diagonal cells."""

    coefficient_sets = (
        (Q(2), Q(-3, 5), Q(7, 11)),
        (Q(1, 3), Q(5, 4), Q(-2, 9), Q(3, 7)),
        (Q(9, 5), Q(-4, 3), Q(1, 8), Q(2, 13), Q(-1, 17)),
    )
    x_packets = (
        (Q(2, 3), Q(5, 4), Q(7, 3)),
        (Q(3, 5), Q(4, 3), Q(9, 5), Q(5, 2)),
    )

    rows = 0
    for coefficients in coefficient_sets:
        p, p_prime = polynomial(coefficients)

        def tp(value: Q) -> Q:
            return value * p(value)

        def tp_prime(value: Q) -> Q:
            return p(value) + value * p_prime(value)

        for xs in x_packets:
            ts = tuple(x * x for x in xs)
            for i, x in enumerate(xs):
                for j, y in enumerate(xs):
                    left = (x * p(ts[i]) + y * p(ts[j])) / (x + y)
                    right = loewner_entry(tp, tp_prime, ts[i], ts[j])
                    right -= x * y * loewner_entry(
                        p, p_prime, ts[i], ts[j]
                    )
                    if left != right:
                        raise AssertionError(
                            {
                                "coefficients": tuple(
                                    fraction_text(value)
                                    for value in coefficients
                                ),
                                "x": fraction_text(x),
                                "y": fraction_text(y),
                                "left": fraction_text(left),
                                "right": fraction_text(right),
                            }
                        )
                    rows += 1
    return rows


def stieltjes_functions(
    atoms: tuple[tuple[Q, Q], ...]
) -> tuple[Callable[[Q], Q], Callable[[Q], Q], Callable[[Q], Q], Callable[[Q], Q]]:
    """Return p, p', tp, (tp)' for a finite positive Stieltjes measure."""

    def p(value: Q) -> Q:
        return sum((weight / (value + location) for location, weight in atoms), Q(0))

    def p_prime(value: Q) -> Q:
        return sum(
            (-weight / (value + location) ** 2 for location, weight in atoms),
            Q(0),
        )

    def tp(value: Q) -> Q:
        return value * p(value)

    def tp_prime(value: Q) -> Q:
        return p(value) + value * p_prime(value)

    return p, p_prime, tp, tp_prime


def check_stieltjes_loewner_grams() -> dict[str, int]:
    """Check the two Loewner Gram formulas and exact nonnegative squares."""

    atom_sets = (
        ((Q(0), Q(2)), (Q(3, 2), Q(5, 7))),
        ((Q(1, 5), Q(3, 4)), (Q(2), Q(7, 6)), (Q(9, 2), Q(4, 9))),
    )
    t_packets = (
        (Q(1, 4), Q(1), Q(9, 4)),
        (Q(4, 9), Q(16, 9), Q(25, 9), Q(49, 9)),
    )
    vectors = (
        (Q(1), Q(-2), Q(3), Q(-1)),
        (Q(2, 5), Q(7, 3), Q(-5, 4), Q(9, 8)),
    )

    cell_rows = 0
    square_rows = 0
    for atoms in atom_sets:
        p, p_prime, tp, tp_prime = stieltjes_functions(atoms)
        for ts in t_packets:
            minus_lp: list[list[Q]] = []
            ltp: list[list[Q]] = []
            for left in ts:
                row_p: list[Q] = []
                row_tp: list[Q] = []
                for right in ts:
                    lp_value = -loewner_entry(p, p_prime, left, right)
                    ltp_value = loewner_entry(tp, tp_prime, left, right)
                    expected_p = sum(
                        (
                            weight
                            / ((left + location) * (right + location))
                            for location, weight in atoms
                        ),
                        Q(0),
                    )
                    expected_tp = sum(
                        (
                            location
                            * weight
                            / ((left + location) * (right + location))
                            for location, weight in atoms
                        ),
                        Q(0),
                    )
                    if lp_value != expected_p or ltp_value != expected_tp:
                        raise AssertionError(
                            (left, right, lp_value, expected_p, ltp_value, expected_tp)
                        )
                    row_p.append(lp_value)
                    row_tp.append(ltp_value)
                    cell_rows += 1
                minus_lp.append(row_p)
                ltp.append(row_tp)

            for raw_vector in vectors:
                vector = raw_vector[: len(ts)]
                q_p = sum(
                    (
                        vector[i] * minus_lp[i][j] * vector[j]
                        for i in range(len(ts))
                        for j in range(len(ts))
                    ),
                    Q(0),
                )
                q_tp = sum(
                    (
                        vector[i] * ltp[i][j] * vector[j]
                        for i in range(len(ts))
                        for j in range(len(ts))
                    ),
                    Q(0),
                )
                square_p = sum(
                    (
                        weight
                        * sum(
                            (
                                vector[i] / (ts[i] + location)
                                for i in range(len(ts))
                            ),
                            Q(0),
                        )
                        ** 2
                        for location, weight in atoms
                    ),
                    Q(0),
                )
                square_tp = sum(
                    (
                        location
                        * weight
                        * sum(
                            (
                                vector[i] / (ts[i] + location)
                                for i in range(len(ts))
                            ),
                            Q(0),
                        )
                        ** 2
                        for location, weight in atoms
                    ),
                    Q(0),
                )
                if q_p != square_p or q_tp != square_tp:
                    raise AssertionError((q_p, square_p, q_tp, square_tp))
                if q_p < 0 or q_tp < 0:
                    raise AssertionError((q_p, q_tp))
                square_rows += 1

    return {"cell_rows": cell_rows, "square_rows": square_rows}


def build_report() -> dict[str, object]:
    return {
        "schema": "xi-architecture-e-loewner-checks-v1",
        "scope": (
            "finite exact rational divided-difference and discrete-Stieltjes "
            "checks only; no Xi, zeta-zero, PF-infinity, or RH certification"
        ),
        "checks": {
            "loewner_difference_rows": check_loewner_difference(),
            "stieltjes_loewner_grams": check_stieltjes_loewner_grams(),
        },
        "all_passed": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        parser.error("the only supported action is --check")
    print(json.dumps(build_report(), sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
