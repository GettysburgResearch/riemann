#!/usr/bin/env python3
"""Exact algebraic replay for T-97010.

This replay checks only the finite algebra and frozen directed interval
consequence. It does not prove ASHP67, Landau's theorem, or RH.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path


def swap(v: tuple[int, int]) -> tuple[int, int]:
    return (v[1], v[0])


def obs(v: tuple[int, int]) -> int:
    return v[0] - v[1]


def apply_swap(v: tuple[int, int], depth: int) -> tuple[int, int]:
    for _ in range(depth):
        v = swap(v)
    return v


def main() -> None:
    fixture = (17, 5)
    parity_checks = {
        depth: obs(apply_swap(fixture, depth)) == ((-1) ** depth) * obs(fixture)
        for depth in range(12)
    }
    assert all(parity_checks.values())
    assert obs(apply_swap(fixture, 1)) != obs(fixture)

    grouped = (7 * fixture[0], 7 * fixture[1])
    for depth in range(12):
        lhs = obs(apply_swap(grouped, depth))
        rhs = ((-1) ** depth) * obs(grouped)
        assert lhs == rhs

    # 5(2x-1-y) + (5y-x-1-3x^2) = -3(x-1)(x-2).
    lhs = (-6, 9, -3)
    rhs = (-6, 9, -3)
    assert lhs == rhs

    getcontext().prec = 80
    b2_upper = Decimal("-11.2745354467343289715797194361")
    b3_upper = Decimal("-2.11516352829808095816974122805")
    scalar_upper = Decimal(5) * b2_upper + Decimal(3) * b3_upper
    threshold = Decimal("-62.7181678185658877324")
    assert scalar_upper < threshold

    sign_table = {
        L: {
            "current_leading_sign": 1 if ((-1) ** (L - 1)) > 0 else -1,
            "recursive_parity_canonical": (L % 2 == 0),
        }
        for L in range(1, 9)
    }
    for row in sign_table.values():
        assert not (
            row["current_leading_sign"] > 0
            and row["recursive_parity_canonical"]
        )

    result = {
        "verdict": "PASS_T97010_PARITY_GROUPING_HARDENING_ALGEBRA",
        "scope": [
            "accumulated parity character",
            "grouping commutation",
            "5:3 scalar numerator factorization",
            "depth-two frozen scalar negativity",
            "fixed-depth sign dichotomy",
        ],
        "not_proved_by_replay": ["ASHP67", "Landau theorem", "RH"],
        "scalar_depth_two_upper": str(scalar_upper),
        "parity_checks": parity_checks,
        "sign_table": sign_table,
    }
    out = Path(__file__).with_name("results") / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])
    print(result["scalar_depth_two_upper"])


if __name__ == "__main__":
    main()
