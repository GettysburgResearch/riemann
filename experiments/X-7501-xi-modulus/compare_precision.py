#!/usr/bin/env python3
"""Check exact identity and rectangle nesting across two xi-modulus productions."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from verify_log_localizer import verify as verify_log_localizer
from verify_modulus_certificate import verify as verify_modulus


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
        raise ComparisonError(f"inverted interval at {name}")
    return lower, upper


def point_map(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    points = data.get("points")
    if not isinstance(points, list):
        raise ComparisonError("points must be a list")
    result = {}
    for raw in points:
        if not isinstance(raw, dict) or not isinstance(raw.get("id"), str):
            raise ComparisonError("malformed point")
        identifier = raw["id"]
        if identifier in result:
            raise ComparisonError("duplicate point")
        result[identifier] = raw
    return result


def compare(low: dict[str, Any], high: dict[str, Any]) -> dict[str, Any]:
    for field in (
        "schema",
        "classification",
        "normalization_id",
        "ordinate",
        "rows",
        "log_rows",
    ):
        if low.get(field) != high.get(field):
            raise ComparisonError(f"precision files differ in {field}")

    low_points, high_points = point_map(low), point_map(high)
    if set(low_points) != set(high_points):
        raise ComparisonError("point sets differ")

    nested_coordinates = 0
    for identifier in sorted(low_points):
        low_point, high_point = low_points[identifier], high_points[identifier]
        if low_point.get("x") != high_point.get("x"):
            raise ComparisonError(f"point coordinate differs for {identifier}")
        for coordinate in ("real", "imag"):
            low_interval = interval(
                low_point["xi_rectangle"][coordinate],
                f"low.{identifier}.{coordinate}",
            )
            high_interval = interval(
                high_point["xi_rectangle"][coordinate],
                f"high.{identifier}.{coordinate}",
            )
            if not (
                low_interval[0]
                <= high_interval[0]
                <= high_interval[1]
                <= low_interval[1]
            ):
                raise ComparisonError(
                    f"high-precision rectangle is not nested for {identifier}.{coordinate}"
                )
            nested_coordinates += 1

    low_modulus, high_modulus = verify_modulus(low), verify_modulus(high)
    low_log, high_log = verify_log_localizer(low), verify_log_localizer(high)
    return {
        "schema": "riemann.xi-modulus-precision-comparison.v1",
        "point_count": len(low_points),
        "nested_coordinate_intervals": nested_coordinates,
        "low_modulus_verdict": low_modulus["verdict"],
        "high_modulus_verdict": high_modulus["verdict"],
        "low_modulus_negative_rows": low_modulus["certified_negative_rows"],
        "high_modulus_negative_rows": high_modulus["certified_negative_rows"],
        "low_modulus_unresolved_rows": low_modulus["unresolved_rows"],
        "high_modulus_unresolved_rows": high_modulus["unresolved_rows"],
        "low_log_localizer_verdict": low_log["verdict"],
        "high_log_localizer_verdict": high_log["verdict"],
        "low_log_localizer_negative_rows": low_log["certified_negative_rows"],
        "high_log_localizer_negative_rows": high_log["certified_negative_rows"],
        "low_log_localizer_unresolved_rows": low_log["unresolved_rows"],
        "high_log_localizer_unresolved_rows": high_log["unresolved_rows"],
        "all_high_rectangles_nested": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("low", type=Path)
    parser.add_argument("high", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = compare(load(args.low), load(args.high))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
