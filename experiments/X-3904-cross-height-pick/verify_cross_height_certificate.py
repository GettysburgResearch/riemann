#!/usr/bin/env python3
"""Exact checker for cross-height complex matched-pole Pick certificates."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

from cross_height import (
    Gaussian,
    coefficient_l1,
    matched_identities,
    matched_pole_vector,
    parse_fraction,
    pick_contraction_coefficients,
    vector_norm_squared,
)
from verify_certificate import CertificateError, Interval, canonical_digest, fraction_json
from verify_value_certificate import SCHEMA as VALUE_SCHEMA, parse_point

VERIFY_SCHEMA = "riemann.xi-cross-height-pick.verification.v1"


def parse_vector(raw: Any, name: str) -> list[Gaussian]:
    if not isinstance(raw, list) or len(raw) < 2:
        raise CertificateError(f"{name} must contain at least two Gaussian rationals")
    try:
        result = [Gaussian.parse(value, f"{name}[{index}]") for index, value in enumerate(raw)]
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificateError(str(exc)) from exc
    if all(value.norm_squared() == 0 for value in result):
        raise CertificateError(f"{name} is the zero vector")
    return result


def matched_channel(
    channel: dict[str, Any], points: dict[str, Any], index: int
) -> dict[str, object]:
    name = f"channels[{index}]"
    identifier = channel.get("id")
    if not isinstance(identifier, str) or not identifier:
        raise CertificateError(f"{name}.id must be a nonempty string")
    if channel.get("kind") != "complex-matched-pole-rayleigh":
        raise CertificateError(f"{name}.kind is unsupported")
    ids = channel.get("points")
    if not isinstance(ids, list) or len(ids) < 2 or not all(isinstance(x, str) for x in ids):
        raise CertificateError(f"{name}.points must contain at least two point IDs")
    if len(set(ids)) != len(ids):
        raise CertificateError(f"{name}.points contains duplicates")
    try:
        selected = [points[point_id] for point_id in ids]
    except KeyError as exc:
        raise CertificateError(f"{name} references an unknown point") from exc
    vector = parse_vector(channel.get("vector"), f"{name}.vector")
    if len(vector) != len(selected):
        raise CertificateError(f"{name} point/vector length mismatch")
    try:
        center = parse_fraction(channel.get("model_center_t"), f"{name}.model_center_t")
        model_d = parse_fraction(channel.get("model_d"), f"{name}.model_d")
    except ValueError as exc:
        raise CertificateError(str(exc)) from exc
    if model_d <= 0:
        raise CertificateError(f"{name}.model_d must be positive")

    relative_nodes = [Gaussian(point.x, point.t - center) for point in selected]
    try:
        expected = matched_pole_vector(relative_nodes, model_d)
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"{name} invalid matched construction: {exc}") from exc
    if vector != expected:
        raise CertificateError(f"{name}.vector does not equal the exact matched-pole construction")
    identities = matched_identities(relative_nodes, vector, model_d)
    if any(value != Gaussian(0) for value in identities["moments"]):
        raise CertificateError(f"{name} moment cancellation failed")
    if identities["alpha"] != Gaussian(0) or identities["beta"] != Gaussian(-1):
        raise CertificateError(f"{name} modeled pole-overlap identity failed")

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
    if norm_squared <= 0:
        raise CertificateError(f"{name} has nonpositive norm")
    normalized = Interval(interval.lower / norm_squared, interval.upper / norm_squared)
    amplification = coefficient_l1(coefficients)
    status = interval.status_nonnegative_under_rh()
    return {
        "id": identifier,
        "kind": "complex-matched-pole-rayleigh",
        "status": status,
        "interval": interval.to_json(),
        "normalized_interval": normalized.to_json(),
        "points": ids,
        "vector": [value.to_json() for value in vector],
        "vector_norm_squared": fraction_json(norm_squared),
        "model_center_t": fraction_json(center),
        "model_d": fraction_json(model_d),
        "modeled_pair_value": fraction_json(Fraction(identities["modeled_pair_value"])),
        "modeled_pair_normalized": fraction_json(
            Fraction(identities["modeled_pair_value"]) / norm_squared
        ),
        "primitive_rectangle_l1_amplification": fraction_json(amplification),
        "normalized_primitive_rectangle_l1_amplification": fraction_json(
            amplification / norm_squared
        ),
        "contraction_coefficients": [value.to_json() for value in coefficients],
        "exact_identities": {
            "vanishing_moment_count": len(identities["moments"]),
            "alpha_overlap": identities["alpha"].to_json(),
            "beta_overlap": identities["beta"].to_json(),
        },
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
    point_rows: list[dict[str, object]] = []
    for index, raw in enumerate(raw_points):
        point = parse_point(raw, index)
        if point.identifier in points:
            raise CertificateError("duplicate point ID")
        points[point.identifier] = point
        point_rows.append({
            "id": point.identifier,
            "x": fraction_json(point.x),
            "t": fraction_json(point.t),
            "f_intersection": point.f.to_json(),
            "zeta_abs_lower": fraction_json(point.zeta_abs_lower),
        })

    channels = [matched_channel(channel, points, index) for index, channel in enumerate(raw_channels)]
    identifiers = [str(channel["id"]) for channel in channels]
    if len(set(identifiers)) != len(identifiers):
        raise CertificateError("duplicate channel ID")
    if declared != identifiers:
        raise CertificateError("declared_channel_ids must exactly equal ordered channel IDs")
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
            "ALL_CROSS_HEIGHT_CHANNELS_CERTIFIED_NONNEGATIVE"
        ),
        "point_count": len(points),
        "channel_count": len(channels),
        "negative_channels": negative,
        "unresolved_channels": unresolved,
        "points": point_rows,
        "channels": channels,
        "proof_boundary": (
            "Exact Gaussian-rational contraction of supplied Arb primitive rectangles. "
            "The checker does not evaluate xi, prove the primitive rectangles, or promote "
            "the D-3201/L-3202 normalization. A negative requires independent directed reproduction."
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
