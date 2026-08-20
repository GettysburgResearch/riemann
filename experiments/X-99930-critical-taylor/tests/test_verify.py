#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t99930_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class TestT99930(unittest.TestCase):
    def test_duplicate_67_coefficients(self) -> None:
        self.assertEqual([V.beta(67**e) for e in range(4)], [1, -2, 1, 0])

    def test_taylor_integral_identity(self) -> None:
        for m in range(3, 8):
            for k in range(1, m + 1):
                for z in (F(1, 7), F(2, 3), F(5, 2)):
                    self.assertEqual(
                        V.remainder(m, k, z), V.integral_remainder(m, k, z)
                    )

    def test_scaling_mutation_is_one_sided(self) -> None:
        m, k, z, c = 8, 5, F(3, 4), F(7, 3)
        self.assertLessEqual(V.remainder(m, k, c * z), c**k * V.remainder(m, k, z))
        # Reversing the inequality is not a valid theorem.
        self.assertNotEqual(V.remainder(m, k, c * z), c**k * V.remainder(m, k, z))

    def test_prime_mass_is_strict(self) -> None:
        result = V.prime_mass_bound()
        self.assertTrue(result["strictly_below_one"])

    def test_critical_kernel_positive_but_not_source_sign(self) -> None:
        self.assertGreaterEqual(V.critical_kernel(2, F(1, 4)), 0)
        # The verifier must retain the arithmetic sign as open.
        self.assertEqual(V.VERDICT, "PASS_T99930_CRITICAL_TAYLOR_RENORMALIZATION")

    def test_last_step_firewall(self) -> None:
        result = V.last_step_firewall()
        self.assertTrue(result["primitive_nonnegative"])
        self.assertEqual(result["negative_final_window"], "-1")


if __name__ == "__main__":
    unittest.main()
