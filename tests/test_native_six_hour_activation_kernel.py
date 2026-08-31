"""Original kernel, exact source paths and certified nonuniform minimizers."""

import importlib.util
import json
import unittest
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "native-six-hour"
    / "native_activation_certificate.py"
)
SPEC = importlib.util.spec_from_file_location(
    "native_six_hour_activation_certificate", PATH
)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeActivationKernelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.K = M.kernel_module()
        cls.primary = M.model_certificate(cls.K, (3, 5, 7), (399, 296, 305))
        cls.control = M.model_certificate(cls.K, (2, 3, 5), (396, 290, 314))
        cls.separated = M.model_certificate(cls.K, (3, 11, 101), (333, 333, 333))

    def test_independent_original_kernel_anchors(self):
        K = self.K
        self.assertEqual(
            K.gamma_square_ratio(F(1)), K.expr(K.q(-288), {F(2): K.q(384, 128)})
        )
        self.assertEqual(
            K.gamma_square_ratio(F(2)), K.expr(K.q(-48), {F(2): K.q(0, 64)})
        )
        self.assertGreater(K.ei(K.gamma_square_ratio(F(1)))[0], 100)

    def test_exact_kernel_symmetry_support_and_nonzero_overlap(self):
        K = self.K
        for ratio in (F(3, 2), F(5, 3), F(7, 5)):
            self.assertEqual(
                K.gamma_square_ratio(ratio), K.gamma_square_ratio(1 / ratio)
            )
        self.assertEqual(K.gamma_square_ratio(F(3)), K.expr())
        self.assertNotEqual(K.gamma_square_ratio(F(2)), K.expr())

    def test_rational_log_and_square_root_brackets(self):
        lower, upper = self.K.log_interval(F(2))
        self.assertGreater(lower, F(693147, 1000000))
        self.assertLess(upper, F(693148, 1000000))
        self.assertEqual(self.K.log_interval(F(1, 2)), (-upper, -lower))
        root = self.K.qi(self.K.q(0, 1))
        self.assertLess(root[0] ** 2, 2)
        self.assertGreater(root[1] ** 2, 2)

    def test_complete_eight_mode_Gram_and_even_odd_orthogonality(self):
        for primes in ((3, 5, 7), (2, 3, 5), (3, 11, 101)):
            row = self.K.kernel_gram(primes)
            self.assertEqual(len(set(row["divisors"])), 8)
            self.assertTrue(
                all(value == self.K.expr() for value in row["even_odd_cross"])
            )
            self.assertEqual(row["gram"][0][1], row["gram"][1][0])

    def test_primary_unique_interior_optimizer_is_not_uniform(self):
        q = self.primary["unique_interior_activation"]
        self.assertGreater(F(q[0]["lower"]), F(3992, 10000))
        self.assertLess(F(q[1]["upper"]), F(2961, 10000))
        self.assertGreater(F(q[2]["lower"]), F(3047, 10000))
        gradients = self.primary["uniform_gradient"]
        self.assertLess(F(gradients[0]["upper"]), F(gradients[1]["lower"]))

    def test_independent_crowded_control_certifies_nonuniformity(self):
        q = self.control["unique_interior_activation"]
        self.assertGreater(F(q[0]["lower"]), F(3959, 10000))
        self.assertLess(F(q[1]["upper"]), F(2906, 10000))
        self.assertGreater(
            F(self.control["uniform_minus_simple_K_scaled_interval"]["lower"]),
            F(9, 100),
        )

    def test_original_physical_energy_normalization_and_simple_source_path(self):
        self.assertEqual(self.primary["postdiscovery_simple_integer_powers"], (4, 3, 3))
        self.assertGreater(
            F(self.primary["uniform_minus_simple_K_scaled_interval"]["lower"]), F(2, 25)
        )
        self.assertGreater(
            F(self.primary["physical_improvement_interval"]["lower"]), F(2, 2625)
        )
        self.assertTrue(
            self.primary["source_endpoint_and_signed_Hankel_current_unchanged"]
        )
        self.assertFalse(
            self.primary["arbitrary_independent_arithmetic_coefficients_fitted"]
        )

    def test_separated_held_out_control_has_exact_uniform_Gram(self):
        K = self.K
        model = K.kernel_gram((3, 11, 101))
        diagonal = K.es(K.gamma_square_ratio(F(1)), F(1, 8))
        for i in range(3):
            for j in range(3):
                self.assertEqual(model["gram"][i][j], diagonal if i == j else K.expr())
        for row in self.separated["unique_interior_activation"]:
            self.assertLessEqual(F(row["lower"]), F(1, 3))
            self.assertGreaterEqual(F(row["upper"]), F(1, 3))

    def test_actual_power_schedule_coefficients_keep_root_and_complete_endpoint(self):
        q = (F(2, 5), F(3, 10), F(3, 10))
        coefficients = [
            2
            * F(-1, 2) ** 3
            * sum((q[j] for j, value in enumerate(flags) if value), F())
            for flags in product((0, 1), repeat=3)
        ]
        self.assertEqual(coefficients[0], 0)
        self.assertEqual(coefficients[-1], F(-1, 4))
        self.assertEqual(sum(coefficients), -1)
        for a, b in zip(coefficients, reversed(coefficients), strict=True):
            self.assertEqual(a + b, F(-1, 4))

    def test_original_discovery_and_preregistration_are_authenticated(self):
        original = json.loads(
            M.frozen_bytes(M.KERNEL_COMMIT, M.DISCOVERY_PATH, M.DISCOVERY_BLOB)
        )
        self.assertEqual(
            original["models"][0]["candidate_integer_power_schedule"], [399, 296, 305]
        )
        self.assertIn(
            b"before the first run",
            M.frozen_bytes(
                M.KERNEL_COMMIT, M.PREREGISTRATION_PATH, M.PREREGISTRATION_BLOB
            ),
        )
        with (
            patch.object(M, "KERNEL_BLOB", "0" * 40),
            self.assertRaisesRegex(ValueError, "authentication"),
        ):
            M.kernel_module()

    def test_certified_positive_Gram_and_no_diagonal_surrogate(self):
        model = self.K.kernel_gram((3, 5, 7))
        intervals, determinant, _, _ = M.optimizer(self.K, model["gram"])
        self.assertGreater(intervals[0][0][0], 0)
        self.assertGreater(determinant[0], 0)
        self.assertLess(intervals[0][1][1], 0)
        self.assertGreater(intervals[0][2][0], 0)

    def test_hostile_numeric_types_caps_and_typed_replay(self):
        for bad in (True, 1.0, -1, 0):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                self.K.gamma_square_ratio(bad)
        with self.assertRaises(ValueError):
            self.K.log_interval(F(2), 65)
        with self.assertRaises(ValueError):
            M.quadratic_expression(
                self.K, self.K.kernel_gram((3, 5, 7))["gram"], (F(1), F(1), F(1))
            )
        for bad in (True, 1.0):
            with (
                self.subTest(candidate=bad),
                self.assertRaisesRegex(ValueError, "typed canonical"),
            ):
                M.replay_equal({"count": bad}, {"count": 1})


if __name__ == "__main__":
    unittest.main()
