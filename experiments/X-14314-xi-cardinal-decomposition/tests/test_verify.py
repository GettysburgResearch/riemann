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
SPEC = importlib.util.spec_from_file_location("x14314_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)
CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


def frac(raw):
    return Fraction(int(raw["numerator"]), int(raw["denominator"]))


class XiCardinalTests(unittest.TestCase):
    def verify(self, mutation=None):
        data = copy.deepcopy(CERT)
        if mutation:
            mutation(data)
        return MOD.verify(data)

    def rejected(self, mutation):
        with self.assertRaises(MOD.CertificateError):
            self.verify(mutation)

    def test_exact_indefinite_decomposition(self):
        out = self.verify()
        self.assertEqual(out["verdict"], "CERTIFIED_XI_CARDINAL_SPECTRAL_DECOMPOSITION")
        self.assertEqual(frac(out["global_form"]), Fraction(8))
        self.assertEqual(frac(out["selected_positive_form"]), Fraction(10))
        self.assertEqual(frac(out["residual_form"]), Fraction(-2))
        self.assertEqual(frac(out["decomposition_check"]), Fraction(8))

    def test_rejects_false_polynomial_root(self):
        self.rejected(lambda d: d["xi_polynomial"].__setitem__(0, 4))

    def test_rejects_missing_conjugate(self):
        self.rejected(lambda d: d["roots"].__setitem__(3, {"real": 0, "imag": -2}))

    def test_rejects_duplicate_selected_root(self):
        self.rejected(lambda d: d.__setitem__("selected_real_roots", [1, 1]))

    def test_rejects_false_global_claim(self):
        self.rejected(lambda d: d.__setitem__("claimed_global_form", 9))

    def test_rejects_false_residual_claim(self):
        self.rejected(lambda d: d.__setitem__("claimed_residual_form", -1))

    def test_rejects_degree_too_large(self):
        self.rejected(lambda d: d.__setitem__("test_polynomial", [0, 0, 0, 0, 1, 1]))

    def test_production_gate(self):
        self.rejected(lambda d: d.__setitem__("classification", MOD.PRODUCTION))
        data = copy.deepcopy(CERT)
        data["classification"] = MOD.PRODUCTION
        data["analytic_gate"] = {"status": MOD.GATE, "sha256": "c" * 64}
        self.assertEqual(self.verify(lambda d: d.update(data))["classification"], MOD.PRODUCTION)


if __name__ == "__main__":
    unittest.main()
