#!/usr/bin/env python3
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

import verify_fast_budget

DIRECT_SCHEMA = "riemann.piecewise-carrier-directed-shard.v1"
FAST_SCHEMA = "riemann.piecewise-carrier-fast-midpoint-shard.v1"
OUTPUT_SCHEMA = "riemann.piecewise-carrier-hybrid-prime-interval.v1"
EXPECTED_VECTOR = "3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297"
EXPECTED_PARAMETER = "ac28f01b3804426fb19275c7cf0588226292d848b7b4d62bb983fd9ac7ad3e34"
EXPECTED_NORMALIZATION = "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"
EXPECTED_SEGMENTS = 5000
EXPECTED_PRIMES = 4_118_054_813
EXPECTED_HIGHER = 28_156
EXPECTED_TOTAL = 4_118_082_969
FAST_CONTRACT = (
    "binary80 nearest basic arithmetic, binary128 phase arithmetic, MPFR setup, "
    "balanced pairwise summation; global moat required"
)


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise CertificateError(f"{name} is not an integer") from exc
    raise CertificateError(f"{name} must be an integer")


def frac(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), name + ".numerator")
    denominator = parse_int(value.get("denominator"), name + ".denominator")
    if denominator <= 0:
        raise CertificateError(f"{name} denominator must be positive")
    return Fraction(numerator, denominator)


def fjson(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def canonical_sha(data: Any) -> str:
    encoded = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def load(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{path}: {exc}") from exc
    if not isinstance(data, dict):
        raise CertificateError(f"{path}: root must be an object")
    data["_path"] = str(path)
    return data


def verify_common(data: dict[str, Any]) -> tuple[int, int]:
    for key, expected in (
        ("vector_sha256", EXPECTED_VECTOR),
        ("parameter_sha256", EXPECTED_PARAMETER),
        ("normalization_sha256", EXPECTED_NORMALIZATION),
    ):
        if data.get(key) != expected:
            raise CertificateError(f"{data['_path']}: {key} mismatch")
    start = parse_int(data.get("segment_start"), "segment_start")
    end = parse_int(data.get("segment_end"), "segment_end")
    if not (0 <= start < end <= EXPECTED_SEGMENTS):
        raise CertificateError(f"{data['_path']}: invalid segment range")
    return start, end


def assemble(items: list[dict[str, Any]]) -> dict[str, Any]:
    if not items:
        raise CertificateError("at least one shard is required")

    ranges: list[tuple[int, int, str, str]] = []
    direct_lower = Fraction(0)
    direct_upper = Fraction(0)
    fast_midpoint = Fraction(0)
    prime_count = higher_count = total_count = 0
    power_shards = direct_count = fast_count = 0
    sources: list[dict[str, Any]] = []

    for data in items:
        schema = data.get("schema")
        start, end = verify_common(data)
        ranges.append((start, end, data["_path"], str(schema)))

        primes = parse_int(data.get("prime_count"), "prime_count")
        higher = parse_int(
            data.get("higher_prime_power_count", 0),
            "higher_prime_power_count",
        )
        terms = parse_int(data.get("total_terms"), "total_terms")
        if primes + higher != terms:
            raise CertificateError(f"{data['_path']}: term-count identity failed")
        prime_count += primes
        higher_count += higher
        total_count += terms

        if schema == DIRECT_SCHEMA:
            direct_count += 1
            power_shards += bool(data.get("include_higher_powers"))
            interval = data.get("prime_rayleigh_interval")
            if not isinstance(interval, dict):
                raise CertificateError(f"{data['_path']}: missing direct interval")
            lower = frac(interval.get("lower"), "lower")
            upper = frac(interval.get("upper"), "upper")
            if lower > upper:
                raise CertificateError(f"{data['_path']}: reversed interval")
            direct_lower += lower
            direct_upper += upper
        elif schema == FAST_SCHEMA:
            fast_count += 1
            if data.get("include_higher_powers") is not False or higher != 0:
                raise CertificateError(
                    f"{data['_path']}: fast shard must contain ordinary primes only"
                )
            if data.get("arithmetic_contract") != FAST_CONTRACT:
                raise CertificateError(f"{data['_path']}: arithmetic contract mismatch")
            parameters = (
                parse_int(data.get("phase_grid_M"), "phase_grid_M"),
                parse_int(data.get("phase_taylor_R"), "phase_taylor_R"),
                parse_int(data.get("log_series_J"), "log_series_J"),
                parse_int(data.get("sqrt_series_J"), "sqrt_series_J"),
            )
            if parameters != (32768, 3, 3, 5):
                raise CertificateError(f"{data['_path']}: accelerator parameter mismatch")
            fast_midpoint += frac(data.get("midpoint_rayleigh"), "midpoint_rayleigh")
        else:
            raise CertificateError(
                f"{data['_path']}: unsupported schema {schema!r}"
            )

        canonical = {key: value for key, value in data.items() if key != "_path"}
        sources.append(
            {
                "path": data["_path"],
                "schema": schema,
                "range": [start, end],
                "sha256": canonical_sha(canonical),
            }
        )

    ranges.sort()
    cursor = 0
    for start, end, path, _schema in ranges:
        if start != cursor:
            raise CertificateError(
                f"coverage gap/overlap at {cursor}; next {path} starts {start}"
            )
        cursor = end
    if cursor != EXPECTED_SEGMENTS:
        raise CertificateError(
            f"coverage ended at {cursor}, expected {EXPECTED_SEGMENTS}"
        )
    if power_shards != 1:
        raise CertificateError("exactly one direct shard must include higher powers")
    if (prime_count, higher_count, total_count) != (
        EXPECTED_PRIMES,
        EXPECTED_HIGHER,
        EXPECTED_TOTAL,
    ):
        raise CertificateError("global term counts mismatch")

    budget = verify_fast_budget.verify()
    moat = frac(budget["components"]["total"], "fast moat")
    lower = direct_lower + fast_midpoint - moat
    upper = direct_upper + fast_midpoint + moat
    if lower > 0:
        status = "STRICT_POSITIVE_PRIME_INTERVAL"
    elif upper < 0:
        status = "STRICT_NEGATIVE_PRIME_INTERVAL"
    else:
        status = "UNRESOLVED_PRIME_INTERVAL"

    output: dict[str, Any] = {
        "schema": OUTPUT_SCHEMA,
        "status": status,
        "vector_sha256": EXPECTED_VECTOR,
        "parameter_sha256": EXPECTED_PARAMETER,
        "normalization_sha256": EXPECTED_NORMALIZATION,
        "coverage": {
            "segments": EXPECTED_SEGMENTS,
            "direct_shards": direct_count,
            "fast_shards": fast_count,
            "prime_count": prime_count,
            "higher_prime_power_count": higher_count,
            "total_terms": total_count,
        },
        "fast_global_moat": fjson(moat),
        "direct_interval_sum": {
            "lower": fjson(direct_lower),
            "upper": fjson(direct_upper),
        },
        "fast_midpoint_sum": fjson(fast_midpoint),
        "complete_prime_interval": {
            "lower": fjson(lower),
            "upper": fjson(upper),
        },
        "sources": sources,
        "proof_boundary": (
            "This is the complete fixed-vector prime interval only. Exact alpha, "
            "nonprime corrections, T-2801 review, and independent reproduction "
            "remain separate."
        ),
    }
    output["certificate_sha256"] = canonical_sha(output)
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        output = assemble([load(path) for path in args.shards])
    except CertificateError as exc:
        print(
            json.dumps(
                {"schema": OUTPUT_SCHEMA, "status": "REJECTED", "reason": str(exc)},
                sort_keys=True,
            )
        )
        return 2
    text = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
