from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import verify


class GreedyCarryParityTests(unittest.TestCase):
    def test_exact_carry_entry(self) -> None:
        self.assertEqual(verify.beta(12, 5), Fraction(4, 13))
        self.assertEqual(verify.beta(10, 10), Fraction(9, 11))

    def test_carry_count_reconstruction(self) -> None:
        for n in range(2, 18):
            for q in range(2, n + 1):
                self.assertEqual(
                    verify.beta(n, q),
                    Fraction(verify.carry_count(n, q), n + 1),
                )

    def test_greedy_minorant_is_nonnegative_and_feasible(self) -> None:
        X = 18
        target = {q: Fraction(X - q, q * X) for q in range(2, X + 1)}
        coefficients, residual, blockers = verify.greedy_minorant(X, target)
        self.assertTrue(all(value >= 0 for value in coefficients.values()))
        self.assertTrue(all(value >= 0 for value in residual.values()))
        self.assertEqual(set(coefficients), set(range(2, X + 1)))
        self.assertTrue(all(2 <= blockers[n] <= n for n in blockers))

    def test_mobius_row_collapse(self) -> None:
        mu = verify.mobius_values(30)
        for n in range(2, 30):
            for m in range(2, n + 1):
                self.assertEqual(
                    verify.mobius_collapsed_entry(n, m, mu),
                    Fraction(2 * m - n - 1, n + 1),
                )

    def test_adjoint_inverse_matches_greedy_control(self) -> None:
        X = 20
        target = {q: Fraction(X - q, q * X) for q in range(2, X + 1)}
        greedy, _, _ = verify.greedy_minorant(X, target)
        self.assertEqual(verify.adjoint_inverse(X, target), greedy)

    def test_negative_target_is_rejected(self) -> None:
        X = 5
        target = {q: Fraction(X - q, q * X) for q in range(2, X + 1)}
        target[4] = Fraction(-1, 10)
        with self.assertRaises(AssertionError):
            verify.greedy_minorant(X, target)

    def test_binary_digit_and_parity_mutations(self) -> None:
        b2 = verify.b2_values(64)
        self.assertEqual(verify.parity_convolution(3, b2), -2)
        self.assertEqual(verify.parity_convolution(4, b2), 0)
        self.assertEqual(verify.digit_convolution(1, b2), 1)
        self.assertEqual(verify.digit_convolution(64, b2), -1)

    def test_complete_result(self) -> None:
        result = verify.build_result()
        self.assertEqual(
            result["verdict"],
            "SYNTHETIC_GREEDY_CARRY_PARITY_ALGEBRA_VERIFIED",
        )
        self.assertEqual(result["carry_count_checks"], 276)
        self.assertEqual(result["binary_kummer_checks"], 322)
        self.assertEqual(result["mobius_row_collapse_checks"], 276)
        self.assertEqual(result["synthetic_non_diagonal_blockers"], 0)
        self.assertEqual(result["synthetic_adjoint_inverse_mismatches"], 0)


if __name__ == "__main__":
    unittest.main()
