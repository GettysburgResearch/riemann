#!/usr/bin/env python3
"""Bounded replay for compact-kernel carrier zero flipping."""

from __future__ import annotations

import argparse
import cmath
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_compact_kernel_carrier_zero_flip.json"

SOURCE_COMMIT = "b0892f2ac6af5bc97010bc281118601547243148"
FROZEN_SOURCES = {
    "research/l-families/atlas/function_field/FFPS_BETA_KERNEL_CARRIER_CHIRALITY.md": (
        "71449163391c3de989fecf9e60c4f77f3efae6c6"
    ),
    "research/l-families/atlas/function_field/ffps_beta_kernel_carrier_chirality.py": (
        "da6c4702268d9211c382ee9a0454c81fa2ad60f9"
    ),
    "research/l-families/atlas/function_field/ffps_beta_kernel_carrier_chirality.json": (
        "66fe36ecde1acf70a83d0d67e784153c64bd6ce9"
    ),
    "tests/test_ffps_beta_kernel_carrier_chirality.py": (
        "365f8c2f109433ce13e419c03a82669194e7d48a"
    ),
}

TOY_WEIGHTS = (Fraction(3, 4), Fraction(-7, 4), Fraction(1))
TOY_EXPONENTIAL_ROOT = Fraction(3, 4)
FREQUENCY_SAMPLES = (
    Fraction(-20),
    Fraction(-3, 2),
    Fraction(-1, 100),
    Fraction(1, 100),
    Fraction(3, 2),
    Fraction(20),
)
COMPLEX_ZERO_SAMPLES = (
    (Fraction(1, 4), Fraction(3, 2)),
    (Fraction(2, 3), Fraction(-5, 4)),
    (Fraction(7, 5), Fraction(1, 3)),
)


def check_source_blobs() -> None:
    for path, expected in FROZEN_SOURCES.items():
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


def validate_complex(value: complex, name: str) -> None:
    if not isinstance(value, (complex, float, int)) or isinstance(value, bool):
        raise TypeError(f"{name} must be complex")
    value = complex(value)
    if not math.isfinite(value.real) or not math.isfinite(value.imag):
        raise ValueError(f"{name} must be finite")


def zero_flip_multiplier(zero: complex, spectral_point: complex) -> complex:
    """Multiplier moving zero z to -conj(z)."""

    validate_complex(zero, "zero")
    validate_complex(spectral_point, "spectral_point")
    zero = complex(zero)
    spectral_point = complex(spectral_point)
    if zero.real == 0.0:
        raise ValueError("the flipped zero must lie off the imaginary axis")
    if spectral_point == zero:
        raise ValueError(
            "multiplier is represented removably only after multiplication"
        )
    return (spectral_point + zero.conjugate()) / (spectral_point - zero)


def conjugate_pair_multiplier(zero: complex, spectral_point: complex) -> complex:
    validate_complex(zero, "zero")
    zero = complex(zero)
    if zero.imag == 0.0:
        raise ValueError("use one real zero flip for a real zero")
    first = zero_flip_multiplier(zero, spectral_point)
    second = zero_flip_multiplier(zero.conjugate(), spectral_point)
    return first * second


def toy_root_polynomial(value: Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, Fraction):
        raise TypeError("value must be a Fraction")
    first, second, third = TOY_WEIGHTS
    return first + second * value + third * value * value


def toy_transform(spectral_point: complex) -> complex:
    validate_complex(spectral_point, "spectral_point")
    spectral_point = complex(spectral_point)
    if spectral_point == 0.0:
        return 0.0j
    exponential = cmath.exp(-spectral_point)
    polynomial = sum(
        float(weight) * exponential**index for index, weight in enumerate(TOY_WEIGHTS)
    )
    return (1.0 - exponential) * polynomial / spectral_point


def toy_flipped_transform(spectral_point: complex) -> complex:
    zero = complex(math.log(4.0 / 3.0), 0.0)
    return toy_transform(spectral_point) * zero_flip_multiplier(zero, spectral_point)


def control_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    maximum_single_error = 0.0
    maximum_pair_error = 0.0
    maximum_toy_error = 0.0
    for frequency_fraction in FREQUENCY_SAMPLES:
        frequency = float(frequency_fraction)
        spectral_point = complex(0.0, frequency)
        original = toy_transform(spectral_point)
        flipped = toy_flipped_transform(spectral_point)
        maximum_toy_error = max(maximum_toy_error, abs(abs(original) - abs(flipped)))
        for real_fraction, imag_fraction in COMPLEX_ZERO_SAMPLES:
            zero = complex(float(real_fraction), float(imag_fraction))
            single = zero_flip_multiplier(zero, spectral_point)
            pair = conjugate_pair_multiplier(zero, spectral_point)
            maximum_single_error = max(maximum_single_error, abs(abs(single) - 1.0))
            maximum_pair_error = max(maximum_pair_error, abs(abs(pair) - 1.0))
        rows.append(
            {
                "frequency": str(frequency_fraction),
                "toy_original_weight": abs(original) ** 2,
                "toy_flipped_weight": abs(flipped) ** 2,
                "toy_weight_error": abs(abs(original) ** 2 - abs(flipped) ** 2),
            }
        )
    if max(maximum_single_error, maximum_pair_error, maximum_toy_error) > 1e-12:
        raise ArithmeticError("zero-flip unit-modulus replay drifted")
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    if sum(TOY_WEIGHTS, Fraction(0)) != 0:
        raise ArithmeticError("toy kernel lost mean zero")
    if toy_root_polynomial(TOY_EXPONENTIAL_ROOT) != 0:
        raise ArithmeticError("toy carrier root drifted")
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "frozen_blobs": FROZEN_SOURCES,
        },
        "finite_zero_flip": {
            "input": "real compact BV K on [0,L], F(z)=0, Re(z)!=0",
            "primitive": (
                "h_z(x)=exp(z*x) integral_0^x exp(-z*u)K(u)du; K^[z]=K+2Re(z)h_z"
            ),
            "transform": "F^[z](s)=F(s)(s+conj(z))/(s-z)",
            "zero_motion": "z -> -conj(z)",
            "invariants": [
                "support [0,L]",
                "compact BV regularity",
                "zero mean whenever the input has zero mean",
                "Fourier magnitude",
                "autocorrelation",
                "every finite translate Gram energy",
            ],
            "real_output_rule": (
                "flip real zeros singly and nonreal zeros in conjugate pairs"
            ),
        },
        "toy_certificate": {
            "kernel": ("weights (3/4,-7/4,1) on [0,1],[1,2],[2,3]"),
            "mean_zero": True,
            "carrier_polynomial": "(y-1)(y-3/4)",
            "right_half_plane_zero": "z=log(4/3)",
            "flipped_zero": "-log(4/3)",
            "rows": control_rows(),
        },
        "programme_conclusion": {
            "finite_window_surgery": (
                "all carrier zeros in a declared compact substrip can be flipped "
                "left without changing the beta Gram"
            ),
            "full_strip_scope": (
                "a full repair follows when only finitely many carrier zeros lie "
                "in the open consumer strip"
            ),
            "infinite_zero_set": (
                "requires a convergent infinite product or a separate global symmetry"
            ),
        },
        "proof_ledger": {
            "constructive_one_zero_flip": "PROVED EXACT",
            "conjugate_pair_real_flip": "PROVED EXACT",
            "support_bv_zero_mean_preservation": "PROVED EXACT",
            "fourier_autocorrelation_energy_invariance": "PROVED EXACT",
            "finite_carrier_defect_repair": "PROVED EXACT",
            "arbitrary_infinite_zero_flip": "NOT PROVED",
            "one_sided_jordan_mass_invariance": "FALSE IN GENERAL / NOT CLAIMED",
            "any_beta_energy_estimate": "NOT PROVED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "toy_intervals": len(TOY_WEIGHTS),
            "frequency_samples": len(FREQUENCY_SAMPLES),
            "complex_zero_samples": len(COMPLEX_ZERO_SAMPLES),
            "zeta_zeros": 0,
            "primes": 0,
            "random_samples": 0,
        },
    }


def canonical_text(result: dict[str, object]) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    text = canonical_text(run(check_sources=not args.no_source_check))
    if args.write_json:
        args.write_json.write_text(text, encoding="utf-8", newline="\n")
    elif args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
            raise RuntimeError("canonical JSON drift")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
