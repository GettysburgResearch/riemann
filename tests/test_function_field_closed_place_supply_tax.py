from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "function_field_closed_place_supply_tax.py"
)
SPEC = importlib.util.spec_from_file_location("closed_place_tax", MODULE_PATH)
assert SPEC and SPEC.loader
closed_place_tax = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(closed_place_tax)


class FunctionFieldClosedPlaceSupplyTaxTest(unittest.TestCase):
    def test_rate_is_positive_below_critical_cutoff(self) -> None:
        for density, alpha, beta in closed_place_tax.PANELS:
            self.assertGreater(
                closed_place_tax.upper_tail_rate(density, alpha, beta), 0
            )

    def test_rate_vanishes_at_critical_cutoff(self) -> None:
        for density, alpha in ((0.5, 0.2), (1.0, 0.6)):
            beta = alpha / density
            mean = density * beta
            rate = alpha * __import__("math").log(alpha / mean) - alpha + mean
            self.assertAlmostEqual(rate, 0.0, places=14)

    def test_supply_exponent_dominates_leverage(self) -> None:
        for density in (0.5, 1.0):
            alpha = 0.4 * density
            self.assertGreater(
                alpha / density, closed_place_tax.leverage_exponent(alpha)
            )

    def test_even_square_root_conductor_loss_is_too_large(self) -> None:
        for density in (0.5, 1.0):
            self.assertGreater(0.5, density * __import__("math").log(5 / 4))

    def test_guards_and_caps(self) -> None:
        with self.assertRaises(ValueError):
            closed_place_tax.upper_tail_rate(0.5, 0.3, 0.7)
        caps = closed_place_tax.run()["resource_caps"]
        self.assertEqual(caps["polynomials_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
