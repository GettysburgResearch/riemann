#!/usr/bin/env python3
"""Bounded replay for the variational probability-carrier optimum."""

from __future__ import annotations

import argparse
import cmath
import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_variational_probability_carrier_optimum.json"

SOURCE_COMMIT = "52577ce7fb5840a93102b4808c87b1b2d6e8c304"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_UNIFORM_MOVING_CARRIER_BETA_CRITERION.md": "a37f8ee6ccd3624b4ee6b0a80a04d2b9e56739a7",
    "research/l-families/atlas/function_field/ffps_uniform_moving_carrier_beta_criterion.py": "6b645c0f1b8c7cbce941c19dc2e426a9f085ada6",
    "research/l-families/atlas/function_field/ffps_uniform_moving_carrier_beta_criterion.json": "6633f55a3eafa766fa9cc35d07e7629e46d2deac",
    "tests/test_ffps_uniform_moving_carrier_beta_criterion.py": "378dfcb86286db7166d0c417dda6694bd95be5f7",
}

SUPPORTS = (2.0, 4.0 * math.log(2.0), math.log(64.0))


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


def validate_support(support: float) -> None:
    if not math.isfinite(support) or support <= 0.0:
        raise ValueError("support must be positive and finite")


def optimal_density(support: float, position: float) -> float:
    validate_support(support)
    if not math.isfinite(position):
        raise ValueError("position must be finite")
    if not 0.0 <= position <= support:
        return 0.0
    return 6.0 * position * (support - position) / support**3


def optimal_detector(support: float, position: float) -> float:
    validate_support(support)
    if not math.isfinite(position):
        raise ValueError("position must be finite")
    if not 0.0 < position < support:
        return 0.0
    return 6.0 * (support - 2.0 * position) / support**3


def minimum_diagonal(support: float) -> float:
    validate_support(support)
    return 12.0 / support**3


def competitor_excess(support: float, coefficient: float) -> float:
    validate_support(support)
    if not math.isfinite(coefficient):
        raise ValueError("coefficient must be finite")
    return coefficient**2 * support**5 / 20.0


def autocorrelation(support: float, lag: float) -> float:
    validate_support(support)
    if not math.isfinite(lag):
        raise ValueError("lag must be finite")
    distance = abs(lag)
    if distance > support:
        return 0.0
    return (
        12.0 / support**3
        - 36.0 * distance / support**4
        + 24.0 * distance**3 / support**6
    )


def annulus_node(support: float) -> float:
    validate_support(support)
    return 0.5 * (math.sqrt(3.0) - 1.0) * support


def density_fourier(support: float, frequency: float) -> complex:
    validate_support(support)
    if not math.isfinite(frequency):
        raise ValueError("frequency must be finite")
    scaled = support * frequency
    if abs(scaled) < 1.0e-5:
        centered = 1.0 - scaled**2 / 40.0 + scaled**4 / 4480.0
    else:
        centered = (
            12.0
            * (2.0 * math.sin(scaled / 2.0) - scaled * math.cos(scaled / 2.0))
            / scaled**3
        )
    return cmath.exp(-0.5j * scaled) * centered


def detector_weight(support: float, frequency: float) -> float:
    return frequency**2 * abs(density_fourier(support, frequency)) ** 2


def notch_root(index: int) -> float:
    if not isinstance(index, int) or index < 1:
        raise ValueError("notch index must be a positive integer")
    left = index * math.pi
    right = (index + 0.5) * math.pi

    def equation(value: float) -> float:
        return math.sin(value) - value * math.cos(value)

    left_value = equation(left)
    for _ in range(80):
        middle = 0.5 * (left + right)
        middle_value = equation(middle)
        if left_value * middle_value <= 0.0:
            right = middle
        else:
            left = middle
            left_value = middle_value
    return 0.5 * (left + right)


def support_rows() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for support in SUPPORTS:
        ratio_band = math.exp(support)
        node = annulus_node(support)
        rows.append(
            {
                "support_S": support,
                "ratio_band_exp_S": ratio_band,
                "minimum_diagonal_12_over_S_cubed": minimum_diagonal(support),
                "annulus_node": node,
                "node_over_support": node / support,
                "central_correlation": autocorrelation(support, 0.0),
                "outer_sample_correlation": autocorrelation(support, 0.75 * support),
            }
        )
    return rows


def notch_rows(support: float = 2.0) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for index in range(1, 4):
        root = notch_root(index)
        frequency = 2.0 * root / support
        rows.append(
            {
                "index": float(index),
                "tan_u_equals_u_root": root,
                "detector_frequency": frequency,
                "replayed_weight": detector_weight(support, frequency),
            }
        )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    rows = support_rows()
    if any(row["outer_sample_correlation"] >= 0.0 for row in rows):
        raise AssertionError("variational detector lost its negative annulus")
    notches = notch_rows()
    if any(row["replayed_weight"] > 1.0e-27 for row in notches):
        raise AssertionError("side-notch replay lost its certified roots")

    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "variational_theorem": {
            "admissible_class": "Q in H_0^1(0,S), Q>=0, integral Q=1",
            "unique_minimizer": "Q_*(x)=6*x*(S-x)/S^3",
            "minimum_detector_energy": "integral |D Q_*|^2=12/S^3",
            "pythagorean_identity": "||D Q||_2^2=12/S^3+||D(Q-Q_*)||_2^2",
            "ratio_band_frontier": "minimum diagonal at ratio band R is 12/(log R)^3",
            "RH_criterion": "the beta energy generated by DQ_* is exactly RH-equivalent",
            "local_field": "H_*(t)=6/S^3*(S*A_S(t)-2*B_S(t)) for local beta mass A_S and log-lag moment B_S",
        },
        "autocorrelation": {
            "formula": "12/S^3-36*|u|/S^4+24*|u|^3/S^6 on |u|<=S",
            "primitive_node_ratio": "(sqrt(3)-1)/2",
            "sign_geometry": "positive central tube and negative outer annulus",
        },
        "spectral_notches": {
            "equation": "tan(S*t/2)=S*t/2",
            "interpretation": "infinitely many real side notches do not defeat the prefix-energy RH criterion",
        },
        "support_rows": rows,
        "notch_rows": notches,
        "proof_ledger": {
            "unique_variational_minimizer": "PROVED",
            "exact_autocorrelation_and_sign_geometry": "PROVED",
            "exact_notch_equation": "PROVED",
            "RH_equivalence_from_frozen_universal_gate": "PROVED",
            "beta_energy_estimate": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "support_rows": len(SUPPORTS),
            "notch_roots": 3,
            "bisection_steps_per_root": 80,
            "quadratures": 0,
            "zeta_zeros": 0,
            "primes": 0,
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
