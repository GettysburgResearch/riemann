import unittest
from fractions import Fraction
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import verify


class CarryGreenTests(unittest.TestCase):
    def test_main(self):
        verify.main()

    def test_wrong_beta_rejected(self):
        self.assertNotEqual(
            verify.beta(10, 3),
            Fraction((10 // 3) * (3 - (10 % 3)), 11),
        )

    def test_nonmobius_mutation_rejected(self):
        mu = verify.mobius_table(20)
        mu[6] = -1
        n, m = 12, 2
        lhs = sum(
            Fraction(mu[k]) * verify.beta(n, m * k)
            for k in range(1, n // m + 1)
        )
        self.assertNotEqual(lhs, Fraction(2 * m - n - 1, n + 1))

    def test_digit_mutation_rejected(self):
        running = 0
        for n in range(1, 20):
            running += verify.c2(n)
        self.assertNotEqual(running + 1, verify.digit_sum_2(19))


if __name__ == "__main__":
    unittest.main()
