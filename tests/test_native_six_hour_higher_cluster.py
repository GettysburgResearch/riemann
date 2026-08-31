"""Full source distance matrices, KKT faces, and physical normalization."""

import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "native-six-hour"
    / "higher_native_cluster_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_six_hour_higher_cluster", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeHigherClusterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = M.scout_module()
        cls.models = {shape: cls.module.discover(shape) for shape in cls.module.PANELS}

    def test_complete_arity_six_source_and_every_active_face(self):
        model = self.models[(0, 1, 2, 3, 4, 5)]
        self.assertEqual(model["all_source_subset_count"], 64)
        self.assertEqual(
            model["complete_same_cardinality_ordered_pair_count_excluding_empty"], 923
        )
        self.assertEqual(model["all_active_supports_checked"], 63)

    def test_four_source_symbolic_atlas_equals_independent_subset_matrix(self):
        for shape in self.module.PANELS:
            if len(shape) == 4:
                matrix, _, _ = self.module.matrices(shape)
                self.assertEqual(matrix, M.atlas_matrix(shape))

    def test_middle_gap_changes_energy_without_changing_activation(self):
        a, b = self.models[(0, 1, 2, 4)], self.models[(0, 1, 4, 6)]
        self.assertEqual(a["unique_activation"], b["unique_activation"])
        self.assertEqual(a["unique_activation"], ["1/18", "4/9", "7/18", "1/9"])
        self.assertNotEqual(a["exact_objective"], b["exact_objective"])

    def test_four_source_wall_and_reflection(self):
        self.assertEqual(
            self.models[(0, 1, 2, 3)]["unique_activation"], ["0", "1/2", "1/2", "0"]
        )
        self.assertEqual(
            self.models[(0, 1, 2, 4)]["unique_activation"],
            self.models[(0, 2, 3, 4)]["unique_activation"][::-1],
        )

    def test_five_source_strict_face_and_independent_polynomial(self):
        matrix, _, _ = self.module.matrices((0, 1, 2, 3, 4))
        polynomial = M.symmetric_reduction(matrix, 5)
        self.assertEqual(
            polynomial["coefficients"], ["128", "8", "20", "-32", "-48", "-32"]
        )
        model = self.models[(0, 1, 2, 3, 4)]
        self.assertEqual(model["unique_activation"], ["0", "5/16", "3/8", "5/16", "0"])
        self.assertEqual(model["inactive_KKT_slacks"], ["7/4", "0", "0", "0", "7/4"])
        self.assertEqual(model["objective_gain"], "401/200")

    def test_six_source_zero_slacks_are_not_strict_complementarity(self):
        matrix, _, _ = self.module.matrices((0, 1, 2, 3, 4, 5))
        polynomial = M.symmetric_reduction(matrix, 6)
        self.assertEqual(
            polynomial["coefficients"], ["625", "-32", "0", "-32", "-32", "-24"]
        )
        model = self.models[(0, 1, 2, 3, 4, 5)]
        self.assertEqual(model["inactive_KKT_slacks"], ["8", "0", "0", "0", "0", "8"])
        self.assertEqual(model["objective_gain"], "70/9")

    def test_original_two_ds_amplitude_and_vandermonde_band_mass(self):
        self.assertEqual(M.source_constants(3)["constant_band_mass"], 6)
        self.assertEqual(M.source_constants(4)["constant_band_mass"], 20)
        self.assertEqual(M.source_constants(6)["constant_band_mass"], 252)
        self.assertEqual(
            M.source_constants(5)["leading_multiplier_before_A_epsilon_over_K"], "1/128"
        )

    def test_ordered_shapes_and_source_caps(self):
        for bad in ((0, 1, 1, 3), (0.0, 1, 2, 3), (0, 1, 2, 13)):
            with self.assertRaises(ValueError):
                M.atlas_matrix(bad)
        for bad in (True, 1, 33):
            with self.assertRaises(ValueError):
                M.source_constants(bad)

    def test_kkt_solution_really_dominates_uniform_on_every_panel(self):
        for model in self.models.values():
            self.assertGreaterEqual(F(model["objective_gain"]), 0)
            self.assertEqual(sum(F(q) for q in model["unique_activation"]), 1)
            self.assertTrue(all(F(x) >= 0 for x in model["inactive_KKT_slacks"]))

    def test_typed_json_and_frozen_executable_authentication(self):
        with self.assertRaises(ValueError):
            M.replay_equal({"arity": 4}, {"arity": 4.0})
        with patch.object(M, "SCOUT_BLOB", "0" * 40), self.assertRaises(ValueError):
            M.scout_module()


if __name__ == "__main__":
    unittest.main()
