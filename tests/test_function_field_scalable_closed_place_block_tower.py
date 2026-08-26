from __future__ import annotations

import importlib.util
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
    / "function_field_scalable_closed_place_block_tower.py"
)
SPEC = importlib.util.spec_from_file_location("closed_place_tower", MODULE_PATH)
assert SPEC and SPEC.loader
closed_place_tower = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(closed_place_tower)


class FunctionFieldScalableClosedPlaceBlockTowerTest(unittest.TestCase):
    def test_orientation_degree_parity(self) -> None:
        self.assertEqual(
            [d for d in range(1, 9) if closed_place_tower.eligible_degree(3, d)],
            [2, 4, 6, 8],
        )
        self.assertEqual(
            [d for d in range(1, 9) if closed_place_tower.eligible_degree(5, d)],
            list(range(1, 9)),
        )

    def test_density_values(self) -> None:
        self.assertEqual(closed_place_tower.eligible_density(3), Fraction(1, 2))
        self.assertEqual(closed_place_tower.eligible_density(5), Fraction(1))

    def test_balanced_frontiers_scale_with_density(self) -> None:
        alpha_half = closed_place_tower.balanced_alpha(0.5)
        alpha_one = closed_place_tower.balanced_alpha(1.0)
        self.assertAlmostEqual(alpha_one, 2 * alpha_half, places=11)
        self.assertAlmostEqual(
            closed_place_tower.density_exponent(alpha_one, 1.0),
            2 * closed_place_tower.density_exponent(alpha_half, 0.5),
            places=11,
        )

    def test_every_sample_block_contracts(self) -> None:
        for panel in closed_place_tower.run()["panels"]:
            self.assertLess(Fraction(panel["sample_block_leverage"]), Fraction(4, 5))

    def test_guards_and_caps(self) -> None:
        with self.assertRaises(ValueError):
            closed_place_tower.eligible_degree(2, 1)
        with self.assertRaises(ValueError):
            closed_place_tower.eligible_degree(15, 2)
        self.assertTrue(closed_place_tower.is_prime_power(9))
        self.assertFalse(closed_place_tower.is_prime_power(15))
        with self.assertRaises(ValueError):
            closed_place_tower.density_exponent(0.6, 0.5)
        caps = closed_place_tower.run()["resource_caps"]
        self.assertEqual(caps["polynomials_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
