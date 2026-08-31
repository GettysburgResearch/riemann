"""Authentic primitive tuples, colour measure and exact coinvariant controls."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "native-six-hour"
    / "flat_gauge_native_tuples.py"
)
SPEC = importlib.util.spec_from_file_location("native_six_hour_flat_gauge", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeFlatGaugeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zero = M.tuple_spec(
            "zero_boolean", 64, (2, 3), (5, 7), (71, 73, 79), (401, 421)
        )
        cls.native = json.loads(M.source_bytes((M.DENSE, M.DENSE_JSON)))
        cls.positive = M.dense_spec(cls.native)

    def test_all_native_local_convolution_coefficients_through_degree_eight(self):
        for degree in range(9):
            with self.subTest(degree=degree):
                row = M.local_product_control(degree)
                self.assertEqual(row["complete_allocation_count"], degree + 1)
                self.assertEqual(
                    row["product_coefficient"],
                    (1, -1, -1, 1)[degree] if degree < 4 else 0,
                )

    def test_flat_generator_unit_and_complete_multiplier_controls(self):
        for degree in range(1, 7):
            with self.subTest(degree=degree):
                row = M.coinvariant_control(degree)
                self.assertTrue(row["L_equals_difference_times_unit"])
                self.assertTrue(row["finite_inverse_verified"])
                self.assertEqual(
                    row["ambient_basis_count"] - row["difference_ideal_basis_count"],
                    row["quotient_basis_count"],
                )
                self.assertFalse(
                    row["physical_ratio_readout_is_truncated_ring_homomorphism"]
                )

    def test_all_twenty_four_boolean_histories_and_original_shares(self):
        left, right = self.zero["left_boolean"], self.zero["right_boolean"]
        self.assertEqual(len(left["nonzero_histories"]), 12)
        self.assertEqual(len(right["nonzero_histories"]), 2)
        pairs = [
            Fraction(a["coefficient"] * b["coefficient"], 60)
            for a in left["nonzero_histories"]
            for b in right["nonzero_histories"]
        ]
        self.assertEqual(pairs.count(Fraction(1, 60)), 12)
        self.assertEqual(pairs.count(Fraction(-1, 60)), 12)
        self.assertEqual(sum(pairs), 0)
        self.assertEqual(self.zero["canonical_stripped_coefficient"], "0")

    def test_zero_chart_temperature_and_positive_held_out_values(self):
        zero = M.raw_temperature_polynomial(self.zero)
        positive = M.raw_temperature_polynomial(self.positive)
        self.assertEqual(M.evaluate(zero, Fraction(1, 2)), Fraction(-3125, 524288))
        self.assertEqual(M.evaluate(positive, Fraction(1, 2)), Fraction(625, 65536))
        self.assertEqual(self.positive["canonical_stripped_coefficient"], "1/9")
        for value in (zero, positive):
            self.assertEqual(M.evaluate(value, 0), 0)
            self.assertEqual(M.evaluate(value, 1), 0)

    def test_native_probability_colour_mean_is_not_counting_diagonal(self):
        row = M.endpoint_colours(self.zero)
        self.assertEqual(row["complete_colour_count"], 512)
        self.assertEqual(len(row["nonzero_colour_coefficients"]), 1)
        self.assertEqual(row["mean_stripped_coefficient"], "-1/512")
        self.assertEqual(row["native_probability_diagonal_stripped"], "1/512")
        self.assertEqual(row["regrouped_mean_diagonal_stripped"], "1/262144")
        self.assertEqual(row["walsh_nonzero_count"], 512)
        self.assertEqual(
            {abs(Fraction(v)) for v in row["complete_walsh_coefficients"]},
            {Fraction(1, 512)},
        )

    def test_shared_prime_has_no_endpoint_tuple_but_complete_contraction_cancels(self):
        row = M.endpoint_colours(self.positive)
        self.assertEqual(row["complete_colour_count"], 128)
        self.assertEqual(row["walsh_nonzero_count"], 0)
        self.assertEqual(row["mean_stripped_coefficient"], "0")
        fourth = M.local_product_control(4)
        self.assertEqual(
            [Fraction(v) for v in fourth["midpoint_allocations"]],
            [
                Fraction(-13, 128),
                Fraction(-3, 32),
                Fraction(25, 64),
                Fraction(-3, 32),
                Fraction(-13, 128),
            ],
        )
        self.assertEqual(fourth["product_coefficient"], 0)

    def test_original_measure_observed_energy_retains_the_true_allocation_diagonal(
        self,
    ):
        first, fourth = M.local_product_control(1), M.local_product_control(4)
        self.assertEqual(first["midpoint_ratio_energy_over_Gamma0_p_minus_n"], "1/2")
        self.assertEqual(
            fourth["midpoint_ratio_energy_over_Gamma0_p_minus_n"], "1563/8192"
        )
        control = M.tuple_control(self.zero)
        midpoint = control["temperature_panels"][2]
        scalar = Fraction(midpoint["raw_stripped_coefficient"])
        self.assertEqual(
            Fraction(midpoint["physical_coefficient_square"]),
            scalar * scalar / (self.zero["N"] * self.zero["M"]),
        )

    def test_frozen_dense_indices_and_numeric_types_are_not_forged(self):
        for value in (self.native["record"]["entries"][0]["N"] + 1, True, 1.0):
            bad = copy.deepcopy(self.native)
            bad["record"]["entries"][0]["N"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.dense_spec(bad)
        for value in (True, -1, 9, 1.0):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.half_coefficient(value)

    def test_caps_source_blob_authentication_and_typed_replay(self):
        with self.assertRaises(ValueError):
            M.boolean_histories((3, 3), 2)
        with self.assertRaises(ValueError):
            M.walsh([1, 2, 3])
        with self.assertRaises(ValueError):
            M.evaluate(M.poly([1, 1]), 0.5)
        key = (M.DENSE, M.DENSE_JSON)
        with patch.dict(M.SOURCES, {key: "0" * 40}), self.assertRaises(ValueError):
            M.source_bytes(key)
        for value in (True, 1.0):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.replay_equal({"count": value}, {"count": 1})

    def test_build_authenticates_primitives_and_preserves_missing_target_interface(
        self,
    ):
        result = M.build()
        self.assertEqual(len(result["sources"]), 10)
        self.assertFalse(result["complete_post_renewal_gamma_identification"])
        self.assertFalse(result["native_principal_moment_counterexample"])
        self.assertFalse(result["all_integrated_scalar_functionals_excluded"])
        self.assertFalse(result["native_temperature_probability_measure_invented"])
        self.assertTrue(result["original_Mellin_measure_retained"])
        self.assertEqual(len(result["complete_local_source_products"]), 9)


if __name__ == "__main__":
    unittest.main()
