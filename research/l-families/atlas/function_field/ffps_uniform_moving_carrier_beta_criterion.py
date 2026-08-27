#!/usr/bin/env python3
"""Bounded replay for the uniform moving-carrier beta criterion."""

from __future__ import annotations

import argparse
import cmath
import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_uniform_moving_carrier_beta_criterion.json"

PHASE_COMMIT = "db37529e44bcaada9a6e39dd6cdd73c97dda8b94"
PHASE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_CRITICAL_MOVING_ORDER_PHASE_BOUNDARY.md": "3a9b6ff9af2184bece44449f56e9fe779e9b3de6",
    "research/l-families/atlas/function_field/ffps_critical_moving_order_phase_boundary.py": "c63e3f2645cc18421a6bd511cd4476e14430a592",
    "research/l-families/atlas/function_field/ffps_critical_moving_order_phase_boundary.json": "5e7c572b698d6fd721110d84c8e08f2a468beaa7",
    "tests/test_ffps_critical_moving_order_phase_boundary.py": "2b3288aecca01bce2b6155ab3636b71b516826cd",
}
FLOW_COMMIT = "46ea68808e238b0c9b85050158ba149649b1b37e"
FLOW_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_TILTED_TENT_DETECTOR_RENORMALIZATION_FLOW.md": "6de962fe78c2f77d3f02e0d11f56f7145eb37f93",
    "research/l-families/atlas/function_field/ffps_tilted_tent_detector_renormalization_flow.py": "8b8c5783714661fd9d6f1803263b544e90b82957",
    "research/l-families/atlas/function_field/ffps_tilted_tent_detector_renormalization_flow.json": "7595d5ce5f24524442c6392de6b23073de1f951b",
    "tests/test_ffps_tilted_tent_detector_renormalization_flow.py": "7763de04d6545ed73b397d00e8485f5631c3ae00",
}

TILTS = (1.0, 2.0, 8.0, 64.0)
ORDERS = (1, 2, 8, 64)
SAMPLES = (0.1 + 0.0j, 0.25 + 1.0j, 0.49 + 6.0j)


def check_source_blobs() -> None:
    for commit, blobs in ((PHASE_COMMIT, PHASE_BLOBS), (FLOW_COMMIT, FLOW_BLOBS)):
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


def atom_laplace(tilt: float, value: complex) -> complex:
    if not math.isfinite(tilt) or tilt < 1.0:
        raise ValueError("tilt must be finite and at least one")
    if not math.isfinite(value.real) or not math.isfinite(value.imag):
        raise ValueError("Laplace value must be finite")
    decay = math.exp(-tilt)
    if value == complex(tilt):
        return tilt * decay / (1.0 - decay)
    return tilt * (cmath.exp(-value) - decay) / ((1.0 - decay) * (tilt - value))


def atom_mean(tilt: float) -> float:
    if not math.isfinite(tilt) or tilt < 1.0:
        raise ValueError("tilt must be finite and at least one")
    decay = math.exp(-tilt)
    return 1.0 / (1.0 - decay) - 1.0 / tilt


def carrier_log_modulus(tilt: float, order: int, value: complex) -> float:
    if not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")
    if value == 0:
        return -math.inf
    atom = atom_laplace(tilt, value / order)
    return math.log(abs(value)) + 2.0 * order * math.log(abs(atom))


def carrier(tilt: float, order: int, value: complex) -> complex:
    if not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")
    return value * atom_laplace(tilt, value / order) ** (2 * order)


def limiting_carrier(tilt: float, value: complex) -> complex:
    return value * cmath.exp(-2.0 * atom_mean(tilt) * value)


def atom_fourier_modulus_squared(tilt: float, frequency: float) -> float:
    if not math.isfinite(frequency):
        raise ValueError("frequency must be finite")
    decay = math.exp(-tilt)
    oscillation = 4.0 * decay / (1.0 - decay) ** 2
    return (1.0 + oscillation * math.sin(frequency / 2.0) ** 2) / (
        1.0 + (frequency / tilt) ** 2
    )


def regularity_scale(tilt: float, order: int) -> float:
    if not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")
    decay = math.exp(-tilt)
    coth_half = (1.0 + decay) / (1.0 - decay)
    return order * tilt * (1.0 + coth_half)


def carrier_rows() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for value in SAMPLES:
        moduli = [
            math.exp(carrier_log_modulus(tilt, order, value))
            for tilt in TILTS
            for order in ORDERS
        ]
        rows.append(
            {
                "real_s": value.real,
                "imag_s": value.imag,
                "minimum_sampled_carrier_modulus": min(moduli),
                "maximum_sampled_carrier_modulus": max(moduli),
            }
        )
    return rows


def real_floor_rows() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for value in (0.05, 0.1, 0.25, 0.49):
        floor = value * math.exp(-2.0 * value)
        moduli = [
            abs(carrier(tilt, order, complex(value)))
            for tilt in TILTS
            for order in ORDERS
        ]
        rows.append(
            {
                "real_s": value,
                "universal_probability_floor": floor,
                "minimum_sampled_carrier": min(moduli),
                "minimum_over_floor": min(moduli) / floor,
            }
        )
    return rows


def convergence_rows() -> list[dict[str, float]]:
    value = 0.37 + 1.25j
    rows: list[dict[str, float]] = []
    for tilt in (1.0, 8.0, 64.0):
        limit = limiting_carrier(tilt, value)
        for order in (1, 8, 64, 512):
            relative_error = abs(carrier(tilt, order, value) / limit - 1.0)
            rows.append(
                {
                    "tilt": tilt,
                    "order": float(order),
                    "relative_error_to_order_limit": relative_error,
                }
            )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    rows = carrier_rows()
    if min(row["minimum_sampled_carrier_modulus"] for row in rows) <= 0.0:
        raise AssertionError("sampled carrier compactum lost nonvanishing")
    convergence = convergence_rows()
    for tilt in (1.0, 8.0, 64.0):
        tilt_rows = [row for row in convergence if row["tilt"] == tilt]
        if (
            not tilt_rows[-1]["relative_error_to_order_limit"]
            < tilt_rows[0]["relative_error_to_order_limit"]
        ):
            raise AssertionError("order limit failed to improve")

    return {
        "source_contract": {
            "phase_commit": PHASE_COMMIT,
            "phase_git_blobs": PHASE_BLOBS,
            "renormalization_commit": FLOW_COMMIT,
            "renormalization_git_blobs": FLOW_BLOBS,
        },
        "theorem": {
            "abstract_reverse_gate": "for any moving probability densities Q_X on [0,2], E_{D Q_X}(X)=X^o(1) implies RH",
            "moving_parameters": "a(X)>=1 and integer m(X)>=1",
            "tilted_reverse_gate": "E_{a(X),m(X)}(X)=X^o(1) implies RH with no growth restriction",
            "forward_gate": "RH and a(X)m(X)=X^o(1) imply E_{a(X),m(X)}(X)=X^o(1)",
            "equivalence_region": "a(X)>=1 and a(X)m(X)=X^o(1)",
            "real_carrier_floor": "Jhat_X(sigma)>=sigma*exp(-2sigma) for every sigma>0",
            "fixed_tilt_carrier_compactum": "inf_{m>=1,s in K}|Jhat_{1,m}(s)|>0 for compact K subset 0<Re(s)<1",
        },
        "exact_formulas": {
            "atom_laplace": "a*(exp(-s)-exp(-a))/((1-exp(-a))*(a-s))",
            "carrier": "s*atom_laplace(a,s/m)^(2m)",
            "carrier_zeros": "forced simple zero s=0; nonforced zeros m*(a-2*pi*i*k), k nonzero, multiplicity 2m",
            "variation_scale": "m*a*(1+coth(a/2))",
            "energy_cost": "O_delta((1+log X)*X^(2delta)*variation_scale^4)",
        },
        "carrier_rows": rows,
        "real_floor_rows": real_floor_rows(),
        "order_limit_rows": convergence,
        "proof_ledger": {
            "universal_probability_derivative_reverse_gate": "PROVED",
            "uniform_moving_carrier_lower_bound": "PROVED",
            "prefix_L2_to_beta_Dirichlet_partial_sums": "PROVED",
            "partial_sums_to_holomorphic_continuation": "PROVED",
            "arbitrary_schedule_reverse_RH_implication": "PROVED",
            "subpower_two_parameter_RH_equivalence": "PROVED",
            "moving_energy_estimate": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "tilts": len(TILTS),
            "orders": len(ORDERS),
            "laplace_samples": len(SAMPLES),
            "finite_field_elements": 0,
            "primes": 0,
            "zeta_zeros": 0,
            "random_samples": 0,
            "quadratures": 0,
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
