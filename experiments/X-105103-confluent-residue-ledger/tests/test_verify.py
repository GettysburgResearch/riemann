#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t105103_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105103 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105103(unittest.TestCase):
    def test_confluent_quartic_principal_parts(self) -> None:
        event = V.local_event([F(1), F(0), F(0), F(1), F(1)], F(0))
        self.assertEqual(event["orders"], {"m": 0, "r": 2, "s": 1})
        self.assertEqual(event["P_pole_order"], 2)
        self.assertEqual(event["Q_pole_order"], 3)
        self.assertEqual(event["P_residue"], "-4/9")
        self.assertEqual(event["Q_residue"], "38/81")
        self.assertEqual(
            event["P_principal_part"],
            [
                {"power": -2, "coefficient": "1/3"},
                {"power": -1, "coefficient": "-4/9"},
            ],
        )
        self.assertEqual(
            event["Q_principal_part"],
            [
                {"power": -3, "coefficient": "1/18"},
                {"power": -2, "coefficient": "-5/27"},
                {"power": -1, "coefficient": "38/81"},
            ],
        )
        self.assertEqual(event["merged_support_kind"], "G_MERGED_EXCEPTIONAL")

    def test_simple_stratum_and_adjacent_debt_controls(self) -> None:
        coefficients = [F(1), F(0), F(0), F(1), F(1)]
        simple = V.local_event(coefficients, F(-3, 4))
        adjacent = V.local_event(coefficients, F(-1, 2))
        self.assertEqual(simple["merged_support_kind"], "S1_SIMPLE_NONCOMMON_FPRIME")
        self.assertEqual(simple["P_residue"], "229/576")
        self.assertEqual(simple["Q_residue"], "52441/331776")
        self.assertEqual(F(simple["Q_residue"]), F(simple["P_residue"]) ** 2)
        self.assertEqual(
            adjacent["merged_support_kind"], "S2_ISOLATED_SIMPLE_FSECOND"
        )
        self.assertEqual(adjacent["P_residue"], "0")
        self.assertEqual(adjacent["Q_residue"], "-75/128")

    def test_common_parent_events_remain_in_manifest(self) -> None:
        simple_common = V.local_event([F(0), F(0), F(1)], F(0))
        multiple_common = V.local_event([F(0), F(0), F(0), F(1)], F(0))
        self.assertEqual(simple_common["orders"], {"m": 2, "r": 1, "s": 0})
        self.assertEqual(multiple_common["orders"], {"m": 3, "r": 2, "s": 1})
        for event in (simple_common, multiple_common):
            self.assertEqual(event["merged_support_kind"], "G_MERGED_EXCEPTIONAL")
            self.assertEqual(event["P_residue"], "0")
            self.assertEqual(event["Q_residue"], "0")

    def test_pole_order_and_residue_are_independent(self) -> None:
        zero_residue = V.local_event([F(1), F(0), F(0), F(1)], F(0))
        triple = V.local_event(
            [F(5), F(-5), F(0), F(0), F(0), F(1)], F(0)
        )
        simple = V.local_event(
            [F(0), F(-5), F(0), F(0), F(0), F(1)], F(0)
        )
        self.assertEqual(zero_residue["Q_pole_order"], 3)
        self.assertEqual(zero_residue["Q_residue"], "0")
        self.assertEqual(triple["Q_pole_order"], 3)
        self.assertEqual(simple["Q_pole_order"], 1)
        self.assertEqual(triple["Q_residue"], "-1/4")
        self.assertEqual(simple["Q_residue"], "-1/4")

    def test_confluent_second_residue_has_both_signs(self) -> None:
        negative = V.local_event(
            [F(1), F(0), F(0), F(1), F(0), F(1)], F(0)
        )
        positive = V.local_event(
            [F(0), F(1), F(0), F(0), F(0), F(1, 5)], F(0)
        )
        self.assertEqual(negative["Q_residue"], "-5/18")
        self.assertEqual(positive["Q_residue"], "1/4")

    def test_full_merged_support_reconstruction(self) -> None:
        ledger = V.merged_support_quartic()
        self.assertEqual(ledger["unique_denominator_event_count"], 3)
        self.assertEqual(ledger["simple_real_critical_count"], 1)
        self.assertEqual(ledger["Phi1"], "-3/64")
        self.assertEqual(ledger["B2"], "169/4096")
        self.assertEqual(ledger["Lambda1_merged"], "-4/9")
        self.assertEqual(ledger["Lambda2_merged"], "38/81")
        self.assertEqual(ledger["simple_stratum_M1"], "-229/576")
        self.assertEqual(ledger["simple_stratum_M2"], "52441/331776")
        self.assertEqual(ledger["reconstructed_M1"], ledger["simple_stratum_M1"])
        self.assertEqual(ledger["reconstructed_M2"], ledger["simple_stratum_M2"])
        self.assertEqual(ledger["naive_dropped_Lambda1_carrier"], "3/64")
        self.assertEqual(ledger["naive_dropped_Lambda2_M2"], "2569/4096")
        self.assertFalse(ledger["transfer_certified"])

    def test_narrow_window_is_exactly_corrected(self) -> None:
        ledger = V.narrow_window_quartic()
        self.assertEqual(ledger["Phi1"], "-4/9")
        self.assertEqual(ledger["B2"], "38/81")
        self.assertEqual(ledger["Lambda1_merged"], "-4/9")
        self.assertEqual(ledger["Lambda2_merged"], "38/81")
        self.assertEqual(ledger["simple_real_critical_count"], 0)
        self.assertEqual(ledger["simple_stratum_M1"], "0")
        self.assertEqual(ledger["simple_stratum_M2"], "0")

    def test_manifest_fails_closed_on_union_mutations(self) -> None:
        coefficients = [F(1), F(0), F(0), F(1), F(1)]
        expected = [F(0), F(-3, 4), F(-1, 2)]
        self.assertEqual(
            len(V.validated_manifest(coefficients, expected, expected)), 3
        )
        with self.assertRaises(AssertionError):
            V.validated_manifest(
                coefficients, [F(0), F(0), F(-1, 2)], expected
            )
        with self.assertRaises(AssertionError):
            V.validated_manifest(coefficients, expected[:-1], expected)
        with self.assertRaises(AssertionError):
            V.validated_manifest(
                coefficients, [F(0), F(-3, 4), F(2)], expected
            )

    def test_infinity_oracles(self) -> None:
        fixtures = [
            ([F(1), F(0), F(0), F(1), F(1)], "-3/64", "169/4096"),
            ([F(0), F(0), F(0), F(1)], "0", "0"),
            ([F(5), F(-5), F(0), F(0), F(0), F(1)], "0", "-9/100"),
            ([F(0), F(-5), F(0), F(0), F(0), F(1)], "0", "-9/100"),
        ]
        for coefficients, first_expected, second_expected in fixtures:
            with self.subTest(coefficients=coefficients):
                oracle = V.infinity_residue_oracle(coefficients)
                self.assertEqual(oracle["sum_finite_P_residues"], first_expected)
                self.assertEqual(oracle["sum_finite_Q_residues"], second_expected)

    def test_shift_and_scale_invariance(self) -> None:
        check = V.shift_scale_invariance()
        self.assertTrue(check["residues_and_global_sums_invariant"])
        self.assertEqual(
            check["base_event"]["P_principal_part"],
            check["shifted_event"]["P_principal_part"],
        )
        self.assertEqual(
            check["base_event"]["Q_principal_part"],
            check["shifted_event"]["Q_principal_part"],
        )
        self.assertEqual(check["base_oracle"], check["shifted_oracle"])

    def test_nonreal_algebraic_squares_are_not_moduli(self) -> None:
        firewall = V.multiple_fsecond_sign_firewall()
        row = firewall["fixtures"]["nonzero_parent"]
        split = row["simple_square_split"]
        self.assertEqual(split["real_simple_square_sum"], "41/200")
        self.assertEqual(split["nonreal_simple_square_sum"], "-9/200")
        self.assertNotEqual(split["nonreal_simple_square_sum"], "41/200")
        self.assertEqual(row["boundary_Q_charge"], "-9/100")
        self.assertEqual(row["multiple_Fsecond_event"]["Q_residue"], "-1/4")

    def test_root_ledgers_independently_match_infinity(self) -> None:
        check = V.root_ledger_crosscheck()
        self.assertTrue(check["independent_infinity_and_root_ledgers_agree"])
        for row in check["fixtures"].values():
            self.assertEqual(
                row["infinity_oracle"]["sum_finite_P_residues"],
                row["V2_first_ledger"],
            )
            self.assertEqual(
                row["infinity_oracle"]["sum_finite_Q_residues"],
                row["V2_V4_second_ledger"],
            )

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
        self.assertTrue(scope["local_confluent_P_residue_recurrence_proved"])
        self.assertTrue(scope["local_confluent_Q_residue_recurrence_proved"])
        self.assertTrue(scope["merged_support_fixed_window_identity_proved"])
        self.assertFalse(scope["interior_simplicity_required_for_contour_identity"])
        self.assertTrue(scope["simple_stratum_count_separated_from_event_count"])
        self.assertFalse(scope["confluent_corrections_estimated"])
        self.assertFalse(scope["multiple_Fprime_reverse_rolle_transfer_proved"])
        self.assertFalse(scope["xi_multiplicity_manifest_proved"])
        self.assertFalse(scope["admissible_height_strip_sequence_controlled"])
        self.assertFalse(scope["strict_coherence_margin_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
