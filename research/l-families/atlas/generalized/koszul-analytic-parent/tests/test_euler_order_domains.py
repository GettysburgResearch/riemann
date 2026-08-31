"""Source compact traces, degree grouping, exact norms and arithmetic pole orders."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "euler_order_domains", HERE / "euler_order_domains_replay.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class SignedBranchSourceTests(unittest.TestCase):
    def test_all_old_branch_places_retain_degree_and_actual_sign(self):
        for index in range(3):
            result = M.branch_inventory(index)
            self.assertEqual(
                sum(
                    row["degree"] * row["count"] for row in result["closed_branch_rows"]
                ),
                4,
            )
            self.assertTrue(
                all(row["chi"] in (-1, 1) for row in result["closed_branch_rows"])
            )

    def test_quartic_orbit_sign_uses_base_norm_without_a_field_four_count(self):
        result = M.branch_inventory(0)
        self.assertEqual(
            result["closed_branch_rows"], [{"degree": 4, "chi": -1, "count": 1}]
        )
        self.assertEqual(result["quartic_root_norm_in_base_field"], 3)
        self.assertFalse(result["degree_four_field_enumerated"])

    def test_extension_branch_sign_counts_remove_squared_rational_points(self):
        for index in range(3):
            result = M.branch_inventory(index)
            old_negative, old_positive = result["rational_branch_chi_counts"]
            extension_negative, extension_positive = result[
                "extension_two_branch_chi_counts"
            ]
            degree_two = {-1: 0, 1: 0}
            for row in result["closed_branch_rows"]:
                if row["degree"] == 2:
                    degree_two[row["chi"]] += row["count"]
            self.assertEqual(extension_negative, 2 * degree_two[-1])
            self.assertEqual(
                extension_positive, 2 * degree_two[1] + old_negative + old_positive
            )

    def test_compact_first_source_has_twelve_proper_and_twelve_boundary_dimensions(
        self,
    ):
        result = M.compact_first_source(0)
        self.assertEqual(result["compact_h0_h1_h2"], [0, 24, 0])
        self.assertEqual(result["weight_one_and_boundary_ranks"], [12, 12])
        self.assertEqual(len(result["compact_first_grade_polynomial"]), 25)
        self.assertEqual(
            result["actual_boundary_polynomial"],
            [1, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 1],
        )

    def test_compact_polynomial_first_powers_equal_primitive_good_fibres(self):
        for index in range(3):
            result = M.compact_first_source(index)
            self.assertEqual(
                result["compact_trace_sums"][:2], result["new_primitive_good_traces"]
            )
            self.assertLessEqual(result["maximum_new_primitive_field_order"], 49)

    def test_closed_degree_two_linear_trace_keeps_frobenius_powers(self):
        for index in range(3):
            result = M.compact_first_source(index)
            self.assertEqual(
                2 * result["closed_degree_one_two_linear_traces"][1],
                result["new_primitive_good_traces"][1]
                - result["rational_good_second_power_trace"],
            )

    def test_good_zero_polynomial_has_fourteen_roots_but_is_not_a_new_curve_numerator(
        self,
    ):
        for index in range(3):
            result = M.compact_first_source(index)
            q = result["parameters"][0]
            self.assertEqual(len(result["first_good_zero_polynomial"]), 15)
            self.assertEqual(result["first_good_zero_polynomial"][-1], -(q**7))
            self.assertTrue(
                result["first_good_zero_polynomial_is_not_a_new_curve_numerator"]
            )

    def test_newton_recurrence_retains_signed_polynomial_trace_convention(self):
        self.assertEqual(M.local_sums_from_polynomial([1, -2], 4), [-2, -4, -8, -16])
        self.assertEqual(M.local_sums_from_polynomial([1, 0, 7], 4), [0, 14, 0, -98])


class GroupedDegreeDomainTests(unittest.TestCase):
    def test_certified_grouped_radius_lies_outside_absolute_Euler_domain(self):
        for q in (5, 7):
            result = M.degree_tail_control(q)
            r = Fraction(*result["radius"])
            upper = Fraction(*result["sqrt_Q_times_radius_upper"])
            self.assertGreater(q * r, 1)
            self.assertLess(q * r * r, 1)
            self.assertGreaterEqual(upper * upper, q * r * r)
            self.assertTrue(result["outside_absolute_Euler_disk"])

    def test_complete_degree_tail_is_the_sum_of_distinct_linear_and_nonlinear_bounds(
        self,
    ):
        result = M.degree_tail_control(7)
        self.assertEqual(
            Fraction(*result["complete_degree_tail_bound"]),
            Fraction(*result["linear_degree_tail_bound"])
            + Fraction(*result["nonlinear_degree_tail_bound"]),
        )
        self.assertGreater(Fraction(*result["complete_degree_tail_bound"]), 0)

    def test_actual_transposition_and_cycle_log_coefficients_keep_support(self):
        self.assertEqual(
            [M.local_log_coefficient("s", -1, n) for n in range(1, 7)],
            [0, 2, 0, 1, 0, Fraction(2, 3)],
        )
        self.assertEqual(
            [M.local_log_coefficient("c", -1, n) for n in range(1, 7)],
            [0, 0, -1, 0, 0, Fraction(1, 2)],
        )

    def test_identity_linear_trace_is_six_times_actual_joint_sign(self):
        self.assertEqual(M.local_log_coefficient("e", 1, 1), 6)
        self.assertEqual(M.local_log_coefficient("e", -1, 1), -6)
        self.assertEqual(M.local_log_coefficient("e", 1, 2), 0)

    def test_second_interior_radius_has_a_separate_rational_growth_certificate(self):
        result = M.degree_tail_control(7, Fraction(1, 3), Fraction(9, 10), 24)
        self.assertEqual(result["radius"], [1, 3])
        self.assertEqual(result["sqrt_Q_times_radius_upper"], [9, 10])
        self.assertGreater(Fraction(*result["complete_degree_tail_bound"]), 0)

    def test_endpoint_or_underestimated_growth_bound_is_rejected(self):
        with self.assertRaises(ValueError):
            M.degree_tail_control(5, Fraction(1, 2), Fraction(3, 4))
        with self.assertRaises(ValueError):
            M.degree_tail_control(7, Fraction(1, 4), Fraction(1, 2))
        with self.assertRaises(ValueError):
            M.degree_tail_control(5, Fraction(1, 4), Fraction(1))

    def test_split_linear_term_dominates_the_actual_absolute_higher_coefficients(self):
        result = M.local_root_and_split_controls()
        r = Fraction(*result["split_small_argument_cap"])
        tail = Fraction(*result["split_absolute_higher_coefficient_bound"])
        self.assertLess(tail, 3 * r)
        self.assertEqual(Fraction(*result["split_linear_term"]), 6 * r)

    def test_bad_even_zero_control_is_outside_the_good_log_claim(self):
        result = M.local_root_and_split_controls()
        self.assertEqual(
            result["bad_even_root_absolute_square_interval"], [[1, 16], [1, 9]]
        )
        self.assertTrue(result["finite_bad_factor_not_in_good_log"])
        self.assertFalse(result["new_parameter_or_field_for_bad_root_control"])


class ExactArithmeticPoleTests(unittest.TestCase):
    def test_actual_seven_point_counts_precede_frobenius_squaring(self):
        result = M.square_field_source_control()
        self.assertEqual(sum(result["elliptic_finite_fibre_counts"]), 7)
        self.assertEqual(sum(result["discriminant_finite_fibre_counts"]), 6)
        self.assertEqual(result["infinity_counts_E_D"], [1, 2])
        self.assertEqual(result["proper_point_counts_E_D"], [8, 8])
        self.assertFalse(result["field_49_enumerated"])

    def test_basechange_uses_frobenius_squared_not_a_new_large_field_fit(self):
        result = M.square_field_source_control()
        self.assertEqual(result["base_field_polynomials_E_D"], [[1, 0, 7], [1, 0, 7]])
        self.assertEqual(
            result["Frobenius_square_polynomials_E_D"], [[1, 14, 49], [1, 14, 49]]
        )

    def test_actual_grade_eight_trivial_multiplicity_is_not_dimension_divided_by_six(
        self,
    ):
        result = M.square_field_source_control()
        self.assertEqual(
            result["source_multiplicities_grades_four_eight"], [[0, 1, 1], [4, 6, 10]]
        )
        self.assertNotEqual(4, (4 + 6 + 2 * 10) // 6)

    def test_square_field_grade_four_apparent_pole_cancels_exactly(self):
        row = M.square_field_source_control()["grade_four_order"]
        self.assertEqual(row["elliptic_denominator_order"], 4)
        self.assertEqual(row["resonance_zero_correction"], 4)
        self.assertEqual(row["signed_order"], 0)
        self.assertEqual(row["pole_order"], 0)

    def test_square_field_grade_two_poles_survive_the_zero_grade_four_principal_multiplicity(
        self,
    ):
        row = M.square_field_source_control()["grade_two_order"]
        self.assertEqual(row["double_grade_trivial_multiplicity"], 0)
        self.assertEqual(row["pole_order"], 2)

    def test_trace_zero_over_the_nonsquare_base_is_not_real_resonance(self):
        row = M.square_field_source_control()["nonsquare_trace_zero_is_not_resonance"]
        self.assertEqual(row["resonance_zero_correction"], 0)
        self.assertEqual(row["pole_order"], 2)

    def test_norm_table_retains_only_prime_two_three_constants(self):
        rows = M.reciprocal_norm_table()
        self.assertEqual(
            [row["monic_reciprocal_polynomial"][0] for row in rows], [2, -2, 1, 3, 9, 3]
        )
        self.assertTrue(
            all(row["monic_reciprocal_polynomial"][-1] == 1 for row in rows)
        )

    def test_pole_formula_rejects_wrong_parity_or_ambiguous_resonance(self):
        with self.assertRaises(ValueError):
            M.even_arithmetic_order(3, 1, 1, False)
        with self.assertRaises(ValueError):
            M.even_arithmetic_order(4, 1, 1, 1)
        with self.assertRaises(ValueError):
            M.even_arithmetic_order(4, 0, 0, False)


class AuthenticationTests(unittest.TestCase):
    def test_frozen_scientific_source_chain_is_authenticated(self):
        M.authenticate_frozen()

    def test_forged_summary_is_not_an_accepted_fixture(self):
        with self.assertRaises(ValueError):
            M.check_payload(
                {
                    "schema": "source-Euler-order-domains-and-pole-divisor-v1",
                    "status": "PASS",
                }
            )

    def test_primitive_types_and_caps_are_enforced_before_dependency_cache(self):
        M.branch_inventory(1)
        for index in (True, 1.0, -1, 3):
            with self.subTest(index=index), self.assertRaises((TypeError, ValueError)):
                M.branch_inventory(index)
        with self.assertRaises(ValueError):
            M.local_sums_from_polynomial([1, True], 4)


if __name__ == "__main__":
    unittest.main()
