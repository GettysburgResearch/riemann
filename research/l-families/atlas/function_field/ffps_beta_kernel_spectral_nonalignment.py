#!/usr/bin/env python3
"""Bounded replay for beta-kernel spectral nonalignment theorems."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_beta_kernel_spectral_nonalignment.json"

SOURCE_COMMITS = {
    "b870366141fe8d5f43d5b81f6e50a67d2a888070": {
        "research/l-families/atlas/function_field/FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md": "bf4d1baa231086ba7e8eafaecd39730d83c9201a",
        "research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.py": "2180038eef7ab639477879e806bb13fdbea0b1ec",
        "research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.json": "c86a40d6a930603b3897ad12a28acc5f21e80dd6",
        "tests/test_ffps_mollified_beta_boundary_shell_identity.py": "5e7de97284878c6f9b5a5ac43b83ccaf9528e242",
    },
    "05aaabe69060c24c8db4ca33c350e109231960f1": {
        "research/l-families/atlas/function_field/FFPS_BANDPASS_BETA_ENERGY_LADDER.md": "0ac23a6c384a896e50fed21ca7d8bf079c338ac0",
        "research/l-families/atlas/function_field/ffps_bandpass_beta_energy_ladder.py": "9ca6db9ad6b0149936efbd0e99f799d89f3cc53a",
        "research/l-families/atlas/function_field/ffps_bandpass_beta_energy_ladder.json": "ff568b48100048f6ad963c7afa23c4ac04c3d291",
        "tests/test_ffps_bandpass_beta_energy_ladder.py": "6b45ddd02148c437bba375d6dbaf753c938e3375",
    },
    "3a1d92b57b6234c046c2abf42d9ab15d03173838": {
        "research/l-families/atlas/function_field/FFPS_TRUNCATED_BETA_ZERO_TUBE_RESIDUE_LAW.md": "5d6c9377ee5d859c0890f20e3c118a3f228a9dc3",
        "research/l-families/atlas/function_field/ffps_truncated_beta_zero_tube_residue_law.py": "a771ebc67c6e48e805112f769f28b7ae3bea2801",
        "research/l-families/atlas/function_field/ffps_truncated_beta_zero_tube_residue_law.json": "51b9c291afe89770b61c8ae4f8d30705619eadd9",
        "tests/test_ffps_truncated_beta_zero_tube_residue_law.py": "8ba42f8a5b514473215c122f2c1a035177e6da93",
    },
}

WINDOW_REPLAY_HEIGHTS = (
    Fraction(1, 10),
    Fraction(1),
    Fraction(10),
    Fraction(1000),
)
LATTICE_REPLAY_CAP = 128
UNIVERSAL_WEIGHT_SAMPLES = (
    Fraction(-100),
    Fraction(-3, 2),
    Fraction(-1, 100),
    Fraction(1, 100),
    Fraction(3, 2),
    Fraction(100),
)

Q2 = tuple[Fraction, Fraction]


def check_source_blobs() -> None:
    for commit, rows in SOURCE_COMMITS.items():
        for path, expected in rows.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def q2_add(left: Q2, right: Q2) -> Q2:
    return left[0] + right[0], left[1] + right[1]


def q2_mul(left: Q2, right: Q2) -> Q2:
    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def q2_convolve(left: tuple[Q2, ...], right: tuple[Q2, ...]) -> tuple[Q2, ...]:
    if not left or not right:
        raise ValueError("polynomials must be nonempty")
    result = [(Fraction(0), Fraction(0))] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            index = left_index + right_index
            result[index] = q2_add(result[index], q2_mul(left_value, right_value))
    return tuple(result)


def boundary_shift_coefficients() -> tuple[Q2, ...]:
    """Coefficients of (1-z)^2(1-sqrt(2)z)^2 in Q(sqrt(2))."""

    rational_difference = (
        (Fraction(1), Fraction(0)),
        (Fraction(-2), Fraction(0)),
        (Fraction(1), Fraction(0)),
    )
    sqrt_two_difference = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-2)),
        (Fraction(2), Fraction(0)),
    )
    return q2_convolve(rational_difference, sqrt_two_difference)


def tail_common_numerator() -> tuple[Fraction, ...]:
    """Numerator over s^2(2s-1) of 13/s+3/s^2-8/(s-1/2)."""

    # Coefficients are in increasing powers of s.
    term_13 = (Fraction(0), Fraction(-13), Fraction(26))
    term_3 = (Fraction(-3), Fraction(6), Fraction(0))
    term_minus_8 = (Fraction(0), Fraction(0), Fraction(-16))
    return tuple(
        sum(values, Fraction(0)) for values in zip(term_13, term_3, term_minus_8)
    )


def factored_tail_numerator() -> tuple[Fraction, ...]:
    """Coefficients of (s-1)(10s+3)."""

    return Fraction(-3), Fraction(-7), Fraction(10)


def frozen_boundary_amplitude_order(lattice_index: int) -> int:
    if isinstance(lattice_index, bool) or not isinstance(lattice_index, int):
        raise TypeError("lattice_index must be an integer")
    return 0 if lattice_index == 0 else 2


def scaled_channel_amplitude_order(lattice_index: int) -> int:
    if isinstance(lattice_index, bool) or not isinstance(lattice_index, int):
        raise TypeError("lattice_index must be an integer")
    return 1 if lattice_index == 0 else 3


def window_scale(height: Fraction) -> Fraction:
    if isinstance(height, bool) or not isinstance(height, Fraction) or height <= 0:
        raise ValueError("height must be a positive Fraction")
    return Fraction(1, 1) / (1 + height)


def window_certificate(height: Fraction) -> dict[str, str | bool]:
    scale = window_scale(height)
    scaled_height = scale * height
    return {
        "height": str(height),
        "scale": str(scale),
        "scaled_height": str(scaled_height),
        "scaled_height_below_one": scaled_height < 1,
        "support_endpoint_in_log2_units": str(5 * scale),
        "carrier_zero_free_open_rh_strip": scale <= 1,
    }


def sqrt_two_integer_relation(left: int, right: int) -> bool:
    """Necessary squared equality for left=right*sqrt(2)."""

    if (
        isinstance(left, bool)
        or not isinstance(left, int)
        or isinstance(right, bool)
        or not isinstance(right, int)
    ):
        raise TypeError("inputs must be integers")
    return left * left == 2 * right * right


def bounded_nonzero_lattice_intersections(cap: int = LATTICE_REPLAY_CAP) -> int:
    if isinstance(cap, bool) or not isinstance(cap, int) or not 1 <= cap <= 512:
        raise ValueError("cap must lie in [1,512]")
    return sum(
        sqrt_two_integer_relation(left, right)
        for left in range(-cap, cap + 1)
        for right in range(-cap, cap + 1)
        if left != 0 and right != 0
    )


def universal_piece_integrals() -> tuple[Fraction, Fraction]:
    """Exact masses from the endpoint antiderivatives of the two pieces."""

    # On y in (-1,0), e^y(y+2) has antiderivative e^y(y+1): mass 1.
    # On y in (0,1), -y e^y has antiderivative -e^y(y-1): mass -1.
    return Fraction(1), Fraction(-1)


def universal_weight(t: float) -> float:
    if not math.isfinite(t):
        raise ValueError("t must be finite")
    numerator = 16.0 * t * t
    spectral_floor = math.sinh(0.5) ** 2 + math.sin(t / 2.0) ** 2
    return numerator * spectral_floor**2 / (1.0 + t * t) ** 2


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    coefficients = boundary_shift_coefficients()
    if coefficients != (
        (Fraction(1), Fraction(0)),
        (Fraction(-2), Fraction(-2)),
        (Fraction(3), Fraction(4)),
        (Fraction(-4), Fraction(-2)),
        (Fraction(2), Fraction(0)),
    ):
        raise AssertionError("boundary shift coefficients drifted")
    if tail_common_numerator() != factored_tail_numerator():
        raise AssertionError("tail rational factorization failed")
    if bounded_nonzero_lattice_intersections() != 0:
        raise AssertionError("unexpected two-channel lattice collision")
    if sum(universal_piece_integrals(), Fraction(0)) != 0:
        raise AssertionError("universal kernel is not mean zero")
    for sample in UNIVERSAL_WEIGHT_SAMPLES:
        if universal_weight(float(sample)) <= 0:
            raise AssertionError("universal weight lost strict positivity")

    return {
        "frozen_boundary": {
            "L": "log(2)",
            "causal_formula": "K_bd=(1-tau_L)^2(1-sqrt(2)tau_L)^2[1_(t>=0)(13+3t-8exp(t/2))]",
            "laplace_transform": "(1-2^(-s))^2(1-2^(1/2-s))^2(s-1)(10s+3)/(2s^2(s-1/2))",
            "removable_values": {
                "s=0": "3(1-sqrt(2))^2(log(2))^2 != 0",
                "s=1/2": "simple zero after removing the apparent pole",
            },
            "complete_zero_divisor": {
                "s=2pi*i*k/L, k!=0": "multiplicity 2",
                "s=1/2+2pi*i*k/L, k!=0": "multiplicity 2",
                "s=1/2": "multiplicity 1",
                "s=1": "multiplicity 1",
                "s=-3/10": "multiplicity 1",
            },
            "real_fourier_zeros": "t=2pi*k/L for nonzero integers k; amplitude order 2 and weight order 4",
            "fourier_weight": "4sin^4(Lt/2)(3-2sqrt(2)cos(Lt))^2(t^2+1)(100t^2+9)/(t^4(t^2+1/4))",
            "weight_at_zero": "9(1-sqrt(2))^4L^4",
            "shift_no_go": "time translation, finite translate polynomials, finite differences, and convolution multipliers cannot remove an inherited K_bd zero",
        },
        "finite_window_scalar_repair": {
            "height": "T>0",
            "scale": "a_T=1/(1+T)",
            "kernel": "C_T=Delta_(a_T L)[K_bd(./a_T)]",
            "support": "[0,5a_T L]",
            "fourier_transform": "(1-exp(-i a_T L t))/L*K_bd_hat(a_T t)",
            "real_zero_set": "2pi*Z/(a_T L); amplitude order 1 at zero and 3 elsewhere",
            "window_positivity": "|C_T_hat(t)|^2>0 for 0<|t|<=T",
            "parameter_dependence": "depends only on T, never on a zeta zero or zero census",
            "carrier": "zero-free in 0<Re(s)<1/2",
            "replay_certificates": [
                window_certificate(height) for height in WINDOW_REPLAY_HEIGHTS
            ],
        },
        "global_direct_sum_repair": {
            "channels": ["C_1", "C_(1/sqrt(2))"],
            "weight": "w_direct(t)=|C_1_hat(t)|^2+|C_(1/sqrt(2))_hat(t)|^2",
            "common_real_zeros": "{0}",
            "positivity": "w_direct(t)>0 for every real t!=0",
            "proof": "a nonzero common zero would give k=m*sqrt(2); parity descent forbids k^2=2m^2",
            "carrier": "both scalar channel carriers are zero-free in 0<Re(s)<1/2",
            "scope": "a vector/direct-sum energy or sum of two Perron inners, not one scalar autocorrelation",
        },
        "universal_scalar_kernel": {
            "tent": "Phi(x)=exp(x-1)(1-|x-1|)_+ on [0,2]",
            "kernel": "K_*(x)=Phi'(x) almost everywhere",
            "piecewise": {
                "0<x<1": "exp(x-1)(x+1)",
                "1<x<2": "exp(x-1)(1-x)",
                "elsewhere": "0",
            },
            "class": "real compact BV L1-intersect-L2, support [0,2], integral zero",
            "laplace_transform": "4s exp(-s)sinh^2((s-1)/2)/(s-1)^2",
            "carrier_zeros": "s=0 simple and s=1+2pi*i*k (k!=0) double",
            "carrier_strip": "zero-free in 0<Re(s)<1/2",
            "fourier_weight": "16t^2(sinh^2(1/2)+sin^2(t/2))^2/(1+t^2)^2",
            "real_zeros": "t=0 only, of weight order 2",
            "critical_zero_nonalignment": "zeta(1/2)<0 by eta(1/2)>0, so every critical-line zero has nonzero ordinate and positive weight",
            "smoothing_ladder": "K_m=D(Phi^(*m)) has the same real zero set and weight decay O(|t|^(2-4m))",
        },
        "zero_tube_consequence": {
            "finite_window": "the scalar C_T discharges w(gamma)>0 on the whole guarded window",
            "all_height_scalar": "K_* discharges w(gamma)>0 at every critical-line zero",
            "all_height_source_locked": "the two-channel direct sum discharges nonalignment globally",
            "what_remains": "the O_T(1/c) Perron estimate, contour displacement, height-uniform tail, and any simplicity or RH conclusion remain unproved",
        },
        "resource_caps": {
            "zeta_zeros": 0,
            "numerical_zeta_value_evaluations": 0,
            "primes": 0,
            "curves": 0,
            "largest_lattice_index_replayed": LATTICE_REPLAY_CAP,
            "window_certificates": len(WINDOW_REPLAY_HEIGHTS),
            "universal_weight_samples": len(UNIVERSAL_WEIGHT_SAMPLES),
        },
        "source_contract": {
            "commits": SOURCE_COMMITS,
            "imported_results": [
                "the exact compact boundary kernel K_bd and its Laplace multiplier",
                "the fixed band-pass transform and RH-strip carrier fence",
                "the local beta zero-tube residue law for a fixed compact band-pass kernel",
            ],
        },
        "scope": {
            "exact_transform_and_zero_classification": True,
            "zero_dependent_kernel_choice": False,
            "zeta_zero_computation": False,
            "perron_bound_proved": False,
            "simplicity_proved": False,
            "rh_proved": False,
            "grh_proved": False,
        },
    }


def canonical_text(result: dict[str, object]) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    args = parser.parse_args()
    result = run(check_sources=not args.no_source_check)
    text = canonical_text(result)
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
            raise RuntimeError("canonical JSON drift")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
