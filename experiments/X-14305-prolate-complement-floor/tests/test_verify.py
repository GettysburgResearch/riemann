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
spec = importlib.util.spec_from_file_location("x14305_verify", ROOT / "verify.py")
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


def fraction(raw):
    return Fraction(int(raw["numerator"]), int(raw["denominator"]))


class ProlateComplementTests(unittest.TestCase):
    def test_synthetic(self):
        output = module.verify(copy.deepcopy(CERT))
        self.assertEqual(
            output["verdict"], "CERTIFIED_COMPLETE_PROLATE_COMPLEMENT_FLOOR"
        )
        self.assertEqual(output["required_rank_cap"], 134)
        self.assertEqual(fraction(output["certified_formula_floor"]), Fraction(1, 3))
        self.assertEqual(
            output["exact_proof_object_sha256"],
            "ee5a5195f7fc51828bbc5126481c274f8be87f7141951bb2e542a876c3cf4097",
        )

    def test_rank_too_small(self):
        certificate = copy.deepcopy(CERT)
        certificate["rank_cap"] = 133
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)

    def test_floor_too_high(self):
        certificate = copy.deepcopy(CERT)
        certificate["claimed_complement_floor"] = {
            "numerator": 334,
            "denominator": 1000,
        }
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)

    def test_bad_eta(self):
        certificate = copy.deepcopy(CERT)
        certificate["eta"] = 1
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)

    def test_bad_pi(self):
        certificate = copy.deepcopy(CERT)
        certificate["pi_lower"] = 0
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)

    def test_production_gate(self):
        certificate = copy.deepcopy(CERT)
        certificate["classification"] = module.PRODUCTION
        with self.assertRaises(module.CertificateError):
            module.verify(certificate)
        certificate["analytic_gate"] = {
            "status": module.ANALYTIC_GATE,
            "sha256": "b" * 64,
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
