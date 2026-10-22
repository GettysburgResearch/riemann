#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t105104_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105104 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105104(unittest.TestCase):
    def test_primitive_identity_simple_cubic(self) -> None:
        primitive = V.primitive_zero_count(
            [F(1), F(-3), F(0), F(1)],
            F(-2),
            F(2),
            [F(-1), F(1)],
            [F(-1), F(1)],
        )
        self.assertEqual(primitive["node_values"], ["-1", "3", "-1", "3"])
        self.assertEqual(primitive["strict_sign_change_edges"], 3)
        self.assertEqual(primitive["common_support_count"], 0)
        self.assertEqual(primitive["distinct_real_zero_count"], 3)
        self.assertEqual(primitive["multiplicity_real_zero_count"], 3)

    def test_primitive_identity_with_common_multiplicity(self) -> None:
        primitive = V.primitive_zero_count(
            [F(0), F(0), F(-2), F(0), F(1)],
            F(-5, 4),
            F(5, 4),
            [F(-1), F(0), F(1)],
            [F(-1), F(0), F(1)],
        )
        self.assertEqual(primitive["common_support_count"], 1)
        self.assertEqual(primitive["common_parent_multiplicity"], 2)
        self.assertEqual(primitive["strict_sign_change_edges"], 0)
        self.assertEqual(primitive["distinct_real_zero_count"], 1)
        self.assertEqual(primitive["multiplicity_real_zero_count"], 2)

    def test_simple_residue_case_recovers_jet_coherence(self) -> None:
        fixture = V.canonical_fixtures()["simple_cubic_recovery"]
        jets = fixture["eligible_odd_noncommon_turns"]
        self.assertEqual([row["rho_jet"] for row in jets], ["-1/2", "-1/6"])
        self.assertEqual([row["ordinary_P_residue"] for row in jets], ["-1/2", "-1/6"])
        self.assertEqual(fixture["jet_first_carrier"], "2/3")
        self.assertEqual(fixture["jet_second_moment"], "5/18")
        self.assertEqual(fixture["jet_coherence"], "4/5")
        self.assertEqual(fixture["omitted_derivative_multiplicity_defect"], 0)

    def test_flat_turn_leading_principal_coefficients(self) -> None:
        fixtures = V.canonical_fixtures()
        good = fixtures["flat_good_quartic"]["eligible_odd_noncommon_turns"][0]
        wrong = fixtures["flat_wrong_quartic"]["eligible_odd_noncommon_turns"][0]
        self.assertEqual(good["critical_order"], 3)
        self.assertEqual(wrong["critical_order"], 3)
        self.assertEqual(good["rho_jet"], "-1/4")
        self.assertEqual(wrong["rho_jet"], "1/4")
        self.assertTrue(good["good_turn"])
        self.assertTrue(wrong["wrong_turn"])
        self.assertEqual(good["Q_leading_principal_coefficient"], "1/48")
        self.assertEqual(wrong["Q_leading_principal_coefficient"], "1/48")
        self.assertEqual(good["ordinary_P_residue"], "0")
        self.assertEqual(wrong["ordinary_P_residue"], "0")

    def test_common_only_fixture_is_exact_with_multiplicity(self) -> None:
        fixture = V.canonical_fixtures()["common_only_x4"]
        self.assertEqual(fixture["common_derivative_order_mass"], 3)
        self.assertEqual(fixture["eligible_turn_support_count"], 0)
        self.assertEqual(
            fixture["primitive_zero_count"]["multiplicity_real_zero_count"], 4
        )
        self.assertEqual(fixture["sharp_sign_lower_bound"], 4)
        self.assertEqual(fixture["componentwise_moment_lower_bound"], 4)

    def test_even_order_stationary_events_are_neutral(self) -> None:
        fixtures = V.canonical_fixtures()
        single = fixtures["neutral_even_stationary"]
        double = fixtures["two_even_stationary_firewall"]
        self.assertEqual(single["eligible_turn_support_count"], 0)
        self.assertEqual(single["omitted_derivative_multiplicity_defect"], 2)
        self.assertEqual(
            single["primitive_zero_count"]["multiplicity_real_zero_count"], 0
        )
        self.assertEqual(double["eligible_turn_support_count"], 0)
        self.assertEqual(len(double["neutral_even_noncommon_events"]), 2)
        self.assertEqual(double["omitted_derivative_multiplicity_defect"], 4)
        self.assertEqual(
            double["primitive_zero_count"]["multiplicity_real_zero_count"], 0
        )

    def test_active_component_count_is_load_bearing(self) -> None:
        fixture = V.canonical_fixtures()["common_and_two_good_turns"]
        self.assertEqual(fixture["common_derivative_order_mass"], 1)
        self.assertEqual(fixture["eligible_turn_support_count"], 2)
        self.assertEqual(fixture["good_turn_count"], 2)
        self.assertEqual(fixture["active_component_count"], 2)
        self.assertEqual(fixture["sharp_sign_lower_bound"], 2)
        exact = fixture["primitive_zero_count"]["multiplicity_real_zero_count"]
        self.assertEqual(exact, 2)
        mutated_q_one = 1 + 1 + 2 * 2 - 2 - 1
        self.assertEqual(mutated_q_one, 3)
        self.assertGreater(mutated_q_one, exact)

    def test_sextic_residue_no_go_pair(self) -> None:
        firewall = V.ordinary_residue_no_go_firewall()
        plus = firewall["plus"]
        minus = firewall["minus"]
        self.assertEqual(
            firewall["ordinary_global_residue_oracle"]["sum_finite_P_residues"],
            "0",
        )
        self.assertEqual(
            firewall["ordinary_global_residue_oracle"]["sum_finite_Q_residues"],
            "0",
        )
        self.assertEqual(
            plus["primitive_zero_count"]["multiplicity_real_zero_count"], 0
        )
        self.assertEqual(
            minus["primitive_zero_count"]["multiplicity_real_zero_count"], 2
        )
        self.assertEqual(
            plus["eligible_odd_noncommon_turns"][0]["rho_jet"], "1/384"
        )
        self.assertEqual(
            minus["eligible_odd_noncommon_turns"][0]["rho_jet"], "-1/384"
        )
        self.assertTrue(firewall["ordinary_residue_data_insufficient"])

    def test_bounded_component_combinatorics(self) -> None:
        check = V.component_combinatorics()
        self.assertEqual(check["maximum_turn_count"], 8)
        self.assertEqual(check["valid_nonadjacent_wrong_patterns_checked"], 141)
        self.assertEqual(check["minimum_internal_edge_slack"], 0)
        self.assertTrue(check["bounded_enumeration_only"])

    def test_derivative_multiplicity_split(self) -> None:
        for fixture in V.canonical_fixtures().values():
            left = fixture["derivative_real_zero_multiplicity"]
            right = (
                fixture["common_derivative_order_mass"]
                + fixture["eligible_turn_support_count"]
                + fixture["omitted_derivative_multiplicity_defect"]
            )
            self.assertEqual(left, right)
        flat = V.canonical_fixtures()["flat_good_quartic"]
        self.assertEqual(flat["derivative_real_zero_multiplicity"], 3)
        self.assertEqual(flat["eligible_turn_support_count"], 1)
        self.assertEqual(flat["omitted_derivative_multiplicity_defect"], 2)

    def test_componentwise_moment_bound(self) -> None:
        fixture = V.canonical_fixtures()["common_and_two_good_turns"]
        self.assertEqual(len(fixture["component_moment_rows"]), 2)
        for row in fixture["component_moment_rows"]:
            self.assertEqual(row["turn_count"], 1)
            self.assertEqual(row["raw_moment_lower_bound"], "0")
            self.assertEqual(row["nonnegative_integer_lower_bound"], 0)
        self.assertEqual(fixture["componentwise_moment_lower_bound"], 2)
        self.assertEqual(fixture["global_jet_moment_lower_bound"], "2")

    def test_manifest_and_endpoint_guards_fail_closed(self) -> None:
        coefficients = [F(1), F(-3), F(0), F(1)]
        with self.assertRaises(AssertionError):
            V.primitive_zero_count(
                coefficients,
                F(-2),
                F(2),
                [F(-1), F(-1)],
                [F(-1), F(1)],
            )
        with self.assertRaises(AssertionError):
            V.primitive_zero_count(
                coefficients, F(-2), F(2), [F(-1)], [F(-1), F(1)]
            )
        with self.assertRaises(AssertionError):
            V.primitive_zero_count(
                coefficients, F(-2), F(2), [], [F(-1), F(1)]
            )
        with self.assertRaises(AssertionError):
            V.primitive_zero_count(
                coefficients,
                F(-2),
                F(2),
                [F(-1), F(0), F(1)],
                [F(-1), F(1)],
            )
        with self.assertRaises(AssertionError):
            V.primitive_zero_count(
                coefficients,
                F(-2),
                F(2),
                [F(-1), F(1)],
                [F(-1), F(-1)],
            )
        with self.assertRaises(AssertionError):
            V.primitive_zero_count(
                coefficients,
                F(-2),
                F(2),
                [F(-1), F(0), F(1)],
                [F(-1), F(0), F(1)],
            )
        with self.assertRaises(AssertionError):
            V.primitive_zero_count(
                [F(-1), F(0), F(1)], F(-1), F(2), [F(0)], [F(0)]
            )
        with self.assertRaises(AssertionError):
            V.jet_event([F(2), F(0), F(0), F(1)], F(0))

    def test_frozen_dependency_is_authenticated(self) -> None:
        dependency = V.dependency_checkpoint()
        self.assertEqual(dependency["commit"], V.BASE_COMMIT)
        self.assertEqual(dependency["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(dependency["artifact_matches_live_producer"])

    def test_committed_artifact_matches_producer_and_content(self) -> None:
        artifact = json.loads(
            (ROOT / "results" / "verification.json").read_text(encoding="utf-8")
        )
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))

    def test_scope_remains_open(self) -> None:
        scope = V.build_payload()["scope"]
        self.assertTrue(scope["arbitrary_multiplicity_real_interval_identity_proved"])
        self.assertTrue(scope["odd_turn_jet_sign_dictionary_proved"])
        self.assertTrue(scope["jet_coherence_transfer_bound_proved"])
        self.assertTrue(scope["common_critical_multiplicity_accounted"])
        self.assertTrue(scope["ordinary_residue_only_extension_refuted"])
        self.assertFalse(scope["jet_data_reconstructed_from_global_boundary_flux"])
        self.assertFalse(scope["xi_effective_turning_proportion_proved"])
        self.assertFalse(scope["xi_multiplicity_defect_controlled"])
        self.assertFalse(scope["xi_jet_moments_estimated"])
        self.assertFalse(scope["strict_xi_jet_coherence_margin_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
