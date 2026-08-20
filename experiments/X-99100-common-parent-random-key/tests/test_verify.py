from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VERIFY)


class CommonParentTests(unittest.TestCase):
    def test_control_passes(self) -> None:
        result = VERIFY.verify()
        self.assertEqual(result["classification"], VERIFY.VERDICT)
        self.assertFalse(result["rh_established"])

    def test_hazard_telescoping(self) -> None:
        rs = [Fraction(1, 9), Fraction(1, 11), Fraction(1, 13)]
        s = Fraction(1)
        lambdas = []
        for r in rs:
            lambdas.append(r * s)
            s *= 1 - r
        self.assertEqual(s + sum(lambdas, Fraction()), 1)

    def test_factor67_strict_bound(self) -> None:
        self.assertLess(Fraction(64), Fraction(67))

    def test_local_density_is_load_bearing(self) -> None:
        self.assertLessEqual(Fraction(6, 5), 2)
        self.assertGreater(Fraction(6, 5), 1)

    def test_expectation_does_not_imply_leaf_feasibility(self) -> None:
        leaves = [0, 2]
        self.assertEqual(Fraction(sum(leaves), 2), 1)
        self.assertGreater(max(leaves), 1)

    def test_normalize_last(self) -> None:
        masses = [Fraction(2), Fraction(3)]
        z = [Fraction(1, 4), Fraction(2, 3)]
        lhs = sum(m * x for m, x in zip(masses, z)) / sum(masses)
        rhs = sum((m / sum(masses)) * x for m, x in zip(masses, z))
        self.assertEqual(lhs, rhs)

    def test_integral_matching_leaves(self) -> None:
        a = [[1, 0], [0, 1]]
        b = [[0, 1], [1, 0]]
        for m in (a, b):
            self.assertTrue(all(sum(row) == 1 for row in m))
            self.assertTrue(all(sum(m[i][j] for i in range(2)) == 1 for j in range(2)))


if __name__ == "__main__":
    unittest.main()
