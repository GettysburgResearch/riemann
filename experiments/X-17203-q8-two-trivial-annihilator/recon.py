#!/usr/bin/env python3
"""NON_DIRECTED floating reconnaissance for Q_G8 near x=18.

The prime-power manifest is complete, but the spline is reconstructed by a
complex128 FFT and linearly interpolated.  Four shifted raw sums then cancel
by many orders of magnitude.  Nothing emitted by this script is a proof or an
interval enclosure.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np


HERE = Path(__file__).resolve().parent
BASE_EXPERIMENT = HERE.parent / "X-17202-rational-ten-notch-moat"
SEARCH_EXPERIMENT = HERE.parent / "X-17201-directed-notch-negative"
sys.path.insert(0, str(SEARCH_EXPERIMENT))

from filter_core import FilterSpec  # noqa: E402
from search import build_density, make_window, prime_power_arrays  # noqa: E402


def q(value: str) -> Fraction:
    return Fraction(value)


def scan(
    *,
    cutoff: int,
    fft_size: int,
    grid: np.ndarray,
    ns: np.ndarray,
    weights: np.ndarray,
    widths: tuple[Fraction, ...],
) -> dict[str, Any]:
    spec = FilterSpec(widths=widths, base_shift=Fraction(2))
    samples, step, density_support = build_density(spec, fft_size)
    base_window = make_window(spec, samples, step, density_support)
    logs = np.log(ns.astype(np.float64))
    log2 = math.log(2.0)
    a1 = (6.0 / 5.0) * log2
    a2 = (2.0 / 3.0) * log2
    support_lo = 2.0
    support_hi = 2.0 + density_support + 2.0 * log2 + a1 + a2
    values = np.empty(len(grid), dtype=np.float64)
    components = np.empty((len(grid), 4), dtype=np.float64)
    counts = np.empty(len(grid), dtype=np.int64)

    for index, x in enumerate(grid):
        lo = int(np.searchsorted(logs, x - support_hi, side="left"))
        hi = int(np.searchsorted(logs, x - support_lo, side="right"))
        u = x - logs[lo:hi]
        local_weights = weights[lo:hi]
        c0 = float(np.dot(local_weights, base_window(u)))
        c1 = float(np.dot(local_weights, base_window(u - a1)))
        c2 = float(np.dot(local_weights, base_window(u - a2)))
        c12 = float(np.dot(local_weights, base_window(u - a1 - a2)))
        components[index] = (c0, c1, c2, c12)
        values[index] = c0 - c1 / 8.0 - c2 / 8.0 + c12 / 64.0
        counts[index] = hi - lo

    abs_index = int(np.argmax(np.abs(values)))
    component_abs_sum = float(
        abs(components[abs_index, 0])
        + abs(components[abs_index, 1]) / 8.0
        + abs(components[abs_index, 2]) / 8.0
        + abs(components[abs_index, 3]) / 64.0
    )
    return {
        "fft_size": fft_size,
        "fft_step": step,
        "density_integral": float(np.trapezoid(samples, dx=step)),
        "density_minimum": float(samples.min()),
        "density_maximum": float(samples.max()),
        "support_hi_float": support_hi,
        "prime_terms_min": int(counts.min()),
        "prime_terms_max": int(counts.max()),
        "minimum": {
            "x": float(grid[int(np.argmin(values))]),
            "value": float(values.min()),
        },
        "maximum": {
            "x": float(grid[int(np.argmax(values))]),
            "value": float(values.max()),
        },
        "largest_abs": {
            "x": float(grid[abs_index]),
            "value": float(values[abs_index]),
            "four_term_component_abs_sum": component_abs_sum,
            "component_abs_sum_over_abs_combination": (
                component_abs_sum / abs(float(values[abs_index]))
                if values[abs_index] != 0.0
                else math.inf
            ),
            "raw_components": [float(v) for v in components[abs_index]],
        },
        "values": values,
    }


def contiguous_runs(mask: np.ndarray) -> list[tuple[int, int]]:
    changes = np.diff(np.concatenate(([False], mask, [False])).astype(np.int8))
    starts = np.nonzero(changes == 1)[0]
    ends = np.nonzero(changes == -1)[0] - 1
    return list(zip(starts.tolist(), ends.tolist()))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=10_000_000)
    parser.add_argument("--grid-points", type=int, default=65)
    parser.add_argument("--fft-sizes", default="262144,1048576")
    parser.add_argument("--x-min", type=float, default=18.0)
    parser.add_argument("--x-max", type=float, default=18.12)
    args = parser.parse_args()
    if args.cutoff < 100 or args.grid_points < 3:
        raise SystemExit("invalid reconnaissance parameters")

    base_cert = json.loads((BASE_EXPERIMENT / "certificate.json").read_text(encoding="utf-8"))
    widths = tuple(Fraction(text) for text in base_cert["filter"]["dyadic_widths"])
    widths += tuple(q(row["width"]) for row in base_cert["filter"]["notches"])
    fft_sizes = [int(text) for text in args.fft_sizes.split(",")]
    if len(fft_sizes) != 2 or fft_sizes[0] >= fft_sizes[1]:
        raise SystemExit("provide exactly two increasing FFT sizes")

    complete_x_max = math.log(args.cutoff) + 2.0
    x_max = min(args.x_max, complete_x_max)
    if args.x_min >= x_max:
        raise SystemExit("cutoff does not cover the requested x interval")
    grid = np.linspace(args.x_min, x_max, args.grid_points)

    started = time.time()
    ns, weights, manifest = prime_power_arrays(args.cutoff)
    scans = [
        scan(
            cutoff=args.cutoff,
            fft_size=size,
            grid=grid,
            ns=ns,
            weights=weights,
            widths=widths,
        )
        for size in fft_sizes
    ]
    coarse_values = scans[0].pop("values")
    fine_values = scans[1].pop("values")
    discrepancy = np.abs(fine_values - coarse_values)
    scale = np.minimum(np.abs(fine_values), np.abs(coarse_values))
    same_sign = np.signbit(fine_values) == np.signbit(coarse_values)
    stable = same_sign & (scale > 6e-18) & (discrepancy < 0.1 * scale)
    candidates: list[dict[str, Any]] = []
    for sign in (1, -1):
        signed = stable & (sign * fine_values > 0.0)
        for left, right in contiguous_runs(signed):
            candidates.append(
                {
                    "sign": sign,
                    "sampled_grid_interval": [float(grid[left]), float(grid[right])],
                    "sample_count": right - left + 1,
                    "fine_sampled_inf_abs_Q": float(
                        np.min(np.abs(fine_values[left : right + 1]))
                    ),
                    "max_cross_resolution_discrepancy": float(
                        np.max(discrepancy[left : right + 1])
                    ),
                    "warning": "NON_DIRECTED sampled points only; not an interval enclosure",
                }
            )

    output = {
        "classification": "NON_DIRECTED_FLOATING_RECONNAISSANCE",
        "filter": "L-17202 q=8 two-trivial-annihilator applied to L-17201 G_0",
        "declared_rh_tail_moat": 6e-18,
        "scan": {
            "requested_x_interval": [args.x_min, args.x_max],
            "complete_manifest_x_interval": [float(grid[0]), float(grid[-1])],
            "grid_points": len(grid),
            "maximum_cross_resolution_discrepancy": float(discrepancy.max()),
            "median_cross_resolution_discrepancy": float(np.median(discrepancy)),
            "stable_sampled_exceedance_runs": candidates,
        },
        "resolutions": scans,
        "manifest": manifest,
        "runtime_seconds": time.time() - started,
        "precision_warning": (
            "The manifest is complete, but density inversion and interpolation use complex128/float64. "
            "Q_G8 is a four-term cancellation. Cross-resolution agreement is only an error heuristic, "
            "not a directed enclosure; no run is an RH certificate."
        ),
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
