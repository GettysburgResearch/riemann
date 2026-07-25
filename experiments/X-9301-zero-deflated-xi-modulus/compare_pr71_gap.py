#!/usr/bin/env python3
"""Require exact identity and directed nesting across two PR71 gap certificates."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x5603-line-gap-discrepancy.v1"


class ComparisonError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ComparisonError(f"{path} must contain an object")
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
    raise ComparisonError(f"{name} must be integer or integer text")


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ComparisonError(f"{name} must be object")
    numerator = integer(raw.get("numerator"), f"{name}.numerator")
    denominator = integer(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise ComparisonError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def binary(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise ComparisonError(f"{name} must be object")
    mantissa = integer(raw.get("mantissa"), f"{name}.mantissa")
    exponent = integer(raw.get("exponent"), f"{name}.exponent")
    return Fraction(mantissa << exponent) if exponent >= 0 else Fraction(mantissa, 1 << (-exponent))


def interval(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise ComparisonError(f"{name} must be object")
    lower = binary(raw.get("lower"), f"{name}.lower")
    upper = binary(raw.get("upper"), f"{name}.upper")
    if lower > upper:
        raise ComparisonError(f"{name} reversed")
    return lower, upper


def compare(low: dict[str, Any], high: dict[str, Any]) -> dict[str, Any]:
    if low.get("schema") != SCHEMA or high.get("schema") != SCHEMA:
        raise ComparisonError("schema mismatch")
    for field in (
        "target",
        "lower_hardy_zero_index",
        "upper_hardy_zero_index",
        "N_lower",
        "N_upper",
        "total_zero_discrepancy_in_line_empty_slab",
        "classification",
    ):
        if low.get(field) != high.get(field):
            raise ComparisonError(f"precision artifacts differ in {field}")
    for field in ("lower_hardy_zero_ball", "upper_hardy_zero_ball"):
        low_interval = interval(low.get(field), f"low.{field}")
        high_interval = interval(high.get(field), f"high.{field}")
        if not (
            low_interval[0]
            <= high_interval[0]
            <= high_interval[1]
            <= low_interval[1]
        ):
            raise ComparisonError(f"high {field} is not nested")
    target = rational(low["target"], "target")
    lower = interval(high["lower_hardy_zero_ball"], "high.lower")
    upper = interval(high["upper_hardy_zero_ball"], "high.upper")
    if not lower[1] < target < upper[0]:
        raise ComparisonError("high-precision balls do not strictly bracket target")
    return {
        "schema": "riemann.x5603-gap-precision-comparison.v1",
        "target": low["target"],
        "low_precision_bits": integer(low.get("precision_bits"), "low.precision_bits"),
        "high_precision_bits": integer(high.get("precision_bits"), "high.precision_bits"),
        "classification": low["classification"],
        "total_zero_discrepancy_in_line_empty_slab": low[
            "total_zero_discrepancy_in_line_empty_slab"
        ],
        "hardy_zero_balls_nested": True,
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
