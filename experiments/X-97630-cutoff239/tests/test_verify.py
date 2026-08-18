from __future__ import annotations
import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t97630_verify", HERE / "verify.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)

class Tests(unittest.TestCase):
    def test_baseline(self):
        out = MOD.validate()
        self.assertEqual(out["cutoff"], 239)
        self.assertEqual(out["strict_margin"], "1/960")

    def test_x184(self):
        out = MOD.validate()
        self.assertTrue(float(out["x184_M_minus_40F_lower_decimal"]) > 18.11)

    def test_low_child(self):
        self.assertTrue(MOD.validate()["low_child_recombination"])

    def test_reserve_countermodel(self):
        self.assertTrue(MOD.validate()["reserve_current_implication_refuted"])

    def test_zero_safe(self):
        self.assertTrue(MOD.validate()["mellin_finite_factors_zero_safe"])

    def test_mutations(self):
        for mutation in MOD.MUTATIONS:
            with self.subTest(mutation=mutation):
                with self.assertRaises(MOD.ContractError):
                    MOD.validate(mutation)

    def test_full_run(self):
        out = MOD.run(Path("/tmp/t97630-test-result.json"), mutations=True)
        self.assertEqual(out["classification"], MOD.VERDICT)
        self.assertEqual(len(out["hostile_mutations_rejected"]), len(MOD.MUTATIONS))

if __name__ == "__main__":
    unittest.main()
