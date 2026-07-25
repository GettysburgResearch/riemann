#!/usr/bin/env python3
"""Compare two exact cross-height verification ladders and require nesting."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(raw: Any) -> Fraction:
    if not isinstance(raw, dict):
        raise ValueError("fraction must be an object")
    return Fraction(int(raw["numerator"]), int(raw["denominator"]))


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def compare(low: dict[str, Any], high: dict[str, Any]) -> dict[str, object]:
    low_rows = {str(row["id"]): row for row in low["channels"]}
    high_rows = {str(row["id"]): row for row in high["channels"]}
    if low_rows.keys() != high_rows.keys():
        raise ValueError("precision ladders use different channel IDs")
    failures = []
    for identifier in sorted(low_rows):
        low_interval = low_rows[identifier]["interval"]
        high_interval = high_rows[identifier]["interval"]
        lower_low = parse_fraction(low_interval["lower"])
        upper_low = parse_fraction(low_interval["upper"])
        lower_high = parse_fraction(high_interval["lower"])
        upper_high = parse_fraction(high_interval["upper"])
        if not (lower_low <= lower_high <= upper_high <= upper_low):
            failures.append(identifier)
        if low_rows[identifier]["vector"] != high_rows[identifier]["vector"]:
            raise ValueError(f"vector drift in {identifier}")
    return {
        "schema": "riemann.xi-cross-height-pick-ladder.v1",
        "channel_count": len(low_rows),
        "all_high_precision_intervals_nested": not failures,
        "nesting_failures": failures,
        "low_status": low["status"],
        "high_status": high["status"],
        "counterexample_candidate": None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("low", type=Path)
    parser.add_argument("high", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = compare(load(args.low), load(args.high))
    if not result["all_high_precision_intervals_nested"]:
        raise SystemExit("precision intervals failed nesting")
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
