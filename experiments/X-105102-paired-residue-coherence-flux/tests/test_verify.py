#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t105102_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105102 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105102(unittest.TestCase):
    def test_real_cubic_paired_windows(self) -> None:
        coefficients = [F(1), F(-3), F(0), F(1)]
        narrow = V.paired_local_ledger(
            "narrow",
            coefficients,
            [V.G(F(-1)), V.G(F(1))],
            [V.ZERO],
            F(1, 2),
            F(1),
        )
        self.assertEqual(narrow["first"]["boundary_first_charge"], "0")
        self.assertEqual(narrow["first"]["first_moment"], "0")
        self.assertIsNone(narrow["coherence"])

        full = V.paired_local_ledger(
            "full",
            coefficients,
            [V.G(F(-1)), V.G(F(1))],
            [V.ZERO],
            F(3, 2),
            F(1),
        )
        self.assertEqual(full["first"]["boundary_first_charge"], "-2/3")
        self.assertEqual(full["first"]["first_moment"], "2/3")
        self.assertEqual(full["second"]["real_m2"], "5/18")
        self.assertEqual(full["coherence"], "4/5")
        self.assertEqual(full["boundary_reconstructed_coherence"], "4/5")
        self.assertTrue(full["displayed_quotient_verified"])
        self.assertEqual(full["formal_coherence_excess"], "3/5")
        self.assertEqual(full["certified_transfer_constant"], "3/5")
        self.assertTrue(full["l104522_transfer_hypotheses_verified"])

    def test_asymmetric_partial_window_has_unit_coherence(self) -> None:
        fixture = V.paired_local_ledger(
            "asymmetric",
            [F(1), F(64), F(-32), F(-4, 3), F(1)],
            [V.G(F(-4)), V.G(F(1)), V.G(F(4))],
            [V.G(F(-2)), V.G(F(8, 3))],
            F(3),
            F(1),
        )
        self.assertEqual(fixture["first"]["inside_critical_roots"], ["1"])
        self.assertEqual(fixture["first"]["boundary_first_charge"], "-49/90")
        self.assertEqual(fixture["first"]["first_moment"], "49/90")
        self.assertEqual(fixture["coherence"], "1")
        self.assertEqual(fixture["formal_coherence_excess"], "1")
        self.assertEqual(fixture["certified_transfer_constant"], "1")

    def test_nonreal_first_correction_cancels_boundary_charge(self) -> None:
        coefficients = [F(1), F(3), F(0), F(1)]
        roots = [V.G(F(0), F(-1)), V.G(F(0), F(1))]
        narrow = V.paired_local_ledger(
            "complex-narrow",
            coefficients,
            roots,
            [V.ZERO],
            F(1),
            F(1, 2),
        )
        self.assertEqual(narrow["first"]["nonreal_first_correction"], "0")
        self.assertEqual(narrow["second"]["nonreal_correction"], "0")

        fixture = V.paired_local_ledger(
            "complex",
            coefficients,
            roots,
            [V.ZERO],
            F(1),
            F(2),
        )
        self.assertEqual(fixture["first"]["boundary_first_charge"], "2/3")
        self.assertEqual(fixture["first"]["nonreal_first_correction"], "2/3")
        self.assertEqual(fixture["first"]["first_moment"], "0")
        self.assertIsNone(fixture["coherence"])

    def test_positive_part_rejects_negative_first_carrier(self) -> None:
        fixture = V.paired_local_ledger(
            "negative-carrier",
            [F(1), F(0), F(1)],
            [V.ZERO],
            [],
            F(1),
            F(1),
        )
        self.assertEqual(fixture["first"]["boundary_first_charge"], "1/2")
        self.assertEqual(fixture["first"]["first_moment"], "-1/2")
        self.assertEqual(fixture["second"]["real_m2"], "1/4")
        self.assertEqual(fixture["coherence"], "0")
        self.assertIsNone(fixture["formal_coherence_excess"])
        self.assertIsNone(fixture["certified_transfer_constant"])

    def test_transfer_flags_withhold_formal_excess(self) -> None:
        endpoint = V.paired_local_ledger(
            "endpoint",
            [F(-1), F(0), F(1)],
            [V.ZERO],
            [],
            F(1),
            F(1),
        )
        self.assertEqual(endpoint["coherence"], "1")
        self.assertEqual(endpoint["formal_coherence_excess"], "1")
        self.assertFalse(endpoint["l104522_endpoint_nonvanishing"])
        self.assertTrue(endpoint["l104522_common_zero_free"])
        self.assertIsNone(endpoint["certified_transfer_constant"])

        common = V.paired_local_ledger(
            "common",
            [F(-95, 3), F(64), F(-32), F(-4, 3), F(1)],
            [V.G(F(-4)), V.G(F(1)), V.G(F(4))],
            [V.G(F(-2)), V.G(F(8, 3))],
            F(5),
            F(1),
        )
        self.assertEqual(common["first"]["first_moment"], "49/12")
        self.assertEqual(common["second"]["real_m2"], "44657/4608")
        self.assertEqual(common["coherence"], "76832/133971")
        self.assertEqual(common["formal_coherence_excess"], "19693/133971")
        self.assertTrue(common["l104522_endpoint_nonvanishing"])
        self.assertFalse(common["l104522_common_zero_free"])
        self.assertIsNone(common["certified_transfer_constant"])

    def test_first_root_manifest_and_boundary_fail_closed(self) -> None:
        coefficients = [F(1), F(3), F(0), F(1)]
        with self.assertRaises(ValueError):
            V.first_residue_ladder(coefficients, [V.BASE.I])
        with self.assertRaises(ValueError):
            V.first_residue_ladder(coefficients, [V.BASE.I, V.BASE.I])
        with self.assertRaises(AssertionError):
            V.first_residue_ladder(coefficients, [V.BASE.I, V.ZERO])
        with self.assertRaises(ValueError):
            V.first_local_ledger(
                "horizontal-boundary",
                coefficients,
                [V.G(F(0), F(-1)), V.G(F(0), F(1))],
                F(1),
                F(1),
            )

    def test_common_numerator_zero_is_removable_for_first_flux(self) -> None:
        fixture = V.paired_local_ledger(
            "common-removable",
            [F(1), F(-2), F(1)],
            [V.G(F(1))],
            [],
            F(2),
            F(1),
        )
        self.assertEqual(fixture["first"]["inside_critical_roots"], ["1"])
        self.assertEqual(fixture["first"]["boundary_first_charge"], "0")
        self.assertEqual(fixture["first"]["first_moment"], "0")
        self.assertEqual(fixture["second"]["boundary_residue_sum"], "0")
        self.assertIsNone(fixture["coherence"])
        self.assertFalse(fixture["l104522_common_zero_free"])
        self.assertFalse(fixture["l104522_transfer_hypotheses_verified"])

    def test_integrated_paired_edge_oracle(self) -> None:
        check = V.integrated_paired_edge_check()
        self.assertEqual(check["first_combined_a_over_pi_plus_b"], ["0", "1/2"])
        self.assertEqual(check["first_residue"], "1/2")
        self.assertEqual(check["second_residue"], "1/4")
        self.assertTrue(check["both_first_sign_mutations_rejected"])
        parity = V.first_schwarz_parity_checks()
        self.assertTrue(parity["even"]["P_is_odd"])
        self.assertTrue(parity["odd"]["P_is_odd"])
        self.assertFalse(parity["generic_real"]["P_is_odd"])

    def test_nonreal_carrier_firewall(self) -> None:
        firewall = V.nonreal_carrier_firewall()
        self.assertEqual(firewall["real_critical_count"], 0)
        self.assertEqual(firewall["critical_y_discriminant"], "-11")
        self.assertEqual(firewall["common_root_candidate_residual"], "3")
        self.assertTrue(firewall["critical_roots_simple_and_not_parent_roots"])
        self.assertTrue(firewall["firewall_constants_derived_from_coefficients"])
        self.assertEqual(firewall["global_first_charge"], "-2/25")
        self.assertEqual(firewall["nonreal_first_correction"], "-2/25")
        self.assertEqual(firewall["corrected_first_moment"], "0")
        self.assertEqual(firewall["dropped_correction_false_carrier"], "2/25")

    def test_coherence_threshold_firewall(self) -> None:
        firewall = V.coherence_threshold_firewall()
        self.assertEqual(firewall["first_moment"], "1/4")
        self.assertEqual(firewall["second_moment"], "9/32")
        self.assertEqual(firewall["coherence"], "2/27")
        self.assertFalse(firewall["positive_transfer_available"])

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
        self.assertTrue(scope["pointwise_thin_strip_corrections_eliminated"])
        self.assertFalse(scope["multiple_zero_confluent_ledger_proved"])
        self.assertFalse(scope["xi_window_hypotheses_proved"])
        self.assertFalse(scope["admissible_height_strip_sequence_controlled"])
        self.assertFalse(scope["first_boundary_charge_estimated"])
        self.assertFalse(scope["nonreal_first_correction_estimated"])
        self.assertFalse(scope["second_boundary_and_corrections_estimated"])
        self.assertFalse(scope["strict_coherence_margin_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
