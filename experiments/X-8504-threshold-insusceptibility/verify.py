#!/usr/bin/env python3
"""Exact checker for O-8502 threshold-entry insusceptibility."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

MANIFEST_MAGIC = "RIEMANN_D0801_AUTOCORRELATION_V1"
VERDICT_SCHEMA = "riemann.piecewise-carrier-fixed-vector.v1"
VERIFY_SCHEMA = "riemann.threshold-entry-insusceptibility.verification.v1"
EXPECTED_VECTOR = "3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297"
EXPECTED_NORMALIZATION = "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"
EXPECTED_PARAMETER = "ac28f01b3804426fb19275c7cf0588226292d848b7b4d62bb983fd9ac7ad3e34"


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


def canonical_sha(data: Any) -> str:
    encoded = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def parse_manifest(path: Path) -> dict[str, Any]:
    try:
        tokens = path.read_text(encoding="utf-8").split()
    except OSError as exc:
        raise CertificateError(f"{path}: {exc}") from exc
    if not tokens or tokens[0] != MANIFEST_MAGIC:
        raise CertificateError("wrong autocorrelation manifest magic")
    index = 1
    metadata: dict[str, Any] = {}
    autocorrelations: list[tuple[int, int]] = []
    while index < len(tokens):
        key = tokens[index]
        index += 1
        if key == "a":
            if index + 2 >= len(tokens):
                raise CertificateError("truncated autocorrelation row")
            lag = int(tokens[index])
            real = int(tokens[index + 1])
            imaginary = int(tokens[index + 2])
            index += 3
            if lag != len(autocorrelations):
                raise CertificateError("autocorrelation rows are not ordered")
            autocorrelations.append((real, imaginary))
        else:
            if index >= len(tokens):
                raise CertificateError(f"missing value for manifest key {key}")
            metadata[key] = tokens[index]
            index += 1
    required = {
        "cells",
        "vector_scale_bits",
        "autocorr_scale_bits",
        "vector_sha256",
        "normalization_sha256",
        "parameter_sha256",
        "cutoff_power10",
        "cutoff",
        "carrier_num",
        "carrier_den",
        "segment_size",
        "total_segments",
        "a_count",
    }
    if set(metadata) != required:
        raise CertificateError("autocorrelation manifest metadata mismatch")
    cells = int(metadata["cells"])
    if int(metadata["a_count"]) != cells + 1 or len(autocorrelations) != cells + 1:
        raise CertificateError("autocorrelation count mismatch")
    if autocorrelations[-1] != (0, 0):
        raise CertificateError("terminal autocorrelation row is not zero")
    return {"metadata": metadata, "autocorrelations": autocorrelations}


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError(f"{path}: root must be an object")
    return value


def verify(manifest: dict[str, Any], verdict: dict[str, Any]) -> dict[str, Any]:
    metadata = manifest["metadata"]
    autocorrelations = manifest["autocorrelations"]
    if int(metadata["cells"]) != 1024:
        raise CertificateError("target cell count mismatch")
    if int(metadata["autocorr_scale_bits"]) != 192:
        raise CertificateError("autocorrelation scale mismatch")
    if metadata["vector_sha256"] != EXPECTED_VECTOR:
        raise CertificateError("manifest vector fingerprint mismatch")
    if metadata["normalization_sha256"] != EXPECTED_NORMALIZATION:
        raise CertificateError("manifest normalization fingerprint mismatch")
    if metadata["parameter_sha256"] != EXPECTED_PARAMETER:
        raise CertificateError("manifest parameter fingerprint mismatch")
    if int(metadata["cutoff"]) != 100_000_000_000:
        raise CertificateError("manifest cutoff mismatch")
    if metadata["carrier_num"] != "94184072727073" or metadata["carrier_den"] != "20":
        raise CertificateError("manifest carrier mismatch")

    if verdict.get("schema") != VERDICT_SCHEMA:
        raise CertificateError("wrong fixed-vector verdict schema")
    if verdict.get("verdict") != "CERTIFIED_POSITIVE_FIXED_VECTOR":
        raise CertificateError("source verdict is not positive")
    for key, expected in (
        ("vector_sha256", EXPECTED_VECTOR),
        ("normalization_sha256", EXPECTED_NORMALIZATION),
        ("parameter_sha256", EXPECTED_PARAMETER),
    ):
        if verdict.get(key) != expected:
            raise CertificateError(f"verdict {key} mismatch")

    a0_real, a0_imaginary = autocorrelations[0]
    endpoint_real, endpoint_imaginary = autocorrelations[1023]
    if a0_real <= 0 or a0_imaginary != 0:
        raise CertificateError("invalid norm autocorrelation")
    endpoint_squared = endpoint_real**2 + endpoint_imaginary**2
    ratio_square_surplus = a0_real**2 - 10**12 * endpoint_squared
    if ratio_square_surplus <= 0:
        raise CertificateError("endpoint ratio is not strictly below 1e-6")

    interval = verdict.get("full_exact_quadratic_interval")
    if not isinstance(interval, dict):
        raise CertificateError("missing fixed-vector interval")
    lower = parse_fraction(interval.get("lower"), "full_interval.lower")
    norm = parse_fraction(verdict.get("vector_norm_squared"), "vector_norm_squared")
    if lower <= 0 or norm <= 0:
        raise CertificateError("source directional data are not positive")
    normalized_lower = lower / norm
    if not normalized_lower > Fraction(1, 4000):
        raise CertificateError("directional lower endpoint does not clear 1/4000")

    # L-4204 gives log(p)/(pi*sqrt(q)) times the endpoint ratio.  Since
    # h(x)=log(x)/sqrt(x) decreases for x>e^2, every q>=1e11 is bounded by
    # h(1e11).  Then 11 log(10)<26, pi>3, sqrt(1e11)>316000, and the exact
    # endpoint ratio is below 1e-6.
    event_upper = Fraction(13, 474_000_000_000)
    required_event_upper = Fraction(1, 36_000_000_000)
    if not event_upper < required_event_upper:
        raise CertificateError("event arithmetic does not clear 1/36e9")
    moat_ratio_upper = required_event_upper / Fraction(1, 4000)
    if moat_ratio_upper != Fraction(1, 9_000_000):
        raise CertificateError("event-to-moat ratio arithmetic mismatch")

    result: dict[str, Any] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": "HISTORICAL_VECTOR_FIRST_CELL_EVENT_EXCLUDED",
        "fingerprints": {
            "vector_sha256": EXPECTED_VECTOR,
            "normalization_sha256": EXPECTED_NORMALIZATION,
            "parameter_sha256": EXPECTED_PARAMETER,
        },
        "endpoint_autocorrelation": {
            "norm_integer": str(a0_real),
            "real_integer": str(endpoint_real),
            "imaginary_integer": str(endpoint_imaginary),
            "ratio_square_surplus": str(ratio_square_surplus),
            "ratio_upper": fraction_json(Fraction(1, 1_000_000)),
        },
        "directional_moat": {
            "normalized_lower": fraction_json(normalized_lower),
            "coarse_lower": fraction_json(Fraction(1, 4000)),
        },
        "first_cell_event": {
            "derived_upper": fraction_json(event_upper),
            "reported_simple_upper": fraction_json(required_event_upper),
            "maximum_fraction_of_coarse_moat": fraction_json(moat_ratio_upper),
        },
        "proof_boundary": (
            "This excludes only the newly admitted prime-power component for the "
            "recovered vector in one first deposition cell.  Smooth background and "
            "other simultaneous events are not bounded here."
        ),
    }
    result["verification_sha256"] = canonical_sha(result)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("autocorrelation_manifest", type=Path)
    parser.add_argument("verdict", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = verify(
            parse_manifest(args.autocorrelation_manifest),
            load_json(args.verdict),
        )
        code = 0
    except CertificateError as exc:
        result = {
            "schema": VERIFY_SCHEMA,
            "verified": False,
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
