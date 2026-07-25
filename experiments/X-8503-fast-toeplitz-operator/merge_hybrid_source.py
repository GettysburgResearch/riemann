#!/usr/bin/env python3
"""Merge directed early Toeplitz boxes and late fast midpoint shards exactly.

The result is one Gaussian-rational Toeplitz reference coefficient vector and one
operator-norm source radius.  Directed rectangle radii are converted through
L-8503.  The L-8505 fast operator budget is added exactly once, independent of
how many fast shards are present.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

DIRECTED_SCHEMA = "riemann.mpfr-toeplitz-box-shard.v1"
FAST_SCHEMA = "riemann.piecewise-carrier-fast-toeplitz-midpoint-shard.v1"
PLAN_SCHEMA = "riemann.hybrid-toeplitz-source-plan.v1"
BUDGET_SCHEMA = "riemann.fast-toeplitz-operator-budget.verification.v1"
OUTPUT_SCHEMA = "riemann.toeplitz-reference-operator-moat.v1"


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


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def parse_hex_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, str):
        raise CertificateError(f"{name} must be a hexadecimal-float string")
    try:
        number = float.fromhex(value)
    except ValueError as exc:
        raise CertificateError(f"{name} is not a hexadecimal float") from exc
    if not number.hex().lower().startswith(("0x", "-0x")) and number != 0:
        raise CertificateError(f"{name} is not finite")
    if number == float("inf") or number == float("-inf") or number != number:
        raise CertificateError(f"{name} must be finite")
    return Fraction.from_float(number)


def canonical_sha(data: Any) -> str:
    encoded = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError(f"{path}: root must be an object")
    return value


@dataclass
class ComplexAccumulator:
    real: Fraction = Fraction(0)
    imaginary: Fraction = Fraction(0)


@dataclass
class Coverage:
    start: int
    end: int
    kind: str
    include_higher_powers: bool
    prime_count: int
    higher_count: int
    total_terms: int
    path: str


def midpoint_radius(lower: Fraction, upper: Fraction, name: str) -> tuple[Fraction, Fraction]:
    if lower > upper:
        raise CertificateError(f"{name}: reversed interval")
    return (lower + upper) / 2, (upper - lower) / 2


def validate_common_parameters(data: dict[str, Any], plan: dict[str, Any], name: str) -> None:
    expected = {
        "cutoff": parse_int(plan.get("cutoff"), "plan.cutoff"),
        "carrier": plan.get("carrier"),
        "cells": parse_int(plan.get("cells"), "plan.cells"),
        "segment_size": parse_int(plan.get("segment_size"), "plan.segment_size"),
        "total_segments": parse_int(plan.get("total_segments"), "plan.total_segments"),
    }
    for key, value in expected.items():
        if data.get(key) != value:
            raise CertificateError(f"{name}: parameter mismatch for {key}")


def merge(
    plan: dict[str, Any],
    budget: dict[str, Any],
    shards: list[tuple[str, dict[str, Any]]],
) -> dict[str, Any]:
    if plan.get("schema") != PLAN_SCHEMA:
        raise CertificateError("wrong source-plan schema")
    if plan.get("status") != "PROOF_PRODUCING_HYBRID_SOURCE_PLAN":
        raise CertificateError("source plan must preserve proof-producing status")
    cells = parse_int(plan.get("cells"), "plan.cells")
    total_segments = parse_int(plan.get("total_segments"), "plan.total_segments")
    fast_start = parse_int(plan.get("fast_start_segment"), "plan.fast_start_segment")
    if not (0 <= fast_start < total_segments):
        raise CertificateError("invalid fast_start_segment")
    expected_counts_raw = plan.get("expected_counts")
    if not isinstance(expected_counts_raw, dict):
        raise CertificateError("plan.expected_counts must be an object")
    expected_counts = {
        key: parse_int(expected_counts_raw.get(key), f"expected_counts.{key}")
        for key in ("prime_count", "higher_prime_power_count", "total_terms")
    }
    parameter_sha = plan.get("parameter_sha256")
    normalization_sha = plan.get("normalization_sha256")
    if not isinstance(parameter_sha, str) or len(parameter_sha) != 64:
        raise CertificateError("invalid parameter fingerprint")
    if not isinstance(normalization_sha, str) or len(normalization_sha) != 64:
        raise CertificateError("invalid normalization fingerprint")

    if budget.get("schema") != BUDGET_SCHEMA or budget.get("verified") is not True:
        raise CertificateError("fast budget is not a verified L-8505 artifact")
    if budget.get("status") != "STATIC_OPERATOR_BUDGET_VERIFIED":
        raise CertificateError("fast budget status mismatch")
    budget_components = budget.get("components")
    if not isinstance(budget_components, dict):
        raise CertificateError("fast budget components missing")
    fast_operator_budget = parse_fraction(budget_components.get("total"), "budget.total")

    coefficient_midpoints = [ComplexAccumulator() for _ in range(cells)]
    direct_operator_radius = Fraction(0)
    coverage: list[Coverage] = []
    fast_shard_count = 0
    directed_shard_count = 0
    prime_count = higher_count = total_terms = 0
    higher_streams = 0

    for path, data in shards:
        schema = data.get("schema")
        name = path
        if schema == DIRECTED_SCHEMA:
            validate_common_parameters(data, plan, name)
            if parse_int(data.get("ambiguous_lags"), f"{name}.ambiguous_lags") != 0:
                raise CertificateError(f"{name}: ambiguous directed support lag")
            start = parse_int(data.get("segment_start"), f"{name}.segment_start")
            end = parse_int(data.get("segment_end"), f"{name}.segment_end")
            include_higher = data.get("include_higher_powers") is True
            rows = data.get("lags")
            if not isinstance(rows, list) or len(rows) != cells:
                raise CertificateError(f"{name}: wrong lag count")
            for lag, row in enumerate(rows):
                if not isinstance(row, dict) or parse_int(row.get("lag"), f"{name}.lag") != lag:
                    raise CertificateError(f"{name}: lag ordering mismatch")
                real_lower = parse_hex_fraction(row.get("real_lower_hex"), f"{name}.real_lower")
                real_upper = parse_hex_fraction(row.get("real_upper_hex"), f"{name}.real_upper")
                imag_lower = parse_hex_fraction(row.get("imag_lower_hex"), f"{name}.imag_lower")
                imag_upper = parse_hex_fraction(row.get("imag_upper_hex"), f"{name}.imag_upper")
                real_mid, real_radius = midpoint_radius(real_lower, real_upper, f"{name}.real")
                imag_mid, imag_radius = midpoint_radius(imag_lower, imag_upper, f"{name}.imag")
                coefficient_midpoints[lag].real += real_mid
                if lag != 0:
                    coefficient_midpoints[lag].imaginary += imag_mid
                    direct_operator_radius += real_radius + imag_radius
                else:
                    # The Hermitian Toeplitz map uses only Re(c_0).
                    direct_operator_radius += real_radius
            directed_shard_count += 1
        elif schema == FAST_SCHEMA:
            validate_common_parameters(data, plan, name)
            if data.get("vector_independent") is not True:
                raise CertificateError(f"{name}: fast coefficient shard is not vector independent")
            if data.get("include_higher_powers") is not False:
                raise CertificateError(f"{name}: fast shard may not include higher powers")
            if data.get("parameter_sha256") != parameter_sha:
                raise CertificateError(f"{name}: parameter fingerprint mismatch")
            if data.get("normalization_sha256") != normalization_sha:
                raise CertificateError(f"{name}: normalization fingerprint mismatch")
            if parse_int(
                data.get("guarded_support_boundary_count"),
                f"{name}.guarded_support_boundary_count",
            ) != 0:
                raise CertificateError(f"{name}: guarded support boundary requires fallback")
            start = parse_int(data.get("segment_start"), f"{name}.segment_start")
            end = parse_int(data.get("segment_end"), f"{name}.segment_end")
            if start < fast_start:
                raise CertificateError(f"{name}: unsupported early fast segment")
            include_higher = False
            rows = data.get("lags")
            if not isinstance(rows, list) or len(rows) != cells:
                raise CertificateError(f"{name}: wrong lag count")
            for lag, row in enumerate(rows):
                if not isinstance(row, dict) or parse_int(row.get("lag"), f"{name}.lag") != lag:
                    raise CertificateError(f"{name}: lag ordering mismatch")
                real_mid = parse_fraction(row.get("real"), f"{name}.real")
                imag_mid = parse_fraction(row.get("imag"), f"{name}.imag")
                coefficient_midpoints[lag].real += real_mid
                if lag != 0:
                    coefficient_midpoints[lag].imaginary += imag_mid
            fast_shard_count += 1
        else:
            raise CertificateError(f"{name}: unsupported shard schema")

        if not (0 <= start < end <= total_segments):
            raise CertificateError(f"{name}: invalid segment range")
        primes = parse_int(data.get("prime_count"), f"{name}.prime_count")
        higher = parse_int(
            data.get("higher_prime_power_count"),
            f"{name}.higher_prime_power_count",
        )
        terms = parse_int(data.get("total_terms"), f"{name}.total_terms")
        if min(primes, higher, terms) < 0 or terms != primes + higher:
            raise CertificateError(f"{name}: term-count mismatch")
        if bool(include_higher) != (higher > 0):
            # A declared higher-power stream may be empty only on a synthetic
            # zero-higher-power plan, which should set both sides false.
            if not (include_higher and expected_counts["higher_prime_power_count"] == 0):
                raise CertificateError(f"{name}: higher-power declaration mismatch")
        coverage.append(
            Coverage(
                start=start,
                end=end,
                kind="directed" if schema == DIRECTED_SCHEMA else "fast",
                include_higher_powers=include_higher,
                prime_count=primes,
                higher_count=higher,
                total_terms=terms,
                path=path,
            )
        )
        prime_count += primes
        higher_count += higher
        total_terms += terms
        higher_streams += int(include_higher)

    if not shards:
        raise CertificateError("at least one shard is required")
    coverage.sort(key=lambda item: (item.start, item.end, item.path))
    cursor = 0
    for item in coverage:
        if item.start != cursor:
            raise CertificateError(f"coverage gap or overlap at segment {cursor}")
        cursor = item.end
    if cursor != total_segments:
        raise CertificateError("incomplete segment coverage")
    if fast_shard_count == 0:
        raise CertificateError("hybrid plan requires at least one fast shard")
    if higher_streams != 1:
        raise CertificateError("exactly one higher-power stream is required")
    actual_counts = {
        "prime_count": prime_count,
        "higher_prime_power_count": higher_count,
        "total_terms": total_terms,
    }
    if actual_counts != expected_counts:
        raise CertificateError("global source counts mismatch")

    prime_operator_radius = direct_operator_radius + fast_operator_budget
    declared_gate = parse_fraction(plan.get("operator_gate"), "plan.operator_gate")
    if not prime_operator_radius < declared_gate:
        raise CertificateError("prime source operator radius does not clear plan gate")

    result: dict[str, Any] = {
        "schema": OUTPUT_SCHEMA,
        "status": "COMPLETE_REFERENCE_AND_PRIME_OPERATOR_MOAT",
        "parameters": {
            "cutoff": parse_int(plan.get("cutoff"), "plan.cutoff"),
            "carrier": plan.get("carrier"),
            "cells": cells,
            "segment_size": parse_int(plan.get("segment_size"), "plan.segment_size"),
            "total_segments": total_segments,
            "fast_start_segment": fast_start,
            "parameter_sha256": parameter_sha,
            "normalization_sha256": normalization_sha,
        },
        "coverage": {
            **actual_counts,
            "directed_shards": directed_shard_count,
            "fast_shards": fast_shard_count,
            "higher_power_streams": higher_streams,
            "ranges": [
                {
                    "start": item.start,
                    "end": item.end,
                    "kind": item.kind,
                    "include_higher_powers": item.include_higher_powers,
                    "path": item.path,
                }
                for item in coverage
            ],
        },
        "operator_radius": {
            "directed_rectangle_l1": fraction_json(direct_operator_radius),
            "fast_global_static": fraction_json(fast_operator_budget),
            "prime_total": fraction_json(prime_operator_radius),
            "required_gate": fraction_json(declared_gate),
        },
        "coefficient_convention": (
            "lag zero uses the real midpoint only; stored lag d>0 is twice the "
            "upper-diagonal matrix entry"
        ),
        "lags": [
            {
                "lag": lag,
                "real": fraction_json(value.real),
                "imag": fraction_json(Fraction(0) if lag == 0 else value.imaginary),
            }
            for lag, value in enumerate(coefficient_midpoints)
        ],
        "proof_boundary": (
            "This exactly merges declared coefficient intervals and midpoint shards "
            "under L-8503/L-8505.  It does not prove that a fast producer follows "
            "its arithmetic contract; source fingerprints and an independent direct "
            "range comparison remain required."
        ),
    }
    result["reference_sha256"] = canonical_sha(result)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("budget_verification", type=Path)
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = merge(
            load_json(args.plan),
            load_json(args.budget_verification),
            [(str(path), load_json(path)) for path in args.shards],
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
