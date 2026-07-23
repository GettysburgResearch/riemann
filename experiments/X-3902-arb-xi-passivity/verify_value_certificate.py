#!/usr/bin/env python3
"""Exact checker for high-height xi'/xi value-ball certificates.

This checker reuses only the interval and finite-contraction algebra from
``verify_certificate.py``. It does not require a repeated functional-equation
evaluation at every expensive high point; that normalization gate is exercised
by the separate low-control certificate.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Sequence

from verify_certificate import (
    CertificateError,
    ComplexRectangle,
    Point,
    canonical_digest,
    evaluate_channel,
    fraction_json,
    parse_binary,
    parse_fraction,
)

SCHEMA = "riemann.xi-passivity-value-balls.v1"
VERIFY_SCHEMA = "riemann.xi-passivity-value-balls.verification.v1"


def parse_point(raw: Any, index: int) -> Point:
    name = f"points[{index}]"
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    identifier = raw.get("id")
    if not isinstance(identifier, str) or not identifier:
        raise CertificateError(f"{name}.id must be a nonempty string")
    x = parse_fraction(raw.get("x"), f"{name}.x")
    t = parse_fraction(raw.get("t"), f"{name}.t")
    if x <= 0:
        raise CertificateError(f"{name} is not strictly right of the critical line")
    via_xi = ComplexRectangle.parse(raw.get("f_via_xi"), f"{name}.f_via_xi")
    via_parts = ComplexRectangle.parse(raw.get("f_via_parts"), f"{name}.f_via_parts")
    intersection = via_xi.intersect(via_parts)
    zeta_abs_lower = parse_binary(raw.get("zeta_abs_lower"), f"{name}.zeta_abs_lower")
    if zeta_abs_lower <= 0:
        raise CertificateError(f"{name} has a zeta denominator ball touching zero")
    # reflected fields are unused by the channel algebra in the imported Point.
    return Point(
        identifier=identifier,
        x=x,
        t=t,
        f=intersection,
        reflected_f=intersection,
        zeta_abs_lower=zeta_abs_lower,
        reflected_zeta_abs_lower=zeta_abs_lower,
    )


def verify_certificate(data: dict[str, Any]) -> dict[str, object]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    raw_points = data.get("points")
    raw_channels = data.get("channels")
    declared = data.get("declared_channel_ids")
    if not isinstance(raw_points, list) or not isinstance(raw_channels, list):
        raise CertificateError("points and channels must be arrays")
    if not isinstance(declared, list) or not all(isinstance(value, str) for value in declared):
        raise CertificateError("declared_channel_ids must be an array of strings")

    points: dict[str, Point] = {}
    summaries: list[dict[str, object]] = []
    for index, raw in enumerate(raw_points):
        point = parse_point(raw, index)
        if point.identifier in points:
            raise CertificateError("duplicate point ID")
        points[point.identifier] = point
        summaries.append(
            {
                "id": point.identifier,
                "x": fraction_json(point.x),
                "t": fraction_json(point.t),
                "f_intersection": point.f.to_json(),
                "zeta_abs_lower": fraction_json(point.zeta_abs_lower),
            }
        )

    channels = [
        evaluate_channel(channel, index, points)
        for index, channel in enumerate(raw_channels)
    ]
    actual_ids = [item["id"] for item in channels]
    if len(set(actual_ids)) != len(actual_ids):
        raise CertificateError("duplicate channel ID")
    if declared != actual_ids:
        raise CertificateError(
            "declared_channel_ids must exactly equal the ordered used channel IDs"
        )
    negative = [item["id"] for item in channels if item["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [item["id"] for item in channels if item["status"] == "UNRESOLVED_ZERO_TOUCH"]
    status = "CERTIFIED_NEGATIVE_WITNESS_PENDING_INDEPENDENT_REPRODUCTION" if negative else (
        "NO_NEGATIVE_CHANNEL_UNRESOLVED_PRESENT" if unresolved else "CERTIFIED_NONNEGATIVE_CONTROLS_ONLY"
    )
    result: dict[str, object] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": status,
        "point_count": len(points),
        "channel_count": len(channels),
        "negative_channels": negative,
        "unresolved_channels": unresolved,
        "points": summaries,
        "channels": channels,
        "proof_boundary": (
            "This checks exact contractions and signs from supplied high-height Arb "
            "rectangles. It does not independently evaluate special functions. The "
            "two-assembly gate is pointwise; functional-equation normalization is "
            "validated separately by the low-control artifact."
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
        result = {"schema": VERIFY_SCHEMA, "verified": False, "status": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
