from __future__ import annotations

import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_selector_young_lattice_propagation_obstruction.py"
)
SPEC = importlib.util.spec_from_file_location(
    "ffps_selector_young_lattice_propagation_obstruction", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load selector propagation module")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SelectorYoungLatticePropagationObstructionTest(unittest.TestCase):
    def test_exact_replay(self) -> None:
        payload = MODULE.run(check_sources=False)
        self.assertFalse(payload["scope"]["constructive_lift_proved"])
        self.assertFalse(payload["scope"]["all_degree_optimum_proved"])
        self.assertFalse(payload["scope"]["linear_programming_used"])
        self.assertEqual(payload["scope"]["maximum_replay_degree"], 256)
        self.assertEqual(len(payload["panels"]), 8)

    def test_first_potential_and_degree_eight_depth(self) -> None:
        self.assertEqual(MODULE.first_two_row_potential(8), Fraction(24))
        panel = MODULE.verify_degree(8)
        self.assertEqual(panel["forced_depth"], 2)
        self.assertEqual(MODULE.signed_forced_lower_bound(8, 2), Fraction(4))

    def test_degree_sixteen_penetrates_four_layers(self) -> None:
        panel = MODULE.verify_degree(16)
        self.assertEqual(panel["forced_depth"], 4)
        self.assertEqual(MODULE.signed_forced_lower_bound(16, 4), Fraction(2276))

    def test_exact_dimension_telescope(self) -> None:
        for degree in (8, 10, 16, 32, 64):
            running = MODULE.first_two_row_potential(degree)
            for index in range(1, (degree - 1) // 2 + 1):
                if index > 1:
                    running -= MODULE.two_row_dimension(degree, index)
                self.assertEqual(
                    running,
                    MODULE.signed_forced_lower_bound(degree, index),
                )
                self.assertEqual(
                    MODULE.two_row_dimension(degree, index),
                    math.comb(degree, index) - math.comb(degree, index - 1),
                )

    def test_forced_depth_is_single_threshold(self) -> None:
        for degree in range(5, 65):
            depth = MODULE.forced_depth(degree)
            self.assertGreater(MODULE.signed_forced_lower_bound(degree, depth), 0)
            maximum = (degree - 1) // 2
            if depth < maximum:
                self.assertLessEqual(
                    MODULE.signed_forced_lower_bound(degree, depth + 1), 0
                )

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.verify_degree(4)
        with self.assertRaises(ValueError):
            MODULE.verify_degree(True)
        with self.assertRaises(ValueError):
            MODULE.two_row_dimension(8, 0)
        with self.assertRaises(ValueError):
            MODULE.hook_predecessor_potential(8, 7)


if __name__ == "__main__":
    unittest.main()
