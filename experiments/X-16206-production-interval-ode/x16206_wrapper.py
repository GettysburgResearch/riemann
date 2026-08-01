"""Wrapper and cofinal schedule emission for X-16206."""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
from typing import Any
from x16206_common import GAMMA, WRAPPER_SCHEMA, fstr, sha_file, write_json

def build_wrapper(outdir: Path, primitive: dict[str, Any], primitive_path: Path) -> Path:
    max_sigma = max(
        Fraction(row["sigma_sq_interval"][1]) for row in primitive["separation_and_pole_data"]
    )
    phase_ledger = {
        "schema": "riemann.x16206-phase-ledger.v1",
        "source_sha256": primitive["source_sha256"],
        "sigma_sq_upper": fstr(max_sigma),
        "window": ["17/8", "9/4"],
        "radial_scale_R": GAMMA,
        "cube_root_q": 46,
        "classification": "DIRECTED_RATIONAL_PHASE_LEDGER",
    }
    phase_sha = write_json(outdir / "phase-ledger.json", phase_ledger)

    endpoint_ledger = {
        "schema": "riemann.x16206-endpoint-ledger.v1",
        "source_sha256": primitive["source_sha256"],
        "p": 4,
        "effective_derivative_l1_upper": 1_000_000,
        "alias_cutoff": 1000,
        "zeta4_minus_one_upper": "9083/108045",
        "classification": "SOURCE_BOUND_RADIAL_ENDPOINT_REMAINDER",
    }
    endpoint_sha = write_json(outdir / "endpoint-ledger.json", endpoint_ledger)

    # These two ledgers are deliberately distinguished from the newly produced
    # radial primitive. They preserve the existing theorem-level wrapper inputs.
    gram_ledger = {
        "schema": "riemann.x16206-gram-ledger.v1",
        "source_sha256": primitive["source_sha256"],
        "first_alias_gram": "identity by exact leakage normalization",
        "bounds": ["1/5", "5"],
        "classification": "ANALYTIC_L16227_LEDGER_NOT_A_NEW_NUMERICAL_GRAM_REPLAY",
    }
    gram_sha = write_json(outdir / "gram-ledger.json", gram_ledger)
    support_ledger = {
        "schema": "riemann.x16206-support-ledger.v1",
        "source_sha256": primitive["source_sha256"],
        "R_block": [50_000, 100_000],
        "families": [
            {"name": "line-centered", "mean_square_upper": "1/1000"},
            {"name": "horizontal", "mean_square_upper": "1/1000"},
        ],
        "classification": "ANALYTIC_COFINAL_LEDGER_NOT_AN_EXPLICIT_ZERO_REPLAY",
    }
    support_sha = write_json(outdir / "support-average-ledger.json", support_ledger)

    agg = primitive["aggregate_for_x16204"]
    cert = {
        "schema": WRAPPER_SCHEMA,
        "phase_partition": {
            "sigma_sq_upper": fstr(max_sigma),
            "omega_left": "17/8",
            "omega_right": "9/4",
            "higher_alias_gap": "1/50",
            "stationary_second_derivative_lower": "11/12",
            "fold_third_lower": "8",
            "fold_third_upper": "60/7",
            "radial_scale_R": GAMMA,
            "cube_root_q": 46,
            "airy_t_radius_upper": "1/46",
            "airy_frequency_radius_upper": "9/2116",
            "interval_phase_ledger_sha256": phase_sha,
        },
        "radial_replay": {
            "classification": "DIRECTED_INTERVAL_ODE",
            "finite_interval_length": agg["finite_interval_length"],
            "transition_bound": agg["transition_bound"],
            "initial_error_upper": agg["initial_error_upper"],
            "residual_sup_upper": agg["residual_sup_upper"],
            "tail_l2_sq_upper": agg["tail_l2_sq_upper"],
            "derivative_transition_bound": agg["derivative_transition_bound"],
            "derivative_initial_error_upper": agg["derivative_initial_error_upper"],
            "derivative_residual_sup_upper": agg["derivative_residual_sup_upper"],
            "derivative_tail_l2_sq_upper": agg["derivative_tail_l2_sq_upper"],
            "claimed_l2_sq_upper": agg["claimed_l2_sq_upper"],
            "claimed_derivative_l2_sq_upper": agg["claimed_derivative_l2_sq_upper"],
            "producer_sha256": primitive["producer_sha256"],
            "primitive_sha256": primitive["primitive_sha256"],
        },
        "poisson_endpoint": {
            "p": 4,
            "pi_lower": "3",
            "zeta4_minus_one_upper": "9083/108045",
            "derivative_l1_upper": "1000000",
            "v_lower": "126",
            "lambda_lower": "126",
            "alias_cutoff_K": 1000,
            "post_cutoff_zeta_tail_upper": "1/3000000000",
            "claimed_point_upper": "1/3000000",
            "claimed_l2_sq_upper": "1/100000000000",
            "polylog_channel_sha256": endpoint_sha,
        },
        "profile_gram": {
            "lower": "1/5",
            "upper": "5",
            "directed_gram_sha256": gram_sha,
        },
        "cofinal_block": {
            "measure_lower": "1",
            "exceptional_measure_upper": "1/100",
            "mean_square_families": [
                {"name": "line-centered", "mean_square_upper": "1/1000", "threshold": "1/10"},
                {"name": "horizontal", "mean_square_upper": "1/1000", "threshold": "1/10"},
            ],
            "support_average_ledger_sha256": support_sha,
        },
        "scalarization": {
            "log_R_lower": "11",
            "bounded_main_correction_upper": "1",
            "deterministic_error_upper": "1/5",
            "claimed_relative_epsilon_upper": "2/3",
        },
        "tail_hierarchy": {
            "a_lower": "11",
            "d4_upper": "1/100000000",
            "d8_lower": "1",
            "target_constant_upper": "2",
            "gap_constant_lower": "1/10",
            "claimed_ground_correction_ratio_upper": "1/900000",
        },
        "production_bindings": {
            "source_sha256": primitive["source_sha256"],
            "actual_primitive_file_sha256": sha_file(primitive_path),
            "actual_primitive_object_sha256": primitive["primitive_sha256"],
            "radial_status": "PRODUCTION",
            "gram_status": "ANALYTIC_LEDGER",
            "support_average_status": "ANALYTIC_LEDGER",
        },
    }
    path = outdir / "wrapper-certificate.json"
    write_json(path, cert)
    return path


def build_schedule(outdir: Path, primitive: dict[str, Any]) -> None:
    levels = []
    for j in range(8):
        gamma = GAMMA * (8**j)
        q = int(gamma ** (1 / 3))
        while (q + 1) ** 3 <= gamma:
            q += 1
        while q**3 > gamma:
            q -= 1
        levels.append(
            {
                "level": j,
                "gamma": gamma,
                "cube_root_q": q,
                "radial_residual_scale_upper": f"181/{gamma}",
                "suggested_radial_z_cutoff": max(4096, int(round(gamma ** (1 / 3))) * 128),
                "mode_window": "0,4,...,4*ceil(log(lambda)^2)",
                "status": "EMITTER_PARAMETER_SET_NOT_YET_RUN" if j else "BASE_PRIMITIVE_EMITTED",
            }
        )
    schedule = {
        "schema": "riemann.x16206-cofinal-emitter-schedule.v1",
        "base_source_sha256": primitive["source_sha256"],
        "gamma_schedule": "100000*8^j",
        "levels": levels,
        "asymptotic_notes": {
            "compact_radial_error": "O(1/gamma)",
            "tail_energy": "choose Z_j->infinity; O(1/Z_j)",
            "horizontal_log_moment": "O(log(Z_j)^2/Z_j)",
            "remaining_nonradial_inputs": "growing Gram and support-average ledgers",
        },
    }
    write_json(outdir / "cofinal-schedule.json", schedule)
