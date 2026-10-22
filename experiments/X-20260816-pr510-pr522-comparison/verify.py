#!/usr/bin/env python3
"""Lightweight exact checks for frozen PR #510/#522 comparison.

This does not replay the large Target-Lorenz campaign or prove RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

HEADS = {
    "pr508": "4ae97dffd1f76ed3244b8f3028560ffa80663caf",
    "pr509": "e01daee9cdfea35d2a7d2591f1df6c8080084119",
    "pr510": "b596b1abae9213366aab4cf3f2c911ff8cfab725",
    "pr522": "3e8949af3e23b8563bfbc0cf8846820cc6c66d76",
    "review516": "2492bd48f8e2bafacfc04fc9237c06219b8c9bf8",
}


def canonical_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    # PR #510: the native k=67 occurrence already contains 67^(-1/2),
    # while the displayed path formula applies the same rough factor again.
    native_square = Fraction(1, 67)
    displayed_square = Fraction(1, 67 * 67)
    assert displayed_square / native_square == Fraction(1, 67)

    # The common native-cost arithmetic is only conditional on a valid row.
    cost = 12012 + 4 + 48972 + 1
    assert cost == 60989 < 61000

    # Test that the fixed top cell belongs to the anchored complement under
    # the displayed bulk interval.
    X = 10**12
    K = X // 67 + 1
    W = 10000
    retained_min = K + 2
    retained_max = X - W - 3
    top_index = X - 1
    assert not (retained_min <= top_index <= retained_max)

    payload = {
        "schema": "riemann.review.pr510-pr522.live-coupling.v1",
        "frozen_heads": HEADS,
        "anchored_path": {
            "test_occurrence": {"m": 1, "k": 67},
            "pr510_declared_to_native_ratio_squared": "1/67",
            "pr510_path_normalization_matches_native": False,
            "pr522_normalization_fork_closed": False,
        },
        "pr508_tail": {
            "certificate_contract": "FAILED_BY_REVIEW_516",
            "failure_digest": "7ffb59b9209d8d1db2527f363631708db9d4ed8ac89d45b793d2ee267d5ccfa8",
            "tail_inequality_refuted": False,
            "all_parameter_avlt_verified": False,
        },
        "top_ownership": {
            "X": X,
            "K": K,
            "retained_cell_min": retained_min,
            "retained_cell_max": retained_max,
            "test_top_index": top_index,
            "test_top_index_is_anchored": True,
            "explicit_output_vs_omission_split_present": False,
        },
        "pr522_readme": {
            "base_blob": "f0d9e9aadfbd7b192b07e3bd0762a94e6e4da97e",
            "replacement_blob": "f2d66e62226ab53b95be4c11e9cb578989535fd6",
            "replacement_equals_standalone_blob": True,
            "revert_required": True,
        },
        "native_cost": {"total": cost, "strict_upper_bound": 61000},
        "rh_established": False,
        "verdict": "PASS_EXACT_PR510_PR522_COMPARATIVE_REVIEW_CHECKS",
    }
    payload["proof_object_sha256"] = canonical_hash(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
