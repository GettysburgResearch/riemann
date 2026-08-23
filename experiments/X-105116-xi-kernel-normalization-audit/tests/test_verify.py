#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x105116_kernel_audit", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load Xi kernel normalization audit")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestXiKernelNormalizationAudit(unittest.TestCase):
    def test_source_locks_are_exact(self) -> None:
        row = V.source_lock()
        self.assertEqual(row["pr"], 720)
        self.assertEqual(row["pr_head"], "beb9d8a4e10fb8c8deb74bb0505a32fe55cddd14")
        self.assertEqual(len(row["pr_head"]), 40)
        self.assertTrue(row["l104531"]["theta_orbit_source_locked"])

    def test_source_defects_are_explicit(self) -> None:
        row = V.source_lock()
        self.assertTrue(row["l104513"]["origin_multiplicity_term_omitted"])
        self.assertFalse(row["l104528"]["unscaled_fourier_display_is_compatible_with_standard_xi"])

    def test_phi_transform_is_half_xi(self) -> None:
        row = V.normalization_ledger()
        self.assertEqual(row["Fourier(Phi)/Xi"], "1/2")
        self.assertEqual(row["standard_kernel_multiplier_over_Phi"], "2")

    def test_l104528_display_requires_repair(self) -> None:
        self.assertTrue(V.normalization_ledger()["l104528_unscaled_display_needs_factor_two_repair"])

    def test_gamma_coefficient_is_four(self) -> None:
        row = V.gamma_constant_ledger()
        self.assertEqual(row["final_pi_squared_coefficient"], "4")
        self.assertIn("4*pi^2", row["corrected_bound"])

    def test_q_offset_is_exact(self) -> None:
        row = V.gamma_constant_ledger()
        self.assertEqual(row["q_offset"], "11/2")
        self.assertEqual(row["q"], "Y+11/2")

    def test_zeta_threshold_is_exact(self) -> None:
        row = V.gamma_constant_ledger()
        self.assertEqual(row["zeta_exponent_at_Y_zero"], "3/2")
        self.assertEqual(row["n_sum"], "sum n^(4-q)<=zeta(3/2)")

    def test_anchor_parity_is_positive(self) -> None:
        row = V.anchor_phase_ledger()
        self.assertIn("cosh", row["even_pair"])
        self.assertIn("sinh", row["odd_pair"])
        self.assertTrue(row["all_fixed_derivatives_nonzero"])

    def test_scope_is_fail_closed(self) -> None:
        row = V.scope()
        self.assertTrue(row["normalization_algebra_verified"])
        self.assertFalse(row["unmerged_source_blobs_imported"])
        self.assertFalse(row["xi_growth_claim_frozen_as_proof_object"])
        self.assertFalse(row["rh_established"])

    def test_committed_result_matches_producer(self) -> None:
        artifact = json.loads((ROOT / "results" / "verification.json").read_text(encoding="utf-8"))
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(artifact["classification"], artifact["verdict"])
        self.assertFalse(artifact["heavy_computation_run"])


if __name__ == "__main__":
    unittest.main()
