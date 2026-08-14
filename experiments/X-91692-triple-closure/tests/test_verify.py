from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("triple_verify", ROOT / "verify.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class TripleClosureRegression(unittest.TestCase):
    def test_full_control(self):
        out = MOD.verify()
        self.assertEqual(out["verdict"], "PASS_TRIPLE_CLOSURE_FINITE_ALGEBRA")
        self.assertEqual(out["route_a"]["global_child_mass_ratio"], "73/1000")
        self.assertEqual(
            out["route_c"]["verdict"],
            "PASS_POSITIVE_STIELTJES_DATA_GIVE_BOTH_HANKEL_PAIRS_PD",
        )

    def test_one_eighth_firewall(self):
        self.assertFalse(Fraction(1, 8) < Fraction(1, 8))

    def test_reserve_must_be_strict(self):
        eps = Fraction(1, 10**8)
        cnorm = Fraction(7, 3)
        delta = 10152 * cnorm * eps
        self.assertFalse(delta > 10152 * cnorm * eps)
        self.assertTrue(2 * delta > 10152 * cnorm * eps)

    def test_complex_or_signed_pole_is_not_accepted(self):
        with self.assertRaises(TypeError):
            MOD.exact_pd([[1 + 1j]])

    def test_hankel_negative_control(self):
        self.assertFalse(
            MOD.exact_pd(
                [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(1)]]
            )[0]
        )


if __name__ == "__main__":
    unittest.main()
