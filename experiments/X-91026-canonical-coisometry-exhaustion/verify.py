#!/usr/bin/env python3
"""Exact finite regression for L-91038/R-91006.

Checks the half-plane product-kernel identity, exact norm exhaustion when the
Blaschke pole factor is constant, and the positive rank-one exhaustion defect
when one crossed pole is retained.  Finite rational algebra only; no xi/RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Callable


Q = Fraction


def b(p: Q, z: Q) -> Q:
    return (z - p) / (z + p)


def bprod(points: tuple[Q, ...], z: Q) -> Q:
    out = Q(1)
    for p in points:
        out *= b(p, z)
    return out


def kernel(f: Callable[[Q], Q], z: Q, w: Q) -> Q:
    return (1 - f(z) * f(w)) / (z + w)


def det(matrix: list[list[Q]]) -> Q:
    a = [row[:] for row in matrix]
    n = len(a)
    ans = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            ans = -ans
        piv = a[j][j]
        ans *= piv
        for k in range(j, n):
            a[j][k] /= piv
        for i in range(j + 1, n):
            c = a[i][j]
            if c:
                for k in range(j, n):
                    a[i][k] -= c * a[j][k]
    return ans


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    points = (Q(1, 3), Q(2, 5), Q(4, 3), Q(5, 2))
    delta_points = (Q(1), Q(2), Q(4))
    zero_port_points = (Q(3, 2),)
    analytic_points = (Q(5, 3), Q(7, 3))

    def Delta(z: Q) -> Q:
        return bprod(delta_points, z)

    def B(z: Q) -> Q:
        return bprod(zero_port_points, z)

    def A(z: Q) -> Q:
        return bprod(analytic_points, z)

    def Theta(z: Q) -> Q:
        return A(z) / B(z)

    def I(z: Q) -> Q:
        return Delta(z) * A(z)

    decomposition_checks = 0
    for z in points:
        for w in points:
            source = kernel(I, z, w) / (
                Delta(z) * B(z) * Delta(w) * B(w)
            )
            critical = kernel(Theta, z, w)
            stable = kernel(Delta, z, w) / (
                Delta(z) * B(z) * Delta(w) * B(w)
            )
            hyperbolic = kernel(B, z, w) / (B(z) * B(w))
            assert source == critical + stable + hyperbolic
            decomposition_checks += 1

    rank_one_checks = 0
    p = zero_port_points[0]
    for z in points:
        for w in points:
            lhs = kernel(B, z, w) / (B(z) * B(w))
            rhs = 2 * p / ((z - p) * (w - p))
            assert lhs == rhs
            rank_one_checks += 1

    # The nonconstant one-pole port has rank one and is PSD.
    H = [
        [kernel(B, z, w) / (B(z) * B(w)) for w in points]
        for z in points
    ]
    psd_checks = 0
    for n in range(1, len(points) + 1):
        minor = [row[:n] for row in H[:n]]
        d = det(minor)
        assert d >= 0
        if n == 1:
            assert d > 0
        else:
            assert d == 0
        psd_checks += 1

    # Delete the pole factor: exact critical+stable exhaustion.
    def Theta0(z: Q) -> Q:
        return A(z)

    def I0(z: Q) -> Q:
        return Delta(z) * A(z)

    exhaustion_checks = 0
    for z in points:
        for w in points:
            source = kernel(I0, z, w) / (Delta(z) * Delta(w))
            critical = kernel(Theta0, z, w)
            stable = kernel(Delta, z, w) / (Delta(z) * Delta(w))
            assert source == critical + stable
            exhaustion_checks += 1

    # With a genuine port, omitting it fails strictly on every diagonal point.
    omission_checks = 0
    minimum_defect = None
    for z in points:
        source = kernel(I, z, z) / (Delta(z) ** 2 * B(z) ** 2)
        critical = kernel(Theta, z, z)
        stable = kernel(Delta, z, z) / (Delta(z) ** 2 * B(z) ** 2)
        defect = source - critical - stable
        assert defect == kernel(B, z, z) / B(z) ** 2
        assert defect > 0
        minimum_defect = (
            defect if minimum_defect is None else min(minimum_defect, defect)
        )
        omission_checks += 1

    proof_text = (
        f"{decomposition_checks}|{rank_one_checks}|{psd_checks}|"
        f"{exhaustion_checks}|{omission_checks}|{minimum_defect}"
    )
    result = {
        "classification": "PASS_CANONICAL_COISOMETRY_EXHAUSTION_EQUIVALENCE",
        "checks": (
            decomposition_checks
            + rank_one_checks
            + psd_checks
            + exhaustion_checks
            + omission_checks
        ),
        "decomposition_checks": decomposition_checks,
        "rank_one_port_checks": rank_one_checks,
        "port_psd_minor_checks": psd_checks,
        "zero_port_exhaustion_checks": exhaustion_checks,
        "nonzero_port_omission_failures": omission_checks,
        "minimum_exact_diagonal_port_defect": str(minimum_defect),
        "proof_object_sha256": hashlib.sha256(proof_text.encode()).hexdigest(),
        "scope": (
            "exact finite rational model-space algebra only; "
            "does not identify the arithmetic tangent source, remove xi zero ports, "
            "or prove RH"
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print("PASS_CANONICAL_COISOMETRY_EXHAUSTION_EQUIVALENCE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
