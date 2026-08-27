#!/usr/bin/env python3
"""Bounded replay for the Chebyshev sharp-BV kernel extremizer."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_chebyshev_bv_kernel_extremizer.json"

SOURCE_COMMIT = "ad78ecf6ac7e9dc099cb5fc3b1d40fca9aaa2b3f"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_COMPACT_KERNEL_INFORMATION_ORDER.md": "ccaef3ad8527aa5c32735ad441829bbe547f0472",
    "research/l-families/atlas/function_field/ffps_compact_kernel_information_order.py": "8b275b88879237074b6181ad77ab784e8f847a0c",
    "research/l-families/atlas/function_field/ffps_compact_kernel_information_order.json": "0030155750437bfbc6f19d13fcbf9a7dc58325c9",
    "tests/test_ffps_compact_kernel_information_order.py": "866e9260195aa01d0ac59a6ad0f6cca420700b30",
}

DLMF_MINIMAX_URL = "https://dlmf.nist.gov/18.38"
MAX_ORDER = 6


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


def validate_order(order: int) -> None:
    if order < 0:
        raise ValueError("order must be nonnegative")


def sharp_energy_constant(order: int) -> int:
    validate_order(order)
    return (
        math.factorial(order) ** 2 * (2 * order + 1) * math.comb(2 * order, order) ** 2
    )


def chebyshev_minimax_error(order: int) -> Fraction:
    """Best degree-r approximation error to x^(r+1) on [0,1]."""
    validate_order(order)
    return Fraction(1, 2 ** (2 * order + 1))


def second_kind_l1_error(order: int) -> Fraction:
    """Best degree-(r-1) L1 approximation error to x^r on [0,1]."""
    validate_order(order)
    return Fraction(1, 4**order)


def extremal_weight_scale(order: int, sensitivity: Fraction = Fraction(1)) -> Fraction:
    validate_order(order)
    sensitivity = Fraction(sensitivity)
    if sensitivity == 0:
        raise ValueError("sensitivity must be nonzero")
    return Fraction(math.factorial(order) * 2 ** (2 * order + 1)) * abs(sensitivity)


def sharp_variation(order: int, sensitivity: Fraction = Fraction(1)) -> Fraction:
    validate_order(order)
    sensitivity = Fraction(sensitivity)
    return Fraction(math.factorial(order + 1) * 2 ** (2 * order + 1)) * abs(sensitivity)


def extremal_step_height(order: int, sensitivity: Fraction = Fraction(1)) -> Fraction:
    return extremal_weight_scale(order, sensitivity) / 2


def sharp_supremum(order: int, sensitivity: Fraction = Fraction(1)) -> Fraction:
    validate_order(order)
    sensitivity = Fraction(sensitivity)
    return Fraction(math.factorial(order) * 4**order) * abs(sensitivity)


def extremal_bv_size(order: int, sensitivity: Fraction = Fraction(1)) -> Fraction:
    """Exact ||K||_infty + Var(K) for the sharp-variation step kernel."""
    validate_order(order)
    sensitivity = Fraction(sensitivity)
    return Fraction(math.factorial(order) * 2 ** (2 * order) * (2 * order + 3)) * abs(
        sensitivity
    )


def extremal_step_energy(order: int, sensitivity: Fraction = Fraction(1)) -> Fraction:
    return extremal_step_height(order, sensitivity) ** 2


def energy_gap_ratio(order: int) -> Fraction:
    validate_order(order)
    return extremal_step_energy(order) / sharp_energy_constant(order)


def polynomial_add(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    length = max(len(left), len(right))
    return tuple(
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(length)
    )


def polynomial_scale(
    polynomial: tuple[Fraction, ...], scalar: Fraction
) -> tuple[Fraction, ...]:
    return tuple(Fraction(scalar) * value for value in polynomial)


def polynomial_product(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    output = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] += left_value * right_value
    return tuple(output)


def shifted_chebyshev_polynomial(degree: int) -> tuple[Fraction, ...]:
    """Coefficients of T_degree(2x-1)."""
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    if degree == 0:
        return (Fraction(1),)
    affine = (Fraction(-1), Fraction(2))
    if degree == 1:
        return affine
    previous = (Fraction(1),)
    current = affine
    for _ in range(2, degree + 1):
        following = polynomial_add(
            polynomial_scale(polynomial_product(affine, current), Fraction(2)),
            polynomial_scale(previous, Fraction(-1)),
        )
        previous, current = current, following
    return current


def shifted_second_kind_polynomial(degree: int) -> tuple[Fraction, ...]:
    """Coefficients of U_degree(2x-1)."""
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    if degree == 0:
        return (Fraction(1),)
    affine_twice = (Fraction(-2), Fraction(4))
    if degree == 1:
        return affine_twice
    previous = (Fraction(1),)
    current = affine_twice
    for _ in range(2, degree + 1):
        following = polynomial_add(
            polynomial_product(affine_twice, current),
            polynomial_scale(previous, Fraction(-1)),
        )
        previous, current = current, following
    return current


def monic_minimax_residual(order: int) -> tuple[Fraction, ...]:
    validate_order(order)
    degree = order + 1
    return polynomial_scale(
        shifted_chebyshev_polynomial(degree), Fraction(1, 2 ** (2 * degree - 1))
    )


def monic_l1_residual(order: int) -> tuple[Fraction, ...]:
    validate_order(order)
    return polynomial_scale(
        shifted_second_kind_polynomial(order), Fraction(1, 4**order)
    )


def extremal_atoms(
    order: int, sensitivity: Fraction = Fraction(1)
) -> tuple[tuple[float, Fraction], ...]:
    """Descending Chebyshev-Lobatto nodes and exact signed atom weights."""
    validate_order(order)
    sensitivity = Fraction(sensitivity)
    if sensitivity == 0:
        raise ValueError("sensitivity must be nonzero")
    degree = order + 1
    scale = extremal_weight_scale(order, sensitivity)
    global_sign = (-1) ** (order + 1) * (1 if sensitivity > 0 else -1)
    atoms = []
    for index in range(degree + 1):
        node = (1 + math.cos(index * math.pi / degree)) / 2
        endpoint_factor = Fraction(1, 2) if index in (0, degree) else Fraction(1)
        weight = global_sign * (-1) ** index * endpoint_factor * scale
        atoms.append((node, weight))
    return tuple(atoms)


def numerical_atom_moment(
    atoms: tuple[tuple[float, Fraction], ...], order: int
) -> float:
    if order < 0:
        raise ValueError("moment order must be nonnegative")
    return sum(float(weight) * node**order for node, weight in atoms)


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    rows = []
    for order in range(MAX_ORDER + 1):
        residual = monic_minimax_residual(order)
        if residual[-1] != 1:
            raise AssertionError("minimax residual was not monic")
        atoms = extremal_atoms(order)
        for lower in range(order + 1):
            if abs(numerical_atom_moment(atoms, lower)) > 2e-8:
                raise AssertionError("atom annihilation failed")
        target = (-1) ** (order + 1) * math.factorial(order + 1)
        if abs(numerical_atom_moment(atoms, order + 1) - target) > 2e-7:
            raise AssertionError("atom target moment failed")
        atom_variation = sum(abs(weight) for _, weight in atoms)
        if atom_variation != sharp_variation(order):
            raise AssertionError("atom variation failed")
        rows.append(
            {
                "information_order": order,
                "minimax_error": fraction_text(chebyshev_minimax_error(order)),
                "monic_residual_coefficients": [
                    fraction_text(value) for value in residual
                ],
                "L1_minimax_error": fraction_text(second_kind_l1_error(order)),
                "monic_L1_residual_coefficients": [
                    fraction_text(value) for value in monic_l1_residual(order)
                ],
                "weight_scale": fraction_text(extremal_weight_scale(order)),
                "sharp_variation": fraction_text(sharp_variation(order)),
                "sharp_supremum": fraction_text(sharp_supremum(order)),
                "step_height": fraction_text(extremal_step_height(order)),
                "BV_size_sup_plus_variation": fraction_text(extremal_bv_size(order)),
                "step_energy": fraction_text(extremal_step_energy(order)),
                "sharp_smooth_energy": sharp_energy_constant(order),
                "step_to_smooth_energy_ratio": fraction_text(energy_gap_ratio(order)),
                "atoms": [
                    {
                        "node_rounded": f"{node:.12f}",
                        "weight": fraction_text(weight),
                    }
                    for node, weight in atoms
                ],
            }
        )

    return {
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "classical_external_input": {
            "source": "NIST DLMF section 18.38",
            "url": DLMF_MINIMAX_URL,
            "statement_used": "the monic Chebyshev polynomial has least uniform norm on [-1,1]",
            "rescaled_consequence": "distance of x^(r+1) from degree-r polynomials on [0,1] is 2^(-2r-1)",
        },
        "sharp_BV_theorem": {
            "variation_bound": "Var_R(K)>=2^(2r+1)*(r+1)!*|b|",
            "unique_extremizer": "the derivative measure is supported on shifted Chebyshev-Lobatto extrema with alternating endpoint-half weights",
            "step_profile": "K alternates between plus/minus r!*2^(2r)*|b| on consecutive Lobatto intervals",
            "supremum_bound": "||K||_infty>=r!*4^r*|b|, from the shifted second-kind Chebyshev L1 extremal polynomial",
            "exact_BV_size": "||K||_infty+Var(K)=r!*2^(2r)*(2r+3)*|b|",
            "complete_BV_size_optimum": "the alternating step kernel simultaneously attains the sharp supremum and variation bounds, so it uniquely minimizes their sum",
            "exact_step_energy": "||K||_2^2=(r!)^2*2^(4r)*b^2",
            "energy_gap": "step_energy/(C_r*b^2)=2^(4r)/((2r+1)*binom(2r,r)^2), tending to pi/2",
            "rows": rows,
        },
        "proof_ledger": {
            "sharp_zero_extended_BV_variation_bound": "PROVED FROM CLASSICAL MINIMAX INPUT",
            "unique_alternating_step_extremizer": "PROVED",
            "exact_sup_variation_and_L2_energy": "PROVED EXACT",
            "step_to_smooth_energy_ratio_and_limit": "PROVED",
            "BV_extremizer_also_minimizes_sup_plus_variation": "PROVED",
            "new_beta_cancellation_or_unconditional_estimate": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_information_order": MAX_ORDER,
            "maximum_atoms": MAX_ORDER + 2,
            "beta_terms": 0,
            "primes": 0,
            "zeta_zeros": 0,
            "root_searches": 0,
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
