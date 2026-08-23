#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t105107_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105107 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105107(unittest.TestCase):
    def test_frozen_dependency_is_authenticated(self) -> None:
        dependency = V.dependency_checkpoint()
        self.assertEqual(dependency["commit"], V.BASE_COMMIT)
        self.assertEqual(dependency["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(dependency["artifact_matches_live_producer"])

    def test_off_centre_beta_includes_self_derivative_and_other_node(self) -> None:
        row = V.off_centre_top_jet_fixture()
        self.assertEqual(row["beta"], "45/56")
        self.assertEqual(row["pick_value_y"], "56/45")
        self.assertEqual(row["optimal_H_infinity_norm"], "56/45")

    def test_off_centre_top_jet_is_exact_and_optimal(self) -> None:
        row = V.off_centre_top_jet_fixture()
        self.assertTrue(row["top_jet_congruences_verified"])
        self.assertEqual(row["pick_matrix_at_optimum"], [["0"]])
        self.assertFalse(row["norm_one_pick_matrix_psd"])
        self.assertTrue(row["all_rational_poles_outside_closed_disk"])

    def test_cluster_inner_selector_attains_checkpoint_7_lower_bound(self) -> None:
        row = V.sharp_cluster_fixture()
        self.assertEqual(row["optimal_H_infinity_norm"], "625")
        self.assertEqual(row["checkpoint_7_blaschke_lower_bound"], "625")
        self.assertTrue(row["lower_bound_attained_exactly"])

    def test_cluster_inner_selector_improves_reduced_polynomial(self) -> None:
        row = V.sharp_cluster_fixture()
        self.assertEqual(row["checkpoint_7_reduced_polynomial_norm"], "676")
        self.assertLess(
            F(row["optimal_H_infinity_norm"]),
            F(row["checkpoint_7_reduced_polynomial_norm"]),
        )
        self.assertTrue(row["selector_real_and_even"])

    def test_cluster_exterior_poles_are_explicit(self) -> None:
        row = V.sharp_cluster_fixture()
        self.assertEqual(row["exterior_poles"], ["-5", "5"])
        self.assertTrue(row["all_exterior_poles_outside_closed_disk"])

    def test_direct_two_node_pick_extremal_interpolates(self) -> None:
        row = V.direct_pick_fixture()
        self.assertEqual(row["nodes"], ["0", "1/2"])
        self.assertEqual(row["values"], ["-1/3", "1/5"])
        self.assertEqual(row["extremal"], "b_{1/3}(z)")
        self.assertEqual(row["optimal_norm"], "1")

    def test_direct_pick_threshold_is_singular_and_load_bearing(self) -> None:
        row = V.direct_pick_fixture()
        self.assertEqual(row["pick_principal_minors_at_optimum"][-1], "0")
        self.assertFalse(row["norm_9_over_10_pick_matrix_psd"])
        self.assertTrue(row["off_diagonal_pick_condition_load_bearing"])

    def test_symmetric_forced_inner_reduction_gives_ordinary_values(self) -> None:
        row = V.symmetric_selector_fixture()
        self.assertEqual(row["forced_inner"], "z")
        self.assertEqual(row["target_values_y"], ["-2", "2"])
        self.assertEqual(row["optimal_H"], "4z")

    def test_full_pick_matrix_rejects_diagonal_only_threshold(self) -> None:
        row = V.symmetric_selector_fixture()
        self.assertFalse(row["diagonal_threshold_full_matrix_psd"])
        self.assertFalse(row["norm_three_full_matrix_psd"])
        self.assertEqual(row["pick_matrix_at_optimum"], [["16", "16"], ["16", "16"]])

    def test_symmetric_optimal_selector_is_real_even(self) -> None:
        row = V.symmetric_selector_fixture()
        self.assertEqual(row["optimal_W"], "4z^2")
        self.assertEqual(row["optimal_norm"], "4")
        self.assertTrue(row["real_even_optimal_selector"])

    def test_target_residue_is_preserved(self) -> None:
        row = V.residue_fixture()
        self.assertEqual(row["target_selector_local_series"], ["0", "1"])
        self.assertEqual(row["target_principal_coefficient"], "7/3")
        self.assertEqual(row["target_weighted_residue"], "7/3")
        self.assertTrue(row["exact_L105105_residue_mechanism_preserved"])

    def test_nontarget_residue_is_annihilated_and_edge_scope_is_honest(self) -> None:
        row = V.residue_fixture()
        self.assertEqual(row["nontarget_selector_local_series"], ["0"])
        self.assertEqual(row["nontarget_weighted_residue"], "0")
        self.assertFalse(row["selector_minimizes_weighted_product_for_nonuniform_h"])

    def test_forced_exponent_and_normalization_mutations_fail(self) -> None:
        firewall = V.mutation_firewalls()
        self.assertTrue(
            firewall["using_target_exponent_d_instead_of_d_minus_1_rejected"]
        )
        self.assertTrue(firewall["omitting_target_blaschke_derivative_rejected"])
        self.assertTrue(
            firewall["using_nontarget_exponent_d_minus_1_rejected"]
        )

    def test_prior_art_and_exterior_pole_firewalls_remain_closed(self) -> None:
        firewall = V.mutation_firewalls()
        self.assertFalse(firewall["diagonal_pick_inequalities_are_sufficient"])
        self.assertFalse(firewall["reduced_polynomial_selector_always_boundary_optimal"])
        self.assertFalse(
            firewall["exterior_rational_poles_can_be_ignored_on_larger_windows"]
        )
        self.assertFalse(
            firewall["accepted_actual_xi_pick_kernel_used_as_interpolation_theorem"]
        )
        self.assertFalse(firewall["historical_colliding_L91014_used_as_dependency"])

    def test_committed_artifact_matches_producer_and_content(self) -> None:
        artifact = json.loads(
            (ROOT / "results" / "verification.json").read_text(encoding="utf-8")
        )
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))

    def test_scope_remains_open(self) -> None:
        scope = V.build_payload()["scope"]
        self.assertTrue(scope["disk_forced_inner_factorization_proved"])
        self.assertTrue(scope["top_jet_problem_reduced_to_value_interpolation"])
        self.assertTrue(scope["finite_pick_matrix_optimal_norm_characterization_proved"])
        self.assertTrue(scope["optimal_constant_boundary_modulus_selector_exists"])
        self.assertTrue(scope["rectifiable_jordan_residue_identity_preserved"])
        self.assertFalse(scope["reduced_polynomial_selector_always_boundary_optimal"])
        self.assertFalse(scope["intrinsic_coalescence_conditioning_removed"])
        self.assertFalse(scope["xi_event_manifest_constructed"])
        self.assertFalse(scope["xi_conformal_coordinates_certified"])
        self.assertFalse(scope["xi_pick_norm_estimated_cofinally"])
        self.assertFalse(scope["xi_unweighted_quotient_edges_estimated"])
        self.assertFalse(scope["xi_weighted_edge_asymptotics_proved"])
        self.assertFalse(scope["strict_xi_jet_coherence_margin_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
