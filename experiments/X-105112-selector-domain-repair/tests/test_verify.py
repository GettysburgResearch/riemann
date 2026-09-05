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
SPEC = importlib.util.spec_from_file_location("t105112_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105112 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105112(unittest.TestCase):
    def test_frozen_dependency_is_authenticated_at_exact_commit(self) -> None:
        row = V.dependency_checkpoint()
        self.assertEqual(
            row["path"],
            "experiments/X-105111-anchored-disk-margin-certificate",
        )
        self.assertEqual(row["commit"], V.BASE_COMMIT)
        self.assertEqual(row["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(row["artifact_matches_live_producer"])

    def test_both_same_domain_equalities_are_exact(self) -> None:
        row = V.same_domain_norm_fixture()
        self.assertEqual(row["edge_location"], "E subset boundary(Omega)")
        self.assertEqual(row["first_margin"], "1/2")
        self.assertEqual(row["first_weighted_supremum"], "8")
        self.assertEqual(row["first_weighted_supremum"], row["tau_1_over_first_margin"])
        self.assertEqual(row["product_margin"], "2/5")
        self.assertEqual(row["second_weighted_supremum"], "15/2")
        self.assertEqual(
            row["second_weighted_supremum"],
            row["tau_2_over_product_margin"],
        )
        self.assertTrue(row["both_same_domain_equalities_exact"])

    def test_arbitrary_edge_uses_actual_weight_norm_product_bound(self) -> None:
        row = V.arbitrary_edge_fixture()
        self.assertEqual(row["weight_edge_norm"], "1")
        self.assertEqual(row["first_margin"], "1/8")
        self.assertEqual(row["actual_weighted_norm"], "2")
        self.assertEqual(row["actual_weight_norm_product_upper"], "8")
        self.assertTrue(row["product_inequality_can_be_strict"])

    def test_closure_maximum_modulus_gives_only_tau_envelope(self) -> None:
        row = V.arbitrary_edge_fixture()
        self.assertTrue(row["maximum_modulus_gives_weight_edge_norm_at_most_tau"])
        self.assertEqual(row["tau_margin_envelope"], "8")
        self.assertNotEqual(row["actual_weighted_norm"], row["tau_margin_envelope"])
        self.assertTrue(row["tau_envelope_need_not_be_equality"])

    def test_polynomial_derivative_identities_are_exact(self) -> None:
        row = V.counterexample_fixture()
        self.assertEqual(row["exponent_coefficients"], ["0", "0", "0", "0", "1/4"])
        self.assertEqual(row["log_derivative_coefficients"], ["0", "0", "0", "1"])
        self.assertEqual(
            row["normalized_second_coefficients"],
            ["0", "0", "3", "0", "0", "0", "1"],
        )
        self.assertEqual(row["F_prime"], "z^3*F")
        self.assertEqual(row["F_second"], "z^2*(z^4+3)*F")

    def test_manifest_and_optimal_selector_are_exact(self) -> None:
        row = V.counterexample_fixture()
        self.assertEqual(
            row["first_manifest"],
            [{"point": "0", "order": 3, "role": "target"}],
        )
        self.assertEqual(row["first_target_principal_coefficient"], "1")
        self.assertEqual(row["optimal_selector"], "z^2")
        self.assertEqual(row["optimal_selector_norm_tau"], "1")
        self.assertTrue(row["optimality_from_maximum_modulus"])

    def test_half_radius_arc_has_no_denominator_event(self) -> None:
        row = V.counterexample_fixture()["half_radius_upper_semicircle"]
        self.assertEqual(row["F_second_factor_lower_bound"], "47/16")
        self.assertFalse(row["is_selector_domain_boundary"])

    def test_half_radius_arc_refutes_broad_tau_equality(self) -> None:
        row = V.counterexample_fixture()["half_radius_upper_semicircle"]
        self.assertEqual(row["first_margin"], "1/8")
        self.assertEqual(row["actual_weighted_norm"], "2")
        self.assertEqual(row["tau_over_margin"], "8")
        self.assertFalse(row["tau_equality_holds"])

    def test_half_radius_actual_weight_norm_bound_is_attained(self) -> None:
        row = V.counterexample_fixture()["half_radius_upper_semicircle"]
        self.assertEqual(row["weight_edge_norm"], "1/4")
        self.assertEqual(row["actual_weight_norm_product_bound"], "2")
        self.assertEqual(
            row["actual_weighted_norm"],
            row["actual_weight_norm_product_bound"],
        )

    def test_unit_semicircle_recovers_same_domain_equality(self) -> None:
        row = V.counterexample_fixture()["unit_upper_semicircle"]
        self.assertTrue(row["is_selector_domain_boundary"])
        self.assertEqual(row["first_margin"], "1")
        self.assertEqual(row["actual_weighted_norm"], "1")
        self.assertEqual(row["tau_over_margin"], "1")
        self.assertTrue(row["tau_equality_holds"])

    def test_general_radius_ledger_locates_equality_exactly(self) -> None:
        row = V.counterexample_fixture()
        self.assertEqual(row["general_radius_actual_norm"], "1/r")
        self.assertEqual(row["general_radius_tau_over_margin"], "1/r^3")
        self.assertTrue(row["tau_equality_for_0_less_r_at_most_1_iff_r_equals_1"])

    def test_repair_ledger_is_forward_only_and_names_frozen_scope(self) -> None:
        row = V.repair_ledger()
        self.assertEqual(len(row["affected_frozen_files"]), 6)
        self.assertTrue(row["literal_wording_overbroad_or_ambiguous"])
        self.assertTrue(row["intended_same_domain_reading_repaired"])
        self.assertFalse(row["frozen_105109_files_modified"])
        self.assertFalse(row["retrospective_105109_verification_claimed"])
        self.assertTrue(row["t105109_same_unit_disk_obstruction_survives"])

    def test_no_forbidden_control_characters_in_load_bearing_files(self) -> None:
        self.assertEqual(V.forbidden_control_characters(), [])

    def test_mutation_firewalls_remain_closed(self) -> None:
        row = V.mutation_firewalls()
        self.assertEqual(len(row), 12)
        self.assertTrue(all(value is False for value in row.values()))
        self.assertFalse(row["constant_modulus_transfers_to_every_other_boundary"])
        self.assertFalse(row["t105109_was_retrospectively_reverified"])
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
        self.assertTrue(scope["same_selector_domain_first_equality_verified"])
        self.assertTrue(scope["same_selector_domain_second_equality_verified"])
        self.assertTrue(scope["off_selector_boundary_tau_equality_refuted"])
        self.assertFalse(scope["retrospective_105109_verification_claimed"])
        self.assertFalse(scope["xi_margin_or_collar_authenticated"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
