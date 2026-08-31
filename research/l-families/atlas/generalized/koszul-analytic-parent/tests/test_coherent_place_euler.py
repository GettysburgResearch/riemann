"""Actual chi^n local operation, new inertia, source cancellation and elliptic poles."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "coherent_place_euler", HERE / "coherent_place_euler_replay.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ActualClosedPlaceTests(unittest.TestCase):
    def test_actual_closed_place_source_matches_corrected_finite_cohomology(self):
        for index in range(3):
            row = M.closed_coefficient_control(index)
            self.assertEqual(
                row["coherent_place_coefficients"],
                M.M.multiply(
                    row["finite_twisted_Lie_coefficients"],
                    [1, 0, row["total_actual_bad_correction"]],
                    2,
                ),
            )

    def test_first_coefficient_is_the_geometric_anti_regular_trace(self):
        for index in range(3):
            row = M.closed_coefficient_control(index)
            self.assertEqual(
                row["coherent_place_coefficients"][1], row["actual_anti_regular_trace"]
            )

    def test_closed_degree_two_retains_actual_rational_frobenius_square(self):
        rows = [M.closed_coefficient_control(index) for index in range(3)]
        for row in rows:
            self.assertEqual(
                2 * row["closed_degree_two_first_grade_trace"],
                row["extension_two_anti_trace"]
                - row["rational_point_second_power_trace"],
            )
        self.assertTrue(
            any(
                row["rational_point_second_power_trace"]
                != row["actual_anti_regular_trace"]
                for row in rows
            )
        )

    def test_new_ramification_changes_all_three_native_corrections(self):
        self.assertEqual(
            [
                M.closed_coefficient_control(index)["total_actual_bad_correction"]
                for index in range(3)
            ],
            [3, 7, 22],
        )

    def test_zero_frobenius_is_recovered_from_actual_joint_source(self):
        self.assertEqual(
            [M.zero_kind(M.native_source(index)) for index in range(3)], ["c", "c", "s"]
        )

    def test_signed_coefficients_have_the_untwisted_divisor_majorant(self):
        for index in range(3):
            row = M.closed_coefficient_control(index)
            for signed, positive in zip(
                row["coherent_place_coefficients"], row["untwisted_place_coefficients"]
            ):
                self.assertLessEqual(abs(signed), positive)

    def test_fixed_chi_module_is_not_the_coherent_grade_two_source(self):
        rows = [M.closed_coefficient_control(index) for index in range(3)]
        self.assertTrue(
            all(
                a != b
                for a, b in (
                    row["rational_grade_two_coherent_and_fixed_module_traces"]
                    for row in rows
                )
            )
        )

    def test_source_validation_precedes_native_count_cache(self):
        M.native_source(1)
        for index in (True, 1.0, -1, 3):
            with self.subTest(index=index), self.assertRaises((TypeError, ValueError)):
                M.native_source(index)


class NewInertiaTests(unittest.TestCase):
    def test_new_ramified_sources_retain_only_even_grades(self):
        for row in M.new_bad_source_control()["local_sources"]:
            self.assertTrue(
                all(value == 0 for value in row["actual_source_prefix"][1::2])
            )
            self.assertEqual(row["new_grade_one_stalk_trace"], 0)

    def test_zero_even_numerators_come_from_full_original_source(self):
        rows = {
            row["source"]: row for row in M.new_bad_source_control()["local_sources"]
        }
        self.assertEqual(rows["zero_e"]["numerator"], [1, 0, 14, 0, 9])
        self.assertEqual(rows["zero_s"]["numerator"], [1])
        self.assertEqual(rows["zero_c"]["numerator"], [1])

    def test_split_infinity_has_its_distinct_full_even_numerator(self):
        rows = {
            row["source"]: row for row in M.new_bad_source_control()["local_sources"]
        }
        self.assertEqual(rows["infinity_C3"]["numerator"], [1, 0, 3, 0, 10, 0, 7, 0, 3])
        self.assertEqual(rows["infinity_C3"]["actual_source_prefix"][:3], [1, 0, 6])
        self.assertEqual(rows["infinity_C3s"]["actual_source_prefix"][:3], [1, 0, 2])

    def test_taking_invariant_inputs_would_lose_nonzero_even_zero_source(self):
        rows = {
            row["source"]: row for row in M.new_bad_source_control()["local_sources"]
        }
        self.assertEqual(rows["zero_e"]["actual_source_prefix"][:3], [1, 0, 18])
        self.assertNotEqual(rows["zero_e"]["actual_source_prefix"], [1] + [0] * 12)

    def test_reciprocal_monic_constants_enforce_the_prime_three_norm_obstruction(self):
        result = M.new_bad_source_control()
        self.assertEqual(
            result["reciprocal_integer_polynomials_in_Weil_power"],
            [[9, 14, 1], [3, 7, 10, 3, 1]],
        )
        self.assertEqual(result["norm_obstruction_prime"], 3)
        self.assertTrue(result["requires_characteristic_greater_than_three"])

    def test_unramified_negative_chi_keeps_even_old_branch_coefficient(self):
        base = M.M.segre_series("C2", 4)
        negative = M.signed_series(base, -1)
        self.assertEqual(negative[2], base[2])
        self.assertEqual(negative[1], -base[1])


class CoherentExtractionTests(unittest.TestCase):
    def test_all_required_grades_cancel_for_both_actual_joint_signs(self):
        for cut in (1, 2, 3, 4, 6):
            for epsilon in (-1, 1):
                for row in M.extraction_control(cut, epsilon)["source_classes"]:
                    self.assertEqual(
                        row["actual_remainder"][: cut + 1], [1] + [0] * cut
                    )

    def test_first_omitted_grade_obeys_the_homogeneous_twist_law(self):
        for cut in (1, 2, 3, 4, 6):
            positive = M.extraction_control(cut, 1)["source_classes"][0][
                "actual_remainder"
            ][cut + 1]
            negative = M.extraction_control(cut, -1)["source_classes"][0][
                "actual_remainder"
            ][cut + 1]
            self.assertEqual(negative, positive * (-1) ** (cut + 1))

    def test_coherent_twist_keeps_the_normalized_constant_coefficient(self):
        self.assertEqual(M.signed_series([1, 6, 18, 40], -1), [1, -6, 18, -40])
        self.assertNotEqual(M.signed_series([1, 6, 18, 40], -1), [-1, -6, -18, -40])

    def test_joint_sign_and_extraction_bounds_fail_closed(self):
        for sign in (True, 1.0, 0, 2):
            with self.subTest(sign=sign), self.assertRaises(ValueError):
                M.extraction_control(2, sign)
        with self.assertRaises(ValueError):
            M.extraction_control(7, 1)


class ActualFiniteCohomologyTests(unittest.TestCase):
    def test_first_four_proper_ranks_keep_twist_parity(self):
        rows = M.first_four_factor_control(0)["actual_cohomology_by_grade"]
        self.assertEqual(
            [row["proper_h0_h1_h2"] for row in rows],
            [[0, 12, 0], [1, 2, 1], [0, 4, 0], [0, 4, 0]],
        )

    def test_first_grade_is_the_actual_degree_twelve_anti_regular_polynomial(self):
        for index in range(3):
            result = M.first_four_factor_control(index)
            q = result["parameters"][0]
            polynomial = result["anti_regular_degree_twelve_polynomial"]
            self.assertEqual(len(polynomial), 13)
            self.assertEqual(polynomial[0], 1)
            self.assertEqual(polynomial[-1], q**6)

    def test_second_grade_keeps_the_original_elliptic_pole_factor(self):
        for index in range(3):
            result = M.first_four_factor_control(index)
            self.assertTrue(result["same_elliptic_denominator_as_untwisted"])
            self.assertEqual(
                result["exact_first_pole_polynomial"],
                M.E.subleading_pole_control(index)[
                    "exact_first_subleading_pole_polynomial"
                ],
            )

    def test_first_Q_pole_disappears_in_the_source_not_by_subtracting_a_scalar(self):
        result = M.first_four_factor_control(1)
        self.assertTrue(result["first_grade_main_Q_pole_absent_from_actual_source"])
        self.assertEqual(
            result["actual_cohomology_by_grade"][0]["proper_h0_h1_h2"][2], 0
        )
        self.assertEqual(
            result["actual_cohomology_by_grade"][1]["proper_h0_h1_h2"][2], 1
        )

    def test_odd_grades_twist_and_even_grades_do_not(self):
        rows = M.first_four_factor_control(2)["actual_cohomology_by_grade"]
        self.assertEqual(
            [row["quadratic_twist_present"] for row in rows], [True, False, True, False]
        )

    def test_twisted_standard_factor_is_rank_four_and_primitive_fields_stay_small(self):
        for index in range(3):
            result = M.first_four_factor_control(index)
            q = result["parameters"][0]
            poly = result["twisted_standard_polynomial"]
            self.assertEqual(len(poly), 5)
            self.assertEqual(poly[-1], q * q)
            self.assertEqual(poly[3], q * poly[1])
            self.assertLessEqual(
                max(M.closed_coefficient_control(index)["primitive_field_orders"]), 49
            )


class AuthenticationTests(unittest.TestCase):
    def test_both_frozen_source_chains_are_authenticated(self):
        M.authenticate_frozen()

    def test_forged_fixture_is_rejected(self):
        with self.assertRaises(ValueError):
            M.check_payload(
                {"schema": "coherent-quadratic-place-Euler-v1", "status": "PASS"}
            )


if __name__ == "__main__":
    unittest.main()
