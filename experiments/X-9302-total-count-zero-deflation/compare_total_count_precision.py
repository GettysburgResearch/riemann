#!/usr/bin/env python3
"""Compare two X-9302 nested total-count artifacts exactly."""
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

SCHEMA = "riemann.x9302-pr71-total-count-windows.v1"
COUNT_INTERVAL_CONVENTION = "(T-R,T+R]"


class CompareError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CompareError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return int(value, 10)
    raise CompareError(f"{name} must be an integer")


def binary(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CompareError(f"{name} must be an object")
    m = integer(raw.get("mantissa"), f"{name}.mantissa")
    e = integer(raw.get("exponent"), f"{name}.exponent")
    return Fraction(m << e) if e >= 0 else Fraction(m, 1 << (-e))


def bounds(raw: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(raw, dict):
        raise CompareError(f"{name} must be an object")
    lo = binary(raw.get("lower"), f"{name}.lower")
    hi = binary(raw.get("upper"), f"{name}.upper")
    if lo > hi:
        raise CompareError(f"{name} is reversed")
    return lo, hi


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text())
    if not isinstance(value, dict) or value.get("schema") != SCHEMA:
        raise CompareError(f"{path}: schema mismatch")
    return value


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("low", type=Path)
    parser.add_argument("high", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        low, high = load(args.low), load(args.high)
        for field in ("classification", "target", "count_interval_convention"):
            if low.get(field) != high.get(field):
                raise CompareError(f"{field} mismatch")
        if low.get("count_interval_convention") != COUNT_INTERVAL_CONVENTION:
            raise CompareError("count interval convention mismatch")
        lw, hw = low.get("windows"), high.get("windows")
        if not isinstance(lw, list) or not isinstance(hw, list) or len(lw) != len(hw):
            raise CompareError("window-list mismatch")
        failures = []
        for index, (a, b) in enumerate(zip(lw, hw)):
            for key in ("id", "radius", "N_lower", "N_upper", "count_lower"):
                if a.get(key) != b.get(key):
                    failures.append(
                        {
                            "index": index,
                            "field": key,
                            "low": a.get(key),
                            "high": b.get(key),
                        }
                    )
            for key in ("N_lower_ball", "N_upper_ball"):
                alo, ahi = bounds(a.get(key), f"low[{index}].{key}")
                blo, bhi = bounds(b.get(key), f"high[{index}].{key}")
                if blo < alo or bhi > ahi:
                    failures.append(
                        {
                            "index": index,
                            "field": key,
                            "reason": "higher precision not nested",
                        }
                    )
            for key in ("lower_endpoint", "upper_endpoint"):
                alo, ahi = bounds(a.get(key), f"low[{index}].{key}")
                blo, bhi = bounds(b.get(key), f"high[{index}].{key}")
                if alo != ahi or blo != bhi or alo != blo:
                    failures.append(
                        {
                            "index": index,
                            "field": key,
                            "reason": "exact endpoint mismatch",
                        }
                    )
        result = {
            "schema": "riemann.x9302-total-count-precision-comparison.v1",
            "low_artifact_sha256": canonical_sha(low),
            "high_artifact_sha256": canonical_sha(high),
            "window_count": len(lw),
            "all_stable_and_nested": not failures,
            "failures": failures,
        }
        code = 0 if not failures else 2
    except (OSError, json.JSONDecodeError, CompareError, ValueError) as exc:
        result = {
            "schema": "riemann.x9302-total-count-precision-comparison.v1",
            "verified": False,
            "error": str(exc),
        }
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
