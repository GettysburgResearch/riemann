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
SPEC = importlib.util.spec_from_file_location("t105108_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105108 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105108(unittest.TestCase):
    def test_frozen_dependency_is_authenticated(self) -> None:
        dependency = V.dependency_checkpoint()
        self.assertEqual(dependency["commit"], V.BASE_COMMIT)
        self.assertEqual(dependency["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(dependency["artifact_matches_live_producer"])

    def test_off_centre_green_load_matches_checkpoint_8(self) -> None:
        row = V.off_centre_local_load_fixture()
        self.assertEqual(row["conformal_radius"], "8/9")
        self.assertEqual(row["pseudohyperbolic_product"], "5/7")
        self.assertEqual(row["local_load"], "56/45")
        self.assertTrue(row["checkpoint_8_load_matches"])

    def test_same_phase_pair_attains_diagonal_lower_bound(self) -> None:
        row = V.phase_pair_fixture()
        self.assertEqual(row["same_phase_values"], ["2", "2"])
        self.assertEqual(row["same_phase_optimal_norm"], "2")
        self.assertEqual(row["same_phase_determinant_factor"], "(256/225)*(s-4)^2")

    def test_opposite_phase_pair_attains_gram_upper_bound(self) -> None:
        row = V.phase_pair_fixture()
        self.assertEqual(row["opposite_phase_values"], ["-2", "2"])
        self.assertEqual(row["gram_condition_number"], "4")
        self.assertEqual(row["opposite_phase_optimal_norm"], "4")
        self.assertEqual(row["opposite_phase_gram_upper_bound"], "4")
        self.assertFalse(row["opposite_phase_pick_at_diagonal_threshold_psd"])

    def test_phase_is_load_bearing_at_fixed_magnitudes(self) -> None:
        row = V.phase_pair_fixture()
        self.assertEqual(row["absolute_target_values"], ["2", "2"])
        self.assertNotEqual(
            row["same_phase_optimal_norm"], row["opposite_phase_optimal_norm"]
        )
        self.assertTrue(row["phase_is_load_bearing"])

    def test_compatible_triple_reconstructs_exact_selector(self) -> None:
        row = V.compatible_triple_fixture()
        self.assertEqual(row["target_values_y"], ["-5", "5"])
        self.assertEqual(row["forced_inner"], "z")
        self.assertEqual(row["optimal_H"], "25*z")
        self.assertEqual(row["optimal_W"], "25*z^2")
        self.assertTrue(row["top_jet_congruences_verified"])

    def test_compatible_triple_exposes_gram_amplification(self) -> None:
        row = V.compatible_triple_fixture()
        self.assertEqual(row["maximum_local_load"], "5")
        self.assertEqual(row["gram_condition_number"], "25")
        self.assertEqual(row["gram_upper_bound"], "25")
        self.assertEqual(row["optimal_norm"], "25")

    def test_compatible_cardinal_bound_is_valid_but_not_exact(self) -> None:
        row = V.compatible_triple_fixture()
        self.assertEqual(row["target_product_separation"], "5/13")
        self.assertEqual(row["cardinal_upper_bound"], "26")
        self.assertLess(F(row["optimal_norm"]), F(row["cardinal_upper_bound"]))

    def test_single_target_collision_has_cubic_load(self) -> None:
        row = V.single_target_collision_fixture()
        self.assertEqual(row["pseudohyperbolic_distance"], "1/5")
        self.assertEqual(row["nontarget_order"], 3)
        self.assertEqual(row["pick_value_y"], "-125")
        self.assertEqual(row["optimal_norm"], "125")
        self.assertTrue(row["top_jet_congruences_verified"])

    def test_fixed_manifest_disk_radius_scaling_is_exact(self) -> None:
        row = V.disk_radius_fixture()
        self.assertEqual(row["formula"], "tau_R=4*R^3")
        self.assertEqual(row["radius_one_optimal_norm"], "4")
        self.assertEqual(row["radius_two_optimal_norm"], "32")
        self.assertEqual(row["radius_doubling_factor"], "8")

    def test_collective_determinant_factor_is_exact(self) -> None:
        row = V.collective_three_target_fixture()
        self.assertEqual(
            row["generalized_determinant_factor"],
            "(16/225)*(s-1)*(s^2-62*s+1)",
        )
        self.assertEqual(row["full_squared_norm_factor"], "s^2-62*s+1")
        self.assertEqual(row["full_squared_norm_isolating_interval"], ["61", "62"])

    def test_every_pair_misses_collective_obstruction(self) -> None:
        row = V.collective_three_target_fixture()
        self.assertEqual(row["maximum_pair_optimal_norm"], "2+sqrt(3)")
        self.assertEqual(row["full_optimal_norm"], "4+sqrt(15)")
        self.assertEqual(
            row["adjacent_pair_squared_norm_isolating_interval"], ["13", "14"]
        )
        self.assertTrue(row["full_optimum_strictly_exceeds_every_pair_optimum"])
        self.assertFalse(row["all_two_by_two_pick_conditions_are_sufficient"])

    def test_mutation_firewalls_remain_closed(self) -> None:
        firewall = V.mutation_firewalls()
        self.assertFalse(firewall["absolute_target_values_determine_pick_optimum"])
        self.assertFalse(firewall["local_load_maximum_controls_multi_target_optimum"])
        self.assertFalse(firewall["cardinal_upper_bound_is_always_exact"])
        self.assertFalse(firewall["pairwise_pick_conditions_are_sufficient"])
        self.assertFalse(
            firewall["pairwise_target_separation_controls_full_event_collision_load"]
        )
        self.assertFalse(
            firewall["fixed_manifest_selector_norm_is_disk_radius_independent"]
        )
        self.assertFalse(
            firewall["raw_pick_kernel_condition_number_is_conformally_intrinsic"]
        )
        self.assertFalse(firewall["accepted_actual_xi_pick_kernel_used"])
        self.assertFalse(firewall["rh_established"])

    def test_committed_artifact_matches_producer_and_content(self) -> None:
        artifact = json.loads(
            (ROOT / "results" / "verification.json").read_text(encoding="utf-8")
        )
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))

    def test_scope_remains_open(self) -> None:
        scope = V.build_payload()["scope"]
        self.assertTrue(scope["green_local_load_formula_verified"])
        self.assertTrue(scope["normalized_target_gram_conditioning_verified"])
        self.assertTrue(scope["phase_sensitive_pick_amplification_verified"])
        self.assertTrue(scope["compatible_selector_gram_upper_bound_sharp"])
        self.assertTrue(scope["collective_three_target_pick_obstruction_verified"])
        self.assertFalse(scope["pairwise_pick_conditions_are_sufficient"])
        self.assertFalse(scope["local_potential_loads_control_pick_interaction"])
        self.assertFalse(scope["xi_event_manifest_constructed"])
        self.assertFalse(scope["xi_conformal_coordinates_certified"])
        self.assertFalse(scope["xi_local_loads_estimated_cofinally"])
        self.assertFalse(scope["xi_target_gram_conditioning_estimated_cofinally"])
        self.assertFalse(scope["xi_pick_norm_estimated_cofinally"])
        self.assertFalse(scope["xi_unweighted_quotient_edges_estimated"])
        self.assertFalse(scope["strict_xi_jet_coherence_margin_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
