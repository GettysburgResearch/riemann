"""Source-specific first chaos, physical mask order and native activation paths."""

import importlib.util
import json
import unittest
from fractions import Fraction
from itertools import product
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "native-six-hour"
    / "native_first_chaos_augmentation.py"
)
SPEC = importlib.util.spec_from_file_location("native_six_hour_first_chaos", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeFirstChaosTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.geodesic = M.geodesic_module()
        cls.zero = M.vector_control(cls.geodesic, cls.geodesic.zero_spec(), True)
        native = json.loads(
            cls.geodesic.source_bytes((cls.geodesic.DENSE, cls.geodesic.DENSE_JSON))
        )
        cls.positive = M.vector_control(
            cls.geodesic, cls.geodesic.held_out_spec(native)
        )

    def test_complete_source_local_walsh_decomposition_and_allowed_dimensions(self):
        self.assertEqual(
            self.zero["dimensions"],
            {
                "ambient": 3888,
                "constant": 32,
                "singleton_total": 208,
                "allowed_subspace": 240,
                "actual_native_curve_span_claimed": False,
            },
        )
        self.assertEqual(self.positive["dimensions"]["allowed_subspace"], 80)
        for row in (self.zero, self.positive):
            self.assertTrue(row["complete_higher_Walsh_residual_zero"])
            self.assertFalse(
                row["singletons_claimed_orthogonal_in_scalar_Mellin_measure"]
            )

    def test_all_local_swaps_are_commuting_involutions_on_complete_factor_space(self):
        exponents = (1, 2, 4)
        vector = tuple(Fraction(i * i - 7) for i in range(30))
        for j in range(3):
            self.assertEqual(
                M.reflect(M.reflect(vector, exponents, j), exponents, j), vector
            )
            for k in range(3):
                self.assertEqual(
                    M.reflect(M.reflect(vector, exponents, j), exponents, k),
                    M.reflect(M.reflect(vector, exponents, k), exponents, j),
                )

    def test_higher_even_sector_defeats_global_exchange_identification_for_general_source(
        self,
    ):
        exponents = (1, 1)
        vector = tuple(Fraction((-1) ** sum(a)) for a in product((0, 1), repeat=2))
        self.assertEqual(tuple(reversed(vector)), vector)
        self.assertEqual(M.character_projection(vector, exponents), (0, 0, 0, 0))
        self.assertEqual(M.character_projection(vector, exponents, (0, 1)), vector)

    def test_actual_Boolean_half_source_has_full_character_and_original_Beta_weight(
        self,
    ):
        odd = M.boolean_control((71, 73, 79))
        even = M.boolean_control((71, 73, 79, 83))
        self.assertEqual(odd["nonzero_core_allocations_per_owner_order"], 0)
        self.assertEqual(odd["canonical_two_owner_coefficient"], "0")
        self.assertEqual(even["nonzero_core_allocations_per_owner_order"], 8)
        self.assertTrue(even["highest_character_nonzero"])
        self.assertTrue(even["global_exchange_even"])
        self.assertEqual(even["actual_Beta_integral"], "1/30")
        self.assertEqual(even["canonical_two_owner_coefficient"], "2/15")
        self.assertEqual(even["nonzero_literal_term_after_Beta"], ["1/120"])
        self.assertFalse(even["measure_is_2d_tau"])

    def test_actual_zero_chart_ratio_mask_has_nonzero_source_commutator(self):
        row = self.zero["actual_ratio_mask"]
        self.assertEqual(row["orbit_size"], 512)
        self.assertGreater(row["retained_count"], 0)
        self.assertLess(row["retained_count"], 512)
        self.assertGreater(
            Fraction(row["mask_commutator_counting_norm_square_times_K"]), 0
        )
        self.assertFalse(row["mask_commutes_with_augmentation_on_actual_source"])
        self.assertTrue(row["mask_after_augmentation_equals_global_even_masked_source"])

    def test_native_physical_move_reselects_metric_and_leaves_ratio_mask(self):
        row = self.zero["actual_ratio_mask"]
        self.assertEqual(row["selected_N"], row["moved_N"] * 71**2)
        self.assertEqual(row["moved_M"], row["selected_M"] * 71**2)
        self.assertGreater(8 * row["selected_N"], row["selected_M"])
        self.assertLess(8 * row["moved_N"], row["moved_M"])
        self.assertNotEqual(row["old_principal_weight"], row["new_principal_weight"])

    def test_power_schedule_activation_weights_and_source_endpoint(self):
        for powers in ((1, 1, 1), (1, 2, 3), (2, 3, 5)):
            row = M.activation_control(powers)
            self.assertEqual(
                [Fraction(v) for v in row["activation_probabilities"]],
                [Fraction(a, sum(powers)) for a in powers],
            )
            self.assertEqual(sum(Fraction(v) for v in row["complete_coefficients"]), -1)
            self.assertFalse(row["primitive_measure_is_probability"])

    def test_separated_actual_kernel_fixture_and_unique_activation_minimum(self):
        row = M.separated_control()
        self.assertEqual(row["complete_divisors"], [1, 3, 11, 33, 101, 303, 1111, 3333])
        self.assertEqual(row["minimum_energy_times_K_over_Gamma0"], "1/6")
        equal = M.activation_control((1, 1, 1))
        unequal = M.activation_control((1, 2, 3))
        self.assertLess(
            Fraction(equal["energy_times_K_over_Gamma0_in_separated_case"]),
            Fraction(unequal["energy_times_K_over_Gamma0_in_separated_case"]),
        )
        self.assertFalse(row["unique_minimizing_path_claimed"])

    def test_higher_sector_characters_and_typed_resource_guards(self):
        for exponents in ((True,), (1.0,), (5,), (4,) * 9):
            with self.subTest(exponents=exponents), self.assertRaises(ValueError):
                M.allowed_dimensions(exponents)
        with self.assertRaises(ValueError):
            M.character_projection((1, 2), (1,), (0, 0))
        with self.assertRaises(ValueError):
            M.reflect((1.0, 2.0), (1,), 0)
        with self.assertRaises(ValueError):
            M.activation_control((1, True))

    def test_exact_executable_source_authentication_rejects_wrong_blob(self):
        with (
            patch.object(M, "GE_BLOB", "0" * 40),
            self.assertRaisesRegex(ValueError, "authentication"),
        ):
            M.geodesic_module()

    def test_typed_json_acceptance_rejects_float_and_boolean_counterfeits(self):
        for bad in (1.0, True):
            with (
                self.subTest(bad=bad),
                self.assertRaisesRegex(ValueError, "typed canonical"),
            ):
                M.replay_equal({"count": bad}, {"count": 1})


if __name__ == "__main__":
    unittest.main()
