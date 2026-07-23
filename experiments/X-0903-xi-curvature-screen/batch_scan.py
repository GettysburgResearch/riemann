#!/usr/bin/env python3
"""Deterministic parallel no-remainder xi-curvature reconnaissance.

The screen is ordinary floating-point discovery arithmetic. It deliberately
omits the Riemann--Siegel remainder and cannot certify a sign.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import json
import random
from pathlib import Path
from typing import Any

from curvature_scan import curvature


def scan(seed: int, count: int, low: int, high: int, workers: int) -> dict[str, Any]:
    if count < 1 or not (0 < workers <= 64) or not (0 < low < high):
        raise ValueError("invalid scan parameters")
    rng = random.Random(seed)
    points = [str(rng.randrange(low, high)) for _ in range(count)]
    rows: list[dict[str, Any]] = []
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(curvature, point): point for point in points}
        for future in as_completed(futures):
            rows.append(future.result())
    for row in rows:
        for key, value in list(row.items()):
            if hasattr(value, "item"):
                row[key] = value.item()
    rows.sort(key=lambda row: row["curvature"])
    return {
        "status": "EMPIRICAL_NO_REMAINDER_NOT_CERTIFIED",
        "seed": seed,
        "range": [low, high],
        "count": len(rows),
        "negative_count": sum(row["curvature"] < 0 for row in rows),
        "minimum_50": rows[:50],
        "warning": (
            "The Riemann--Siegel remainder and all rounding errors are omitted. "
            "A negative is only a nomination; a positive finite scan proves nothing."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--count", type=int, default=1000)
    parser.add_argument("--low", type=int, default=3_000_000_000_000)
    parser.add_argument("--high", type=int, default=10_000_000_000_000)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = scan(args.seed, args.count, args.low, args.high, args.workers)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
