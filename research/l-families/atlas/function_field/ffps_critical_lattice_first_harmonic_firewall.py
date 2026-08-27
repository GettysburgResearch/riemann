#!/usr/bin/env python3
"""Replay for the critical lattice coherent first-harmonic firewall."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "3778eb0f5a80a92a4ca8ffb938f247c79ae6bf37"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_CRITICAL_BETA_SPECTRAL_WITNESS_PRINCIPLE.md": (
        "2e3e0b395e3162e6b73bab5c06ea94e39a360a80"
    ),
    "research/l-families/atlas/function_field/ffps_critical_beta_spectral_witness_principle.py": (
        "488f2fa28524ddf1fbb9c5d16053b6d4cd3cbb74"
    ),
    "research/l-families/atlas/function_field/ffps_critical_beta_spectral_witness_principle.json": (
        "d48dd56093fb4782308bda622f0d5041f2256a16"
    ),
    "tests/test_ffps_critical_beta_spectral_witness_principle.py": (
        "71c7b5222b73cd2bd5d8649b3cacf208fa68c2a5"
    ),
    "research/l-families/atlas/function_field/FFPS_INFINITE_DYADIC_BOX_BANDPASS_SMOOTHER.md": (
        "01d3ea427883fb761f6301f71d9dd05c552c5056"
    ),
    "research/l-families/atlas/function_field/ffps_infinite_dyadic_box_bandpass_smoother.py": (
        "2ba0f30c9bd67cdb01af639d320daf8133b5bb77"
    ),
    "research/l-families/atlas/function_field/ffps_infinite_dyadic_box_bandpass_smoother.json": (
        "7a38b5f943a8dc1c0afde8d1cc91f35118b767ca"
    ),
    "tests/test_ffps_infinite_dyadic_box_bandpass_smoother.py": (
        "d6a30d654d46edfa01add55cec55b0b3253a12b0"
    ),
}

EXCEPTIONAL_PRIME = 67
TOY_PRIME = 5
COEFFICIENT_CAP = 625

Gaussian = tuple[Fraction, Fraction]


def check_source_contract() -> None:
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
            raise RuntimeError(f"source blob mismatch: {path}")


def validate_positive_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{label} must be a positive integer")


def mobius(value: int) -> int:
    validate_positive_integer(value, "value")
    remaining = value
    parity = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            parity += 1
            if remaining % divisor == 0:
                return 0
        divisor += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def beta(value: int, prime: int) -> int:
    validate_positive_integer(value, "value")
    validate_positive_integer(prime, "prime")
    return mobius(value) - (mobius(value // prime) if value % prime == 0 else 0)


def beta_magnitude_decomposition(value: int, prime: int) -> int:
    direct = mobius(value) ** 2
    if value % prime == 0:
        direct += mobius(value // prime) ** 2
    return direct


def magnitude_identity_panel(prime: int, cap: int) -> dict[str, object]:
    validate_positive_integer(prime, "prime")
    validate_positive_integer(cap, "cap")
    rows: list[tuple[int, int]] = []
    for value in range(1, cap + 1):
        magnitude = abs(beta(value, prime))
        decomposition = beta_magnitude_decomposition(value, prime)
        if magnitude != decomposition:
            raise ArithmeticError("beta magnitude decomposition changed")
        rows.append((value, magnitude))
    explicit_layers = [abs(beta(2 * prime**exponent, prime)) for exponent in range(4)]
    payload = json.dumps(rows, separators=(",", ":"))
    return {
        "prime": prime,
        "cap": cap,
        "identity": "|beta_q(n)|=mu(n)^2+1_(q|n)mu(n/q)^2",
        "dirichlet_series": "(1+q^(-s))*zeta(s)/zeta(2s)",
        "mean_density": "(1+1/q)/zeta(2)",
        "explicit_layers_on_residue_2": explicit_layers,
        "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
    }


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gnorm2(value: Gaussian) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def coherent_four_cell_panel() -> dict[str, object]:
    phases = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
        (Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    coefficients = (Fraction(1), Fraction(2), Fraction(4), Fraction(8))
    amplitude = (Fraction(0), Fraction(0))
    for coefficient, phase in zip(coefficients, phases, strict=True):
        amplitude = gadd(amplitude, gmul((coefficient, Fraction(0)), phase))
    coordinate_square = gnorm2(amplitude)
    vector_square = sum(
        (coefficient * coefficient for coefficient in coefficients), Fraction(0)
    )
    rayleigh_lower_bound = coordinate_square / vector_square
    if coordinate_square != 45 or vector_square != 85:
        raise ArithmeticError("coherent four-cell control changed")
    return {
        "phase_cycle": [[str(real), str(imag)] for real, imag in phases],
        "positive_coefficients": [str(value) for value in coefficients],
        "first_harmonic_amplitude": [str(value) for value in amplitude],
        "coordinate_square": str(coordinate_square),
        "coefficient_l2_square": str(vector_square),
        "single_row_rayleigh_lower_bound": str(rayleigh_lower_bound),
        "purpose": (
            "finite exact normalization control only; the theorem uses the "
            "squarefree-density asymptotic rather than this toy row"
        ),
    }


def growing_notch_frontier_panel() -> dict[str, object]:
    slopes = (
        Fraction(0),
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(3, 4),
    )
    rows = [
        {
            "r_over_logX_over_loglogX": str(slope),
            "coherent_power_exponent": str(1 - 2 * slope),
        }
        for slope in slopes
    ]
    return {
        "rows": rows,
        "law": (
            "if r(X)=(c+o(1))*log(X)/loglog(X), the coherent first "
            "harmonic has size X^(1-2c+o(1))"
        ),
        "subpower_threshold": "c>=1/2",
        "fixed_detector_warning": (
            "the RH-equivalent detector requires fixed r; a moving r(X) is "
            "only a source-blind suppression diagnostic"
        ),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imports": (
                "single weighted spectral witness theorem and exact order-r "
                "zero of the infinite-smoother kernel at frequency zero"
            ),
        },
        "literal_magnitude_source": magnitude_identity_panel(
            EXCEPTIONAL_PRIME, COEFFICIENT_CAP
        ),
        "toy_magnitude_source": magnitude_identity_panel(TOY_PRIME, COEFFICIENT_CAP),
        "first_harmonic": {
            "frequency": "t_(1,X)=2*pi/(log(X)+S+delta)",
            "magnitude_dirichlet_polynomial": (
                "P_X(t)=sum_(n<=X)|beta(n)|*n^(-1/2-it)"
            ),
            "asymptotic": ("P_X(t_(1,X))=2*(1+1/67)/zeta(2)*sqrt(X)*(1+o(1))"),
            "kernel_constant": ("K_0=Khat_bd(0)=3*(1-sqrt(2))^2*(log(2))^2"),
            "weighted_coordinate": (
                "|Bhat(t_1)|^2|P_X(t_1)|^2/L_X"
                "~4*((1+1/67)/zeta(2))^2*K_0^2*(2*pi)^(2r)"
                "*X/L_X^(2r+1)"
            ),
            "fixed_r_verdict": "X^(1-o(1)) for every fixed notch order r",
        },
        "operator_norm_firewall": {
            "magnitude_vector": "v_n=|beta(n)|/sqrt(n)",
            "vector_square_upper_bound": "sum_(n<=X)|beta(n)|^2/n<=4*(1+log X)",
            "gram_lower_bound": ("lambda_max(G_X)>=constant_r*X/(log X)^(2r+2)"),
            "verdict": (
                "the subpower-rank critical Gram has power-size operator norm; "
                "low rank or source-blind positivity cannot prove the beta bound"
            ),
        },
        "growing_notch": growing_notch_frontier_panel(),
        "bounded_replay": {
            "coherent_four_cell": coherent_four_cell_panel(),
        },
        "scope": {
            "literal_beta_magnitudes_preserved": True,
            "mobius_signs_preserved": False,
            "countermodel_is_source_blind": True,
            "actual_beta_witness_estimated": False,
            "moving_notch_is_fixed_detector": False,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "coefficient_identity_cap": COEFFICIENT_CAP,
            "toy_fourier_cells": 4,
            "primes_enumerated": 0,
            "zeta_zeros": 0,
            "floating_point_operations": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    if not args.check and not args.write_json:
        print(rendered, end="")


if __name__ == "__main__":
    main()
