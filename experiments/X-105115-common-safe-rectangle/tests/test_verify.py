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
SPEC = importlib.util.spec_from_file_location("t105115_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105115 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105115(unittest.TestCase):
    def test_frozen_dependency_is_authenticated(self) -> None:
        row = V.dependency_checkpoint()
        self.assertEqual(row["commit"], V.BASE_COMMIT)
        self.assertEqual(row["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(row["artifact_matches_live_producer"])

    def test_metadata_base_and_dependency_are_exact(self) -> None:
        row = V.metadata_ledger()
        self.assertEqual(row["checkpoint_base"], V.CHECKPOINT_BASE)
        self.assertEqual(row["dependency_commit"], V.BASE_COMMIT)
        self.assertEqual(row["dependency_digest"], V.BASE_DIGEST)
        self.assertFalse(row["heavy_computation_run"])

    def test_projection_intervals_are_merged_exactly(self) -> None:
        row = V.geometry_fixture()
        self.assertEqual(row["merged_bad_T"], [["3/2", "5/2"], ["11/4", "13/4"]])
        self.assertEqual(row["merged_bad_eta"], [["1/2", "3/2"], ["7/4", "9/4"]])

    def test_projection_and_safe_measures_are_exact(self) -> None:
        row = V.geometry_fixture()
        self.assertEqual(row["bad_measures"], {"T": "3/2", "eta": "3/2"})
        self.assertEqual(row["good_measures"], {"T": "3/2", "eta": "3/2"})
        self.assertEqual(row["safe_product_measure"], "9/4")

    def test_strict_total_radius_gate_and_safe_pair(self) -> None:
        row = V.geometry_fixture()
        self.assertEqual(row["total_radius"], "1")
        self.assertEqual(row["twice_total_radius"], "2")
        self.assertTrue(row["strict_total_radius_gate_holds"])
        self.assertEqual(row["selected_safe_pair"], {"T": "7/2", "eta": "5/2"})

    def test_supporting_line_scope_is_not_overstated(self) -> None:
        self.assertTrue(V.geometry_fixture()["supporting_line_product_is_only_sufficient_for_finite_edges"])

    def test_nonstrict_gate_counterexample_is_exact(self) -> None:
        row = V.sharpness_fixture()
        self.assertTrue(row["Delta_equals_2S"])
        self.assertEqual(row["bad_measure"], "2")
        self.assertEqual(row["safe_measure"], "0")
        self.assertTrue(row["nonstrict_gate_is_insufficient"])

    def test_sharpness_claim_is_coordinatewise(self) -> None:
        self.assertEqual(
            V.sharpness_fixture()["sharpness_scope"],
            "coordinatewise using only total radius",
        )

    def test_restricted_tonelli_normalization_is_exact(self) -> None:
        row = V.tonelli_ledger()
        self.assertEqual(row["unrestricted_mean"], "2")
        self.assertEqual(row["selected_safe_bound"], "8")
        self.assertEqual(row["exact_kappa"], "4")
        self.assertEqual(row["total_radius_relaxed_kappa"], "9")

    def test_full_shell_integrability_firewall_is_explicit(self) -> None:
        row = V.tonelli_ledger()
        self.assertTrue(row["full_shell_integrability_required_for_kappa_comparison"])
        self.assertFalse(row["unsafe_raw_singularities_are_automatically_integrable"])
        self.assertIn("restricted integral", row["safe_only_fallback"])

    def test_raw_quotient_envelopes_are_exact(self) -> None:
        row = V.raw_quotient_ledger()
        self.assertEqual(row["quotient_sup_bounds"], {"F/F'": "3", "F^2/(F'F'')": "6"})
        self.assertEqual(row["selected_edge_length"], "24")
        self.assertEqual(row["weighted_integral_bounds"]["using_I_1"], "15")
        self.assertEqual(row["weighted_integral_bounds"]["using_I_2"], "42")

    def test_raw_route_allows_F_zeros_but_covers_denominators(self) -> None:
        row = V.raw_quotient_ledger()
        self.assertFalse(row["F_zero_disks_required"])
        self.assertEqual(row["denominator_zero_cover_required"], ["F'", "F''"])
        self.assertFalse(row["post_cancellation_minimality_claimed"])

    def test_selector_domain_firewall_is_preserved(self) -> None:
        row = V.selector_firewall()
        self.assertTrue(row["same_domain_optimal_selector_constant_modulus"])
        self.assertFalse(row["outer_optimal_selector_constant_modulus_on_intermediate_edge_is_guaranteed"])
        self.assertTrue(row["fixed_outer_carriers_required_for_shell_average"])
        self.assertFalse(row["rebuilding_after_rectangle_selection_is_allowed"])

    def test_mutation_firewalls_and_control_characters(self) -> None:
        row = V.mutation_firewalls()
        self.assertEqual(len(row), 12)
        self.assertTrue(all(value is False for value in row.values()))
        self.assertEqual(V.forbidden_control_characters(), [])

    def test_payload_scope_remains_finite_and_non_RH(self) -> None:
        scope = V.build_payload()["scope"]
        self.assertTrue(scope["finite_supporting_line_projection_verified"])
        self.assertTrue(scope["restricted_tonelli_normalization_verified"])
        self.assertFalse(scope["full_shell_integrability_authenticated_for_xi"])
        self.assertFalse(scope["cofinal_xi_safe_shell_established"])
        self.assertFalse(scope["selector_margin_absorption_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])

    def test_payload_hashes_result_and_digest(self) -> None:
        artifact = json.loads((ROOT / "results" / "verification.json").read_text(encoding="utf-8"))
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))
        self.assertEqual(len(artifact["content_sha256"]), 7)
        self.assertEqual(artifact["classification"], artifact["verdict"])
        self.assertEqual(artifact["source"]["checkpoint_base"], V.CHECKPOINT_BASE)
        claimed = artifact.pop("proof_object_sha256")
        canonical = json.dumps(artifact, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(claimed, hashlib.sha256(canonical).hexdigest())


if __name__ == "__main__":
    unittest.main()
