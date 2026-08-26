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
    / "ffps_boolean_half_source_diagonal_gain.py"
)
SPEC = importlib.util.spec_from_file_location("half_source_gain", MODULE_PATH)
assert SPEC and SPEC.loader
half_source_gain = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(half_source_gain)


class FfpsBooleanHalfSourceDiagonalGainTest(unittest.TestCase):
    def test_exact_half_source_recombination(self) -> None:
        for panel in half_source_gain.identity_panels():
            self.assertLessEqual(
                Fraction(panel["maximum_absolute_coefficient"]),
                Fraction(panel["three_halves_majorant"]),
            )

    def test_rough_support_formula(self) -> None:
        support = (103, 107, 127, 131, 139)
        for size in range(1, len(support) + 1):
            expected = Fraction((-1) ** size - 1, 2**size)
            self.assertEqual(
                half_source_gain.recombined_half_source(support[:size], 39),
                expected,
            )

    def test_poor_tail_has_an_extra_log_saving(self) -> None:
        alpha = 0.274064461784
        self.assertGreater(half_source_gain.tail_log_saving(alpha), 0)
        self.assertLess(
            half_source_gain.bad_tail_log_exponent(alpha),
            float(half_source_gain.HALF_SOURCE_SQUARE_WEIGHT - 1),
        )

    def test_guards_and_caps(self) -> None:
        with self.assertRaises(ValueError):
            half_source_gain.bad_tail_log_exponent(2)
        caps = half_source_gain.run()["resource_caps"]
        self.assertEqual(caps["maximum_two_box_assignments"], 64)
        self.assertEqual(caps["source_atoms_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
