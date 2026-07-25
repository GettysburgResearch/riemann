#!/usr/bin/env python3
"""Require indexed Hardy-zero ball nesting across two X-9301 block runs."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x9301-pr71-hardy-zero-block.v1"


class ComparisonError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ComparisonError("root must be an object")
    return value


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ComparisonError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise ComparisonError(f"{name} must be integer text") from exc
    raise ComparisonError(f"{name} must be an integer")


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ComparisonError(f"{name} must be an object")
    numerator = integer(raw.get("numerator"), f"{name}.numerator")
    denominator = integer(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise ComparisonError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def binary_value(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ComparisonError(f"{name} must be an object")
    mantissa = integer(raw.get("mantissa"), f"{name}.mantissa")
    exponent = integer(raw.get("exponent"), f"{name}.exponent")
    return Fraction(mantissa << exponent) if exponent >= 0 else Fraction(mantissa, 1 << (-exponent))


def interval(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise ComparisonError(f"{name} must be an object")
    lower = binary_value(raw.get("lower"), f"{name}.lower")
    upper = binary_value(raw.get("upper"), f"{name}.upper")
    if lower > upper:
        raise ComparisonError(f"{name} is reversed")
    return lower, upper


def zero_map(data: dict[str, Any]) -> dict[int, tuple[Fraction, Fraction]]:
    raw_zeros = data.get("zeros")
    if not isinstance(raw_zeros, list):
        raise ComparisonError("zeros must be a list")
    result: dict[int, tuple[Fraction, Fraction]] = {}
    for zero in raw_zeros:
        if not isinstance(zero, dict):
            raise ComparisonError("bad zero record")
        zero_index = integer(zero.get("zero_index"), "zero_index")
        if zero_index in result:
            raise ComparisonError("duplicate zero index")
        result[zero_index] = interval(zero.get("ball"), f"zero.{zero_index}")
    return result


def compare(low: dict[str, Any], high: dict[str, Any]) -> dict[str, Any]:
    for data in (low, high):
        if (
            data.get("schema") != SCHEMA
            or data.get("classification") != "CERTIFIED_CRITICAL_LINE_ZERO_BLOCK"
        ):
            raise ComparisonError("schema/classification mismatch")
    for field in (
        "target",
        "requested_start_index",
        "requested_length",
        "returned_count",
        "target_below_zero_index",
        "target_above_zero_index",
    ):
        if low.get(field) != high.get(field):
            raise ComparisonError(f"precision artifacts differ in {field}")

    low_zeros, high_zeros = zero_map(low), zero_map(high)
    if set(low_zeros) != set(high_zeros):
        raise ComparisonError("zero-index sets differ")
    for zero_index in sorted(low_zeros):
        low_interval = low_zeros[zero_index]
        high_interval = high_zeros[zero_index]
        if not (
            low_interval[0]
            <= high_interval[0]
            <= high_interval[1]
            <= low_interval[1]
        ):
            raise ComparisonError(f"high ball is not nested at index {zero_index}")

    ordered = [high_zeros[index] for index in sorted(high_zeros)]
    if any(
        ordered[index][1] >= ordered[index + 1][0]
        for index in range(len(ordered) - 1)
    ):
        raise ComparisonError("high-precision zero balls overlap or touch")

    target = rational(low["target"], "target")
    below = integer(low["target_below_zero_index"], "target_below_zero_index")
    above = integer(low["target_above_zero_index"], "target_above_zero_index")
    if not high_zeros[below][1] < target < high_zeros[above][0]:
        raise ComparisonError("target is not strictly bracketed")

    return {
        "schema": "riemann.x9301-pr71-zero-block-comparison.v1",
        "zero_count": len(low_zeros),
        "low_precision_bits": integer(low.get("precision_bits"), "low.precision_bits"),
        "high_precision_bits": integer(
            high.get("precision_bits"), "high.precision_bits"
        ),
        "all_high_balls_nested": True,
        "strict_target_bracketing": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("low", type=Path)
    parser.add_argument("high", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = compare(load(args.low), load(args.high))
    except (OSError, json.JSONDecodeError, ComparisonError) as exc:
        print(json.dumps({"compared": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
