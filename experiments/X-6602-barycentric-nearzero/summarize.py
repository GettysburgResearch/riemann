#!/usr/bin/env python3
"""Summarize and compare exact eight-node barycentric verification intervals."""
from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

PREFIX = "bary8_"
SCHEMA = "riemann.xi-barycentric-nearzero-summary.v1"


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} must not be bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return int(value, 10)
    raise ValueError(f"{name} must be an integer")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise ValueError(f"{name}.denominator must be positive")
    return Fraction(
        parse_int(value.get("numerator"), f"{name}.numerator"), denominator
    )


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def scientific(value: Fraction, digits: int = 25) -> str:
    with localcontext() as context:
        context.prec = digits
        decimal = Decimal(value.numerator) / Decimal(value.denominator)
        return f"{decimal:.{digits - 1}E}"


def load_rows(path: Path) -> tuple[dict[str, Any], dict[str, tuple[Fraction, Fraction, str]]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("verified") is not True:
        raise ValueError(f"{path}: verification is not accepted")
    channels = data.get("channels")
    if not isinstance(channels, list):
        raise ValueError(f"{path}: channels must be an array")
    rows: dict[str, tuple[Fraction, Fraction, str]] = {}
    for index, channel in enumerate(channels):
        if not isinstance(channel, dict):
            raise ValueError(f"{path}: channel {index} is malformed")
        identifier = channel.get("id")
        if not isinstance(identifier, str) or not identifier.startswith(PREFIX):
            continue
        interval = channel.get("interval")
        if not isinstance(interval, dict):
            raise ValueError(f"{path}: {identifier} has no interval")
        lower = parse_fraction(interval.get("lower"), f"{identifier}.lower")
        upper = parse_fraction(interval.get("upper"), f"{identifier}.upper")
        status = channel.get("status")
        if status not in {
            "CERTIFIED_NEGATIVE",
            "CERTIFIED_NONNEGATIVE",
            "UNRESOLVED_ZERO_TOUCH",
        }:
            raise ValueError(f"{path}: {identifier} has unsupported status {status!r}")
        if identifier in rows:
            raise ValueError(f"{path}: duplicate row {identifier}")
        rows[identifier] = (lower, upper, status)
    if not rows:
        raise ValueError(f"{path}: no barycentric rows found")
    return data, rows


def summarize(path: Path) -> dict[str, object]:
    source, rows = load_rows(path)
    ordered = sorted(rows.items(), key=lambda item: (item[1][1], item[1][0], item[0]))
    counts = {
        status: sum(1 for _, (_, _, row_status) in rows.items() if row_status == status)
        for status in (
            "CERTIFIED_NEGATIVE",
            "CERTIFIED_NONNEGATIVE",
            "UNRESOLVED_ZERO_TOUCH",
        )
    }
    tightest_id, (tightest_lower, tightest_upper, tightest_status) = ordered[0]
    return {
        "schema": SCHEMA,
        "source": str(path),
        "source_verification_sha256": source.get("verification_sha256"),
        "row_count": len(rows),
        "counts": counts,
        "tightest": {
            "id": tightest_id,
            "status": tightest_status,
            "lower": fraction_json(tightest_lower),
            "upper": fraction_json(tightest_upper),
            "lower_scientific": scientific(tightest_lower),
            "upper_scientific": scientific(tightest_upper),
            "width_scientific": scientific(tightest_upper - tightest_lower),
        },
        "rows_by_upper_endpoint": [
            {
                "id": identifier,
                "status": status,
                "lower_scientific": scientific(lower),
                "upper_scientific": scientific(upper),
                "width_scientific": scientific(upper - lower),
            }
            for identifier, (lower, upper, status) in ordered
        ],
        "proof_boundary": (
            "Rows are exact contractions of the supplied outward primitive rectangles. "
            "A negative requires independent directed special-function reproduction."
        ),
    }


def compare(low_path: Path, high_path: Path) -> dict[str, object]:
    _, low = load_rows(low_path)
    _, high = load_rows(high_path)
    if set(low) != set(high):
        raise ValueError("precision runs have different row IDs")
    failures: list[dict[str, str]] = []
    sign_changes: list[dict[str, str]] = []
    for identifier in sorted(low):
        low_lower, low_upper, low_status = low[identifier]
        high_lower, high_upper, high_status = high[identifier]
        if high_lower < low_lower or high_upper > low_upper:
            failures.append(
                {
                    "id": identifier,
                    "low": f"[{low_lower},{low_upper}]",
                    "high": f"[{high_lower},{high_upper}]",
                }
            )
        if high_status != low_status:
            sign_changes.append(
                {"id": identifier, "low_status": low_status, "high_status": high_status}
            )
    return {
        "schema": "riemann.xi-barycentric-nesting-audit.v1",
        "low_source": str(low_path),
        "high_source": str(high_path),
        "row_count": len(low),
        "nested_count": len(low) - len(failures),
        "nesting_failures": failures,
        "status_changes": sign_changes,
        "all_nested": not failures,
    }


def write(value: object, path: Path | None) -> None:
    text = json.dumps(value, indent=2, sort_keys=True) + "\n"
    if path:
        path.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    one = subparsers.add_parser("summarize")
    one.add_argument("verification", type=Path)
    one.add_argument("--output", type=Path)
    two = subparsers.add_parser("compare")
    two.add_argument("low", type=Path)
    two.add_argument("high", type=Path)
    two.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    if args.command == "summarize":
        write(summarize(args.verification), args.output)
        return 0
    result = compare(args.low, args.high)
    write(result, args.output)
    return 0 if result["all_nested"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
