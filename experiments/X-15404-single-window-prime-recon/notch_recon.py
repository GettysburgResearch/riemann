#!/usr/bin/env python3
"""Non-directed low-zero notch reconnaissance for the pole-free prime window."""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import mpmath as mp
import numpy as np

from recon import interpolate, prime_power_events


def build_notched_convolution(
    zero_ordinates: list[float],
    notch_count: int,
    fft_size: int,
) -> tuple[np.ndarray, float, float, float]:
    notch_lengths = [2.0 * math.pi / t for t in zero_ordinates[:notch_count]]
    total_box_length = 1.0 + sum(notch_lengths)
    period = 2.0 ** math.ceil(math.log2(max(4.0, 2.0 * total_box_length + 1.0)))
    freq = np.fft.fftfreq(fft_size, d=period / fft_size) * (2.0 * np.pi)
    amplitude = np.ones(fft_size, dtype=np.float64)

    for r in notch_lengths:
        amplitude *= np.sinc((freq * r / 2.0) / np.pi)
    for j in range(1, 64):
        r = 2.0 ** (-j)
        amplitude *= np.sinc((freq * r / 2.0) / np.pi)

    transform = np.exp(-1j * freq * total_box_length) * amplitude * amplitude
    samples = np.fft.ifft((fft_size / period) * transform).real
    return samples, period / fft_size, total_box_length, sum(notch_lengths)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=10_000_000)
    parser.add_argument("--fft-size", type=int, default=1 << 18)
    parser.add_argument("--grid-points", type=int, default=3_000)
    parser.add_argument("--notches", default="0,1,2,5")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    notch_counts = sorted({int(x) for x in args.notches.split(",")})
    if not notch_counts or notch_counts[0] < 0:
        raise SystemExit("notch counts must be nonnegative")

    started = time.time()
    mp.mp.dps = 50
    needed = max(1, max(notch_counts))
    zeros = [float(mp.im(mp.zetazero(j))) for j in range(1, needed + 1)]
    ns, weights, prime_count = prime_power_events(args.cutoff)
    logs = np.log(ns.astype(np.float64))
    h = math.log(4.0)
    x_max = math.log(args.cutoff) + 2.0

    ladders = []
    for notch_count in notch_counts:
        samples, step, total_length, notch_cost = build_notched_convolution(
            zeros, notch_count, args.fft_size
        )

        def density(points: np.ndarray) -> np.ndarray:
            out = np.zeros_like(points, dtype=np.float64)
            mask = (points >= 0.0) & (points <= 2.0 * total_length)
            if np.any(mask):
                out[mask] = interpolate(samples, step, points[mask])
            return out

        def window(points: np.ndarray) -> np.ndarray:
            return density(points - 2.0)

        max_support = 2.0 + 2.0 * total_length + h

        def statistic(x: float) -> tuple[float, int]:
            lo = int(np.searchsorted(logs, x - max_support, side="left"))
            hi = int(np.searchsorted(logs, x - 2.0, side="right"))
            u = x - logs[lo:hi]
            values = window(u) - 2.0 * window(u - h)
            return float(np.dot(weights[lo:hi], values)), hi - lo

        x_min = max(max_support, 14.0)
        grid = np.linspace(x_min, x_max, args.grid_points)
        values = np.asarray([statistic(float(x))[0] for x in grid])
        min_index = int(np.argmin(values))
        max_index = int(np.argmax(values))

        ladders.append(
            {
                "notch_count": notch_count,
                "design_zero_ordinates": zeros[:notch_count],
                "notch_support_cost": notch_cost,
                "profile_box_length": total_length,
                "full_window_support_max": max_support,
                "scan_x_min": x_min,
                "scan_x_max": x_max,
                "minimum": {
                    "x": float(grid[min_index]),
                    "value": float(values[min_index]),
                },
                "maximum": {
                    "x": float(grid[max_index]),
                    "value": float(values[max_index]),
                },
                "empirical_mean_square": float(np.mean(values * values)),
                "empirical_rms": float(np.sqrt(np.mean(values * values))),
                "density_integral": float(np.trapezoid(samples, dx=step)),
            }
        )

    result = {
        "classification": "EMPIRICAL_NON_DIRECTED",
        "cutoff": args.cutoff,
        "ordinary_primes": prime_count,
        "prime_power_terms": int(len(ns)),
        "fft_size": args.fft_size,
        "grid_points_per_ladder": args.grid_points,
        "ladders": ladders,
        "runtime_seconds": time.time() - started,
        "proof_boundary": (
            "notches use mpmath midpoint zeros; FFT/window and prime accumulation "
            "are ordinary floating arithmetic"
        ),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
