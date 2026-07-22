#!/usr/bin/env python3
"""Shardable complete-prime accumulator for the piecewise carrier family D-0801.

The numerical backend is exploratory: phase reduction uses NumPy long double,
transcendental functions and accumulation use ordinary floating point.  Every
shard records an exact contiguous integer interval and whether the separate
higher-prime-power stream was included.  `merge.py` refuses gaps, overlaps, or
missing/duplicated higher powers.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

SCHEMA = "riemann.carrier-piecewise-shard.v1"
TWO_PI_LD = np.longdouble(2) * np.longdouble(np.pi)


def simple_primes(limit: int) -> np.ndarray:
    if limit < 2:
        return np.empty(0, dtype=np.int64)
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    return np.flatnonzero(sieve).astype(np.int64)


def segment_primes(low: int, high: int, base_primes: np.ndarray) -> np.ndarray:
    """Return every prime in the half-open integer interval [low, high)."""
    if not (2 <= low <= high):
        raise ValueError("require 2 <= low <= high")
    mark = np.ones(high - low, dtype=bool)
    root = math.isqrt(max(high - 1, 1))
    for raw in base_primes:
        p = int(raw)
        start = max(p * p, ((low + p - 1) // p) * p)
        if start >= high:
            if p > root:
                break
            continue
        mark[start - low : high - low : p] = False
    return (np.flatnonzero(mark) + low).astype(np.int64)


def higher_prime_powers(cutoff: int, base_primes: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return (q,p) for q=p^a<=cutoff with a>=2, once per prime power."""
    qs: list[int] = []
    ps: list[int] = []
    for raw in base_primes:
        p = int(raw)
        q = p * p
        while q <= cutoff:
            qs.append(q)
            ps.append(p)
            if q > cutoff // p:
                break
            q *= p
    return np.asarray(qs, dtype=np.int64), np.asarray(ps, dtype=np.int64)


def accumulate_terms(
    coefficients: np.ndarray,
    q: np.ndarray,
    p: np.ndarray,
    *,
    cutoff: int,
    carrier: np.longdouble,
) -> None:
    """Accumulate exact hat-cell placement with empirical phase arithmetic."""
    if len(q) == 0:
        return
    if q.shape != p.shape:
        raise ValueError("q and p arrays must have the same shape")
    cells = len(coefficients)
    log_cutoff = np.log(np.longdouble(cutoff))
    q_ld = q.astype(np.longdouble)
    log_q = np.log(q_ld)
    scaled = cells * (log_q / log_cutoff).astype(np.float64)
    lag = np.floor(scaled).astype(np.int64)
    fraction = scaled - lag
    amplitude = (
        np.log(p.astype(np.longdouble))
        / (np.longdouble(np.pi) * np.sqrt(q_ld))
    ).astype(np.float64)
    phase = np.remainder(carrier * log_q, TWO_PI_LD).astype(np.float64)
    real = amplitude * np.cos(phase)
    imag = -amplitude * np.sin(phase)  # exp(-i*T*log(q))

    for target, weight in ((lag, 1.0 - fraction), (lag + 1, fraction)):
        mask = target < cells
        indices = target[mask]
        coefficients.real += np.bincount(
            indices, weights=weight[mask] * real[mask], minlength=cells
        )
        coefficients.imag += np.bincount(
            indices, weights=weight[mask] * imag[mask], minlength=cells
        )


def total_segments(cutoff: int, segment_size: int) -> int:
    if cutoff < 2 or segment_size < 1:
        raise ValueError("cutoff >= 2 and segment_size >= 1 are required")
    return (cutoff - 2) // segment_size + 1


def compute_shard(
    *,
    cutoff: int,
    carrier_text: str,
    cells: int,
    segment_size: int,
    start_segment: int,
    end_segment: int,
    include_higher_powers: bool,
) -> dict[str, Any]:
    if cells < 1:
        raise ValueError("cells must be positive")
    total = total_segments(cutoff, segment_size)
    if not (0 <= start_segment <= end_segment <= total):
        raise ValueError("segment range is outside the complete stream")
    carrier = np.longdouble(carrier_text)
    base = simple_primes(math.isqrt(cutoff))
    coefficients = np.zeros(cells, dtype=np.complex128)
    prime_count = 0

    for segment in range(start_segment, end_segment):
        low = 2 + segment * segment_size
        high = min(cutoff + 1, low + segment_size)
        primes = segment_primes(low, high, base)
        accumulate_terms(
            coefficients, primes, primes, cutoff=cutoff, carrier=carrier
        )
        prime_count += len(primes)

    higher_count = 0
    if include_higher_powers:
        q, p = higher_prime_powers(cutoff, base)
        accumulate_terms(coefficients, q, p, cutoff=cutoff, carrier=carrier)
        higher_count = len(q)

    coverage_low = 2 + start_segment * segment_size
    coverage_high = min(cutoff + 1, 2 + end_segment * segment_size)
    return {
        "schema": SCHEMA,
        "experiment_id": "X-0801",
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "cutoff": cutoff,
            "carrier": carrier_text,
            "cells": cells,
            "segment_size": segment_size,
            "total_segments": total,
            "phase_reduction": "numpy.longdouble product and remainder; float64 sin/cos",
        },
        "segment_range": {"start": start_segment, "end": end_segment},
        "integer_coverage": {"low_inclusive": coverage_low, "high_exclusive": coverage_high},
        "include_higher_prime_powers": include_higher_powers,
        "prime_count": int(prime_count),
        "higher_prime_power_count": int(higher_count),
        "coefficients": {
            "real": coefficients.real.tolist(),
            "imag": coefficients.imag.tolist(),
        },
        "warning": (
            "The stream is complete for its declared shard, but arithmetic is not "
            "directed-rounding interval arithmetic. A negative merged leading value "
            "would be a nomination only."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cutoff", type=int, required=True)
    parser.add_argument("--carrier", required=True)
    parser.add_argument("--cells", type=int, default=1024)
    parser.add_argument("--segment-size", type=int, default=20_000_000)
    parser.add_argument("--start-segment", type=int, default=0)
    parser.add_argument("--end-segment", type=int)
    parser.add_argument("--include-higher-powers", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    total = total_segments(args.cutoff, args.segment_size)
    end = total if args.end_segment is None else args.end_segment
    result = compute_shard(
        cutoff=args.cutoff,
        carrier_text=args.carrier,
        cells=args.cells,
        segment_size=args.segment_size,
        start_segment=args.start_segment,
        end_segment=end,
        include_higher_powers=args.include_higher_powers,
    )
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
