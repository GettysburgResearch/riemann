#!/usr/bin/env python3
"""Require primitive and row-interval nesting for two X-9301 certificates."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "verify_zero_deflated_modulus", ROOT / "verify_zero_deflated_modulus.py"
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
        raise ComparisonError(f"{path} must contain object")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ComparisonError(f"{name} must be object")
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
        raise ComparisonError(f"{name} must be object")
    lower = rational(raw.get("lower"), f"{name}.lower")
    upper = rational(raw.get("upper"), f"{name}.upper")
    if lower > upper:
        raise ComparisonError(f"{name} reversed")
    return lower, upper


def point_map(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    points = data.get("points")
    if not isinstance(points, list):
        raise ComparisonError("points must be list")
    result: dict[str, dict[str, Any]] = {}
    for point in points:
        if (
            not isinstance(point, dict)
            or not isinstance(point.get("id"), str)
            or point["id"] in result
        ):
            raise ComparisonError("bad point")
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
        "ordinate",
        "log_terms",
        "zero_bins",
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
            low_interval = interval(
                low_points[identifier]["xi_rectangle"][coordinate],
                f"low.{identifier}.{coordinate}",
            )
            high_interval = interval(
                high_points[identifier]["xi_rectangle"][coordinate],
                f"high.{identifier}.{coordinate}",
            )
            if not (
                low_interval[0]
                <= high_interval[0]
                <= high_interval[1]
                <= low_interval[1]
            ):
                raise ComparisonError(
                    f"high primitive not nested at {identifier}.{coordinate}"
                )
            nested_coordinates += 1

    low_result, high_result = VERIFY.verify(low), VERIFY.verify(high)
    low_rows, high_rows = row_map(low_result), row_map(high_result)
    if set(low_rows) != set(high_rows):
        raise ComparisonError("row outputs differ")
    nested_rows = 0
    for identifier in sorted(low_rows):
        low_interval = interval(low_rows[identifier]["interval"], f"low.row.{identifier}")
        high_interval = interval(
            high_rows[identifier]["interval"], f"high.row.{identifier}"
        )
        if not (
            low_interval[0]
            <= high_interval[0]
            <= high_interval[1]
            <= low_interval[1]
        ):
            raise ComparisonError(f"high row not nested at {identifier}")
        nested_rows += 1

    return {
        "schema": "riemann.x9301-precision-comparison.v1",
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
    except (
        OSError,
        json.JSONDecodeError,
        ComparisonError,
        VERIFY.CertificateError,
    ) as exc:
        print(json.dumps({"compared": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
