#!/usr/bin/env python3
"""Bounded exact replay for the fixed infinite dyadic-box band-pass smoother."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREDECESSOR_COMMIT = "05aaabe69060c24c8db4ca33c350e109231960f1"
PREDECESSOR_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_BANDPASS_BETA_ENERGY_LADDER.md": (
        "0ac23a6c384a896e50fed21ca7d8bf079c338ac0"
    ),
    "research/l-families/atlas/function_field/ffps_bandpass_beta_energy_ladder.py": (
        "9ca6db9ad6b0149936efbd0e99f799d89f3cc53a"
    ),
    "research/l-families/atlas/function_field/ffps_bandpass_beta_energy_ladder.json": (
        "ff568b48100048f6ad963c7afa23c4ac04c3d291"
    ),
    "tests/test_ffps_bandpass_beta_energy_ladder.py": (
        "6b45ddd02148c437bba375d6dbaf753c938e3375"
    ),
}

PARTIAL_LEVEL_CAP = 8
ENVELOPE_EXPONENT_CAP = 16
REPLAY_ORDER_CAP = 4
TOY_BOUNDARY_KERNEL = (Fraction(3), Fraction(-1), Fraction(4), Fraction(2))


def check_source_contract() -> None:
    for path, expected in PREDECESSOR_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{PREDECESSOR_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"predecessor blob mismatch: {path}")


def validate_positive_integer(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")


def convolve(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    if not left or not right:
        raise ValueError("convolution inputs must be nonempty")
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def finite_difference(cells: tuple[Fraction, ...], order: int) -> tuple[Fraction, ...]:
    if not cells:
        raise ValueError("cells must be nonempty")
    if (
        isinstance(order, bool)
        or not isinstance(order, int)
        or not 1 <= order <= REPLAY_ORDER_CAP
    ):
        raise ValueError("order exceeds the bounded replay cap")
    result = cells
    for _ in range(order):
        result = convolve(result, (Fraction(1), Fraction(-1)))
    return result


def dyadic_width(level: int) -> Fraction:
    validate_positive_integer(level)
    return Fraction(1, 2**level)


def partial_total_width(levels: int) -> Fraction:
    validate_positive_integer(levels)
    return sum((dyadic_width(level) for level in range(1, levels + 1)), Fraction(0))


def discrete_dyadic_smoother(levels: int) -> tuple[Fraction, ...]:
    """Common-grid exact replay of the first ``levels`` causal boxes."""
    validate_positive_integer(levels)
    if levels > PARTIAL_LEVEL_CAP:
        raise ValueError("levels exceed the bounded replay cap")
    result = (Fraction(1),)
    for level in range(1, levels + 1):
        width_cells = 2 ** (levels - level)
        box = (Fraction(1, width_cells),) * width_cells
        result = convolve(result, box)
    return result


def moments(cells: tuple[Fraction, ...], highest: int) -> tuple[Fraction, ...]:
    if not cells:
        raise ValueError("cells must be nonempty")
    if isinstance(highest, bool) or not isinstance(highest, int) or highest < 0:
        raise ValueError("highest must be a nonnegative integer")
    return tuple(
        sum(
            (value * index**degree for index, value in enumerate(cells)),
            Fraction(0),
        )
        for degree in range(highest + 1)
    )


def autocorrelation(cells: tuple[Fraction, ...]) -> dict[int, Fraction]:
    if not cells:
        raise ValueError("cells must be nonempty")
    radius = len(cells) - 1
    return {
        shift: sum(
            (
                cells[index] * cells[index + shift]
                for index in range(max(0, -shift), min(len(cells), len(cells) - shift))
            ),
            Fraction(0),
        )
        for shift in range(-radius, radius + 1)
    }


def correlation_moments(
    correlation: dict[int, Fraction], highest: int
) -> tuple[Fraction, ...]:
    if not correlation:
        raise ValueError("correlation must be nonempty")
    if isinstance(highest, bool) or not isinstance(highest, int) or highest < 0:
        raise ValueError("highest must be a nonnegative integer")
    return tuple(
        sum(
            (value * shift**degree for shift, value in correlation.items()),
            Fraction(0),
        )
        for degree in range(highest + 1)
    )


def truncated_series_product(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...], degree: int
) -> tuple[Fraction, ...]:
    if not left or not right:
        raise ValueError("series inputs must be nonempty")
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
        raise ValueError("degree must be a nonnegative integer")
    output = [Fraction(0)] * (degree + 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            if left_index + right_index <= degree:
                output[left_index + right_index] += left_value * right_value
    return tuple(output)


def box_laplace_series(width: Fraction, degree: int) -> tuple[Fraction, ...]:
    if width <= 0:
        raise ValueError("width must be positive")
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
        raise ValueError("degree must be a nonnegative integer")
    return tuple(
        Fraction((-1) ** exponent, math.factorial(exponent + 1)) * width**exponent
        for exponent in range(degree + 1)
    )


def partial_laplace_series(levels: int, degree: int) -> tuple[Fraction, ...]:
    validate_positive_integer(levels)
    result = (Fraction(1),) + (Fraction(0),) * degree
    for level in range(1, levels + 1):
        result = truncated_series_product(
            result, box_laplace_series(dyadic_width(level), degree), degree
        )
    return result


def envelope_binary_exponent(binary_scale: int) -> int:
    """Exponent E with |Phi(2^M/ell)| <= 2^E from the first M-2 boxes."""
    if (
        isinstance(binary_scale, bool)
        or not isinstance(binary_scale, int)
        or not 3 <= binary_scale <= ENVELOPE_EXPONENT_CAP
    ):
        raise ValueError("binary scale exceeds the bounded replay cap")
    return -((binary_scale - 1) * (binary_scale - 2) // 2)


def partial_smoother_panel() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for levels in range(1, PARTIAL_LEVEL_CAP + 1):
        smoother = discrete_dyadic_smoother(levels)
        series = partial_laplace_series(levels, 2)
        expected_width = Fraction(1) - Fraction(1, 2**levels)
        if partial_total_width(levels) != expected_width:
            raise ArithmeticError("dyadic support sum changed")
        if sum(smoother, Fraction(0)) != 1:
            raise ArithmeticError("partial smoother lost probability mass")
        if series[0] != 1 or series[1] != -expected_width / 2:
            raise ArithmeticError("partial Laplace product changed its linear term")
        rows.append(
            {
                "levels": levels,
                "total_width": str(expected_width),
                "common_grid_cells": len(smoother),
                "mass": str(sum(smoother, Fraction(0))),
                "laplace_linear_coefficient": str(series[1]),
            }
        )
    return {"rows": rows}


def notch_panel() -> dict[str, object]:
    smoother = discrete_dyadic_smoother(PARTIAL_LEVEL_CAP)
    rows: list[dict[str, object]] = []
    for order in range(1, REPLAY_ORDER_CAP + 1):
        bandpass = convolve(finite_difference(TOY_BOUNDARY_KERNEL, order), smoother)
        bandpass_moments = moments(bandpass, order)
        correlation = autocorrelation(bandpass)
        correlation_values = correlation_moments(correlation, 2 * order)
        if any(bandpass_moments[:order]) or bandpass_moments[order] == 0:
            raise ArithmeticError("dyadic smoothing changed the exact notch order")
        if any(correlation_values[: 2 * order]) or correlation_values[2 * order] == 0:
            raise ArithmeticError("autocorrelation lost the doubled notch")
        rows.append(
            {
                "difference_order": order,
                "kernel_zero_moments": order,
                "correlation_zero_moments": 2 * order,
                "kernel_leading_moment": str(bandpass_moments[order]),
                "correlation_leading_moment": str(correlation_values[2 * order]),
            }
        )
    return {"partial_levels": PARTIAL_LEVEL_CAP, "rows": rows}


def envelope_panel() -> dict[str, object]:
    rows = []
    for binary_scale in range(3, ENVELOPE_EXPONENT_CAP + 1):
        exponent = envelope_binary_exponent(binary_scale)
        expected = -((binary_scale - 1) * (binary_scale - 2) // 2)
        if exponent != expected or exponent >= 0:
            raise ArithmeticError("dyadic Fourier envelope exponent changed")
        rows.append(
            {
                "M": binary_scale,
                "a_interval": f"[2^{binary_scale},2^{binary_scale + 1})",
                "upper_bound": f"2^({exponent})",
            }
        )
    return {"rows": rows}


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commit": PREDECESSOR_COMMIT,
            "git_blobs": PREDECESSOR_BLOBS,
            "imported": (
                "fixed band-pass beta energy ladder and its pinned boundary/Mellin inputs"
            ),
            "source_line_endings": (
                "irrelevant because the contract uses Git object IDs"
            ),
        },
        "infinite_smoother": {
            "widths": "ell_k=ell/2^k for k>=1",
            "support": "[0,ell]",
            "probability_density": True,
            "regularity": "C-infinity",
            "laplace_product": (
                "Phi_ell(s)=product_(k>=1) (1-exp(-ell*s/2^k))/(ell*s/2^k)"
            ),
            "right_half_plane_zero_free": True,
            "fourier_envelope": (
                "for a=ell*|t| and M=floor(log2(a))>=3, "
                "|Phi_ell(it)|<=2^(-(M-1)(M-2)/2)"
            ),
        },
        "fixed_bandpass": {
            "kernel": "B_(r,infinity)=eta_(ell,infinity)*Delta_epsilon^r K_bd",
            "support": "[0,4log2+r*epsilon+ell]",
            "laplace_multiplier": (
                "Phi_ell(s)*((1-exp(-epsilon*s))/epsilon)^r*M_ext(s)/s"
            ),
            "autocorrelation_zero_order": "exactly 2r",
            "rh_equivalent_energy": True,
            "estimate_proved": False,
        },
        "spectral_tail": {
            "dirichlet_polynomial": ("D_X(t)=sum_(n<=X) beta(n)*n^(-1/2-it)"),
            "plancherel": ("E(X)=(1/(2pi))*integral |Bhat(t)|^2*|D_X(t)|^2 dt"),
            "trivial_source_bound": "|D_X(t)|<=4*sqrt(X)",
            "critical_cutoff": (
                "T_kappa^crit(X)=exp(kappa*sqrt(log X)), fixed kappa>0"
            ),
            "critical_tail_exponent": (
                "energy on |t|>=T_kappa^crit(X) is at most X^(1-kappa^2/log(2)+o(1))"
            ),
            "critical_rh_criterion": (
                "RH iff the spectral energy on |t|<=exp(sqrt(log(2)*log(X))) is X^o(1)"
            ),
            "critical_scope": (
                "kappa=sqrt(log(2)) gives an X^o(1) tail; larger fixed "
                "kappa gives power saving; no arithmetic optimality is claimed"
            ),
            "subpower_cutoff": (
                "T_theta(X)=exp((log X)^(1/2+theta)), fixed 0<theta<1/2"
            ),
            "reduced_criterion": (
                "RH iff the spectral energy on |t|<=T_theta(X) is X^o(1), "
                "for any one fixed theta in (0,1/2)"
            ),
            "superpower_tail": (
                "for every fixed theta in (0,1/2) and A>0, the energy on "
                "|t|>=T_theta(X) is O_(A,theta,fixed)(X^(-A))"
            ),
            "general_cutoff_condition": ("log(T(X))/sqrt(log X) tends to infinity"),
            "fixed_power_corollary": (
                "the tail on |t|>=X^delta is O_(A,delta,fixed)(X^(-A))"
            ),
        },
        "partial_product_replay": partial_smoother_panel(),
        "notch_replay": notch_panel(),
        "envelope_replay": envelope_panel(),
        "scope": {
            "fixed_parameters": True,
            "theta_fixed_in_open_interval_zero_one_half": True,
            "critical_constant_is_method_threshold_not_optimality_claim": True,
            "horizon_dependent_filter": False,
            "low_frequency_estimate": False,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "partial_convolution_levels": PARTIAL_LEVEL_CAP,
            "binary_envelope_exponent": ENVELOPE_EXPONENT_CAP,
            "difference_order": REPLAY_ORDER_CAP,
            "zeta_zeros": 0,
            "finite_fields": 0,
            "curves": 0,
            "l_functions": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    print(rendered, end="")


if __name__ == "__main__":
    main()
