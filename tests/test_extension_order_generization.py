"""Source maps invisible to every ordinary closed-point Euler factor."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/extension-order-defect/generization_replay.py"
)
SPEC = importlib.util.spec_from_file_location("generization_invisibility", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class ActualMapTests(unittest.TestCase):
    def test_unit_generization_is_unchanged(self):
        row = R.map_control(0)
        self.assertEqual(row["original_image_rows"], [0])
        self.assertEqual(row["counterfeit_image_rows"], [0])
        self.assertEqual(row["original_generization_rank"], 1)

    def test_actual_degree_one_rank_discriminator(self):
        row = R.map_control(1)
        self.assertEqual(row["boundary_dimension"], 3)
        self.assertEqual(row["nearby_invariant_dimension"], 3)
        self.assertEqual(row["original_generization_rank"], 3)
        self.assertEqual(row["counterfeit_generization_rank"], 0)

    def test_degree_three_extension_order_defect_is_not_generization_defect(self):
        row = R.map_control(3)
        self.assertEqual(row["boundary_dimension"], 23)
        self.assertEqual(row["nearby_invariant_dimension"], 26)
        self.assertEqual(row["original_generization_rank"], 23)
        self.assertEqual(row["counterfeit_generization_rank"], 0)

    def test_literal_boundary_is_a_subset_with_unique_image_rows(self):
        for grade in range(7):
            nearby, boundary = R.old_basis(grade)
            row = R.map_control(grade)
            self.assertEqual(
                [nearby[index] for index in row["original_image_rows"]], boundary
            )
            self.assertEqual(len(set(row["original_image_rows"])), len(boundary))

    def test_quadratic_sign_on_same_boundary_is_retained(self):
        for grade in range(7):
            positive = R.map_control(grade, 1)
            negative = R.map_control(grade, -1)
            self.assertEqual(
                positive["original_image_rows"], negative["original_image_rows"]
            )
            self.assertEqual(
                negative["shared_boundary_frobenius_eigenvalue"], (-1) ** grade
            )

    def test_actual_multiplication_and_augmentation(self):
        result = R.multiplication_controls()
        self.assertGreater(result["literal_products_checked"], 100)
        self.assertTrue(result["original_inclusion_multiplicative"])
        self.assertTrue(result["augmentation_multiplicative"])
        self.assertTrue(result["augmentation_unit_preserved"])

    def test_wrong_bidegree_and_grade_overflow_fail_closed(self):
        with self.assertRaises(ValueError):
            R.monomial_grade((1, 0, 0, 0, 0, 0, 0))
        with self.assertRaises(ValueError):
            R.source_product((4, 0, 4, 0, 0, 0, 0), (3, 0, 3, 0, 0, 0, 0))
        for bad in (True, 1.0, -1, 7):
            with self.assertRaises(ValueError):
                R.old_basis(bad)

    def test_old_literal_basis_agrees_with_frozen_source(self):
        _, finite = R.source()
        for grade in range(7):
            old = finite.primitive_c2(grade)
            row = R.map_control(grade)
            self.assertEqual(row["boundary_dimension"], old["after_dimension"])
            self.assertEqual(row["nearby_invariant_dimension"], old["before_dimension"])

    def test_new_point_zero_old_cokernel_does_not_fix_generization(self):
        _, finite = R.source()
        zero = finite.primitive_zero(2)
        self.assertEqual(zero["cokernel_dimension"], 0)
        self.assertEqual(zero["common_class_traces_e_s_c"][0], 20)
        self.assertGreater(zero["common_class_traces_e_s_c"][0], 0)

    def test_infinity_residual_action_is_retained(self):
        _, finite = R.source()
        inf = finite.primitive_infinity(4)
        self.assertGreater(inf["after_dimension"], inf["after_residual_trace"])
        determinant = R.residual_determinant(
            inf["after_dimension"], inf["after_residual_trace"], 1, 1
        )
        squared = R.residual_determinant(
            inf["after_dimension"], inf["after_residual_trace"], 1, 2
        )
        self.assertEqual(determinant["power_traces"][1], inf["after_dimension"])
        self.assertEqual(squared["power_traces"][0], inf["after_dimension"])


class FrobeniusShadowTests(unittest.TestCase):
    def test_zero_first_trace_does_not_kill_determinant(self):
        result = R.residual_determinant(2, 0, 1, 1)
        self.assertEqual(result["power_traces"][:3], [0, 2, 0])
        self.assertEqual(result["determinant_prefix"][:3], [1, 0, -1])

    def test_actual_standard_cycle_determinant(self):
        result = R.determinant_control([2, 0, -1], "c")
        self.assertEqual(result["determinant_prefix"][:4], [1, 1, 1, 0])
        self.assertEqual(result["power_traces"][:3], [-1, -1, 2])

    def test_third_frobenius_power_recovers_cycle_identity(self):
        result = R.determinant_control([2, 0, -1], "c", 1, 3)
        self.assertEqual(result["powered_class"], "e")
        self.assertEqual(result["determinant_prefix"][:3], [1, -2, 1])

    def test_quadratic_twist_changes_odd_newton_traces(self):
        positive = R.determinant_control([2, 0, -1], "c", 1)
        negative = R.determinant_control([2, 0, -1], "c", -1)
        for index, (a, b) in enumerate(
            zip(positive["power_traces"], negative["power_traces"], strict=True), 1
        ):
            self.assertEqual(b, (-1) ** index * a)
        self.assertEqual(negative["determinant_prefix"][:3], [1, -1, 1])

    def test_closed_point_splitting_keeps_power_and_degree(self):
        self.assertEqual(
            R.closed_point_base_change(4, 6),
            {
                "old_degree": 4,
                "extension_degree": 6,
                "new_closed_points": 2,
                "new_degree": 2,
                "frobenius_power": 3,
            },
        )
        self.assertEqual(R.closed_point_base_change(3, 2)["frobenius_power"], 2)
        self.assertEqual(R.closed_point_base_change(2, 2)["new_closed_points"], 2)

    def test_twist_must_be_powered_under_constant_extension(self):
        split = R.closed_point_base_change(3, 2)
        powered = split["frobenius_power"]
        actual = R.determinant_control([2, 0, -1], "c", (-1) ** powered, powered)
        wrong = R.determinant_control([2, 0, -1], "c", -1, powered)
        self.assertNotEqual(actual["determinant_prefix"], wrong["determinant_prefix"])

    def test_nonrepresentation_character_is_rejected(self):
        with self.assertRaises(ValueError):
            R.determinant_control([1, 1, 0], "c")
        with self.assertRaises(ValueError):
            R.residual_determinant(3, 0, 1, 1)
        with self.assertRaises(ValueError):
            R.newton_determinant([0, 1], 2)

    def test_caps_types_and_class_names(self):
        for bad in (True, 1.0, 0, 13):
            with self.assertRaises(ValueError):
                R.closed_point_base_change(bad, 2)
        with self.assertRaises(ValueError):
            R.determinant_control([2, 0, -1], "unknown")
        with self.assertRaises(ValueError):
            R.determinant_control([2, 0, -1], "c", True)


class AuthenticationTests(unittest.TestCase):
    def test_authentication_precedes_import(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("blocked")),
            patch.object(R.importlib.util, "spec_from_file_location") as imported,
        ):
            with self.assertRaises(ValueError):
                R.source()
            imported.assert_not_called()

    def test_wrong_git_blob_rejected_before_source_read(self):
        pins = {"bad": {"freeze": "known", "path": "absent", "blob": "expected"}}
        with (
            patch.object(R, "PINS", pins),
            patch.object(R.subprocess, "check_output", return_value="wrong\n"),
            self.assertRaises(ValueError),
        ):
            R.authenticate()

    def test_json_numeric_and_container_counterfeits(self):
        for value in (True, 1.0, "1"):
            self.assertFalse(R.strict_equal({"n": 1}, {"n": value}))
        self.assertFalse(R.strict_equal([1], (1,)))
        self.assertFalse(R.strict_equal({1: "x"}, {"1": "x"}))

    def test_nonfinite_json_fails_closed(self):
        for value in (float("nan"), float("inf")):
            self.assertFalse(R.strict_equal([value], [value]))

    def test_payload_checker_rejects_same_python_numeric_value(self):
        good = {"rank": 0, "unit": 1, "source_fixed": True}
        for key, value in (("rank", False), ("unit", 1.0), ("source_fixed", 1)):
            bad = copy.deepcopy(good)
            bad[key] = value
            with (
                patch.object(R, "build_payload", return_value=good),
                self.assertRaises(ValueError),
            ):
                R.check_payload(bad)

    def test_frozen_fixture_and_real_source_discriminator(self):
        data = json.loads(R.FIXTURE.read_bytes())
        R.check_payload(data)
        row = data["old_C2_maps"][2]
        self.assertEqual(row["original_generization_rank"], 3)
        self.assertEqual(row["counterfeit_generization_rank"], 0)
        self.assertEqual(
            data["new_zero_maps"][2]["old_after_before_defect_dimension"], 0
        )


if __name__ == "__main__":
    unittest.main()
