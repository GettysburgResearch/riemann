#!/usr/bin/env python3
"""Bind direct completed-xi rectangles and rigorous nested total-zero counts.

The total counts are unconditional. The emitted certificate uses them only
inside the L-9303 implication: under RH, every counted zero is forced onto the
critical line and the nested table becomes an order-statistic deflation ledger.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import string
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

PRIMITIVE_SCHEMA = "riemann.xi-modulus-primitives.v1"
COUNT_SCHEMA = "riemann.x9302-pr71-total-count-windows.v1"
COUNT_CLASSIFICATION = "CERTIFIED_NESTED_TOTAL_ZETA_ZERO_COUNTS"
CONFIG_SCHEMA = "riemann.xi-modulus-zero-deflation-config.v1"
OUTPUT_SCHEMA = "riemann.xi-modulus-total-count-deflation.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
GATE = "CERTIFIED_TOTAL_ZETA_ZERO_LOWER_BOUND"


class BridgeError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise BridgeError(f"{path} must contain an object")
    return value


def parse_integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise BridgeError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
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
    return Fraction(mantissa << exponent) if exponent >= 0 else Fraction(mantissa, 1 << (-exponent))


def binary_interval(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise BridgeError(f"{name} must be an object")
    lower = binary_value(raw.get("lower"), f"{name}.lower")
    upper = binary_value(raw.get("upper"), f"{name}.upper")
    if lower > upper:
        raise BridgeError(f"{name} is reversed")
    return lower, upper


def exact_binary(raw: Any, name: str) -> Fraction:
    lower, upper = binary_interval(raw, name)
    if lower != upper:
        raise BridgeError(f"{name} is not exact")
    return lower


def unique_integer(bounds: tuple[Fraction, Fraction], name: str) -> int:
    lower, upper = bounds
    ceil_lower = -((-lower.numerator) // lower.denominator)
    floor_upper = upper.numerator // upper.denominator
    if ceil_lower != floor_upper:
        raise BridgeError(f"{name} does not isolate one integer")
    return ceil_lower


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def validate_sha(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(ch not in string.hexdigits for ch in value)
    ):
        raise BridgeError(f"{name} must be a 64-character hexadecimal digest")
    return value.lower()


def validate_rows(rows: Any, point_ids: set[str]) -> list[dict[str, Any]]:
    if not isinstance(rows, list) or not rows:
        raise BridgeError("config rows must be a nonempty list")
    output: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise BridgeError(f"row {index} must be an object")
        row_id = row.get("id")
        if not isinstance(row_id, str) or not row_id or row_id in seen:
            raise BridgeError("row IDs must be nonempty and unique")
        seen.add(row_id)
        kind = row.get("kind")
        if kind == "deflated-monotonicity":
            identifiers = [row.get("left"), row.get("right")]
        elif kind == "deflated-cross-loewner-determinant":
            left, right = row.get("rows"), row.get("columns")
            if not isinstance(left, list) or not isinstance(right, list):
                raise BridgeError("Loewner rows and columns must be lists")
            identifiers = left + right
        else:
            raise BridgeError(f"unsupported production row kind {kind!r}")
        if any(not isinstance(item, str) or item not in point_ids for item in identifiers):
            raise BridgeError(f"row {index} references an unknown point")
        output.append(row)
    return output


def parse_count_windows(counts: dict[str, Any], target: Fraction) -> list[dict[str, Any]]:
    if counts.get("schema") != COUNT_SCHEMA:
        raise BridgeError("total-count schema mismatch")
    if counts.get("classification") != COUNT_CLASSIFICATION:
        raise BridgeError("total-count artifact is not proof-classified")
    if rational(counts.get("target"), "counts.target") != target:
        raise BridgeError("primitive and total-count ordinates differ")
    raw_windows = counts.get("windows")
    if not isinstance(raw_windows, list) or not raw_windows:
        raise BridgeError("total-count windows must be nonempty")

    artifact_sha = canonical_sha(counts)
    output: list[dict[str, Any]] = []
    previous_radius = Fraction(0)
    previous_count = 0
    seen: set[str] = set()
    for index, raw in enumerate(raw_windows):
        if not isinstance(raw, dict):
            raise BridgeError(f"count window {index} must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in seen:
            raise BridgeError("count-window IDs must be nonempty and unique")
        seen.add(identifier)
        radius = rational(raw.get("radius"), f"windows[{index}].radius")
        if radius <= previous_radius:
            raise BridgeError("count-window radii must be strictly increasing")
        lower_endpoint = exact_binary(raw.get("lower_endpoint"), f"windows[{index}].lower_endpoint")
        upper_endpoint = exact_binary(raw.get("upper_endpoint"), f"windows[{index}].upper_endpoint")
        if lower_endpoint != target - radius or upper_endpoint != target + radius:
            raise BridgeError("count-window endpoints do not equal target plus/minus radius")
        n_lower_bounds = binary_interval(raw.get("N_lower_ball"), f"windows[{index}].N_lower_ball")
        n_upper_bounds = binary_interval(raw.get("N_upper_ball"), f"windows[{index}].N_upper_ball")
        n_lower = unique_integer(n_lower_bounds, f"windows[{index}].N_lower_ball")
        n_upper = unique_integer(n_upper_bounds, f"windows[{index}].N_upper_ball")
        if parse_integer(raw.get("N_lower"), f"windows[{index}].N_lower") != n_lower:
            raise BridgeError("N_lower field does not match its count ball")
        if parse_integer(raw.get("N_upper"), f"windows[{index}].N_upper") != n_upper:
            raise BridgeError("N_upper field does not match its count ball")
        count = n_upper - n_lower
        if count < 0:
            raise BridgeError("total zero count decreased across a window")
        if parse_integer(raw.get("count_lower"), f"windows[{index}].count_lower") != count:
            raise BridgeError("count_lower does not equal N_upper-N_lower")
        if count < previous_count:
            raise BridgeError("nested total-zero counts are not nondecreasing")
        output.append(
            {
                "id": identifier,
                "radius": fj(radius),
                "count_lower": count,
                "gate": {
                    "status": GATE,
                    "sha256": hashlib.sha256(
                        (artifact_sha + ":" + identifier).encode("ascii")
                    ).hexdigest(),
                },
            }
        )
        previous_radius = radius
        previous_count = count
    if previous_count <= 0:
        raise BridgeError("final nested total-zero count is zero")
    return output


def build(
    primitives: dict[str, Any], counts: dict[str, Any], config: dict[str, Any]
) -> dict[str, Any]:
    if primitives.get("schema") != PRIMITIVE_SCHEMA:
        raise BridgeError("primitive schema mismatch")
    if primitives.get("normalization_id") != NORMALIZATION:
        raise BridgeError("primitive normalization mismatch")
    if config.get("schema") != CONFIG_SCHEMA:
        raise BridgeError("config schema mismatch")
    if config.get("normalization_id") not in (None, NORMALIZATION):
        raise BridgeError("config normalization mismatch")
    common_scale = parse_integer(
        primitives.get("common_xi_scale_power_of_two", 0),
        "primitives.common_xi_scale_power_of_two",
    )

    target = rational(primitives.get("ordinate"), "primitives.ordinate")
    windows = parse_count_windows(counts, target)

    raw_points = primitives.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise BridgeError("primitive points must be a nonempty list")
    points: list[dict[str, Any]] = []
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
    log_terms = parse_integer(config.get("log_terms", 256), "config.log_terms")
    output = {
        "schema": OUTPUT_SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "normalization_id": NORMALIZATION,
        "common_xi_scale_power_of_two": common_scale,
        "ordinate": fj(target),
        "log_terms": log_terms,
        "points": sorted(points, key=lambda point: rational(point["u"], "point.u")),
        "count_windows": windows,
        "rows": rows,
        "source": {
            "primitive_schema": PRIMITIVE_SCHEMA,
            "primitive_sha256": canonical_sha(primitives),
            "primitive_common_xi_scale_power_of_two": common_scale,
            "total_count_schema": COUNT_SCHEMA,
            "total_count_sha256": canonical_sha(counts),
            "total_count_classification": COUNT_CLASSIFICATION,
        },
    }
    output["certificate_sha256"] = canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primitives", type=Path)
    parser.add_argument("counts", type=Path)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = build(load(args.primitives), load(args.counts), load(args.config))
    except (OSError, json.JSONDecodeError, BridgeError) as exc:
        print(json.dumps({"built": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "schema": result["schema"],
                "point_count": len(result["points"]),
                "count_window_count": len(result["count_windows"]),
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
