#!/usr/bin/env python3
"""Bounded replay for the moving-support probability-carrier phase diagram."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_moving_support_carrier_phase_diagram.json"

SOURCE_COMMIT = "19f274c9335ecffb357e296b3fd5fefdeba5f3fd"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_VARIATIONAL_PROBABILITY_CARRIER_OPTIMUM.md": "d216e254e550c3f3cad49e3dac29da2b0b76e760",
    "research/l-families/atlas/function_field/ffps_variational_probability_carrier_optimum.py": "f7a8628858f2a23bc4b9f164ea0cde1601c03235",
    "research/l-families/atlas/function_field/ffps_variational_probability_carrier_optimum.json": "a37d9b0bf1c43bed0df268a764427fa6c3870211",
    "tests/test_ffps_variational_probability_carrier_optimum.py": "6a8c9d45391014df212f4e2773be0d7a3e57e2e8",
}

LOG_X_ROWS = (100.0, 400.0, 1600.0)
SUPPORT_EXPONENTS = (0.0, 0.05, 0.1, 1.0 / 6.0, 1.0 / 3.0)
LOG_192 = math.log(192.0)


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


def parabolic_norms(support: float) -> dict[str, float]:
    if not math.isfinite(support) or support <= 0.0:
        raise ValueError("support must be positive and finite")
    return {
        "detector_L2_squared": 12.0 / support**3,
        "detector_supremum": 6.0 / support**2,
        "detector_total_variation": 24.0 / support**2,
    }


def centered_test_norm_squared(field_length: float) -> float:
    if not math.isfinite(field_length) or field_length <= 0.0:
        raise ValueError("field length must be positive and finite")
    return field_length**3 / 12.0


def sharp_prefix_bound(energy: float, field_length: float) -> float:
    if not math.isfinite(energy) or energy < 0.0:
        raise ValueError("energy must be nonnegative and finite")
    return math.sqrt(energy * centered_test_norm_squared(field_length))


def renormalized_energy(energy: float, field_length: float) -> float:
    if not math.isfinite(energy) or energy < 0.0:
        raise ValueError("energy must be nonnegative and finite")
    if not math.isfinite(field_length) or field_length <= 0.0:
        raise ValueError("field length must be positive and finite")
    return field_length**3 * energy


def parabolic_renormalized_forward_cost(log_x: float, support: float) -> float:
    if not math.isfinite(log_x) or log_x < 0.0:
        raise ValueError("log_x must be nonnegative and finite")
    if not math.isfinite(support) or support < 1.0:
        raise ValueError("support must be finite and at least one")
    return 900.0 * ((log_x + support) / support) ** 4


def trivial_dilution_schedule_exponent(width_power: float) -> float:
    if not math.isfinite(width_power) or not 0.0 <= width_power < 3.0:
        raise ValueError("width power must lie in [0, 3)")
    return 1.0 / (3.0 - width_power)


def projected_exponential_variance(z: float) -> float:
    if not math.isfinite(z) or z < 0.0:
        raise ValueError("z must be nonnegative and finite")
    if z == 0.0:
        return 0.0
    if z < 1.0e-4:
        return (
            z**2 / 12.0
            - z**3 / 12.0
            + 17.0 * z**4 / 360.0
            - 7.0 * z**5 / 360.0
            + 43.0 * z**6 / 6720.0
        )
    mean = -math.expm1(-z) / z
    second_moment = -math.expm1(-2.0 * z) / (2.0 * z)
    return second_moment - mean**2


def projected_laplace_cost(field_length: float, alpha: float) -> float:
    if not math.isfinite(field_length) or field_length <= 0.0:
        raise ValueError("field length must be positive and finite")
    if not math.isfinite(alpha) or alpha <= 0.0:
        raise ValueError("alpha must be positive and finite")
    variance = projected_exponential_variance(alpha * field_length)
    return math.sqrt(field_length * variance) / alpha


def autocorrelation_second_moment(prefix: float) -> float:
    if not math.isfinite(prefix):
        raise ValueError("prefix must be finite")
    return -2.0 * prefix**2


def pythagorean_energy(
    prefix: float, field_length: float, shape_defect_energy: float
) -> float:
    if not math.isfinite(prefix):
        raise ValueError("prefix must be finite")
    if not math.isfinite(field_length) or field_length <= 0.0:
        raise ValueError("field length must be positive and finite")
    if not math.isfinite(shape_defect_energy) or shape_defect_energy < 0.0:
        raise ValueError("shape defect energy must be nonnegative and finite")
    return 12.0 * prefix**2 / field_length**3 + shape_defect_energy


def reverse_abscissa_choice(
    support_slope: float, target_real_part: float
) -> dict[str, float]:
    if not math.isfinite(support_slope) or support_slope < 0.0:
        raise ValueError("support slope must be nonnegative and finite")
    if not math.isfinite(target_real_part) or target_real_part <= 0.0:
        raise ValueError("target real part must be positive and finite")
    alpha = target_real_part / (2.0 * (support_slope + 1.0))
    partial_sum_exponent = alpha * support_slope
    convergence_abscissa = alpha + partial_sum_exponent
    return {
        "alpha": alpha,
        "partial_sum_exponent": partial_sum_exponent,
        "convergence_abscissa": convergence_abscissa,
        "margin_to_target": target_real_part - convergence_abscissa,
    }


def optimized_laplace_parameter(support: float) -> float:
    if not math.isfinite(support) or support <= 0.0:
        raise ValueError("support must be positive and finite")
    return 1.5 / support


def zero_exclusion_boundary(support_exponent: float) -> float:
    if not math.isfinite(support_exponent) or support_exponent < 0.0:
        raise ValueError("support exponent must be nonnegative and finite")
    return 0.5 + 1.5 * support_exponent


def trivial_log_energy_bound(log_x: float, log_support: float) -> float:
    if not math.isfinite(log_x) or log_x <= 0.0:
        raise ValueError("log_x must be positive and finite")
    if not math.isfinite(log_support):
        raise ValueError("log_support must be finite")
    return LOG_192 + log_x - 3.0 * log_support


def phase_rows() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for log_x in LOG_X_ROWS:
        schedules = (
            ("fixed_support", math.log(2.0)),
            ("logarithmic_support", math.log(log_x)),
            ("cubic_escape", log_x / 3.0),
        )
        for name, log_support in schedules:
            log_bound = trivial_log_energy_bound(log_x, log_support)
            rows.append(
                {
                    "log_X": log_x,
                    "schedule_code": float(
                        {
                            "fixed_support": 0,
                            "logarithmic_support": 1,
                            "cubic_escape": 2,
                        }[name]
                    ),
                    "log_support": log_support,
                    "trivial_log_energy_bound": log_bound,
                    "bound_exponent_over_log_X": log_bound / log_x,
                }
            )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    rows = phase_rows()
    cubic = [row for row in rows if row["schedule_code"] == 2.0]
    if any(abs(row["trivial_log_energy_bound"] - LOG_192) > 1.0e-12 for row in cubic):
        raise AssertionError("cubic escape failed to flatten the trivial energy bound")
    reverse = reverse_abscissa_choice(3.0, 0.2)
    if not reverse["margin_to_target"] > 0.0:
        raise AssertionError("logarithmic-support reverse margin failed")
    sharp_row = {
        "field_length": 2.0,
        "extremal_energy": parabolic_norms(2.0)["detector_L2_squared"],
    }
    sharp_row["recovered_prefix_bound"] = sharp_prefix_bound(
        sharp_row["extremal_energy"], sharp_row["field_length"]
    )
    if abs(sharp_row["recovered_prefix_bound"] - 1.0) > 1.0e-12:
        raise AssertionError("centered-moment extremizer failed")
    forward_cost_rows = [
        {
            "log_X": log_x,
            "support": support,
            "cost": parabolic_renormalized_forward_cost(log_x, support),
            "polylog_upper_bound": 900.0 * (1.0 + log_x) ** 4,
        }
        for log_x, support in ((100.0, 1.0), (100.0, 100.0), (100.0, 1.0e12))
    ]
    if any(row["cost"] > row["polylog_upper_bound"] for row in forward_cost_rows):
        raise AssertionError("all-support parabolic forward gate failed")
    projected_rows = [
        {
            "z": z,
            "variance": projected_exponential_variance(z),
            "centered_variance_upper_bound": z**2 / 12.0,
            "unprojected_second_moment_upper_bound": 1.0 / (2.0 * z),
        }
        for z in (0.01, 0.1, 1.0, 10.0)
    ]
    if any(
        row["variance"]
        > min(
            row["centered_variance_upper_bound"],
            row["unprojected_second_moment_upper_bound"],
        )
        + 1.0e-14
        for row in projected_rows
    ):
        raise AssertionError("projected exponential variance bound failed")

    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "reverse_theorem": {
            "support_gate": "pointwise-uniform S_X<=X^(gamma+o(1))",
            "energy_gate": "E_Q(X)=X^o(1)",
            "conclusion": "no zeta zero with Re(rho)>1/2+3*gamma/2; gamma=0 gives RH",
            "prefix_bound": "|B(X)|^2<=E_Q(X)*(log(X)+S_X)^3/12",
            "positivity_needed": False,
            "support_envelope_needed": False,
        },
        "width_renormalized_theorem": {
            "definition": "R_Q(X)=(log(X)+S_X)^3*E_Q(X)",
            "reverse": "R_Q(X)=X^o(1) implies RH for every finite support schedule",
            "forward_gate": "(log(X)+S_X)^4*(||J_X||_infinity+Var(J_X))^2=X^o(1)",
            "parabolic_equivalence": "RH iff R_S(X)=X^o(1) for every schedule S_X>=1",
            "dilution_firewall": "the width factor is the sharp centered-moment recovery price",
            "bounded_forward_cost_rows": forward_cost_rows,
        },
        "renormalization_exponent_trichotomy": {
            "p_below_3": "S_X=X^(1/(3-p)) makes L_X^p*E_S(X)=O(1) by Young",
            "p_equal_3": "exact all-support RH equivalence",
            "p_above_3": "current RH forward gate retains S_X^(p-3) for S_X much larger than log(X)",
            "firewall": "the p>3 row is a limit of the proved forward bound, not an impossibility theorem",
            "sample_trivial_schedule_exponents": [
                {
                    "width_power_p": width_power,
                    "support_exponent": trivial_dilution_schedule_exponent(width_power),
                }
                for width_power in (0.0, 1.0, 2.0, 2.5)
            ],
        },
        "centered_moment_duality": {
            "identities": "integral(H_X)=0 and integral(t*H_X)=-B(X)",
            "center": "(log(X)+S_X)/2",
            "test_norm_squared": "(log(X)+S_X)^3/12",
            "sharp_inequality": "E_Q(X)*(log(X)+S_X)^3>=12*|B(X)|^2",
            "equality_field": "H(t)=6*B*(L-2*t)/L^3 on [0,L]",
            "information_firewall": "sharp for support, zero mass, first moment, and L2 data; not for full beta convolution structure",
            "bounded_extremizer_row": sharp_row,
            "autocorrelation_identity": "integral(u^2*C_X(u),u)=-2*B(X)^2",
            "pythagorean_decomposition": "E_Q=12*|B(X)|^2/L^3+||H_X-H_X_star||_2^2",
        },
        "projected_laplace_replay": {
            "variance": "V(z)=(1-exp(-2z))/(2z)-((1-exp(-z))/z)^2",
            "exact_cost": "sqrt(L*V(alpha*L))/(alpha*Qhat(alpha))",
            "positive_carrier_bound": "exp(alpha*S)*min(L^(3/2)/sqrt(12),1/(sqrt(2)*alpha^(3/2)))",
            "variance_rows": projected_rows,
            "limit": "alpha->0 recovers the sharp centered-moment inequality",
        },
        "independent_laplace_replay": {
            "parameter": "alpha=3/(2*S)",
            "cost": "exp(3/2)/sqrt(2)*(2*S/3)^(3/2)",
            "scope": "requires nonnegative normalized Q; reproduces the wedge exponent",
        },
        "forward_theorem": {
            "assumptions": "RH and (log(X)+S_X)*(||J_X||_infinity+Var(J_X))^2=X^o(1)",
            "conclusion": "E_Q(X)=X^o(1)",
            "parabolic_corollary": "the forward gate holds for every S_X>=1",
        },
        "parabolic_escape": {
            "norms": "||J_S||_2^2=12/S^3, ||J_S||_infinity=6/S^2, Var(J_S)=24/S^2",
            "trivial_bound": "E_S(X)<=192*X/S^3",
            "renormalized_trivial_bound": "R_S(X)<=192*X*((log(X)+S)/S)^3",
            "cubic_scale": "S_X>=X^(1/3) makes the energy O(1) unconditionally",
            "firewall": "positive-power support does not give a full RH reverse theorem from raw energy",
        },
        "reverse_margin_control": reverse,
        "zero_exclusion_rows": [
            {
                "support_exponent_gamma": exponent,
                "excluded_zero_real_parts_above": zero_exclusion_boundary(exponent),
            }
            for exponent in SUPPORT_EXPONENTS
        ],
        "phase_rows": rows,
        "proof_ledger": {
            "exact_carrier_moment_identities": "PROVED",
            "exact_signed_autocorrelation_second_moment": "PROVED",
            "exact_pythagorean_mertens_shape_decomposition": "PROVED",
            "sharp_centered_support_energy_inequality": "PROVED",
            "optimal_constant_in_abstract_information_class": "PROVED",
            "exact_projected_finite_alpha_carrier_inequality": "PROVED",
            "arbitrary_support_renormalized_reverse_RH_gate": "PROVED",
            "all_support_parabolic_renormalized_RH_equivalence": "PROVED",
            "support_exponent_zero_exclusion_wedge": "PROVED",
            "subpower_support_reverse_RH_gate": "PROVED",
            "moving_support_forward_gate_under_RH": "PROVED",
            "parabolic_forward_gate_for_all_supports_at_least_one": "PROVED",
            "parabolic_trivial_energy_bound": "PROVED",
            "cubic_normalization_escape": "PROVED",
            "width_renormalization_removes_trivial_dilution": "PROVED",
            "subcubic_width_power_trivial_dilution_schedule": "PROVED",
            "supercubic_all_support_forward_gate": "NOT PROVED",
            "positive_power_support_full_RH_gate": "NOT PROVED",
            "arithmetic_improvement_over_centered_wedge": "NOT PROVED",
            "parabolic_beta_estimate_in_RH_bearing_region": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "log_horizons": len(LOG_X_ROWS),
            "support_schedules": 3,
            "beta_terms": 0,
            "zeta_zeros": 0,
            "primes": 0,
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
