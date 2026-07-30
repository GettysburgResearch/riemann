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
spec = importlib.util.spec_from_file_location("x14306_verify", ROOT / "verify.py")
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


def fraction(raw):
    return Fraction(int(raw["numerator"]), int(raw["denominator"]))


class MultibandFloorTests(unittest.TestCase):
    def test_synthetic(self):
        output = module.verify(copy.deepcopy(CERT))
        self.assertEqual(output["required_rank_cap"], 7)
        self.assertEqual(fraction(output["certified_formula_floor"]), Fraction(5, 6))
        self.assertEqual(
            output["exact_proof_object_sha256"],
            "4fcd9ceb05a3002675ce704bef43f3a4ad398ba29974ee11b8b8a7898d97ae66",
        )

    def test_rank_too_small(self):
        certificate = copy.deepcopy(CERT)
        certificate["rank_cap"] = 6
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)

    def test_floor_too_high(self):
        certificate = copy.deepcopy(CERT)
        certificate["claimed_complement_floor"] = 1
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)

    def test_symbol_bounds_reversed(self):
        certificate = copy.deepcopy(CERT)
        certificate["global_symbol_lower"] = 5
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)

    def test_negative_measure_rejected(self):
        certificate = copy.deepcopy(CERT)
        certificate["bad_measure_upper"] = -1
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)

    def test_production_gate(self):
        certificate = copy.deepcopy(CERT)
        certificate["classification"] = module.PRODUCTION
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)
        certificate["symbol_cover_gate"] = {
            "status": module.GATE,
            "sha256": "c" * 64,
        }
        self.assertEqual(
            module.verify(certificate)["classification"], module.PRODUCTION
        )

    def test_boolean_rejected(self):
        certificate = copy.deepcopy(CERT)
        certificate["rank_cap"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)


if __name__ == "__main__":
    unittest.main()
