#!/usr/bin/env python3
"""Rebind an indexed Hardy-zero block to another exact target ordinate."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

SCHEMA = "riemann.x9301-pr71-hardy-zero-block.v1"
CLASSIFICATION = "CERTIFIED_CRITICAL_LINE_ZERO_BLOCK"


class RebindError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RebindError(f"{path} must contain an object")
    return value


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise RebindError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise RebindError(f"{name} must be integer text") from exc
    raise RebindError(f"{name} must be an integer")


def binary_value(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise RebindError(f"{name} must be an object")
    mantissa = integer(raw.get("mantissa"), f"{name}.mantissa")
    exponent = integer(raw.get("exponent"), f"{name}.exponent")
    return (
        Fraction(mantissa << exponent)
        if exponent >= 0
        else Fraction(mantissa, 1 << (-exponent))
    )


def binary_interval(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise RebindError(f"{name} must be an object")
    lower = binary_value(raw.get("lower"), f"{name}.lower")
    upper = binary_value(raw.get("upper"), f"{name}.upper")
    if lower > upper:
        raise RebindError(f"{name} is reversed")
    return lower, upper


def rebind(
    block: dict[str, Any], numerator: int, denominator: int = 1 << 32
) -> dict[str, Any]:
    if (
        block.get("schema") != SCHEMA
        or block.get("classification") != CLASSIFICATION
    ):
        raise RebindError("source block schema/classification mismatch")
    if denominator <= 0:
        raise RebindError("target denominator must be positive")
    target = Fraction(numerator, denominator)
    raw_zeros = block.get("zeros")
    if not isinstance(raw_zeros, list) or len(raw_zeros) < 4:
        raise RebindError("source block must contain at least four zeros")
    if integer(block.get("returned_count"), "returned_count") != len(raw_zeros):
        raise RebindError("source returned_count mismatch")
    if integer(block.get("requested_length"), "requested_length") != len(raw_zeros):
        raise RebindError("source requested_length mismatch")
    start = integer(block.get("requested_start_index"), "requested_start_index")

    parsed: list[tuple[int, Fraction, Fraction]] = []
    previous_upper: Fraction | None = None
    for position, zero in enumerate(raw_zeros):
        if not isinstance(zero, dict):
            raise RebindError(f"zero {position} must be an object")
        if integer(zero.get("local_index"), f"zero {position}.local_index") != position:
            raise RebindError("zero local indices are not consecutive")
        zero_index = integer(zero.get("zero_index"), f"zero {position}.zero_index")
        if zero_index != start + position:
            raise RebindError("zero indices are not consecutive")
        lower, upper = binary_interval(zero.get("ball"), f"zero {position}.ball")
        if previous_upper is not None and previous_upper >= lower:
            raise RebindError("zero balls overlap, touch, or are unordered")
        previous_upper = upper
        if lower <= target <= upper:
            raise RebindError("target overlaps a certified zero ball")
        parsed.append((zero_index, lower, upper))

    below = [
        (position, zero)
        for position, zero in enumerate(parsed)
        if zero[2] < target
    ]
    above = [
        (position, zero)
        for position, zero in enumerate(parsed)
        if zero[1] > target
    ]
    if not below or not above:
        raise RebindError("target is not strictly inside the zero block")
    below_position, below_zero = below[-1]
    above_position, above_zero = above[0]
    if above_position != below_position + 1:
        raise RebindError("target is not bracketed by consecutive zero balls")

    output = copy.deepcopy(block)
    output["target"] = {
        "numerator": str(numerator),
        "denominator": str(denominator),
    }
    output["target_below_local_index"] = below_position
    output["target_above_local_index"] = above_position
    output["target_below_zero_index"] = str(below_zero[0])
    output["target_above_zero_index"] = str(above_zero[0])
    output["derived_target_rebinding"] = {
        "source_zero_block_sha256": canonical_sha(block),
        "source_target": block.get("target"),
        "method": (
            "Exact rational comparison against every preserved indexed "
            "Hardy-zero ball"
        ),
    }
    output["proof_boundary"] = (
        str(block.get("proof_boundary", "")).rstrip()
        + " Target bracketing metadata was deterministically rebound by exact "
        "rational comparison; every zero ball and index is unchanged."
    ).strip()
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("block", type=Path)
    parser.add_argument("--target-numerator", type=int, required=True)
    parser.add_argument("--target-denominator", type=int, default=1 << 32)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = rebind(
            load(args.block), args.target_numerator, args.target_denominator
        )
    except (OSError, json.JSONDecodeError, RebindError) as exc:
        print(json.dumps({"rebound": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "schema": result["schema"],
                "target": result["target"],
                "target_below_zero_index": result["target_below_zero_index"],
                "target_above_zero_index": result["target_above_zero_index"],
                "artifact_sha256": canonical_sha(result),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
