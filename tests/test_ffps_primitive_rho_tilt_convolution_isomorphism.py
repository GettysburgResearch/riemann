from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_primitive_rho_tilt_convolution_isomorphism.py"
)
SPEC = importlib.util.spec_from_file_location("primitive_rho_convolution", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class PrimitiveRhoTiltConvolutionIsomorphismTest(unittest.TestCase):
    def test_predecessor_blobs(self) -> None:
        subject.check_predecessor_blobs()
        subject.check_scope_markers()

    def test_exact_local_coefficients(self) -> None:
        self.assertEqual(subject.g_prime_power(2, 0), 1)
        self.assertEqual(subject.g_prime_power(2, 4), Fraction(1, 3))
        self.assertEqual(subject.h_prime_power(2, 4), Fraction(-8, 81))
        panel = subject.local_coefficient_panel(5, 7)
        self.assertEqual(panel["rho_p"], "5/6")
        self.assertEqual(len(panel["rows"]), 8)
        self.assertTrue(all(row["a"] == row["m_times_g"] for row in panel["rows"]))
        self.assertTrue(all(row["m"] == row["a_times_h"] for row in panel["rows"]))
        self.assertTrue(all(row["delta"] == row["g_times_h"] for row in panel["rows"]))

    def test_exact_global_convolutions(self) -> None:
        for n in range(1, 181):
            if n % subject.EXCEPTIONAL_PRIME == 0:
                continue
            with self.subTest(n=n):
                self.assertEqual(
                    subject.dirichlet_convolution_value(subject.m, subject.g, n),
                    subject.a(n),
                )
                self.assertEqual(
                    subject.dirichlet_convolution_value(subject.a, subject.h, n),
                    subject.m(n),
                )
                self.assertEqual(
                    subject.dirichlet_convolution_value(subject.g, subject.h, n),
                    subject.delta(n),
                )

    def test_multiplicative_values(self) -> None:
        self.assertEqual(subject.rho(30), Fraction(5, 12))
        self.assertEqual(subject.a(30), Fraction(-5, 12))
        self.assertEqual(subject.g(12), Fraction(1, 12))
        self.assertEqual(subject.h(12), Fraction(1, 18))

    def test_finite_operator_inverse(self) -> None:
        certificate = subject.finite_operator_certificate(32)
        self.assertEqual(certificate["dimension"], 32)
        self.assertTrue(certificate["inverse_both_orders"])
        self.assertTrue(certificate["unit_diagonal"])

    def test_exact_summatory_transfers(self) -> None:
        transfer = subject.summatory_transfer_panel(90)
        exceptional = subject.exceptional_prime_transfer_panel(150)
        self.assertEqual(transfer["checked_endpoints"], 90)
        self.assertEqual(exceptional["checked_endpoints"], 150)
        self.assertTrue(
            all(
                row["M_rho"] == row["M_rho_from_g"] and row["M_0"] == row["M_0_from_h"]
                for row in transfer["sample_rows"]
            )
        )
        self.assertTrue(
            all(
                row["M"] == row["M_from_M_0"] and row["M_0"] == row["M_0_from_M"]
                for row in exceptional["sample_rows"]
            )
        )

    def test_half_weighted_pair_coefficients(self) -> None:
        panel = subject.pair_coefficient_panel()
        for row in panel["rows_after_clearing_common_half_weight"]:
            self.assertEqual(
                row["rho_scaled_coefficient"],
                row["rho_via_g_scaled_coefficient"],
            )
            self.assertEqual(
                row["ordinary_scaled_coefficient"],
                row["ordinary_via_h_scaled_coefficient"],
            )

    def test_primitive_boolean_pair_compression(self) -> None:
        panel = subject.primitive_boolean_pair_panel()
        self.assertTrue(panel["forward_inverse_absolute_masses_equal"])
        self.assertEqual(panel["primitive_scalar_uniform_cost_both_directions"], "K_67")
        self.assertEqual(
            panel["primitive_squared_energy_uniform_cost_both_directions"],
            "K_67^2",
        )
        self.assertTrue(
            all(
                row["rho_scaled_coefficient"] == row["rho_via_boolean_g"]
                and row["ordinary_scaled_coefficient"] == row["ordinary_via_boolean_h"]
                for row in panel["rows"]
            )
        )
        self.assertTrue(
            all(
                row["absolute_forward_state_mass"] == row["absolute_inverse_state_mass"]
                for row in panel["local_rows"]
            )
        )

    def test_primitive_support_equivalence(self) -> None:
        panel = subject.primitive_support_equivalence_panel(6)
        self.assertTrue(panel["equivalence"])
        self.assertEqual(panel["checked_quintuples"], 6**5)
        self.assertGreater(panel["surviving_quintuples"], 0)
        self.assertTrue(subject.raw_primitive_support(2, 3, 5, 7, 11))
        self.assertFalse(subject.raw_primitive_support(2, 3, 5, 7, 10))
        self.assertEqual(
            subject.raw_primitive_support(2, 3, 5, 7, 11),
            subject.compressed_primitive_support(2, 3, 5, 7, 11),
        )

    def test_finite_generalized_panel_certificate(self) -> None:
        panel = subject.finite_generalized_panel_certificate()
        self.assertEqual(
            panel["direct_scaled_value"], panel["generalized_scaled_value"]
        )
        self.assertGreater(panel["direct_terms"], 0)
        self.assertGreater(panel["generalized_terms"], panel["direct_terms"])
        self.assertEqual(panel["sieve"], 7)
        self.assertEqual(panel["total_product"], 30)

    def test_compatible_triple_bijection(self) -> None:
        panel = subject.compatible_triple_panel(6)
        self.assertTrue(panel["bijection"])
        self.assertTrue(
            all(
                row["admissible_triples"] == row["image_triples"]
                for row in panel["rows"]
            )
        )
        self.assertTrue(all(row["bounded_image_exhausted"] for row in panel["rows"]))
        self.assertEqual(panel["bit_cube_exhaustion"]["compatible_triples"], 64)
        self.assertEqual(panel["bit_cube_exhaustion"]["zero_mode_triples"], 27)
        self.assertTrue(panel["bit_cube_exhaustion"]["independent_target_scan_equal"])
        self.assertTrue(
            all(
                row["compatible_triples"] == 3 ** row["omega"]
                and row["zero_mode_saturated_rays"] == 2 ** row["omega"]
                for row in panel["color_count_rows"]
            )
        )
        triple = subject.compatible_triple(2, 0, 6, 5, 7)
        self.assertEqual(triple, (67**2 * 6, 5, 210))
        self.assertEqual(subject.recover_compatible_triple(2, 0, *triple), (6, 5, 7))
        with self.assertRaises(ValueError):
            subject.recover_compatible_triple(0, 0, 4, 5, 20)
        with self.assertRaises(ValueError):
            subject.recover_compatible_triple(1, 0, 6, 5, 30)
        hierarchy = subject.gate_hierarchy_panel()
        exact = hierarchy["exact_conversion_witness"]
        self.assertEqual(exact["compatible_ray_energy"], "9/5")
        self.assertEqual(exact["restricted_full_q_energy"], "3/10")
        self.assertEqual(exact["ratio"], "6")
        off_ray = hierarchy["off_ray_blindness_witness"]
        self.assertEqual(off_ray["compatible_d_energy"], "0")
        self.assertEqual(off_ray["restricted_ray_q_energy"], "0")
        self.assertEqual(off_ray["full_q_energy"], "1/5")
        hidden = hierarchy["collective_gate_is_weaker_than_uniform_ray_control"]
        self.assertEqual(
            hidden["rows"][-1]["collective_weighted_contribution_squared"], "1/11"
        )
        self.assertFalse(hierarchy["ray_and_full_q_gates_formally_comparable"])
        coloring = subject.fixed_q_coloring_panel()
        self.assertEqual(
            [row["color_count"] for row in coloring["sweep_rows"]],
            [1, 2, 4, 8],
        )
        self.assertEqual(
            [row["cleared_common_weight"] for row in coloring["sweep_rows"]],
            ["1", "1/3", "1/12", "1/72"],
        )
        witness = coloring["synthetic_cancellation_witness"]
        self.assertEqual(witness["color_vector"], ["1"])
        self.assertEqual(witness["color_energy"], "1")
        self.assertEqual(witness["largest_ray_energy"], "9")
        self.assertEqual(witness["raywise_l1_norm"], "11")
        self.assertEqual(witness["squared_outer_coefficient"], "1/864")
        self.assertEqual(witness["auxcolor_quadratic_contribution"], "1/(12*sqrt(6))")
        self.assertEqual(
            witness["zero_mode_coefficient_squared_times_color_energy"], "1/864"
        )
        reverse = coloring["remote_ray_reverse_witness"]
        self.assertEqual(reverse["raywise_weighted_l1_contribution_squared"], "1/11")
        self.assertEqual(reverse["weighted_color_energy_squared"], "144/11")

    def test_colored_cube_norm_and_hereditary_replay(self) -> None:
        panel = subject.colored_cube_panel(2)
        self.assertEqual(panel["configuration_count"], 9)
        self.assertEqual(panel["checked_coordinate_projections"], 512)
        self.assertGreater(panel["downward_closed_projection_count"], 2)
        self.assertTrue(panel["forward_inverse_norms_equal"])
        self.assertTrue(
            all(
                Fraction(row["two_dimensional_gram_determinant"]) == 1
                for row in panel["local_rows"]
            )
        )

    def test_harmonic_dilation_criticality(self) -> None:
        panel = subject.harmonic_dilation_panel(6, 90)
        self.assertTrue(panel["weight_one_is_critical"])
        self.assertEqual(panel["global_absolute_convergence"], "exactly w<1")
        self.assertIn("delta_R", panel["sharpness_witness"])
        self.assertGreater(panel["height_majorant_checks"], 0)
        for row in panel["rows"]:
            self.assertEqual(
                Fraction(row["left_norm_squared"]),
                Fraction(6 ** row["weight"])
                * Fraction(row["right_restricted_norm_squared"]),
            )

    def test_convergence_majorants_are_exactly_positive(self) -> None:
        rows = subject.convergence_majorant_panel()
        self.assertEqual([row["prime"] for row in rows], list(subject.REPLAY_PRIMES))
        self.assertTrue(
            all(row["g_bound_square_margin_9p_minus_16"] >= 0 for row in rows)
        )
        self.assertTrue(
            all(
                Fraction(row["h_bound_square_margin_p2_over_4_plus_1"]) > 0
                for row in rows
            )
        )

    def test_canonical_fixture_and_firewall(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(result, fixture)
        self.assertTrue(
            result["summatory_seminorm_transfer"]["mertens_exponents_coincide"]
        )
        scope = result["scope_firewall"]
        self.assertFalse(scope["actual_zero_mode_has_native_sieve_average"])
        self.assertFalse(scope["sharp_finite_height_blocks_preserved"])
        self.assertTrue(scope["coprimality_preserved_in_generalized_panel"])
        self.assertFalse(scope["arbitrary_cross_coprimality_obstruction_remaining"])
        self.assertTrue(scope["ratio_kernel_preserved_in_generalized_panel"])
        self.assertFalse(scope["fixed_ratio_band_is_hereditary"])
        self.assertFalse(scope["dyadic_endpoint_structure_preserved"])
        self.assertFalse(scope["generalized_primitive_carleson_estimate_proved"])
        self.assertFalse(scope["genprimcar_and_rayprimcar_formally_equivalent"])
        self.assertFalse(scope["rayprimcar_estimate_proved"])
        self.assertFalse(scope["collprimcar_estimate_proved"])
        self.assertFalse(scope["auxcolorprimcar_estimate_proved"])
        self.assertFalse(scope["colorprimcar_estimate_proved"])
        self.assertTrue(scope["compatible_scale_bijection_proved"])
        self.assertTrue(
            scope["fixed_core_equal_color_weight_extends_to_each_fixed_positive_d"]
        )
        self.assertFalse(scope["fixed_total_modulus_has_d_independent_color_weight"])
        self.assertFalse(
            scope["harmonic_dilation_has_height_independent_absolute_cost"]
        )
        self.assertTrue(
            scope["harmonic_dilation_tax_is_polylog_under_native_height_cutoff"]
        )
        self.assertFalse(scope["weighted_induced_dilation_estimate_proved"])
        self.assertFalse(scope["uniform_induced_dilation_estimate_proved"])
        self.assertFalse(scope["primcar_estimate_proved"])
        self.assertFalse(scope["rh_or_grh_proved"])

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.rho(0)
        with self.assertRaises(ValueError):
            subject.g(67)
        with self.assertRaises(ValueError):
            subject.g_prime_power(67, 1)
        with self.assertRaises(ValueError):
            subject.h_prime_power(4, 1)
        with self.assertRaises(ValueError):
            subject.local_coefficient_panel(2, -1)
        with self.assertRaises(ValueError):
            subject.multiply_matrices(
                [[Fraction(1)]],
                [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]],
            )


if __name__ == "__main__":
    unittest.main()
