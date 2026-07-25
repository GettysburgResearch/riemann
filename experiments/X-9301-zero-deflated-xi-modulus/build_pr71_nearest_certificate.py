#!/usr/bin/env python3
"""Bind direct-xi primitives to the nearest proof-grade PR71 Hardy-zero balls."""
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
BLOCK_SCHEMA = "riemann.x9301-pr71-hardy-zero-block.v1"
CONFIG_SCHEMA = "riemann.xi-modulus-zero-deflation-config.v1"
OUTPUT_SCHEMA = "riemann.xi-modulus-zero-deflation.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
GATE = "CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND"


class BuildError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise BuildError(f"{path} must contain an object")
    return value


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise BuildError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise BuildError(f"{name} must be integer text") from exc
    raise BuildError(f"{name} must be an integer")


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise BuildError(f"{name} must be an object")
    numerator = integer(raw.get("numerator"), f"{name}.numerator")
    denominator = integer(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise BuildError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def binary_value(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise BuildError(f"{name} must be an object")
    mantissa = integer(raw.get("mantissa"), f"{name}.mantissa")
    exponent = integer(raw.get("exponent"), f"{name}.exponent")
    return Fraction(mantissa << exponent) if exponent >= 0 else Fraction(mantissa, 1 << (-exponent))


def binary_interval(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise BuildError(f"{name} must be an object")
    lower = binary_value(raw.get("lower"), f"{name}.lower")
    upper = binary_value(raw.get("upper"), f"{name}.upper")
    if lower > upper:
        raise BuildError(f"{name} is reversed")
    return lower, upper


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def validate_rows(config: dict[str, Any], point_ids: set[str]) -> list[dict[str, Any]]:
    if config.get("schema") != CONFIG_SCHEMA:
        raise BuildError("config schema mismatch")
    if config.get("normalization_id") not in (None, NORMALIZATION):
        raise BuildError("config normalization mismatch")
    raw_rows = config.get("rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise BuildError("rows must be nonempty")
    seen: set[str] = set()
    for index, row in enumerate(raw_rows):
        if (
            not isinstance(row, dict)
            or not isinstance(row.get("id"), str)
            or not row["id"]
            or row["id"] in seen
        ):
            raise BuildError("row IDs must be nonempty and unique")
        seen.add(row["id"])
        kind = row.get("kind")
        if kind == "deflated-monotonicity":
            used = [row.get("left"), row.get("right")]
        elif kind == "deflated-cross-loewner-determinant":
            if not isinstance(row.get("rows"), list) or not isinstance(
                row.get("columns"), list
            ):
                raise BuildError("Loewner rows and columns must be lists")
            used = row["rows"] + row["columns"]
        else:
            raise BuildError(f"unsupported row kind {kind!r}")
        if any(
            not isinstance(identifier, str) or identifier not in point_ids
            for identifier in used
        ):
            raise BuildError(f"row {index} references an unknown point")
    return raw_rows


def build(
    primitives: dict[str, Any],
    block: dict[str, Any],
    config: dict[str, Any],
    nearest_count: int,
) -> dict[str, Any]:
    if (
        primitives.get("schema") != PRIMITIVE_SCHEMA
        or primitives.get("normalization_id") != NORMALIZATION
    ):
        raise BuildError("primitive schema/normalization mismatch")
    if (
        block.get("schema") != BLOCK_SCHEMA
        or block.get("classification") != "CERTIFIED_CRITICAL_LINE_ZERO_BLOCK"
    ):
        raise BuildError("zero block is not proof classified")
    if nearest_count <= 0:
        raise BuildError("nearest_count must be positive")

    ordinate = rational(primitives.get("ordinate"), "primitives.ordinate")
    if ordinate != rational(block.get("target"), "block.target"):
        raise BuildError("ordinate mismatch")

    raw_points = primitives.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise BuildError("points missing")
    points: list[dict[str, Any]] = []
    point_ids: set[str] = set()
    for index, point in enumerate(raw_points):
        if (
            not isinstance(point, dict)
            or not isinstance(point.get("id"), str)
            or not point["id"]
            or point["id"] in point_ids
        ):
            raise BuildError("bad point")
        point_ids.add(point["id"])
        x = rational(point.get("x"), f"point {index}.x")
        if (
            x <= 0
            or not isinstance(point.get("xi_rectangle"), dict)
            or point.get("functional_equation_residual_contains_zero") is not True
        ):
            raise BuildError("invalid primitive point")
        canonical = {
            "id": point["id"],
            "u": fraction_json(x * x),
            "xi_rectangle": point["xi_rectangle"],
        }
        points.append({**canonical, "point_sha256": canonical_sha(canonical)})

    requested_rows = validate_rows(config, point_ids)
    log_terms = integer(config.get("log_terms", 256), "log_terms")

    raw_zeros = block.get("zeros")
    if not isinstance(raw_zeros, list) or len(raw_zeros) < nearest_count:
        raise BuildError("insufficient zero balls")
    parsed: list[dict[str, Any]] = []
    previous_upper: Fraction | None = None
    seen_indices: set[int] = set()
    for index, zero in enumerate(raw_zeros):
        if not isinstance(zero, dict):
            raise BuildError("bad zero record")
        zero_index = integer(zero.get("zero_index"), f"zero {index}.index")
        if zero_index in seen_indices:
            raise BuildError("duplicate zero index")
        seen_indices.add(zero_index)
        lower, upper = binary_interval(zero.get("ball"), f"zero {index}.ball")
        if previous_upper is not None and previous_upper >= lower:
            raise BuildError("zero balls overlap or touch")
        previous_upper = upper
        distance_square_upper = max(
            (ordinate - lower) ** 2,
            (ordinate - upper) ** 2,
        )
        parsed.append(
            {
                "index": zero_index,
                "lower": lower,
                "upper": upper,
                "B": distance_square_upper,
            }
        )

    parsed.sort(key=lambda item: (item["B"], item["index"]))
    selected = parsed[:nearest_count]
    rank_by_index = {item["index"]: rank + 1 for rank, item in enumerate(selected)}
    block_digest = canonical_sha(block)

    zero_bins: list[dict[str, Any]] = []
    for zero in sorted(selected, key=lambda item: (item["lower"], item["upper"])):
        gate_digest = hashlib.sha256(
            f"{block_digest}:{zero['index']}".encode("ascii")
        ).hexdigest()
        zero_bins.append(
            {
                "id": f"pr71-zero-{zero['index']}",
                "lower_ordinate": fraction_json(zero["lower"]),
                "upper_ordinate": fraction_json(zero["upper"]),
                "count_lower": 1,
                "gate": {"status": GATE, "sha256": gate_digest},
                "distance_rank": rank_by_index[zero["index"]],
                "distance_square_upper": fraction_json(zero["B"]),
            }
        )

    output = {
        "schema": OUTPUT_SCHEMA,
        "classification": "RIEMANN_XI_DIRECTED",
        "normalization_id": NORMALIZATION,
        "ordinate": fraction_json(ordinate),
        "log_terms": log_terms,
        "points": sorted(points, key=lambda point: rational(point["u"], "point.u")),
        "zero_bins": zero_bins,
        "rows": requested_rows,
        "source": {
            "primitive_sha256": canonical_sha(primitives),
            "zero_block_sha256": block_digest,
            "zero_block_precision_bits": integer(
                block.get("precision_bits"), "block.precision_bits"
            ),
            "nearest_count": nearest_count,
            "selected_zero_indices": [item["index"] for item in selected],
        },
    }
    output["certificate_sha256"] = canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primitives", type=Path)
    parser.add_argument("block", type=Path)
    parser.add_argument("config", type=Path)
    parser.add_argument("--nearest-count", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = build(
            load(args.primitives),
            load(args.block),
            load(args.config),
            args.nearest_count,
        )
    except (OSError, json.JSONDecodeError, BuildError) as exc:
        print(json.dumps({"built": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "schema": result["schema"],
                "nearest_count": args.nearest_count,
                "selected_zero_indices": result["source"]["selected_zero_indices"],
                "certificate_sha256": result["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
