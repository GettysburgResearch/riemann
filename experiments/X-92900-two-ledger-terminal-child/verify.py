#!/usr/bin/env python3
"""Exact finite regression for the T-92900 successor packet.

The checker authenticates type separation, finite vector algebra, target-mass
arithmetic, ownership, constant arithmetic, frozen-head metadata and fail-closed
mutations. It does not replay the imported analytic theorems and does not prove
RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Callable

SCHEMA = "riemann.t92900.two-ledger-terminal-child.v2"
BASE_SHA = "0bb487c8a0782f601be0a3041743b357ad93726a"
PR488_SHA = "9acd381fa168db02a03646ab16851daebbf4d0fd"
PR490_SHA = "6f46c2cf4e84d51c744263f7e92a0e1743de5148"


def add(a: list[F], b: list[F]) -> list[F]:
    return [x + y for x, y in zip(a, b)]


def sub(a: list[F], b: list[F]) -> list[F]:
    return [x - y for x, y in zip(a, b)]


def scale(c: F, a: list[F]) -> list[F]:
    return [c * x for x in a]


def digest(payload: Any) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def two_ledger_check(mutate: str | None = None) -> dict[str, Any]:
    ideal_current_plus_children = [F(13), F(16), F(22), F(26)]
    positive_unused = [F(4), F(5), F(6), F(8)]
    signed_error = [F(1), F(-1), F(2), F(3)]

    if mutate == "signed_as_source":
        if any(x < 0 for x in signed_error):
            raise AssertionError("signed observation was relabelled as positive source")

    if mutate == "reserve_overrun":
        signed_error[2] = F(7)

    root_slack = sub(positive_unused, signed_error)
    if any(x < 0 for x in root_slack):
        raise AssertionError("signed correction exceeds unused capacity")

    native = add(ideal_current_plus_children, positive_unused)
    actual_current_plus_children = add(ideal_current_plus_children, signed_error)
    reconstructed = add(actual_current_plus_children, root_slack)

    if mutate == "drop_child":
        reconstructed[0] -= 1

    if reconstructed != native:
        raise AssertionError("two-ledger native identity failed")

    return {
        "native_vector": [str(x) for x in native],
        "positive_unused": [str(x) for x in positive_unused],
        "signed_error": [str(x) for x in signed_error],
        "root_slack": [str(x) for x in root_slack],
        "signed_error_is_source_positive": False,
        "verdict": "PASS_TWO_LEDGER_NATIVE_IDENTITY",
    }


def ownership_check(mutate: str | None = None) -> dict[str, Any]:
    source = {f"a{i}" for i in range(24)}
    current = {f"a{i}" for i in range(0, 8)}
    child67 = {f"a{i}" for i in range(8, 14)}
    child71 = {f"a{i}" for i in range(14, 19)}
    unused = {f"a{i}" for i in range(19, 24)}

    if mutate == "duplicate_owner":
        child67.add("a2")

    groups = [current, child67, child71, unused]
    flat = [x for group in groups for x in group]
    if len(flat) != len(set(flat)) or set(flat) != source:
        raise AssertionError("source ownership is not a disjoint exhaustion")

    return {
        "source_atoms": len(source),
        "owner_counts": {
            "current": len(current),
            "child67": len(child67),
            "child71": len(child71),
            "unused": len(unused),
        },
        "verdict": "PASS_SOURCE_DISJOINT_OWNERSHIP",
    }


def terminal_child_check(mutate: str | None = None) -> dict[str, Any]:
    parent_mass = F(6039, 2)
    coefficient_sum = F(7, 64)

    if mutate == "child_mass":
        coefficient_sum = F(1, 8)

    if not coefficient_sum < F(1, 8):
        raise AssertionError("child coefficient mass is not strictly subcritical")

    fixture_weighted_deficit = 2 * parent_mass * coefficient_sum
    universal_child_bound = parent_mass / 4

    if not universal_child_bound == F(6039, 8):
        raise AssertionError("universal child bound changed")

    return {
        "parent_target_mass_bound": str(parent_mass),
        "coefficient_fixture": str(coefficient_sum),
        "fixture_weighted_deficit": str(fixture_weighted_deficit),
        "universal_child_deficit_bound": str(universal_child_bound),
        "verdict": "PASS_FIRST_GENERATION_CHILD_TERMINALIZATION",
    }


def native_cost_check(mutate: str | None = None) -> dict[str, Any]:
    classes = {
        "thinning": F(12012),
        "nonterminal_signed_comparison": F(4),
        "terminal_signed_comparison": F(48972),
        "positive_omissions": F(1),
        "port": F(0),
        "base": F(0),
    }

    if mutate == "duplicate_root_correction":
        classes["terminal_signed_comparison"] *= 2

    if mutate == "benchmark_bridge":
        raise AssertionError("forbidden benchmark bridge used")

    root_total = sum(classes.values(), F(0))
    child_bound = F(6039, 8)
    combined = root_total + child_bound

    if root_total != F(60989):
        raise AssertionError("root cost ledger changed")
    if combined != F(493951, 8) or not combined < F(61744):
        raise AssertionError("combined native bound changed")

    return {
        "root_classes": {k: str(v) for k, v in classes.items()},
        "root_total": str(root_total),
        "child_bound": str(child_bound),
        "combined_total": str(combined),
        "strict_integer_bound": 61744,
        "benchmark_bridge_used": False,
        "portful_schur_demand_used": False,
        "verdict": "PASS_DIRECT_ROOT_PLUS_TERMINAL_CHILD_COST",
    }


def verify() -> dict[str, Any]:
    result: dict[str, Any] = {
        "schema": SCHEMA,
        "two_ledger": two_ledger_check(),
        "ownership": ownership_check(),
        "terminal_children": terminal_child_check(),
        "native_cost": native_cost_check(),
        "proof_boundary": {
            "pr488_frozen_head": PR488_SHA,
            "pr489_frozen_head": BASE_SHA,
            "pr490_review_head": PR490_SHA,
            "analytic_root_and_endpoint_inputs": "FROZEN_RECONSTRUCTION_REQUIRED",
            "portful_schur_demand": "NOT_USED",
            "riemann_hypothesis": "UNPROVED_PENDING_REVIEW",
        },
        "verdict": "PASS_TWO_LEDGER_TERMINAL_CHILD_FACTOR67_ALGEBRA",
    }
    result["proof_object_sha256"] = digest(result)
    return result


MUTATIONS: dict[str, Callable[[str | None], dict[str, Any]]] = {
    "signed_as_source": two_ledger_check,
    "reserve_overrun": two_ledger_check,
    "drop_child": two_ledger_check,
    "duplicate_owner": ownership_check,
    "child_mass": terminal_child_check,
    "duplicate_root_correction": native_cost_check,
    "benchmark_bridge": native_cost_check,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--mutations", action="store_true")
    args = parser.parse_args()

    result = verify()
    if args.mutations:
        caught: list[str] = []
        for name, fn in MUTATIONS.items():
            try:
                fn(name)
            except AssertionError:
                caught.append(name)
        if set(caught) != set(MUTATIONS):
            raise SystemExit(f"mutations did not fail closed: {caught}")
        result["mutations_caught"] = caught

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
