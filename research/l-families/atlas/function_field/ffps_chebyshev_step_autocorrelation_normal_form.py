#!/usr/bin/env python3
"""Bounded replay for Chebyshev-step autocorrelation geometry."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_chebyshev_step_autocorrelation_normal_form.json"

SOURCE_COMMIT = "c223f8fe1b7d89f457db07ce6cc44940fa215aeb"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_SHARP_BV_SAFE_FACTOR_PHASE_DIAGRAM.md": "ae4aed4fa1736633a940f79c0e678f1aabe85d29",
    "research/l-families/atlas/function_field/ffps_sharp_bv_safe_factor_phase_diagram.py": "6e455bc03e264cd429ed12553d4c9e3ec2a993f9",
    "research/l-families/atlas/function_field/ffps_sharp_bv_safe_factor_phase_diagram.json": "ffffe417f2870ca2be7442bd920583441594319d",
    "tests/test_ffps_sharp_bv_safe_factor_phase_diagram.py": "3abfe3d60ac333781f26d9d9c1a3eeefb6bc1f7f",
}

MAX_ORDER = 8


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def validate_order(order: int) -> None:
    if order < 0:
        raise ValueError("order must be nonnegative")


def step_height(order: int) -> int:
    validate_order(order)
    return math.factorial(order) * 4**order


def cell_boundaries(order: int) -> tuple[float, ...]:
    """Ascending endpoints and U_r roots in [0,1]."""
    validate_order(order)
    degree = order + 1
    return tuple(
        (1 - math.cos(index * math.pi / degree)) / 2 for index in range(degree + 1)
    )


def derivative_weights(order: int) -> tuple[int, ...]:
    """Jump weights divided by the signed first-cell height h."""
    validate_order(order)
    return tuple(
        (-1) ** index * (1 if index in (0, order + 1) else 2)
        for index in range(order + 2)
    )


def minimum_cell_width(order: int) -> float:
    validate_order(order)
    return math.sin(math.pi / (2 * (order + 1))) ** 2


def normalized_cusp_slope(order: int) -> int:
    validate_order(order)
    return 2 * order + 1


def curvature_origin_mass(order: int) -> int:
    """Origin mass of -R'' divided by h^2."""
    weights = derivative_weights(order)
    return sum(weight * weight for weight in weights)


def normalized_correlation(order: int, lag: float) -> float:
    """Exact interval-overlap evaluation, divided by h^2."""
    validate_order(order)
    boundaries = cell_boundaries(order)
    total = 0.0
    for left_index in range(order + 1):
        left_a = boundaries[left_index]
        left_b = boundaries[left_index + 1]
        for right_index in range(order + 1):
            right_a = boundaries[right_index] - lag
            right_b = boundaries[right_index + 1] - lag
            overlap = max(0.0, min(left_b, right_b) - max(left_a, right_a))
            total += (-1) ** (left_index + right_index) * overlap
    return total


def normalized_curvature_atoms(order: int) -> tuple[tuple[float, int], ...]:
    """Combined atoms of -R''/h^2, with rounded lag keys."""
    boundaries = cell_boundaries(order)
    weights = derivative_weights(order)
    combined: dict[float, int] = {}
    for left_index, left in enumerate(boundaries):
        for right_index, right in enumerate(boundaries):
            lag = round(right - left, 14)
            combined[lag] = (
                combined.get(lag, 0) + weights[left_index] * weights[right_index]
            )
    return tuple(
        (lag, weight) for lag, weight in sorted(combined.items()) if weight != 0
    )


def local_zero_inside_cusp(order: int) -> bool:
    validate_order(order)
    return 1 / (2 * order + 1) <= minimum_cell_width(order)


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    rows = []
    for order in range(MAX_ORDER + 1):
        delta = minimum_cell_width(order)
        sample_lag = delta / 2
        measured = normalized_correlation(order, sample_lag)
        predicted = 1 - normalized_cusp_slope(order) * sample_lag
        if abs(measured - predicted) > 2e-12:
            raise AssertionError("small-lag cusp replay failed")
        if curvature_origin_mass(order) != 2 * normalized_cusp_slope(order):
            raise AssertionError("curvature origin mass failed")
        curvature = normalized_curvature_atoms(order)
        if sum(weight for _, weight in curvature) != 0:
            raise AssertionError("curvature total mass failed")
        rows.append(
            {
                "information_order": order,
                "step_height_for_b_1": step_height(order),
                "cells": order + 1,
                "minimum_cell_width": f"{delta:.15f}",
                "normalized_cusp_slope": normalized_cusp_slope(order),
                "origin_curvature_mass": curvature_origin_mass(order),
                "distinct_nonzero_curvature_atoms": len(curvature),
                "local_linear_zero_inside_cusp_window": local_zero_inside_cusp(order),
                "half_window_correlation": f"{measured:.15f}",
            }
        )

    return {
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "autocorrelation_normal_form": {
            "kernel": "K_r(t)=(-1)^r*r!*4^r*b*sgn(U_r(2t-1)) on (0,1)",
            "jump_measure": "dK=h*sum_j (-1)^j*c_j*delta_(y_j), c_end=1 and c_interior=2",
            "curvature": "-R''=tilde(dK)*dK",
            "small_lag_law": "R(s)/R(0)=1-(2r+1)|s| for |s|<=sin^2(pi/(2(r+1)))",
            "low_frequency_law": "Khat(xi)=b*(i*xi)^r+O(xi^(r+1)); evenness sharpens Rhat(xi)=b^2*xi^(2r)+O(xi^(2r+2))",
            "resolution_asymptotic": "minimum cell width~pi^2/(4(r+1)^2)",
            "rows": rows,
        },
        "proof_ledger": {
            "finite_atomic_curvature_normal_form": "PROVED",
            "exact_small_lag_cusp": "PROVED",
            "low_frequency_notch_order": "PROVED",
            "high_order_cusp_window_shrinks_quadratically": "PROVED",
            "local_cusp_locates_first_autocorrelation_zero_for_all_r": "REFUTED FOR r>=4",
            "autocorrelation_geometry_improves_beta_cancellation": "NOT PROVED",
            "new_unconditional_beta_estimate": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_information_order": MAX_ORDER,
            "maximum_cells": MAX_ORDER + 1,
            "maximum_raw_curvature_pairs": (MAX_ORDER + 2) ** 2,
            "beta_terms": 0,
            "primes": 0,
            "zeta_zeros": 0,
            "root_searches": 0,
            "random_samples": 0,
            "quadratures": 0,
            "curve_computations": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    payload = run(check_sources=not args.no_source_check)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write_json is not None:
        args.write_json.write_text(text, encoding="utf-8")
    elif args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
            raise RuntimeError(f"canonical fixture mismatch: {OUTPUT}")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
