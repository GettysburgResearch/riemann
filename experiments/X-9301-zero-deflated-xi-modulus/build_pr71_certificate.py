#!/usr/bin/env python3
"""Bind PR #71 direct-xi primitives and X-5603 Hardy-zero balls to X-9301."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

PRIMITIVE_SCHEMA = "riemann.xi-modulus-primitives.v1"
GAP_SCHEMA = "riemann.x5603-line-gap-discrepancy.v1"
CONFIG_SCHEMA = "riemann.xi-modulus-zero-deflation-config.v1"
OUTPUT_SCHEMA = "riemann.xi-modulus-zero-deflation.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
GATE = "CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND"


class BridgeError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise BridgeError(f"{path} must contain an object")
    return value


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise BridgeError(f"{name} must be an integer")
    return value


def parse_integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise BridgeError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise BridgeError(f"{name} must be an integer string") from exc
    raise BridgeError(f"{name} must be an integer or integer string")


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise BridgeError(f"{name} must be an object")
    numerator = parse_integer(raw.get("numerator"), f"{name}.numerator")
    denominator = parse_integer(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise BridgeError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def binary_value(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise BridgeError(f"{name} must be an object")
    mantissa = parse_integer(raw.get("mantissa"), f"{name}.mantissa")
    exponent = parse_integer(raw.get("exponent"), f"{name}.exponent")
    if exponent >= 0:
        return Fraction(mantissa << exponent)
    return Fraction(mantissa, 1 << (-exponent))


def binary_interval(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise BridgeError(f"{name} must be an object")
    lower = binary_value(raw.get("lower"), f"{name}.lower")
    upper = binary_value(raw.get("upper"), f"{name}.upper")
    if lower > upper:
        raise BridgeError(f"{name} is reversed")
    return lower, upper


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def validate_rows(rows: Any, point_ids: set[str]) -> list[dict[str, Any]]:
    if not isinstance(rows, list) or not rows:
        raise BridgeError("config rows must be a nonempty list")
    result = []
    row_ids: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise BridgeError(f"row {index} must be an object")
        row_id = row.get("id")
        if not isinstance(row_id, str) or not row_id or row_id in row_ids:
            raise BridgeError("row IDs must be nonempty and unique")
        row_ids.add(row_id)
        kind = row.get("kind")
        if kind == "deflated-monotonicity":
            ids = [row.get("left"), row.get("right")]
        elif kind == "deflated-cross-loewner-determinant":
            rows_raw, columns_raw = row.get("rows"), row.get("columns")
            if not isinstance(rows_raw, list) or not isinstance(columns_raw, list):
                raise BridgeError("Loewner rows and columns must be lists")
            ids = rows_raw + columns_raw
        else:
            raise BridgeError(f"unsupported production row kind {kind!r}")
        if any(
            not isinstance(identifier, str) or identifier not in point_ids
            for identifier in ids
        ):
            raise BridgeError(f"row {index} references an unknown point")
        result.append(row)
    return result


def build(
    primitives: dict[str, Any],
    gap: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    if primitives.get("schema") != PRIMITIVE_SCHEMA:
        raise BridgeError("primitive schema mismatch")
    if primitives.get("normalization_id") != NORMALIZATION:
        raise BridgeError("primitive normalization mismatch")
    if gap.get("schema") != GAP_SCHEMA:
        raise BridgeError("gap schema mismatch")
    if config.get("schema") != CONFIG_SCHEMA:
        raise BridgeError("config schema mismatch")
    if config.get("normalization_id") not in (None, NORMALIZATION):
        raise BridgeError("config normalization mismatch")

    t_primitive = rational(primitives.get("ordinate"), "primitives.ordinate")
    t_gap = rational(gap.get("target"), "gap.target")
    if t_primitive != t_gap:
        raise BridgeError("primitive and gap ordinates differ")

    classification = gap.get("classification")
    if classification not in (
        "CERTIFIED_EMPTY_FULL_STRIP_INTERIOR_SLAB",
        "CERTIFIED_OFF_CRITICAL_ZERO_IN_LINE_EMPTY_SLAB",
    ):
        raise BridgeError("gap artifact is not proof-classified")

    lower_ball = binary_interval(
        gap.get("lower_hardy_zero_ball"), "lower_hardy_zero_ball"
    )
    upper_ball = binary_interval(
        gap.get("upper_hardy_zero_ball"), "upper_hardy_zero_ball"
    )
    if not (lower_ball[1] < t_gap < upper_ball[0]):
        raise BridgeError("Hardy-zero balls do not strictly bracket the exact target")
    if lower_ball[1] >= upper_ball[0]:
        raise BridgeError("Hardy-zero balls overlap or touch")

    raw_points = primitives.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise BridgeError("primitive points must be a nonempty list")
    points = []
    point_ids: set[str] = set()
    for index, point in enumerate(raw_points):
        if not isinstance(point, dict):
            raise BridgeError(f"primitive point {index} must be an object")
        identifier = point.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in point_ids:
            raise BridgeError("primitive point IDs must be nonempty and unique")
        point_ids.add(identifier)
        x = rational(point.get("x"), f"point {identifier}.x")
        if x <= 0:
            raise BridgeError("horizontal offsets must be positive")
        rectangle = point.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise BridgeError(f"point {identifier} lacks xi_rectangle")
        if point.get("functional_equation_residual_contains_zero") is not True:
            raise BridgeError(f"point {identifier} failed the functional-equation gate")
        canonical = {"id": identifier, "u": fj(x * x), "xi_rectangle": rectangle}
        points.append({**canonical, "point_sha256": canonical_sha(canonical)})

    rows = validate_rows(config.get("rows"), point_ids)
    log_terms = exact_int(config.get("log_terms", 256), "config.log_terms")
    gap_digest = canonical_sha(gap)

    zero_bins = [
        {
            "id": "pr71-lower-hardy-zero",
            "lower_ordinate": fj(lower_ball[0]),
            "upper_ordinate": fj(lower_ball[1]),
            "count_lower": 1,
            "gate": {
                "status": GATE,
                "sha256": hashlib.sha256(
                    (gap_digest + ":lower").encode("ascii")
                ).hexdigest(),
            },
        },
        {
            "id": "pr71-upper-hardy-zero",
            "lower_ordinate": fj(upper_ball[0]),
            "upper_ordinate": fj(upper_ball[1]),
            "count_lower": 1,
            "gate": {
                "status": GATE,
                "sha256": hashlib.sha256(
                    (gap_digest + ":upper").encode("ascii")
                ).hexdigest(),
            },
        },
    ]

    output = {
        "schema": OUTPUT_SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "normalization_id": NORMALIZATION,
        "ordinate": fj(t_gap),
        "log_terms": log_terms,
        "points": sorted(points, key=lambda point: rational(point["u"], "point.u")),
        "zero_bins": zero_bins,
        "rows": rows,
        "source": {
            "primitive_schema": PRIMITIVE_SCHEMA,
            "primitive_sha256": canonical_sha(primitives),
            "gap_schema": GAP_SCHEMA,
            "gap_sha256": gap_digest,
            "gap_classification": classification,
        },
    }
    output["certificate_sha256"] = canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primitives", type=Path)
    parser.add_argument("gap", type=Path)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = build(load(args.primitives), load(args.gap), load(args.config))
    except (OSError, json.JSONDecodeError, BridgeError) as exc:
        print(json.dumps({"built": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "schema": result["schema"],
                "point_count": len(result["points"]),
                "zero_bin_count": len(result["zero_bins"]),
                "row_count": len(result["rows"]),
                "certificate_sha256": result["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
