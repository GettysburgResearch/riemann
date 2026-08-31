"""Actual convex-source optimization and independent certified-root controls."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction as F
from itertools import pairwise
from pathlib import Path

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour/native_synchronized_face_certificate.py"
)
SPEC = importlib.util.spec_from_file_location(
    "native_synchronized_minimum_under_test", PATH
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeSynchronizedMinimumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scout = M.scout_module()
        cls.data = json.loads(M.frozen("discovery"))

    def test_complete_original_physical_source_is_retained(self):
        self.assertEqual(len(self.data["all63_original_source_records"]), 63)
        self.assertEqual(len(self.data["all45_original_ratios"]), 45)

    def test_strict_original_metric_not_a_replacement_quadratic(self):
        self.assertGreater(F(self.data["strict_metric_determinant"]["lower"]), 0)
        self.assertEqual(len(self.data["exact_original_augmented_Gram"]), 3)
        self.assertTrue(
            all(len(row) == 3 for row in self.data["exact_original_augmented_Gram"])
        )

    def test_all_candidate_classes_and_every_cubic_root_retained(self):
        names = [row["name"] for row in self.data["all_candidates"]]
        self.assertTrue(
            {"interior", "lower_boundary", "endpoint_zero", "endpoint_one"}
            <= set(names)
        )
        self.assertEqual(
            sum(name.startswith("upper_boundary_root_") for name in names),
            len(self.data["all_upper_boundary_root_intervals"]),
        )

    def test_exactly_one_full_convex_body_kkt_point(self):
        selected = [
            row
            for row in self.data["all_candidates"]
            if row["full_convex_body_KKT_certified"]
        ]
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["name"], self.data["unique_certified_candidate"])
        self.assertEqual(selected[0]["name"], "endpoint_zero")
        self.assertGreater(F(selected[0]["energy"]["lower"]), 0)
        self.assertTrue(
            all(
                F(row["lower"]) > 5
                for row in selected[0]["details"]["endpoint_tangent_half_gradients"]
            )
        )

    def test_root_isolation_respects_fixed_caps(self):
        self.assertLessEqual(self.data["root_isolation_nodes"], 1024)
        poly = tuple(
            tuple(F(row[side]) for side in ("lower", "upper"))
            for row in self.data["upper_boundary_derivative_coefficients"]
        )
        for x in (0, 1):
            self.assertGreater(
                self.scout.polynomial_value(poly, self.scout.point(x))[0], 0
            )
        for row in self.data["all_upper_boundary_root_intervals"]:
            a, b = F(row["lower"]), F(row["upper"])
            self.assertTrue(0 <= a <= b <= 1)
            self.assertLessEqual(b - a, F(1, 2**64))

    def test_all_declared_source_comparisons_are_retained(self):
        self.assertEqual(
            [row["name"] for row in self.data["all_declared_comparisons"]],
            ["diagonal", "w_equals_s_squared", "fixed_joint_quadratic"],
        )
        self.assertTrue(
            all(
                row["all_comparison_signs_retained"]
                for row in self.data["all_declared_comparisons"]
            )
        )

    def test_fixed_rational_witness_is_an_actual_feasible_monotone_source_path(self):
        row = self.data["fixed_rational_actual_path"]
        d, e, mixture = F(row["D"]), F(row["E"]), F(row["mixture"])
        self.assertTrue(
            0 <= d <= 1 and d / 2 <= e <= d - d * d / 2 and 0 <= mixture <= 1
        )
        points = [tuple(map(F, p)) for p in row["five_equal_time_path_vertices"]]
        self.assertEqual(points[0], (0, 0, 0))
        self.assertEqual(points[-1], (1, 1, 1))
        for start, end in pairwise(points):
            self.assertTrue(all(a <= b for a, b in zip(start, end, strict=True)))
        self.assertEqual(len(row["complete_original_source"]), 63)
        self.assertEqual(len(row["complete_physical_rational_ratio_image"]), 45)

    def test_independent_rational_sturm_controls(self):
        controls = M.root_controls(self.scout)
        self.assertEqual([len(row["known_roots"]) for row in controls], [3, 2, 1, 0])
        refused = M.retained_symmetric_guard(self.scout)
        self.assertEqual(refused["known_roots"], ["1/4", "1/2", "3/4"])
        self.assertEqual(refused["status"], "retained_uncertified_dyadic_control")
        self.assertIs(refused["frozen_scout_changed"], False)

    def test_multiple_root_guard_is_not_silently_ignored(self):
        poly = tuple(self.scout.point(x) for x in (F(1, 4), F(-1), F(1)))
        with self.assertRaises(ValueError):
            self.scout.sturm_sequence(poly)

    def test_curved_boundary_polynomial_has_correct_source_factor(self):
        g00, g01, g11, b0, b1 = F(2), F(1, 3), F(3), F(-1), F(-2)
        coefficients = (
            2 * (b0 + b1),
            2 * (g00 + 2 * g01 + g11 - b1),
            -3 * (g01 + g11),
            g11,
        )
        for d in (F(1, 5), F(2, 3), F(4, 5)):
            e = d - d * d / 2
            tangent = 2 * (
                (b0 + g00 * d + g01 * e) + (1 - d) * (b1 + g01 * d + g11 * e)
            )
            self.assertEqual(sum(c * d**i for i, c in enumerate(coefficients)), tangent)

    def test_actual_subclass_scope_does_not_claim_all_path_or_diagonal_optimality(self):
        for key in (
            "full_all_path_optimum_claimed",
            "literal_site_diagonal_minimum_claimed",
            "full_gamma_identified",
        ):
            self.assertIs(self.data[key], False)

    def test_exact_input_and_typed_artifact_guards(self):
        for wrong in (True, 0.5):
            with self.assertRaises(ValueError):
                self.scout.point(wrong)
        for wrong in (True, 1.0):
            with self.assertRaises(ValueError):
                M.strict_equal({"x": wrong}, {"x": 1})
        candidate = copy.deepcopy(self.data)
        candidate["unique_certified_candidate"] = "fabricated"
        with self.assertRaises(ValueError):
            M.strict_equal(candidate, self.data)


if __name__ == "__main__":
    unittest.main()
