from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import verify


class DigitalFreezeTests(unittest.TestCase):
    def test_corridor_identity(self) -> None:
        for modulus in (2, 3, 5, 11):
            for k in range(2, 20):
                for e in range(2, k + 1):
                    self.assertEqual(
                        verify.beta(modulus * (k + 1) - 1, modulus * e),
                        verify.beta(k, e),
                    )

    def test_wrong_row_shift_is_rejected(self) -> None:
        self.assertNotEqual(verify.beta(5 * (8 + 1), 5 * 3), verify.beta(8, 3))

    def test_base_five_convolution(self) -> None:
        limit = 100
        mu = verify.mobius_values(limit)
        p = 5
        b = [0] * (limit + 1)
        c = [0] * (limit + 1)
        for n in range(1, limit + 1):
            b[n] = mu[n] - (mu[n // p] if n % p == 0 else 0)
            c[n] = 1 - (p - 1) * verify.valuation(n, p)
        for n in range(1, limit + 1):
            value = sum(c[d] * b[n // d] for d in verify.divisors(n))
            expected = 1 if n == 1 else (-p if n == p else 0)
            self.assertEqual(value, expected)

    def test_complete_result(self) -> None:
        result = verify.build_result()
        self.assertEqual(result["corridor_renormalization_checks"], 13475)
        self.assertEqual(result["base_p_convolution_checks"], 2000)
        self.assertEqual(
            result["verdict"],
            "PASS_EXACT_DIGITAL_FREEZE_AND_BASE_P_PHASE_ALGEBRA",
        )


if __name__ == "__main__":
    unittest.main()
