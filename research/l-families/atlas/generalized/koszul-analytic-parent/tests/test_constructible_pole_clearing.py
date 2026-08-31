"""Source operations, ramified counterfeits and distinct global coefficient laws."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "constructible_clearing", HERE / "constructible_pole_clearing_replay.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ActualConstructibleSourceTests(unittest.TestCase):
    def test_standard_determinants_retain_all_three_actual_classes(self):
        self.assertEqual(
            [M.standard_determinant(kind) for kind in ("e", "s", "c")],
            [[1, -2, 1], [1, 0, -1], [1, 1, 1]],
        )

    def test_actual_second_relation_contains_the_declared_standard_summand(self):
        self.assertEqual(M.F.adams_source_row(2)["multiplicities"], [1, 0, 1])

    def test_generic_generator_is_in_internal_degree_two(self):
        row = M.local_source("good", "e")
        self.assertEqual(
            row["standard_stalk_determinant_in_t_squared"][:5], [1, 0, -2, 0, 1]
        )
        self.assertEqual(row["declared_B_series"][:3], [1, 6, 20])

    def test_tensor_sym_convolution_matches_local_determinants_with_both_signs(self):
        for kind in ("e", "s", "c"):
            for sign in (-1, 1):
                row = M.local_source("good", kind, sign)
                self.assertEqual(row["declared_B_series"], row["tensor_Sym_series"])

    def test_twist_does_not_silently_change_extra_standard_generator(self):
        plus = M.local_source("good", "e", 1)
        minus = M.local_source("good", "e", -1)
        self.assertEqual(
            plus["standard_stalk_determinant_in_t_squared"],
            minus["standard_stalk_determinant_in_t_squared"],
        )
        self.assertEqual(plus["declared_B_series"][1], -minus["declared_B_series"][1])

    def test_old_branch_standard_stalk_is_one_dimensional(self):
        row = M.local_source("old_branch", "C2")
        self.assertEqual(
            row["standard_stalk_determinant_in_t_squared"][:5], [1, 0, -1, 0, 0]
        )

    def test_old_branch_ambient_first_extension_is_not_the_declared_source(self):
        self.assertEqual(
            M.extension_order_control()["old_C2_degree_three_pair"], [23, 26]
        )

    def test_old_branch_negative_frobenius_retains_the_sign_of_the_counterfeit(self):
        self.assertEqual(
            M.extension_order_control(-1)["old_C2_degree_three_pair"], [-23, -26]
        )

    def test_split_infinity_exposes_crossed_invariant_degree_four_terms(self):
        self.assertEqual(
            M.extension_order_control()["infinity_order_controls"][0][
                "declared_and_ambient_grade_four"
            ],
            [25, 38],
        )

    def test_nonsplit_infinity_uses_frobenius_trace_not_invariant_dimension(self):
        self.assertEqual(
            M.extension_order_control()["infinity_order_controls"][1][
                "declared_and_ambient_grade_four"
            ],
            [3, 4],
        )

    def test_infinity_declared_source_has_no_extra_standard_stalk(self):
        for kind in ("C3", "C3s"):
            row = M.local_source("infinity", kind)
            self.assertEqual(row["original_A_series"], row["declared_B_series"])

    def test_zero_inertia_commutes_with_the_untwisted_standard_addition(self):
        for kind in ("e", "s", "c"):
            declared = M.local_source("zero", kind)["declared_B_series"]
            ambient = M.A.even_series(M.local_source("good", kind)["declared_B_series"])
            self.assertEqual(declared, ambient)
            self.assertTrue(all(declared[n] == 0 for n in range(1, len(declared), 2)))

    def test_unknown_strata_and_wrong_inertia_are_rejected(self):
        for place, kind in (
            ("middle_extension", "e"),
            ("old_branch", "e"),
            ("zero", "C2"),
            ("infinity", "s"),
        ):
            with self.subTest(place=place, kind=kind), self.assertRaises(ValueError):
                M.local_source(place, kind)

    def test_primitive_types_and_caps_fail_closed(self):
        for cut in (True, 2.0, 1, 17):
            with self.subTest(cut=cut), self.assertRaises((TypeError, ValueError)):
                M.local_source("good", "e", cut=cut)
        for sign in (True, 1.0, 0):
            with self.subTest(sign=sign), self.assertRaises(ValueError):
                M.local_source("good", "e", sign)


class GlobalSourceAndAnalyticCasesTests(unittest.TestCase):
    def test_actual_all_stalk_euler_coefficients_match_standard_cohomology(self):
        for index in range(3):
            row = M.source_coefficient_control(index)
            self.assertEqual(
                row["new_B_coefficients_by_all_stalks"],
                row["new_B_coefficients_by_elliptic_cohomology"],
            )

    def test_ramified_standard_sum_is_the_actual_elliptic_polynomial_coefficient(self):
        for index in range(3):
            row = M.source_coefficient_control(index)
            self.assertEqual(
                row["actual_standard_stalk_sum_including_ramification"],
                row["elliptic_polynomial"][1],
            )

    def test_original_and_modified_coefficients_have_the_explicit_degree_two_law(self):
        for index in range(3):
            row = M.source_coefficient_control(index)
            old = row["original_E_chi_coefficients"]
            new = row["new_B_coefficients_by_all_stalks"]
            self.assertEqual(new[:2], old[:2])
            self.assertEqual(new[2] - old[2], row["elliptic_polynomial"][1])

    def test_no_new_field_or_parameter_is_counted(self):
        for index in range(3):
            self.assertLessEqual(
                max(M.source_coefficient_control(index)["primitive_field_orders"]), 49
            )
        self.assertFalse(M.F.actual_clearing_factor()["new_field_enumerated"])

    def test_nonresonant_fourth_grade_poles_survive_the_second_grade_clearing(self):
        row = M.analytic_case_control()
        self.assertEqual(row["actual_fourth_relation"]["multiplicities"], [0, 1, 1])
        for source in row["nonsquare_source_cases"]:
            self.assertEqual(
                source["grade_four_order_control"]["pole_order"],
                1 + int(source["E_and_D_have_common_roots"]),
            )
            self.assertEqual(source["new_root_growth_power_of_Q"], [1, 8])

    def test_fully_resonant_source_uses_frobenius_square_and_distinct_new_function(
        self,
    ):
        row = M.analytic_case_control()
        self.assertEqual(row["fully_resonant_new_root_limsup"], 1)
        self.assertEqual(
            row["fully_resonant_source"]["minimal_normalized_pole_clearing_polynomial"],
            [1, 0, 14, 0, 49],
        )
        self.assertTrue(
            row["fully_resonant_source"]["modified_function_distinct_from_original"]
        )

    def test_typed_fixture_rejects_bool_substitution_for_integer(self):
        candidate = M.build_payload()
        candidate["standard_stalk_determinants"]["e"][0] = True
        with self.assertRaises(ValueError):
            M.check_payload(candidate)

    def test_fixture_rejects_tampered_operation_order(self):
        candidate = copy.deepcopy(M.build_payload())
        candidate["extension_order_controls"][0]["old_C2_degree_three_pair"][0] = -26
        with self.assertRaises(ValueError):
            M.check_payload(candidate)

    def test_dependency_authentication_fails_before_replay(self):
        with (
            patch.object(M.subprocess, "check_output", return_value="wrong\n"),
            self.assertRaises(ValueError),
        ):
            M.authenticate_frozen()


if __name__ == "__main__":
    unittest.main()
