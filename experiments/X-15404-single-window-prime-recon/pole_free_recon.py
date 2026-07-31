#!/usr/bin/env python3
"""Non-directed reconnaissance for the pole-free two-shift prime window."""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import mpmath as mp
import numpy as np

from recon import build_window, interpolate, prime_power_events


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=10_000_000)
    parser.add_argument("--fft-size", type=int, default=1 << 17)
    parser.add_argument("--grid-points", type=int, default=8_000)
    parser.add_argument("--zero-count", type=int, default=50)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    started = time.time()
    window, step = build_window(args.fft_size)
    ns, weights, prime_count = prime_power_events(args.cutoff)
    logs = np.log(ns.astype(np.float64))
    h = math.log(4.0)

    def Fstar(points: np.ndarray) -> np.ndarray:
        out = np.zeros_like(points, dtype=np.float64)
        mask = (points >= 2.0) & (points <= 4.0)
        if np.any(mask):
            out[mask] = interpolate(window, step, points[mask] - 2.0)
        return out

    def statistic(x: float) -> tuple[float, int]:
        lo = int(np.searchsorted(logs, x - (4.0 + h), side="left"))
        hi = int(np.searchsorted(logs, x - 2.0, side="right"))
        u = x - logs[lo:hi]
        values = Fstar(u) - 2.0 * Fstar(u - h)
        return float(np.dot(weights[lo:hi], values)), hi - lo

    mp.mp.dps = 60
    zeros = [float(mp.im(mp.zetazero(j))) for j in range(1, args.zero_count + 1)]

    def base_amplitude(t: float) -> float:
        value = 1.0
        for j in range(1, 64):
            argument = t * (2.0 ** (-j)) / 2.0
            value *= 1.0 if argument == 0.0 else math.sin(argument) / argument
        return value

    zero_array = np.asarray(zeros)
    base_weights = np.asarray([base_amplitude(t) ** 2 for t in zeros])
    pole_free_coefficients = base_weights * (
        1.0 - 2.0 * np.exp(-1j * h * zero_array)
    )

    def zero_prediction(x: float) -> float:
        # Fhat(i gamma)=exp(-3 i gamma)|M(i gamma)|^2.
        return float(
            -2.0
            * np.real(
                np.sum(
                    pole_free_coefficients
                    * np.exp(1j * zero_array * (x - 3.0))
                )
            )
        )

    x_min = 6.0 + h
    x_max = math.log(args.cutoff) + 2.0
    grid = np.linspace(x_min, x_max, args.grid_points)
    values = np.empty_like(grid)
    term_counts = np.empty(args.grid_points, dtype=np.int64)
    for index, x in enumerate(grid):
        values[index], term_counts[index] = statistic(float(x))

    min_index = int(np.argmin(values))
    max_index = int(np.argmax(values))
    empirical_mean_square = float(np.mean(values * values))
    predicted_mean_square = float(
        2.0 * np.sum(np.abs(pole_free_coefficients) ** 2)
    )

    checkpoints = sorted(
        set(
            [
                8.0,
                10.0,
                12.0,
                14.0,
                16.0,
                float(grid[min_index]),
                float(grid[max_index]),
            ]
        )
    )
    comparisons = []
    for x in checkpoints:
        if not (x_min <= x <= x_max):
            continue
        value, count = statistic(x)
        prediction = zero_prediction(x)
        comparisons.append(
            {
                "x": x,
                "prime_power_terms": count,
                "raw_prime_statistic": value,
                "first_n_zero_prediction": prediction,
                "difference": value - prediction,
            }
        )

    result = {
        "classification": "EMPIRICAL_NON_DIRECTED",
        "cutoff": args.cutoff,
        "ordinary_primes": prime_count,
        "prime_power_terms": int(len(ns)),
        "fft_size": args.fft_size,
        "grid_points": args.grid_points,
        "zero_count": args.zero_count,
        "shift_h": h,
        "scan": {
            "x_min": x_min,
            "x_max": x_max,
            "minimum": {"x": float(grid[min_index]), "value": float(values[min_index])},
            "maximum": {"x": float(grid[max_index]), "value": float(values[max_index])},
            "empirical_mean_square": empirical_mean_square,
            "empirical_rms": math.sqrt(empirical_mean_square),
            "first_n_zero_mean_square": predicted_mean_square,
            "first_n_zero_rms": math.sqrt(predicted_mean_square),
        },
        "comparisons": comparisons,
        "runtime_seconds": time.time() - started,
        "proof_boundary": (
            "ordinary FFT/binary64/mpmath reconnaissance; no interval arithmetic, "
            "independent backend, or certified zero/prime manifest"
        ),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
