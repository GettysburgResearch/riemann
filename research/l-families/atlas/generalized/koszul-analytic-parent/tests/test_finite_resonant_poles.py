"""Actual source threshold, complete sign cases and distinct coefficient operations."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "finite_resonant_poles", HERE / "finite_resonant_poles_replay.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ActualAdamsSourceTests(unittest.TestCase):
    def test_squarefree_mobius_and_square_divisibility_are_exact(self):
        self.assertEqual(
            [M.mobius(n) for n in (1, 2, 4, 6, 12, 30, 49)], [1, -1, 0, 1, 0, -1, 0]
        )

    def test_source_group_powers_are_not_replaced_by_the_same_class(self):
        self.assertEqual(M.powered_class("s", 2), "e")
        self.assertEqual(M.powered_class("c", 3), "e")
        self.assertEqual(M.powered_class("c", 2), "c")

    def test_constant_four_cancellation_is_not_incorrectly_applied_at_grade_one(self):
        row = M.adams_source_row(1)
        self.assertEqual(row["actual_characters"], [6, 0, 0])
        self.assertEqual(row["multiplicities"], [1, 1, 2])

    def test_actual_low_relation_source_is_retained(self):
        self.assertEqual(M.adams_source_row(2)["actual_characters"], [3, 1, 0])
        self.assertEqual(M.adams_source_row(4)["multiplicities"], [0, 1, 1])
        self.assertEqual(M.adams_source_row(8)["multiplicities"], [4, 6, 10])

    def test_exact_elliptic_total_uses_dimension_minus_transposition_trace(self):
        for n in range(2, 17):
            row = M.adams_source_row(n)
            _, b, c = row["multiplicities"]
            self.assertEqual(row["exact_twice_B_plus_C"], 2 * (b + c))

    def test_source_caps_and_types_fail_closed(self):
        for n in (True, 1.0, 0, 65):
            with self.subTest(n=n), self.assertRaises((TypeError, ValueError)):
                M.adams_source_row(n)


class UniformThresholdTests(unittest.TestCase):
    def test_uniform_proof_starts_at_explicit_positive_margin_1228(self):
        self.assertEqual(M.uniform_bound_control(6)["sufficient_integer_margin"], 1228)

    def test_bounded_actual_characters_lie_between_the_proved_uniform_bounds(self):
        from fractions import Fraction

        for n in (6, 8, 10, 12, 16, 24, 32):
            row = M.uniform_bound_control(n)
            lower = Fraction(*row["A_double_grade_lower"])
            upper = Fraction(*row["twice_B_plus_C_upper"])
            self.assertGreater(lower, upper)
            self.assertGreaterEqual(row["actual_A_double_grade"], lower)
            self.assertLessEqual(row["actual_twice_B_plus_C"], upper)

    def test_normalized_sufficient_bound_decreases_at_the_start(self):
        from fractions import Fraction

        row = M.uniform_bound_control(6)
        self.assertLess(
            Fraction(*row["next_even_normalized_RHS"]),
            Fraction(*row["normalized_sufficient_RHS"]),
        )
        self.assertLess(Fraction(*row["normalized_sufficient_RHS"]), 64)

    def test_strict_source_margin_gives_zeros_not_just_removed_poles(self):
        for n in (6, 8, 10, 12, 16):
            row = M.uniform_bound_control(n)
            self.assertGreater(row["actual_strict_order_margin"], 0)

    def test_low_or_wrong_parity_grade_is_not_certified_by_the_uniform_tail_bound(self):
        with self.assertRaises(ValueError):
            M.uniform_bound_control(4)
        with self.assertRaises(ValueError):
            M.uniform_bound_control(7)


class CompleteLowPoleTests(unittest.TestCase):
    def test_both_elliptic_sign_cases_have_exactly_two_double_poles(self):
        result = M.low_grade_sign_cases()
        self.assertEqual(result["total_interior_poles"], 2)
        self.assertEqual(result["order_of_each_pole"], 2)
        for row in result["sign_cases"]:
            self.assertEqual(row["grade_two_E_point"]["pole_order"], 2)

    def test_equal_sign_grade_four_is_regular_at_the_former_pole(self):
        row = M.low_grade_sign_cases()["sign_cases"][0]
        self.assertTrue(row["elliptic_signs_agree"])
        self.assertEqual(row["grade_four_E_point"]["signed_order"], 0)

    def test_opposite_sign_grade_four_has_true_zeros_in_both_eigenvalue_sets(self):
        row = M.low_grade_sign_cases()["sign_cases"][1]
        self.assertFalse(row["elliptic_signs_agree"])
        self.assertEqual(row["grade_four_E_point"]["zero_order"], 2)
        self.assertEqual(row["grade_four_D_point"]["zero_order"], 2)

    def test_actual_negative_resonant_eigenvalue_keeps_positive_recurrence_coefficients(
        self,
    ):
        result = M.actual_clearing_factor()
        self.assertEqual(result["actual_alpha_E"], -7)
        self.assertEqual(
            result["minimal_normalized_pole_clearing_polynomial"], [1, 0, 14, 0, 49]
        )
        self.assertFalse(result["new_field_enumerated"])


class DistinctCoefficientOperationsTests(unittest.TestCase):
    def test_two_double_principal_parts_have_the_exact_rational_coefficients(self):
        result = M.principal_part_calibration()
        self.assertEqual(result["principal_coefficients"][:4], [4, 30, 300, 750])
        self.assertEqual(result["cleared_principal_polynomial"], [4, 30, 100, -750])

    def test_opposite_poles_can_cancel_the_linear_growth_on_one_parity(self):
        coefficients = M.principal_part_calibration()["principal_coefficients"]
        for n, value in enumerate(coefficients):
            self.assertEqual(value, 4 * (n + 1) * 5**n if n % 2 == 0 else 6 * 5**n)

    def test_new_integral_cleared_sequence_is_not_the_old_exponential_sequence(self):
        result = M.principal_part_calibration()
        old = result["integer_tail_added_coefficients"]
        new = result["new_pole_cleared_integer_coefficients"]
        self.assertNotEqual(old, new)
        self.assertTrue(all(value == 576 for value in new[4:]))
        self.assertTrue(all(type(value) is int for value in new))

    def test_algebraic_calibration_does_not_claim_actual_complex_residues(self):
        result = M.principal_part_calibration()
        self.assertTrue(result["calibration_not_actual_source_residues"])
        self.assertTrue(result["source_complex_residues_not_computed"])
        self.assertTrue(
            result["calibration_tail_is_not_claimed_to_have_a_full_natural_boundary"]
        )

    def test_integer_recurrence_keeps_negative_index_terms_zero(self):
        self.assertEqual(
            M.pole_clearing_coefficients([1, 2, 3, 4, 5], -7), [1, 2, 17, 32, 96]
        )
        with self.assertRaises(ValueError):
            M.pole_clearing_coefficients([True], -7)


class AuthenticationTests(unittest.TestCase):
    def test_exact_frozen_divisor_source_is_authenticated(self):
        M.authenticate_frozen()

    def test_forged_fixture_does_not_substitute_for_full_replay(self):
        with self.assertRaises(ValueError):
            M.check_payload(
                {"schema": "finite-fully-resonant-coherent-poles-v1", "status": "PASS"}
            )


if __name__ == "__main__":
    unittest.main()
