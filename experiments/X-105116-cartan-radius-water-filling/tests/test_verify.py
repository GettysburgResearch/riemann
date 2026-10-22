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
SPEC = importlib.util.spec_from_file_location("t105116_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105116 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105116(unittest.TestCase):
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

    def test_interior_allocation_is_exact(self) -> None:
        row = V.interior_fixture()
        self.assertEqual(row["epsilon"], ["1/6", "2/9", "1/5"])
        self.assertEqual(row["allocated_radius"], ["1/3", "2/3", "1"])
        self.assertEqual(row["budget"], "2")

    def test_interior_kkt_multiplier_is_common(self) -> None:
        row = V.interior_fixture()
        self.assertEqual(row["multiplier"], "3")
        self.assertTrue(row["unique_interior_optimizer"])

    def test_symbolic_log_penalty_identity_is_exact(self) -> None:
        row = V.interior_fixture()
        self.assertEqual(row["log_arguments"], ["12", "9", "10"])
        self.assertEqual(row["encoded_log_product"], "972000")

    def test_capped_water_filling_is_exact(self) -> None:
        row = V.capped_fixture()
        self.assertEqual(row["multiplier"], "1/4")
        self.assertEqual(row["epsilon"], ["1", "4/9"])
        self.assertEqual(row["allocated_radius"], ["1", "4"])
        self.assertTrue(row["first_index_capped"])

    def test_cartan_coefficients_cancel_correctly(self) -> None:
        row = V.cartan_specialization_fixture()
        self.assertEqual(row["u=A/beta"], ["2", "3/2"])
        self.assertEqual(row["v=r_2*A/beta"], ["8", "6"])
        self.assertTrue(row["growth_load_cancels_from_u_over_v"])

    def test_common_radius_gives_equal_epsilon(self) -> None:
        row = V.cartan_specialization_fixture()
        self.assertEqual(row["epsilon"], ["1/7", "1/7"])
        self.assertFalse(row["inverse_growth_allocation_is_optimal"])

    def test_fractional_slack_preserves_strict_gate(self) -> None:
        row = V.fractional_slack_fixture()
        self.assertEqual(row["closed_nominal_budget"], "4")
        self.assertEqual(row["twice_budget"], "8")
        self.assertTrue(row["strict_gate"])

    def test_fractional_slack_bounds_kappa(self) -> None:
        row = V.fractional_slack_fixture()
        self.assertEqual(row["asymmetric_relaxed_kappa"], "15")
        self.assertEqual(row["delta_inverse_square"], "25")
        self.assertTrue(row["symmetric_bound_is_attained_by_maximal_disjoint_projections"])

    def test_strict_open_budget_has_no_minimizer(self) -> None:
        row = V.strict_budget_refutation()
        self.assertFalse(row["minimizer_exists"])
        self.assertTrue(row["closed_budget_optimum_is_open_budget_infimum"])
        self.assertTrue(row["fractional_slack_restores_strict_geometry"])

    def test_formula_ledger_declares_objective_and_cap(self) -> None:
        row = V.formula_ledger()
        self.assertIn("u_j*log", row["objective"])
        self.assertIn("min(1", row["capped_solution"])
        self.assertTrue(row["objective_weights_must_be_declared"])
        self.assertFalse(row["epsilon_independent_spatial_terms_optimized"])

    def test_mutation_firewalls_are_all_false(self) -> None:
        row = V.mutation_firewalls()
        self.assertEqual(len(row), 12)
        self.assertTrue(all(value is False for value in row.values()))

    def test_no_forbidden_control_characters(self) -> None:
        self.assertEqual(V.forbidden_control_characters(), [])

    def test_payload_scope_remains_finite_and_non_RH(self) -> None:
        scope = V.build_payload()["scope"]
        self.assertTrue(scope["capped_finite_optimizer_verified"])
        self.assertTrue(scope["fractional_slack_safe_shell_verified"])
        self.assertFalse(scope["xi_scalarization_weights_authenticated"])
        self.assertFalse(scope["optimized_selector_absorption_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])

    def test_payload_hashes_result_and_digest(self) -> None:
        artifact = json.loads((ROOT / "results" / "verification.json").read_text(encoding="utf-8"))
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))
        self.assertEqual(len(artifact["content_sha256"]), 7)
        self.assertEqual(artifact["classification"], artifact["verdict"])
        claimed = artifact.pop("proof_object_sha256")
        canonical = json.dumps(artifact, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(claimed, hashlib.sha256(canonical).hexdigest())


if __name__ == "__main__":
    unittest.main()
