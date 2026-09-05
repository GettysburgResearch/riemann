#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t105110_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105110 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105110(unittest.TestCase):
    def test_frozen_dependency_is_authenticated(self) -> None:
        dependency = V.dependency_checkpoint()
        self.assertEqual(
            dependency["path"],
            "experiments/X-105109-log-derivative-edge-obstruction",
        )
        self.assertEqual(dependency["commit"], V.BASE_COMMIT)
        self.assertEqual(dependency["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(dependency["artifact_matches_live_producer"])

    def test_straight_kernel_primitive_and_orientation_are_exact(self) -> None:
        row = V.straight_kernel_fixture()
        self.assertEqual(row["orientation"], "increasing_t")
        self.assertEqual(
            row["kernel_integral"],
            "(1/2)*log((B^2+delta^2)/(A^2+delta^2))+i*sigma*(atan(B/delta)+atan(A/delta))",
        )
        self.assertEqual(row["absolute_integral"], "asinh(A/delta)+asinh(B/delta)")
        self.assertTrue(row["orientation_reversal_changes_sign"])
        self.assertFalse(row["transcendental_numerical_evaluation_used"])

    def test_centered_log_cancels_but_endpoint_log_does_not(self) -> None:
        row = V.straight_kernel_fixture()
        self.assertEqual(row["centered_real_log_ratio"], "1")
        self.assertEqual(row["centered_absolute_bound"], "pi")
        self.assertEqual(row["endpoint_real_log_ratio"], "5")
        self.assertNotEqual(row["endpoint_real_log_ratio"], "1")

    def test_finite_principal_part_certificate_tracks_every_debt(self) -> None:
        row = V.principal_part_certificate_fixture()
        self.assertEqual(row["pole_count"], 3)
        self.assertEqual(row["weighted_residue_l1"], "13/4")
        self.assertEqual(row["remainder_edge_l1"], "5/3")
        self.assertEqual(row["fixture_kernel_bound"], "pi+log(2)")
        self.assertFalse(row["normal_collar_distance_enters_bound"])
        self.assertTrue(row["weighted_quotient_continuation_required"])
        self.assertTrue(row["complete_exterior_pole_list_required"])
        self.assertFalse(row["multiple_or_common_events_covered"])

    def test_exterior_residue_formulas_are_replayed(self) -> None:
        row = V.exterior_residue_fixture()
        self.assertEqual(row["simple_F_prime_identity"], "A(p)=L_prime(p)")
        self.assertEqual(row["probe_first_residue"], "2/3")
        self.assertEqual(row["probe_second_F_prime_residue"], "2/9")
        self.assertEqual(row["probe_second_F_second_residue"], "5/14")

    def test_simultaneous_first_second_quotient_identity_and_sign(self) -> None:
        row = V.simultaneous_quotient_fixture()
        self.assertEqual(row["log_derivative"], "w=z-delta")
        self.assertEqual(row["second_denominator"], "w^2+1")
        self.assertEqual(row["partial_fraction_numerator_coefficients"], ["1", "0", "0"])
        self.assertEqual(row["first_centered_integral"], "-2*i*atan(a/delta)")
        self.assertEqual(
            row["second_centered_integral"],
            "-2*i*atan(a/delta)+i*atan(2*a*delta/(1+delta^2-a^2))",
        )
        self.assertEqual(row["both_fixed_edge_limits"], "-i*pi")

    def test_suprema_and_pointwise_comparison_are_exact(self) -> None:
        row = V.simultaneous_quotient_fixture()
        self.assertEqual(row["first_supremum"], "1/delta")
        self.assertEqual(row["second_supremum"], "1/(delta*(1+delta^2))")
        self.assertEqual(row["probe_first_supremum"], "4")
        self.assertEqual(row["probe_second_supremum"], "64/17")
        self.assertEqual(row["factor_modulus_lower_bound"], "3/4")
        self.assertEqual(row["factor_modulus_upper_bound"], "3/2")
        self.assertEqual(row["pointwise_h2_over_h1_bounds"], ["2/3", "4/3"])

    def test_second_supremum_monotonicity_certificate_is_exact(self) -> None:
        row = V.simultaneous_quotient_fixture()
        self.assertEqual(
            row["squared_denominator_derivative"],
            "1+3*d^2+2*(3*d-2)*t+3*t^2",
        )
        self.assertEqual(
            row["derivative_positive_decomposition"],
            "(1-t)*(1-3*t)+3*d*(d+2*t)",
        )
        self.assertTrue(row["oriented_integrals_uniformly_bounded"])

    def test_dyadic_absolute_integral_debt_grows_rationally(self) -> None:
        row = V.dyadic_absolute_divergence_fixture()
        self.assertEqual(row["sequence"], "a=1/2,delta=a/2^m")
        self.assertEqual(row["two_sided_per_block_h1_lower_bound"], "8/9")
        self.assertEqual(row["two_sided_per_block_h2_lower_bound"], "16/27")
        self.assertGreater(
            F(row["rows"][1]["first_absolute_integral_lower_bound"]),
            F(row["rows"][0]["first_absolute_integral_lower_bound"]),
        )
        self.assertGreater(
            F(row["rows"][1]["second_absolute_integral_lower_bound"]),
            F(row["rows"][0]["second_absolute_integral_lower_bound"]),
        )

    def test_fixed_edge_quantifier_is_load_bearing(self) -> None:
        row = V.dyadic_absolute_divergence_fixture()
        self.assertTrue(row["absolute_integral_divergence_requires_a_over_delta_unbounded"])
        self.assertFalse(row["absolute_integral_divergence_uniform_for_all_a_delta"])

    def test_one_sided_corner_failure_retains_logarithmic_debt(self) -> None:
        row = V.one_sided_fixture()
        self.assertEqual(row["probe_log_ratio"], "17")
        self.assertEqual(row["probe_correction_numerator"], ["49/64", "-1/8"])
        self.assertFalse(row["corner_projection_uniformly_bounded"])
        self.assertFalse(row["arbitrary_edge_partition_inherits_centered_cancellation"])

    def test_F_delta_domain_manifest_and_selector_scope(self) -> None:
        row = V.f_delta_scope_fixture()
        self.assertTrue(row["pole_delta_is_exterior_to_left_rectangle"])
        self.assertEqual(row["left_rectangle_interior_manifest"], [])
        self.assertEqual(row["unit_weight_role"], "fixed_test_weight")
        self.assertFalse(row["unit_weight_is_empty_problem_optimum"])
        self.assertEqual(row["empty_problem_optimal_selector"], "0")
        self.assertTrue(row["fixed_a_required_for_stated_absolute_divergence"])

    def test_hostile_family_manifest_residue_and_selector_are_fixed(self) -> None:
        row = V.hostile_remainder_fixture()
        self.assertEqual(row["log_derivative"], "z*exp(-N*z^2)")
        self.assertEqual(row["global_F_prime_manifest"], [{"point": "0", "order": 1, "role": "target"}])
        self.assertEqual(row["target_residue"], "1")
        self.assertEqual(row["optimal_selector"], "1")
        self.assertEqual(row["optimal_selector_norm"], "1")
        self.assertFalse(row["exterior_critical_points_exist"])

    def test_hostile_right_edge_has_exact_rational_growth_certificate(self) -> None:
        row = V.hostile_remainder_fixture()
        self.assertTrue(row["right_edge_integral_is_pure_positive_imaginary"])
        self.assertEqual(row["rational_kernel_coefficient"], "1953/8320")
        self.assertEqual(row["simplified_exponential_lower_bound"], "exp(N)/(5*N)")
        self.assertEqual(row["Taylor_growth_certificate"], "exp(N)>N^3/6")
        self.assertEqual(row["probe_cubic_Taylor_term"], "36")
        self.assertEqual(row["rational_growth_lower_bound"], "N^2/30")
        self.assertEqual(row["probe_rational_growth_lower_bound"], "6/5")

    def test_full_contour_and_holomorphic_remainder_scope_are_distinct(self) -> None:
        row = V.hostile_remainder_fixture()
        self.assertEqual(row["full_normalized_contour_charge"], "1")
        self.assertEqual(row["additive_remainder_value_at_zero"], "0")
        self.assertFalse(row["additive_remainder_is_zero_free"])
        self.assertTrue(row["multiplicative_exponential_is_zero_free"])
        self.assertFalse(row["remainder_edge_L1_uniformly_bounded"])
        self.assertFalse(row["second_quotient_treated"])
        self.assertFalse(row["window_height_fixed"])
        self.assertFalse(row["fixed_function_family"])

    def test_mutation_firewalls_remain_closed(self) -> None:
        firewall = V.mutation_firewalls()
        self.assertEqual(len(firewall), 14)
        self.assertTrue(all(value is False for value in firewall.values()))
        self.assertFalse(firewall["normal_pole_approach_forces_oriented_divergence"])
        self.assertFalse(firewall["corner_separation_is_dispensable"])
        self.assertFalse(firewall["remainder_bound_is_automatic_from_manifest"])
        self.assertFalse(firewall["fixed_unit_weight_is_empty_manifest_optimum"])
        self.assertFalse(firewall["additive_holomorphic_remainder_is_zero_free"])
        self.assertFalse(firewall["rh_established"])

    def test_artifact_matches_live_producer_and_hash_manifest(self) -> None:
        artifact = json.loads((ROOT / "results" / "verification.json").read_text(encoding="utf-8"))
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))
        self.assertEqual(len(artifact["content_sha256"]), 7)

    def test_canonical_digest_and_open_scope(self) -> None:
        artifact = V.build_payload()
        claimed = artifact.pop("proof_object_sha256")
        canonical = json.dumps(artifact, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(claimed, hashlib.sha256(canonical).hexdigest())
        scope = artifact["scope"]
        self.assertTrue(scope["straight_edge_simple_pole_cancellation_verified"])
        self.assertTrue(scope["stable_manifest_individual_edge_refutation_verified"])
        self.assertFalse(scope["weighted_quotient_continuation_proved_for_xi"])
        self.assertFalse(scope["xi_exterior_principal_part_manifest_constructed"])
        self.assertFalse(scope["xi_weighted_exterior_residue_l1_bound_proved"])
        self.assertFalse(scope["xi_corner_separation_or_pairing_proved"])
        self.assertFalse(scope["xi_pole_subtracted_remainder_bound_proved"])
        self.assertFalse(scope["hostile_second_quotient_analogue_proved"])
        self.assertFalse(scope["hostile_family_is_finite_order"])
        self.assertFalse(scope["hostile_windows_have_fixed_height"])
        self.assertFalse(scope["cofinal_weighted_edge_passage_proved"])
        self.assertFalse(scope["strict_xi_jet_coherence_margin_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
