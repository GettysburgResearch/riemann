"""Whole-source accessibility, source-face stability, and original-observation controls."""

import copy
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour/native_path_synchronization.py"
)
SPEC = importlib.util.spec_from_file_location("native_path_sync_under_test", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativePathSynchronizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = M.build()
        cls.occupation, cls.module, cls.data, cls.quadratic, cls.kernel = (
            M.source_modules()
        )

    def test_all_nine_profiles_retain_all_sixty_three_source_pairs(self):
        self.assertEqual(len(self.result["quadratic_profiles"]), 9)
        self.assertEqual(len(self.result["complete_ordered_records"]), 63)
        for row in self.result["quadratic_profiles"]:
            self.assertEqual(len(row["complete_source"]), 63)
            self.assertEqual(len(row["synchronized_source"]), 63)
            self.assertEqual(len(row["all_original_diagonals"]), 4)

    def test_five_open_monotone_witnesses_are_independent(self):
        for p in M.PARAMETERS[1:6]:
            self.assertTrue(all(-1 < x < 1 for x in p))
        self.assertEqual(
            abs(F(self.result["open_basis_determinant"])),
            2 * M.H**8 / (36 * 60 * 30 * 60),
        )

    def test_exact_quadratic_source_formula_uses_nonlinear_common_parameter(self):
        a, b, c = F(1, 4), F(-1, 4), F(1, 2)
        A, B, C, D, E, FF = M.moments((a, b, c))
        self.assertEqual(
            (A, D, FF),
            (F(1, 2) + (b - a) / 6, F(1, 2) + (c - a) / 6, F(1, 2) + (c - b) / 6),
        )
        self.assertEqual(C - 2 * B + F(1, 3), (b - a) ** 2 / 30)
        self.assertEqual(
            (b - a) * (60 * (E - F(1, 3)) - 5 * (c - a)),
            (c - a) * (60 * (B - F(1, 3)) - 5 * (b - a)),
        )

    def test_original_ratio_functionals_include_all_alias_weights(self):
        for row in self.result["quadratic_profiles"]:
            values = tuple(map(F, row["moments"]))
            self.assertEqual(F(row["physical_square"]), M.square(values))
            self.assertEqual(F(row["physical_cycle"]), F(1, 2))
        record = self.result["complete_ordered_records"]
        index = next(
            i for i, row in enumerate(record) if (row["n"], row["m"]) == (2, 4)
        )
        self.assertTrue(
            all(
                F(row["complete_source"][index]) == F(5, 16)
                for row in self.result["quadratic_profiles"]
            )
        )

    def test_synchronization_is_idempotent_on_the_source_chart(self):
        for row in self.result["quadratic_profiles"]:
            values = tuple(map(F, row["moments"]))
            sync = M.projection(values)
            self.assertEqual(M.projection(sync), sync)
            self.assertEqual(sync[3:5], values[3:5])
            self.assertEqual(M.square(sync), 0)

    def test_four_sharp_staircases_retain_observed_linear_term(self):
        self.assertEqual(len(self.result["sharp_staircases"]), 4)
        ratios = [(row["a"], row["b"]) for row in self.result["ratio_order"]]
        for row in self.result["sharp_staircases"]:
            delta = F(row["delta"])
            self.assertEqual(F(row["L"]), delta**3 / 3)
            self.assertEqual(F(row["F_minus_D"]), -delta)
            self.assertEqual(
                F(row["physical_rational_ratio_difference"][ratios.index((3, 5))]),
                -delta / 2,
            )

    def test_fifteen_controls_fill_both_boundaries_of_the_source_face(self):
        self.assertEqual(len(self.result["exposed_face_controls"]), 15)
        for row in self.result["exposed_face_controls"]:
            a, b, c, d, e, ff = map(F, row["moments"])
            self.assertEqual((a, b, c, ff), (F(1, 2), F(1, 3), F(1, 3), d))
            self.assertLessEqual(d / 2, e)
            self.assertLessEqual(e, d - d * d / 2)
            if F(row["mixture"]) == 0:
                self.assertEqual(e, d / 2)
            if F(row["mixture"]) == 1:
                self.assertEqual(e, d - d * d / 2)

    def test_actual_axis_sources_escape_quadratic_cycle_hyperplane(self):
        axes = {name: path for name, path, _ in self.occupation.path_panel(self.module)}
        cycles = []
        records = self.data["complete_ordered_records"]
        ratios = [(row["a"], row["b"]) for row in self.data["ratio_order"]]
        for name in ("axis_235", "axis_532"):
            vector = self.occupation.source_vector(self.module, axes[name], records)
            field = M.observed_field(self.module, self.kernel, vector, records, ratios)
            cycles.append(M.original_functionals(self.kernel, field)[1])
        self.assertEqual(cycles, [0, 1])

    def test_true_reparameterization_preserves_current_not_primitive_site_diagonal(
        self,
    ):
        base, common = (
            self.result["quadratic_profiles"][0],
            self.result["quadratic_profiles"][-1],
        )
        self.assertEqual(base["complete_source"], common["complete_source"])
        self.assertNotEqual(
            base["all_original_diagonals"]["primitive_2ds_site"],
            common["all_original_diagonals"]["primitive_2ds_site"],
        )

    def test_gram_constraint_rejects_false_source_moments(self):
        false = (F(1, 2), F(1, 2), F(1, 3), F(), F(), F())
        self.assertLess(M.gram_slack(false), 0)
        for row in self.result["quadratic_profiles"]:
            self.assertGreaterEqual(F(row["Gram_PSD_slack"]), 0)

    def test_all_original_metric_probes_retained_without_assumed_orthogonality(self):
        probes = self.result["all_eight_original_metric_orthogonality_probes"]
        self.assertEqual(len(probes), 8)
        if self.result["source_projection_is_orthogonal"] is False:
            self.assertTrue(any(row["certified_nonzero"] for row in probes))

    def test_same_coefficient_observation_does_not_claim_all_native_decoder(self):
        self.assertIs(
            self.result["finite_six_dimensional_source_observation_commutes"], True
        )
        for key in (
            "primitive_diagonal_isometry_claimed",
            "whole_affine_hyperplane_attainable_claimed",
            "full_post_renewal_gamma_identified",
        ):
            self.assertIs(self.result[key], False)

    def test_typed_artifact_and_whole_source_mutations_rejected(self):
        for wrong in (True, 1.0):
            with self.assertRaises(ValueError):
                M.strict_equal({"x": wrong}, {"x": 1})
        candidate = copy.deepcopy(self.result)
        candidate["quadratic_profiles"][0]["complete_source"][0] = "1"
        with self.assertRaises(ValueError):
            M.strict_equal(candidate, self.result)

    def test_exact_bounded_native_domains_reject_counterfeits(self):
        for value in (True, 0.5, F(1, 2**129)):
            with self.assertRaises(ValueError):
                M.exact(value)
        with self.assertRaises(ValueError):
            M.moments((0, 2, 0))
        with self.assertRaises(ValueError):
            M.staircase(F())
        with self.assertRaises(ValueError):
            M.face_path(F(1, 2), F(2))


if __name__ == "__main__":
    unittest.main()
