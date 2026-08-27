#!/usr/bin/env python3
"""Bounded exact replay for compact-kernel information order."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_compact_kernel_information_order.json"

SOURCE_COMMIT = "f49c463be37b264d121aa27677f9b7ae2a2afdac"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_CARRIER_ENSEMBLE_CONDITION_FIREWALL.md": "ca9874570739bf5d84e920ddad9b1b4e76a78200",
    "research/l-families/atlas/function_field/ffps_carrier_ensemble_condition_firewall.py": "b11895c8e7015b5eca9f7bb63c17fe7b6ecf68c8",
    "research/l-families/atlas/function_field/ffps_carrier_ensemble_condition_firewall.json": "c24077db591207a9edbb5fc0b7318bf45c0c0e5f",
    "tests/test_ffps_carrier_ensemble_condition_firewall.py": "35b6b9b7a443400d512db0f83c72f279a2b4b180",
}

MAX_POLYNOMIAL_DEGREE = 4


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


def sharp_constant(order: int) -> int:
    if order < 0:
        raise ValueError("order must be nonnegative")
    return (
        math.factorial(order) ** 2 * (2 * order + 1) * math.comb(2 * order, order) ** 2
    )


def polynomial_moment_on_interval(
    coefficients: tuple[Fraction, ...],
    order: int,
    support: Fraction = Fraction(1),
    origin: Fraction = Fraction(0),
) -> Fraction:
    if order < 0:
        raise ValueError("moment order must be nonnegative")
    support = Fraction(support)
    origin = Fraction(origin)
    if support <= 0:
        raise ValueError("support must be positive")
    upper = origin + support
    return sum(
        Fraction(value)
        * (upper ** (degree + order + 1) - origin ** (degree + order + 1))
        / (degree + order + 1)
        for degree, value in enumerate(coefficients)
    )


def information_order_and_sensitivity(
    coefficients: tuple[Fraction, ...],
    support: Fraction = Fraction(1),
    origin: Fraction = Fraction(0),
) -> tuple[int, Fraction]:
    if not coefficients or all(Fraction(value) == 0 for value in coefficients):
        raise ValueError("kernel must be nonzero")
    for order in range(len(coefficients)):
        moment = polynomial_moment_on_interval(coefficients, order, support, origin)
        if moment != 0:
            return order, Fraction((-1) ** order, math.factorial(order)) * moment
    raise AssertionError("nonzero polynomial had no surviving moment")


def coefficient_bv_envelope(
    coefficients: tuple[Fraction, ...], support: Fraction = Fraction(1)
) -> Fraction:
    """Safe upper bound for ||K||_infty+Var_R(K zero-extended)."""
    if not coefficients:
        raise ValueError("coefficients must be nonempty")
    support = Fraction(support)
    if support <= 0:
        raise ValueError("support must be positive")
    values = tuple(Fraction(value) for value in coefficients)
    sup_bound = sum(abs(value) * support**degree for degree, value in enumerate(values))
    left_jump = abs(values[0])
    right_jump = abs(
        sum(value * support**degree for degree, value in enumerate(values))
    )
    derivative_l1_bound = sum(
        abs(value) * support**degree
        for degree, value in enumerate(values)
        if degree >= 1
    )
    return sup_bound + left_jump + right_jump + derivative_l1_bound


def normalized_reverse_energy_factor(
    order: int,
    sensitivity: Fraction,
    hull: Fraction,
) -> Fraction:
    if order < 0:
        raise ValueError("order must be nonnegative")
    sensitivity = Fraction(sensitivity)
    hull = Fraction(hull)
    if sensitivity == 0 or hull <= 0:
        raise ValueError("require nonzero sensitivity and positive hull")
    return hull ** (2 * order + 1) / (sensitivity**2 * sharp_constant(order))


def moving_kernel_geometric_factor(
    order: int,
    sensitivity: Fraction,
    hull: Fraction,
    bv_size: Fraction,
) -> Fraction:
    if order < 0:
        raise ValueError("order must be nonnegative")
    sensitivity = Fraction(sensitivity)
    hull = Fraction(hull)
    bv_size = Fraction(bv_size)
    if sensitivity == 0 or hull <= 0 or bv_size < 0:
        raise ValueError("invalid moving-kernel data")
    return (
        hull ** (2 * order + 2) * bv_size**2 / (sensitivity**2 * sharp_constant(order))
    )


def translate_polynomial(
    coefficients: tuple[Fraction, ...], shift: Fraction
) -> tuple[Fraction, ...]:
    """Coefficients of K(t-shift) as a polynomial in t."""
    shift = Fraction(shift)
    output = [Fraction(0) for _ in coefficients]
    for degree, value in enumerate(coefficients):
        value = Fraction(value)
        for power in range(degree + 1):
            output[power] += (
                value * math.comb(degree, power) * (-shift) ** (degree - power)
            )
    return tuple(output)


def sensitivity_preserving_dilation(
    coefficients: tuple[Fraction, ...], order: int, scale: Fraction
) -> tuple[Fraction, ...]:
    """Coefficients of S^(-r-1) K(t/S), supported on [0,S]."""
    if order < 0:
        raise ValueError("order must be nonnegative")
    scale = Fraction(scale)
    if scale <= 0:
        raise ValueError("scale must be positive")
    return tuple(
        Fraction(value) / scale ** (order + 1 + degree)
        for degree, value in enumerate(coefficients)
    )


def exact_zero_extended_variation_linear(
    coefficients: tuple[Fraction, Fraction], support: Fraction = Fraction(1)
) -> Fraction:
    support = Fraction(support)
    if support <= 0:
        raise ValueError("support must be positive")
    c0, c1 = (Fraction(value) for value in coefficients)
    return abs(c0) + abs(c0 + c1 * support) + abs(c1) * support


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    examples = (
        ("low_pass", (Fraction(1),)),
        ("linear_bandpass", (Fraction(1), Fraction(-2))),
        ("optimal_rung_1", (Fraction(6), Fraction(-12))),
        ("optimal_rung_2", (Fraction(60), Fraction(-360), Fraction(360))),
    )
    rows = []
    for name, coefficients in examples:
        order, sensitivity = information_order_and_sensitivity(coefficients)
        envelope = coefficient_bv_envelope(coefficients)
        rows.append(
            {
                "name": name,
                "coefficients": [fraction_text(value) for value in coefficients],
                "information_order": order,
                "sensitivity": fraction_text(sensitivity),
                "sharp_constant": sharp_constant(order),
                "coefficient_BV_envelope": fraction_text(envelope),
                "sample_geometric_factor_L_2": fraction_text(
                    moving_kernel_geometric_factor(
                        order, sensitivity, Fraction(2), envelope
                    )
                ),
            }
        )

    base = (Fraction(1), Fraction(-2))
    base_order, base_sensitivity = information_order_and_sensitivity(base)
    shifted = translate_polynomial(base, Fraction(3))
    shifted_order, shifted_sensitivity = information_order_and_sensitivity(
        shifted, Fraction(1), Fraction(3)
    )
    dilated = sensitivity_preserving_dilation(base, base_order, Fraction(5))
    dilated_order, dilated_sensitivity = information_order_and_sensitivity(
        dilated, Fraction(5)
    )
    if (shifted_order, shifted_sensitivity) != (base_order, base_sensitivity):
        raise AssertionError("translation invariance failed")
    if (dilated_order, dilated_sensitivity) != (base_order, base_sensitivity):
        raise AssertionError("dilation sensitivity failed")

    return {
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "compact_kernel_theorem": {
            "information_order": "r(K)=min{q in nonnegative integers: integral t^q K(t) dt != 0}",
            "sensitivity": "b(K)=(-1)^r*integral(t^r*K)/r!",
            "reverse_bound": "||K*mu_X||_2^2>=b(K)^2*C_r*|B(X)|^2/L^(2r+1)",
            "BV_forward_bound": "||K*mu_X||_2^2<=L*(||K||_infty+Var_R K)^2*(B^*(X))^2",
            "fixed_kernel_equivalence": "for every fixed nonzero compact real BV kernel, RH iff raw energy=X^o(1) iff normalized reverse energy=X^o(1)",
            "moving_kernel_safe_factor": "G_X=L^(2r+2)*(||K_X||_infty+Var K_X)^2/(b_X^2*C_r)",
            "moving_kernel_conclusion": "if r is fixed, b_X!=0, and G_X=X^o(1), normalized field energy is equivalent to RH",
            "sensitivity_preserving_dilation": "K_S(t)=S^(-r-1)*K(t/S), so G_X=(L/S)^(2r+2)*M(K)^2/(b(K)^2*C_r)",
            "rows": rows,
            "translation_certificate": {
                "base_coefficients_on_0_1": [fraction_text(value) for value in base],
                "shifted_coefficients_on_3_4": [
                    fraction_text(value) for value in shifted
                ],
                "order": shifted_order,
                "sensitivity": fraction_text(shifted_sensitivity),
                "support_interval": "[3,4]",
            },
            "dilation_certificate": {
                "scale": 5,
                "coefficients_on_0_5": [fraction_text(value) for value in dilated],
                "order": dilated_order,
                "sensitivity": fraction_text(dilated_sensitivity),
            },
        },
        "proof_ledger": {
            "information_order_and_compact_primitive_factorization": "PROVED",
            "universal_moment_reverse_bound": "PROVED",
            "BV_Abel_forward_bound_under_RH": "PROVED",
            "every_fixed_nonzero_compact_BV_kernel_RH_equivalence": "PROVED",
            "moving_kernel_safe_geometric_factor": "PROVED SUFFICIENT",
            "translation_and_sensitivity_preserving_dilation_laws": "PROVED",
            "failure_outside_safe_geometric_window": "NOT PROVED",
            "new_unconditional_beta_estimate": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_polynomial_degree": MAX_POLYNOMIAL_DEGREE,
            "exact_polynomial_examples": len(examples),
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
