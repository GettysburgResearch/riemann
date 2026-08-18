from __future__ import annotations
import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x97680", ROOT / "verify.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)

class Tests(unittest.TestCase):
    def test_source_fixture(self):
        out = MOD.paired_source_fixture()
        self.assertIn("root", out)

    def test_depth_fixture(self):
        out = MOD.layer_fixture()
        self.assertLess(Fraction(out["signed_current"]), 0)

    def test_baseline(self):
        out = MOD.validate()
        self.assertEqual(out["source_faithfulness"], "PASS")
        self.assertEqual(out["NCBI67"], "OPEN")
        self.assertFalse(out["RH_established"])

    def test_mutations(self):
        for m in MOD.MUTATIONS:
            with self.subTest(m=m), self.assertRaises(MOD.ContractError):
                MOD.validate(m)

    def test_full(self):
        out = MOD.run(Path("/tmp/x97680.json"), True)
        self.assertEqual(out["classification"], MOD.VERDICT)
        self.assertEqual(len(out["hostile_mutations_rejected"]), len(MOD.MUTATIONS))

if __name__ == "__main__":
    unittest.main()
