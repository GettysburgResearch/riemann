#!/usr/bin/env python3
"""Adapt an X-7501 direct-xi certificate to the X-9301 zero-deflated schema."""
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

SOURCE_SCHEMA = "riemann.xi-modulus-witness.v1"
CONFIG_SCHEMA = "riemann.xi-modulus-zero-deflation-config.v1"
OUTPUT_SCHEMA = "riemann.xi-modulus-zero-deflation.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


class AdapterError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AdapterError(f"{path} must contain an object")
    return value


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise AdapterError(f"{name} must be an integer")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise AdapterError(f"{name} must be an object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise AdapterError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def point_map(raw_points: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(raw_points, list) or not raw_points:
        raise AdapterError("source points must be a nonempty list")
    result: dict[str, dict[str, Any]] = {}
    for index, point in enumerate(raw_points):
        if not isinstance(point, dict):
            raise AdapterError(f"source point {index} must be an object")
        identifier = point.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in result:
            raise AdapterError("source point ids must be nonempty and unique")
        result[identifier] = point
    return result


def referenced_ids(rows: Any) -> set[str]:
    if not isinstance(rows, list) or not rows:
        raise AdapterError("config rows must be a nonempty list")
    result: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise AdapterError(f"config row {index} must be an object")
        kind = row.get("kind")
        if kind in ("raw-monotonicity", "deflated-monotonicity"):
            for field in ("left", "right"):
                value = row.get(field)
                if not isinstance(value, str):
                    raise AdapterError(f"row {index}.{field} must be a point id")
                result.add(value)
        elif kind in (
            "raw-cross-loewner-determinant",
            "deflated-cross-loewner-determinant",
        ):
            for field in ("rows", "columns"):
                values = row.get(field)
                if not isinstance(values, list) or not values or any(
                    not isinstance(value, str) for value in values
                ):
                    raise AdapterError(f"row {index}.{field} must be a nonempty id list")
                result.update(values)
        else:
            raise AdapterError(f"unsupported config row kind {kind!r}")
    return result


def adapt(source: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    if source.get("schema") != SOURCE_SCHEMA:
        raise AdapterError("source schema mismatch")
    if source.get("normalization_id") != NORMALIZATION:
        raise AdapterError("source normalization mismatch")
    if config.get("schema") != CONFIG_SCHEMA:
        raise AdapterError("config schema mismatch")
    if config.get("normalization_id") not in (None, NORMALIZATION):
        raise AdapterError("config normalization mismatch")

    classification = source.get("classification")
    if classification not in ("SYNTHETIC_MODEL", "RIEMANN_XI_DIRECTED"):
        raise AdapterError("source classification cannot be promoted")
    ordinate = rational(source.get("ordinate"), "source.ordinate")
    rows = config.get("rows")
    needed = referenced_ids(rows)
    source_points = point_map(source.get("points"))
    if not needed <= source_points.keys():
        missing = sorted(needed - source_points.keys())
        raise AdapterError(f"config references missing source points: {missing}")

    points = []
    for identifier in sorted(
        needed,
        key=lambda key: rational(source_points[key].get("x"), f"point {key}.x"),
    ):
        source_point = source_points[identifier]
        x = rational(source_point.get("x"), f"point {identifier}.x")
        if x <= 0:
            raise AdapterError("source horizontal offsets must be positive")
        rectangle = source_point.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise AdapterError(f"source point {identifier} lacks xi_rectangle")
        canonical = {
            "id": identifier,
            "u": fj(x * x),
            "xi_rectangle": rectangle,
        }
        points.append(
            {
                **canonical,
                "point_sha256": canonical_sha(canonical),
                "source_point_sha256": source_point.get("point_sha256"),
            }
        )

    zero_bins = config.get("zero_bins")
    if not isinstance(zero_bins, list) or not zero_bins:
        raise AdapterError("config zero_bins must be a nonempty list")
    log_terms = exact_int(config.get("log_terms", 256), "config.log_terms")

    output = {
        "schema": OUTPUT_SCHEMA,
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "ordinate": fj(ordinate),
        "log_terms": log_terms,
        "points": points,
        "zero_bins": zero_bins,
        "rows": rows,
        "source": {
            "schema": SOURCE_SCHEMA,
            "canonical_sha256": canonical_sha(source),
            "declared_certificate_sha256": source.get("certificate_sha256"),
        },
    }
    output["certificate_sha256"] = canonical_sha(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = adapt(load(args.source), load(args.config))
    except (OSError, json.JSONDecodeError, AdapterError) as exc:
        print(json.dumps({"adapted": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "schema": output["schema"],
                "point_count": len(output["points"]),
                "row_count": len(output["rows"]),
                "zero_bin_count": len(output["zero_bins"]),
                "certificate_sha256": output["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
