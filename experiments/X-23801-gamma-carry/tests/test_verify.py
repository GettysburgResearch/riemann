#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
V = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(V)


class GammaCarryTests(unittest.TestCase):
    def test_carry_endpoint_identity(self) -> None:
        for n in range(2, 40):
            for q in range(2, n + 1):
                self.assertEqual(V.beta(n, q), V.carry_endpoint(n, q))

    def test_wrong_denominator_rejected(self) -> None:
        n, q = 17, 5
        k, r = divmod(n, q)
        wrong = F(k * (q - 1 - r), n)
        self.assertNotEqual(wrong, V.carry_endpoint(n, q))

    def test_integer_left_limit_is_zero(self) -> None:
        # (n+1)/q=3 is a reset knot.  The finite coefficient uses the left limit.
        self.assertEqual(V.carry_endpoint(8, 3), 0)
        self.assertEqual(V.beta(8, 3), 0)

    def test_harmonic_interval_mass(self) -> None:
        for m in range(1, 50):
            self.assertEqual(V.interval_mass(m), F(1, m * (m + 1)))

    def test_partial_fraction_mutation(self) -> None:
        s = 4
        correct = V.rational_factor(s)
        half = F(2 * s + 1, 2)
        wrong = F(1, s) - F(7, 8) / half - F(1, 16) / (half * half)
        self.assertNotEqual(correct, wrong)
        self.assertEqual(correct, V.partial_fraction_factor(s))


if __name__ == "__main__":
    unittest.main()
