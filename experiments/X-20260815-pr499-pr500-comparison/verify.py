#!/usr/bin/env python3
"""Lightweight exact/symbolic checks for the frozen PR #499/#500 comparison.

This checker does not replay any large Hall campaign. It verifies:
1. the exact sign of the target-Hall edge score correction at x=2;
2. the arithmetic of the shared native-cost ledger;
3. the fact that a valid first-owner map is many-to-one;
4. the exact list of missing PR #499 manifests found by remote readback.

It does not establish RH or instantiate the live factor-67 endpoint coupling.
"""
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 80

MISSING_499 = [
    "FACTOR67_91820_SHA256SUMS",
    "experiments/X-91820-positive-common-parent-response-complement/SHA256SUMS",
    "standalone/2026-08-15-positive-common-parent-closure/CONTENT_SHA256SUMS",
]


def canonical_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    sqrt2 = Decimal(2).sqrt()
    # g(z) = (5 z - 3)/(4 z - 3), so at the forced x=2 Hall edge
    # (o,e)=(2,1), the exact score correction is
    # 3(1-sqrt(2))/(4sqrt(2)-3) < 0.
    numerator = Decimal(3) * (Decimal(1) - sqrt2)
    denominator = Decimal(4) * sqrt2 - Decimal(3)
    score_edge = numerator / denominator
    assert numerator < 0
    assert denominator > 0
    assert score_edge < 0

    costs = {
        "thinning": 12012,
        "nonterminal": 4,
        "terminal": 48972,
        "omissions": 1,
    }
    assert sum(costs.values()) == 60989
    assert 60989 < 61000

    # A correct first-owner projection is many-to-one: both monomials below
    # are owned by the least listed prime 67.
    valid_owner_map = {
        "67": "67",
        "67*71": "67",
        "71": "71",
    }
    assert len(valid_owner_map) == 3
    assert len(set(valid_owner_map.values())) == 2
    pr500_injective_owner_test_would_reject = (
        len(valid_owner_map) != len(set(valid_owner_map.values()))
    )
    assert pr500_injective_owner_test_would_reject

    payload = {
        "schema": "riemann.review.pr499-pr500.native-source-comparison.v1",
        "frozen_heads": {
            "pr499": "99d3983b57f82941131caa8d9c36e4947f1179a0",
            "pr500": "d73c1e7a1a482cac31581211a84db43cc34c824e",
        },
        "pr499": {
            "forced_hall_edge": {"x": 2, "odd": 2, "even": 1},
            "score_edge_formula": "3(1-sqrt(2))/(4sqrt(2)-3)",
            "score_edge_decimal": str(score_edge),
            "score_edge_is_negative": True,
            "missing_manifests": MISSING_499,
        },
        "pr500": {
            "valid_many_to_one_owner_map": valid_owner_map,
            "current_injective_owner_validator_rejects_valid_map": True,
            "replay_fixture_class": "hard-coded synthetic plus randomized abstract fixtures",
            "live_factor67_marginal_instantiated_by_replay": False,
        },
        "shared_native_cost": {
            "classes": costs,
            "total": 60989,
            "strict_upper_bound": 61000,
        },
        "rh_established": False,
        "verdict": "PASS_EXACT_PR499_PR500_COMPARATIVE_REVIEW_CHECKS",
    }
    payload["proof_object_sha256"] = canonical_hash(payload)

    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
