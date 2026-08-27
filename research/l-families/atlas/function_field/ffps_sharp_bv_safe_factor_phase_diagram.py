#!/usr/bin/env python3
"""Bounded replay for the sharp universal-BV safe-factor phase diagram."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_sharp_bv_safe_factor_phase_diagram.json"

SOURCE_COMMIT = "798feab0bb333efd8b45ab197131cd13658a5ca9"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_CHEBYSHEV_BV_KERNEL_EXTREMIZER.md": "0daf4e6181d1c452b957bff255ba79062bf411a0",
    "research/l-families/atlas/function_field/ffps_chebyshev_bv_kernel_extremizer.py": "cdee20c916566802b59278f07cfc51ebcedb7606",
    "research/l-families/atlas/function_field/ffps_chebyshev_bv_kernel_extremizer.json": "8bd2400c05e946fde6241253f7f90b5fbe0aa1ce",
    "tests/test_ffps_chebyshev_bv_kernel_extremizer.py": "e4d9ce253dcec5a7f88bbfefedf4fb5bbcf06c5d",
}

MAX_ORDER = 12


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


def sharp_bv_shape_constant(order: int) -> int:
    """Minimum W^(r+1) M(K)/|b(K)| at information order r."""
    validate_order(order)
    return math.factorial(order) * 4**order * (2 * order + 3)


def order_constant(order: int) -> Fraction:
    """Minimum dimensionless M^2/(b^2 C_r) after width normalization."""
    validate_order(order)
    return Fraction(
        16**order * (2 * order + 3) ** 2,
        (2 * order + 1) * math.comb(2 * order, order) ** 2,
    )


def consecutive_ratio(order: int) -> Fraction:
    """A_(r+1)/A_r in reduced exact form."""
    validate_order(order)
    return Fraction(
        4 * (order + 1) ** 2 * (2 * order + 5) ** 2,
        (2 * order + 1) * (2 * order + 3) ** 3,
    )


def monotonicity_gap_numerator(order: int) -> int:
    """Numerator before cancellation in A_(r+1)/A_r - 1."""
    validate_order(order)
    return 32 * order**3 + 132 * order**2 + 172 * order + 73


def ratio_drop_numerator(order: int) -> int:
    """Positive numerator proving consecutive ratios decrease to one."""
    validate_order(order)
    return (
        256 * order**5
        + 2496 * order**4
        + 9408 * order**3
        + 17216 * order**2
        + 15392 * order
        + 5444
    )


def width_penalty(order: int, log_horizon: Fraction, width: Fraction) -> Fraction:
    validate_order(order)
    log_horizon = Fraction(log_horizon)
    width = Fraction(width)
    if log_horizon < 0:
        raise ValueError("log horizon must be nonnegative")
    if width <= 0:
        raise ValueError("width must be positive")
    return ((width + log_horizon) / width) ** (2 * order + 2)


def exact_minimum_safe_factor(
    order: int, log_horizon: Fraction, width: Fraction
) -> Fraction:
    return order_constant(order) * width_penalty(order, log_horizon, width)


def power_law_safe(*, order_exponent: Fraction, width_exponent: Fraction) -> bool:
    """Strict power-law phase for r=ell^rho and W=ell^sigma."""
    order_exponent = Fraction(order_exponent)
    width_exponent = Fraction(width_exponent)
    return order_exponent < max(Fraction(1), width_exponent)


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    rows = []
    previous = None
    for order in range(MAX_ORDER + 1):
        constant = order_constant(order)
        if previous is not None and constant <= previous:
            raise AssertionError("order constants are not strictly increasing")
        if order < MAX_ORDER and consecutive_ratio(order) <= 1:
            raise AssertionError("consecutive ratio is not greater than one")
        rows.append(
            {
                "information_order": order,
                "sharp_BV_shape_constant": sharp_bv_shape_constant(order),
                "order_constant_A_r": fraction_text(constant),
                "ratio_to_2pi_r_squared": (
                    None
                    if order == 0
                    else f"{float(constant) / (2 * math.pi * order**2):.12f}"
                ),
                "next_ratio": (
                    None
                    if order == MAX_ORDER
                    else fraction_text(consecutive_ratio(order))
                ),
                "positive_gap_numerator": (
                    None if order == MAX_ORDER else monotonicity_gap_numerator(order)
                ),
                "positive_ratio_drop_numerator": (
                    None if order >= MAX_ORDER - 1 else ratio_drop_numerator(order)
                ),
            }
        )
        previous = constant

    sample_width_rows = []
    for order in range(4):
        for width in (1, 2, 4):
            sample_width_rows.append(
                {
                    "information_order": order,
                    "log_horizon": 4,
                    "support_width": width,
                    "minimum_safe_factor": fraction_text(
                        exact_minimum_safe_factor(order, Fraction(4), Fraction(width))
                    ),
                }
            )

    return {
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "sharp_phase_theorem": {
            "shape_bound": "W^(r+1) M(K)/|b(K)| >= r!*4^r*(2r+3)",
            "safe_factor_bound": "G_X >= A_r*(1+log(X)/W)^(2r+2)",
            "order_constant": "A_r=16^r*(2r+3)^2/((2r+1)*binom(2r,r)^2)",
            "consecutive_ratio": "A_(r+1)/A_r=4*(r+1)^2*(2r+5)^2/((2r+1)*(2r+3)^3)>1",
            "ratio_gap": "numerator gap=32r^3+132r^2+172r+73",
            "ratio_shape": "A_(r+1)/A_r decreases strictly to one, so A_r is strictly log-concave",
            "asymptotic": "A_r=2*pi*r^2*(1+11/(4r)+53/(32r^2)+O(r^-3))",
            "global_order_winner": "r=0, with A_0=9",
            "zero_mean_order_winner": "among r>=1, the winner is r=1, with A_1=100/3",
            "power_law_safe_region": "for r=(log X)^rho and W=(log X)^sigma, the sharp BV certificate is subpower exactly when rho<max(1,sigma), away from bounded/order-zero conventions",
            "rows": rows,
            "sample_width_rows": sample_width_rows,
        },
        "proof_ledger": {
            "sharp_fixed_width_shape_minimum": "PROVED",
            "unique_dilated_Chebyshev_equality_case": "PROVED",
            "strict_growth_in_information_order": "PROVED",
            "strict_log_concavity_in_information_order": "PROVED",
            "moving_information_order_safe_extension": "PROVED SUFFICIENT",
            "universal_BV_route_prefers_low_pass": "PROVED",
            "higher_order_never_improves_actual_beta_energy": "NOT PROVED",
            "failure_outside_safe_factor_precludes_RH_equivalence": "NOT PROVED",
            "new_unconditional_beta_cancellation": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_information_order": MAX_ORDER,
            "sample_widths": 3,
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
