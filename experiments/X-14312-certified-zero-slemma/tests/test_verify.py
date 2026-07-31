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
SPEC = importlib.util.spec_from_file_location("x14312_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)
CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


def frac(raw):
    return Fraction(int(raw["numerator"]), int(raw["denominator"]))


class CertifiedZeroSLemmaTests(unittest.TestCase):
    def verify(self, mutation=None):
        data = copy.deepcopy(CERT)
        if mutation is not None:
            mutation(data)
        return MOD.verify(data)

    def rejected(self, mutation):
        with self.assertRaises(MOD.CertificateError):
            self.verify(mutation)

    def test_exact_visible_floor_separates_global_negative(self):
        out = self.verify()
        self.assertEqual(out["verdict"], "CERTIFIED_VISIBLE_CONE_LOWER_FLOOR")
        self.assertEqual(frac(out["visible_floor_certified"]), Fraction(5, 4))
        self.assertEqual(frac(out["midpoint_global_diagnostic_rayleigh"]), Fraction(-1))
        self.assertEqual(frac(out["robust_slater_margin"]), Fraction(1, 4))

    def test_rejects_floor_above_exact_optimum(self):
        self.rejected(lambda d: d.__setitem__("claimed_visible_floor", "126/100"))

    def test_rejects_negative_multiplier(self):
        self.rejected(lambda d: d.__setitem__("multiplier", -1))

    def test_rejects_failed_slater(self):
        self.rejected(lambda d: d.__setitem__("slater_vector", [0, 1]))

    def test_rejects_nonpositive_metric(self):
        self.rejected(lambda d: d.__setitem__("metric", [[1, 0], [0, 0]]))

    def test_visibility_radius_is_charged(self):
        def mutate(data):
            data["visibility_radius"] = "1/100"
        self.rejected(mutate)

    def test_form_radius_is_charged(self):
        def mutate(data):
            data["form_radius"] = "1/100"
        self.rejected(mutate)

    def test_production_requires_typed_gate(self):
        def production(data):
            data["classification"] = MOD.PRODUCTION
        self.rejected(production)
        data = copy.deepcopy(CERT)
        data["classification"] = MOD.PRODUCTION
        data["analytic_gate"] = {"status": MOD.GATE, "sha256": "a" * 64}
        self.assertEqual(self.verify(lambda d: d.update(data))["classification"], MOD.PRODUCTION)


if __name__ == "__main__":
    unittest.main()
