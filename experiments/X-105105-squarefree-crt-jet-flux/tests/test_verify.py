#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t105105_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105105 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105105(unittest.TestCase):
    def test_frozen_dependency_is_authenticated(self) -> None:
        dependency = V.dependency_checkpoint()
        self.assertEqual(dependency["commit"], V.BASE_COMMIT)
        self.assertEqual(dependency["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(dependency["artifact_matches_live_producer"])

    def test_simple_cubic_selectors_kill_adjacent_debt(self) -> None:
        row = V.selector_fixtures()["simple_cubic_with_adjacent_debt_killed"]
        self.assertEqual(row["first_selector"], ["1"])
        self.assertEqual(row["second_selector"], ["0", "0", "1"])
        self.assertEqual(row["weighted_first_residues"], ["-1/2", "0", "-1/6"])
        self.assertEqual(row["weighted_second_residues"], ["1/4", "0", "1/36"])
        self.assertEqual(row["jet_first_sum"], "-2/3")
        self.assertEqual(row["jet_second_moment"], "5/18")

    def test_flat_target_uses_full_multiplicity_selector(self) -> None:
        row = V.selector_fixtures()["flat_quartic"]
        self.assertEqual(row["first_selector"], ["0", "0", "1"])
        self.assertEqual(row["second_selector"], ["0", "0", "0", "0", "3"])
        self.assertEqual(row["weighted_first_residues"], ["-1/4"])
        self.assertEqual(row["weighted_second_residues"], ["1/16"])

    def test_mixed_simple_and_flat_targets_share_one_charge(self) -> None:
        row = V.selector_fixtures()["mixed_simple_flat"]
        self.assertEqual(row["weighted_first_residues"], ["-1/10", "0", "1/20"])
        self.assertEqual(row["weighted_second_residues"], ["1/100", "0", "1/400"])
        self.assertEqual(row["jet_first_sum"], "-1/20")
        self.assertEqual(row["jet_second_moment"], "1/80")
        self.assertEqual(max(len(row["first_selector"]), len(row["second_selector"])), 7)

    def test_common_event_is_removable_not_a_selector_target(self) -> None:
        row = V.selector_fixtures()["common_only"]
        self.assertEqual(row["events"][0]["orders"], {"m": 4, "r": 3, "s": 2})
        self.assertEqual(row["events"][0]["P_actual_pole_order"], 0)
        self.assertEqual(row["events"][0]["Q_actual_pole_order"], 0)
        self.assertEqual(row["first_selector"], ["0"])
        self.assertEqual(row["second_selector"], ["0"])

    def test_even_stationary_actual_poles_are_annihilated(self) -> None:
        row = V.selector_fixtures()["even_stationary_only"]
        self.assertEqual(row["events"][0]["orders"], {"m": 0, "r": 2, "s": 1})
        self.assertEqual(row["events"][0]["P_actual_pole_order"], 2)
        self.assertEqual(row["events"][0]["Q_actual_pole_order"], 3)
        self.assertEqual(row["first_selector"], ["0"])
        self.assertEqual(row["second_selector"], ["0"])
        self.assertEqual(row["weighted_second_residues"], ["0"])

    def test_nonreal_and_adjacent_support_can_be_killed_exactly(self) -> None:
        fixtures = V.selector_fixtures()
        row = fixtures["nonreal_and_adjacent_support_annihilated"]
        self.assertEqual(row["eligible_target_manifest"], [])
        self.assertEqual(row["weighted_first_residues"], ["0", "0", "0"])
        self.assertEqual(row["weighted_second_residues"], ["0", "0", "0"])
        self.assertTrue(row["all_nontarget_actual_poles_annihilated"])
        parity = fixtures["parity_symmetric_partial_cancellation"]
        self.assertEqual(parity["first_selector"], ["1/2", "0", "1/2"])
        self.assertEqual(
            parity["second_selector"], ["0", "0", "1/2", "0", "1/2"]
        )
        self.assertEqual(parity["jet_first_sum"], "-2/5")
        self.assertEqual(parity["jet_second_moment"], "2/25")
        zero_event = [event for event in parity["events"] if event["point"] == "0"][0]
        self.assertEqual(zero_event["orders"], {"m": 1, "r": 0, "s": 3})
        self.assertEqual(zero_event["P_actual_pole_order"], 0)
        self.assertEqual(zero_event["Q_actual_pole_order"], 1)

    def test_squarefree_simple_carriers_recover_jet_moments(self) -> None:
        row = V.squarefree_corollary_fixtures()["simple_cubic"]
        self.assertEqual(row["first_crt_carrier"], ["-1/3", "1/6"])
        self.assertEqual(row["second_crt_carrier"], ["5/36", "-1/9"])
        self.assertEqual(row["real_jet_first_carrier"], "2/3")
        self.assertEqual(row["real_jet_second_moment"], "5/18")

    def test_squarefree_mixed_and_common_strata(self) -> None:
        rows = V.squarefree_corollary_fixtures()
        mixed = rows["mixed_simple_flat"]
        common = rows["common_and_two_turns"]
        nonlinear = rows["nonlinear_flat_stratum"]
        self.assertEqual(mixed["first_crt_carrier"], ["-5/32", "1/160"])
        self.assertEqual(mixed["real_jet_second_moment"], "313/6400")
        self.assertEqual(common["first_crt_carrier"], ["0", "0", "-1/8"])
        common_event = [event for event in common["events"] if event["point"] == "0"][0]
        self.assertTrue(common_event["common_parent_zero"])
        self.assertIsNone(common_event["rho_jet"])
        self.assertEqual(common_event["algebraic_leading_carrier"], "0")
        self.assertEqual(nonlinear["first_crt_carrier"], ["-2/35"])
        self.assertEqual(nonlinear["second_crt_carrier"], ["4/1225"])
        self.assertEqual(
            [event["rho_jet"] for event in nonlinear["events"]],
            ["-2/35", "-2/35"],
        )

    def test_squarefree_nonreal_trace_is_algebraic_not_positive(self) -> None:
        row = V.squarefree_corollary_fixtures()["nonreal_pair"]
        self.assertEqual(row["global_first_residue_trace"], "2/3")
        self.assertEqual(row["global_second_residue_trace"], "-5/18")
        self.assertEqual(row["nonreal_first_correction"], "2/3")
        self.assertEqual(row["nonreal_second_algebraic_square_correction"], "-5/18")
        self.assertEqual(row["real_jet_first_carrier"], "0")
        self.assertEqual(row["real_jet_second_moment"], "0")

    def test_squarefree_factor_manifest_mutations_fail_closed(self) -> None:
        firewall = V.mutation_firewalls()
        self.assertTrue(firewall["omitted_factor_rejected"])
        self.assertTrue(firewall["wrong_multiplicity_label_rejected"])
        self.assertTrue(firewall["nonmonic_factor_rejected"])
        self.assertTrue(firewall["nonsquarefree_factor_rejected"])
        self.assertTrue(firewall["overlapping_strata_rejected"])
        self.assertTrue(firewall["nonlinear_derivative_power_mutation_rejected"])

    def test_selector_and_target_manifests_fail_closed(self) -> None:
        firewall = V.mutation_firewalls()
        self.assertTrue(firewall["selector_manifest_missing_rejected"])
        self.assertTrue(firewall["selector_manifest_duplicate_rejected"])
        self.assertTrue(firewall["selector_manifest_extraneous_rejected"])
        self.assertTrue(firewall["selector_target_omission_rejected"])
        self.assertTrue(firewall["both_target_manifests_incomplete_rejected"])

    def test_unweighted_adjacent_charge_is_not_selected_moment(self) -> None:
        firewall = V.mutation_firewalls()
        row = firewall["simple_cubic_adjacent_debt"]
        self.assertEqual(row["naive_Q_residues"], ["1/4", "-1/18", "1/36"])
        self.assertEqual(row["naive_Q_charge"], "2/9")
        self.assertEqual(row["target_jet_second_moment"], "5/18")
        self.assertTrue(row["F_double_prime_only_pole_annihilated"])
        partial = firewall["partial_common_cancellation"]
        self.assertEqual(partial["unweighted_Q_residue"], "-1/4")
        self.assertEqual(partial["selected_Q_residue"], "0")

    def test_second_selector_factor_and_flux_square_are_load_bearing(self) -> None:
        row = V.mutation_firewalls()["flat_quartic"]
        self.assertEqual(row["rho_jet"], "-1/4")
        self.assertEqual(row["desired_jet_square"], "1/16")
        self.assertEqual(row["residue_of_squared_first_flux"], "0")
        self.assertEqual(row["residue_without_load_bearing_r_factor"], "1/48")
        self.assertEqual(row["ordinary_Q_residue"], "-1/24")
        self.assertEqual(row["scaled_true_rho_jet"], "-1/4")
        self.assertTrue(row["radical_support_without_local_unit_is_not_scale_invariant"])

    def test_committed_artifact_matches_producer_and_content(self) -> None:
        artifact = json.loads(
            (ROOT / "results" / "verification.json").read_text(encoding="utf-8")
        )
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))

    def test_scope_remains_open(self) -> None:
        scope = V.build_payload()["scope"]
        self.assertTrue(scope["fixed_window_holomorphic_crt_selector_identity_proved"])
        self.assertTrue(scope["all_nontarget_actual_poles_annihilated"])
        self.assertTrue(scope["finite_polynomial_squarefree_crt_bridge_proved"])
        self.assertTrue(scope["xi_fixed_window_selector_exists_given_exact_event_manifest"])
        self.assertFalse(scope["xi_event_manifest_constructed"])
        self.assertFalse(scope["xi_selector_boundary_norm_estimated"])
        self.assertFalse(scope["xi_cofinal_window_limit_proved"])
        self.assertFalse(scope["xi_jet_moments_estimated"])
        self.assertFalse(scope["strict_xi_jet_coherence_margin_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
