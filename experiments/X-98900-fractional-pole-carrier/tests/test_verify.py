from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x98900_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)
BASE = json.loads((ROOT / "certificates" / "control.json").read_text(encoding="utf-8"))


class PolePhaseTests(unittest.TestCase):
    def run_cert(self, mutate=None):
        data = copy.deepcopy(BASE)
        if mutate:
            mutate(data)
        return MOD.verify(data)

    def rejected(self, mutate):
        with self.assertRaises(MOD.VerificationError):
            self.run_cert(mutate)

    def test_control(self):
        out = self.run_cert()
        self.assertEqual(out["verdict"], "PASS_X98900_FRACTIONAL_POLE_AND_PHASE_FIREWALLS")
        self.assertEqual(out["phased_determinant"], "-80/81")

    def test_rejects_theta_at_threshold(self):
        self.rejected(lambda d: d.__setitem__("theta", "1/192"))

    def test_rejects_false_local_factor(self):
        self.rejected(lambda d: d.__setitem__("local_dyadic_factor_at_one", "1/2"))

    def test_rejects_wrong_prime(self):
        self.rejected(lambda d: d["phase_fixture"].__setitem__("prime", 5))

    def test_rejects_false_rate(self):
        self.rejected(lambda d: d["expected"].__setitem__("actual_energy_exponent", "1/4"))

    def test_rejects_false_phase_determinant(self):
        self.rejected(lambda d: d["expected"].__setitem__("phased_determinant", "0"))

    def test_rejects_boolean_theta(self):
        self.rejected(lambda d: d.__setitem__("theta", True))


if __name__ == "__main__":
    unittest.main()
