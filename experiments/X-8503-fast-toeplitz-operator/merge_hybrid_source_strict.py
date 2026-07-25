#!/usr/bin/env python3
"""Strict binding layer for merge_hybrid_source.py.

This wrapper recomputes the self-hash of the L-8505 budget verification and the
binding hash of every fast shard before delegating to the exact coefficient and
radius merger.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import merge_hybrid_source as base

PLAN_SCHEMA = base.PLAN_SCHEMA
BUDGET_SCHEMA = base.BUDGET_SCHEMA
FAST_SCHEMA = base.FAST_SCHEMA
OUTPUT_SCHEMA = base.OUTPUT_SCHEMA
CertificateError = base.CertificateError
parse_fraction = base.parse_fraction
canonical_sha = base.canonical_sha

ARITHMETIC_CONTRACT = (
    "x86 binary80 nearest basic arithmetic; binary128 segment-relative phase; "
    "MPFR setup; M=32768 R=3; two-hat coefficient deposits; balanced pairwise "
    "summation; zero guarded support-boundary events"
)


def verify_self_hash(data: dict[str, Any], field: str, name: str) -> str:
    claimed = data.get(field)
    if not isinstance(claimed, str) or len(claimed) != 64:
        raise CertificateError(f"{name}: missing canonical hash")
    body = dict(data)
    body.pop(field, None)
    actual = canonical_sha(body)
    if actual != claimed:
        raise CertificateError(f"{name}: canonical hash mismatch")
    return claimed


def merge(
    plan: dict[str, Any],
    budget: dict[str, Any],
    shards: list[tuple[str, dict[str, Any]]],
) -> dict[str, Any]:
    if plan.get("schema") != PLAN_SCHEMA:
        raise CertificateError("wrong source-plan schema")
    expected_budget_sha = plan.get("fast_budget_verification_sha256")
    if not isinstance(expected_budget_sha, str) or len(expected_budget_sha) != 64:
        raise CertificateError("plan lacks fast-budget verification fingerprint")
    budget_sha = verify_self_hash(
        budget,
        "verification_sha256",
        "fast budget verification",
    )
    if budget_sha != expected_budget_sha:
        raise CertificateError("fast-budget verification fingerprint mismatch")

    for path, shard in shards:
        if shard.get("schema") != FAST_SCHEMA:
            continue
        if shard.get("arithmetic_contract") != ARITHMETIC_CONTRACT:
            raise CertificateError(f"{path}: arithmetic contract mismatch")
        if shard.get("binding", {}).get("status") != "BOUND_TO_EXACT_SOURCE_PLAN":
            raise CertificateError(f"{path}: fast shard is not bound to the source plan")
        verify_self_hash(shard, "binding_sha256", path)
        if shard.get("parameter_sha256") != plan.get("parameter_sha256"):
            raise CertificateError(f"{path}: parameter fingerprint mismatch")
        if shard.get("normalization_sha256") != plan.get("normalization_sha256"):
            raise CertificateError(f"{path}: normalization fingerprint mismatch")
        for field, expected in (
            ("phase_grid_M", 32768),
            ("phase_taylor_R", 3),
            ("log_series_terms", 4),
            ("sqrt_polynomial_degree", 5),
        ):
            if base.parse_int(shard.get(field), f"{path}.{field}") != expected:
                raise CertificateError(f"{path}: {field} mismatch")
        if base.parse_int(
            shard.get("setup_precision_bits"),
            f"{path}.setup_precision_bits",
        ) < 128:
            raise CertificateError(f"{path}: setup precision is too small")

    result = base.merge(plan, budget, shards)
    result["strict_binding"] = {
        "fast_budget_verification_sha256": budget_sha,
        "bound_fast_shards": sum(
            shard.get("schema") == FAST_SCHEMA for _, shard in shards
        ),
        "status": "CANONICAL_HASHES_REPLAYED",
    }
    # Replace the base hash because the strict-binding object is part of the
    # accepted proof object.
    result.pop("reference_sha256", None)
    result["reference_sha256"] = canonical_sha(result)
    return result


def load(path: Path) -> dict[str, Any]:
    return base.load_json(path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("budget_verification", type=Path)
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = merge(
            load(args.plan),
            load(args.budget_verification),
            [(str(path), load(path)) for path in args.shards],
        )
        code = 0
    except CertificateError as exc:
        result = {
            "schema": OUTPUT_SCHEMA,
            "status": "REJECTED",
            "reason": str(exc),
        }
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
