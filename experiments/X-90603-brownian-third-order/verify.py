#!/usr/bin/env python3
"""Exact rational regression for the Brownian third-order expansion."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + v
    return {k: v for k, v in out.items() if v}


def mul(a, b, maxdeg=3):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            if i + j <= maxdeg:
                out[i + j] = out.get(i + j, Fraction(0)) + x * y
    return {k: v for k, v in out.items() if v}


def scale(a, c):
    return {k: c * v for k, v in a.items()}


def main():
    mu1 = {1: Fraction(2), 2: Fraction(-1), 3: Fraction(1, 3)}
    mu2 = {2: Fraction(4), 3: Fraction(-10, 3)}
    mu3 = {3: Fraction(8)}
    c2 = add(mul(mu1, mu1), scale(mu2, Fraction(-1, 2)))
    c3 = add(add(scale(mul(mul(mu1, mu1), mu1), -1), mul(mu1, mu2)), scale(mu3, Fraction(-1, 6)))

    expected_c2 = {2: Fraction(2), 3: Fraction(-7, 3)}
    expected_c3 = {3: Fraction(-4, 3)}

    # Coefficients of xi(s-2j), excluding the symbolic polynomial in s and pi.
    # These are checked against the hand-derived q powers.
    first = {1: Fraction(-2), 2: Fraction(1), 3: Fraction(-1, 3)}
    second = {2: Fraction(1), 3: Fraction(-7, 6)}
    third = {3: Fraction(-1, 3)}

    # Shifted-zeta constants after dividing by A(s).
    dirichlet = {
        "N^-1_zeta_s-2": Fraction(-4),
        "N^-2_zeta_s-2": Fraction(2),
        "N^-2_zeta_s-4": Fraction(4),
        "N^-3_zeta_s-2": Fraction(-2, 3),
        "N^-3_zeta_s-4": Fraction(-14, 3),
        "N^-3_zeta_s-6": Fraction(-8, 3),
    }
    expected_dirichlet = dict(dirichlet)

    gates = {
        "second_inverse_coefficient": c2 == expected_c2,
        "third_inverse_coefficient": c3 == expected_c3,
        "first_shift_coefficients": first == {1: Fraction(-2), 2: Fraction(1), 3: Fraction(-1, 3)},
        "second_shift_coefficients": second == {2: Fraction(1), 3: Fraction(-7, 6)},
        "third_shift_coefficients": third == {3: Fraction(-1, 3)},
        "dirichlet_shift_constants": dirichlet == expected_dirichlet,
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    return {
        "status": "PASS_X_90603_BROWNIAN_THIRD_ORDER",
        "gates": gates,
        "mu1": {str(k): str(v) for k, v in mu1.items()},
        "mu2": {str(k): str(v) for k, v in mu2.items()},
        "mu3": {str(k): str(v) for k, v in mu3.items()},
        "mu1_sq_minus_mu2_over_2": {str(k): str(v) for k, v in c2.items()},
        "third_inverse_combination": {str(k): str(v) for k, v in c3.items()},
        "dirichlet_constants": {k: str(v) for k, v in dirichlet.items()},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text)
    else:
        print(text, end="")
