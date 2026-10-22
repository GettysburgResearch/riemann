#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t105111_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105111 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105111(unittest.TestCase):
    def test_frozen_dependency_is_authenticated(self) -> None:
        dependency = V.dependency_checkpoint()
        self.assertEqual(
            dependency["path"],
            "experiments/X-105110-principal-part-edge-cancellation",
        )
        self.assertEqual(dependency["commit"], V.BASE_COMMIT)
        self.assertEqual(dependency["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(dependency["artifact_matches_live_producer"])

    def test_normalized_derivative_identities_are_coefficient_exact(self) -> None:
        row = V.normalized_derivative_fixture()
        self.assertEqual(row["first_derivative_identity"], "G1_prime=A-L^2")
        self.assertEqual(
            row["product_derivative_identity"],
            "G12_prime=A^2+L*B-2*L^2*A",
        )
        self.assertTrue(row["identities_verified_by_polynomial_coefficients"])
        self.assertGreater(len(row["normalized_third_coefficients"]), 3)

    def test_log_density_identities_are_cross_multiplied_exactly(self) -> None:
        row = V.normalized_derivative_fixture()
        self.assertEqual(row["density_probe"], "1/3")
        self.assertEqual(row["first_density"], row["first_density_formula"])
        self.assertEqual(row["product_density"], row["product_density_formula"])

    def test_anchored_drop_uses_signed_subarcs_and_includes_anchor(self) -> None:
        row = V.anchored_drop_fixture()
        self.assertEqual(row["values_left_anchor_right"], ["1", "7/8", "3/4"])
        self.assertEqual(row["exact_downward_ratio"], "7/6")
        self.assertEqual(row["exact_drop"], "log(7/6)")
        self.assertTrue(row["anchor_included_so_drop_nonnegative"])
        self.assertTrue(row["signed_subarc_integral_used"])

    def test_total_variation_is_a_sufficient_relaxation(self) -> None:
        row = V.anchored_drop_fixture()
        self.assertEqual(row["total_variation_ratio"], "4/3")
        self.assertLessEqual(
            F(row["exact_downward_ratio"]),
            F(row["total_variation_ratio"]),
        )
        self.assertTrue(row["real_log_variation_no_larger_than_complex_variation"])
        self.assertTrue(row["nonvanishing_authenticated_before_log_division"])

    def test_rational_fixture_margins_and_drop_ratios_are_exact(self) -> None:
        row = V.rational_margin_fixture()
        self.assertEqual(row["first_margin"], "3/4")
        self.assertEqual(row["product_margin"], "15/64")
        self.assertEqual(row["first_drop_ratio"], "4/3")
        self.assertEqual(row["product_drop_ratio"], "16/5")
        self.assertTrue(row["both_monotone_positive"])

    def test_two_closed_disks_cover_the_complete_edge(self) -> None:
        row = V.disk_cover_fixture()
        self.assertEqual(row["centers"], ["1/4", "3/4"])
        self.assertEqual(row["radius"], "1/4")
        self.assertEqual(row["real_intervals"], [["0", "1/2"], ["1/2", "1"]])
        self.assertTrue(row["complete_edge_including_endpoints_covered"])
        self.assertTrue(row["closed_disks_inside_holomorphy_domain"])

    def test_first_disk_center_derivative_and_slack_ledger_is_exact(self) -> None:
        row = V.disk_cover_fixture()
        self.assertEqual(row["first_center_values"], ["15/16", "13/16"])
        self.assertEqual(row["first_derivative_suprema"], ["1/4", "1/4"])
        self.assertEqual(row["first_slacks"], ["7/8", "3/4"])
        self.assertEqual(row["minimum_first_slack"], "3/4")

    def test_product_disk_derivative_suprema_are_attained_exactly(self) -> None:
        row = V.disk_cover_fixture()
        self.assertEqual(row["product_derivative_suprema"], ["11/16", "131/256"])
        self.assertEqual(
            row["product_majorant_coefficients"],
            [["611/256", "45/8", "3"], ["443/256", "39/8", "3"]],
        )
        self.assertTrue(row["product_suprema_exact_by_positive_coefficient_attainment"])

    def test_product_disk_slacks_are_positive_and_exact(self) -> None:
        row = V.disk_cover_fixture()
        self.assertEqual(row["product_center_values"], ["2415/4096", "1365/4096"])
        self.assertEqual(row["product_slacks"], ["1711/4096", "841/4096"])
        self.assertEqual(row["minimum_product_slack"], "841/4096")
        self.assertGreater(F(row["minimum_product_slack"]), 0)

    def test_fixed_anchor_family_attains_exponential_loss(self) -> None:
        row = V.sharp_anchor_fixture()
        self.assertEqual(row["q_probe"], "1/4")
        self.assertEqual(row["anchor_value"], "1")
        self.assertEqual(row["margin"], "1/4")
        self.assertEqual(row["drop_ratio"], "4")
        self.assertTrue(row["exponential_loss_attained"])

    def test_first_margin_does_not_control_product_margin(self) -> None:
        row = V.first_product_independence_fixture()
        self.assertEqual(row["parameter_probe"], "1/4")
        self.assertEqual(row["first_margin"], "3/4")
        self.assertEqual(row["product_factor"], "1/16")
        self.assertEqual(row["product_margin"], "3/64")
        self.assertTrue(row["first_margin_stays_positive_at_product_collapse"])
        self.assertFalse(row["first_margin_alone_controls_product_margin"])

    def test_counterfamily_polynomial_and_nonsample_values_are_exact(self) -> None:
        row = V.counterfamily_fixture()
        self.assertEqual(row["Q_coefficients"], ["0", "0", "1/4", "0", "-5/4", "0", "1"])
        self.assertEqual(row["Q_at_nonsample"], "-315/4096")
        self.assertEqual(row["Q_prime_at_nonsample"], "-159/512")
        self.assertEqual(row["Q_square_at_nonsample"], "99225/16777216")

    def test_counterfamily_global_first_manifest_and_selector_are_fixed(self) -> None:
        row = V.counterfamily_fixture()
        self.assertEqual(
            row["global_first_event_manifest"],
            [{"point": "0", "order": 1, "role": "target"}],
        )
        self.assertEqual(row["first_target_residue"], "1")
        self.assertEqual(row["first_optimal_selector"], "1")
        self.assertEqual(row["first_optimal_selector_norm"], "1")
        self.assertTrue(row["complete_first_manifest_is_stable"])

    def test_counterfamily_anchor_values_are_parameter_independent(self) -> None:
        row = V.counterfamily_fixture()
        self.assertEqual(
            row["anchor_rows"],
            [
                {"point": "1/2", "L": "1/2", "L_prime": "1", "A": "5/4", "L_times_A": "5/8"},
                {"point": "1", "L": "1", "L_prime": "1", "A": "2", "L_times_A": "2"},
            ],
        )

    def test_counterfamily_nonsample_collapse_has_exact_rational_certificate(self) -> None:
        row = V.counterfamily_fixture()
        self.assertEqual(row["collapse_sequence"], "C_n=n/Q(zeta)^2")
        self.assertEqual(row["collapse_linear_coefficient"], "212/35")
        self.assertEqual(
            row["nonsample_A_formula"],
            "zeta^2*exp(-2*n)+(1-(212/35)*n)*exp(-n)",
        )
        self.assertEqual(row["exp_minus_n_bound"], "6/n^3")
        self.assertEqual(row["bound_probe_n"], 8)
        self.assertTrue(row["both_nonsample_denominators_converge_to_zero"])
        self.assertFalse(row["product_log_drop_is_uniformly_bounded"])

    def test_mutation_firewalls_remain_closed(self) -> None:
        firewall = V.mutation_firewalls()
        self.assertEqual(len(firewall), 16)
        self.assertTrue(all(value is False for value in firewall.values()))
        self.assertFalse(firewall["log_division_is_valid_before_nonvanishing_authentication"])
        self.assertFalse(firewall["arbitrary_weight_has_constant_modulus_selector_equality"])
        self.assertFalse(firewall["first_margin_controls_product_margin"])
        self.assertFalse(firewall["stable_first_manifest_implies_stable_second_manifest"])
        self.assertFalse(firewall["counterfamily_has_uniform_product_log_drop"])
        self.assertFalse(firewall["rh_established"])

    def test_artifact_matches_live_producer_and_hash_manifest(self) -> None:
        artifact = json.loads((ROOT / "results" / "verification.json").read_text(encoding="utf-8"))
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))
        self.assertEqual(len(artifact["content_sha256"]), 7)

    def test_canonical_digest_and_open_scope(self) -> None:
        artifact = V.build_payload()
        claimed = artifact.pop("proof_object_sha256")
        canonical = json.dumps(artifact, sort_keys=True, separators=(",", ":")).encode()
        self.assertEqual(claimed, hashlib.sha256(canonical).hexdigest())
        scope = artifact["scope"]
        self.assertTrue(scope["exact_anchored_log_drop_verified"])
        self.assertTrue(scope["finite_disk_positive_slack_certificate_verified"])
        self.assertTrue(scope["selector_equality_restricted_to_same_selector_domain_boundary_arc"])
        self.assertFalse(scope["xi_anchor_values_authenticated"])
        self.assertFalse(scope["xi_zero_free_disk_cover_authenticated"])
        self.assertFalse(scope["xi_log_variation_bounds_proved"])
        self.assertFalse(scope["xi_third_normalized_derivative_bounds_proved"])
        self.assertFalse(scope["cofinal_green_gram_selector_growth_absorbed"])
        self.assertFalse(scope["xi_pole_subtracted_remainder_and_corner_ledger_proved"])
        self.assertFalse(scope["strict_xi_jet_coherence_margin_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
