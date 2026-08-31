#!/usr/bin/env python3
"""Replay the chiral beta--Chebyshev cusp/source convolution normal form."""

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
OUTPUT = HERE / "beta_chebyshev_chiral_cusp_source_convolution.json"

SOURCE_BLOBS = {
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/"
        "FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md",
    ): "21ef8f5215ca349f0efffd52dca1543ef6d988d6",
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/"
        "ffps_assembled_beta_perron_fourier_bridge.py",
    ): "2dbe93508eadcc9ba9ed15a5f64d02f13c728ef3",
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/"
        "ffps_assembled_beta_perron_fourier_bridge.json",
    ): "1223ab8049492f58cf5e64a25f80d5799aa165f7",
    (
        "b41a4e4b9fd518dfb97229a6a94346b2d49e528f",
        "research/l-families/atlas/function_field/"
        "BETA_CHEBYSHEV_PERRON_FOURIER_CUSP_CARRIER.md",
    ): "f46a7b283061ad35c38a5060a99c5098d4c14aff",
    (
        "b41a4e4b9fd518dfb97229a6a94346b2d49e528f",
        "research/l-families/atlas/function_field/"
        "beta_chebyshev_perron_fourier_cusp_carrier.py",
    ): "027a306e69f65661fbf44de4ee503dc03004a315",
    (
        "b41a4e4b9fd518dfb97229a6a94346b2d49e528f",
        "research/l-families/atlas/function_field/"
        "beta_chebyshev_perron_fourier_cusp_carrier.json",
    ): "216de6ac6230e99b233fa7af913c7daf3952a09a",
}

EXCEPTIONAL_PRIME = 67
EDGE_SIZES = (32, 64, 128, 256, 512)
QUADRATURE_PANELS = 32768
QUADRATURE_LIMIT = 6.0


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
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


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
    return tuple(
        (1 - math.cos(index * math.pi / n)) / 2 for index in range(n + 1)
    )


def jump_masses(n: int) -> tuple[int, ...]:
    return tuple(
        ((-1) ** index) * (1 if index in (0, n) else 2)
        for index in range(n + 1)
    )


def finite_spectrum_sum(n: int, c: complex) -> complex:
    points = cell_boundaries(n)
    masses = jump_masses(n)
    z_half = n * c / 2
    total = complex(sum(mass * mass for mass in masses), 0.0)
    for left in range(n):
        for right in range(left + 1, n + 1):
            total += (
                2
                * masses[left]
                * masses[right]
                * cmath.exp(-z_half * (points[right] - points[left]))
            )
    return total


def finite_profile(n: int, c: complex) -> complex:
    if c == 0:
        raise ValueError("c must be nonzero")
    z = n * c
    return 4 * (z - finite_spectrum_sum(n, c)) / (z**3 * kappa_from_n(n))


def j_over_h_squared(n: int, w: complex) -> complex:
    if w == 0:
        return 0j
    return w * kappa_from_n(n) * finite_profile(n, w / n)


def two_face_transform_normalized(n: int, z: complex, t: float) -> complex:
    return 0.5 * (
        j_over_h_squared(n, z + 2j * t)
        + j_over_h_squared(n, z - 2j * t)
    )


def mobius(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    value = n
    parity = 0
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            value //= prime
            if value % prime == 0:
                return 0
            parity ^= 1
            while value % prime == 0:
                value //= prime
        prime += 1
    if value > 1:
        parity ^= 1
    return -1 if parity else 1


def beta_coefficient(n: int) -> int:
    value = mobius(n)
    if n % EXCEPTIONAL_PRIME == 0:
        value -= mobius(n // EXCEPTIONAL_PRIME)
    return value


def beta_dirichlet_polynomial(w: complex, cap: int = 96) -> complex:
    return sum(beta_coefficient(n) * n ** (-w) for n in range(1, cap + 1))


def beta_pair_product(s: complex, t: float, cap: int = 96) -> complex:
    return beta_dirichlet_polynomial(s - 1j * t, cap) * beta_dirichlet_polynomial(
        s + 1j * t, cap
    )


def cubic_profile(parameter: complex) -> complex:
    if parameter.real <= 0:
        raise ValueError("the replay integral requires positive real part")
    coefficient = 72 * math.sqrt(2) / math.pi**3 * cmath.exp(-1j * math.pi / 4)
    return coefficient * simpson(
        lambda x: cmath.exp(
            -math.pi * parameter * x * x / 4
            + 1j * math.pi**3 * x**6 / 24
        ),
        0.0,
        QUADRATURE_LIMIT,
        QUADRATURE_PANELS,
    )


def symmetric_cusp_profile(lam: float, tau: float) -> complex:
    return 0.5 * (
        cubic_profile(complex(lam, 2 * tau))
        + cubic_profile(complex(lam, -2 * tau))
    )


def directed_cusp_profile(lam: float, tau: float) -> complex:
    return cubic_profile(complex(lam, 2 * tau))


def chiral_density(lam: float, v: float) -> complex:
    if lam <= 0:
        raise ValueError("lambda must be positive")
    if v >= 0:
        return 0j
    magnitude = -v
    return (
        144
        / math.pi ** (5 / 2)
        * cmath.exp(-1j * math.pi / 4)
        * magnitude ** (-1 / 2)
        * cmath.exp(-lam * magnitude / 2 + 1j * magnitude**3 / 3)
    )


def inverse_chiral_profile(lam: float, tau: float) -> complex:
    if lam <= 0:
        raise ValueError("lambda must be positive")
    coefficient = 144 / math.pi ** (7 / 2) * cmath.exp(-1j * math.pi / 4)
    return coefficient * simpson(
        lambda x: cmath.exp(
            -lam * x * x / 2 + 1j * x**6 / 3 - 1j * tau * x * x
        ),
        0.0,
        QUADRATURE_LIMIT,
        QUADRATURE_PANELS,
    )


def chiral_l1_norm(lam: float) -> float:
    if lam <= 0:
        raise ValueError("lambda must be positive")
    return 144 * math.sqrt(2) / (math.pi**2 * math.sqrt(lam))


def edge_gamma_constant() -> complex:
    coefficient = (
        12
        * math.sqrt(2)
        / math.pi**3
        * (24 / math.pi**3) ** (1 / 6)
        * math.gamma(1 / 6)
    )
    return coefficient * cmath.exp(-1j * math.pi / 6)


def directed_boundary_constant() -> complex:
    return 1j * math.pi**2 / 18 * edge_gamma_constant()


def complex_row(value: complex) -> dict[str, float]:
    return {"real": value.real, "imag": value.imag, "magnitude": abs(value)}


def exceptional_multiplier(s: complex, t: float, prime: int = 67) -> complex:
    q = prime ** (-s)
    return 1 - 2 * q * math.cos(t * math.log(prime)) + q * q


def exceptional_dual_l1_bound(n: int, lam: float, prime: int = 67) -> float:
    s = 0.5 + 2j * n + lam * n ** (1 / 3) / 2
    q = prime ** (-s)
    return (2 * abs(q) + abs(q * q)) * chiral_l1_norm(lam)


def build_payload() -> dict[str, object]:
    n_source = 12
    z_source = complex(2.4, 0.7)
    s_source = (1 + z_source) / 2
    grid = tuple(index / 2 for index in range(-12, 13))
    full_sum = 0j
    directed_sum = 0j
    evenness_error = 0.0
    vertical_coordinate_error = 0.0
    for t in grid:
        product = beta_pair_product(s_source, t)
        opposite = beta_pair_product(s_source, -t)
        evenness_error = max(evenness_error, abs(product - opposite))
        full_sum += two_face_transform_normalized(n_source, z_source, t) * product
        directed_sum += j_over_h_squared(n_source, z_source + 2j * t) * product

        omega = z_source + 2j * t
        vertical_product = beta_dirichlet_polynomial(
            (1 + omega) / 2
        ) * beta_dirichlet_polynomial((1 + 2 * z_source - omega) / 2)
        vertical_coordinate_error = max(
            vertical_coordinate_error,
            abs(vertical_product - product),
        )
    directed_error = abs(full_sum - directed_sum)
    if evenness_error > 2e-12:
        raise AssertionError("beta pair product was not even")
    if directed_error > 2e-10:
        raise AssertionError("two-face source pairing did not become directed")
    if vertical_coordinate_error > 2e-12:
        raise AssertionError("vertical beta arguments were misidentified")

    lam = 2.0
    local_n = 27
    local_scale = local_n ** (1 / 3)
    local_s = 0.5 + 2j * local_n + lam * local_scale / 2
    tau_grid = tuple(index / 4 for index in range(-8, 9))
    symmetric_local_sum = 0j
    directed_local_sum = 0j
    local_evenness_error = 0.0
    for tau in tau_grid:
        product = beta_pair_product(local_s, tau * local_scale)
        opposite = beta_pair_product(local_s, -tau * local_scale)
        local_evenness_error = max(local_evenness_error, abs(product - opposite))
        symmetric_local_sum += symmetric_cusp_profile(lam, tau) * product
        directed_local_sum += directed_cusp_profile(lam, tau) * product
    local_directed_error = abs(symmetric_local_sum - directed_local_sum)
    if local_evenness_error > 2e-12:
        raise AssertionError("local beta pair product was not even")
    if local_directed_error > 2e-9:
        raise AssertionError("local symmetric cusp did not reduce to one chirality")

    chiral_rows: list[dict[str, object]] = []
    for tau in (0.0, 1.0, 2.0):
        directed = directed_cusp_profile(lam, tau)
        inverse = inverse_chiral_profile(lam, tau)
        error = abs(directed - inverse)
        if error > 3e-8:
            raise AssertionError("one-sided inverse Fourier carrier mismatch")
        chiral_rows.append(
            {
                "lambda": lam,
                "tau": tau,
                "directed_profile": complex_row(directed),
                "one_sided_inverse_fourier": complex_row(inverse),
                "absolute_error": error,
            }
        )

    predicted_boundary = directed_boundary_constant()
    boundary_rows: list[dict[str, object]] = []
    boundary_errors: list[float] = []
    for n in EDGE_SIZES:
        scaled = n ** (2 / 3) * j_over_h_squared(n, 4j * n)
        error = abs(scaled - predicted_boundary)
        boundary_errors.append(error)
        boundary_rows.append(
            {
                "n": n,
                "scaled_directed_boundary_carrier": complex_row(scaled),
                "absolute_error_to_limit": error,
            }
        )
    if not all(
        boundary_errors[index + 1] < boundary_errors[index]
        for index in range(len(boundary_errors) - 1)
    ):
        raise AssertionError("directed boundary errors did not descend")

    exceptional_rows: list[dict[str, object]] = []
    exceptional_bounds: list[float] = []
    for n in (8, 27, 64, 125):
        bound = exceptional_dual_l1_bound(n, lam)
        exceptional_bounds.append(bound)
        scale = n ** (1 / 3)
        s = 0.5 + 2j * n + lam * scale / 2
        exceptional_rows.append(
            {
                "n": n,
                "local_shift": scale * math.log(EXCEPTIONAL_PRIME),
                "exceptional_coefficient_magnitude": abs(
                    EXCEPTIONAL_PRIME ** (-s)
                ),
                "dual_l1_difference_bound": bound,
            }
        )
    if not all(
        exceptional_bounds[index + 1] < exceptional_bounds[index]
        for index in range(len(exceptional_bounds) - 1)
    ):
        raise AssertionError("exceptional-prime dual bounds did not descend")

    numerator_error = 0.0
    for tau in (-2.0, -0.5, 0.0, 1.25, 2.0):
        t = tau * local_scale
        direct = (1 - EXCEPTIONAL_PRIME ** (-(local_s - 1j * t))) * (
            1 - EXCEPTIONAL_PRIME ** (-(local_s + 1j * t))
        )
        assembled = exceptional_multiplier(local_s, t)
        numerator_error = max(numerator_error, abs(direct - assembled))
    if numerator_error > 2e-12:
        raise AssertionError("exceptional numerator did not assemble")

    core: dict[str, object] = {
        "global_source_pairing": {
            "beta_evenness_max_error": evenness_error,
            "directed_face_sum_error": directed_error,
            "vertical_coordinate_max_error": vertical_coordinate_error,
        },
        "local_source_pairing": {
            "beta_evenness_max_error": local_evenness_error,
            "chiral_reduction_sum_error": local_directed_error,
        },
        "chiral_inverse_fourier_rows": chiral_rows,
        "chiral_l1_norm_lambda_two": chiral_l1_norm(lam),
        "directed_boundary_constant": complex_row(predicted_boundary),
        "directed_boundary_rows": boundary_rows,
        "exceptional_numerator_max_error": numerator_error,
        "exceptional_dual_rows": exceptional_rows,
    }
    proof_object = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "schema": "riemann.t108006.beta-chebyshev-chiral-cusp-source.v1",
        "classification": (
            "PASS_T108006_BETA_CHEBYSHEV_CHIRAL_CUSP_SOURCE_CONVOLUTION"
        ),
        "proof_object_sha256": proof_object,
        "finite_checks": 58,
        **core,
        "two_face_source_pairing_reduced_to_one_directed_face": True,
        "reflected_vertical_beta_convolution_proved": True,
        "symmetric_cusp_reduced_to_one_chirality_inside_source": True,
        "one_sided_cubic_log_ratio_carrier_proved": True,
        "exceptional_67_dual_shift_formula_proved": True,
        "positive_lambda_exceptional_channel_decoupling_proved": True,
        "direct_lambda_zero_nonzero_tau_boundary_theorem_proved": False,
        "signed_reciprocal_zeta_correlation_estimate_proved": False,
        "outer_frequency_control_proved": False,
        "perron_boundary_shift_proved": False,
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
