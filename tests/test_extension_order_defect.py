"""Actual invariant bases, cokernel Frobenius and distinct Euler constructions."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/l-families/atlas/generalized/extension-order-defect/replay.py"
SPEC = importlib.util.spec_from_file_location("extension_order_defect", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class PrimitiveInvariantSourceTests(unittest.TestCase):
    def test_literal_fourier_vectors_are_actual_sum_zero_eigenvectors(self):
        source = M.primitive_fourier_source()
        self.assertTrue(source["literal_cycle_and_reflection_checked"])
        self.assertNotEqual(source["nonzero_standard_minor"], (0, 0))

    def test_c2_comparison_is_an_explicit_injection_not_dimension_subtraction(self):
        for degree in range(9):
            row = M.primitive_c2(degree)
            self.assertTrue(
                row["injection_certified_by_disjoint_orbit_coordinate_supports"]
            )
            self.assertEqual(
                row["after_dimension"],
                sum(c["after_independent_columns"] for c in row["components"]),
            )

    def test_old_c2_degree_three_has_the_actual_23_26_defect(self):
        row = M.primitive_c2(3)
        self.assertEqual(
            [
                row["after_dimension"],
                row["before_dimension"],
                row["cokernel_dimension"],
            ],
            [23, 26, 3],
        )

    def test_degree_four_contains_both_crossed_and_even_generator_defects(self):
        row = M.primitive_c2(4)
        self.assertEqual(row["cokernel_dimension"], 9)
        self.assertEqual(
            [
                c["before_orbit_basis_size"] - c["after_independent_columns"]
                for c in row["components"]
            ],
            [0, 8, 1],
        )

    def test_no_old_defect_before_degree_three(self):
        self.assertEqual(
            [M.primitive_c2(n)["cokernel_dimension"] for n in range(3)], [0, 0, 0]
        )

    def test_infinity_uses_a_literal_invariant_subquotient(self):
        row = M.primitive_infinity(4)
        self.assertEqual([row["after_dimension"], row["before_dimension"]], [25, 38])
        self.assertTrue(row["after_basis_is_literal_k_zero_subset"])

    def test_nonsplit_infinity_trace_one_does_not_mean_dimension_one(self):
        row = M.primitive_infinity(4)
        self.assertEqual(row["cokernel_dimension"], 13)
        self.assertEqual(row["cokernel_residual_trace"], 1)
        self.assertEqual(row["cokernel_residual_plus_minus_multiplicities"], [7, 6])

    def test_quadratic_infinity_inertia_kills_every_odd_grade(self):
        for n in (1, 3, 5, 7):
            self.assertEqual(M.primitive_infinity(n)["before_dimension"], 0)

    def test_new_zero_has_no_defect_in_all_primitive_grades(self):
        for n in range(9):
            row = M.primitive_zero(n)
            self.assertTrue(row["after_equals_before_on_the_same_basis"])
            self.assertEqual(row["cokernel_dimension"], 0)

    def test_s4_holdout_exposes_a_new_crossed_source_dimension(self):
        row = M.primitive_c2(3, 4)
        self.assertEqual(
            [
                row["after_dimension"],
                row["before_dimension"],
                row["cokernel_dimension"],
            ],
            [120, 125, 5],
        )

    def test_primitive_caps_and_boolean_substitutions_fail_closed(self):
        for grade in (True, 1.0, -1, 9):
            with self.subTest(grade=grade), self.assertRaises(ValueError):
                M.primitive_c2(grade)
        with self.assertRaises(ValueError):
            M.primitive_c2(4, 4)


class AllGradeAndScalarShadowTests(unittest.TestCase):
    def test_all_primitive_dimensions_and_residual_traces_match_rational_source(self):
        self.assertEqual(M.primitive_comparison()["primitive_max_grade"], 8)

    def test_closed_numerators_match_frozen_source_molien_in_every_declared_grade(self):
        self.assertEqual(len(M.all_grade_rational_controls()), 4)

    def test_old_c2_additive_defect_has_the_simplified_positive_numerator(self):
        cut = 24
        denominator = M.mul(
            M.mul(M.power([1, -1], 6, cut), M.power([1, 1], 3, cut), cut),
            [1, 0, 1],
            cut,
        )
        expected = M.divide([0, 0, 0, 3, 0, 2, 1], denominator, cut)
        self.assertEqual(M.rational_local("old", "difference", cut), expected)

    def test_nonsplit_infinity_ratio_is_a_different_function_from_its_cokernel_series(
        self,
    ):
        ratio = M.rational_local("infinity_nonsplit", "ratio", 16)
        self.assertEqual(ratio, M.substitute(M.power([1, -1], -1, 16), 4, 1, 16))

    def test_first_old_scalar_shadow_mismatch_is_degree_four_not_three(self):
        for epsilon in (-1, 1):
            row = M.scalar_shadow_control("old", epsilon)
            self.assertEqual(row["first_difference_grade"], 4)
            self.assertEqual(row["Hilbert_ratio"][3:5], [3 * epsilon, 0])
            self.assertEqual(row["ordinary_graded_determinant"][3:5], [3 * epsilon, 9])

    def test_split_infinity_nonlinear_ratio_can_have_negative_coefficients(self):
        row = M.scalar_shadow_control("infinity_split")
        self.assertEqual(row["Hilbert_ratio"][4:7:2], [13, -8])
        self.assertEqual(row["ordinary_graded_determinant"][4:7:2], [13, 70])

    def test_nonsplit_ordinary_determinant_preserves_seven_plus_and_six_minus(self):
        row = M.ordinary_cokernel_graded("infinity_nonsplit", 8)
        grade_four = next(
            r for r in row["finite_grade_eigenmultiplicities"] if r["grade"] == 4
        )
        self.assertEqual(grade_four["Frobenius_plus_minus"], [7, 6])

    def test_bad_strata_and_float_signs_are_rejected(self):
        with self.assertRaises(ValueError):
            M.rational_local("zero", "difference")
        with self.assertRaises(ValueError):
            M.rational_local("old", "ratio", epsilon=1.0)

    def test_cached_composition_input_validation_precedes_cache_lookup(self):
        M.compositions(2, 2)
        with self.assertRaises(ValueError):
            M.compositions(2.0, 2)


class ActualGlobalAndAuthenticationTests(unittest.TestCase):
    def test_actual_full_boundary_products_reproduce_the_finite_rational_correction(
        self,
    ):
        for index in range(3):
            row = M.global_boundary_control(index)
            self.assertEqual(
                row["before_bad_product"],
                M.mul(
                    row["after_bad_product"], row["rational_boundary_Hilbert_ratio"], 16
                ),
            )

    def test_actual_closed_branch_degree_and_residue_sign_are_retained(self):
        for index in range(3):
            row = M.global_boundary_control(index)
            self.assertEqual(
                sum(v["degree"] * v["count"] for v in row["actual_closed_branch_rows"]),
                4,
            )
            self.assertTrue(row["no_degree_four_field_enumerated"])

    def test_global_ratio_is_distinguished_without_fitting_a_first_coefficient(self):
        for index in range(3):
            row = M.global_boundary_control(index)
            self.assertGreater(row["rational_ratio_pole_order_at_one"], 0)
            self.assertEqual(
                row["rational_boundary_Hilbert_ratio"][4],
                13 if row["parameters"][0] % 3 == 1 else 1,
            )

    def test_actual_global_cokernel_determinant_is_not_the_hilbert_ratio(self):
        for index in range(3):
            row = M.global_boundary_control(index)
            self.assertNotEqual(
                row["rational_boundary_Hilbert_ratio"],
                row["ordinary_graded_boundary_determinant"],
            )

    def test_new_numerator_reciprocals_have_only_unit_or_three_prime_support(self):
        row = M.arithmetic_nonvanishing_controls()
        self.assertEqual(row["old_C2_reciprocal_low_to_high"], [1, 1, 3, 0, 1])
        self.assertEqual(
            row["split_infinity_reciprocal_low_to_high"], [3, 10, 22, 14, 20, 2, 1]
        )

    def test_primitive_payload_rejects_a_bool_in_place_of_an_integer(self):
        candidate = M.build_payload()
        candidate["primitive_invariant_comparison"]["old_C2"][0]["before_dimension"] = (
            True
        )
        with self.assertRaises(ValueError):
            M.check_payload(candidate)

    def test_payload_rejects_the_false_single_dimension_nonsplit_stalk(self):
        candidate = copy.deepcopy(M.build_payload())
        candidate["primitive_invariant_comparison"]["infinity_with_residual_Frobenius"][
            4
        ]["cokernel_dimension"] = 1
        with self.assertRaises(ValueError):
            M.check_payload(candidate)

    def test_source_authentication_fails_before_any_replay(self):
        with (
            patch.object(M.subprocess, "check_output", return_value="wrong\n"),
            self.assertRaises(ValueError),
        ):
            M.authenticate_frozen()


if __name__ == "__main__":
    unittest.main()
