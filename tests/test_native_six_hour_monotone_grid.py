"""Complete native grid coverage, signed scoring, source replay and refinement."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour/native_monotone_grid_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_complete_grid_certificate", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeMonotoneGridTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scout = M.frozen("scout", True)
        cls.calibration = json.loads(M.frozen("calibration"))
        cls.heldout = json.loads(M.frozen("heldout"))
        cls.panels = cls.calibration["panels"] + cls.heldout["panels"]

    def test_exact_source_authentication_precedes_import(self):
        with (
            patch.object(
                M.subprocess, "check_output", side_effect=ValueError("source changed")
            ),
            patch("builtins.compile") as compiler,
        ):
            with self.assertRaisesRegex(ValueError, "source changed"):
                M.frozen("scout", True)
            compiler.assert_not_called()

    def test_complete_calibration_and_heldout_counts(self):
        self.assertEqual(
            [(row["N"], row["path_count"]) for row in self.panels],
            [(2, 90), (3, 1680), (4, 34650)],
        )
        for row in self.panels:
            self.assertEqual(row["path_count"], row["expected_path_count"])
            self.assertEqual(len(row["complete_word_coordinate_score_sha256"]), 64)

    def test_heldout_has_same_frozen_executable_and_metric(self):
        self.assertEqual(
            self.calibration["owned_sha256_lf"], self.heldout["owned_sha256_lf"]
        )
        self.assertEqual(
            self.calibration["quantized_original_metric"],
            self.heldout["quantized_original_metric"],
        )
        self.assertEqual(F(self.heldout["dyadic_coefficient_denominator"]), 2**512)
        self.assertIs(self.heldout["floating_selection_used"], False)

    def test_every_unique_winner_keeps_all63_and45(self):
        for panel in self.panels:
            self.assertEqual(panel["surviving_coordinate_class_count"], 1)
            self.assertEqual(panel["surviving_word_count"], 1)
            row = panel["all_surviving_classes"][0]
            self.assertEqual(row["first_word"], "23" * panel["N"] + "5" * panel["N"])
            self.assertEqual(len(row["complete63_literal_source"]), 63)
            self.assertEqual(len(row["complete45_rational_ratio_image"]), 45)

    def test_exact_score_intervals_and_original_energy_order(self):
        energies = []
        for panel in self.panels:
            self.assertEqual(panel["minimum_status"], "exact_all_surviving_classes_tie")
            row = panel["all_surviving_classes"][0]
            denominator = int(panel["integer_score_denominator"])
            self.assertLessEqual(
                F(row["lower_score"], denominator), F(row["upper_score"], denominator)
            )
            energies.append(
                tuple(
                    F(panel["minimum_energy_interval"][side])
                    for side in ("lower", "upper")
                )
            )
        self.assertGreater(energies[0][0], energies[1][1])
        self.assertGreater(energies[1][0], energies[2][1])

    def test_zero_metric_retains_every_tied_word(self):
        zero = {
            "constant": (0, 0),
            "cross": [(0, 0)] * 6,
            "gram": [[(0, 0)] * 6 for _ in range(6)],
        }
        result = self.scout.enumerate_paths(2, zero)
        self.assertEqual(result["count"], 90)
        self.assertEqual(
            sum(x["word_multiplicity"] for x in result["candidates"].values()), 90
        )
        self.assertEqual(result["best_upper"], 0)

    def test_signed_metric_and_exact_axis_controls(self):
        controls = M.synthetic_controls(self.scout)
        self.assertGreater(controls["signed_quadratic_A_half_word_count"], 0)
        self.assertEqual(len(controls["six_exact_axis_moments"]), 6)
        self.assertIs(controls["synthetic_controls_claimed_native_metrics"], False)

    def test_refinement_preserves_the_actual_source_coordinates(self):
        coarse, _ = self.scout.word_path(2, "232355")
        fine, _ = self.scout.word_path(4, "223322335555")
        self.assertEqual(fine, tuple(8 * x for x in coarse))

    def test_alternating_formula_is_not_promoted_to_all_resolution_optimality(self):
        for n in range(1, 5):
            numerators, _ = self.scout.word_path(n, "23" * n + "5" * n)
            values = tuple(F(x, 2 * n**3) for x in numerators)
            self.assertEqual(
                values,
                (
                    F(n - 1, 2 * n),
                    F((n - 1) * (4 * n + 1), 12 * n * n),
                    F((n - 1) * (2 * n - 1), 12 * n * n),
                    0,
                    0,
                    0,
                ),
            )
        row = next(
            row
            for row in self.panels[-1]["all_declared_comparisons"]
            if row["name"] == "exact_synchronized_face_minimum"
        )
        self.assertGreater(F(row["control_minus_first_candidate"]["lower"]), 0)

    def test_original_norm_convergence_constants_remain_explicit(self):
        constants = self.calibration["convergence_constants"]
        self.assertEqual(
            F(constants["energy_rate_constant_upper"]),
            2
            * F(constants["C_source_upper"])
            * F(constants["uniform_field_norm_upper"]),
        )
        for panel in self.panels:
            bounds = panel["all_path_infimum_bounds"]
            self.assertLessEqual(F(bounds["lower"]), F(bounds["upper"]))
            self.assertIs(panel["all_path_optimizer_claimed"], False)

    def test_original_measure_and_full_source_scope(self):
        for payload in (self.calibration, self.heldout):
            self.assertEqual(payload["literal_source_measure"], "2ds")
            self.assertIs(payload["original_Mellin_measure"], True)
            self.assertIs(payload["full_gamma_source_identified"], False)
            self.assertEqual(len(payload["complete63_record_order"]), 63)
            self.assertEqual(len(payload["complete45_ratio_order"]), 45)

    def test_typed_grid_and_complete_artifact_guards(self):
        for wrong in (True, 2.0, 0, 5):
            with self.assertRaises(ValueError):
                self.scout.valid_grid(wrong)
        for wrong in ("235", "222355", "23235x"):
            with self.assertRaises(ValueError):
                self.scout.word_path(2, wrong)
        for wrong in (True, 1.0):
            with self.assertRaises(ValueError):
                M.strict_equal({"rank": 1}, {"rank": wrong})
        changed = copy.deepcopy(self.heldout)
        changed["panels"][0]["path_count"] -= 1
        with self.assertRaises(ValueError):
            M.strict_equal(changed, self.heldout)


if __name__ == "__main__":
    unittest.main()
