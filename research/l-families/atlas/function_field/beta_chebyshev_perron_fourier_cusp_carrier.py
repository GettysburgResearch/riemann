#!/usr/bin/env python3
"""Bounded replay for the local Perron--Fourier cubic-cusp carrier."""

from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "beta_chebyshev_perron_fourier_cusp_carrier.json"

SOURCE_BLOBS = {
    (
        "9e4bd5ba7b4efb08bb114b0689c823e646e8d6b6",
        "research/l-families/atlas/function_field/BETA_CHEBYSHEV_CUBIC_CUSP_EDGE_PROFILE.md",
    ): "9ffa128b9d64b981499e81c25d39dd9f8c7dac96",
    (
        "9e4bd5ba7b4efb08bb114b0689c823e646e8d6b6",
        "research/l-families/atlas/function_field/beta_chebyshev_cubic_cusp_edge_profile.py",
    ): "db42aa1ac15fa2fcdd7c7665654cb98398900e4f",
    (
        "9e4bd5ba7b4efb08bb114b0689c823e646e8d6b6",
        "research/l-families/atlas/function_field/beta_chebyshev_cubic_cusp_edge_profile.json",
    ): "b955919e40a81febb0d74bed30990efaa63eaf94",
    (
        "9e4bd5ba7b4efb08bb114b0689c823e646e8d6b6",
        "tests/test_beta_chebyshev_cubic_cusp_edge_profile.py",
    ): "cdbc61875c084a7680842a3fddb064380a82f0ed",
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/FFPS_BANDPASS_ASSEMBLED_PERRON_LEAKAGE.md",
    ): "e7959b8788b8a374920aa53bcafd1fb28cda3b72",
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.py",
    ): "52023bb4527a32a2c9983fdd25707da3361242e8",
}

PROFILE_PANELS = 32768
PROFILE_LIMIT = 6.0
FINITE_ORDERS = (31, 63, 127, 255)
TAU_ROWS = (0.0, 1.0, 2.0)


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        actual = completed.stdout.strip()
        if actual != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def simpson(function, left: float, right: float, panels: int) -> complex:
    if panels < 2 or panels % 2:
        raise ValueError("panels must be positive and even")
    step = (right - left) / panels
    endpoint = function(left) + function(right)
    real_terms = [endpoint.real]
    imag_terms = [endpoint.imag]
    for index in range(1, panels):
        coefficient = 4 if index % 2 else 2
        value = function(left + index * step)
        real_terms.append(coefficient * value.real)
        imag_terms.append(coefficient * value.imag)
    return complex(math.fsum(real_terms), math.fsum(imag_terms)) * step / 3


def cell_boundaries(order: int) -> tuple[float, ...]:
    if order < 1:
        raise ValueError("order must be at least one")
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


def jump_transform(order: int, z: complex) -> complex:
    """J_r(z)/h_r^2 from the exact jump Green kernel."""
    if z == 0:
        raise ValueError("z must be nonzero")
    a = z / 2
    atoms = jump_data(order)
    return sum(
        left_mass
        * right_mass
        * (1 - cmath.exp(-a * abs(left - right)) - a * abs(left - right))
        / a**2
        for left, left_mass in atoms
        for right, right_mass in atoms
    )


def finite_zero_mode_profile(order: int, c: complex) -> complex:
    n = order + 1
    z = n * c
    return jump_transform(order, z) / (z * kappa(order))


def finite_frequency_transform(order: int, z: complex, frequency: float) -> complex:
    """Integral R_r(s)e^{-z|s|/2}e^{-it s} ds, normalized by h_r^2."""
    return (
        jump_transform(order, z + 2j * frequency)
        + jump_transform(order, z - 2j * frequency)
    ) / 2


def finite_frequency_profile(order: int, c: complex, frequency: float) -> complex:
    n = order + 1
    z = n * c
    return finite_frequency_transform(order, z, frequency) / (z * kappa(order))


def _exponential_integral(alpha: complex, left: float, right: float, sign: int) -> complex:
    if abs(alpha) < 1e-12:
        return right - left
    if sign == 1:
        return (cmath.exp(alpha * right) - cmath.exp(alpha * left)) / alpha
    if sign == -1:
        return (cmath.exp(-alpha * left) - cmath.exp(-alpha * right)) / alpha
    raise ValueError("sign must be +1 or -1")


def _triangle_integral(alpha: complex, width: float) -> complex:
    if abs(alpha) < 1e-8:
        return (
            width**2 / 2
            - alpha * width**3 / 6
            + alpha**2 * width**4 / 24
        )
    return width / alpha - (1 - cmath.exp(-alpha * width)) / alpha**2


def direct_cell_frequency_transform(order: int, z: complex, frequency: float) -> complex:
    """Independent exact cell-pair evaluation of the tilted Fourier transform."""
    boundaries = cell_boundaries(order)
    alpha_plus = z / 2 + 1j * frequency
    alpha_minus = z / 2 - 1j * frequency
    total = 0j
    for left_cell in range(order + 1):
        left_start = boundaries[left_cell]
        left_end = boundaries[left_cell + 1]
        width = left_end - left_start
        total += _triangle_integral(alpha_plus, width)
        total += _triangle_integral(alpha_minus, width)
        left_sign = (-1) ** left_cell
        for right_cell in range(left_cell + 1, order + 1):
            right_start = boundaries[right_cell]
            right_end = boundaries[right_cell + 1]
            right_sign = (-1) ** right_cell
            plus = _exponential_integral(
                alpha_plus, left_start, left_end, 1
            ) * _exponential_integral(alpha_plus, right_start, right_end, -1)
            minus = _exponential_integral(
                alpha_minus, left_start, left_end, 1
            ) * _exponential_integral(alpha_minus, right_start, right_end, -1)
            total += left_sign * right_sign * (plus + minus)
    return total


def cubic_cusp_profile_complex(zeta: complex) -> complex:
    """Analytic continuation of the T-108002 cusp profile to Re(zeta)>0."""
    if zeta.real <= 0:
        raise ValueError("zeta must lie in the open right half-plane")
    constant = 72 * math.sqrt(2) / math.pi**3 * cmath.exp(-1j * math.pi / 4)
    integral = simpson(
        lambda x: cmath.exp(
            -math.pi * zeta * x * x / 4
            + 1j * math.pi**3 * x**6 / 24
        ),
        0.0,
        PROFILE_LIMIT,
        PROFILE_PANELS,
    )
    return constant * integral


def perron_fourier_cusp(lam: float, tau: float) -> complex:
    if lam <= 0:
        raise ValueError("lambda must be positive")
    return (
        cubic_cusp_profile_complex(complex(lam, 2 * tau))
        + cubic_cusp_profile_complex(complex(lam, -2 * tau))
    ) / 2


def dual_lag_carrier(lam: float, v: float) -> complex:
    """Fourier transform in tau of the limiting local carrier, v != 0."""
    if lam <= 0:
        raise ValueError("lambda must be positive")
    if v == 0:
        raise ValueError("the locally integrable dual carrier is singular at zero")
    magnitude = abs(v)
    return (
        72
        / math.pi ** 2.5
        * cmath.exp(-1j * math.pi / 4)
        * magnitude ** -0.5
        * cmath.exp(-lam * magnitude / 2 + 1j * magnitude**3 / 3)
    )


def inverse_dual_lag_carrier(lam: float, tau: float) -> complex:
    """Independent inverse-Fourier replay after v=x^2 removes the cusp."""
    if lam <= 0:
        raise ValueError("lambda must be positive")
    constant = 144 / math.pi ** 3.5 * cmath.exp(-1j * math.pi / 4)
    integral = simpson(
        lambda x: cmath.exp(-lam * x * x / 2 + 1j * x**6 / 3)
        * math.cos(tau * x * x),
        0.0,
        PROFILE_LIMIT,
        PROFILE_PANELS,
    )
    return constant * integral


def build_payload() -> dict[str, object]:
    split_rows = []
    for order, z, frequency in (
        (3, complex(3.0, 4.0), 0.75),
        (7, complex(2.5, 6.0), 1.25),
        (12, complex(4.0, 3.0), 2.0),
    ):
        by_cells = direct_cell_frequency_transform(order, z, frequency)
        by_split = finite_frequency_transform(order, z, frequency)
        error = abs(by_cells - by_split)
        if error > 2e-12:
            raise AssertionError("exact frequency-splitting identity failed")
        split_rows.append(
            {
                "order": order,
                "z_real": z.real,
                "z_imag": z.imag,
                "frequency": frequency,
                "absolute_error": error,
            }
        )

    lam = 2.0
    cusp_rows = []
    for tau in TAU_ROWS:
        target = perron_fourier_cusp(lam, tau)
        inverse = inverse_dual_lag_carrier(lam, tau)
        dual_error = abs(target - inverse)
        if dual_error > 2e-10:
            raise AssertionError("dual lag carrier failed inverse-Fourier replay")
        finite_rows = []
        errors = []
        for order in FINITE_ORDERS:
            n = order + 1
            c = 4j + lam * n ** (-2 / 3)
            value = finite_frequency_profile(order, c, tau * n ** (1 / 3))
            scaled = value / n ** (1 / 3)
            error = abs(scaled - target)
            errors.append(error)
            finite_rows.append(
                {
                    "n": n,
                    "real": scaled.real,
                    "imag": scaled.imag,
                    "absolute_error_to_limit": error,
                }
            )
        if not all(errors[index + 1] < errors[index] for index in range(len(errors) - 1)):
            raise AssertionError("finite two-parameter cusp errors did not descend")
        cusp_rows.append(
            {
                "lambda": lam,
                "tau": tau,
                "limit_real": target.real,
                "limit_imag": target.imag,
                "inverse_dual_error": dual_error,
                "finite": finite_rows,
            }
        )

    evenness = abs(perron_fourier_cusp(lam, 1.25) - perron_fourier_cusp(lam, -1.25))
    if evenness > 1e-12:
        raise AssertionError("limiting Fourier cusp was not even in tau")

    dual_sample = dual_lag_carrier(lam, 1.0)
    core = {
        "split_rows": split_rows,
        "cusp_rows": cusp_rows,
        "evenness_error": evenness,
        "dual_sample": {"real": dual_sample.real, "imag": dual_sample.imag},
    }
    proof_object = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "schema": "riemann.t108004.beta-chebyshev-perron-fourier-cusp.v1",
        "classification": "PASS_T108004_BETA_CHEBYSHEV_PERRON_FOURIER_CUSP_CARRIER",
        "proof_object_sha256": proof_object,
        "finite_checks": 3 + len(TAU_ROWS) * (len(FINITE_ORDERS) + 2) + 2,
        "split_rows": split_rows,
        "cusp_rows": cusp_rows,
        "evenness_error": evenness,
        "dual_sample": core["dual_sample"],
        "frequency_split_identity_proved": True,
        "complex_cusp_extension_proved": True,
        "two_parameter_perron_fourier_cusp_proved": True,
        "exact_dual_lag_carrier_proved": True,
        "natural_frequency_window": "t=tau*n^(1/3)",
        "natural_log_ratio_window": "log(m/n)=v*n^(-1/3)",
        "beta_source_correlation_estimate_proved": False,
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
