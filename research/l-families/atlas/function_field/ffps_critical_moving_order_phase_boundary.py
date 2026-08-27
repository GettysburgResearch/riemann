#!/usr/bin/env python3
"""Bounded replay for the critical moving-order beta phase boundary."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from decimal import ROUND_CEILING, Decimal, localcontext
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_critical_moving_order_phase_boundary.json"

MICROSCOPE_COMMIT = "d30994d59d27adb6d9686a10854ae097092bf54b"
MICROSCOPE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_FIXED_SUPPORT_BETA_MESOSCOPIC_MICROSCOPE.md": "1690fbbe217030c23bbed6d18954ebd44c3fce92",
    "research/l-families/atlas/function_field/ffps_fixed_support_beta_mesoscopic_microscope.py": "c29cb7b79f12e0dbc77cf631b9aeb6a80c63648a",
    "research/l-families/atlas/function_field/ffps_fixed_support_beta_mesoscopic_microscope.json": "5a970b9d687f1809617c37136b5f4646ea9a10e7",
    "tests/test_ffps_fixed_support_beta_mesoscopic_microscope.py": "845e89e23f5c29214d018c3976a483605c7134b4",
}
SMOOTHER_COMMIT = "b631040b76d696dbc69cadde7af240077f605c94"
SMOOTHER_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_INFINITE_DYADIC_BOX_BANDPASS_SMOOTHER.md": "01d3ea427883fb761f6301f71d9dd05c552c5056",
    "research/l-families/atlas/function_field/ffps_infinite_dyadic_box_bandpass_smoother.py": "2ba0f30c9bd67cdb01af639d320daf8133b5bb77",
    "research/l-families/atlas/function_field/ffps_infinite_dyadic_box_bandpass_smoother.json": "7a38b5f943a8dc1c0afde8d1cc91f35118b767ca",
    "tests/test_ffps_infinite_dyadic_box_bandpass_smoother.py": "d6a30d654d46edfa01add55cec55b0b3253a12b0",
}

LOG_X_ROWS = (100.0, 400.0, 1600.0, 6400.0)
PHASE_ROWS = (
    (0.0, 0.25),
    (0.5, 0.25),
    (1.0, 0.5),
    (1.0, 1.0),
    (1.0, 2.0),
)


def check_source_blobs() -> None:
    for commit, blobs in (
        (MICROSCOPE_COMMIT, MICROSCOPE_BLOBS),
        (SMOOTHER_COMMIT, SMOOTHER_BLOBS),
    ):
        for path, expected in blobs.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=3,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"frozen source blob mismatch: {path}")


def mean_and_variance() -> tuple[float, float]:
    e = math.e
    return (
        2.0 / (e - 1.0),
        2.0 * (e * e - 3.0 * e + 1.0) / (e - 1.0) ** 2,
    )


def p_fourier_modulus_squared(frequency: float) -> float:
    if not math.isfinite(frequency):
        raise ValueError("frequency must be finite")
    e = math.e
    atom = (e * e + 1.0 - 2.0 * e * math.cos(frequency)) / (
        (e - 1.0) ** 2 * (1.0 + frequency * frequency)
    )
    return atom * atom


def log_p_fourier_modulus_squared(frequency: float) -> float:
    if not math.isfinite(frequency):
        raise ValueError("frequency must be finite")
    e = math.e
    coefficient = 4.0 * e / (e - 1.0) ** 2
    sine = math.sin(frequency / 2.0)
    return 2.0 * (
        math.log1p(coefficient * sine * sine) - math.log1p(frequency * frequency)
    )


def critical_log_frequency(log_x: float) -> float:
    if not math.isfinite(log_x) or log_x <= 0.0:
        raise ValueError("log_x must be positive and finite")
    return math.sqrt(math.log(2.0) * log_x)


def continuous_order(log_x: float, alpha: float, multiplier: float) -> float:
    if not math.isfinite(alpha) or not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must lie in [0,1]")
    if not math.isfinite(multiplier) or multiplier <= 0.0:
        raise ValueError("variance multiplier must be positive and finite")
    _, variance = mean_and_variance()
    log_t = critical_log_frequency(log_x)
    return multiplier * variance * math.exp(2.0 * log_t) / log_x**alpha


def _decimal_integer_order(
    log_x: float, alpha: float, multiplier: float, *, precision: int
) -> int:
    """Evaluate the declared variance-multiple ceiling at high precision."""
    if not math.isfinite(log_x) or log_x <= 0.0:
        raise ValueError("log_x must be positive and finite")
    if not math.isfinite(alpha) or not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must lie in [0,1]")
    if not math.isfinite(multiplier) or multiplier <= 0.0:
        raise ValueError("variance multiplier must be positive and finite")
    with localcontext() as context:
        context.prec = precision
        one = Decimal(1)
        two = Decimal(2)
        e = context.exp(one)
        variance = two * (e * e - Decimal(3) * e + one) / (e - one) ** 2
        log_x_decimal = Decimal(str(log_x))
        alpha_decimal = Decimal(str(alpha))
        multiplier_decimal = Decimal(str(multiplier))
        log_t = context.sqrt(context.ln(two) * log_x_decimal)
        denominator = context.exp(alpha_decimal * context.ln(log_x_decimal))
        order = multiplier_decimal * variance * context.exp(two * log_t) / denominator
        return max(1, int(order.to_integral_value(rounding=ROUND_CEILING)))


def integer_order(log_x: float, alpha: float, multiplier: float) -> int:
    """Return a precision-stable ceiling for c=multiplier*sigma^2."""
    order_90 = _decimal_integer_order(log_x, alpha, multiplier, precision=90)
    order_130 = _decimal_integer_order(log_x, alpha, multiplier, precision=130)
    if order_90 != order_130:
        raise ArithmeticError("order ceiling was not stable across decimal precisions")
    return order_130


def exact_endpoint_decay(log_x: float, alpha: float, multiplier: float) -> float:
    log_t = critical_log_frequency(log_x)
    order = integer_order(log_x, alpha, multiplier)
    frequency = math.exp(log_t)
    return -order * log_p_fourier_modulus_squared(frequency / order)


def predicted_endpoint_decay(log_x: float, alpha: float, multiplier: float) -> float:
    return log_x**alpha / multiplier


def smoother_stair_decay(log_x: float, ell: float = 1.0) -> float:
    if not math.isfinite(ell) or ell <= 0.0:
        raise ValueError("ell must be positive and finite")
    log_t = critical_log_frequency(log_x)
    log_a = math.log(ell) + log_t
    level = math.floor(log_a / math.log(2.0))
    if level < 3:
        return 0.0
    return math.log(2.0) * (level - 1) * (level - 2)


def endpoint_rows() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for log_x in LOG_X_ROWS:
        continuous = continuous_order(log_x, 1.0, 1.0)
        order = integer_order(log_x, 1.0, 1.0)
        exact = exact_endpoint_decay(log_x, 1.0, 1.0)
        predicted = predicted_endpoint_decay(log_x, 1.0, 1.0)
        rows.append(
            {
                "log_X": log_x,
                "log_T_star": critical_log_frequency(log_x),
                "log_order": math.log(order),
                "order_is_subpower_ratio": math.log(order) / log_x,
                "high_precision_minus_float_ceiling": order - math.ceil(continuous),
                "exact_ladder_decay": exact,
                "predicted_ladder_decay": predicted,
                "decay_ratio": exact / predicted,
                "smoother_stair_decay": smoother_stair_decay(log_x),
                "stair_decay_over_log_X": smoother_stair_decay(log_x) / log_x,
            }
        )
    return rows


def phase_rows() -> list[dict[str, float]]:
    log_x = LOG_X_ROWS[-1]
    rows: list[dict[str, float]] = []
    for alpha, multiplier in PHASE_ROWS:
        exact = exact_endpoint_decay(log_x, alpha, multiplier)
        stair = smoother_stair_decay(log_x)
        rows.append(
            {
                "alpha": alpha,
                "constant_over_variance": multiplier,
                "ladder_decay_over_log_X": exact / log_x,
                "stair_decay_over_log_X": stair / log_x,
                "certified_margin_over_log_X": (stair - exact) / log_x,
            }
        )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    _, variance = mean_and_variance()
    rows = endpoint_rows()
    if abs(rows[-1]["decay_ratio"] - 1.0) >= abs(rows[0]["decay_ratio"] - 1.0):
        raise AssertionError("endpoint cumulant control failed to improve")
    if not rows[-1]["order_is_subpower_ratio"] < rows[0]["order_is_subpower_ratio"]:
        raise AssertionError("critical order failed its subpower control")
    if not rows[-1]["stair_decay_over_log_X"] > rows[0]["stair_decay_over_log_X"]:
        raise AssertionError("stair decay failed to approach its limit")

    return {
        "source_contract": {
            "microscope_commit": MICROSCOPE_COMMIT,
            "microscope_git_blobs": MICROSCOPE_BLOBS,
            "smoother_commit": SMOOTHER_COMMIT,
            "smoother_git_blobs": SMOOTHER_BLOBS,
        },
        "constants": {
            "variance_sigma_squared": variance,
            "critical_boundary_constant": variance,
            "natural_log_2": math.log(2.0),
        },
        "phase_theorem": {
            "critical_frequency": "T_*(X)=exp(sqrt(log(2)*log(X)))",
            "order_family": "m_{alpha,c}(X)=ceil(c*T_*^2/(log X)^alpha)",
            "proved_equivalence_region": "0<=alpha<1 and c>0, or alpha=1 and c>=sigma^2",
            "canonical_boundary_order": "m_dagger(X)=ceil(sigma^2*T_*^2/log X)",
            "criterion": "RH iff E_{m_dagger(X)}(X)=X^o(1)",
        },
        "endpoint_rows": rows,
        "phase_rows": phase_rows(),
        "proof_ledger": {
            "uniform_small_argument_ladder_expansion": "PROVED",
            "low_high_window_comparison": "PROVED",
            "phase_region_RH_equivalence": "PROVED",
            "boundary_constant_sigma_squared": "PROVED FOR THIS COMPARISON",
            "criterion_failure_below_boundary": "NOT PROVED",
            "beta_energy_estimate": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "log_horizons": len(LOG_X_ROWS),
            "phase_rows": len(PHASE_ROWS),
            "finite_field_elements": 0,
            "primes": 0,
            "zeta_zeros": 0,
            "random_samples": 0,
            "quadratures": 0,
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
