from __future__ import annotations

import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_second_boundary_zero_density.py"
)
SPEC = importlib.util.spec_from_file_location("second_density", MODULE_PATH)
assert SPEC and SPEC.loader
second_density = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(second_density)


class SecondBoundaryZeroDensityTest(unittest.TestCase):
    def test_rademacher_multiplicity(self) -> None:
        self.assertEqual(second_density.rademacher_multiplicity(4, 0), 6)
        self.assertEqual(second_density.rademacher_multiplicity(4, 2), 4)
        self.assertEqual(second_density.rademacher_multiplicity(4, 1), 0)
        self.assertEqual(second_density.rademacher_multiplicity(4, 6), 0)

    def test_exact_small_q_probabilities(self) -> None:
        self.assertEqual(
            second_density.d3_local_zero_probability(3), Fraction(1639, 8192)
        )
        for q in second_density.Q_PANELS:
            probability = second_density.d3_local_zero_probability(q)
            self.assertGreater(probability, 0)
            self.assertLess(probability, 1)

    def test_profile_weight_tends_to_claimed_scale(self) -> None:
        values = [
            float(h * h * second_density.leading_profile_weight(h))
            for h in (25, 50, 100, 200)
        ]
        target = (1 + math.log(2)) / 3
        self.assertLess(abs(values[-1] - target), 0.005)
        self.assertLess(abs(values[-1] - target), abs(values[0] - target))

    def test_chaos_moments(self) -> None:
        self.assertEqual(second_density.chaos_even_moment(2), 1)
        self.assertEqual(second_density.chaos_even_moment(4), 10)
        self.assertEqual(second_density.chaos_even_moment(6), 760)

    def test_invalid_and_resource_caps(self) -> None:
        for q in (True, 2, 15):
            with self.assertRaises(ValueError):
                second_density.d3_local_zero_probability(q)
        with self.assertRaises(ValueError):
            second_density.leading_profile_weight(4)
        with self.assertRaises(ValueError):
            second_density.chaos_even_moment(8)
        caps = second_density.run()["resource_caps"]
        self.assertEqual(caps["residue_classes_enumerated"], 0)
        self.assertEqual(caps["polynomials_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
