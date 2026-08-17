from pathlib import Path
import importlib.util
import sys
import unittest

HERE=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("v96400",HERE/"verify.py")
MOD=importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name]=MOD
SPEC.loader.exec_module(MOD)

class Tests(unittest.TestCase):
    def test_baseline(self):
        out=MOD.validate()
        self.assertEqual(out["no_common_zero"]["factorization"],"-3(x-1)(x-2)")
    def test_partition(self):
        out=MOD.interval_refinement()
        self.assertEqual(out["recursive_mass"],"6823/245025")
    def test_q2(self):
        self.assertLess(float(MOD.q2_score_obstruction()),0)
    def test_mutations(self):
        for m in MOD.MUTATIONS:
            with self.subTest(m=m), self.assertRaises(MOD.ContractError):
                MOD.validate(m)
    def test_full(self):
        p=MOD.run(mutations=True)
        self.assertEqual(p["verdict"],MOD.VERDICT)
        self.assertFalse(p["rh_established_by_replay"])

if __name__=="__main__":
    unittest.main()
