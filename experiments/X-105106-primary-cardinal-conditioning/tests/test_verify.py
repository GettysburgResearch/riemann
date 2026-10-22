#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t105106_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load T-105106 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestT105106(unittest.TestCase):
    def test_frozen_dependency_is_authenticated(self) -> None:
        dependency = V.dependency_checkpoint()
        self.assertEqual(dependency["commit"], V.BASE_COMMIT)
        self.assertEqual(dependency["proof_object_sha256"], V.BASE_DIGEST)
        self.assertTrue(dependency["artifact_matches_live_producer"])

    def test_primary_cardinal_formula_hits_every_top_jet(self) -> None:
        row = V.cardinal_fixtures()["mixed_multiplicity"]
        self.assertEqual(row["total_primary_order"], 6)
        self.assertEqual(row["degree"], 5)
        self.assertEqual(
            row["selector"],
            ["1", "7/6", "-7/12", "-5/8", "1/6", "1/24"],
        )

    def test_leading_coefficient_formula_is_exact(self) -> None:
        row = V.cardinal_fixtures()["mixed_multiplicity"]
        self.assertEqual(row["leading_coefficient_formula"], "1/24")
        self.assertEqual(row["selector"][-1], "1/24")

    def test_coefficient_and_separation_envelopes_hold(self) -> None:
        row = V.cardinal_fixtures()["mixed_multiplicity"]
        self.assertTrue(row["coefficient_bound_verified"])
        self.assertTrue(row["separation_bound_verified"])
        self.assertLessEqual(
            F(row["weighted_coefficient_norm"]),
            F(row["uniform_primary_cardinal_bound"]),
        )
        self.assertLessEqual(
            F(row["exact_condition_sum"]), F(row["separation_condition_sum"])
        )

    def test_sign_stable_data_force_real_even_selector(self) -> None:
        row = V.cardinal_fixtures()["real_even_sign_stable"]
        self.assertTrue(row["real_coefficients"])
        self.assertTrue(row["even_selector"])
        self.assertTrue(row["D_even_degree_improves_to_at_most_D_minus_2"])
        self.assertEqual(row["degree"], 8)
        self.assertEqual(row["leading_coefficient_formula"], "0")

    def test_even_cluster_attains_degree_and_delta_exponent(self) -> None:
        row = V.sharp_even_cluster()
        self.assertEqual(row["selector"], ["1", "0", "-50", "0", "625"])
        self.assertEqual(row["total_primary_order"], 5)
        self.assertTrue(row["degree_D_minus_1_is_attained"])
        self.assertTrue(row["delta_exponent_D_minus_1_is_necessary"])

    def test_blaschke_bound_blocks_higher_degree_escape(self) -> None:
        row = V.sharp_even_cluster()
        self.assertEqual(row["exact_unit_circle_sup_norm"], "676")
        self.assertEqual(row["all_holomorphic_selector_blaschke_lower_bound"], "625")
        self.assertGreaterEqual(
            F(row["exact_unit_circle_sup_norm"]),
            F(row["all_holomorphic_selector_blaschke_lower_bound"]),
        )

    def test_first_flux_quartic_selector_is_sharp_and_even(self) -> None:
        row = V.paired_flux_cluster()
        self.assertEqual(row["first_selector"], ["1", "0", "25"])
        self.assertEqual(row["first_unit_circle_sup_norm"], "26")
        self.assertEqual(row["first_blaschke_lower_bound"], "25")
        self.assertEqual(row["rho_jet"], "25")

    def test_second_flux_quartic_selector_is_sharp_and_even(self) -> None:
        row = V.paired_flux_cluster()
        self.assertEqual(row["second_selector"], ["1", "0", "100", "0", "1875"])
        self.assertEqual(row["second_unit_circle_sup_norm"], "1976")
        self.assertEqual(row["second_blaschke_lower_bound"], "1875")
        self.assertEqual(row["rho_jet_squared"], "625")
        self.assertTrue(row["higher_degree_holomorphic_escape_blocked"])

    def test_pole_cancelled_partial_fraction_identity(self) -> None:
        row = V.edge_reduction_fixture()
        self.assertTrue(row["identity_verified"])
        self.assertEqual(row["W_over_M"], "7/36")
        self.assertEqual(row["cardinal_partial_fraction_sum"], "7/36")

    def test_event_data_do_not_bound_holomorphic_remainder(self) -> None:
        row = V.edge_reduction_fixture()
        self.assertTrue(row["same_pole_and_principal_part_for_all_C"])
        self.assertFalse(row["event_data_alone_bounds_holomorphic_remainder"])
        self.assertEqual(row["small_remainder_boundary_norm"], "2")
        self.assertEqual(row["large_remainder_boundary_norm"], "101")

    def test_load_bearing_mutations_fail_closed(self) -> None:
        firewall = V.mutation_firewalls()
        self.assertTrue(firewall["omitted_M_target_normalization_rejected"])
        self.assertTrue(
            firewall["using_local_power_d_instead_of_d_minus_1_rejected"]
        )
        self.assertTrue(firewall["radicalizing_repeated_nontarget_rejected"])

    def test_count_order_and_parity_only_bound_is_refuted(self) -> None:
        firewall = V.mutation_firewalls()
        near = firewall["same_count_orders_and_parity_at_epsilon_1_over_5"]
        nearer = firewall["same_count_orders_and_parity_at_epsilon_1_over_50"]
        self.assertEqual(near["D"], nearer["D"])
        self.assertGreater(F(nearer["norm"]), F(near["norm"]))
        self.assertTrue(firewall["count_multiplicity_parity_only_uniform_bound_refuted"])
        self.assertFalse(
            firewall["unweighted_edge_decay_survives_arbitrary_polynomial_weight"]
        )
        self.assertFalse(firewall["quarantined_moving_order_vandermonde_claim_used"])

    def test_committed_artifact_matches_producer_and_content(self) -> None:
        artifact = json.loads(
            (ROOT / "results" / "verification.json").read_text(encoding="utf-8")
        )
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))

    def test_scope_remains_open(self) -> None:
        scope = V.build_payload()["scope"]
        self.assertTrue(scope["top_jet_primary_cardinal_formula_proved"])
        self.assertTrue(scope["finite_window_coefficient_and_boundary_envelope_proved"])
        self.assertTrue(scope["pole_cancelled_weighted_edge_reduction_proved"])
        self.assertTrue(scope["separation_free_uniform_selector_bound_refuted"])
        self.assertFalse(scope["real_even_parity_cures_selector_conditioning"])
        self.assertFalse(
            scope["sharp_cluster_higher_degree_holomorphic_escape_exists"]
        )
        self.assertFalse(scope["xi_event_manifest_constructed"])
        self.assertFalse(scope["xi_conditioning_products_estimated_cofinally"])
        self.assertFalse(scope["xi_pole_cancelled_holomorphic_factors_estimated"])
        self.assertFalse(scope["xi_weighted_edge_asymptotics_proved"])
        self.assertFalse(scope["strict_xi_jet_coherence_margin_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
