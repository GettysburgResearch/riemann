#!/usr/bin/env python3
"""Fraction-only complete positivity certificate for the theta quartet source."""

from __future__ import annotations

from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib
import json


def need(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def derivative_atom(coefficients: list[Q]) -> list[Q]:
    result = [Q(0)] * (len(coefficients) + 1)
    for power, coefficient in enumerate(coefficients):
        result[power] += (2 * power + Q(1, 2)) * coefficient
        result[power + 1] -= 2 * coefficient
    return result


def shift(coefficients: list[Q], left: Q, width: Q = Q(1)) -> list[Q]:
    return [
        width**power * sum(
            (coefficient * comb(original, power) * left**(original - power)
             for original, coefficient in enumerate(coefficients) if original >= power),
            Q(0),
        )
        for power in range(len(coefficients))
    ]


def add_scaled(a: list[Q], b: list[Q], scale: Q) -> list[Q]:
    return [(a[j] if j < len(a) else Q(0))
            + scale * (b[j] if j < len(b) else Q(0))
            for j in range(max(len(a), len(b)))]


def main() -> None:
    p0 = [Q(0), Q(-6), Q(4)]
    polynomials = [p0]
    for _ in range(4):
        polynomials.append(derivative_atom(polynomials[-1]))
    need(polynomials[2] == [Q(0), Q(-75, 2), Q(165), Q(-112), Q(16)], "second derivative")
    need(polynomials[4] == [Q(0), Q(-1875, 8), Q(15465, 4), Q(-8512), Q(5176), Q(-1056), Q(64)], "fourth derivative")

    second_positive = shift(add_scaled(polynomials[2], p0, Q(20)), Q(3))
    need(second_positive == [Q(9, 2), Q(33, 2), Q(101), Q(80), Q(16)], "second derivative lower certificate")
    need(all(c > 0 for c in second_positive), "second derivative complete tail")

    fourth_positive = add_scaled(polynomials[4], p0, Q(4000))
    cells = []
    minimum = None
    for left in range(3, 10):
        power = shift(fourth_positive, Q(left))
        bernstein = [sum((power[j] * Q(comb(k, j), comb(6, j))
                          for j in range(k + 1)), Q(0)) for k in range(7)]
        need(all(coefficient > 0 for coefficient in bernstein), f"Bernstein cell [{left},{left+1}]")
        cell_minimum = min(bernstein)
        minimum = cell_minimum if minimum is None else min(minimum, cell_minimum)
        cells.append({"interval": [left, left + 1], "bernstein_coefficients": [str(c) for c in bernstein]})
    need(minimum == Q(5339753, 120), "global compact certificate minimum")
    tail = shift(polynomials[4], Q(10))
    need(tail == [Q(8129125, 4), Q(30619925, 8), Q(7576425, 4), Q(422528), Q(48376), Q(2784), Q(64)], "fourth derivative tail polynomial")
    need(all(coefficient > 0 for coefficient in tail), "fourth derivative complete tail")

    # R^4-40R^2-4000 is increasing for R>=10; at R=10 its value is 2000.
    need(Q(10)**4 - 40 * Q(10)**2 - 4000 == 2000, "global source positivity margin")
    # Writing R=10+x gives a positive-coefficient unbounded-height certificate.
    height_polynomial = shift([Q(-4000), Q(0), Q(-40), Q(0), Q(1)], Q(10))
    need(all(c > 0 for c in height_polynomial), "unbounded height positivity")

    # Exact complex polynomial evaluation at all four added roots, using pairs.
    def multiply(z: tuple[Q, Q], w: tuple[Q, Q]) -> tuple[Q, Q]:
        return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]

    quartet_checks = 0
    for height in map(Q, (10, 1025, 10000)):
        for width in (Q(1, 4), Q(1, 100), Q(1, 10000)):
            for real_sign in (-1, 1):
                for imaginary_sign in (-1, 1):
                    z = (real_sign * height, imaginary_sign * width)
                    z2 = multiply(z, z)
                    z4 = multiply(z2, z2)
                    coefficient = 2 * (width**2 - height**2)
                    value = (z4[0] + coefficient * z2[0] + (height**2 + width**2)**2,
                             z4[1] + coefficient * z2[1])
                    need(value == (0, 0), "exact added quartet location")
                    quartet_checks += 1

    result = {
        "status": "PASS_EXACT_THETA_QUARTET_SOURCE_CERTIFICATE",
        "arithmetic": "fractions.Fraction only",
        "atom_second_derivative_global_lower": -20,
        "atom_fourth_derivative_global_lower": -4000,
        "compact_coverage": "[3,10] with all7 degree-six Bernstein coefficients on each of7 unit cells",
        "compact_coefficients_verified": 49,
        "compact_minimum_coefficient": str(minimum),
        "cells": cells,
        "unbounded_atom_tail": "t>=10: all positive Taylor coefficients at10",
        "source_height_threshold": 10,
        "strict_source_margin_at_threshold": 2000,
        "quartet_location_checks": quartet_checks,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "classical_inputs": ["pi>3", "correct even theta Fourier identity", "theta derivative convergence and decay", "known xi zero strip"],
        "actual_xi_zeros_numerically_evaluated": False,
        "high_derivative_saddle_numerically_verified": False,
        "source_is_actual_theta": False,
        "rh_proved": False,
    }
    Path(__file__).with_name("theta_quartet_certificate.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["status"], f"Bernstein_coefficients=49 quartet_checks={quartet_checks} unbounded_tails=2")


if __name__ == "__main__":
    main()
