#!/usr/bin/env python3
"""Bounded replay for the fixed-support beta mesoscopic microscope."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_fixed_support_beta_mesoscopic_microscope.json"

LADDER_COMMIT = "3658d4c31cc866e15d48ab1fc9d8d119136da424"
LADDER_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_ZERO_FREE_BETA_ENERGY_LADDER.md": "bd4cbb842e78c1dad5d380c8d20ff14c39bba15e",
    "research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py": "df80000192292cc5fc1cd08013f152fb257054f9",
    "research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.json": "7e8889aa0dd1b01674e20158a52502cff0d8dffa",
    "tests/test_ffps_zero_free_beta_energy_ladder.py": "983a1320f89087028f6724fe36aaca5ca1309b15",
}
FLOW_COMMIT = "46ea68808e238b0c9b85050158ba149649b1b37e"
FLOW_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_TILTED_TENT_DETECTOR_RENORMALIZATION_FLOW.md": "6de962fe78c2f77d3f02e0d11f56f7145eb37f93",
    "research/l-families/atlas/function_field/ffps_tilted_tent_detector_renormalization_flow.py": "8b8c5783714661fd9d6f1803263b544e90b82957",
    "research/l-families/atlas/function_field/ffps_tilted_tent_detector_renormalization_flow.json": "7595d5ce5f24524442c6392de6b23073de1f951b",
    "tests/test_ffps_tilted_tent_detector_renormalization_flow.py": "7763de04d6545ed73b397d00e8485f5631c3ae00",
}

ORDERS = (4, 16, 64)
TAUS = (0.5, 1.0, math.sqrt(2.0), 2.0, 3.0)
AUTOCORRELATION_POINTS = (0.0, 1.0, math.sqrt(2.0), 2.0, 3.0)
SIMPSON_PANELS = 8192
SIMPSON_RADIUS = 14.0


def check_source_blobs() -> None:
    for commit, blobs in (
        (LADDER_COMMIT, LADDER_BLOBS),
        (FLOW_COMMIT, FLOW_BLOBS),
    ):
        for path, expected in blobs.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=3,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"frozen source blob mismatch: {path}")


def validate_order(order: int) -> None:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")


def mean_and_variance() -> tuple[float, float]:
    e = math.e
    mean = 2.0 / (e - 1.0)
    variance = 2.0 * (e * e - 3.0 * e + 1.0) / (e - 1.0) ** 2
    return mean, variance


def atom_fourier_modulus_squared(frequency: float) -> float:
    if not math.isfinite(frequency):
        raise ValueError("frequency must be finite")
    e = math.e
    numerator = e * e + 1.0 - 2.0 * e * math.cos(frequency)
    denominator = (e - 1.0) ** 2 * (1.0 + frequency * frequency)
    return numerator / denominator


def p_fourier_modulus_squared(frequency: float) -> float:
    value = atom_fourier_modulus_squared(frequency)
    return value * value


def compressed_weight(order: int, frequency: float) -> float:
    validate_order(order)
    if not math.isfinite(frequency):
        raise ValueError("frequency must be finite")
    return frequency * frequency * p_fourier_modulus_squared(frequency / order) ** order


def scaled_weight(order: int, tau: float) -> float:
    validate_order(order)
    if not math.isfinite(tau):
        raise ValueError("tau must be finite")
    _, variance = mean_and_variance()
    return (
        tau
        * tau
        * p_fourier_modulus_squared(tau / math.sqrt(variance * order)) ** order
    )


def gaussian_derivative_weight(tau: float) -> float:
    if not math.isfinite(tau):
        raise ValueError("tau must be finite")
    return tau * tau * math.exp(-(tau * tau))


def gaussian_derivative_autocorrelation(position: float) -> float:
    if not math.isfinite(position):
        raise ValueError("position must be finite")
    return (
        (1.0 - position * position / 2.0)
        * math.exp(-(position * position) / 4.0)
        / (4.0 * math.sqrt(math.pi))
    )


def simpson_even(function, *, radius: float = SIMPSON_RADIUS) -> float:
    panels = SIMPSON_PANELS
    step = 2.0 * radius / panels
    total = function(-radius) + function(radius)
    for index in range(1, panels):
        point = -radius + index * step
        total += (4.0 if index % 2 else 2.0) * function(point)
    return total * step / 3.0


def normalized_energy_constant(order: int) -> float:
    return simpson_even(lambda tau: scaled_weight(order, tau)) / (2.0 * math.pi)


def normalized_autocorrelation(order: int, position: float) -> float:
    return simpson_even(
        lambda tau: scaled_weight(order, tau) * math.cos(tau * position)
    ) / (2.0 * math.pi)


def weight_control_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for order in ORDERS:
        errors = [
            abs(scaled_weight(order, tau) - gaussian_derivative_weight(tau))
            for tau in TAUS
        ]
        rows.append(
            {
                "order": order,
                "maximum_sample_weight_error": max(errors),
                "normalized_energy_constant": normalized_energy_constant(order),
                "normalized_energy_limit": 1.0 / (4.0 * math.sqrt(math.pi)),
            }
        )
    return rows


def autocorrelation_control_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for order in ORDERS:
        values = {
            format(position, ".12g"): normalized_autocorrelation(order, position)
            for position in AUTOCORRELATION_POINTS
        }
        errors = [
            abs(
                values[format(position, ".12g")]
                - gaussian_derivative_autocorrelation(position)
            )
            for position in AUTOCORRELATION_POINTS
        ]
        rows.append(
            {
                "order": order,
                "values": values,
                "maximum_sample_error": max(errors),
            }
        )
    return rows


def nonmonotonicity_control() -> dict[str, float]:
    frequency = 4.0 * math.pi
    first = compressed_weight(1, frequency)
    second = compressed_weight(2, frequency)
    late = compressed_weight(128, frequency)
    if not second < first < late < frequency * frequency:
        raise AssertionError("declared nonmonotonicity control failed")
    return {
        "frequency": frequency,
        "weight_order_1": first,
        "weight_order_2": second,
        "weight_order_128": late,
        "pointwise_limit": frequency * frequency,
    }


def critical_scale_rows() -> list[dict[str, float]]:
    _, variance = mean_and_variance()
    rows: list[dict[str, float]] = []
    for log_x in (100.0, 400.0, 1600.0):
        log_t = math.sqrt(math.log(2.0) * log_x)
        log_order = math.log(variance) + 2.0 * log_t
        rows.append(
            {
                "log_X": log_x,
                "log_T_star": log_t,
                "log_m_star": log_order,
                "log_m_over_log_X": log_order / log_x,
            }
        )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    mean, variance = mean_and_variance()
    if not 0.0 < variance < 1.0:
        raise AssertionError("variance left its declared range")
    weight_rows = weight_control_rows()
    autocorrelation_rows = autocorrelation_control_rows()
    if not (
        weight_rows[-1]["maximum_sample_weight_error"]
        < weight_rows[0]["maximum_sample_weight_error"]
    ):
        raise AssertionError("scaled weight control did not improve")
    if not (
        autocorrelation_rows[-1]["maximum_sample_error"]
        < autocorrelation_rows[0]["maximum_sample_error"]
    ):
        raise AssertionError("autocorrelation control did not improve")
    if (
        not critical_scale_rows()[-1]["log_m_over_log_X"]
        < critical_scale_rows()[0]["log_m_over_log_X"]
    ):
        raise AssertionError("critical order failed its subpower regression")

    return {
        "source_contract": {
            "ladder_commit": LADDER_COMMIT,
            "ladder_git_blobs": LADDER_BLOBS,
            "renormalization_commit": FLOW_COMMIT,
            "renormalization_git_blobs": FLOW_BLOBS,
        },
        "exact_bridge": {
            "compressed_density": "Q_m(x)=m*P^{*m}(m*x)",
            "compressed_detector": "J_m^c(x)=m^2*K_m(m*x)",
            "centered_detector": "J_m^G(y)=m*sigma^2*K_m(m*mu+sigma*sqrt(m)*y)",
            "detector_scaling": "J_m^c(x)=(m/sigma^2)*J_m^G(sqrt(m)*(x-mu)/sigma)",
            "autocorrelation_scaling": "R_m^c(sigma*v/sqrt(m))=(m^(3/2)/sigma^3)*R_m^G(v)",
        },
        "constants": {
            "mean": mean,
            "variance": variance,
            "sigma": math.sqrt(variance),
            "gaussian_energy": 1.0 / (4.0 * math.sqrt(math.pi)),
            "gaussian_node": math.sqrt(2.0),
        },
        "spectral_microscope": {
            "scaled_weight": "tilde_w_m(tau)=(sigma^2/m)w_m(sqrt(m)*tau/sigma)",
            "limit": "tau^2*exp(-tau^2), locally uniformly and in L1",
            "exact_energy_identity": "(sigma^3/m^(3/2))*E_m(X)=(2pi)^-1 integral tilde_w_m(tau)|D_X(sqrt(m)*tau/sigma)|^2 dtau",
            "critical_order": "m_*(X)=ceil(sigma^2*exp(2*sqrt(log(2)*log(X))))=X^o(1)",
        },
        "weight_control_rows": weight_rows,
        "autocorrelation_control_rows": autocorrelation_rows,
        "nonmonotonicity_control": nonmonotonicity_control(),
        "critical_scale_rows": critical_scale_rows(),
        "proof_ledger": {
            "exact_scaling_bridge": "PROVED EXACT",
            "scaled_weight_and_autocorrelation_limits": "PROVED FROM THE PINNED RENORMALIZATION THEOREM",
            "mesoscopic_sign_tubes_away_from_the_gaussian_node": "PROVED",
            "norm_and_jordan_asymptotics": "PROVED FROM THE EXACT BRIDGE",
            "pointwise_order_monotonicity": "FALSE",
            "growing_order_beta_estimate": "NOT PROVED",
            "uniform_growing_order_RH_equivalence": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "orders": list(ORDERS),
            "weight_samples_per_order": len(TAUS),
            "autocorrelation_samples_per_order": len(AUTOCORRELATION_POINTS),
            "simpson_panels": SIMPSON_PANELS,
            "simpson_radius": SIMPSON_RADIUS,
            "zeta_zeros": 0,
            "primes": 0,
            "curves": 0,
            "random_samples": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    payload = run(check_sources=not args.no_source_check)
    if args.write_json is not None:
        args.write_json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    elif not args.check:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
