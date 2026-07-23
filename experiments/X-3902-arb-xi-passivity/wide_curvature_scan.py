#!/usr/bin/env python3
"""Deterministic high-height curvature nomination for later Arb escalation.

This is an EMPIRICAL discovery layer. It invokes the provenance-corrected
moment-FFT curvature program from X-3901 at exact decimal centers, preserves the
full raw JSON for each window, and selects the smallest positive minima without
turning any no-remainder sign into a certificate.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, getcontext
import json
from pathlib import Path
import subprocess
import sys
import time
from typing import Any, Iterable, Sequence

SCHEMA = "riemann.xi-wide-curvature-nomination.v1"
getcontext().prec = 50


def van_der_corput_base2(index: int) -> Decimal:
    if index < 1:
        raise ValueError("index must be positive")
    value = Decimal(0)
    denominator = Decimal(1)
    n = index
    while n:
        n, remainder = divmod(n, 2)
        denominator *= 2
        value += Decimal(remainder) / denominator
    return value


def deterministic_centers(
    count: int,
    *,
    lower: Decimal = Decimal("3000000000000"),
    upper: Decimal = Decimal("5000000000000"),
    decimal_shift: Decimal = Decimal("0.1234"),
) -> tuple[str, ...]:
    if count < 1:
        raise ValueError("count must be positive")
    if not lower < upper:
        raise ValueError("lower must be less than upper")
    span = upper - lower
    return tuple(
        format(lower + span * van_der_corput_base2(index) + decimal_shift, "f")
        for index in range(1, count + 1)
    )


def flatten(value: Any, path: tuple[str, ...] = ()) -> Iterable[tuple[str, Any]]:
    if isinstance(value, dict):
        for key, item in value.items():
            yield from flatten(item, path + (str(key),))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from flatten(item, path + (str(index),))
    else:
        yield ".".join(path), value


def numeric(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return None
    return None


def path_value(value: Any, path: str) -> Any:
    current = value
    for part in path.split("."):
        current = current[int(part)] if isinstance(current, list) else current[part]
    return current


def summarize_window(
    data: dict[str, Any],
    *,
    index: int,
    center: str,
) -> dict[str, Any]:
    negative_fields: list[tuple[str, float]] = []
    curvature_minima: list[tuple[float, str]] = []
    minimum_t_fields: list[tuple[str, float]] = []
    for path, value in flatten(data):
        number = numeric(value)
        if number is None:
            continue
        lower_path = path.lower()
        if "negative" in lower_path:
            negative_fields.append((path, number))
        if ("minimum" in lower_path or "min_" in lower_path) and "curvature" in lower_path:
            curvature_minima.append((number, path))
        if (
            ("minimum" in lower_path or "argmin" in lower_path)
            and (lower_path.endswith(".t") or "ordinate" in lower_path or lower_path.endswith("_t"))
        ):
            minimum_t_fields.append((path, number))

    if not curvature_minima:
        raise ValueError(f"window {index} did not expose a curvature minimum")
    minimum_curvature, minimum_key = min(curvature_minima)

    nominee_t: str | None = None
    nominee_t_key: str | None = None
    for path, number in minimum_t_fields:
        if abs(number - float(center)) > 1000:
            continue
        raw = path_value(data, path)
        nominee_t = str(raw)
        nominee_t_key = path
        break
    if nominee_t is None:
        nominee_t = center
        nominee_t_key = "fallback_center"

    positive_negative_counts = [
        {"path": path, "value": value}
        for path, value in negative_fields
        if value > 0
    ]
    return {
        "window_index": index,
        "center": center,
        "minimum_curvature": minimum_curvature,
        "minimum_curvature_key": minimum_key,
        "nominee_t": nominee_t,
        "nominee_t_key": nominee_t_key,
        "positive_negative_count_fields": positive_negative_counts,
    }


def run_scan(
    *,
    source_script: Path,
    output_directory: Path,
    window_count: int,
    spacing: str,
    points: int,
    order: int,
    nominee_count: int,
) -> dict[str, Any]:
    if not source_script.is_file():
        raise FileNotFoundError(source_script)
    if points < 2 or points & (points - 1):
        raise ValueError("points must be a power of two >= 2")
    if nominee_count < 1 or nominee_count > window_count:
        raise ValueError("invalid nominee_count")

    output_directory.mkdir(parents=True, exist_ok=True)
    centers = deterministic_centers(window_count)
    rows: list[dict[str, Any]] = []
    started = time.time()
    for index, center in enumerate(centers, start=1):
        path = output_directory / f"window-{index:03d}.json"
        command = [
            sys.executable,
            str(source_script),
            "--center",
            center,
            "--spacing",
            spacing,
            "--points",
            str(points),
            "--order",
            str(order),
            "--output",
            str(path),
        ]
        completed = subprocess.run(command, capture_output=True, text=True)
        if completed.returncode:
            raise RuntimeError(
                f"window {index} failed with code {completed.returncode}: "
                f"{completed.stderr[-2000:]}"
            )
        data = json.loads(path.read_text(encoding="utf-8"))
        rows.append(summarize_window(data, index=index, center=center))

    if any(row["positive_negative_count_fields"] for row in rows):
        nomination_status = "NO_REMAINDER_NEGATIVE_SAMPLES_PRESENT"
    else:
        nomination_status = "NO_NEGATIVE_NO_REMAINDER_SAMPLE"

    ordered = sorted(rows, key=lambda row: float(row["minimum_curvature"]))
    unique_nominees: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row in ordered:
        nominee_t = str(row["nominee_t"])
        if nominee_t in seen:
            continue
        seen.add(nominee_t)
        unique_nominees.append(row)
        if len(unique_nominees) == nominee_count:
            break

    return {
        "schema": SCHEMA,
        "status": nomination_status,
        "classification": "EMPIRICAL_DISCOVERY_ONLY",
        "parameters": {
            "lower": "3000000000000",
            "upper": "5000000000000",
            "window_count": window_count,
            "spacing": spacing,
            "points_per_window": points,
            "taylor_order": order,
            "total_samples": window_count * points,
            "nominee_count": nominee_count,
        },
        "elapsed_seconds": time.time() - started,
        "top_nominees": unique_nominees,
        "all_windows": rows,
        "counterexample_candidate": None,
        "warning": (
            "The moment-FFT omits the rigorous final Riemann-Siegel quotient remainder. "
            "Its signs only nominate exact ordinates for subsequent Arb evaluation."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    experiment = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-script",
        type=Path,
        default=experiment.parent / "X-3901-xi-passivity-adversarial" / "nufft_curvature.py",
    )
    parser.add_argument("--window-directory", type=Path, required=True)
    parser.add_argument("--windows", type=int, default=96)
    parser.add_argument("--spacing", default="0.01")
    parser.add_argument("--points", type=int, default=65536)
    parser.add_argument("--order", type=int, default=18)
    parser.add_argument("--nominees", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = run_scan(
        source_script=args.source_script,
        output_directory=args.window_directory,
        window_count=args.windows,
        spacing=args.spacing,
        points=args.points,
        order=args.order,
        nominee_count=args.nominees,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
