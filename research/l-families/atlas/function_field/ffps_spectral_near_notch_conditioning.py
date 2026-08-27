#!/usr/bin/env python3
"""Bounded replay for the spectral near-notch conditioning law."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_spectral_near_notch_conditioning.json"

SOURCE_COMMIT = "805ab873cb051c739f19978ebb772b2625adcffb"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_SPECTRAL_ZERO_FREE_CARRIER_TILT.md": "a23f6f57dc87ef698fd06e9fe2680119e032e37b",
    "research/l-families/atlas/function_field/ffps_spectral_zero_free_carrier_tilt.py": "f8f7c7596c368293cf5005c25e8f156ebcf0b94c",
    "research/l-families/atlas/function_field/ffps_spectral_zero_free_carrier_tilt.json": "3d7e74420af1b85c7ab35a11166c54e3218434d2",
    "tests/test_ffps_spectral_zero_free_carrier_tilt.py": "2c2215c3810089b46b7f3d83d5ed7b5aa77f3e85",
}

DLMF_ZERO_URL = "https://dlmf.nist.gov/10.21#i"
DLMF_ASYMPTOTIC_URL = "https://dlmf.nist.gov/10.52#ii"
MAX_RUNG = 4
NUMERICAL_ROOT_RUNGS = 3
NUMERICAL_ROOTS_PER_RUNG = 2
BISECTION_STEPS = 72


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


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


def validate_rung(rung: int) -> None:
    if rung < 1:
        raise ValueError("rung must be positive")


def odd_double_factorial(value: int) -> int:
    if value < 1 or value % 2 == 0:
        raise ValueError("value must be a positive odd integer")
    output = 1
    for factor in range(1, value + 1, 2):
        output *= factor
    return output


def energy_curvature(rung: int) -> Fraction:
    validate_rung(rung)
    return Fraction(2 * rung + 1, 2 * rung + 3)


def centered_second_moment(rung: int) -> Fraction:
    validate_rung(rung)
    return Fraction(1, 2 * rung + 3)


def normalized_notch_modulus_jet(
    rung: int,
    first_derivative: Fraction,
    second_derivative: Fraction,
    third_derivative: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    """Coefficients of tau^2, tau^3, tau^4 at an old simple notch.

    The derivatives are F'(a_k), F''(a_k), F'''(a_k) for
    F(a)=Phi(-i*a).  Division by Phi(tau)^2 is included.
    """
    validate_rung(rung)
    d1 = Fraction(first_derivative)
    d2 = Fraction(second_derivative)
    d3 = Fraction(third_derivative)
    tau2 = d1**2
    tau3 = Fraction(0)
    tau4 = d2**2 / 4 - d1 * d3 / 3 - centered_second_moment(rung) * d1**2
    return tau2, tau3, tau4


def local_rescaled_profile(first_derivative: Fraction, offset: Fraction) -> Fraction:
    d1 = Fraction(first_derivative)
    y = Fraction(offset)
    return d1**2 * (1 + y**2)


def notch_floor_per_energy(rung: int, derivative_squared: Fraction) -> Fraction:
    validate_rung(rung)
    derivative_squared = Fraction(derivative_squared)
    if derivative_squared <= 0:
        raise ValueError("derivative square must be positive")
    return derivative_squared / energy_curvature(rung)


def energy_per_notch_floor(rung: int, derivative_squared: Fraction) -> Fraction:
    return 1 / notch_floor_per_energy(rung, derivative_squared)


def compact_band_floor_coefficient(
    derivative_squares: tuple[Fraction, ...],
) -> Fraction:
    if not derivative_squares:
        raise ValueError("band must contain at least one old notch")
    values = tuple(Fraction(value) for value in derivative_squares)
    if any(value <= 0 for value in values):
        raise ValueError("all derivative squares must be positive")
    return min(values)


def compact_band_condition_product(
    rung: int, derivative_squares: tuple[Fraction, ...]
) -> Fraction:
    return energy_curvature(rung) / compact_band_floor_coefficient(derivative_squares)


def local_minimum_shift_times_root(rung: int) -> int:
    """The exact coefficient in a_k*(a_k(tau)-a_k)/tau^2."""
    validate_rung(rung)
    return rung + 1


def minimum_floor_quartic_ratio(rung: int, inverse_root_square: Fraction) -> Fraction:
    """Coefficient eta_min in floor/(D^2*tau^2)=1+eta_min*tau^2+..."""
    validate_rung(rung)
    inverse_root_square = Fraction(inverse_root_square)
    if inverse_root_square <= 0:
        raise ValueError("inverse root square must be positive")
    return (
        Fraction(1, 3)
        - centered_second_moment(rung)
        - Fraction((2 * rung + 2) * (2 * rung + 3), 3) * inverse_root_square
    )


def old_frequency_quartic_ratio(rung: int, inverse_root_square: Fraction) -> Fraction:
    """Coefficient eta_old at the unshifted old-notch frequency."""
    validate_rung(rung)
    inverse_root_square = Fraction(inverse_root_square)
    if inverse_root_square <= 0:
        raise ValueError("inverse root square must be positive")
    return (
        Fraction(1, 3)
        - centered_second_moment(rung)
        - Fraction((2 * rung + 2) * (2 * rung + 6), 12) * inverse_root_square
    )


def high_notch_derivative_power(rung: int) -> int:
    validate_rung(rung)
    return rung + 1


def high_notch_squared_condition_power(rung: int) -> int:
    return 2 * high_notch_derivative_power(rung)


def spherical_bessel_j(rung: int, argument: float) -> float:
    """Small bounded numerical certificate; not used in the proof."""
    if rung < 0:
        raise ValueError("spherical order must be nonnegative")
    if argument <= 0:
        raise ValueError("argument must be positive")
    j0 = math.sin(argument) / argument
    if rung == 0:
        return j0
    j1 = math.sin(argument) / argument**2 - math.cos(argument) / argument
    if rung == 1:
        return j1
    previous, current = j0, j1
    for order in range(1, rung):
        following = (2 * order + 1) * current / argument - previous
        previous, current = current, following
    return current


def first_positive_spherical_roots(rung: int, count: int) -> tuple[float, ...]:
    validate_rung(rung)
    if count < 1:
        raise ValueError("root count must be positive")
    step = math.pi / 64
    left = 1.0
    left_value = spherical_bessel_j(rung, left)
    roots: list[float] = []
    right = left + step
    while len(roots) < count and right <= 64.0:
        right_value = spherical_bessel_j(rung, right)
        if left_value * right_value < 0:
            low, high = left, right
            low_value = left_value
            for _ in range(BISECTION_STEPS):
                midpoint = (low + high) / 2
                midpoint_value = spherical_bessel_j(rung, midpoint)
                if low_value * midpoint_value <= 0:
                    high = midpoint
                else:
                    low = midpoint
                    low_value = midpoint_value
            roots.append((low + high) / 2)
        left, left_value = right, right_value
        right += step
    if len(roots) != count:
        raise RuntimeError("bounded root certificate failed")
    return tuple(roots)


def notch_derivative_magnitude(rung: int, root: float) -> float:
    validate_rung(rung)
    if root <= 0:
        raise ValueError("root must be positive")
    derivative = spherical_bessel_j(rung - 1, root)
    return odd_double_factorial(2 * rung + 1) * abs(derivative) / root**rung


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    symbolic_rows = []
    for rung in range(1, MAX_RUNG + 1):
        sample_jet = normalized_notch_modulus_jet(
            rung, Fraction(rung + 1), Fraction(2 * rung + 1), Fraction(3 * rung + 2)
        )
        if sample_jet[1] != 0:
            raise AssertionError("odd notch-modulus coefficient did not vanish")
        synthetic_squares = (
            Fraction((rung + 1) ** 2),
            Fraction((rung + 2) ** 2, 4),
            Fraction((rung + 3) ** 2, 9),
        )
        symbolic_rows.append(
            {
                "rung": rung,
                "energy_curvature": fraction_text(energy_curvature(rung)),
                "centered_second_moment": fraction_text(centered_second_moment(rung)),
                "sample_notch_modulus_coefficients_tau_2_to_tau_4": [
                    fraction_text(value) for value in sample_jet
                ],
                "sample_local_profile_y_minus1_0_1": [
                    fraction_text(
                        local_rescaled_profile(Fraction(rung + 1), Fraction(y))
                    )
                    for y in (-1, 0, 1)
                ],
                "sample_band_floor_coefficient": fraction_text(
                    compact_band_floor_coefficient(synthetic_squares)
                ),
                "sample_energy_times_condition_limit": fraction_text(
                    compact_band_condition_product(rung, synthetic_squares)
                ),
                "high_notch_derivative_decay_power": high_notch_derivative_power(rung),
                "high_notch_squared_condition_growth_power": high_notch_squared_condition_power(
                    rung
                ),
                "local_minimum_shift_times_root": local_minimum_shift_times_root(rung),
                "sample_minimum_floor_quartic_ratio_at_inverse_root_square_1_over_25": fraction_text(
                    minimum_floor_quartic_ratio(rung, Fraction(1, 25))
                ),
                "sample_old_frequency_quartic_ratio_at_inverse_root_square_1_over_25": fraction_text(
                    old_frequency_quartic_ratio(rung, Fraction(1, 25))
                ),
            }
        )

    numerical_rows = []
    for rung in range(1, NUMERICAL_ROOT_RUNGS + 1):
        for index, root in enumerate(
            first_positive_spherical_roots(rung, NUMERICAL_ROOTS_PER_RUNG), start=1
        ):
            derivative = notch_derivative_magnitude(rung, root)
            numerical_rows.append(
                {
                    "rung": rung,
                    "root_index": index,
                    "root_rounded": f"{root:.12f}",
                    "spherical_residual_abs": f"{abs(spherical_bessel_j(rung, root)):.3e}",
                    "D_m_k_rounded": f"{derivative:.12f}",
                    "notch_floor_per_energy_rounded": f"{derivative**2 / float(energy_curvature(rung)):.12f}",
                }
            )

    return {
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "classical_external_inputs": [
            {
                "source": "NIST DLMF 10.21(i)",
                "url": DLMF_ZERO_URL,
                "use": "reality and simplicity of the positive Bessel zeros",
            },
            {
                "source": "NIST DLMF 10.52(ii)",
                "url": DLMF_ASYMPTOTIC_URL,
                "use": "fixed-order large-argument spherical-Bessel asymptotics",
            },
        ],
        "near_notch_theorem": {
            "F_formula": "F_m(a)=Phi_m(-i*a)=(2m+1)!!*j_m(a)/a^m",
            "old_notches": "a_k=j_(m+1/2,k), omega_k=2*a_k/S",
            "derivative_constant": "D_(m,k)=|F_m'(a_k)|=(2m+1)!!*|j_m'(a_k)|/a_k^m",
            "pointwise_floor": "|Qhat_tau(omega_k)|^2=D_(m,k)^2*tau^2+O(tau^4)",
            "energy_excess": "Delta_m(tau)=E_m(tau)/E_m(0)-1=((2m+1)/(2m+3))*tau^2+O(tau^4)",
            "exact_tradeoff": "lim |Qhat_tau(omega_k)|^2/Delta_m(tau)=D_(m,k)^2*((2m+3)/(2m+1))",
            "local_profile": "for a=a_k+|tau|*y, |Qhat_tau(2a/S)|^2/tau^2 -> D_(m,k)^2*(1+y^2)",
            "minimum_shift": "a_k(tau)=a_k+(m+1)*tau^2/a_k+O(tau^4)",
            "minimum_quartic_ratio": "eta_min=1/3-1/(2m+3)-(2m+2)*(2m+3)/(3*a_k^2)",
            "old_frequency_quartic_ratio": "eta_old=1/3-1/(2m+3)-(2m+2)*(2m+6)/(12*a_k^2)",
            "compact_band": "if band endpoints avoid old notches and the band contains some, lambda_A(tau)=d_(m,A)^2*tau^2+O(tau^4)",
            "condition_product": "Delta_m(tau)/lambda_A(tau) -> ((2m+1)/(2m+3))/d_(m,A)^2",
            "high_notch_asymptotic": "D_(m,k)~(2m+1)!!*a_k^(-m-1), so individual squared conditioning grows like a_k^(2m+2)",
            "symbolic_rows": symbolic_rows,
            "bounded_numerical_certificates": numerical_rows,
        },
        "proof_ledger": {
            "even_pointwise_notch_jet_through_tau_4": "PROVED EXACT",
            "pointwise_energy_floor_tradeoff": "PROVED EXACT FROM FROZEN CURVATURE",
            "local_rescaled_quadratic_profile": "PROVED EXACT",
            "fixed_compact_band_floor_law": "PROVED",
            "high_notch_conditioning_power": "PROVED FROM CLASSICAL ASYMPTOTICS",
            "uniform_coercivity_from_zero_freeness": "DISPROVED",
            "new_beta_cancellation_or_subpower_estimate": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_symbolic_rung": MAX_RUNG,
            "numerical_root_rungs": NUMERICAL_ROOT_RUNGS,
            "numerical_roots_per_rung": NUMERICAL_ROOTS_PER_RUNG,
            "bisection_steps_per_root": BISECTION_STEPS,
            "beta_terms": 0,
            "primes": 0,
            "zeta_zeros": 0,
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
