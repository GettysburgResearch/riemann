#!/usr/bin/env python3
"""Bounded exact replay for the carrier-ensemble condition firewall."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_carrier_ensemble_condition_firewall.json"

SOURCE_COMMIT = "0123d1ecb097294fc132cf251aebeab9a6bda169"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_HIGHER_DERIVATIVE_CARRIER_HIERARCHY.md": "d9eda9b3abf512c93c6b0f5c8a84b06b658fe385",
    "research/l-families/atlas/function_field/ffps_higher_derivative_carrier_hierarchy.py": "83e7ed029c5613f392022c262e4e6bdb95627499",
    "research/l-families/atlas/function_field/ffps_higher_derivative_carrier_hierarchy.json": "8b2be0d6b3bc8a78c44f98269d7a139b7635c3f3",
    "tests/test_ffps_higher_derivative_carrier_hierarchy.py": "3eb7bde31a113603e2a28c50ef29483f0357c9d6",
}

MAX_RUNG = 4


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


def sharp_constant(rung: int) -> int:
    if rung < 0:
        raise ValueError("rung must be nonnegative")
    return math.factorial(rung) ** 2 * (2 * rung + 1) * math.comb(2 * rung, rung) ** 2


def support_condition(rung: int, hull: Fraction, support: Fraction) -> Fraction:
    if rung < 0:
        raise ValueError("rung must be nonnegative")
    hull = Fraction(hull)
    support = Fraction(support)
    if support <= 0 or hull < support:
        raise ValueError("require hull >= support > 0")
    return (hull / support) ** (2 * rung + 1)


def direct_sum_data(
    channels: tuple[tuple[int, Fraction, Fraction, Fraction], ...],
) -> dict[str, Fraction | tuple[Fraction, ...]]:
    """Channels are (rung, weight, support, hull)."""
    if not channels:
        raise ValueError("at least one channel is required")
    reverse = Fraction(0)
    diagonal = Fraction(0)
    convex_weights: list[Fraction] = []
    conditions: list[Fraction] = []
    for rung, weight, support, hull in channels:
        weight = Fraction(weight)
        support = Fraction(support)
        hull = Fraction(hull)
        if rung < 0 or weight < 0 or support <= 0 or hull < support:
            raise ValueError("invalid direct-sum channel")
        constant = Fraction(sharp_constant(rung))
        channel_reverse = weight * constant / hull ** (2 * rung + 1)
        channel_diagonal = weight * constant / support ** (2 * rung + 1)
        reverse += channel_reverse
        diagonal += channel_diagonal
        convex_weights.append(channel_reverse)
        conditions.append(support_condition(rung, hull, support))
    if reverse <= 0:
        raise ValueError("at least one channel weight must be positive")
    return {
        "reverse": reverse,
        "diagonal": diagonal,
        "ratio": diagonal / reverse,
        "convex_weights": tuple(convex_weights),
        "conditions": tuple(conditions),
    }


def polynomial_add(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    length = max(len(left), len(right))
    output = tuple(
        (left[i] if i < len(left) else Fraction(0))
        + (right[i] if i < len(right) else Fraction(0))
        for i in range(length)
    )
    while len(output) > 1 and output[-1] == 0:
        output = output[:-1]
    return output


def polynomial_scale(
    polynomial: tuple[Fraction, ...], scalar: Fraction
) -> tuple[Fraction, ...]:
    scalar = Fraction(scalar)
    return tuple(scalar * value for value in polynomial)


def polynomial_product(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    output = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] += left_value * right_value
    return tuple(output)


def polynomial_derivative(
    polynomial: tuple[Fraction, ...], order: int = 1
) -> tuple[Fraction, ...]:
    if order < 0:
        raise ValueError("derivative order must be nonnegative")
    output = polynomial
    for _ in range(order):
        if len(output) <= 1:
            return (Fraction(0),)
        output = tuple(Fraction(i) * output[i] for i in range(1, len(output)))
    return output


def polynomial_moment(polynomial: tuple[Fraction, ...], order: int) -> Fraction:
    if order < 0:
        raise ValueError("moment order must be nonnegative")
    return sum(value / (i + order + 1) for i, value in enumerate(polynomial))


def polynomial_norm_squared(polynomial: tuple[Fraction, ...]) -> Fraction:
    return polynomial_moment(polynomial_product(polynomial, polynomial), 0)


def optimal_carrier_support_one(rung: int) -> tuple[Fraction, ...]:
    if rung < 0:
        raise ValueError("rung must be nonnegative")
    coefficient = Fraction(math.factorial(2 * rung + 1), math.factorial(rung) ** 2)
    left = tuple(
        Fraction(math.comb(rung, power) * (-1) ** power) for power in range(rung + 1)
    )
    shifted = (Fraction(0),) * rung + left
    return polynomial_scale(shifted, coefficient)


def optimal_detector_support_one(rung: int) -> tuple[Fraction, ...]:
    return polynomial_derivative(optimal_carrier_support_one(rung), rung)


def lowest_surviving_moment(polynomial: tuple[Fraction, ...]) -> tuple[int, Fraction]:
    if not polynomial or all(value == 0 for value in polynomial):
        raise ValueError("kernel must be nonzero")
    for order in range(len(polynomial)):
        moment = polynomial_moment(polynomial, order)
        if moment != 0:
            sensitivity = Fraction((-1) ** order, math.factorial(order)) * moment
            return order, sensitivity
    raise AssertionError("nonzero polynomial had no surviving moment")


def coherent_sharp_lower_bound(
    polynomial: tuple[Fraction, ...], support: Fraction = Fraction(1)
) -> Fraction:
    support = Fraction(support)
    if support <= 0:
        raise ValueError("support must be positive")
    rung, sensitivity = lowest_surviving_moment(polynomial)
    return sensitivity**2 * sharp_constant(rung) / support ** (2 * rung + 1)


def matrix_transpose_product(
    matrix: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    if not matrix or not matrix[0] or any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("matrix must be nonempty and rectangular")
    rows = tuple(tuple(Fraction(value) for value in row) for row in matrix)
    width = len(rows[0])
    return tuple(
        tuple(sum(row[i] * row[j] for row in rows) for j in range(width))
        for i in range(width)
    )


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    constants = [sharp_constant(rung) for rung in range(MAX_RUNG + 1)]
    direct = direct_sum_data(
        (
            (1, Fraction(1), Fraction(1), Fraction(2)),
            (2, Fraction(1, 30), Fraction(1), Fraction(2)),
        )
    )
    if direct["ratio"] != 16:
        raise AssertionError("direct-sum example failed")

    k1 = optimal_detector_support_one(1)
    k2 = optimal_detector_support_one(2)
    coherent = polynomial_add(k1, polynomial_scale(k2, Fraction(1, 10)))
    cancellation = (Fraction(6), Fraction(-36), Fraction(36))
    if polynomial_norm_squared(coherent) != Fraction(96, 5):
        raise AssertionError("coherent example norm failed")
    if lowest_surviving_moment(cancellation) != (2, Fraction(1, 10)):
        raise AssertionError("cancellation rung failed")
    if polynomial_norm_squared(cancellation) != coherent_sharp_lower_bound(
        cancellation
    ):
        raise AssertionError("cancellation optimizer failed")

    r_matrix = (
        (Fraction(1), Fraction(1, 2)),
        (Fraction(0), Fraction(1)),
    )
    a_matrix = matrix_transpose_product(r_matrix)
    g1 = polynomial_add(k1, polynomial_scale(k2, Fraction(1, 2)))
    g2 = k2
    psd_energy = polynomial_norm_squared(g1) + polynomial_norm_squared(g2)

    return {
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "ensemble_theorem": {
            "sharp_constants_m_0_through_4": constants,
            "direct_sum_identity": "Delta/A is the reverse-coefficient-weighted average of kappa_j=(L_j/S_j)^(2m_j+1)",
            "direct_sum_example": {
                key: (
                    [fraction_text(value) for value in value]
                    if isinstance(value, tuple)
                    else fraction_text(value)
                )
                for key, value in direct.items()
            },
            "coherent_factorization": "r is the first nonzero moment of K; K=D^r Q_K with compact Q_K and mass b=(-1)^r*moment_r(K)/r!",
            "coherent_lower_bounds": "||K||_2^2>=b^2*C_r/W^(2r+1), ||K*mu_X||_2^2>=b^2*C_r*|B(X)|^2/L^(2r+1)",
            "coherent_example": {
                "K1_coefficients": [fraction_text(value) for value in k1],
                "K2_coefficients": [fraction_text(value) for value in k2],
                "K1_plus_K2_over_10": [fraction_text(value) for value in coherent],
                "norm_squared": fraction_text(polynomial_norm_squared(coherent)),
                "sharp_lower_bound": fraction_text(
                    coherent_sharp_lower_bound(coherent)
                ),
            },
            "cancellation_example": {
                "kernel_coefficients": [fraction_text(value) for value in cancellation],
                "surviving_rung": 2,
                "sensitivity": "1/10",
                "norm_squared": fraction_text(polynomial_norm_squared(cancellation)),
                "sharp_lower_bound": fraction_text(
                    coherent_sharp_lower_bound(cancellation)
                ),
            },
            "PSD_example": {
                "R": [[fraction_text(value) for value in row] for row in r_matrix],
                "A_equals_R_transpose_R": [
                    [fraction_text(value) for value in row] for row in a_matrix
                ],
                "row_norms": [
                    fraction_text(polynomial_norm_squared(g1)),
                    fraction_text(polynomial_norm_squared(g2)),
                ],
                "total_energy": fraction_text(psd_energy),
            },
            "order_zero_loophole": "Q_(0,S)=1_[0,S]/S has kappa_0=L/S and RH iff L*||Q_(0,S)*mu_X||_2^2=X^o(1) for every S_X>=1",
        },
        "proof_ledger": {
            "positive_direct_sum_convex_ratio_identity": "PROVED EXACT",
            "positive_direct_sum_beats_best_constituent": "DISPROVED",
            "positive_multiscale_mixture_beats_hull_optimizer": "DISPROVED",
            "coherent_lowest_surviving_moment_factorization": "PROVED",
            "finite_common_Hilbert_PSD_row_reduction": "PROVED",
            "m_1_optimal_at_common_support_ratio_among_zero_mean_derivative_rungs": "PROVED",
            "m_0_low_pass_loophole_and_RH_equivalence": "PROVED",
            "source_specific_beta_cancellation_from_support_geometry": "NOT PROVED",
            "growing_adaptive_or_indefinite_ensemble_theorem": "NOT PROVED",
            "new_unconditional_beta_estimate": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_rung": MAX_RUNG,
            "polynomial_examples": 4,
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
