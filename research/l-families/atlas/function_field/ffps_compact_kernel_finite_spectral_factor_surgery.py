#!/usr/bin/env python3
"""Bounded replay for finite compact-kernel spectral-factor surgery."""

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
OUTPUT = HERE / "ffps_compact_kernel_finite_spectral_factor_surgery.json"

ZERO_FLIP_COMMIT = "011ad6d3f3dade7638f0e5ec9c9d404c889f214d"
CHIRALITY_COMMIT = ZERO_FLIP_COMMIT
SOURCE_BLOBS = {
    (
        ZERO_FLIP_COMMIT,
        "research/l-families/atlas/function_field/FFPS_COMPACT_KERNEL_CARRIER_ZERO_FLIP.md",
    ): "4d08a600643e2189a3ba4c9600d9b88d4de1105c",
    (
        ZERO_FLIP_COMMIT,
        "research/l-families/atlas/function_field/ffps_compact_kernel_carrier_zero_flip.py",
    ): "f3b3759ff49ca1c1343b7eb9539031b650c8f7ac",
    (
        ZERO_FLIP_COMMIT,
        "research/l-families/atlas/function_field/ffps_compact_kernel_carrier_zero_flip.json",
    ): "5ddeb3284e02d41d87583772fb92147e02781578",
    (
        ZERO_FLIP_COMMIT,
        "tests/test_ffps_compact_kernel_carrier_zero_flip.py",
    ): "3e3c6859b9219946ece4a44575c5bdd7fa6b5281",
    (
        CHIRALITY_COMMIT,
        "research/l-families/atlas/function_field/FFPS_BETA_KERNEL_CARRIER_CHIRALITY.md",
    ): "ab15fb0a719545e66417985d32609f9f182e81c9",
    (
        CHIRALITY_COMMIT,
        "research/l-families/atlas/function_field/ffps_beta_kernel_carrier_chirality.py",
    ): "da6c4702268d9211c382ee9a0454c81fa2ad60f9",
    (
        CHIRALITY_COMMIT,
        "research/l-families/atlas/function_field/ffps_beta_kernel_carrier_chirality.json",
    ): "66fe36ecde1acf70a83d0d67e784153c64bd6ce9",
    (
        CHIRALITY_COMMIT,
        "tests/test_ffps_beta_kernel_carrier_chirality.py",
    ): "365f8c2f109433ce13e419c03a82669194e7d48a",
}

Point = tuple[Fraction, Fraction]
RIGHT_REAL: Point = (Fraction(2), Fraction(0))
RIGHT_COMPLEX: Point = (Fraction(1), Fraction(2))
FREQUENCY_SAMPLES = (
    Fraction(-20),
    Fraction(-3, 2),
    Fraction(-1, 100),
    Fraction(1, 100),
    Fraction(3, 2),
    Fraction(20),
)
ALLPASS_ZERO_SAMPLES = (
    (Fraction(1, 4), Fraction(3, 2)),
    (Fraction(2, 3), Fraction(-5, 4)),
    (Fraction(7, 5), Fraction(1, 3)),
)
JORDAN_WEIGHTS = (Fraction(1), Fraction(-4, 3))
JORDAN_EXPONENTIAL_ROOT = Fraction(3, 4)


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def validate_point(point: Point, name: str = "point") -> None:
    if (
        not isinstance(point, tuple)
        or len(point) != 2
        or any(
            isinstance(value, bool) or not isinstance(value, Fraction)
            for value in point
        )
    ):
        raise TypeError(f"{name} must be a pair of Fractions")


def reflect_zero(point: Point) -> Point:
    """Return R(z)=-conj(z) in exact Cartesian coordinates."""

    validate_point(point)
    real, imaginary = point
    return (-real, imaginary)


def conjugate_zero(point: Point) -> Point:
    validate_point(point)
    real, imaginary = point
    return (real, -imaginary)


def format_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def format_point(point: Point) -> str:
    validate_point(point)
    real, imaginary = point
    sign = "+" if imaginary >= 0 else "-"
    return f"{format_fraction(real)}{sign}{format_fraction(abs(imaginary))}i"


def apply_orbit_flow(
    multiplicities: dict[Point, int], source: Point, amount: int
) -> dict[Point, int]:
    """Move `amount` zero copies from source z to R(z)."""

    validate_point(source, "source")
    if source[0] == 0:
        raise ValueError("imaginary-axis zeros are fixed by reflection")
    if isinstance(amount, bool) or not isinstance(amount, int):
        raise TypeError("flow amount must be an integer")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in multiplicities.values()
    ):
        raise ValueError("multiplicities must be nonnegative integers")
    for point in multiplicities:
        validate_point(point, "multiplicity point")
    target = reflect_zero(source)
    result = dict(multiplicities)
    result[source] = result.get(source, 0) - amount
    result[target] = result.get(target, 0) + amount
    if result[source] < 0 or result[target] < 0:
        raise ValueError("flow exceeds the available divisor multiplicity")
    return result


def compose_flow_amounts(first: int, second: int) -> int:
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in (first, second)
    ):
        raise TypeError("flow amounts must be integers")
    return first + second


def conjugate_pair_coefficients(point: Point) -> dict[str, tuple[Fraction, ...]]:
    """Return ascending coefficients for B_z B_conj(z)."""

    validate_point(point)
    real, imaginary = point
    if real == 0:
        raise ValueError("the zero must lie off the imaginary axis")
    if imaginary == 0:
        raise ValueError("a real zero needs only one elementary factor")
    norm = real * real + imaginary * imaginary
    return {
        "numerator": (norm, 2 * real, Fraction(1)),
        "denominator": (norm, -2 * real, Fraction(1)),
    }


def validate_complex(value: complex, name: str) -> None:
    if not isinstance(value, (complex, float, int)) or isinstance(value, bool):
        raise TypeError(f"{name} must be complex")
    value = complex(value)
    if not math.isfinite(value.real) or not math.isfinite(value.imag):
        raise ValueError(f"{name} must be finite")


def allpass_multiplier(zero: complex, spectral_point: complex) -> complex:
    validate_complex(zero, "zero")
    validate_complex(spectral_point, "spectral_point")
    zero = complex(zero)
    spectral_point = complex(spectral_point)
    if zero.real == 0.0:
        raise ValueError("the zero must lie off the imaginary axis")
    if spectral_point == zero:
        raise ValueError("evaluate only after the removable pole is canceled")
    return (spectral_point + zero.conjugate()) / (spectral_point - zero)


def finite_multiplier(zeros: tuple[complex, ...], spectral_point: complex) -> complex:
    validate_complex(spectral_point, "spectral_point")
    product = 1.0 + 0.0j
    for zero in zeros:
        product *= allpass_multiplier(zero, spectral_point)
    return product


def real_preserving_mean_sign(real_flip_count: int) -> int:
    if isinstance(real_flip_count, bool) or not isinstance(real_flip_count, int):
        raise TypeError("real flip count must be an integer")
    return -1 if real_flip_count % 2 else 1


def jordan_root_polynomial(value: Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, Fraction):
        raise TypeError("value must be a Fraction")
    first, second = JORDAN_WEIGHTS
    return first + second * value


def jordan_transform(spectral_point: complex) -> complex:
    validate_complex(spectral_point, "spectral_point")
    spectral_point = complex(spectral_point)
    if spectral_point == 0.0:
        return complex(float(sum(JORDAN_WEIGHTS, Fraction(0))), 0.0)
    exponential = cmath.exp(-spectral_point)
    polynomial = 1.0 - (4.0 / 3.0) * exponential
    return (1.0 - exponential) * polynomial / spectral_point


def jordan_flipped_transform(spectral_point: complex) -> complex:
    zero = complex(math.log(4.0 / 3.0), 0.0)
    return jordan_transform(spectral_point) * allpass_multiplier(zero, spectral_point)


def divisor_flow_control() -> dict[str, object]:
    right_real = RIGHT_REAL
    left_real = reflect_zero(right_real)
    right_complex = RIGHT_COMPLEX
    left_complex = reflect_zero(right_complex)
    right_conjugate = conjugate_zero(right_complex)
    left_conjugate = reflect_zero(right_conjugate)
    initial = {
        right_real: 3,
        left_real: 1,
        right_complex: 2,
        left_complex: 0,
        right_conjugate: 2,
        left_conjugate: 0,
    }
    real_first = apply_orbit_flow(initial, right_real, 1)
    real_sequential = apply_orbit_flow(real_first, right_real, 1)
    real_direct = apply_orbit_flow(initial, right_real, compose_flow_amounts(1, 1))
    if real_sequential != real_direct:
        raise ArithmeticError("flow composition stopped being additive")
    complex_first = apply_orbit_flow(real_direct, right_complex, 2)
    complex_second = apply_orbit_flow(complex_first, right_conjugate, 2)
    reverse_order = apply_orbit_flow(real_direct, right_conjugate, 2)
    reverse_order = apply_orbit_flow(reverse_order, right_complex, 2)
    if complex_second != reverse_order:
        raise ArithmeticError("disjoint reflection-orbit flows stopped commuting")
    restored = apply_orbit_flow(complex_second, right_real, -2)
    restored = apply_orbit_flow(restored, right_complex, -2)
    restored = apply_orbit_flow(restored, right_conjugate, -2)
    if restored != initial:
        raise ArithmeticError("inverse divisor flow failed")

    def render(divisor: dict[Point, int]) -> dict[str, int]:
        return {format_point(point): divisor[point] for point in sorted(divisor)}

    return {
        "reflection": "R(a+ib)=-a+ib",
        "initial_divisor": render(initial),
        "two_real_flips_sequential": render(real_sequential),
        "two_real_flips_direct": render(real_direct),
        "conjugate_pair_orbits_forward": render(complex_second),
        "disjoint_orbit_reverse_order": render(reverse_order),
        "inverse_flows_restore_initial": render(restored),
        "real_flow_capacity": "-m_R(z) <= n_O <= m_z",
    }


def allpass_control() -> dict[str, object]:
    maximum_unit_error = 0.0
    maximum_commutator_error = 0.0
    maximum_inverse_error = 0.0
    for frequency_fraction in FREQUENCY_SAMPLES:
        spectral_point = complex(0.0, float(frequency_fraction))
        zeros = tuple(
            complex(float(real), float(imaginary))
            for real, imaginary in ALLPASS_ZERO_SAMPLES
        )
        forward = finite_multiplier(zeros, spectral_point)
        reverse = finite_multiplier(tuple(reversed(zeros)), spectral_point)
        maximum_unit_error = max(maximum_unit_error, abs(abs(forward) - 1.0))
        maximum_commutator_error = max(maximum_commutator_error, abs(forward - reverse))
        zero = zeros[0]
        reflected = -zero.conjugate()
        inverse_product = finite_multiplier((zero, reflected), spectral_point)
        maximum_inverse_error = max(maximum_inverse_error, abs(inverse_product - 1.0))
    if max(maximum_unit_error, maximum_commutator_error, maximum_inverse_error) > 1e-12:
        raise ArithmeticError("finite all-pass controls drifted")
    return {
        "elementary_factor": "B_z(s)=(s+conj(z))/(s-z)",
        "reflection": "R(z)=-conj(z)",
        "inverse_law": "B_R(z)=B_z^(-1)",
        "composition_law": "finite normalized factors commute and orbit flows add",
        "maximum_unit_modulus_error": maximum_unit_error,
        "maximum_commutator_error": maximum_commutator_error,
        "maximum_inverse_error": maximum_inverse_error,
    }


def jordan_obstruction_control() -> dict[str, object]:
    if sum(JORDAN_WEIGHTS, Fraction(0)) != Fraction(-1, 3):
        raise ArithmeticError("Jordan counterexample mean drifted")
    if jordan_root_polynomial(JORDAN_EXPONENTIAL_ROOT) != 0:
        raise ArithmeticError("Jordan counterexample carrier root drifted")
    zero = math.log(4.0 / 3.0)
    lower_bound = float(Fraction(31, 108))
    upper_bound = float(Fraction(1, 3))
    if not lower_bound < zero < upper_bound:
        raise ArithmeticError("declared logarithm bounds failed")
    original_positive_mass = 1.0
    original_negative_mass = 4.0 / 3.0
    flipped_positive_mass = 2.0 / (3.0 * zero) - 1.0
    flipped_negative_mass = 2.0 / (3.0 * zero) - 4.0 / 3.0
    if not (
        original_positive_mass < flipped_positive_mass < original_negative_mass
        and 0.0 < flipped_negative_mass < original_positive_mass
    ):
        raise ArithmeticError("Jordan-mass separation failed")
    maximum_weight_error = 0.0
    for frequency_fraction in FREQUENCY_SAMPLES:
        spectral_point = complex(0.0, float(frequency_fraction))
        original = jordan_transform(spectral_point)
        flipped = jordan_flipped_transform(spectral_point)
        maximum_weight_error = max(
            maximum_weight_error, abs(abs(original) ** 2 - abs(flipped) ** 2)
        )
    if maximum_weight_error > 1e-12:
        raise ArithmeticError("Jordan example lost Fourier-weight equality")
    return {
        "kernel": "weights (1,-4/3) on [0,1] and [1,2]",
        "carrier_zero": "a=log(4/3), with exp(-a)=3/4",
        "exact_log_bounds": "31/108 < log(4/3) < 1/3",
        "original_mean": "-1/3",
        "flipped_mean": "+1/3",
        "original_positive_mass": original_positive_mass,
        "original_negative_mass": original_negative_mass,
        "flipped_positive_mass": flipped_positive_mass,
        "flipped_negative_mass": flipped_negative_mass,
        "original_l1_mass": original_positive_mass + original_negative_mass,
        "flipped_l1_mass": flipped_positive_mass + flipped_negative_mass,
        "maximum_replayed_weight_error": maximum_weight_error,
        "verdict": "Fourier energy does not determine oriented Jordan or L1 mass",
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    pair_coefficients = conjugate_pair_coefficients(RIGHT_COMPLEX)
    return {
        "status": (
            "exact finite rational all-pass classification and abelian divisor-flow "
            "calculus; no infinite-product or global minimum-phase theorem"
        ),
        "source_contract": {
            "git_blobs": {
                f"{commit}:{path}": blob
                for (commit, path), blob in SOURCE_BLOBS.items()
            },
            "import_scope": (
                "the one-zero ODE and Fourier multiplier are imported and rederived; "
                "the corrected zero-mean law is refined to the finite exact phase law"
            ),
        },
        "finite_allpass_group": allpass_control(),
        "divisor_flow": divisor_flow_control(),
        "real_structure": {
            "rule": (
                "real zeros may move singly; nonreal flows must be matched on the "
                "conjugate reflection orbit"
            ),
            "conjugate_pair_numerator_coefficients": [
                str(value) for value in pair_coefficients["numerator"]
            ],
            "conjugate_pair_denominator_coefficients": [
                str(value) for value in pair_coefficients["denominator"]
            ],
            "mean_law": (
                "F_new(0)=eta*F(0)*product_O(-conj(z_O)/z_O)^n_O; "
                "eta=1 for normalized ODE surgery"
            ),
            "zero_mean": "preserved",
            "nonzero_real_mean": (
                "conjugate-pair flows preserve it; each real-zero flip changes its sign"
            ),
            "three_real_flip_sign": real_preserving_mean_sign(3),
            "four_real_flip_sign": real_preserving_mean_sign(4),
        },
        "rational_converse": {
            "statement": (
                "a rational A with no imaginary-axis pole, |A(it)|=1, and "
                "A(infinity)=1 is a finite product of elementary B_z factors"
            ),
            "entireness_gate": (
                "every pole multiplicity of reduced A must be supplied by a zero of F"
            ),
            "unit_scalar_extension": (
                "without A(infinity)=1 there is one additional constant phase"
            ),
        },
        "jordan_l1_counterexample": jordan_obstruction_control(),
        "invariant_scope": {
            "preserved": [
                "support containment in the same compact interval",
                "compact BV regularity",
                "Fourier magnitude",
                "autocorrelation",
                "every finite translate Gram energy",
                "zero mean when present",
            ],
            "not_preserved_in_general": [
                "nonzero mean phase or sign",
                "kernel pointwise shape",
                "L1 norm",
                "positive and negative Jordan masses",
                "oriented complete fields",
            ],
            "fixed_obstructions": [
                "imaginary-axis zeros cannot move without changing Fourier magnitude",
                "real output forces conjugate-matched nonreal flows",
                "finite surgery cannot orient an infinite wrong-half-plane divisor",
                "an infinite product must separately preserve convergence, exponential type, support, and BV regularity",
            ],
        },
        "proof_ledger": {
            "one_zero_ode_surgery": "IMPORTED AND REDERIVED EXACT",
            "finite_allpass_composition_commutation_inverse": "PROVED EXACT",
            "reflection_orbit_divisor_capacity_classification": "PROVED EXACT",
            "finite_rational_allpass_converse": "PROVED EXACT",
            "real_output_and_mean_phase_laws": "PROVED EXACT",
            "support_bv_fourier_autocorrelation_gram_invariance": "PROVED EXACT",
            "jordan_l1_invariance": "REFUTED BY AN EXPLICIT TWO-INTERVAL KERNEL",
            "global_minimum_phase_for_infinite_divisors": "NOT PROVED",
            "arbitrary_infinite_allpass_product": "NOT PROVED",
            "any_beta_energy_estimate": "NOT PROVED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "exact_reflection_orbits": 3,
            "allpass_zero_samples": len(ALLPASS_ZERO_SAMPLES),
            "frequency_samples": len(FREQUENCY_SAMPLES),
            "kernel_intervals_in_counterexample": len(JORDAN_WEIGHTS),
            "root_finders": 0,
            "quadratures": 0,
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
    if args.write_json is not None:
        args.write_json.write_text(text, encoding="utf-8")
    elif args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
            raise RuntimeError("canonical JSON drift")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
