"""Complete original-kernel face coverage and the three-phase source boundary."""

import importlib.util
import json
import unittest
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour"
    / "boundary_layer_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_six_hour_boundary_layer", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeBoundaryLayerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scout = M.scout_module()
        cls.prototype = cls.scout.load_module(
            cls.scout.PROTOTYPE_COMMIT,
            cls.scout.PROTOTYPE_PATH,
            cls.scout.PROTOTYPE_BLOB,
        )
        cls.kernel = cls.prototype.load_module(
            cls.prototype.KERNEL_COMMIT,
            cls.prototype.KERNEL_PATH,
            cls.prototype.KERNEL_BLOB,
        )
        cls.discovery = json.loads(M.frozen(M.DISCOVERY, M.DISCOVERY_BLOB))

    def test_every_original_source_allocation_and_every_activation_face_is_present(
        self,
    ):
        expected = [
            list(support) for k in range(1, 5) for support in combinations(range(4), k)
        ]
        self.assertEqual(len(self.discovery["models"]), 3)
        for model in self.discovery["models"]:
            self.assertEqual(len(model["all16_source_records"]), 16)
            self.assertEqual(model["complete_same_band_ordered_pair_count"], 69)
            self.assertEqual(
                [row["support"] for row in model["all15_face_certificates"]], expected
            )

    def test_selected_faces_have_full_original_kkt_not_only_predicted_supports(self):
        self.assertEqual(
            [model["certified_support"] for model in self.discovery["models"]],
            [[1, 2], [1, 2, 3], [0, 1, 2, 3]],
        )
        for model in self.discovery["models"]:
            selected = [
                row
                for row in model["all15_face_certificates"]
                if row["full_KKT_certified"]
            ]
            self.assertEqual(len(selected), 1)
            self.assertEqual(selected[0]["support"], model["certified_support"])
            self.assertTrue(selected[0]["all_active_masses_strictly_positive"])
            self.assertTrue(
                selected[0][
                    "all_active_stationarity_equations_exact_by_Cramer_definition"
                ]
            )
            for row in selected[0]["all_inactive_KKT"]:
                self.assertGreater(F(row["half_gradient_slack"]["lower"]), 0)
            lower = sum(F(row["lower"]) for row in selected[0]["activation_intervals"])
            upper = sum(F(row["upper"]) for row in selected[0]["activation_intervals"])
            self.assertLessEqual(lower, 1)
            self.assertGreaterEqual(upper, 1)

    def test_original_physical_factor_and_kernel_are_retained(self):
        for model in self.discovery["models"]:
            self.assertEqual(
                F(model["physical_Gram_multiplier"]), F(1, 64 * model["K"])
            )
            self.assertFalse(model["quadratic_kernel_substitution"])
            self.assertTrue(model["failed_predictions_retained"])
            self.assertGreater(F(model["original_energy_interval"]["lower"]), 0)

    def test_first_three_primes_are_unchanged_and_every_fourth_is_a_fixed_window(self):
        prime_scout = self.scout.load_module(
            self.scout.ACQUISITION_COMMIT, self.scout.PRIME_PATH, self.scout.PRIME_BLOB
        )
        source = prime_scout.prime_module()
        acquisition = json.loads(
            self.scout.frozen_bytes(
                self.scout.ACQUISITION_COMMIT,
                self.scout.ACQUISITION_PATH,
                self.scout.ACQUISITION_BLOB,
            )
        )
        self.assertEqual(acquisition["fixed_prefix"], [99999931, 101999927, 104039917])
        self.assertLessEqual(acquisition["total_candidates"], 202)
        for multiplier, row in zip(
            prime_scout.MULTIPLIERS, acquisition["windows"], strict=True
        ):
            M.replay_equal(prime_scout.window(source, multiplier), row)
        for model in self.discovery["models"]:
            self.assertEqual(model["primes"][:3], acquisition["fixed_prefix"])
            self.assertTrue(all(source.prime(p) for p in model["primes"]))

    def test_dimensionless_kkt_has_central_one_endpoint_and_interior_phases(self):
        cases = [M.dimensionless_phase(z) for z in (F(1, 2), F(2), F(4))]
        self.assertEqual(
            [row["active_endpoint_indices"] for row in cases], [(), (1,), (0, 1)]
        )
        self.assertEqual(cases[1]["dimensionless_endpoint_masses"], ["0", "1"])
        self.assertEqual(cases[2]["dimensionless_endpoint_masses"], ["2/3", "10/3"])

    def test_threshold_equalities_are_explicitly_unassigned(self):
        for z in (-3, -1, 1, 3):
            result = M.dimensionless_phase(z)
            self.assertTrue(result["threshold_case"])
            self.assertFalse(result["exact_finite_zero_pattern_assigned"])

    def test_negative_outer_gap_reflects_the_complete_endpoint_kkt(self):
        for z in (F(1, 2), F(2), F(4)):
            positive, negative = M.dimensionless_phase(z), M.dimensionless_phase(-z)
            self.assertEqual(
                positive["dimensionless_endpoint_masses"],
                negative["dimensionless_endpoint_masses"][::-1],
            )
            self.assertEqual(
                positive["all_dimensionless_gradients"],
                negative["all_dimensionless_gradients"][::-1],
            )

    def test_full_source_second_moment_normalization_on_nonarithmetic_shapes(self):
        for a, b in ((1, 1), (2, 3), (1, 4), (5, 2)):
            result = M.second_moment_control(a, b)
            self.assertEqual(result["all69_ordered_source_pairs"], 69)
            self.assertEqual(
                result["endpoint_gradient_gaps"],
                [-4 * a * (a + b), 0, 0, -4 * a * (a + b)],
            )

    def test_outward_interval_operations_enclose_exact_rational_controls(self):
        a, b = self.scout.point(F(1, 3)), self.scout.point(F(2, 7))
        product = self.scout.times(a, b)
        self.assertLessEqual(product[0], F(2, 21))
        self.assertGreaterEqual(product[1], F(2, 21))
        recovered = self.scout.times(product, self.scout.inverse(b))
        self.assertLessEqual(recovered[0], F(1, 3))
        self.assertGreaterEqual(recovered[1], F(1, 3))

    def test_cramer_orientation_control_distinguishes_minimum_from_maximum(self):
        gram = tuple(
            tuple(self.kernel.expr(self.kernel.q(int(i == j))) for j in range(4))
            for i in range(4)
        )
        full = self.scout.face(self.kernel, gram, (0, 1, 2, 3))
        self.assertTrue(full["full_KKT_certified"])
        for row in full["activation_intervals"]:
            self.assertEqual(F(row["lower"]), F(1, 4))
            self.assertEqual(F(row["upper"]), F(1, 4))
        partial = self.scout.face(self.kernel, gram, (0, 1))
        self.assertFalse(partial["full_KKT_certified"])
        self.assertTrue(
            all(row["strict_negative"] for row in partial["all_inactive_KKT"])
        )

    def test_singular_control_is_retained_as_uncertified_without_dividing_by_zero(self):
        gram = tuple(
            tuple(self.kernel.expr(self.kernel.q(1)) for _ in range(4))
            for _ in range(4)
        )
        result = self.scout.face(self.kernel, gram, (0, 1, 2, 3))
        self.assertFalse(result["positive_tangent_metric_certified"])
        self.assertFalse(result["full_KKT_certified"])

    def test_exact_input_and_source_authentication_guards(self):
        for value in (True, 1.0, 9):
            with self.assertRaises(ValueError):
                M.dimensionless_phase(value)
        with self.assertRaises(ValueError):
            M.second_moment_control(True, 2)
        with self.assertRaises(ValueError):
            M.replay_equal({"faces": 15}, {"faces": 15.0})
        with patch.object(M, "SCOUT_BLOB", "0" * 40), self.assertRaises(ValueError):
            M.scout_module()


if __name__ == "__main__":
    unittest.main()
