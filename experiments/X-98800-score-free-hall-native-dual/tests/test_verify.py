from __future__ import annotations

import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
MOD = importlib.util.module_from_spec(SPEC)
import sys
sys.modules[SPEC.name] = MOD
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class TestT98800(unittest.TestCase):
    def test_full_result(self):
        result = MOD.build_result()
        self.assertEqual(result["classification"], MOD.VERDICT)
        self.assertFalse(result["rh_established"])

    def test_score_firewall(self):
        self.assertLess(MOD.exact_score_firewall(), 0)

    def test_bonus_unscoreable(self):
        b = MOD.RowBonus((MOD.Fraction(1),))
        with self.assertRaises(TypeError):
            _ = b.score

    def test_hall_identity(self):
        h = MOD.hall_fixture()
        self.assertTrue(all(x >= 0 for x in h["bonus_rows"]))

    def test_radix_inverse(self):
        _, ordinary = MOD.radix_four_inverse()
        self.assertTrue(all(x >= 0 for x in ordinary.values()))

    def test_ownership_mutation(self):
        self.assertTrue(MOD.ownership_mutations())


if __name__ == "__main__":
    unittest.main()
