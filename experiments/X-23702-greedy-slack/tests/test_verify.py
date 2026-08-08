from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import verify


class GreedySlackTests(unittest.TestCase):
    def test_exact_control(self) -> None:
        result = verify.build_result()
        self.assertEqual(
            result["verdict"], "EXACT_GREEDY_SLACK_SCOPE_CONTROL_VERIFIED"
        )
        self.assertEqual(result["positive_final_slack"], "29/500")
        self.assertEqual(result["diagonal_loss_row_5"], "87/1000")

    def test_blocker_mutation(self) -> None:
        target = {
            2: Fraction(91, 100), 3: Fraction(41, 50),
            4: Fraction(33, 50), 5: Fraction(33, 50),
            6: Fraction(63, 100), 7: Fraction(11, 20),
            8: Fraction(53, 100), 9: Fraction(0),
        }
        _, residual, blockers, losses = verify.greedy(9, target)
        self.assertEqual(blockers[5], 4)
        self.assertNotEqual(blockers[5], 5)
        self.assertEqual(residual[5], verify.beta(5, 5) * losses[5])

    def test_row_sum_identity(self) -> None:
        for n in range(2, 80):
            self.assertEqual(
                verify.carry_row_sum(n),
                verify.carry_row_sum_via_divisors(n),
            )

    def test_target_mutation_changes_control(self) -> None:
        target = {
            2: Fraction(91, 100), 3: Fraction(41, 50),
            4: Fraction(33, 50), 5: Fraction(33, 50),
            6: Fraction(63, 100), 7: Fraction(11, 20),
            8: Fraction(53, 100), 9: Fraction(0),
        }
        target[5] += Fraction(1, 100)
        _, residual, _, _ = verify.greedy(9, target)
        self.assertNotEqual(residual[5], Fraction(29, 500))


if __name__ == "__main__":
    unittest.main()
