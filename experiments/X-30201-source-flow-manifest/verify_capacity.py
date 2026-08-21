#!/usr/bin/env python3
"""Exact finite regression for Hausdorff source mass versus central capacity."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


def check_eta_layer_cake(limit: int = 300) -> dict[str, object]:
    cases = 0
    for N in range(3, limit + 1):
        c = [Fraction(0)] * (N + 2)
        for n in range(2, N + 1):
            c[n] = Fraction(1, n)
        d = [Fraction(0)] * (N + 1)
        for n in range(2, N + 1):
            d[n] = c[n] - c[n + 1]
            assert d[n] >= 0
        for q in range(2, N + 1):
            # The complete central tree T_n has carry load floor(n/q).
            flow_load = sum(d[n] * (n // q) for n in range(2, N + 1))
            source_load = sum(c[m] for m in range(q, N + 1, q))
            assert flow_load == source_load, (N, q, flow_load, source_load)
            cases += 1
    return {"cases": cases, "limit_N": limit}


def check_capacity_ratio(limit_k: int = 10000) -> dict[str, object]:
    cases = 0
    for k in range(1, limit_k + 1):
        A = Fraction(1, 2 * k)
        B = Fraction(1, 2 * k + 1)
        root = A - B
        assert root == Fraction(1, 2 * k * (2 * k + 1))
        assert B / root == 2 * k
        assert root < B
        cases += 1
    return {
        "cases": cases,
        "limit_k": limit_k,
        "first_available": "1/6",
        "first_required": "1/3",
    }


def check_general_decreasing_sources(limit: int = 80) -> dict[str, object]:
    cases = 0
    for N in range(3, limit + 1):
        families = [
            [Fraction(0)] * 2
            + [Fraction(1, n * n) for n in range(2, N + 1)]
            + [Fraction(0)],
            [Fraction(0)] * 2
            + [Fraction(N - n + 1, N * n) for n in range(2, N + 1)]
            + [Fraction(0)],
        ]
        for c in families:
            if len(c) < N + 2:
                c += [Fraction(0)] * (N + 2 - len(c))
            for n in range(2, N):
                assert c[n] >= c[n + 1] >= 0
            d = [Fraction(0)] * (N + 1)
            for n in range(2, N + 1):
                d[n] = c[n] - c[n + 1]
                assert d[n] >= 0
            for q in range(2, N + 1):
                flow_load = sum(d[n] * (n // q) for n in range(2, N + 1))
                source_load = sum(c[m] for m in range(q, N + 1, q))
                assert flow_load == source_load
                cases += 1
    return {"cases": cases, "limit_N": limit}


def main() -> None:
    results = {
        "schema": "X-30202-central-capacity-v1",
        "classification": "EXACT_FINITE_ALGEBRA_ONLY",
        "checks": {
            "eta_tree_layer_cake": check_eta_layer_cake(),
            "eta_capacity_ratio": check_capacity_ratio(),
            "general_decreasing_sources": check_general_decreasing_sources(),
        },
        "does_not_prove": [
            "SFC",
            "cycle-adjusted capacity feasibility",
            "Cycle Debt",
            "RH",
        ],
    }
    canonical = json.dumps(results, indent=2, sort_keys=True) + "\n"
    results["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(results, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "capacity-verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
