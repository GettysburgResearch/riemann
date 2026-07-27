#!/usr/bin/env python3
"""Compare two rigorous line-gap discrepancy certificates."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

BALL_FIELDS = (
    "lower_hardy_zero_ball",
    "upper_hardy_zero_ball",
    "line_gap",
)


def endpoint(raw: dict[str, str]) -> Fraction:
    mantissa = int(raw["mantissa"])
    exponent = int(raw["exponent"])
    if exponent >= 0:
        return Fraction(mantissa << exponent, 1)
    return Fraction(mantissa, 1 << (-exponent))


def interval(raw: dict[str, object]) -> tuple[Fraction, Fraction]:
    return endpoint(raw["lower"]), endpoint(raw["upper"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("low", type=Path)
    parser.add_argument("high", type=Path)
    args = parser.parse_args()
    low = json.loads(args.low.read_text(encoding="utf-8"))
    high = json.loads(args.high.read_text(encoding="utf-8"))

    exact_fields = (
        "lower_hardy_zero_index",
        "upper_hardy_zero_index",
        "N_lower",
        "N_upper",
        "total_zero_discrepancy_in_line_empty_slab",
        "classification",
    )
    mismatches = {
        key: {"low": low.get(key), "high": high.get(key)}
        for key in exact_fields
        if low.get(key) != high.get(key)
    }

    nesting_failures = []
    for key in BALL_FIELDS:
        low_lo, low_hi = interval(low[key])
        high_lo, high_hi = interval(high[key])
        if high_lo < low_lo or high_hi > low_hi:
            nesting_failures.append(key)

    result = {
        "schema": "riemann.x5603-line-gap-discrepancy-comparison.v1",
        "verified": not mismatches and not nesting_failures,
        "exact_field_mismatches": mismatches,
        "ball_nesting_failures": nesting_failures,
        "nested_ball_fields": [key for key in BALL_FIELDS if key not in nesting_failures],
        "classification": high.get("classification"),
        "discrepancy": high.get("total_zero_discrepancy_in_line_empty_slab"),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["verified"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
