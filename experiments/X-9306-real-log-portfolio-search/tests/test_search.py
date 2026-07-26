from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x9306_search", ROOT / "search.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SearchKernelTests(unittest.TestCase):
    def test_three_point_log_concavity_polynomial(self):
        nodes = [Fraction(1), Fraction(2), Fraction(3)]
        beta = [Fraction(-1), Fraction(2), Fraction(-1)]
        self.assertEqual(MODULE.response_polynomial(nodes, beta), [Fraction(2)])

    def test_safe_endpoint_response_has_positive_coefficients(self):
        nodes = [Fraction(1), Fraction(2), Fraction(5), Fraction(7)]
        beta = [Fraction(-1), Fraction(0), Fraction(0), Fraction(1)]
        polynomial = MODULE.response_polynomial(nodes, beta)
        self.assertTrue(all(value > 0 for value in polynomial))

    def test_rationalization_repairs_small_defect(self):
        nodes = [Fraction(1), Fraction(2), Fraction(3)]
        floating = MODULE.np.array([-1.0, 2.0 + 1e-10, -1.0])
        frozen = MODULE.rationalize_and_repair(nodes, floating)
        self.assertIsNotNone(frozen)
        beta, polynomial = frozen
        self.assertEqual(sum(beta), 0)
        self.assertTrue(all(value >= 0 for value in polynomial))
        self.assertEqual(sum(polynomial), 1)

    def test_log_enclosure_contains_known_value(self):
        interval = MODULE.log_fraction(Fraction(2), 80)
        import math
        value = Fraction.from_float(math.log(2))
        self.assertLess(interval.lo, value)
        self.assertGreater(interval.hi, value)


if __name__ == "__main__":
    unittest.main()
