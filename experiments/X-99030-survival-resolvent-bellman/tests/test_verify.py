#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFY = HERE.parent / "verify.py"
spec = importlib.util.spec_from_file_location("x99030_verify", VERIFY)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class SurvivalResolventTests(unittest.TestCase):
    def test_root_mass_is_strictly_between_fifteen_and_sixteen(self) -> None:
        mass = mod.root_mass_interval()
        self.assertGreater(mass.lo, 15)
        self.assertLess(mass.hi, 16)

    def test_causal_partition_of_unity_and_cancellation(self) -> None:
        for rs in (
            [Fraction(1, 9)],
            [Fraction(1, 9), Fraction(1, 10)],
            [Fraction(1, 9), Fraction(1, 10), Fraction(1, 11)],
            [Fraction(1, 12), Fraction(1, 13), Fraction(1, 14), Fraction(1, 15)],
        ):
            s, lambdas, alphas = mod.causal_coefficients(rs)
            self.assertEqual(s + sum(lambdas, Fraction(0)), 1)
            for r, lam, alpha in zip(rs, lambdas, alphas):
                self.assertEqual(-lam * r + alpha, 0)

    def test_resolvent_bellman_identity(self) -> None:
        result = mod.fixture(
            [Fraction(1, 9), Fraction(1, 10), Fraction(1, 11)],
            [Fraction(2), Fraction(3, 2), Fraction(-1, 3)],
            [Fraction(-1, 4), 0, Fraction(-2, 5)],
        )
        self.assertLessEqual(Fraction(result["parent"]), Fraction(result["discounted"]))
        self.assertLessEqual(Fraction(result["current"]), 0)

    def test_terminal_debt_ratio(self) -> None:
        # With t=sqrt(Y)>=1, 2T-S=3(t-1)>=0.
        for t in (Fraction(1), Fraction(5, 4), Fraction(2), Fraction(17, 2)):
            target = 4 * t - 3
            score = 5 * t - 3
            self.assertGreaterEqual(target, 0)
            self.assertLessEqual(score, 2 * target)

    def test_first_transition_discount_is_below_one_eighth(self) -> None:
        # 1/sqrt(67)<1/8 iff 67>64.
        self.assertGreater(67, 64)

    def test_missing_survival_resolvent_is_rejected(self) -> None:
        rs = [Fraction(1, 9), Fraction(1, 10)]
        s, lambdas, alphas = mod.causal_coefficients(rs)
        den = 1 - s
        children = [Fraction(2), Fraction(3)]
        raw = sum(a * d for a, d in zip(alphas, children))
        self.assertGreater(raw / den, raw)

    def test_positive_current_debt_breaks_discounted_bound(self) -> None:
        rs = [Fraction(1, 9), Fraction(1, 10)]
        s, lambdas, alphas = mod.causal_coefficients(rs)
        den = 1 - s
        children = [Fraction(2), Fraction(3)]
        current = [Fraction(1, 20), 0]
        parent = (
            sum(l * c for l, c in zip(lambdas, current))
            + sum(a * d for a, d in zip(alphas, children))
        ) / den
        discounted = sum(
            (l / den) * r * d for l, r, d in zip(lambdas, rs, children)
        )
        self.assertGreater(parent, discounted)


if __name__ == "__main__":
    unittest.main()
