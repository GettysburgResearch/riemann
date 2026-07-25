#!/usr/bin/env python3
"""Exact checker for a frozen arbitrary-height complex Pick vector."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

from cross_height import Gaussian, coefficient_l1, pick_contraction_coefficients, vector_norm_squared
from verify_certificate import CertificateError, Interval, canonical_digest, fraction_json
from verify_value_certificate import SCHEMA as VALUE_SCHEMA, parse_point

VERIFY_SCHEMA = "riemann.xi-complex-pick-candidate.verification.v1"


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def parse_dyadic_vector(raw: Any, expected_length: int, name: str) -> list[Gaussian]:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    bits = exact_int(raw.get("scale_bits"), f"{name}.scale_bits")
    real = raw.get("real_numerators")
    imag = raw.get("imag_numerators")
    if bits < 0:
        raise CertificateError(f"{name}.scale_bits must be nonnegative")
    if not isinstance(real, list) or not isinstance(imag, list):
        raise CertificateError(f"{name} numerator arrays are required")
    if len(real) != expected_length or len(imag) != expected_length:
        raise CertificateError(f"{name} arrays must have length {expected_length}")
    denominator = 1 << bits
    result = [
        Gaussian(
            Fraction(exact_int(r, f"{name}.real_numerators[{index}]"), denominator),
            Fraction(exact_int(i, f"{name}.imag_numerators[{index}]"), denominator),
        )
        for index, (r, i) in enumerate(zip(real, imag))
    ]
    if all(value.norm_squared() == 0 for value in result):
        raise CertificateError(f"{name} is the zero vector")
    return result


def evaluate_channel(
    channel: dict[str, Any], points: dict[str, Any], index: int
) -> dict[str, object]:
    name = f"channels[{index}]"
    identifier = channel.get("id")
    if not isinstance(identifier, str) or not identifier:
        raise CertificateError(f"{name}.id must be a nonempty string")
    if channel.get("kind") != "complex-pick-rayleigh":
        raise CertificateError(f"{name}.kind must be 'complex-pick-rayleigh'")
    ids = channel.get("points")
    if not isinstance(ids, list) or len(ids) < 2 or not all(isinstance(x, str) for x in ids):
        raise CertificateError(f"{name}.points must contain at least two IDs")
    if len(set(ids)) != len(ids):
        raise CertificateError(f"{name}.points contains duplicates")
    try:
        selected = [points[point_id] for point_id in ids]
    except KeyError as exc:
        raise CertificateError(f"{name} references an unknown point") from exc
    vector = parse_dyadic_vector(channel.get("vector"), len(selected), f"{name}.vector")
    coefficients = pick_contraction_coefficients(
        [point.x for point in selected],
        [point.t for point in selected],
        vector,
    )
    interval = Interval.exact(Fraction(0))
    for coefficient, point in zip(coefficients, selected):
        interval = interval.add(point.f.real.scale(coefficient.real))
        interval = interval.add(point.f.imag.scale(-coefficient.imag))
    norm_squared = vector_norm_squared(vector)
    normalized = Interval(interval.lower / norm_squared, interval.upper / norm_squared)
    amplification = coefficient_l1(coefficients)
    return {
        "id": identifier,
        "kind": "complex-pick-rayleigh",
        "status": interval.status_nonnegative_under_rh(),
        "points": ids,
        "interval": interval.to_json(),
        "normalized_interval": normalized.to_json(),
        "vector_norm_squared": fraction_json(norm_squared),
        "contraction_coefficients": [value.to_json() for value in coefficients],
        "primitive_rectangle_l1_amplification": fraction_json(amplification),
        "normalized_primitive_rectangle_l1_amplification": fraction_json(
            amplification / norm_squared
        ),
        "vector_sha256": canonical_digest(channel["vector"]),
        "source_nomination": channel.get("source_nomination"),
    }


def verify_certificate(data: dict[str, Any]) -> dict[str, object]:
    if data.get("schema") != VALUE_SCHEMA:
        raise CertificateError(f"schema must be {VALUE_SCHEMA!r}")
    raw_points = data.get("points")
    raw_channels = data.get("channels")
    declared = data.get("declared_channel_ids")
    if not isinstance(raw_points, list) or not isinstance(raw_channels, list):
        raise CertificateError("points and channels must be arrays")
    if not isinstance(declared, list) or not all(isinstance(value, str) for value in declared):
        raise CertificateError("declared_channel_ids must be an array of strings")
    points: dict[str, Any] = {}
    for index, raw in enumerate(raw_points):
        point = parse_point(raw, index)
        if point.identifier in points:
            raise CertificateError("duplicate point ID")
        points[point.identifier] = point
    channels = [evaluate_channel(channel, points, index) for index, channel in enumerate(raw_channels)]
    identifiers = [str(channel["id"]) for channel in channels]
    if declared != identifiers or len(set(identifiers)) != len(identifiers):
        raise CertificateError("declared_channel_ids must exactly equal unique ordered IDs")
    negative = [row["id"] for row in channels if row["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [row["id"] for row in channels if row["status"] == "UNRESOLVED_ZERO_TOUCH"]
    result: dict[str, object] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": (
            "CERTIFIED_NEGATIVE_WITNESS_PENDING_INDEPENDENT_REPRODUCTION"
            if negative else
            "NO_NEGATIVE_CHANNEL_UNRESOLVED_PRESENT"
            if unresolved else
            "CERTIFIED_NONNEGATIVE_CONTROLS_ONLY"
        ),
        "point_count": len(points),
        "channel_count": len(channels),
        "negative_channels": negative,
        "unresolved_channels": unresolved,
        "channels": channels,
        "proof_boundary": (
            "Exact contraction of supplied primitive Arb rectangles using a pre-registered "
            "dyadic vector. The checker does not evaluate xi or promote D-3201/L-3202. "
            "Any negative requires independent directed reproduction."
        ),
    }
    result["verification_sha256"] = canonical_digest(result)
    claimed = data.get("certificate_sha256")
    if claimed is not None:
        body = dict(data)
        body.pop("certificate_sha256", None)
        if claimed != canonical_digest(body):
            raise CertificateError("certificate_sha256 mismatch")
        result["certificate_sha256"] = claimed
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify_certificate(data)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {
            "schema": VERIFY_SCHEMA,
            "verified": False,
            "status": "REJECTED",
            "reason": str(exc),
        }
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
