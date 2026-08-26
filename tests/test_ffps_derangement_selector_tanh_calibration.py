from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_derangement_selector_tanh_calibration.py"
)
SPEC = importlib.util.spec_from_file_location(
    "ffps_derangement_selector_tanh_calibration", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load tanh calibration module")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DerangementSelectorTanhCalibrationTest(unittest.TestCase):
    def test_exact_replay(self) -> None:
        payload = MODULE.run(check_sources=False)
        self.assertFalse(payload["scope"]["all_degree_weighted_l1_optimum_proved"])
        self.assertEqual(payload["theorem"]["full_cycle_dual_mass"], "2^(d-1)/d")
        self.assertEqual(len(payload["finite_replay"]), 9)

    def test_tanh_coefficients(self) -> None:
        self.assertEqual(MODULE.tanh_coefficient(1), Fraction(1))
        self.assertEqual(MODULE.tanh_coefficient(3), Fraction(-1, 3))
        self.assertEqual(MODULE.tanh_coefficient(5), Fraction(2, 15))
        self.assertEqual(MODULE.tanh_coefficient(7), Fraction(-17, 315))
        self.assertEqual(MODULE.tanh_coefficient(2), Fraction(0))

    def test_first_forbidden_residual(self) -> None:
        degree_six = MODULE.verify_degree(6)
        self.assertEqual(
            degree_six["forbidden_derangement_residual_types"], [[2, 2, 2]]
        )
        self.assertEqual(degree_six["transform_by_cycle_count"]["3"], "-16")

    def test_hook_saturation(self) -> None:
        degree = 10
        for depth in range(degree):
            hook = (degree - depth, *([1] * depth))
            self.assertEqual(
                MODULE.descent_parity_coefficient(hook),
                (-1) ** depth * MODULE.dimension(hook),
            )

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.verify_degree(1)
        with self.assertRaises(ValueError):
            MODULE.predicted_class_transform(6, 0)
        with self.assertRaises(ValueError):
            MODULE.character((3,), (2,))


if __name__ == "__main__":
    unittest.main()
