#!/usr/bin/env python3
"""Exact finite checks for T-101500/T-101510.

The script checks algebraic identities only. It does not prove any terminal
arithmetic estimate and explicitly records that RH is unproved.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def neg(x: Fraction) -> Fraction:
    return max(-x, Fraction(0))


def check_matched_transfer() -> int:
    checks = 0
    vals = [Fraction(n, 3) for n in range(-12, 13)]
    for f in vals:
        for g in vals:
            best = None
            for tau in vals + [-f, g]:
                rhs = neg(f + tau) + neg(g - tau)
                assert neg(f + g) <= rhs
                best = rhs if best is None else min(best, rhs)
                checks += 1
            assert best == neg(f + g)
    return checks


def poly_mul(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, Fraction(0)) + x * y
    return {k: v for k, v in out.items() if v}


def poly_add(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + v
    return {k: v for k, v in out.items() if v}


def poly_scale_shift(a: dict[int, Fraction], c: Fraction, shift: int) -> dict[int, Fraction]:
    return {k + shift: c * v for k, v in a.items() if c * v}


def check_triangular_forms() -> int:
    # One commuting formal variable per owner is encoded in disjoint bit places.
    rs = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 5), Fraction(5, 7)]
    B = [{0: Fraction(1), 1 << i: -r} for i, r in enumerate(rs)]
    A = [{0: Fraction(1), 2 << i: -(r * r)} for i, r in enumerate(rs)]

    prod_b = {0: Fraction(1)}
    prod_a = {0: Fraction(1)}
    for x in B:
        prod_b = poly_mul(prod_b, x)
    for x in A:
        prod_a = poly_mul(prod_a, x)
    target = poly_add(prod_a, {k: -v for k, v in prod_b.items()})

    least: dict[int, Fraction] = {}
    greatest: dict[int, Fraction] = {}
    k = len(rs)
    for i, r in enumerate(rs):
        left_b = {0: Fraction(1)}
        right_a = {0: Fraction(1)}
        left_a = {0: Fraction(1)}
        right_b = {0: Fraction(1)}
        for h in range(i):
            left_b = poly_mul(left_b, B[h])
            left_a = poly_mul(left_a, A[h])
        for h in range(i + 1, k):
            right_a = poly_mul(right_a, A[h])
            right_b = poly_mul(right_b, B[h])
        owner = poly_scale_shift(B[i], r, 1 << i)
        least = poly_add(least, poly_mul(poly_mul(left_b, owner), right_a))
        greatest = poly_add(greatest, poly_mul(poly_mul(left_a, owner), right_b))
    assert least == target
    assert greatest == target
    return len(target)


def check_adaptive_residual() -> int:
    checks = 0
    vals = [Fraction(n, 5) for n in range(-20, 21)]
    for f in vals:
        for r in vals:
            if f + r >= 0:
                assert neg(f) <= max(r, Fraction(0))
                checks += 1
    return checks


def check_regional_gate() -> int:
    checks = 0
    vals = [Fraction(n, 4) for n in range(0, 21)]
    for fminus in vals:
        for left in vals:
            for right in vals:
                if fminus <= left and fminus <= right:
                    chosen = left if left <= right else right
                    assert fminus <= chosen
                    checks += 1
    return checks


def main() -> None:
    result = {
        "verdict": "PASS_T101500_JOINT_COMPENSATED_MATRIX_RECOVERY",
        "matched_transfer_checks": check_matched_transfer(),
        "triangular_form_coefficients": check_triangular_forms(),
        "adaptive_residual_checks": check_adaptive_residual(),
        "regional_gate_checks": check_regional_gate(),
        "qmt101500_proved": False,
        "amt101500_proved": False,
        "lcor101510_proved": False,
        "rcor101510_proved": False,
        "rh_established": False,
    }
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print("RH UNPROVED")


if __name__ == "__main__":
    main()
