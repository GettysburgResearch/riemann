#!/usr/bin/env python3
"""Require primitive and row nesting for two total-count-deflated certificates."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "verify_total_count_deflation", ROOT / "verify_total_count_deflation.py"
)
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)


class ComparisonError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ComparisonError(f"{path} must contain an object")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ComparisonError(f"{name} must be an object")
    numerator, denominator = raw.get("numerator"), raw.get("denominator")
    if (
        isinstance(numerator, bool)
        or not isinstance(numerator, int)
        or isinstance(denominator, bool)
        or not isinstance(denominator, int)
        or denominator <= 0
    ):
        raise ComparisonError(f"bad rational at {name}")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise ComparisonError(f"{name} must be an object")
    lower = rational(raw.get("lower"), f"{name}.lower")
    upper = rational(raw.get("upper"), f"{name}.upper")
    if lower > upper:
        raise ComparisonError(f"{name} is reversed")
    return lower, upper


def point_map(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = data.get("points")
    if not isinstance(raw, list):
        raise ComparisonError("points must be a list")
    result: dict[str, dict[str, Any]] = {}
    for point in raw:
        if (
            not isinstance(point, dict)
            or not isinstance(point.get("id"), str)
            or point["id"] in result
        ):
            raise ComparisonError("malformed or duplicate point")
        result[point["id"]] = point
    return result


def row_map(result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for row in result["rows"]:
        if row["id"] in rows:
            raise ComparisonError("duplicate row output")
        rows[row["id"]] = row
    return rows


def compare(low: dict[str, Any], high: dict[str, Any]) -> dict[str, Any]:
    for field in (
        "schema",
        "classification",
        "normalization_id",
        "common_xi_scale_power_of_two",
        "ordinate",
        "log_terms",
        "count_windows",
        "rows",
    ):
        if low.get(field) != high.get(field):
            raise ComparisonError(f"certificates differ in {field}")

    low_points, high_points = point_map(low), point_map(high)
    if set(low_points) != set(high_points):
        raise ComparisonError("point sets differ")
    nested_coordinates = 0
    for identifier in sorted(low_points):
        if low_points[identifier].get("u") != high_points[identifier].get("u"):
            raise ComparisonError(f"node differs at {identifier}")
        for coordinate in ("real", "imag"):
            low_bounds = interval(
                low_points[identifier]["xi_rectangle"][coordinate],
                f"low.{identifier}.{coordinate}",
            )
            high_bounds = interval(
                high_points[identifier]["xi_rectangle"][coordinate],
                f"high.{identifier}.{coordinate}",
            )
            if not low_bounds[0] <= high_bounds[0] <= high_bounds[1] <= low_bounds[1]:
                raise ComparisonError(
                    f"higher-precision primitive is not nested at {identifier}.{coordinate}"
                )
            nested_coordinates += 1

    low_result, high_result = VERIFY.verify(low), VERIFY.verify(high)
    low_rows, high_rows = row_map(low_result), row_map(high_result)
    if set(low_rows) != set(high_rows):
        raise ComparisonError("row outputs differ")
    nested_rows = 0
    for identifier in sorted(low_rows):
        low_bounds = interval(low_rows[identifier]["interval"], f"low.row.{identifier}")
        high_bounds = interval(high_rows[identifier]["interval"], f"high.row.{identifier}")
        if not low_bounds[0] <= high_bounds[0] <= high_bounds[1] <= low_bounds[1]:
            raise ComparisonError(f"higher-precision row is not nested at {identifier}")
        nested_rows += 1

    return {
        "schema": "riemann.x9302-total-deflation-precision-comparison.v1",
        "point_count": len(low_points),
        "nested_primitive_coordinates": nested_coordinates,
        "row_count": len(low_rows),
        "nested_row_intervals": nested_rows,
        "low_verdict": low_result["verdict"],
        "high_verdict": high_result["verdict"],
        "low_negative_rows": low_result["certified_negative_rows"],
        "high_negative_rows": high_result["certified_negative_rows"],
        "low_unresolved_rows": low_result["unresolved_rows"],
        "high_unresolved_rows": high_result["unresolved_rows"],
        "all_high_intervals_nested": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("low", type=Path)
    parser.add_argument("high", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = compare(load(args.low), load(args.high))
        code = 0
    except (OSError, json.JSONDecodeError, ComparisonError, VERIFY.CertificateError) as exc:
        result = {
            "schema": "riemann.x9302-total-deflation-precision-comparison.v1",
            "compared": False,
            "error": str(exc),
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
