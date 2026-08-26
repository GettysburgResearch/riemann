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
    / "ffps_higher_order_atom_free_escape.py"
)
SPEC = importlib.util.spec_from_file_location("higher_escape", MODULE_PATH)
assert SPEC and SPEC.loader
higher_escape = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(higher_escape)


class HigherOrderAtomFreeEscapeTest(unittest.TestCase):
    def test_uniform_sharpness(self) -> None:
        for support_size in range(2, 9):
            for order in range(2, min(4, support_size) + 1):
                row = higher_escape.uniform_certificate(support_size, order)
                self.assertTrue(row["equality"])
                self.assertEqual(row["ordered_distinct_energy"], row["closed_form"])

    def test_nonuniform_lower_bound(self) -> None:
        masses = (
            Fraction(1, 3),
            Fraction(1, 4),
            Fraction(1, 6),
            Fraction(1, 8),
            Fraction(1, 12),
            Fraction(1, 24),
        )
        self.assertEqual(sum(masses), 1)
        for order in (2, 3):
            self.assertGreaterEqual(
                higher_escape.ordered_distinct_energy(masses, order),
                higher_escape.delocalization_lower_bound(masses, order),
            )

    def test_one_atom_cannot_contribute(self) -> None:
        masses = (Fraction(1), Fraction(0), Fraction(0))
        self.assertEqual(higher_escape.ordered_distinct_energy(masses, 2), 0)
        self.assertEqual(higher_escape.ordered_distinct_energy(masses, 3), 0)
        self.assertEqual(higher_escape.delocalization_lower_bound(masses, 2), 0)

    def test_invalid_and_resource_caps(self) -> None:
        with self.assertRaises(ValueError):
            higher_escape.ordered_distinct_energy((), 2)
        with self.assertRaises(ValueError):
            higher_escape.ordered_distinct_energy((Fraction(1),), 2)
        with self.assertRaises(ValueError):
            higher_escape.ordered_distinct_energy((Fraction(1), Fraction(1)), True)
        caps = higher_escape.run()["resource_caps"]
        self.assertEqual(caps["largest_ordered_tuple_count"], 1680)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
