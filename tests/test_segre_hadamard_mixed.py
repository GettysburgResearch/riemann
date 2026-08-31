"""Mixed-rank canonical leading characters and a degree jump without collision."""

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "research/l-families/atlas/generalized/segre-hadamard-source"
SPEC = importlib.util.spec_from_file_location(
    "segre_hadamard_mixed", HERE / "mixed_replay.py"
)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class MixedCanonicalControls(unittest.TestCase):
    def test_first_geometry_and_actual_leading_character(self):
        row = R.grouped_numerator([((2, 3), 2), ((5, 7, 11), 1)])
        self.assertEqual(row["s_D_c_M_generic_degree"], [9, 5, 4, 3, 6])
        self.assertEqual(row["canonical_leading_character"], 6**5 * 385**2 * 25)
        self.assertEqual(row["fixed_top_tor_dimension_at_identity"], 4)

    def test_reversed_multiplicity_heldout(self):
        row = R.grouped_numerator([((2, 3), 1), ((5, 7, 11), 2)])
        self.assertEqual(row["s_D_c_M_generic_degree"], [12, 6, 6, 3, 9])
        self.assertEqual(row["canonical_leading_character"], 6**4 * 385**6 * 5)
        self.assertEqual(row["fixed_top_tor_dimension_at_identity"], 2)

    def test_grouped_base_is_not_full_ambient_base(self):
        row = R.grouped_numerator([((2, 3), 2), ((5, 7, 11), 1)])
        self.assertEqual(len(row["denominator"]) - 1, 9)
        self.assertEqual(row["numerator"][1], 6 * (5 + 7 + 11))

    def test_identity_top_character_is_dimension_not_scalar_fit(self):
        row = R.grouped_numerator([((1, 1), 2), ((1, 1, 1), 1)])
        self.assertEqual(row["canonical_leading_character"], 4)
        self.assertFalse(row["distinct_generator_weights"])

    def test_trace_zero_does_not_remove_top_tor_space(self):
        row = R.grouped_numerator([((1, -1), 2), ((5, 7, 11), 1)])
        self.assertEqual(row["canonical_leading_character"], 0)
        self.assertEqual(row["fixed_top_tor_dimension_at_identity"], 4)
        self.assertEqual(row["actual_numerator_degree"], 5)

    def test_trace_zero_complete_source_formula(self):
        b = (Fraction(5), Fraction(7), Fraction(11))
        row = R.grouped_numerator([((1, -1), 2), (b, 1)])
        expected = R.trim(
            R.multiply(R.determinant_poly(b), [1, 0, R.elementary(b)[2]], 9)
        )
        self.assertEqual(row["numerator"], expected)

    def test_heldout_trace_zero_is_even(self):
        row = R.grouped_numerator([((1, -1), 1), ((5, 7, 11), 2)])
        self.assertLessEqual(row["actual_numerator_degree"], 8)
        self.assertTrue(
            all(value == 0 for i, value in enumerate(row["numerator"]) if i % 2)
        )

    def test_equal_rank_recovers_monomial_top_character(self):
        row = R.grouped_numerator([((2, 3), 1), ((5, 7), 1)])
        self.assertEqual(row["s_D_c_M_generic_degree"], [4, 3, 1, 2, 2])
        self.assertEqual(row["canonical_leading_character"], -6 * 35)
        self.assertEqual(row["fixed_top_tor_dimension_at_identity"], 1)

    def test_full_ternary_binary_segre_comparison(self):
        row = R.grouped_numerator([((2, 3), 1), ((5, 7, 11), 1)])
        self.assertEqual(row["s_D_c_M_generic_degree"], [6, 4, 2, 3, 3])
        self.assertEqual(row["canonical_leading_character"], 6 * 385 * 5)

    def test_zero_nonrational_and_oversized_inputs_are_refused(self):
        bad = (
            [((0, 1), 1)],
            [((1.0, 2), 1)],
            [((1, 2), True)],
            [((1, 2, 3, 4), 4)],
            [((1,), 1)],
        )
        for groups in bad:
            with self.assertRaises(ValueError):
                R.grouped_numerator(groups)


class PoleAndDegreeControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = R.collision_free_degree_drop()

    def test_actual_companion_recurrence_has_h2_zero(self):
        self.assertEqual(self.result["source_h_A"][:7], [1, 1, 0, -1, -1, 0, 1])

    def test_degree_deficit_jumps_without_common_factor(self):
        self.assertEqual(self.result["generic_vs_actual_degree_deficit"], [4, 5])
        self.assertEqual(self.result["gcd_N_Q"], [1])
        self.assertEqual(len(self.result["denominator"]) - 1, 8)

    def test_all_eight_poles_remain_distinct(self):
        self.assertEqual(self.result["gcd_Q_derivative"], [1])
        self.assertTrue(self.result["all_eight_poles_distinct_and_retained"])

    def test_exact_cubic_numerator_from_source(self):
        e = R.elementary((5, 7, 11, 13))
        self.assertEqual(self.result["numerator"], [1, 0, -e[2], e[3]])

    def test_second_positive_panel_not_same_numeric_fixture(self):
        row = R.collision_free_degree_drop((1, 2, 3, 4))
        self.assertEqual(row["numerator"], [1, 0, -35, 50])
        self.assertEqual(row["gcd_N_Q"], [1])

    def test_distinct_positive_hypothesis_is_enforced(self):
        for values in ((1, 1, 2, 3), (-1, 1, 2, 3), (0, 1, 2, 3)):
            with self.assertRaises(ValueError):
                R.collision_free_degree_drop(values)

    def test_exact_gcd_catches_deliberate_common_factor(self):
        common = [Fraction(1), Fraction(-2)]
        left = R.multiply(common, [1, 3], 2)
        right = R.multiply(common, [1, 0, 1], 3)
        self.assertEqual(R.polynomial_gcd(left, right), [Fraction(-1, 2), 1])

    def test_full_small_build_checks_preregistered_deformations(self):
        result = R.build()
        self.assertEqual(len(result["deformation"]), 6)
        self.assertFalse(result["scalar_degree_loss_implies_betti_jump"])
        self.assertFalse(result["full_resolution_computed"])

    def test_checker_rejects_boolean_alias_with_original_proof_digest(self):
        record = R.payload()
        record["result"]["generic_comparison"]["denominator"][0] = True
        with self.assertRaises(ValueError):
            R.check_payload(record)

    def test_checker_rejects_float_alias_with_original_proof_digest(self):
        record = R.payload()
        record["result"]["generic_comparison"]["denominator"][0] = 1.0
        with self.assertRaises(ValueError):
            R.check_payload(record)

    def test_checker_rejects_scalar_change_with_original_proof_digest(self):
        record = R.payload()
        record["result"]["generic_comparison"]["denominator"][0] = 2
        with self.assertRaises(ValueError):
            R.check_payload(record)


if __name__ == "__main__":
    unittest.main()
