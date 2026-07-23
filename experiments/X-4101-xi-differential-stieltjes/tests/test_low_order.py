from __future__ import annotations

import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import synthetic  # noqa: E402


class LowOrderInequalityTests(unittest.TestCase):
    def test_explicit_inequalities_match_moment_determinants(self) -> None:
        ordinates = [Fraction(-5), Fraction(-1), Fraction(4), Fraction(9)]
        zeros = [(Fraction(0), gamma) for gamma in ordinates]
        x = Fraction(3, 5)
        height = Fraction(2, 7)
        u = x * x
        jet = synthetic.finite_logderivative_jet(zeros, x, height, 3)
        moments = synthetic.moments_from_jet(jet, x, 3)

        h = moments[0]
        h1 = -moments[1]
        h2 = 2 * moments[2]
        h3 = -6 * moments[3]

        hankel_expression = h * h2 - 2 * h1 * h1
        hankel = synthetic.hankel_matrix(moments, 1)
        hankel_determinant = (
            hankel[0][0] * hankel[1][1]
            - hankel[0][1] * hankel[1][0]
        )
        self.assertEqual(hankel_expression, 2 * hankel_determinant)
        self.assertGreaterEqual(hankel_expression, 0)

        l0 = h + u * h1
        l1 = -h1 - u * h2 / 2
        l2 = h2 / 2 + u * h3 / 6
        localizing_expression = l0 * l2 - l1 * l1
        localizing = synthetic.localizing_matrix(moments, u, 1)
        localizing_determinant = (
            localizing[0][0] * localizing[1][1]
            - localizing[0][1] * localizing[1][0]
        )
        self.assertEqual(localizing[0][0], l0)
        self.assertEqual(localizing[0][1], l1)
        self.assertEqual(localizing[1][1], l2)
        self.assertEqual(localizing_expression, localizing_determinant)
        self.assertGreaterEqual(l0, 0)
        self.assertGreaterEqual(l2, 0)
        self.assertGreaterEqual(localizing_expression, 0)

    def test_single_ordinate_matrices_have_zero_determinant(self) -> None:
        ordinates = [Fraction(7)]
        zeros = [(Fraction(0), ordinates[0])]
        x = Fraction(4, 5)
        height = Fraction(1, 3)
        u = x * x
        jet = synthetic.finite_logderivative_jet(zeros, x, height, 3)
        moments = synthetic.moments_from_jet(jet, x, 3)
        hankel = synthetic.hankel_matrix(moments, 1)
        localizing = synthetic.localizing_matrix(moments, u, 1)
        self.assertEqual(
            hankel[0][0] * hankel[1][1]
            - hankel[0][1] * hankel[1][0],
            0,
        )
        self.assertEqual(
            localizing[0][0] * localizing[1][1]
            - localizing[0][1] * localizing[1][0],
            0,
        )

    def test_wrong_hankel_factor_is_detected(self) -> None:
        ordinates = [Fraction(-3), Fraction(8)]
        zeros = [(Fraction(0), gamma) for gamma in ordinates]
        x = Fraction(5, 6)
        height = Fraction(1, 4)
        jet = synthetic.finite_logderivative_jet(zeros, x, height, 2)
        moments = synthetic.moments_from_jet(jet, x, 2)
        h = moments[0]
        h1 = -moments[1]
        h2 = 2 * moments[2]
        correct = h * h2 - 2 * h1 * h1
        wrong = h * h2 - h1 * h1
        self.assertNotEqual(correct, wrong)


if __name__ == "__main__":
    unittest.main()
