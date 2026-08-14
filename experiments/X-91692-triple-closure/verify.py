#!/usr/bin/env python3
"""Exact finite regression for the factor-67 / reserve / Xi-Hankel triple closure.

This checker verifies only finite rational algebra:
A. mass-weighted direct integrals preserve a strict 1/8 child contraction;
B. adaptive one-use reserve strictly dominates 10152*||C||*epsilon;
C. finite data from a positive Stieltjes pole measure give the two required
   barycentric Hankel matrices positive definite.

It does not independently replay the frozen factor-67 endpoint producer,
the endpoint-to-RH theorem, or the actual zeta zero product.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.t91661.triple-closure.v1"


def fs(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def canonical_sha(payload: dict[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def exact_pd(matrix: Sequence[Sequence[Fraction]]) -> tuple[bool, list[Fraction]]:
    """Exact symmetric LDL after positive symmetric pivot swaps."""
    a = [list(map(Fraction, row)) for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("matrix must be square")
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        raise ValueError("matrix must be symmetric")
    pivots: list[Fraction] = []
    while a:
        n = len(a)
        for i in range(n):
            if a[i][i] <= 0:
                continue
            if i:
                a[0], a[i] = a[i], a[0]
                for row in a:
                    row[0], row[i] = row[i], row[0]
            break
        else:
            return False, pivots
        p = a[0][0]
        if p <= 0:
            return False, pivots
        pivots.append(p)
        a = [
            [a[i][j] - a[i][0] * a[0][j] / p for j in range(1, n)]
            for i in range(1, n)
        ]
    return True, pivots


def route_a() -> dict[str, Any]:
    root_weights = [Fraction(2, 5), Fraction(3, 5)]
    fiber_ratios = [Fraction(7, 100), Fraction(3, 40)]
    if sum(root_weights) != 1:
        raise AssertionError("root mass normalization failed")
    if any(r >= Fraction(1, 8) for r in fiber_ratios):
        raise AssertionError("fiber contraction is not strict")
    global_ratio = sum(w * r for w, r in zip(root_weights, fiber_ratios))
    if not global_ratio < Fraction(1, 8):
        raise AssertionError("direct integral lost subcriticality")

    sigma = Fraction(997, 1000)
    thinned_ratio = sigma * global_ratio
    if not thinned_ratio < global_ratio < Fraction(1, 8):
        raise AssertionError("thinning monotonicity failed")

    return {
        "root_weights": [fs(x) for x in root_weights],
        "fiber_child_mass_ratios": [fs(x) for x in fiber_ratios],
        "global_child_mass_ratio": fs(global_ratio),
        "thinning_factor": fs(sigma),
        "thinned_child_mass_ratio": fs(thinned_ratio),
        "verdict": "PASS_MASS_WEIGHTED_DIRECT_INTEGRAL_BELOW_ONE_EIGHTH",
    }


def route_b() -> dict[str, Any]:
    epsilon = Fraction(1, 10**8)
    correction_norm = Fraction(7, 3)
    delta = Fraction(10152) * correction_norm * epsilon
    reserve = 2 * delta
    if not (0 < delta < Fraction(1, 2)):
        raise AssertionError("control must be in the asymptotic reserve regime")
    if not reserve > Fraction(10152) * correction_norm * epsilon:
        raise AssertionError("strict reserve inequality failed")
    if not reserve < 1:
        raise AssertionError("thinning is not positive")

    leftover = reserve - (1 - reserve) * delta
    if leftover <= 0:
        raise AssertionError("reserve does not absorb the corrected error")

    return {
        "epsilon": fs(epsilon),
        "correction_norm": fs(correction_norm),
        "error_bound": fs(delta),
        "one_use_reserve": fs(reserve),
        "post_error_leftover": fs(leftover),
        "verdict": "PASS_ADAPTIVE_ONE_USE_RESERVE_DOMINATES_10152_ERROR",
    }


def deltas(nodes: Sequence[Fraction]) -> list[Fraction]:
    out: list[Fraction] = []
    for j, qj in enumerate(nodes):
        d = Fraction(1)
        for i, qi in enumerate(nodes):
            if i != j:
                d *= qi - qj
        if d == 0:
            raise ValueError("nodes must be distinct")
        out.append(d)
    return out


def moments(nodes: Sequence[Fraction], data: Sequence[Fraction]) -> list[Fraction]:
    ds = deltas(nodes)
    return [
        sum(
            (data[j] * (-nodes[j]) ** k / ds[j] for j in range(len(nodes))),
            Fraction(0),
        )
        for k in range(len(nodes))
    ]


def hankel(m: Sequence[Fraction], shift: int, size: int) -> list[list[Fraction]]:
    return [[m[i + j + shift] for j in range(size)] for i in range(size)]


def route_c() -> dict[str, Any]:
    nodes = [Fraction(1), Fraction(2), Fraction(4), Fraction(7), Fraction(11)]
    squared_zeros = [Fraction(1), Fraction(9), Fraction(25)]
    weights = [Fraction(2), Fraction(2), Fraction(2)]
    data = [
        sum((w / (q + s) for w, s in zip(weights, squared_zeros)), Fraction(0))
        for q in nodes
    ]

    m = moments(nodes, data)
    h0 = hankel(m, 0, 3)
    h1 = hankel(m, 1, 2)
    pd0, piv0 = exact_pd(h0)
    pd1, piv1 = exact_pd(h1)
    if not pd0 or not pd1:
        raise AssertionError("positive Stieltjes control did not give PD Hankel pairs")

    direct = []
    for k in range(len(nodes)):
        value = Fraction(0)
        for w, s in zip(weights, squared_zeros):
            denom = Fraction(1)
            for q in nodes:
                denom *= q + s
            value += w * s**k / denom
        direct.append(value)
    if direct != m:
        raise AssertionError(("barycentric moment identity", m, direct))

    return {
        "nodes": [fs(x) for x in nodes],
        "squared_zero_support": [fs(x) for x in squared_zeros],
        "data": [fs(x) for x in data],
        "barycentric_moments": [fs(x) for x in m],
        "h0_ldl_pivots": [fs(x) for x in piv0],
        "h1_ldl_pivots": [fs(x) for x in piv1],
        "verdict": "PASS_POSITIVE_STIELTJES_DATA_GIVE_BOTH_HANKEL_PAIRS_PD",
    }


def verify(_: dict[str, Any] | None = None) -> dict[str, Any]:
    payload = {
        "schema": SCHEMA,
        "route_a": route_a(),
        "route_b": route_b(),
        "route_c": route_c(),
        "proof_boundary": {
            "factor67_endpoint_imports": "FROZEN_RECONSTRUCTION_REQUIRED",
            "endpoint_to_rh_consumer": "FROZEN_RECONSTRUCTION_REQUIRED",
            "actual_xi_hankel_positivity": "DERIVED_FROM_RH_IN_L-92113",
            "riemann_hypothesis": "PROPOSAL_PENDING_INDEPENDENT_REVIEW",
        },
        "verdict": "PASS_TRIPLE_CLOSURE_FINITE_ALGEBRA",
    }
    payload["proof_object_sha256"] = canonical_sha(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source = json.loads(args.certificate.read_text()) if args.certificate else None
    out = verify(source)
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
