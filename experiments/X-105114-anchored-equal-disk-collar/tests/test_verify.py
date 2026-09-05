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
SPEC = importlib.util.spec_from_file_location("t105114_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105114 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105114(unittest.TestCase):
    def test_frozen_dependency_is_authenticated(self) -> None:
        row = V.dependency_checkpoint()
        self.assertEqual(row["commit"], V.BASE_COMMIT)
        self.assertEqual(row["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(row["artifact_matches_live_producer"])

    def test_hypotheses_and_normalization_are_explicit(self) -> None:
        row = V.formula_ledger()
        self.assertEqual(row["hypotheses"]["radii"], "0<r_1<r_2<r_3")
        self.assertEqual(row["hypotheses"]["epsilon"], "0<epsilon<=1")
        self.assertEqual(row["hypotheses"]["anchor"], "f(a)!=0")
        self.assertTrue(row["amplitude_scale_invariant"])
        self.assertTrue(row["coordinate_scale_invariant"])

    def test_jensen_count_and_radius_budget_are_recorded(self) -> None:
        row = V.formula_ledger()
        self.assertEqual(row["jensen_count"], "n<=A_f/beta")
        self.assertEqual(row["nominal_radius_sum"], "S_f<=epsilon*r_2*A_f/beta")

    def test_strong_intermediate_bound_retains_multiplicity(self) -> None:
        row = V.formula_ledger()
        self.assertIn("-n*log(2/epsilon)", row["strong_intermediate_bound"])
        self.assertIn("2*r_1/(r_2-r_1)", row["combined_bound"])

    def test_standard_radii_reduce_exactly(self) -> None:
        row = V.standard_radius_ledger()
        self.assertEqual(row["beta"], "1")
        self.assertEqual(row["harnack_coefficient"], "2")
        self.assertEqual(row["nominal_radius_sum"], "S_f<=2*epsilon*R*A_f")

    def test_rational_fixture_replays_constants(self) -> None:
        row = V.rational_fixture()
        self.assertEqual(row["harnack_coefficient"], "2")
        self.assertEqual(row["combined_coefficient"], "5")
        self.assertEqual(row["epsilon_disk_radius"], "1/2")

    def test_fixture_counts_zeros_with_multiplicity(self) -> None:
        row = V.rational_fixture()
        self.assertEqual(row["total_multiplicity"], 4)
        self.assertEqual(row["functions"][1]["zeros"], ["1/4", "1/4"])
        self.assertEqual(row["nominal_radius_sum"], "2")

    def test_jensen_power_checks_are_exact(self) -> None:
        rows = V.rational_fixture()["functions"]
        self.assertEqual([row["jensen_power_check"] for row in rows], ["2^1<=17", "2^2<=289", "2^1<=33"])

    def test_blaschke_factor_and_probe_checks_are_exact(self) -> None:
        row = V.rational_fixture()
        self.assertEqual(row["probe"], "2/5")
        self.assertEqual(len(row["factor_rows"]), 3)
        self.assertEqual(row["probe_values"], ["13/5", "9/25", "21/5"])

    def test_selected_rectangle_avoids_unique_bad_disks(self) -> None:
        row = V.rational_fixture()
        self.assertEqual(row["selected_rectangle"], {"T": "4/5", "eta": "3/5"})
        self.assertTrue(row["selected_rectangle_avoids_all_unique_disks"])

    def test_exact_projection_can_beat_nominal_relaxation(self) -> None:
        row = V.projection_fixture()
        self.assertEqual(row["positive_vertical_bad_union"], "[0,3/4]")
        self.assertEqual(row["positive_horizontal_bad_union"], "[0,1/2]")
        self.assertTrue(row["exact_projection_can_beat_nominal_2S_relaxation"])

    def test_raw_route_charges_only_denominator_zeros(self) -> None:
        row = V.raw_quotient_ledger()
        self.assertEqual(row["lower_modulus_disk_indices"], [1, 2])
        self.assertFalse(row["F_zero_disks_charged"])
        self.assertTrue(row["log_derivative_route_requires_F_nonzero"])

    def test_source_and_xi_normalization_are_locked(self) -> None:
        row = V.source_and_normalization_ledger()
        self.assertFalse(row["printed_display_imported_verbatim"])
        self.assertEqual(row["proof_normalization"], "f(z)/f(a)")
        self.assertEqual(row["xi_normalization"], "Xi_t(z)=xi(1/2+i*z)")
        self.assertFalse(row["origin_is_common_three_derivative_anchor"])

    def test_constant_function_refutes_unnormalized_display(self) -> None:
        row = V.amplitude_counterexample()
        self.assertEqual(row["growth_difference"], "0")
        self.assertEqual(row["claimed_right_side"], "0")
        self.assertTrue(row["literal_unnormalized_display_false"])
        self.assertEqual(row["normalized_left_side"], "0")

    def test_mutation_firewalls_and_control_characters(self) -> None:
        row = V.mutation_firewalls()
        self.assertEqual(len(row), 12)
        self.assertTrue(all(value is False for value in row.values()))
        self.assertEqual(V.forbidden_control_characters(), [])

    def test_payload_hashes_digest_and_open_scope(self) -> None:
        artifact = json.loads((ROOT / "results" / "verification.json").read_text(encoding="utf-8"))
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))
        self.assertEqual(len(artifact["content_sha256"]), 7)
        claimed = artifact.pop("proof_object_sha256")
        canonical = json.dumps(artifact, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(claimed, hashlib.sha256(canonical).hexdigest())
        scope = artifact["scope"]
        self.assertTrue(scope["normalized_finite_minimum_modulus_verified"])
        self.assertTrue(scope["raw_route_smaller_exceptional_union_verified"])
        self.assertFalse(scope["common_xi_anchor_authenticated"])
        self.assertFalse(scope["selector_margin_absorption_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
