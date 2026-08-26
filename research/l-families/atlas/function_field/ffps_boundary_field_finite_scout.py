#!/usr/bin/env python3
"""Bounded floating-point scout for the compact beta boundary field G."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import subprocess
from pathlib import Path
from types import ModuleType

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCOUT_COMMIT = "928cf3f3da653ff9608adfe6c050e0578e249350"
BOUNDARY_COMMIT = "9e19e27614e473b3b7d06cfc3d51f92eb39ff009"
SOURCE_BLOBS = {
    SCOUT_COMMIT: {
        "research/l-families/atlas/function_field/FFPS_MOLLIFIED_BETA_FINITE_SCOUT.md": "e3235e9a24b21b11f852587e2a31fbb617b1763a",
        "research/l-families/atlas/function_field/ffps_mollified_beta_finite_scout.py": "3ef4973fb46630c9068d364dd108d05b3c4b8aed",
        "research/l-families/atlas/function_field/ffps_mollified_beta_finite_scout.json": "79e00d6cdf527ddd02fde26603d4554f48fb04f0",
        "tests/test_ffps_mollified_beta_finite_scout.py": "92f09e8bd6b5dcb7f9197e244a31b01b8f2b324d",
    },
    BOUNDARY_COMMIT: {
        "research/l-families/atlas/function_field/FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md": "bf4d1baa231086ba7e8eafaecd39730d83c9201a",
        "research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.py": "2180038eef7ab639477879e806bb13fdbea0b1ec",
        "research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.json": "c86a40d6a930603b3897ad12a28acc5f21e80dd6",
        "tests/test_ffps_mollified_beta_boundary_shell_identity.py": "5e7de97284878c6f9b5a5ac43b83ccaf9528e242",
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
    imported_path = (
        "research/l-families/atlas/function_field/ffps_mollified_beta_finite_scout.py"
    )
    current = subprocess.run(
        ["git", "hash-object", f"--path={imported_path}", imported_path],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=2,
    )
    if current.stdout.strip() != SOURCE_BLOBS[SCOUT_COMMIT][imported_path]:
        raise RuntimeError("current imported finite-scout implementation drifted")


def load_mollified_scout() -> ModuleType:
    path = HERE / "ffps_mollified_beta_finite_scout.py"
    spec = importlib.util.spec_from_file_location("mollified_beta_scout", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load the frozen finite-scout implementation")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def boundary_kernel(grid: np.ndarray) -> np.ndarray:
    """Evaluate the compact causal primitive K_bd on a log grid."""

    if grid.ndim != 1:
        raise ValueError("grid must be one-dimensional")
    scout = load_mollified_scout()
    log_two = math.log(2.0)
    support = 4.0 * log_two
    result = np.zeros_like(grid, dtype=np.float64)
    for index, coefficient in enumerate(scout.dyadic_coefficients()):
        offset = grid - index * log_two
        mask = offset >= 0.0
        positive = offset[mask]
        result[mask] += coefficient * (
            13.0 + 3.0 * positive - 8.0 * np.exp(positive / 2.0)
        )
    result[(grid < 0.0) | (grid > support)] = 0.0
    return result


def _panel_arrays(
    max_power: int, cells_per_log_two: int
) -> tuple[np.ndarray, np.ndarray, float, dict[str, int]]:
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

    scout = load_mollified_scout()
    limit = 1 << max_power
    log_two = math.log(2.0)
    step = log_two / cells_per_log_two
    source_cells = max_power * cells_per_log_two
    kernel_cells = 4 * cells_per_log_two
    beta = scout.beta_array(limit)
    source = np.zeros(source_cells, dtype=np.float64)
    for value in range(1, limit + 1):
        coefficient = int(beta[value])
        if coefficient:
            index = round(math.log(value) / step)
            if index < source_cells:
                source[index] += coefficient / math.sqrt(value)

    kernel_grid = (np.arange(kernel_cells, dtype=np.float64) + 0.5) * step
    kernel = boundary_kernel(kernel_grid)
    boundary = scout.fft_convolution(source, kernel)[:source_cells]
    metadata = {
        "source_limit": limit,
        "source_nonzero_terms": int(np.count_nonzero(beta[1:])),
        "source_cells": source_cells,
        "kernel_cells": kernel_cells,
        "fft_length": scout.linear_convolution_fft_length(source_cells, kernel_cells),
    }
    return boundary, source, step, metadata


def run_panel(max_power: int, cells_per_log_two: int) -> dict[str, object]:
    boundary, _, step, metadata = _panel_arrays(max_power, cells_per_log_two)
    rows = []
    for power in range(6, max_power + 1):
        values = boundary[: power * cells_per_log_two]
        negative_mass = float(step * np.sum(np.maximum(-values, 0.0)))
        absolute_mass = float(step * np.sum(np.abs(values)))
        signed_mass = float(step * np.sum(values))
        rows.append(
            {
                "power": power,
                "Y": 1 << power,
                "negative_mass": negative_mass,
                "absolute_mass": absolute_mass,
                "signed_mass": signed_mass,
                "jordan_residual": absolute_mass - 2.0 * negative_mass,
            }
        )
    return {
        "max_power": max_power,
        "cells_per_log_two": cells_per_log_two,
        **metadata,
        "rows": rows,
    }


def first_difference_control(
    max_power: int, cells_per_log_two: int
) -> dict[str, float]:
    scout = load_mollified_scout()
    boundary, source, step, _ = _panel_arrays(max_power, cells_per_log_two)
    log_two = math.log(2.0)
    epsilon = log_two / 2.0
    shift = cells_per_log_two // 2
    translated = np.zeros_like(boundary)
    translated[shift:] = boundary[:-shift]
    from_boundary = (boundary - translated) / epsilon

    support = 4.0 * log_two + epsilon
    kernel_cells = math.ceil(support / step)
    grid = (np.arange(kernel_cells, dtype=np.float64) + 0.5) * step
    mollified_kernel = scout.mollified_kernel(grid, epsilon)
    direct = scout.fft_convolution(source, mollified_kernel)[: len(boundary)]
    maximum_absolute = float(np.max(np.abs(direct - from_boundary)))
    maximum_relative = maximum_absolute / max(float(np.max(np.abs(direct))), 1.0)
    return {
        "maximum_absolute_difference": maximum_absolute,
        "maximum_relative_difference": maximum_relative,
    }


def linear_fit(
    rows: list[dict[str, object]], key: str, minimum_power: int = 10
) -> dict[str, float | int]:
    selected = [row for row in rows if int(row["power"]) >= minimum_power]
    if len(selected) < 2:
        raise ValueError("linear fit requires at least two selected rows")
    x_values = np.array([float(row["power"]) for row in selected])
    y_values = np.array([float(row[key]) for row in selected])
    slope, intercept = np.polyfit(x_values, y_values, 1)
    residuals = y_values - (slope * x_values + intercept)
    return {
        "minimum_power": minimum_power,
        "row_count": len(selected),
        "slope_per_doubling": float(slope),
        "intercept": float(intercept),
        "maximum_absolute_residual": float(np.max(np.abs(residuals))),
    }


def run(max_power: int = 18) -> dict[str, object]:
    if (
        isinstance(max_power, bool)
        or not isinstance(max_power, int)
        or not 11 <= max_power <= 18
    ):
        raise ValueError("scout fit requires max_power in [11,18]")
    panels = [run_panel(max_power, resolution) for resolution in (256, 512)]
    comparisons = []
    for coarse, fine in zip(panels[0]["rows"], panels[1]["rows"], strict=True):
        comparisons.append(
            {
                "power": coarse["power"],
                "negative_relative_difference": abs(
                    coarse["negative_mass"] - fine["negative_mass"]
                )
                / max(abs(fine["negative_mass"]), 1.0e-300),
                "absolute_relative_difference": abs(
                    coarse["absolute_mass"] - fine["absolute_mass"]
                )
                / max(abs(fine["absolute_mass"]), 1.0e-300),
            }
        )
    fine_rows = panels[1]["rows"]
    first_difference = first_difference_control(max_power, 512)
    source_construction_passes = len(panels) + 1
    fine_resolution = int(panels[1]["cells_per_log_two"])
    validation_kernel_cells = 9 * fine_resolution // 2
    maximum_linear_convolution_cells = max(
        max(
            int(panel["source_cells"]) + int(panel["kernel_cells"]) - 1
            for panel in panels
        ),
        int(panels[1]["source_cells"]) + validation_kernel_cells - 1,
    )
    return {
        "frozen_sources": SOURCE_BLOBS,
        "status": "finite floating-point scout; no asymptotic or RH inference",
        "field": "G=sum beta(n)/sqrt(n)*K_bd(t-log(n))",
        "panels": panels,
        "resolution_comparison": comparisons,
        "first_difference_control": first_difference,
        "fine_panel_linear_scout": {
            "negative_mass": linear_fit(fine_rows, "negative_mass"),
            "absolute_mass": linear_fit(fine_rows, "absolute_mass"),
            "interpretation": "finite-window linear fits in log_2(Y) only",
        },
        "resource_caps": {
            "maximum_source_limit": 1 << 18,
            "source_construction_passes": source_construction_passes,
            "maximum_source_placement_visits": (source_construction_passes * (1 << 18)),
            "panel_count": len(panels),
            "resolutions": [256, 512],
            "horizons_per_panel": max_power - 5,
            "maximum_source_grid_cells": max(
                int(panel["source_cells"]) for panel in panels
            ),
            "maximum_boundary_kernel_grid_cells": max(
                int(panel["kernel_cells"]) for panel in panels
            ),
            "maximum_validation_kernel_grid_cells": validation_kernel_cells,
            "maximum_linear_convolution_cells": maximum_linear_convolution_cells,
            "boundary_fft_convolutions": 3,
            "mollified_validation_convolutions": 1,
            "maximum_fft_length": 1
            << (maximum_linear_convolution_cells - 1).bit_length(),
            "curve_enumerations": 0,
            "conductor_enumerations": 0,
            "zero_searches": 0,
        },
    }


def rounded_summary(max_power: int = 18) -> dict[str, object]:
    if max_power != 18:
        raise ValueError("canonical summary is frozen at max_power=18")
    result = run(max_power)
    fine = {int(row["power"]): row for row in result["panels"][1]["rows"]}

    def rounded(value: object) -> object:
        return round(value, 9) if isinstance(value, float) else value

    checkpoints = []
    for power in (10, 14, 18):
        row = fine[power]
        checkpoints.append(
            {
                key: rounded(row[key])
                for key in (
                    "power",
                    "Y",
                    "negative_mass",
                    "absolute_mass",
                    "signed_mass",
                    "jordan_residual",
                )
            }
        )
    return {
        "schema": "riemann.function_field.ffps_boundary_field_finite_scout.v1",
        "status": result["status"],
        "frozen_sources": result["frozen_sources"],
        "parameters": {
            "max_power": 18,
            "coarse_cells_per_log_two": 256,
            "fine_cells_per_log_two": 512,
        },
        "checkpoints": checkpoints,
        "fine_window_linear_fits": {
            key: {
                name: rounded(value)
                for name, value in result["fine_panel_linear_scout"][key].items()
            }
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
        "first_difference_control": {
            key: round(value, 15)
            for key, value in result["first_difference_control"].items()
        },
        "interpretation": (
            "finite data suggest roughly linear boundary-field variation in "
            "log(Y); this is not an asymptotic or RH inference"
        ),
        "resource_caps": result["resource_caps"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-power", type=int, default=18)
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    if args.check:
        check_source_blobs()
    output = (
        rounded_summary(args.max_power)
        if args.summary or args.check or args.write_json
        else run(args.max_power)
    )
    rendered = json.dumps(output, indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
