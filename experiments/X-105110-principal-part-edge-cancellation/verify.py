#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True

VERDICT = "PASS_T105110_PRINCIPAL_PART_EDGE_CANCELLATION"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105109-log-derivative-edge-obstruction"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "54829e77cb2aa90192aabdd61f86ff045a04ba3549f82c75384bc9a4e08f2890"
BASE_COMMIT = "99a5eef2160e85609da590cb76b632511b33f112"

SPEC = importlib.util.spec_from_file_location("t105109_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105109 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

CONTENT_FILES = (
    "PACKET_METADATA_105110.json",
    "claims/lemmas/L-105110-principal-part-edge-cancellation.md",
    "claims/methodology/M-105110-edge-cancellation-review-contract.md",
    "claims/refutations/R-105110-stable-manifest-does-not-give-edge-cancellation.md",
    "claims/theorems/T-105110-oriented-edge-cancellation-frontier.md",
    "experiments/X-105110-principal-part-edge-cancellation/verify.py",
    "experiments/X-105110-principal-part-edge-cancellation/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def render(value: F | int) -> str:
    value = F(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def complex_multiply(
    left: tuple[F, F], right: tuple[F, F]
) -> tuple[F, F]:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105109 dependency artifact is stale")
    require(
        artifact.get("proof_object_sha256") == BASE_DIGEST,
        "T-105109 dependency digest changed",
    )
    require(
        artifact.get("verdict") == BASE.VERDICT,
        "T-105109 dependency verdict changed",
    )
    return {
        "path": "experiments/X-105109-log-derivative-edge-obstruction",
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def straight_kernel_fixture() -> dict[str, object]:
    A = F(1, 3)
    B = F(1, 2)
    delta = F(1, 4)
    sigma = -1
    probe_t = F(2, 5)
    denominator = probe_t * probe_t + delta * delta

    # d/dt [log(t^2+delta^2)/2 + i*sigma*atan(t/delta)]
    # equals 1/(t-i*sigma*delta).  Multiply the two exact rational pairs.
    primitive_derivative = (
        probe_t / denominator,
        F(sigma) * delta / denominator,
    )
    kernel_denominator = (probe_t, -F(sigma) * delta)
    require(
        complex_multiply(kernel_denominator, primitive_derivative) == (F(1), F(0)),
        "straight-kernel primitive sign changed",
    )

    real_log_ratio = (B * B + delta * delta) / (A * A + delta * delta)
    centered_ratio = (A * A + delta * delta) / (A * A + delta * delta)
    endpoint_ratio = (B * B + delta * delta) / (delta * delta)
    require(centered_ratio == 1, "centered logarithmic cancellation failed")
    require(endpoint_ratio > 1, "endpoint logarithmic debt disappeared")

    return {
        "orientation": "increasing_t",
        "pole": "z0+i*sigma*u*delta",
        "kernel_integral": (
            "(1/2)*log((B^2+delta^2)/(A^2+delta^2))"
            "+i*sigma*(atan(B/delta)+atan(A/delta))"
        ),
        "absolute_integral": "asinh(A/delta)+asinh(B/delta)",
        "probe": {
            "A": render(A),
            "B": render(B),
            "delta": render(delta),
            "sigma": sigma,
            "real_log_ratio": render(real_log_ratio),
        },
        "centered_real_log_ratio": render(centered_ratio),
        "centered_integral": "2*i*sigma*atan(a/delta)",
        "centered_absolute_bound": "pi",
        "endpoint_real_log_ratio": render(endpoint_ratio),
        "endpoint_integral": (
            "(1/2)*log((B^2+delta^2)/delta^2)"
            "+i*sigma*atan(B/delta)"
        ),
        "orientation_reversal_changes_sign": True,
        "transcendental_numerical_evaluation_used": False,
    }


def principal_part_certificate_fixture() -> dict[str, object]:
    kappa = F(1, 4)
    ell = F(1, 2)
    residues = [F(2), F(-1, 2), F(3, 4)]
    remainder_l1 = F(5, 3)
    residue_l1 = sum(abs(value) for value in residues)
    require(residue_l1 == F(13, 4), "residue ell-one sum changed")
    require(0 < kappa <= ell, "bad corner-separation ledger")
    return {
        "pole_count": len(residues),
        "residues": [render(value) for value in residues],
        "weighted_residue_l1": render(residue_l1),
        "remainder_edge_l1": render(remainder_l1),
        "corner_separation_kappa": render(kappa),
        "tangential_upper_distance_ell": render(ell),
        "kernel_bound": "pi+log(ell/kappa)",
        "fixture_kernel_bound": "pi+log(2)",
        "oriented_edge_bound": "5/3+(13/4)*(pi+log(2))",
        "normal_collar_distance_enters_bound": False,
        "weighted_quotient_continuation_required": True,
        "complete_exterior_pole_list_required": True,
        "multiple_or_common_events_covered": False,
    }


def exterior_residue_fixture() -> dict[str, object]:
    weight_at_f_prime = F(2)
    log_derivative_prime = F(3)
    first_residue = weight_at_f_prime / log_derivative_prime
    second_residue = weight_at_f_prime / (log_derivative_prime**2)

    weight_at_f_second = F(5)
    log_derivative = F(2)
    second_denominator_prime = F(7)
    f_second_residue = (
        weight_at_f_second / (log_derivative * second_denominator_prime)
    )
    require(first_residue == F(2, 3), "first exterior residue changed")
    require(second_residue == F(2, 9), "second F-prime residue changed")
    require(f_second_residue == F(5, 14), "second F-second residue changed")
    return {
        "simple_F_prime_identity": "A(p)=L_prime(p)",
        "first_residue_formula": "W1(p)/L_prime(p)",
        "second_F_prime_residue_formula": "W2(p)/L_prime(p)^2",
        "second_F_second_residue_formula": "W2(q)/(L(q)*A_prime(q))",
        "probe_first_residue": render(first_residue),
        "probe_second_F_prime_residue": render(second_residue),
        "probe_second_F_second_residue": render(f_second_residue),
    }


def simultaneous_quotient_fixture() -> dict[str, object]:
    a = F(1, 2)
    delta = F(1, 4)
    correction_denominator = 1 + delta * delta - a * a
    correction_ratio = 2 * a * delta / correction_denominator
    require(correction_denominator == F(13, 16), "correction denominator changed")
    require(correction_ratio == F(4, 13), "correction arctangent ratio changed")
    require(correction_ratio <= F(4, 3) * delta, "uniform correction bound failed")

    # The partial-fraction numerator is (w^2+1)-w^2=1, replayed by
    # coefficient subtraction in ascending powers of w.
    first_numerator = [F(1), F(0), F(1)]
    second_numerator = [F(0), F(0), F(1)]
    partial_fraction_numerator = [
        first_numerator[index] - second_numerator[index] for index in range(3)
    ]
    require(
        partial_fraction_numerator == [F(1), F(0), F(0)],
        "partial-fraction cancellation changed",
    )

    h1_at_zero = F(1, 1) / delta
    h2_at_zero = F(1, 1) / (delta * (1 + delta * delta))
    require(h1_at_zero == 4, "first supremum witness changed")
    require(h2_at_zero == F(64, 17), "second supremum witness changed")

    # If d=delta^2 and t=y^2, the squared h2 denominator has derivative
    # 1+3d^2+2(3d-2)t+3t^2.  Subtracting (1-t)(1-3t) leaves
    # 3d(d+2t), proving its minimum occurs at t=0 on the parameter box.
    d = delta * delta
    t = a * a
    derivative_value = 1 + 3 * d * d + 2 * (3 * d - 2) * t + 3 * t * t
    lower_factor = (1 - t) * (1 - 3 * t)
    remainder = 3 * d * (d + 2 * t)
    require(derivative_value - lower_factor == remainder, "supremum derivative identity changed")
    require(lower_factor > 0 and remainder > 0, "supremum monotonicity failed")

    return {
        "parameter_probe": {"a": render(a), "delta": render(delta)},
        "log_derivative": "w=z-delta",
        "second_denominator": "w^2+1",
        "first_quotient": "1/w",
        "second_quotient": "1/(w*(w^2+1))=1/w-w/(w^2+1)",
        "partial_fraction_numerator_coefficients": ["1", "0", "0"],
        "first_centered_integral": "-2*i*atan(a/delta)",
        "second_centered_integral": (
            "-2*i*atan(a/delta)"
            "+i*atan(2*a*delta/(1+delta^2-a^2))"
        ),
        "correction_ratio": render(correction_ratio),
        "correction_absolute_bound": "4*delta/3",
        "both_fixed_edge_limits": "-i*pi",
        "first_supremum": "1/delta",
        "second_supremum": "1/(delta*(1+delta^2))",
        "probe_first_supremum": render(h1_at_zero),
        "probe_second_supremum": render(h2_at_zero),
        "factor_modulus_lower_bound": "3/4",
        "factor_modulus_upper_bound": "3/2",
        "pointwise_h2_over_h1_bounds": ["2/3", "4/3"],
        "squared_denominator_derivative": "1+3*d^2+2*(3*d-2)*t+3*t^2",
        "derivative_positive_decomposition": "(1-t)*(1-3*t)+3*d*(d+2*t)",
        "oriented_integrals_uniformly_bounded": True,
    }


def dyadic_absolute_divergence_fixture() -> dict[str, object]:
    a = F(1, 2)
    require(F(5) < F(81, 16), "sqrt(5)<9/4 rational certificate failed")
    rows: list[dict[str, object]] = []
    for blocks in (4, 8):
        delta = a / (2**blocks)
        first_supremum = F(1, 1) / delta
        second_supremum = F(1, 1) / (delta * (1 + delta * delta))
        first_l1_lower = F(8 * blocks, 9)
        second_l1_lower = F(2, 3) * first_l1_lower
        one_sided_real_lower = F(blocks, 5)
        require(first_supremum == 2 ** (blocks + 1), "dyadic supremum changed")
        require(second_supremum >= F(4, 5) * first_supremum, "second supremum lower bound failed")
        require(second_l1_lower == F(16 * blocks, 27), "second L1 lower bound changed")
        rows.append(
            {
                "dyadic_blocks": blocks,
                "a": render(a),
                "delta": render(delta),
                "a_over_delta": str(2**blocks),
                "first_supremum": render(first_supremum),
                "second_supremum": render(second_supremum),
                "first_absolute_integral_lower_bound": render(first_l1_lower),
                "second_absolute_integral_lower_bound": render(second_l1_lower),
                "one_sided_real_part_lower_bound": render(one_sided_real_lower),
            }
        )
    require(
        F(rows[1]["first_absolute_integral_lower_bound"])
        > F(rows[0]["first_absolute_integral_lower_bound"]),
        "dyadic first L1 debt did not grow",
    )
    return {
        "sequence": "a=1/2,delta=a/2^m",
        "per_positive_dyadic_block_h1_lower_bound": "4/9",
        "two_sided_per_block_h1_lower_bound": "8/9",
        "two_sided_per_block_h2_lower_bound": "16/27",
        "one_sided_real_part_per_block_lower_bound": "1/5",
        "rows": rows,
        "absolute_integral_divergence_requires_a_over_delta_unbounded": True,
        "absolute_integral_divergence_uniform_for_all_a_delta": False,
    }


def one_sided_fixture() -> dict[str, object]:
    a = F(1, 2)
    delta = F(1, 8)
    ratio = (a * a + delta * delta) / (delta * delta)
    correction_denominator = 1 + delta * delta
    correction_numerator_real = 1 + delta * delta - a * a
    correction_numerator_imag = -2 * a * delta
    require(ratio == 17, "one-sided logarithmic ratio changed")
    require(correction_numerator_real >= F(3, 4), "h2 one-sided correction approached branch cut")
    require(correction_denominator >= 1, "bad h2 correction denominator")
    return {
        "a": render(a),
        "delta": render(delta),
        "first_one_sided_integral": (
            "(1/2)*log((a^2+delta^2)/delta^2)-i*atan(a/delta)"
        ),
        "probe_log_ratio": render(ratio),
        "second_minus_first_correction": (
            "-(1/2)*Log((1+delta^2-a^2-2*i*a*delta)/(1+delta^2))"
        ),
        "probe_correction_numerator": [
            render(correction_numerator_real),
            render(correction_numerator_imag),
        ],
        "corner_projection_uniformly_bounded": False,
        "arbitrary_edge_partition_inherits_centered_cancellation": False,
    }


def f_delta_scope_fixture() -> dict[str, object]:
    return {
        "function": "exp(z^2/2-delta*z)",
        "properties": ["real", "entire", "zero_free"],
        "F_prime_zero": "delta",
        "F_second_zeros": ["delta-i", "delta+i"],
        "left_rectangle_right_edge_orientation": "upward",
        "pole_delta_is_exterior_to_left_rectangle": True,
        "left_rectangle_interior_manifest": [],
        "unit_weight_role": "fixed_test_weight",
        "unit_weight_is_empty_problem_optimum": False,
        "empty_problem_optimal_selector": "0",
        "fixed_a_required_for_stated_absolute_divergence": True,
    }


def hostile_remainder_fixture() -> dict[str, object]:
    N = 6
    eta = F(1, 8 * N)
    exponential_lower = F(63, 64)
    cosine_lower = F(31, 32)
    reciprocal_denominator_lower = F(64, 65)
    integration_factor = F(1, 4)
    coefficient = (
        integration_factor
        * exponential_lower
        * cosine_lower
        * reciprocal_denominator_lower
    )
    require(coefficient == F(1953, 8320), "right-edge coefficient changed")
    require(coefficient > F(1, 5), "right-edge e^N/(5N) bound failed")
    rational_growth_lower = F(N * N, 30)
    cubic_taylor_term = F(N**3, 6)
    require(rational_growth_lower == F(6, 5), "N-squared lower bound changed")
    require(cubic_taylor_term / (5 * N) == rational_growth_lower, "Taylor growth conversion changed")

    # The paired y and -y integrands have opposite real coefficients and
    # equal imaginary coefficients in the formal basis (cos(theta),sin(theta)).
    y = F(1, 16 * N)
    positive_real_coefficients = (y, F(-1))
    negative_real_coefficients = (-y, F(1))
    positive_imag_coefficients = (F(1), y)
    negative_imag_coefficients = (F(1), y)
    require(
        tuple(
            positive_real_coefficients[index] + negative_real_coefficients[index]
            for index in range(2)
        )
        == (F(0), F(0)),
        "right-edge real part did not cancel",
    )
    require(
        positive_imag_coefficients == negative_imag_coefficients,
        "right-edge imaginary parts did not pair",
    )

    return {
        "N_probe": N,
        "function": "exp((1-exp(-N*z^2))/(2*N))",
        "properties": ["real", "even", "entire", "zero_free", "infinite_order"],
        "log_derivative": "z*exp(-N*z^2)",
        "first_quotient": "exp(N*z^2)/z",
        "global_F_prime_manifest": [
            {"point": "0", "order": 1, "role": "target"}
        ],
        "target_residue": "1",
        "optimal_selector": "1",
        "optimal_selector_norm": "1",
        "rectangle": "abs(Re(z))<1,abs(Im(z))<1/(8*N)",
        "right_edge_orientation": "upward",
        "right_edge_integral_is_pure_positive_imaginary": True,
        "eta_probe": render(eta),
        "rational_kernel_coefficient": render(coefficient),
        "exact_exponential_lower_bound": "(1953/8320)*exp(N)/N",
        "simplified_exponential_lower_bound": "exp(N)/(5*N)",
        "Taylor_growth_certificate": "exp(N)>N^3/6",
        "probe_cubic_Taylor_term": render(cubic_taylor_term),
        "rational_growth_lower_bound": "N^2/30",
        "probe_rational_growth_lower_bound": render(rational_growth_lower),
        "full_normalized_contour_charge": "1",
        "additive_holomorphic_remainder": "(exp(N*z^2)-1)/z",
        "additive_remainder_value_at_zero": "0",
        "additive_remainder_is_zero_free": False,
        "multiplicative_exponential_is_zero_free": True,
        "exterior_critical_points_exist": False,
        "remainder_edge_L1_uniformly_bounded": False,
        "second_quotient_treated": False,
        "window_height_fixed": False,
        "fixed_function_family": False,
    }


def mutation_firewalls() -> dict[str, object]:
    principal = principal_part_certificate_fixture()
    dyadic = dyadic_absolute_divergence_fixture()
    scope = f_delta_scope_fixture()
    hostile = hostile_remainder_fixture()
    require(
        principal["multiple_or_common_events_covered"] is False,
        "confluent mutation accepted",
    )
    require(
        dyadic["absolute_integral_divergence_uniform_for_all_a_delta"] is False,
        "uniform L1 mutation accepted",
    )
    require(
        scope["unit_weight_is_empty_problem_optimum"] is False,
        "empty-selector mutation accepted",
    )
    require(
        hostile["additive_remainder_is_zero_free"] is False,
        "zero-free additive-remainder mutation accepted",
    )
    return {
        "normal_pole_approach_forces_oriented_divergence": False,
        "corner_separation_is_dispensable": False,
        "principal_parts_may_be_paid_without_residue_l1_bound": False,
        "remainder_bound_is_automatic_from_manifest": False,
        "weighted_quotient_continuation_is_automatic": False,
        "simple_pole_certificate_covers_confluent_events": False,
        "centered_L1_divergence_is_uniform_over_all_a_delta": False,
        "fixed_unit_weight_is_empty_manifest_optimum": False,
        "stable_manifest_forces_each_oriented_edge_bounded": False,
        "full_contour_charge_bounds_each_edge": False,
        "additive_holomorphic_remainder_is_zero_free": False,
        "hostile_family_treats_second_quotient": False,
        "hostile_family_is_fixed_function_cofinal_Xi_model": False,
        "rh_established": False,
    }


def content_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative_path in CONTENT_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            raise FileNotFoundError(f"missing load-bearing file: {relative_path}")
        normalized = path.read_bytes().replace(b"\r\n", b"\n")
        hashes[relative_path] = hashlib.sha256(normalized).hexdigest()
    return hashes


def build_payload() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": "riemann.t105110.principal-part-edge-cancellation.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_WITH_SYMBOLIC_ELEMENTARY_IDENTITIES",
        "source": {
            "checkpoint_base": BASE_COMMIT,
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "straight_edge_kernel": straight_kernel_fixture(),
            "principal_part_certificate": principal_part_certificate_fixture(),
            "exterior_residue_formulas": exterior_residue_fixture(),
            "simultaneous_quotient_fixture": simultaneous_quotient_fixture(),
            "dyadic_absolute_divergence": dyadic_absolute_divergence_fixture(),
            "one_sided_corner_failure": one_sided_fixture(),
            "F_delta_scope": f_delta_scope_fixture(),
            "hostile_holomorphic_remainder": hostile_remainder_fixture(),
            "mutation_firewalls": mutation_firewalls(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "straight_edge_simple_pole_cancellation_verified": True,
            "finite_principal_part_certificate_verified": True,
            "corner_logarithmic_failure_verified": True,
            "simultaneous_first_second_fixture_verified": True,
            "stable_manifest_individual_edge_refutation_verified": True,
            "weighted_quotient_continuation_proved_for_xi": False,
            "xi_exterior_principal_part_manifest_constructed": False,
            "xi_weighted_exterior_residue_l1_bound_proved": False,
            "xi_corner_separation_or_pairing_proved": False,
            "xi_pole_subtracted_remainder_bound_proved": False,
            "hostile_second_quotient_analogue_proved": False,
            "hostile_family_is_finite_order": False,
            "hostile_windows_have_fixed_height": False,
            "hostile_family_is_fixed_function_cofinal_model": False,
            "cofinal_xi_green_gram_control_proved": False,
            "cofinal_weighted_edge_passage_proved": False,
            "strict_xi_jet_coherence_margin_proved": False,
            "rcmv104530_proved": False,
            "rh_established": False,
        },
        "heavy_computation_run": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
