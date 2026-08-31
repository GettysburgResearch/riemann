"""Actual source-site reconstruction and its noninterchangeable measures."""

import copy
import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "native-six-hour"
    / "canonical_native_preimage.py"
)
SPEC = importlib.util.spec_from_file_location(
    "native_six_hour_canonical_preimage", PATH
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeCanonicalPreimageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = M.geodesic_module()
        cls.left = M.side(cls.module, (2, 3), (71, 73, 79), 64)
        cls.right = M.side(cls.module, (5, 7), (401, 421), 64)
        cls.zero = M.bilateral(cls.left, cls.right)

    def test_original_cutoff_convention_and_nontrivial_cutoff(self):
        self.assertEqual(M.a_u((), 64), 0)
        self.assertEqual(M.a_u((71, 73), 64), -1)
        self.assertEqual(M.a_u((2, 3), 64), 0)
        self.assertEqual(M.a_u((2, 3), 2), 0)
        self.assertEqual(M.a_u((2, 3), 3), 1)

    def test_all_squarefree_primitive_factors_and_sites(self):
        for labels, factors, sites, value in [
            ((2, 3), 4, 4, "1"),
            ((2, 3, 71), 8, 12, "-1"),
        ]:
            cone = M.raw_cone(self.module, labels)
            self.assertEqual(cone["complete_factor_count"], factors)
            self.assertEqual(len(cone["sites"]), sites)
            self.assertEqual(cone["coefficient"], value)
            self.assertTrue(cone["root_free_left_retained"])

    def test_actual_colour_probability_is_not_counting_weight_square(self):
        cone = M.raw_cone(self.module, (2, 3, 71))
        colours = cone["endpoint_colours"]
        self.assertEqual(sum(Fraction(x["probability"]) for x in colours), 1)
        self.assertEqual(
            sum(Fraction(x["probability"]) * x["coefficient"] for x in colours), -1
        )
        self.assertEqual(cone["colour_probability_diagonal"], "1")
        self.assertEqual(cone["colour_weighted_counting_diagonal"], "1/8")

    def test_all_twenty_four_histories_and_nested_3072_sites(self):
        self.assertEqual(self.left["complete_Boolean_partition_count"], 27)
        self.assertEqual(self.left["zero_history_count"], 15)
        self.assertEqual(self.right["complete_Boolean_partition_count"], 9)
        self.assertEqual(self.right["zero_history_count"], 7)
        self.assertEqual(self.zero["history_count"], 24)
        self.assertEqual(self.zero["nested_site_count"], 3072)
        self.assertEqual(
            self.zero["nested_coefficient_histogram"], {"-1/11520": 2304, "1/3840": 768}
        )
        self.assertEqual(self.zero["coefficient_before_1_over_sqrt_NM"], "0")

    def test_owner_extraction_before_completion_has_correct_physical_weight(self):
        self.assertEqual(self.left["N"], 1005930209094)
        self.assertEqual(self.right["N"], 997518551435)
        for row in self.left["histories"]:
            self.assertEqual(
                Fraction(row["completion_multiplier_square"]) / row["raw_product"],
                Fraction(1, self.left["N"]),
            )
            self.assertNotEqual(row["raw_product"], self.left["N"])

    def test_independent_half_source_convolution_cancels_odd_core(self):
        self.assertEqual(M.half_square((71, 73, 79), 64), 0)
        self.assertEqual(M.half_square((401, 421), 64), 2)
        self.assertEqual(M.half_source((71, 73, 79), 64), Fraction(-1, 4))
        self.assertEqual(M.half_source((71, 73), 64), 0)

    def test_continuous_integrated_and_history_diagonals_are_distinct(self):
        self.assertEqual(
            self.zero["diagonals_before_1_over_NM"],
            {
                "continuous": "29/25200",
                "integrated_site": "1/14400",
                "history": "1/150",
                "recombined": "0",
            },
        )
        self.assertEqual(self.left["beta_per_owner_order"], "1/20")
        self.assertEqual(self.right["beta_per_owner_order"], "1/12")

    def test_same_map_positive_rough_two_prime_cores(self):
        a = M.side(self.module, (2, 3), (71, 73), 64)
        b = M.side(self.module, (5, 7), (79, 83), 64)
        pair = M.bilateral(a, b)
        self.assertEqual(pair["coefficient_before_1_over_sqrt_NM"], "1/9")
        self.assertEqual(pair["nested_site_count"], 256)
        self.assertEqual(
            pair["diagonals_before_1_over_NM"],
            {
                "continuous": "1/2025",
                "integrated_site": "1/20736",
                "history": "1/324",
                "recombined": "1/81",
            },
        )

    def test_exact_bounds_and_clean_labels(self):
        for bad in (True, 64.0, 0, 2**25):
            with self.assertRaises(ValueError):
                M.a_u((71,), bad)
        for owners, core in [((2, 2), (71,)), ((2, 3), (3, 71)), ((2, 3), (9,))]:
            with self.assertRaises(ValueError):
                M.side(self.module, owners, core, 64)

    def test_typed_fixture_and_frozen_source_authentication(self):
        changed = copy.deepcopy(self.zero)
        changed["history_count"] = 24.0
        with self.assertRaises(ValueError):
            M.replay_equal(changed, self.zero)
        with patch.object(M, "GE_BLOB", "0" * 40), self.assertRaises(ValueError):
            M.geodesic_module()


if __name__ == "__main__":
    unittest.main()
