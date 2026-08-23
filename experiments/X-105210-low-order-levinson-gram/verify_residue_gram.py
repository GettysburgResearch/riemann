#!/usr/bin/env python3
"""Exact critical-residue Gram fixtures for L-105212.

The fixtures are positive symmetric finite Fourier packets

    F_q(t) = 2 cos(t) + 2 q cos(2t)

with rational q.  The critical points 0 and pi are exact.  The script verifies
the block Gram, residue projection, pairwise dispersion, and coherence-defect
identities using Fraction arithmetic only.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def determinant_2(a: Fraction, b: Fraction, d: Fraction) -> Fraction:
    return a * d - b * b


def determinant_3(matrix: list[list[Fraction]]) -> Fraction:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def check_fixture(q: Fraction) -> int:
    # F(t)=2cos(t)+2qcos(2t).
    f_zero = 2 + 2 * q
    h_zero = -2 - 8 * q
    f_pi = -2 + 2 * q
    h_pi = 2 - 8 * q
    assert h_zero != 0 and h_pi != 0

    rho_zero = f_zero / h_zero
    rho_pi = f_pi / h_pi

    lambda_zero = -f_zero * h_zero
    lambda_pi = -f_pi * h_pi
    assert lambda_zero > 0

    # L-105212 vectors y_j=omega_(0,c_j)/h_j^2.
    k00 = lambda_zero / (h_zero ** 4)
    k11 = lambda_zero / (h_pi ** 4)
    k01 = lambda_pi / ((h_zero ** 2) * (h_pi ** 2))

    p_zero = lambda_zero / (h_zero ** 2)
    p_pi = lambda_pi / (h_pi ** 2)
    assert p_zero == -rho_zero
    assert p_pi == -rho_pi

    block = [
        [lambda_zero, p_zero, p_pi],
        [p_zero, k00, k01],
        [p_pi, k01, k11],
    ]

    checks = 2
    assert determinant_2(block[0][0], block[0][1], block[1][1]) >= 0
    assert determinant_2(block[0][0], block[0][2], block[2][2]) >= 0
    assert determinant_2(block[1][1], block[1][2], block[2][2]) >= 0
    assert determinant_3(block) >= 0
    checks += 4

    for q0, q1 in ((1, 1), (1, -1), (2, -3), (-4, 1)):
        residue_linear = q0 * rho_zero + q1 * rho_pi
        gram_quadratic = q0 * q0 * k00 + 2 * q0 * q1 * k01 + q1 * q1 * k11
        assert residue_linear * residue_linear <= lambda_zero * gram_quadratic
        checks += 1

    residue_difference = (rho_zero - rho_pi) ** 2
    gram_distance = k00 + k11 - 2 * k01
    assert residue_difference <= lambda_zero * gram_distance
    checks += 1

    residues = (rho_zero, rho_pi)
    m1 = -(rho_zero + rho_pi)
    m2 = rho_zero * rho_zero + rho_pi * rho_pi
    assert 2 * m2 - (rho_zero + rho_pi) ** 2 == residue_difference
    checks += 1

    if m1 > 0:
        coherence = m1 * m1 / (2 * m2)
        assert 2 * m2 * (1 - coherence) == residue_difference
        checks += 1

    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    fixtures = (Fraction(1, 8), Fraction(1, 10), Fraction(1, 12), Fraction(1, 16))
    checks = sum(check_fixture(q) for q in fixtures)

    result = {
        "verdict": "PASS_X_105212_CRITICAL_RESIDUE_GRAM",
        "arithmetic_class": "EXACT_RATIONAL_FINITE_POSITIVE_FOURIER_PACKETS",
        "fixtures": len(fixtures),
        "checks": checks,
        "esde105212_proved": False,
        "hloc105210_proved": False,
        "rh_established": False,
    }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
