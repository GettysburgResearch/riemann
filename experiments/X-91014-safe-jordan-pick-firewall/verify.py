#!/usr/bin/env python3
"""Exact finite regression for R-91005/L-91014/L-91015.

This checker verifies rational identities and finite matrix controls only.
It does not evaluate xi or prove any analytic continuation theorem.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Iterable


def det_fraction(matrix: list[list[F]]) -> F:
    """Exact determinant by fraction-preserving Gaussian elimination."""
    a = [row[:] for row in matrix]
    n = len(a)
    sign = 1
    out = F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j] != 0), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            sign *= -1
        p = a[j][j]
        out *= p
        for i in range(j + 1, n):
            ratio = a[i][j] / p
            for k in range(j, n):
                a[i][k] -= ratio * a[j][k]
    return out * sign


def f_value(q: F, u: F, y: F) -> F:
    return ((q + F(1, 2)) ** 2 - y * y) / (
        (q + F(1, 2) + u) ** 2 - y * y
    )


def h_value(q: F, u: F, y: F) -> F:
    return f_value(q, u, y) / q


def rational_channel(q: F, u: F) -> F:
    return (q + 1) / ((q + u) * (q + u + 1))


def target_pick_entry(q: F, r: F, u: F, y: F) -> F:
    return (1 - f_value(q, u, y) * f_value(r, u, y)) / (1 + u + q + r)


def expected_pick_det(q: F, r: F, u: F, y: F) -> F:
    dq = (1 + 2 * q + 2 * u - 2 * y) * (1 + 2 * q + 2 * u + 2 * y)
    dr = (1 + 2 * r + 2 * u - 2 * y) * (1 + 2 * r + 2 * u + 2 * y)
    return -F(256) * u * u * (q - r) ** 2 * (2 * y - u) * (2 * y + u) / (
        dq * dq * dr * dr
    )


def f_derivative(q: F, u: F, y: F) -> F:
    den = (1 + 2 * q + 2 * u - 2 * y) ** 2 * (
        1 + 2 * q + 2 * u + 2 * y
    ) ** 2
    num = 8 * u * (
        4 * q * q + 4 * q * u + 4 * q + 2 * u + 4 * y * y + 1
    )
    return num / den


def expected_schwarz_gap(q: F, u: F, y: F) -> F:
    den = (1 + 2 * q + 2 * u - 2 * y) ** 2 * (
        1 + 2 * q + 2 * u + 2 * y
    ) ** 2
    return -16 * u * (2 * y - u) * (2 * y + u) / den


def leading_principal_dets(matrix: list[list[F]]) -> list[F]:
    return [det_fraction([row[:k] for row in matrix[:k]]) for k in range(1, len(matrix) + 1)]


def cauchy_hankel(points: Iterable[F], terms: list[tuple[F, F]]) -> list[list[F]]:
    pts = list(points)
    return [
        [sum(c / ((qi + qj) / 2 + a) for c, a in terms) for qj in pts]
        for qi in pts
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    y = F(1, 4)
    u = F(1, 8)
    qs = [F(1, 10), F(1, 7), F(1, 4), F(2, 5), F(3, 4), F(1), F(7, 4), F(3)]

    # Bare one-Green partial fractions:
    # h(q) = 4/(7q) + 2/(8q+3) + 10/[7(8q+7)].
    bare_pf_checks = 0
    for q in qs:
        rhs = F(4, 7) / q + F(2) / (8 * q + 3) + F(10, 7) / (8 * q + 7)
        assert h_value(q, u, y) == rhs
        bare_pf_checks += 1

    # Strengthened modified rational channel partial fractions.
    modified_terms = [
        (F(35, 96), F(1, 8)),
        (F(5, 16), F(3, 8)),
        (F(5, 48), F(7, 8)),
        (F(7, 32), F(9, 8)),
    ]
    assert sum(c for c, _ in modified_terms) == 1
    modified_pf_checks = 0
    for q in qs:
        lhs = rational_channel(q, u) * f_value(q, u, y)
        rhs = sum(c / (q + a) for c, a in modified_terms)
        assert lhs == rhs
        modified_pf_checks += 1

    # Exact two-point target Pick determinant formula on a grid.
    pick_det_checks = 0
    negative_pick_count = 0
    for i, q in enumerate(qs):
        for r in qs[i + 1 :]:
            p11 = target_pick_entry(q, q, u, y)
            p22 = target_pick_entry(r, r, u, y)
            p12 = target_pick_entry(q, r, u, y)
            det = p11 * p22 - p12 * p12
            assert det == expected_pick_det(q, r, u, y)
            assert det < 0
            pick_det_checks += 1
            negative_pick_count += 1

    # Exact infinitesimal Schwarz--Pick defect.
    schwarz_checks = 0
    for q in qs:
        f = f_value(q, u, y)
        gap = (1 - f * f) / (1 + u + 2 * q) - f_derivative(q, u, y)
        assert gap == expected_schwarz_gap(q, u, y)
        assert gap < 0
        schwarz_checks += 1

    # Positive one-Green Hankel controls from explicit positive Cauchy sums.
    pts = [F(1, 10), F(1, 4), F(1, 2), F(1), F(2)]
    bare_terms = [
        (F(4, 7), F(0)),
        (F(1, 4), F(3, 8)),
        (F(5, 28), F(7, 8)),
    ]
    bare_hankel = cauchy_hankel(pts, bare_terms)
    bare_dets = leading_principal_dets(bare_hankel)
    assert all(d > 0 for d in bare_dets)

    modified_hankel = cauchy_hankel(pts, modified_terms)
    modified_dets = leading_principal_dets(modified_hankel)
    assert all(d > 0 for d in modified_dets)

    # Functional-equation polynomial identity on exact samples.
    functional_equation_checks = 0
    for s in [F(-3), F(-1, 2), F(0), F(1, 3), F(7, 8), F(1), F(5, 2)]:
        lhs = (s - F(1, 2)) ** 2 - y * y
        rhs = ((1 - s) - F(1, 2)) ** 2 - y * y
        assert lhs == rhs
        functional_equation_checks += 1

    result = {
        "status": "PASS_SAFE_JORDAN_PICK_CONTINUATION_FIREWALL",
        "scope": (
            "Exact rational identities and finite matrices only; no xi evaluation, "
            "no Nevanlinna-Pick proof formalization, and no RH conclusion."
        ),
        "parameters": {"u": "1/8", "y": "1/4"},
        "checks": {
            "bare_one_green_partial_fractions": bare_pf_checks,
            "modified_rational_partial_fractions": modified_pf_checks,
            "strictly_negative_two_point_pick_determinants": negative_pick_count,
            "pick_determinant_formula": pick_det_checks,
            "strict_schwarz_pick_failures": schwarz_checks,
            "functional_equation_samples": functional_equation_checks,
            "bare_one_green_hankel_orders": len(bare_dets),
            "modified_channel_hankel_orders": len(modified_dets),
        },
        "all_positive_partial_fraction_residues": True,
        "all_one_green_hankel_leading_minors_positive": True,
        "all_nontrivial_target_pick_determinants_negative": True,
        "selected_exact_values": {
            "bare_hankel_det_order_5": str(bare_dets[-1]),
            "modified_hankel_det_order_5": str(modified_dets[-1]),
            "pick_det_q_1_10_r_3": str(
                expected_pick_det(F(1, 10), F(3), u, y)
            ),
            "schwarz_gap_q_1": str(expected_schwarz_gap(F(1), u, y)),
        },
    }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(result["status"])
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
