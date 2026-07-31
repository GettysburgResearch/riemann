from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SPEC = importlib.util.spec_from_file_location("x14313_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)
CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


def frac(raw):
    return Fraction(int(raw["numerator"]), int(raw["denominator"]))


class SeparatedZeroFrameTests(unittest.TestCase):
    def verify(self, mutation=None):
        data = copy.deepcopy(CERT)
        if mutation:
            mutation(data)
        return MOD.verify(data)

    def rejected(self, mutation):
        with self.assertRaises(MOD.CertificateError):
            self.verify(mutation)

    def test_synthetic_floor(self):
        out = self.verify()
        self.assertEqual(out["verdict"], "CERTIFIED_SEPARATED_ZERO_FRAME_FLOOR")
        self.assertEqual(frac(out["formula_frame_floor"]), Fraction(147, 100))
        self.assertEqual(frac(out["claimed_frame_floor"]), Fraction(147, 100))

    def test_rejects_floor_too_high(self):
        self.rejected(lambda d: d.__setitem__("claimed_frame_floor", "148/100"))

    def test_rejects_row_sum_one(self):
        self.rejected(lambda d: d.__setitem__("relative_row_sum_upper", 1))

    def test_rejects_negative_tail(self):
        self.rejected(lambda d: d.__setitem__("entry_tail_upper", "-1/100"))

    def test_rejects_zero_count(self):
        self.rejected(lambda d: d.__setitem__("zero_count", 0))

    def test_production_gate(self):
        self.rejected(lambda d: d.__setitem__("classification", MOD.PRODUCTION))
        data = copy.deepcopy(CERT)
        data["classification"] = MOD.PRODUCTION
        data["analytic_gate"] = {"status": MOD.GATE, "sha256": "b" * 64}
        self.assertEqual(self.verify(lambda d: d.update(data))["classification"], MOD.PRODUCTION)


if __name__ == "__main__":
    unittest.main()
