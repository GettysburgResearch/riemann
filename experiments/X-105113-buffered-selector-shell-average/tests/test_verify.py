#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t105113_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105113 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105113(unittest.TestCase):
    def test_frozen_dependency_is_authenticated_at_exact_commit(self) -> None:
        row = V.dependency_checkpoint()
        self.assertEqual(row["path"], "experiments/X-105112-selector-domain-repair")
        self.assertEqual(row["commit"], V.BASE_COMMIT)
        self.assertEqual(row["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(row["artifact_matches_live_producer"])

    def test_coordinate_orientation_identity_matches_edge_average(self) -> None:
        row = V.orientation_fixture()
        self.assertEqual(row["vertical_sign"], "+i*sgn(x)")
        self.assertEqual(row["horizontal_sign"], "-sgn(y)")
        self.assertEqual(row["vertical_area_component"], row["vertical_oriented_edge_average"])
        self.assertEqual(row["horizontal_area_component"], row["horizontal_oriented_edge_average"])
        self.assertTrue(row["coordinate_and_orientation_identity_exact"])

    def test_oriented_polynomial_total_has_zero_contour_charge(self) -> None:
        row = V.orientation_fixture()
        self.assertNotEqual(row["vertical_area_component"], {"real": "0", "imaginary": "0"})
        self.assertEqual(row["total_contour_charge"], {"real": "0", "imaginary": "0"})
        vertical = row["vertical_area_component"]
        horizontal = row["horizontal_area_component"]
        self.assertEqual(vertical["real"], str(-V.F(horizontal["real"])))
        self.assertEqual(vertical["imaginary"], str(-V.F(horizontal["imaginary"])))

    def test_tonelli_vertical_and_horizontal_means_are_exact(self) -> None:
        row = V.tonelli_fixture()
        self.assertEqual(row["vertical_weighted_area"], row["vertical_parameter_edge_integral"])
        self.assertEqual(row["horizontal_weighted_area"], row["horizontal_parameter_edge_integral"])
        self.assertTrue(row["tonelli_mean_exact"])

    def test_inverse_widths_are_paired_with_correct_coordinates(self) -> None:
        row = V.tonelli_fixture()
        self.assertEqual(row["vertical_inverse_width"], "1/Delta_T")
        self.assertEqual(row["horizontal_inverse_width"], "1/Delta_eta")
        self.assertTrue(row["coordinate_width_pairing_exact"])

    def test_measurable_width_constants_are_sharp(self) -> None:
        row = V.sharp_width_fixture()
        self.assertEqual(row["vertical_indicator_boundary_cost"], row["vertical_indicator_area_over_Delta_T"])
        self.assertEqual(row["horizontal_indicator_boundary_cost"], row["horizontal_indicator_area_over_Delta_eta"])
        self.assertTrue(row["both_width_constants_attained"])

    def test_prescribed_weight_uses_one_aggregate_cost(self) -> None:
        row = V.prescribed_weight_fixture()
        self.assertTrue(row["one_aggregate_cost_used_per_prescribed_pair"])
        self.assertEqual(row["prescribed_weight_rows"][0]["selected_rectangle"], "A")
        self.assertEqual(row["prescribed_weight_rows"][1]["selected_rectangle"], "B")
        self.assertTrue(row["selected_rectangle_can_depend_on_weights"])

    def test_prescribed_weight_quantifier_is_not_universal(self) -> None:
        row = V.prescribed_weight_fixture()
        self.assertEqual(row["component_means"], ["1", "1"])
        self.assertFalse(row["universal_componentwise_rectangle_exists"])

    def test_cubic_derivatives_are_exact(self) -> None:
        row = V.cubic_fixture()
        self.assertEqual(row["F_coefficients"], ["1", "0", "-1", "1/3"])
        self.assertEqual(row["F_prime_coefficients"], ["0", "-2", "1"])
        self.assertEqual(row["F_second_coefficients"], ["-2", "2"])
        self.assertEqual(row["F_third_coefficients"], ["2"])

    def test_cubic_residues_are_exact(self) -> None:
        row = V.cubic_fixture()["residues"]
        self.assertEqual(row, {"P_at_0": "-1/2", "P_at_2": "-1/6", "Q_at_0": "1/4", "Q_at_1": "-1/18", "Q_at_2": "1/36"})

    def test_core_only_charges_jump_at_buffer_events(self) -> None:
        row = V.cubic_fixture()
        self.assertEqual(row["core_only_normalized_P_charges_for_T_regions"], ["-1/2", "-1/2", "-2/3"])
        self.assertEqual(row["core_only_normalized_Q_charges_for_T_regions"], ["1/4", "7/36", "2/9"])

    def test_outer_actual_manifests_include_all_buffer_events(self) -> None:
        row = V.cubic_fixture()["outer_actual_manifests"]
        self.assertEqual([entry["point"] for entry in row["P"]], ["0", "2"])
        self.assertEqual([entry["point"] for entry in row["Q"]], ["0", "1", "2"])
        self.assertEqual(row["P"][0]["role"], "target")
        self.assertTrue(all(entry["order"] == 1 for entries in row.values() for entry in entries))

    def test_buffer_selectors_satisfy_target_and_zero_congruences(self) -> None:
        row = V.cubic_fixture()
        self.assertEqual(row["W_1_coefficients"], ["1", "-1/2"])
        self.assertEqual(row["W_2_coefficients"], ["1", "-3/2", "1/2"])
        self.assertEqual(row["selector_values"], {"W1_at_0": "1", "W1_at_2": "0", "W2_at_0": "1", "W2_at_1": "0", "W2_at_2": "0"})

    def test_canceled_carriers_and_fixed_charges_are_exact(self) -> None:
        row = V.cubic_fixture()
        self.assertEqual(row["canceled_first_carrier"], "-F/(2*z)")
        self.assertEqual(row["canceled_second_carrier"], "F^2/(4*z)")
        self.assertEqual(row["buffered_normalized_charges"], ["-1/2", "1/4"])
        self.assertTrue(row["complete_outer_manifest_restores_invariance"])

    def test_manifest_contract_preserves_actual_outer_scope(self) -> None:
        row = V.manifest_ledger()
        self.assertEqual(row["manifest_type"], "complete actual-pole manifest on outer rectangle")
        self.assertEqual(row["all_other_outer_events"], "zero congruence to full actual order")
        self.assertTrue(row["outer_boundary_raw_regular"])
        self.assertTrue(row["abstract_finiteness_is_not_Xi_authentication"])

    def test_no_forbidden_control_characters_in_load_bearing_files(self) -> None:
        self.assertEqual(V.forbidden_control_characters(), [])

    def test_mutation_firewalls_remain_closed(self) -> None:
        row = V.mutation_firewalls()
        self.assertEqual(len(row), 15)
        self.assertTrue(all(value is False for value in row.values()))
        self.assertFalse(row["one_rectangle_works_for_every_weight_pair"])
        self.assertFalse(row["shell_budget_discards_selector_cost"])
        self.assertFalse(row["rh_established"])

    def test_artifact_hash_manifest_canonical_digest_and_open_scope(self) -> None:
        artifact = json.loads((ROOT / "results" / "verification.json").read_text(encoding="utf-8"))
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))
        self.assertEqual(len(artifact["content_sha256"]), 7)
        claimed = artifact.pop("proof_object_sha256")
        canonical = json.dumps(artifact, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(claimed, hashlib.sha256(canonical).hexdigest())
        scope = artifact["scope"]
        self.assertTrue(scope["signed_two_parameter_shell_identity_verified"])
        self.assertTrue(scope["simultaneous_prescribed_weight_selection_verified"])
        self.assertTrue(scope["core_only_transport_refuted"])
        self.assertFalse(scope["complete_cofinal_xi_manifests_authenticated"])
        self.assertFalse(scope["positive_signed_xi_first_moment_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
