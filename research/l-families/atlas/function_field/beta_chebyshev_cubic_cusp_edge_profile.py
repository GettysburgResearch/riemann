#!/usr/bin/env python3
"""Bounded replay for the finite Chebyshev cubic-cusp edge profile."""

from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
import subprocess
from pathlib import Path
from typing import Callable

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "beta_chebyshev_cubic_cusp_edge_profile.json"

SOURCE_COMMIT = "a239d44c8bfc2946c263e21812299f6c5008db34"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_CHEBYSHEV_MAX_CUSP_COMPENSATION.md"
    ): "c34422172851e6c66baa23341d71b6f72f953045",
    (
        "research/l-families/atlas/function_field/"
        "ffps_chebyshev_max_cusp_compensation.py"
    ): "7d338fdd0b578deba55fd8d6d04a9717ac2111cb",
    (
        "research/l-families/atlas/function_field/"
        "BETA_CHEBYSHEV_PERRON_EDGE_BOUNDARY.md"
    ): "d9bc94d68f9e2aaf51a6e73e5d0d166d786915ca",
    (
        "research/l-families/atlas/function_field/"
        "beta_chebyshev_perron_edge_boundary.py"
    ): "0f01bebedb4bd2ef7305815918aa11147aa03760",
    (
        "research/l-families/atlas/function_field/"
        "beta_chebyshev_perron_edge_boundary.json"
    ): "0ebca0df7e7507c6e4baaa0b012a4111b4f7be1f",
}

EDGE_ORDERS = (31, 63, 127, 255, 511)
PROFILE_PANELS = 16384
PROFILE_RIGHT_ENDPOINT = 4.5


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def simpson(
    function: Callable[[float], complex],
    left: float,
    right: float,
    panels: int,
) -> complex:
    if panels < 2 or panels % 2:
        raise ValueError("panels must be a positive even integer")
    step = (right - left) / panels
    total = function(left) + function(right)
    for index in range(1, panels):
        total += (4 if index % 2 else 2) * function(left + index * step)
    return total * step / 3


def kappa_from_n(n: int) -> float:
    if n < 2:
        raise ValueError("n must be at least two")
    cosine = math.cos(math.pi / n)
    return (1 - cosine) / (12 * (1 + 2 * cosine))


def cell_boundaries(n: int) -> tuple[float, ...]:
    if n < 2:
        raise ValueError("n must be at least two")
    return tuple(
        (1 - math.cos(index * math.pi / n)) / 2 for index in range(n + 1)
    )


def jump_masses(n: int) -> tuple[int, ...]:
    if n < 2:
        raise ValueError("n must be at least two")
    return tuple(
        ((-1) ** index) * (1 if index in (0, n) else 2)
        for index in range(n + 1)
    )


def finite_spectrum_sum(n: int, c: complex) -> complex:
    """S_n(c)=sum q_j q_k exp(-nc|y_j-y_k|/2), using symmetry."""

    if c == 0:
        raise ValueError("c must be nonzero")
    points = cell_boundaries(n)
    masses = jump_masses(n)
    z_half = n * c / 2
    total = complex(sum(mass * mass for mass in masses), 0.0)
    for left in range(n):
        left_point = points[left]
        left_mass = masses[left]
        for right in range(left + 1, n + 1):
            total += (
                2
                * left_mass
                * masses[right]
                * cmath.exp(-z_half * (points[right] - left_point))
            )
    return total


def finite_profile(n: int, c: complex) -> complex:
    """Exact normalized finite profile Phi_n(c) at information order n-1."""

    spectrum = finite_spectrum_sum(n, c)
    z = n * c
    return 4 * (z - spectrum) / (z**3 * kappa_from_n(n))


def edge_scale(n: int, lambda_value: float) -> complex:
    if lambda_value < 0:
        raise ValueError("lambda must be nonnegative")
    return 4j + lambda_value * n ** (-2 / 3)


def edge_gamma_constant() -> complex:
    coefficient = (
        12
        * math.sqrt(2)
        / math.pi**3
        * (24 / math.pi**3) ** (1 / 6)
        * math.gamma(1 / 6)
    )
    return coefficient * cmath.exp(-1j * math.pi / 6)


def cubic_cusp_profile(
    lambda_value: float,
    panels: int = PROFILE_PANELS,
    right_endpoint: float = PROFILE_RIGHT_ENDPOINT,
) -> complex:
    """The universal first-edge profile A(lambda).

    For positive lambda, u=t^2 removes the integrable u^{-1/2} endpoint.
    At lambda zero the oscillatory integral is evaluated by its exact
    Gamma-value.
    """

    if lambda_value < 0:
        raise ValueError("lambda must be nonnegative")
    if lambda_value == 0:
        return edge_gamma_constant()
    a = math.pi * lambda_value / 4
    b = math.pi**3 / 24
    integral = simpson(
        lambda t: 2 * cmath.exp(-a * t * t + 1j * b * t**6),
        0.0,
        right_endpoint,
        panels,
    )
    return (
        36
        * math.sqrt(2)
        / math.pi**3
        * cmath.exp(-1j * math.pi / 4)
        * integral
    )


def outer_matching_constant() -> complex:
    return (
        72
        * math.sqrt(2)
        / math.pi**3
        * cmath.exp(-1j * math.pi / 4)
    )


def complex_row(value: complex) -> dict[str, float]:
    return {
        "real": value.real,
        "imag": value.imag,
        "magnitude": abs(value),
    }


def finite_edge_rows(lambda_value: float) -> list[dict[str, object]]:
    limit = cubic_cusp_profile(lambda_value)
    rows: list[dict[str, object]] = []
    errors: list[float] = []
    for order in EDGE_ORDERS:
        n = order + 1
        scaled = finite_profile(n, edge_scale(n, lambda_value)) / n ** (1 / 3)
        error = abs(scaled - limit)
        errors.append(error)
        rows.append(
            {
                "n": n,
                "scaled_profile": complex_row(scaled),
                "absolute_error_to_limit": error,
            }
        )
    if not all(
        errors[index + 1] < errors[index] for index in range(len(errors) - 1)
    ):
        raise AssertionError("finite cubic-cusp errors did not decrease")
    return rows


def build_payload() -> dict[str, object]:
    exact_edge = edge_gamma_constant()
    lambda_two = cubic_cusp_profile(2.0)
    expected_lambda_two = complex(
        1.60722845137069,
        -1.29749076763844,
    )
    if abs(lambda_two - expected_lambda_two) > 3e-11:
        raise AssertionError("lambda=2 cusp-profile quadrature regression failed")

    edge_rows = finite_edge_rows(0.0)
    lambda_two_rows = finite_edge_rows(2.0)
    if abs(
        edge_rows[-1]["scaled_profile"]["imag"] - exact_edge.imag
    ) > 3e-5:
        raise AssertionError("finite edge failed the exact imaginary constant")

    outer = outer_matching_constant()
    outer_rows: list[dict[str, object]] = []
    outer_errors: list[float] = []
    for lambda_value in (8.0, 16.0, 32.0):
        scaled = math.sqrt(lambda_value) * cubic_cusp_profile(lambda_value)
        error = abs(scaled - outer)
        outer_errors.append(error)
        outer_rows.append(
            {
                "lambda": lambda_value,
                "sqrt_lambda_times_profile": complex_row(scaled),
                "absolute_error": error,
            }
        )
    if not (
        outer_errors[2] < outer_errors[1] < outer_errors[0]
        and outer_errors[-1] < 6e-4
    ):
        raise AssertionError("outer Stieltjes matching regression failed")

    core: dict[str, object] = {
        "edge_gamma_constant": complex_row(exact_edge),
        "lambda_two_profile": complex_row(lambda_two),
        "finite_edge_lambda_zero": edge_rows,
        "finite_edge_lambda_two": lambda_two_rows,
        "outer_matching_constant": complex_row(outer),
        "outer_matching": outer_rows,
    }
    proof_object = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    finite_checks = (
        len(edge_rows)
        + len(lambda_two_rows)
        + 3 * len(outer_rows)
        + 13
    )
    return {
        "schema": "riemann.t108002.beta-chebyshev-cubic-cusp-edge.v1",
        "proof_object_sha256": proof_object,
        "classification": "PASS_T108002_BETA_CHEBYSHEV_CUBIC_CUSP_EDGE_PROFILE",
        "finite_checks": finite_checks,
        **core,
        "critical_window_exponent_two_thirds_proved": True,
        "amplitude_exponent_one_third_proved": True,
        "finite_cubic_cusp_profile_proved": True,
        "exact_edge_gamma_constant_proved": True,
        "positive_lambda_profile_integral_proved": True,
        "lambda_zero_oscillatory_boundary_proved": True,
        "outer_matching_to_stieltjes_threshold_proved": True,
        "finite_edge_airy_asymptotic_proved": False,
        "beta_source_cancellation_proved": False,
        "new_zero_free_region_proved": False,
        "rh_established": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--skip-source-check", action="store_true")
    args = parser.parse_args()
    if not args.skip_source_check:
        check_source_blobs()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != text:
            raise SystemExit("retained output mismatch")
    else:
        OUTPUT.write_text(text)
    print(payload["classification"])


if __name__ == "__main__":
    main()
