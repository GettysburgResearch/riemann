#!/usr/bin/env python3
"""Bounded exact replay for the truncated beta zero-tube residue law."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "3dbf13f6d1c49e573a5b9cd8355d9c124273062b"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_BANDPASS_ASSEMBLED_PERRON_LEAKAGE.md": (
        "e7959b8788b8a374920aa53bcafd1fb28cda3b72"
    ),
    "research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.py": (
        "52023bb4527a32a2c9983fdd25707da3361242e8"
    ),
    "research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.json": (
        "0031e9ae114d7bf6c60d69789d5d52fe4cf04f6e"
    ),
    "tests/test_ffps_bandpass_assembled_perron_leakage.py": (
        "efc9cde7eef3e833aaa5ac40b5d37b1e34f76770"
    ),
}
MAX_MULTIPLICITY = 6


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
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def validate_multiplicity(multiplicity: int) -> None:
    if (
        isinstance(multiplicity, bool)
        or not isinstance(multiplicity, int)
        or multiplicity < 1
    ):
        raise ValueError("multiplicity must be a positive integer")


def cauchy_mass_over_pi(multiplicity: int) -> Fraction:
    """I_m/pi for I_m=int_R (1+u^2)^(-m) du."""
    validate_multiplicity(multiplicity)
    return Fraction(
        math.comb(2 * multiplicity - 2, multiplicity - 1),
        4 ** (multiplicity - 1),
    )


def real_c_residue_coefficient(multiplicity: int) -> int:
    """Coefficient after delta=c/2 and the Perron factor 1/(2*pi)."""
    validate_multiplicity(multiplicity)
    ratio = cauchy_mass_over_pi(multiplicity)
    result = 2 ** (2 * multiplicity - 2) * ratio
    if result.denominator != 1:
        raise ArithmeticError("real-c residue coefficient was not integral")
    return result.numerator


def notch_mass_over_pi(multiplicity: int, notch_half_order: int) -> Fraction:
    """Beta(r+1/2,m-r-1/2)/pi for 0<=r<=m-1."""
    validate_multiplicity(multiplicity)
    if (
        isinstance(notch_half_order, bool)
        or not isinstance(notch_half_order, int)
        or notch_half_order < 0
        or notch_half_order >= multiplicity
    ):
        raise ValueError("notch half-order must lie in [0,multiplicity-1]")
    other = multiplicity - notch_half_order - 1
    numerator = math.factorial(2 * notch_half_order) * math.factorial(2 * other)
    denominator = (
        4 ** (multiplicity - 1)
        * math.factorial(notch_half_order)
        * math.factorial(other)
        * math.factorial(multiplicity - 1)
    )
    return Fraction(numerator, denominator)


def notch_real_c_coefficient(multiplicity: int, notch_half_order: int) -> Fraction:
    ratio = notch_mass_over_pi(multiplicity, notch_half_order)
    return 2 ** (2 * multiplicity - 2 * notch_half_order - 2) * ratio


def discrete_autocorrelation(values: tuple[Fraction, ...]) -> dict[int, Fraction]:
    if not values:
        raise ValueError("kernel must be nonempty")
    radius = len(values) - 1
    return {
        lag: sum(
            values[index] * values[index + lag]
            for index in range(len(values))
            if 0 <= index + lag < len(values)
        )
        for lag in range(-radius, radius + 1)
    }


def autocorrelation_panel() -> dict[str, object]:
    kernel = (Fraction(1), Fraction(-2), Fraction(1))
    if (
        sum(kernel) != 0
        or sum(index * value for index, value in enumerate(kernel)) != 0
    ):
        raise ArithmeticError("toy second difference lost its fixed notch")
    correlation = discrete_autocorrelation(kernel)
    absolute_lag = sum(abs(lag) * value for lag, value in correlation.items())
    cumulative = []
    total = Fraction(0)
    for value in kernel:
        total += value
        cumulative.append(total)
    cumulative_norm = sum(value * value for value in cumulative)
    if absolute_lag != -2 * cumulative_norm:
        raise ArithmeticError("absolute-lag identity failed")
    leakage_derivative = -absolute_lag / 2
    if leakage_derivative != cumulative_norm or leakage_derivative <= 0:
        raise ArithmeticError("linear max-tilt leakage lost positivity")
    return {
        "kernel": [str(value) for value in kernel],
        "difference_order": 2,
        "autocorrelation_notch_order": 4,
        "correlation_by_lag": {
            str(lag): str(value) for lag, value in sorted(correlation.items())
        },
        "absolute_lag_moment": str(absolute_lag),
        "cumulative_norm_square": str(cumulative_norm),
        "max_tilt_linear_coefficient": str(leakage_derivative),
    }


def multiplicity_table() -> list[dict[str, object]]:
    rows = []
    for multiplicity in range(1, MAX_MULTIPLICITY + 1):
        central = math.comb(2 * multiplicity - 2, multiplicity - 1)
        if real_c_residue_coefficient(multiplicity) != central:
            raise ArithmeticError("central-binomial Perron normalization failed")
        rows.append(
            {
                "multiplicity": multiplicity,
                "I_m_over_pi": str(cauchy_mass_over_pi(multiplicity)),
                "real_c_coefficient": central,
                "real_c_power": 1 - 2 * multiplicity,
                "c_times_inner_power": 2 - 2 * multiplicity,
                "compatible_with_O_1_over_c_unnotched": multiplicity == 1,
            }
        )
    return rows


def notch_table() -> list[dict[str, object]]:
    rows = []
    for multiplicity in range(1, MAX_MULTIPLICITY + 1):
        for notch_half_order in range(multiplicity):
            coefficient = notch_real_c_coefficient(multiplicity, notch_half_order)
            rows.append(
                {
                    "multiplicity": multiplicity,
                    "notch_weight_order": 2 * notch_half_order,
                    "real_c_coefficient": str(coefficient),
                    "real_c_power": 2 * notch_half_order + 1 - 2 * multiplicity,
                    "compatible_with_O_1_over_c": (
                        multiplicity <= notch_half_order + 1
                    ),
                }
            )
    return rows


def toy_residue_panel() -> dict[str, object]:
    residue_square = Fraction(9, 4)
    weight = Fraction(5, 3)
    rows = []
    for multiplicity in range(1, 5):
        rows.append(
            {
                "multiplicity": multiplicity,
                "coefficient": str(
                    residue_square * weight * real_c_residue_coefficient(multiplicity)
                ),
                "power_of_c": 1 - 2 * multiplicity,
            }
        )
    return {
        "local_residue_square": str(residue_square),
        "local_weight": str(weight),
        "real_c_rows": rows,
        "zeta_zeros_computed": 0,
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "theorem": {
            "local_multiple_zero_law": (
                "delta^(2m-1)|B_beta(1/2+delta+it)|^2 dt -> I_m*Q_rho*Dirac_gamma"
            ),
            "simple_distribution": (
                "delta|B_beta|^2 dt -> pi*sum_rho Q_rho*Dirac_gamma"
            ),
            "real_c_perron_coefficient": "binomial(2m-2,m-1)*Q_rho*w(gamma)",
            "unnotched_O_1_over_c_forces": "every weighted critical-line zero is simple",
            "fixed_notch_O_1_over_c_forces": (
                "multiplicity m<=r+1 at a weight zero of order 2r"
            ),
            "max_tilt_warning": (
                "a nonzero linear leakage coefficient contributes at c^(2-2m)"
            ),
        },
        "exact_replays": {
            "multiplicity_constants": multiplicity_table(),
            "notch_constants": notch_table(),
            "toy_local_residues": toy_residue_panel(),
            "autocorrelation": autocorrelation_panel(),
        },
        "scope": {
            "height_window_fixed": True,
            "local_zero_isolating_tube_assumed": True,
            "critical_zeros_computed": False,
            "infinite_t_tail_controlled": False,
            "perron_contour_shift_proved": False,
            "O_1_over_c_bound_proved": False,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "maximum_symbolic_multiplicity": MAX_MULTIPLICITY,
            "toy_kernel_length": 3,
            "floating_point_operations": 0,
            "zeta_zeros": 0,
            "large_matrices": 0,
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
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    if not args.check and not args.write_json:
        print(rendered, end="")


if __name__ == "__main__":
    main()
