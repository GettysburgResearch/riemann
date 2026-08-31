"""Closed-place source, finite extraction, positive residue and S4 calibration."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "segre_place_euler", HERE / "segre_place_euler_replay.py"
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ClosedPlaceSourceTests(unittest.TestCase):
    def test_degree_two_counts_include_Frobenius_squaring(self):
        data = M.closed_place_data(0)
        self.assertEqual(data["degree_one_good"]["s"], 2)
        wrong = Fraction(
            data["extension_two_good"]["e"] - data["degree_one_good"]["e"], 2
        )
        self.assertNotEqual(wrong, data["degree_two_good"]["e"])
        self.assertEqual(wrong - data["degree_two_good"]["e"], 1)

    def test_every_degree_two_base_place_is_accounted_for(self):
        for index in range(3):
            data = M.closed_place_data(index)
            q = data["parameters"][0]
            self.assertEqual(
                sum(data["degree_two_good"].values())
                + dict(data["finite_branch_orbits"])[2],
                (q * q - q) // 2,
            )

    def test_degree_four_branch_orbit_is_not_dropped_after_two_field_counts(self):
        self.assertEqual(
            dict(M.closed_place_data(0)["finite_branch_orbits"]), {1: 0, 2: 0, 4: 1}
        )

    def test_all_three_native_branch_orbit_profiles(self):
        self.assertEqual(
            dict(M.closed_place_data(1)["finite_branch_orbits"]), {1: 0, 2: 2, 4: 0}
        )
        self.assertEqual(
            dict(M.closed_place_data(2)["finite_branch_orbits"]), {1: 2, 2: 1, 4: 0}
        )

    def test_full_place_Euler_agrees_with_independent_cohomology_and_correction(self):
        for index in range(3):
            result = M.global_coefficient_control(index)
            self.assertEqual(result["place_Euler_coefficients"][0], 1)
            self.assertTrue(
                all(
                    isinstance(value, int) and value >= 0
                    for value in result["place_Euler_coefficients"]
                )
            )

    def test_actual_residual_infinity_changes_degree_two_correction(self):
        self.assertEqual(M.global_coefficient_control(0)["degree_two_correction"], 2)
        self.assertEqual(M.global_coefficient_control(1)["degree_two_correction"], 4)
        self.assertEqual(M.global_coefficient_control(2)["degree_two_correction"], 16)

    def test_bad_correction_keeps_grade_one_and_changes_grade_two(self):
        for index in range(3):
            correction = M.bad_correction_series(index)
            self.assertEqual(correction[:2], [1, 0])
            self.assertGreater(correction[2], 0)

    def test_source_indices_are_validated_before_cache(self):
        M.closed_place_data(1)
        for value in (True, 1.0, -1, 3):
            with self.subTest(value=value), self.assertRaises((ValueError, TypeError)):
                M.closed_place_data(value)


class FiniteExtractionTests(unittest.TestCase):
    def test_actual_regular_source_first_extraction_is_the_proved_polynomial(self):
        result = M.extraction_control(1)
        by_class = {
            row["class"]: row["Euler_remainder"] for row in result["source_classes"]
        }
        self.assertEqual(
            by_class, {"e": [1, 0, -3, 2], "s": [1, 0, -1, 0], "c": [1, 0, 0, -1]}
        )

    def test_every_required_low_grade_disappears(self):
        for cut in (1, 2, 3, 6):
            for row in M.extraction_control(cut)["source_classes"]:
                self.assertEqual(row["Euler_remainder"][: cut + 1], [1] + [0] * cut)

    def test_first_omitted_source_grade_has_correct_sign_and_dimension(self):
        for cut in (1, 2, 3, 6):
            row = M.extraction_control(cut)["source_classes"][0]
            next_grade = M.M.lie_rows(cut + 1)[-1]
            self.assertEqual(
                row["Euler_remainder"][cut + 1],
                next_grade["parity_sign"] * next_grade["class_traces"][0],
            )

    def test_formal_operations_fail_closed_on_nonunit_denominator(self):
        with self.assertRaises(ValueError):
            M.divide([1], [2], 2)
        with self.assertRaises(ValueError):
            M.integer_power([1, -1], True, 2)

    def test_extraction_caps_are_bounded(self):
        with self.assertRaises(ValueError):
            M.extraction_control(9)
        with self.assertRaises(ValueError):
            M.source_parent_prefix("C2", 1, 3)


class PositiveResidueTests(unittest.TestCase):
    def test_source_defined_residue_intervals_are_strictly_positive(self):
        for index in range(3):
            result = M.residue_control(index)
            low, high = [
                Fraction(*pair) for pair in result["positive_residue_interval"]
            ]
            self.assertGreater(low, 0)
            self.assertGreater(high, low)
            self.assertFalse(result["higher_degree_fields_recounted"])

    def test_relative_residue_error_is_the_proved_missing_place_bound(self):
        for index in range(3):
            result = M.residue_control(index)
            low, high = [
                Fraction(*pair) for pair in result["positive_residue_interval"]
            ]
            error = Fraction(*result["proved_omitted_log_bound"])
            self.assertEqual(low, high * (1 - error))
            self.assertLess(error, Fraction(1, 50))

    def test_each_source_factor_in_residue_is_positive(self):
        result = M.residue_control(0)
        for key in (
            "proper_closure_residue",
            "actual_upstairs_boundary_factor",
            "actual_bad_Segre_factor",
            "good_place_tail_through_degree_two",
        ):
            self.assertGreater(Fraction(*result[key]), 0)

    def test_first_extraction_tail_uses_actual_class(self):
        t = Fraction(1, 5)
        self.assertEqual(M.first_tail("e", t), Fraction(112, 125))
        self.assertEqual(M.first_tail("s", t), Fraction(24, 25))
        self.assertEqual(M.first_tail("c", t), Fraction(124, 125))

    def test_positive_local_domains_are_enforced(self):
        with self.assertRaises(ValueError):
            M.first_tail("e", Fraction(1))
        with self.assertRaises(ValueError):
            M.segre_value("C2", Fraction(0))


class SharpSubleadingSourceTests(unittest.TestCase):
    def test_first_four_characters_are_actual_source_characters(self):
        self.assertEqual(
            [row["character"] for row in M.first_four_s3_sources()],
            [[6, 0, 0], [3, 1, 0], [2, 0, -1], [3, -1, 0]],
        )

    def test_grades_three_and_four_have_no_trivial_constituent(self):
        rows = M.first_four_s3_sources()
        self.assertEqual(
            [row["multiplicities"] for row in rows],
            [[1, 1, 2], [1, 0, 1], [0, 0, 1], [0, 1, 1]],
        )
        self.assertEqual(
            [row["proper_factor_exponents_one_Q_D_E"][1] for row in rows], [-1, 1, 0, 0]
        )

    def test_full_invariant_bad_numerators_are_not_invariant_input_series(self):
        result = M.bad_numerator_control()
        self.assertEqual(
            {row["kind"]: row["numerator"] for row in result["local_sources"]},
            {"C2": [1, 1, 3, 1], "C3": [1, -1, 3], "C3s": [1]},
        )
        self.assertEqual(
            result["local_sources"][0]["source_series_checked_through"], 12
        )

    def test_finite_branch_units_and_infinity_nonunits_have_distinct_obstructions(self):
        result = M.bad_numerator_control()
        self.assertTrue(result["C2_monic_constant_one"])
        self.assertEqual(result["C3_root_modulus_squared"], [1, 3])

    def test_subleading_factor_is_actual_elliptic_polynomial_at_z_squared(self):
        for index in range(3):
            result = M.subleading_pole_control(index)
            pe = result["elliptic_polynomial"]
            self.assertEqual(
                result["exact_first_subleading_pole_polynomial"],
                [1, 0, pe[1], 0, pe[2]],
            )
            self.assertEqual(result["grade_four_trivial_multiplicity"], 0)
            self.assertEqual(result["source_four_grade_product_through_degree"], 20)

    def test_grade_four_extraction_removes_four_actual_grades(self):
        for row in M.extraction_control(4)["source_classes"]:
            self.assertEqual(row["Euler_remainder"][:5], [1, 0, 0, 0, 0])


class S4SourceCriterionTests(unittest.TestCase):
    def test_first_S4_Lie_grade_is_the_actual_tensor_source(self):
        row = M.s4_lie_sources()[0]
        self.assertEqual(row["actual_character"], [12, 2, 0, 0, 0])
        self.assertEqual(row["multiplicities"], [1, 0, 1, 2, 1])
        self.assertEqual(row["closed_h0_h1_h2"], [1, 14, 1])

    def test_second_S4_grade_uses_exterior_square_relations(self):
        row = M.s4_lie_sources()[1]
        self.assertEqual(row["actual_character"], [18, 0, 2, 0, 0])
        self.assertEqual(row["multiplicities"], [1, 1, 2, 2, 2])
        self.assertEqual(row["closed_h0_h1_h2"], [1, 28, 1])

    def test_S4_compact_support_retains_seven_geometric_punctures(self):
        rows = M.s4_lie_sources()
        self.assertEqual(rows[0]["compact_h0_h1_h2"], [0, 61, 1])
        self.assertEqual(rows[1]["compact_h0_h1_h2"], [0, 91, 1])

    def test_actual_S4_finite_bad_fibres_match_both_Lie_sources(self):
        for index in range(3):
            result = M.s4_source_control(index)
            self.assertEqual([row["extension"] for row in result], [1, 2])
            self.assertLessEqual(max(row["field_order"] for row in result), 49)

    def test_S4_identity_root_and_conjugate_are_on_opposite_sides_of_one(self):
        result = M.root_certificate()
        lo, hi = [Fraction(*pair) for pair in result["S4_positive_rho_interval"]]
        clo, chi = [Fraction(*pair) for pair in result["S4_conjugate_interval"]]
        self.assertGreater(lo, 0)
        self.assertLess(hi, 1)
        self.assertGreater(clo, 1)
        self.assertEqual(lo + chi, 2)
        self.assertEqual(hi + clo, 2)

    def test_noncollision_criterion_is_not_asserted_as_a_classification(self):
        self.assertTrue(
            M.root_certificate()[
                "criterion_not_a_classification_when_noncollision_fails"
            ]
        )

    def test_frozen_source_authentication(self):
        M.authenticate_frozen()

    def test_forged_fixture_summary_is_rejected(self):
        with self.assertRaises(ValueError):
            M.check_payload(
                {"schema": "source-corrected-Segre-place-Euler-v1", "status": "PASS"}
            )


if __name__ == "__main__":
    unittest.main()
