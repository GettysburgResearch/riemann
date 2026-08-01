#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x20803_verify", ROOT / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ShiftedLatticeTests(unittest.TestCase):
    def test_main_ladder(self) -> None:
        result = MODULE.verify_range(range(1, 9), Fraction(3, 4))
        self.assertEqual(result["verdict"], "PASS_EXACT_SHIFTED_LATTICE_SOURCE_NOTCH")
        self.assertEqual(len(result["levels"]), 8)

    def test_source_is_one(self) -> None:
        level = MODULE.build_level(6, Fraction(3, 4))
        self.assertEqual(level["source"], "1/1")

    def test_coefficients_are_positive(self) -> None:
        level = MODULE.build_level(7, Fraction(3, 4))
        values = [Fraction(value) for value in level["u"]]
        self.assertTrue(all(value > 0 for value in values))

    def test_half_shift_is_rejected_by_strict_scope(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.build_level(4, Fraction(1, 2))

    def test_unit_shift_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.build_level(4, Fraction(1, 1))

    def test_nonpositive_dimension_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.build_level(0, Fraction(3, 4))


if __name__ == "__main__":
    unittest.main()
