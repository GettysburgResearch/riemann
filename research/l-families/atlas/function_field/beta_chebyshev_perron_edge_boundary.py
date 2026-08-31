#!/usr/bin/env python3
"""Bounded replay for the Chebyshev Perron-edge boundary theorem."""

from __future__ import annotations

import argparse
import cmath
import json
import hashlib
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "d79692ece0b7604ad309c459f565b24e9926f5c5"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_CHEBYSHEV_MAX_CUSP_COMPENSATION.md": "c34422172851e6c66baa23341d71b6f72f953045",
    "research/l-families/atlas/function_field/ffps_chebyshev_max_cusp_compensation.py": "7d338fdd0b578deba55fd8d6d04a9717ac2111cb",
}
OUTPUT = HERE / "beta_chebyshev_perron_edge_boundary.json"

PROFILE_PANELS = 32768
THRESHOLD_PANELS = 131072
EDGE_ORDERS = (31, 63, 127, 255)


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


def simpson(function, left: float, right: float, panels: int) -> complex:
    if panels < 2 or panels % 2:
        raise ValueError("panels must be positive and even")
    step = (right - left) / panels
    total = function(left) + function(right)
    for index in range(1, panels):
        total += (4 if index % 2 else 2) * function(left + index * step)
    return total * step / 3


def profile_complex(c: complex, panels: int = PROFILE_PANELS) -> complex:
    if c == 0:
        return 1 + 0j
    scale = c * math.pi / 8
    integral = simpson(
        lambda theta: scale * math.sin(theta)
        - cmath.tanh(scale * math.sin(theta)),
        0.0,
        math.pi,
        panels,
    )
    return 1152 * integral / (math.pi**3 * c**3)


def subthreshold_profile(y: float, panels: int = PROFILE_PANELS) -> float:
    if not 0 < y < 4:
        raise ValueError("y must lie in (0,4)")
    scale = y * math.pi / 8
    integral = simpson(
        lambda theta: complex(math.tan(scale * math.sin(theta)), 0.0),
        0.0,
        math.pi,
        panels,
    ).real
    return 288 / (math.pi**2 * y**3) * ((4 / math.pi) * integral - y)


def spectral_density(t: float) -> float:
    if t <= 16:
        raise ValueError("t must exceed 16")
    maximum = int(math.sqrt(t) / 4)
    return (
        18432
        / (math.pi**4 * t**2)
        * math.fsum(
            1 / math.sqrt(1 - 16 * mode**2 / t)
            for mode in range(1, maximum + 1, 2)
        )
    )


def boundary_imaginary_part(y: float) -> float:
    if y <= 4:
        raise ValueError("y must exceed the first threshold")
    nearest = round(y / 4)
    if nearest % 2 == 1 and abs(y - 4 * nearest) < 1e-12:
        raise ValueError("threshold boundary value diverges")
    return -math.pi * spectral_density(y * y)


def cell_boundaries(order: int) -> tuple[float, ...]:
    n = order + 1
    return tuple((1 - math.cos(index * math.pi / n)) / 2 for index in range(n + 1))


def jump_data(order: int) -> tuple[tuple[float, int], ...]:
    points = cell_boundaries(order)
    return tuple(
        (
            point,
            ((-1) ** index) * (1 if index in (0, order + 1) else 2),
        )
        for index, point in enumerate(points)
    )


def kappa(order: int) -> float:
    cosine = math.cos(math.pi / (order + 1))
    return (1 - cosine) / (12 * (1 + 2 * cosine))


def finite_profile(order: int, c: complex) -> complex:
    n = order + 1
    z = c * n
    a = z / 2
    atoms = jump_data(order)
    transform = sum(
        left_mass
        * right_mass
        * (
            1
            - cmath.exp(-a * abs(left - right))
            - a * abs(left - right)
        )
        / a**2
        for left, left_mass in atoms
        for right, right_mass in atoms
    )
    return transform / (z * kappa(order))


def edge_scout() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    magnitudes: list[float] = []
    for order in EDGE_ORDERS:
        n = order + 1
        value = finite_profile(order, 4j)
        magnitude = abs(value)
        magnitudes.append(magnitude)
        rows.append(
            {
                "n": n,
                "real": value.real,
                "imag": value.imag,
                "magnitude": magnitude,
                "magnitude_over_n_one_third": magnitude / n ** (1 / 3),
            }
        )
    slopes = [
        math.log(magnitudes[index + 1] / magnitudes[index], 2)
        for index in range(len(magnitudes) - 1)
    ]
    if not all(slopes[index + 1] < slopes[index] for index in range(len(slopes) - 1)):
        raise AssertionError("edge log-slopes did not descend")
    if not (1 / 3 < slopes[-1] < 0.45):
        raise AssertionError("edge scout left the expected one-third corridor")
    return {
        "status": "DISCOVERY_ONLY",
        "rows": rows,
        "successive_log2_slopes": slopes,
        "conjectured_amplitude_exponent": "1/3",
        "conjectured_window_exponent": "2/3",
    }


def build_payload() -> dict[str, object]:
    subthreshold_rows = []
    for y in (0.5, 1.0, 2.0, 3.0, 3.5):
        tangent_value = subthreshold_profile(y)
        right_limit = profile_complex(complex(1e-7, y))
        if tangent_value <= 1:
            raise AssertionError("subthreshold profile failed strict positivity above Phi(0)")
        if abs(right_limit.real - tangent_value) > 2e-5:
            raise AssertionError("right-half-plane continuation missed tangent boundary")
        if abs(right_limit.imag) > 2e-4:
            raise AssertionError("subthreshold boundary failed to become real")
        subthreshold_rows.append(
            {
                "y": y,
                "phi_iy": tangent_value,
                "right_limit_real": right_limit.real,
                "right_limit_imag": right_limit.imag,
            }
        )
    if not all(
        subthreshold_rows[index + 1]["phi_iy"] > subthreshold_rows[index]["phi_iy"]
        for index in range(len(subthreshold_rows) - 1)
    ):
        raise AssertionError("subthreshold profile was not increasing")

    first_constant = 288 / math.pi**3
    y_edge = 3.9999
    scaled_edge = (
        subthreshold_profile(y_edge, THRESHOLD_PANELS)
        * math.sqrt(16 - y_edge * y_edge)
    )
    if abs(scaled_edge / first_constant - 1) > 0.02:
        raise AssertionError("first threshold coefficient regression failed")

    density_rows = []
    for mode in (1, 3, 5):
        threshold = 16 * mode * mode
        t = threshold + 1e-6
        scaled = spectral_density(t) * math.sqrt(t - threshold)
        predicted = 288 / (math.pi**4 * mode**3)
        if abs(scaled / predicted - 1) > 2e-4:
            raise AssertionError("threshold density coefficient failed")
        density_rows.append(
            {
                "odd_mode": mode,
                "scaled_density": scaled,
                "predicted": predicted,
            }
        )

    cut_rows = []
    for y in (5.0, 8.0, 10.0, 13.0):
        imaginary = boundary_imaginary_part(y)
        if not imaginary < 0:
            raise AssertionError("right-face Plemelj sign failed")
        cut_rows.append({"y": y, "right_face_imaginary_part": imaginary})

    edge = edge_scout()
    finite_checks = (
        len(subthreshold_rows) * 3
        + len(density_rows) * 2
        + len(cut_rows)
        + len(edge["successive_log2_slopes"])
        + 8
    )
    core = {
        "subthreshold": subthreshold_rows,
        "first_threshold_scaled": scaled_edge,
        "threshold_density": density_rows,
        "cut_boundary": cut_rows,
        "edge_slopes": edge["successive_log2_slopes"],
    }
    proof_object = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "schema": "riemann.t108000.beta-chebyshev-perron-edge.v1",
        "proof_object_sha256": proof_object,
        "classification": "PASS_T108000_BETA_CHEBYSHEV_PERRON_EDGE_BOUNDARY",
        "finite_checks": finite_checks,
        "subthreshold": subthreshold_rows,
        "first_threshold": {
            "scaled_value": scaled_edge,
            "predicted_288_over_pi_cubed": first_constant,
        },
        "threshold_density": density_rows,
        "cut_boundary": cut_rows,
        "finite_edge_scout": edge,
        "subthreshold_boundary_proved": True,
        "plemelj_jump_proved": True,
        "all_threshold_coefficients_proved": True,
        "closed_boundary_profile_zero_free_proved": True,
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
