#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x20804_verify", ROOT / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class FlatEndpointTests(unittest.TestCase):
    def test_ladder(self) -> None:
        result = MODULE.verify(8)
        self.assertEqual(result["verdict"], "PASS_EXACT_FACTORIAL_SOURCE_NOTCH")
        self.assertEqual(len(result["levels"]), 8)

    def test_source_identity(self) -> None:
        for r in range(1, 9):
            self.assertEqual(MODULE.build_level(r)["source"], "1/1")

    def test_zero_mean_coordinate(self) -> None:
        level = MODULE.build_level(7)
        self.assertEqual(Fraction(level["u"][0]), 0)

    def test_alternating_coefficients(self) -> None:
        level = MODULE.build_level(6)
        values = [Fraction(value) for value in level["u"][1:]]
        self.assertEqual([value > 0 for value in values], [False, True, False, True, False, True])

    def test_metric_bound(self) -> None:
        level = MODULE.build_level(8)
        self.assertLessEqual(
            Fraction(level["metric"]),
            Fraction(level["binomial_metric_bound"]),
        )

    def test_bad_dimension(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.build_level(0)


if __name__ == "__main__":
    unittest.main()
