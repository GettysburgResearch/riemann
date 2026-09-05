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
SPEC = importlib.util.spec_from_file_location("t105109_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105109 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105109(unittest.TestCase):
    def test_frozen_dependency_is_authenticated(self) -> None:
        dependency = V.dependency_checkpoint()
        self.assertEqual(
            dependency["path"],
            "experiments/X-105108-green-gram-selector-conditioning",
        )
        self.assertEqual(dependency["commit"], V.BASE_COMMIT)
        self.assertEqual(dependency["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(dependency["artifact_matches_live_producer"])

    def test_margin_ledger_uses_product_margin(self) -> None:
        row = V.margin_ledger_fixture()
        self.assertEqual(row["first_quotient_formula"], "1/L")
        self.assertEqual(row["second_quotient_formula"], "1/(L*A)")
        self.assertEqual(row["m1"], "1")
        self.assertEqual(row["m2"], "1")
        self.assertEqual(row["m12"], "10")
        self.assertFalse(row["m12_equals_m1_times_m2"])

    def test_constant_modulus_gives_exact_weighted_suprema(self) -> None:
        row = V.margin_ledger_fixture()
        self.assertEqual(row["weighted_first_supremum"], "2")
        self.assertEqual(row["weighted_second_supremum"], "3/10")
        self.assertTrue(row["constant_boundary_modulus_gives_exact_weighted_supremum"])

    def test_first_gauge_collapses_L_and_preserves_jets(self) -> None:
        row = V.gauge_fixture()
        self.assertEqual(row["P_at_boundary"], "8/27")
        self.assertEqual(row["Q1_prime_at_boundary"], "8/27")
        self.assertEqual(row["t1"], "-45/8")
        self.assertEqual(row["transformed_L_first_gauge"], "1/3")
        self.assertTrue(row["specified_interior_jets_preserved"])
        self.assertTrue(row["epsilon_zero_collapses_denominator"])

    def test_second_gauge_has_no_cross_term_and_is_not_same_manifest(self) -> None:
        row = V.gauge_fixture()
        self.assertEqual(row["Q2_prime_at_boundary"], "0")
        self.assertEqual(row["Q2_second_at_boundary"], "16/27")
        self.assertEqual(row["t2"], "-189/64")
        self.assertEqual(row["transformed_L_second_gauge"], "5/3")
        self.assertEqual(row["transformed_A_second_gauge"], "7/20")
        self.assertFalse(row["complete_derivative_manifest_preserved"])

    def test_log_derivative_polynomial_identities_are_exact(self) -> None:
        row = V.derivative_polynomial_fixture()
        self.assertTrue(row["A_equals_L_squared_plus_L_prime"])
        self.assertTrue(row["A_equals_P_of_z_squared_over_s_squared"])
        self.assertEqual(row["P_minus_one_in_s"], ["-1", "1"])
        self.assertEqual(row["P_zero_in_s"], ["0", "0", "1"])
        self.assertEqual(row["P_one_in_s"], ["1", "-5", "2"])
        self.assertEqual(row["P_at_s_in_s"], ["0", "0", "-2"])

    def test_discriminant_certificate_is_symbolically_replayed(self) -> None:
        row = V.derivative_polynomial_fixture()
        self.assertEqual(row["discriminant_in_s"], ["0", "0", "0", "108", "9", "8"])
        self.assertEqual(row["discriminant_factor"], "s^3*(8*s^2+9*s+108)")

    def test_complete_manifests_and_common_zero_firewall(self) -> None:
        row = V.event_manifest_fixture()
        self.assertEqual(row["first_disk_manifest"], [{"point": "0", "order": 1, "role": "target"}])
        self.assertEqual(len(row["second_disk_manifest"]), 3)
        self.assertEqual(row["P_root_order"], "gamma<-1<0<alpha<1<s<beta")
        self.assertTrue(row["all_interior_events_simple"])
        self.assertFalse(row["common_F_prime_F_second_events"])
        self.assertEqual(row["A_at_zero"], "1")
        self.assertEqual(row["A_at_outer_F_prime_zeros"], "-2")
        self.assertFalse(row["boundary_poles_for_strict_parameter_range"])

    def test_rational_sign_oracle_is_exact(self) -> None:
        row = V.rational_checkpoint_fixture()
        self.assertEqual(
            row["sign_values"],
            ["-110401/10000", "1/100", "11219/320000", "-2153/50000", "-10049/5000", "4763/1250"],
        )
        self.assertEqual(row["negative_root_interval"], ["-2", "-1"])
        self.assertEqual(row["alpha_interval"], ["3/8", "2/5"])
        self.assertEqual(row["positive_root_interval"], ["101/100", "3"])
        self.assertFalse(row["floating_point_root_finding_used"])

    def test_rational_boundary_values_are_exact(self) -> None:
        row = V.rational_checkpoint_fixture()
        self.assertEqual(row["first_boundary_quotient_at_one"], "101")
        self.assertEqual(row["second_boundary_quotient_at_one"], "-1030301/20098")
        self.assertEqual(row["tau_two_interval"], ["5/2", "8/3"])

    def test_target_laurent_residues_are_both_one(self) -> None:
        row = V.local_residue_fixture()
        self.assertEqual(row["first_laurent_terms_at_zero"], ["z^-1", "100/101*z"])
        self.assertEqual(row["second_laurent_terms_at_zero"], ["z^-1", "299/101*z"])
        self.assertEqual(row["first_target_residue"], "1")
        self.assertEqual(row["second_target_residue"], "1")

    def test_selector_beta_sign_and_cancellation_are_load_bearing(self) -> None:
        row = V.selector_fixture()
        self.assertEqual(row["first_selector"], "1")
        self.assertEqual(row["second_beta_zero"], "-alpha")
        self.assertEqual(row["second_target_value"], "-1/alpha")
        self.assertEqual(row["second_selector_at_zero"], "1")
        self.assertTrue(row["second_nontargets_cancelled"])

    def test_selector_norm_and_golden_limit_are_exact(self) -> None:
        row = V.selector_fixture()
        self.assertEqual(row["second_selector_norm"], "1/alpha")
        self.assertEqual(row["second_selector_boundary_modulus"], "1/alpha")
        self.assertEqual(row["P_one_factorization"], "(x+1)*(x^2-3*x+1)")
        self.assertEqual(row["alpha_limit"], "(3-sqrt(5))/2")
        self.assertEqual(row["second_selector_norm_limit"], "(3+sqrt(5))/2")
        self.assertTrue(row["selector_norms_bounded_as_s_decreases_to_one"])
        self.assertFalse(row["floating_point_arithmetic_used"])

    def test_boundary_obstruction_grows_while_full_contours_stay_fixed(self) -> None:
        row = V.boundary_obstruction_fixture()
        self.assertEqual(row["sequence"], "s_n=1+1/n")
        self.assertEqual(row["first_quotient_sequence"], "n+1")
        self.assertEqual(
            row["second_quotient_sequence"],
            "-(n+1)^3/(2*n^2+n-2)",
        )
        self.assertEqual(row["second_absolute_lower_bound"], "n/3")
        first_values = [F(value) for value in row["first_quotient_at_one"]]
        second_values = [abs(F(value)) for value in row["second_quotient_at_one"]]
        self.assertGreater(first_values[1], first_values[0])
        self.assertGreater(second_values[1], second_values[0])
        self.assertEqual(row["first_full_weighted_contour_integral"], "1")
        self.assertEqual(row["second_full_weighted_contour_integral"], "1")
        self.assertFalse(row["oriented_contour_integral_divergence_claimed"])
        self.assertTrue(row["phase_sensitive_edge_cancellation_remains_open"])

    def test_mutation_firewalls_remain_closed(self) -> None:
        firewall = V.mutation_firewalls()
        false_keys = {
            "second_quotient_is_inverse_A_only",
            "second_quotient_is_inverse_L_squared_plus_A",
            "m12_equals_m1_times_m2",
            "upper_log_derivative_bounds_supply_required_lower_margin",
            "constant_modulus_selector_attenuates_bad_supremum_edge",
            "finite_interior_jets_determine_boundary_margins",
            "gauge_preserves_complete_derivative_manifest",
            "bounded_selector_norms_control_absolute_edges",
            "interior_manifest_authenticates_exterior_collar",
            "second_nontarget_locations_fixed_in_s",
            "absolute_edge_divergence_implies_oriented_integral_divergence",
            "explicit_family_is_Xi",
            "parameter_endpoints_included",
            "rh_established",
        }
        self.assertEqual(set(firewall), false_keys)
        self.assertTrue(all(firewall[key] is False for key in false_keys))

    def test_committed_artifact_matches_producer_and_hash_manifest(self) -> None:
        artifact = json.loads((ROOT / "results" / "verification.json").read_text(encoding="utf-8"))
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))
        self.assertEqual(len(artifact["content_sha256"]), 7)

    def test_proof_digest_is_canonical_and_scope_remains_open(self) -> None:
        artifact = V.build_payload()
        claimed = artifact.pop("proof_object_sha256")
        canonical = json.dumps(artifact, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(claimed, hashlib.sha256(canonical).hexdigest())
        scope = artifact["scope"]
        self.assertTrue(scope["log_derivative_denominator_ledger_verified"])
        self.assertTrue(scope["bounded_selector_edge_obstruction_verified"])
        self.assertFalse(scope["gauge_preserves_complete_derivative_manifest"])
        self.assertFalse(scope["bounded_selector_norms_control_absolute_edges"])
        self.assertFalse(scope["oriented_contour_integral_divergence_proved"])
        self.assertFalse(scope["phase_sensitive_oriented_edge_cancellation_refuted"])
        self.assertFalse(scope["xi_actual_pole_manifest_constructed"])
        self.assertFalse(scope["xi_exterior_collar_certified"])
        self.assertFalse(scope["xi_log_derivative_lower_margins_proved"])
        self.assertFalse(scope["xi_oriented_edge_cancellation_proved"])
        self.assertFalse(scope["cofinal_weighted_edge_decay_proved"])
        self.assertFalse(scope["strict_xi_jet_coherence_margin_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
