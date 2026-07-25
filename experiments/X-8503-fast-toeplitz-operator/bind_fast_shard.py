#!/usr/bin/env python3
"""Bind a raw fast Toeplitz midpoint shard to an exact source plan.

The C++ producer obtains parameter and normalization fingerprints from the
committed manifest. This exact wrapper adds redundant human-readable common
fields, binds the precise producer Git blob, and hashes the complete shard. It
refuses to repair a fingerprint, range, lag, operation-order, or source mismatch.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

RAW_SCHEMA = "riemann.piecewise-carrier-fast-toeplitz-midpoint-shard.v1"
PLAN_SCHEMA = "riemann.hybrid-toeplitz-source-plan.v1"
ARITHMETIC_CONTRACT = (
    "x86 binary80 nearest basic arithmetic; binary128 segment-relative phase; "
    "MPFR setup; M=32768 R=3; two-hat coefficient deposits; balanced pairwise "
    "summation; zero guarded support-boundary events"
)


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not an integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def canonical_sha(data: Any) -> str:
    encoded = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def git_blob_sha1(path: Path) -> str:
    try:
        content = path.read_bytes()
    except OSError as exc:
        raise CertificateError(f"{path}: {exc}") from exc
    header = f"blob {len(content)}\0".encode("ascii")
    return hashlib.sha1(header + content).hexdigest()


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError(f"{path}: root must be an object")
    return value


def bind(
    raw: dict[str, Any],
    plan: dict[str, Any],
    producer_git_blob_sha1: str,
) -> dict[str, Any]:
    if raw.get("schema") != RAW_SCHEMA:
        raise CertificateError("wrong raw fast-shard schema")
    if plan.get("schema") != PLAN_SCHEMA:
        raise CertificateError("wrong source-plan schema")
    expected_blob = plan.get("fast_producer_git_blob_sha1")
    if not isinstance(expected_blob, str) or len(expected_blob) != 40:
        raise CertificateError("source plan lacks a producer Git-blob fingerprint")
    if producer_git_blob_sha1 != expected_blob:
        raise CertificateError("producer Git-blob fingerprint mismatch")
    if raw.get("vector_independent") is not True:
        raise CertificateError("fast shard must be vector independent")
    if raw.get("include_higher_powers") is not False:
        raise CertificateError("fast shard may not include higher powers")
    if raw.get("arithmetic_contract") != ARITHMETIC_CONTRACT:
        raise CertificateError("arithmetic contract mismatch")
    if raw.get("parameter_sha256") != plan.get("parameter_sha256"):
        raise CertificateError("parameter fingerprint mismatch")
    if raw.get("normalization_sha256") != plan.get("normalization_sha256"):
        raise CertificateError("normalization fingerprint mismatch")
    if parse_int(raw.get("phase_grid_M"), "phase_grid_M") != 32768:
        raise CertificateError("phase grid mismatch")
    if parse_int(raw.get("phase_taylor_R"), "phase_taylor_R") != 3:
        raise CertificateError("phase Taylor order mismatch")
    if parse_int(raw.get("log_series_terms"), "log_series_terms") != 4:
        raise CertificateError("log series order mismatch")
    if parse_int(raw.get("sqrt_polynomial_degree"), "sqrt_polynomial_degree") != 5:
        raise CertificateError("sqrt polynomial degree mismatch")
    if parse_int(raw.get("setup_precision_bits"), "setup_precision_bits") < 128:
        raise CertificateError("setup precision too small")
    if parse_int(
        raw.get("guarded_support_boundary_count"),
        "guarded_support_boundary_count",
    ) != 0:
        raise CertificateError("guarded support boundary requires directed fallback")

    cells = parse_int(plan.get("cells"), "plan.cells")
    total_segments = parse_int(plan.get("total_segments"), "plan.total_segments")
    fast_start = parse_int(plan.get("fast_start_segment"), "plan.fast_start_segment")
    start = parse_int(raw.get("segment_start"), "segment_start")
    end = parse_int(raw.get("segment_end"), "segment_end")
    if not (fast_start <= start < end <= total_segments):
        raise CertificateError("fast shard range is outside licensed late range")
    rows = raw.get("lags")
    if not isinstance(rows, list) or len(rows) != cells:
        raise CertificateError("fast shard lag count mismatch")
    if [parse_int(row.get("lag"), "lag") for row in rows] != list(range(cells)):
        raise CertificateError("fast shard lag ordering mismatch")

    primes = parse_int(raw.get("prime_count"), "prime_count")
    higher = parse_int(raw.get("higher_prime_power_count"), "higher_prime_power_count")
    terms = parse_int(raw.get("total_terms"), "total_terms")
    if min(primes, higher, terms) < 0 or higher != 0 or terms != primes:
        raise CertificateError("fast shard term counts are inconsistent")

    bound = dict(raw)
    bound.update(
        {
            "cutoff": parse_int(plan.get("cutoff"), "plan.cutoff"),
            "carrier": plan.get("carrier"),
            "cells": cells,
            "segment_size": parse_int(plan.get("segment_size"), "plan.segment_size"),
            "total_segments": total_segments,
            "binding": {
                "plan_schema": PLAN_SCHEMA,
                "parameter_sha256": plan.get("parameter_sha256"),
                "normalization_sha256": plan.get("normalization_sha256"),
                "producer_git_blob_sha1": producer_git_blob_sha1,
                "status": "BOUND_TO_EXACT_SOURCE_PLAN",
            },
        }
    )
    bound.pop("binding_sha256", None)
    bound["binding_sha256"] = canonical_sha(bound)
    return bound


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("raw_shard", type=Path)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--producer-source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        result = bind(
            load(args.raw_shard),
            load(args.plan),
            git_blob_sha1(args.producer_source),
        )
        code = 0
    except CertificateError as exc:
        result = {
            "schema": RAW_SCHEMA,
            "status": "REJECTED",
            "reason": str(exc),
        }
        code = 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
