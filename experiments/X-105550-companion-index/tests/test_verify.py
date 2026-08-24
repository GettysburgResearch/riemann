from __future__ import annotations
import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve()
MOD = HERE.parents[1] / "verify.py"
spec = importlib.util.spec_from_file_location("t105550_verify", MOD)
v = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(v)

class Tests(unittest.TestCase):
    def test_companion(self):
        self.assertGreaterEqual(v.companion_fixture_checks()["fixtures"], 200)
    def test_phase(self):
        self.assertGreater(v.phase_algebra_checks()["exact_phase_derivative_checks"], 500)
    def test_rank_energy(self):
        self.assertEqual(len(v.separated_rank_energy_checks()["fixtures"]), 3)
    def test_dipole(self):
        self.assertTrue(v.dipole_checks()["arbitrarily_small_norm_with_rank_one"])
    def test_fail_closed(self):
        p=v.payload()
        self.assertFalse(p["cpindex105550_proved"])
        self.assertFalse(p["ninety_percent_established"])
        self.assertFalse(p["public_record_beaten"])
        self.assertFalse(p["rh_established"])

if __name__ == "__main__":
    unittest.main()
