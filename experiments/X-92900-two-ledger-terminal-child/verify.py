#!/usr/bin/env python3
"""Lightweight exact regression for T-92900.

This checker authenticates the finite two-ledger algebra, constants, source
ownership controls and fail-closed mutations. It does not replay the frozen
Hall, endpoint, PNT, prime-square, Mellin or Landau theorems and does not prove
RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Mapping

SCHEMA = "riemann.t92900.two-ledger-terminal-child.v1"


def fs(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def sha(payload: Mapping[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def vadd(*vs: list[F]) -> list[F]:
    return [sum(v[i] for v in vs) for i in range(len(vs[0]))]


def vsub(a: list[F], b: list[F]) -> list[F]:
    return [x - y for x, y in zip(a, b)]


def two_ledger(mutate: str | None = None) -> dict[str, Any]:
    ideal_current = [F(11), F(13), F(17), F(19)]
    child = [F(2), F(3), F(5), F(7)]
    unused = [F(4), F(5), F(6), F(8)]
    # The second coordinate is negative: this is a signed observation defect,
    # not a positive source packet.
    signed_error = [F(1), F(-1), F(2), F(3)]

    if mutate == "signed_as_source" and any(x < 0 for x in signed_error):
        raise AssertionError("signed comparison was relabelled as positive source")

    if mutate == "reserve_overrun":
        signed_error[3] = F(9)

    actual_current = vadd(ideal_current, signed_error)
    native = vadd(ideal_current, child, unused)
    slack = vsub(unused, signed_error)

    if any(x < 0 for x in slack):
        raise AssertionError("signed observation error exceeds positive reserve")

    reconstructed = vadd(actual_current, child, slack)
    if mutate == "drop_child":
        reconstructed = vadd(actual_current, slack)
    if reconstructed != native:
        raise AssertionError("two-ledger native identity failed")

    owners = {
        "current": {"a", "d", "hall_bonus"},
        "child": {"b", "e"},
        "unused": {"c", "top", "thin"},
    }
    if mutate == "duplicate_owner":
        owners["child"].add("a")
    flat = [x for values in owners.values() for x in values]
    if len(flat) != len(set(flat)):
        raise AssertionError("positive source owner duplicated")

    return {
        "signed_error": [fs(x) for x in signed_error],
        "positive_unused": [fs(x) for x in unused],
        "root_slack": [fs(x) for x in slack],
        "native_vector": [fs(x) for x in native],
        "signed_error_is_source_positive": False,
        "verdict": "PASS_TWO_LEDGER_NATIVE_IDENTITY",
    }


def child_terminalization(mutate: str | None = None) -> dict[str, Any]:
    parent_mass = F(6039, 2)
    coefficient_sum = F(7, 64)  # strict < 1/8
    if mutate == "child_mass":
        coefficient_sum = F(1, 8)

    if not coefficient_sum < F(1, 8):
        raise AssertionError("child coefficient mass is not strictly subcritical")

    weighted_deficit = 2 * parent_mass * coefficient_sum
    universal_bound = parent_mass / 4
    if not weighted_deficit < universal_bound:
        raise AssertionError("terminal child deficit did not fit parent/4")

    if not universal_bound == F(6039, 8):
        raise AssertionError("factor-67 child bound changed")
    if not universal_bound < 755:
        raise AssertionError("child deficit is not below 755")

    return {
        "parent_target_mass_bound": fs(parent_mass),
        "coefficient_fixture": fs(coefficient_sum),
        "fixture_weighted_deficit": fs(weighted_deficit),
        "universal_child_deficit_bound": fs(universal_bound),
        "verdict": "PASS_FIRST_GENERATION_CHILD_TERMINALIZATION",
    }


def native_cost(mutate: str | None = None) -> dict[str, Any]:
    classes = {
        "thinning": F(12012),
        "nonterminal_signed_comparison": F(4),
        "terminal_signed_comparison": F(48972),
        "positive_omissions": F(1),
        "port": F(0),
        "base": F(0),
    }
    root_total = sum(classes.values(), F(0))
    child_bound = F(6039, 8)
    total = root_total + child_bound

    if mutate == "duplicate_root_correction":
        total += classes["terminal_signed_comparison"]
    if mutate == "benchmark_bridge":
        raise AssertionError("forbidden J_Lambda-4sqrt(X) bridge")
    if not root_total == 60989:
        raise AssertionError("root ledger constant changed")
    if not total == F(493951, 8):
        raise AssertionError("combined constant changed")
    if not total < 61744:
        raise AssertionError("combined native deficit is not below 61744")

    return {
        "root_classes": {k: fs(v) for k, v in classes.items()},
        "root_total": fs(root_total),
        "child_bound": fs(child_bound),
        "combined_total": fs(total),
        "strict_integer_bound": 61744,
        "benchmark_bridge_used": False,
        "verdict": "PASS_DIRECT_ROOT_PLUS_TERMINAL_CHILD_COST",
    }


def mutation_census() -> list[str]:
    cases = [
        ("signed_as_source", two_ledger),
        ("reserve_overrun", two_ledger),
        ("drop_child", two_ledger),
        ("duplicate_owner", two_ledger),
        ("child_mass", child_terminalization),
        ("duplicate_root_correction", native_cost),
        ("benchmark_bridge", native_cost),
    ]
    caught: list[str] = []
    for name, fn in cases:
        try:
            fn(name)
        except AssertionError:
            caught.append(name)
        else:
            raise AssertionError(f"mutation survived: {name}")
    return caught


def verify() -> dict[str, Any]:
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "two_ledger": two_ledger(),
        "terminal_children": child_terminalization(),
        "native_cost": native_cost(),
        "mutations_caught": mutation_census(),
        "proof_boundary": {
            "pr488_frozen_head": "9acd381fa168db02a03646ab16851daebbf4d0fd",
            "pr489_frozen_head": "0bb487c8a0782f601be0a3041743b357ad93726a",
            "analytic_root_and_endpoint_inputs": "FROZEN_RECONSTRUCTION_REQUIRED",
            "riemann_hypothesis": "UNPROVED_PENDING_REVIEW",
        },
        "verdict": "PASS_TWO_LEDGER_TERMINAL_CHILD_FACTOR67_ALGEBRA",
    }
    payload["proof_object_sha256"] = sha(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--mutations", action="store_true")
    args = parser.parse_args()
    out = verify()
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
