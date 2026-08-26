#!/usr/bin/env python3
"""Light numerical scout for the fixed-mollified complete beta detector.

This is a finite floating-point experiment, not a theorem producer.
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ANALYTIC_SOURCE_COMMIT = "9f29bdb6ea7375df84de550d62f9d0984634a8dd"
RAW_COMPARATOR_COMMIT = "78e5ce8e75bce174e3014a33b6fe086112577a1e"
SOURCE_BLOBS = {
    ANALYTIC_SOURCE_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_SIGNED_DIFFERENTIAL_ATOMIC_SHELL_FIREWALL.md"
        ): "8dff1025fd7d794497b71c2ba2920a51ff9095f2",
        (
            "research/l-families/atlas/function_field/"
            "FFPS_MOLLIFIED_BETA_RH_EQUIVALENCE.md"
        ): "053c27bac9f8dec63c4865ab3563a7d985de7cbe",
    },
    RAW_COMPARATOR_COMMIT: {
        (
            "research/l-families/atlas/function_field/"
            "FFPS_COMPLETE_BETA_ATOMIC_VARIATION_FIREWALL.md"
        ): "e85848a9a6b24fd4911c2f58d8fb5cb316124d99",
    },
}


def check_source_blobs() -> None:
    for commit, rows in SOURCE_BLOBS.items():
        for path, expected in rows.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def mobius_sieve(limit: int) -> np.ndarray:
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 1 << 18:
        raise ValueError("limit must lie in [1,2^18]")
    mu = np.zeros(limit + 1, dtype=np.int8)
    mu[1] = 1
    primes: list[int] = []
    composite = np.zeros(limit + 1, dtype=np.bool_)
    for value in range(2, limit + 1):
        if not composite[value]:
            primes.append(value)
            mu[value] = -1
        for prime in primes:
            product = value * prime
            if product > limit:
                break
            composite[product] = True
            if value % prime == 0:
                mu[product] = 0
                break
            mu[product] = -mu[value]
    return mu


def beta_array(limit: int) -> np.ndarray:
    mu = mobius_sieve(limit)
    beta = mu.astype(np.int16)
    for value in range(67, limit + 1, 67):
        beta[value] -= int(mu[value // 67])
    return beta


def dyadic_coefficients() -> np.ndarray:
    radical = math.sqrt(2.0)
    return np.array(
        [1.0, -2.0 - 2.0 * radical, 3.0 + 4.0 * radical, -4.0 - 2.0 * radical, 2.0],
        dtype=np.float64,
    )


def mollified_kernel(grid: np.ndarray, epsilon: float) -> np.ndarray:
    """Evaluate eta_epsilon*K_ext in log coordinate."""

    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    log_two = math.log(2.0)
    support = 4.0 * log_two + epsilon
    result = np.zeros_like(grid, dtype=np.float64)
    coefficients = dyadic_coefficients()
    for index, coefficient in enumerate(coefficients):
        start = index * log_two
        offset = grid - start
        atom_mask = (offset >= 0.0) & (offset < epsilon)
        result[atom_mask] += 5.0 * coefficient / epsilon

        ramp_mask = (offset >= 0.0) & (offset < epsilon)
        ramp = offset[ramp_mask]
        result[ramp_mask] += (
            coefficient / epsilon * (3.0 * ramp - 8.0 * (np.exp(ramp / 2.0) - 1.0))
        )

        tail_mask = offset >= epsilon
        tail = offset[tail_mask]
        result[tail_mask] += (
            coefficient
            / epsilon
            * (
                3.0 * epsilon
                - 8.0 * (np.exp(tail / 2.0) - np.exp((tail - epsilon) / 2.0))
            )
        )
    result[(grid < 0.0) | (grid > support)] = 0.0
    return result


def linear_convolution_fft_length(left_length: int, right_length: int) -> int:
    if left_length < 1 or right_length < 1:
        raise ValueError("convolution lengths must be positive")
    output_length = left_length + right_length - 1
    return 1 << (output_length - 1).bit_length()


def fft_convolution(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    output_length = len(left) + len(right) - 1
    fft_length = linear_convolution_fft_length(len(left), len(right))
    transformed = np.fft.rfft(left, fft_length) * np.fft.rfft(right, fft_length)
    return np.fft.irfft(transformed, fft_length)[:output_length]


def run_panel(max_power: int, cells_per_log_two: int) -> dict[str, object]:
    if (
        isinstance(max_power, bool)
        or not isinstance(max_power, int)
        or not 8 <= max_power <= 18
    ):
        raise ValueError("max_power must lie in [8,18]")
    if isinstance(cells_per_log_two, bool) or cells_per_log_two not in (
        128,
        256,
        512,
        1024,
    ):
        raise ValueError("unsupported grid resolution")
    limit = 1 << max_power
    log_two = math.log(2.0)
    epsilon = log_two / 2.0
    step = log_two / cells_per_log_two
    support = 4.0 * log_two + epsilon
    source_cells = max_power * cells_per_log_two
    kernel_cells = math.ceil(support / step)

    beta = beta_array(limit)
    odd_weighted_prefix = np.zeros(limit + 1, dtype=np.float64)
    running = 0.0
    for value in range(1, limit + 1):
        if value % 2:
            running += abs(int(beta[value])) / math.sqrt(value)
        odd_weighted_prefix[value] = running
    source = np.zeros(source_cells, dtype=np.float64)
    for value in range(1, limit + 1):
        coefficient = int(beta[value])
        if coefficient:
            index = round(math.log(value) / step)
            if index < source_cells:
                source[index] += coefficient / math.sqrt(value)

    # Midpoint sampling avoids assigning half of every rectangular atom twice.
    # The chosen epsilon and all dyadic knots are exact grid multiples.
    kernel_grid = (np.arange(kernel_cells, dtype=np.float64) + 0.5) * step
    kernel = mollified_kernel(kernel_grid, epsilon)
    detector = fft_convolution(source, kernel)[:source_cells]

    rows = []
    for power in range(6, max_power + 1):
        endpoint = power * cells_per_log_two
        values = detector[:endpoint]
        negative_mass = float(step * np.sum(np.maximum(-values, 0.0)))
        absolute_mass = float(step * np.sum(np.abs(values)))
        raw_root_limit = (1 << power) // 32
        raw_atomic_lower_bound = (50.0 + 35.0 * math.sqrt(2.0)) * float(
            odd_weighted_prefix[raw_root_limit]
        )
        rows.append(
            {
                "power": power,
                "Y": 1 << power,
                "negative_mass": negative_mass,
                "absolute_mass": absolute_mass,
                "raw_root_limit": raw_root_limit,
                "raw_atomic_lower_bound": raw_atomic_lower_bound,
                "mollified_to_raw_lower_ratio": (
                    negative_mass / raw_atomic_lower_bound
                ),
                "effective_negative_exponent": (
                    math.log(max(negative_mass, 1.0e-300)) / (power * log_two)
                ),
            }
        )

    return {
        "max_power": max_power,
        "cells_per_log_two": cells_per_log_two,
        "epsilon_over_log_two": 0.5,
        "source_limit": limit,
        "source_nonzero_terms": int(np.count_nonzero(beta[1:])),
        "grid_cells": source_cells,
        "kernel_cells": kernel_cells,
        "kernel_integral_midpoint": float(step * np.sum(kernel)),
        "rows": rows,
    }


def linear_fit(
    rows: list[dict[str, object]], key: str, minimum_power: int
) -> dict[str, float | int]:
    selected = [row for row in rows if int(row["power"]) >= minimum_power]
    if len(selected) < 2:
        raise ValueError("linear fit requires at least two selected rows")
    x_values = np.array([float(row["power"]) for row in selected])
    y_values = np.array([float(row[key]) for row in selected])
    x_mean = float(np.mean(x_values))
    y_mean = float(np.mean(y_values))
    slope = float(
        np.sum((x_values - x_mean) * (y_values - y_mean))
        / np.sum((x_values - x_mean) ** 2)
    )
    intercept = y_mean - slope * x_mean
    residual = y_values - (slope * x_values + intercept)
    return {
        "minimum_power": minimum_power,
        "row_count": len(selected),
        "slope_per_doubling": slope,
        "intercept": intercept,
        "maximum_absolute_residual": float(np.max(np.abs(residual))),
    }


def run(max_power: int = 18) -> dict[str, object]:
    if (
        isinstance(max_power, bool)
        or not isinstance(max_power, int)
        or not 11 <= max_power <= 18
    ):
        raise ValueError("scout fit requires max_power in [11,18]")
    panels = [run_panel(max_power, resolution) for resolution in (256, 512)]
    coarse = panels[0]["rows"]
    fine = panels[1]["rows"]
    comparisons = []
    for left, right in zip(coarse, fine, strict=True):
        comparisons.append(
            {
                "power": left["power"],
                "negative_relative_difference": abs(
                    left["negative_mass"] - right["negative_mass"]
                )
                / max(abs(right["negative_mass"]), 1.0e-300),
                "absolute_relative_difference": abs(
                    left["absolute_mass"] - right["absolute_mass"]
                )
                / max(abs(right["absolute_mass"]), 1.0e-300),
            }
        )
    return {
        "frozen_sources": SOURCE_BLOBS,
        "status": "finite floating-point scout; no asymptotic or RH inference",
        "kernel": (
            "eta_(log(2)/2) convolved with the exact inverse-Mellin "
            "finite-difference formula for K_ext"
        ),
        "panels": panels,
        "resolution_comparison": comparisons,
        "fine_panel_linear_scout": {
            "negative_mass": linear_fit(fine, "negative_mass", 10),
            "absolute_mass": linear_fit(fine, "absolute_mass", 10),
            "interpretation": (
                "a finite-window linear fit in log_2(Y), not an asymptotic claim"
            ),
        },
        "resource_caps": {
            "maximum_source_limit": 1 << 18,
            "panel_count": len(panels),
            "resolutions": [256, 512],
            "maximum_source_grid_cells": max(
                int(panel["grid_cells"]) for panel in panels
            ),
            "maximum_kernel_grid_cells": max(
                int(panel["kernel_cells"]) for panel in panels
            ),
            "maximum_linear_convolution_cells": max(
                int(panel["grid_cells"]) + int(panel["kernel_cells"]) - 1
                for panel in panels
            ),
            "maximum_fft_length": max(
                linear_convolution_fft_length(
                    int(panel["grid_cells"]), int(panel["kernel_cells"])
                )
                for panel in panels
            ),
            "horizons_per_panel": max_power - 5,
            "curve_enumerations": 0,
            "conductor_enumerations": 0,
            "zero_searches": 0,
        },
    }


def rounded_summary(max_power: int = 18) -> dict[str, object]:
    if max_power != 18:
        raise ValueError("canonical rounded summary requires max_power=18")
    result = run(max_power)
    fine_panel = result["panels"][1]
    rows = {int(row["power"]): row for row in fine_panel["rows"]}

    def rounded(value: object) -> object:
        return round(value, 9) if isinstance(value, float) else value

    checkpoints = []
    for power in (10, 14, 18):
        row = rows[power]
        checkpoints.append(
            {
                key: rounded(row[key])
                for key in (
                    "power",
                    "Y",
                    "negative_mass",
                    "absolute_mass",
                    "raw_root_limit",
                    "raw_atomic_lower_bound",
                    "mollified_to_raw_lower_ratio",
                )
            }
        )
    fits = result["fine_panel_linear_scout"]
    return {
        "schema": "riemann.function_field.ffps_mollified_beta_finite_scout.v1",
        "status": result["status"],
        "frozen_sources": result["frozen_sources"],
        "parameters": {
            "max_power": max_power,
            "epsilon_over_log_two": 0.5,
            "coarse_cells_per_log_two": 256,
            "fine_cells_per_log_two": 512,
        },
        "kernel_zero_mass_controls": [
            rounded(panel["kernel_integral_midpoint"]) for panel in result["panels"]
        ],
        "checkpoints": checkpoints,
        "grid_semantics": {
            "source_placement": "log(n) rounded to the nearest log-grid node",
            "detector_samples": "midpoints of output log cells",
            "mass_quadrature": "midpoint rule with one factor of the log step",
            "raw_comparator": "exact at Y, with complete odd groups m<=floor(Y/32)",
        },
        "fine_window_linear_fits": {
            key: {name: rounded(value) for name, value in fits[key].items()}
            for key in ("negative_mass", "absolute_mass")
        },
        "maximum_resolution_relative_difference": rounded(
            max(
                max(
                    row["negative_relative_difference"],
                    row["absolute_relative_difference"],
                )
                for row in result["resolution_comparison"]
            )
        ),
        "final_resolution_relative_difference": {
            key: rounded(result["resolution_comparison"][-1][key])
            for key in (
                "negative_relative_difference",
                "absolute_relative_difference",
            )
        },
        "interpretation": (
            "finite data through 2^18 suggest roughly linear growth in log(Y); "
            "this is not an asymptotic or RH inference"
        ),
        "resource_caps": result["resource_caps"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-power", type=int, default=18)
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        check_source_blobs()
    output = (
        rounded_summary(args.max_power)
        if args.summary or args.check
        else run(args.max_power)
    )
    rendered = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.check:
        canonical = Path(__file__).with_suffix(".json")
        if not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered:
            raise SystemExit("canonical JSON fixture is stale")
    print(rendered, end="")


if __name__ == "__main__":
    main()
