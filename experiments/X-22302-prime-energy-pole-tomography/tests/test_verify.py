from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x22302_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)

CERTIFICATE = ROOT / "certificates" / "synthetic.json"


class PoleTomographyTests(unittest.TestCase):
    def payload(self):
        return json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def resign(self, payload):
        payload["proof_object_sha256"] = module.canonical_sha256(payload)
        return payload

    def test_baseline(self):
        result = module.verify(self.payload())
        self.assertEqual(
            result["classification"],
            "EXACT_SYNTHETIC_POLE_TOMOGRAPHY_VERIFIED",
        )
        self.assertEqual(result["scaled_inverse_distance_constant"], "9/4")
        self.assertEqual(result["punctured_line_energy_lower_bounds"][-1], "36")

    def test_zero_residue_rejected(self):
        payload = self.payload()
        payload["residue_modulus_sq"] = "0"
        self.resign(payload)
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_dominance_rejected(self):
        payload = self.payload()
        payload["principal_part_dominance"] = "2"
        self.resign(payload)
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_unordered_offsets_rejected(self):
        payload = self.payload()
        payload["horizontal_offsets"][1] = "3/4"
        self.resign(payload)
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_scaled_claim_rejected(self):
        payload = self.payload()
        payload["claimed"]["scaled_inverse_distance_constant"] = "2"
        self.resign(payload)
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_annulus_claim_rejected(self):
        payload = self.payload()
        payload["claimed"]["last_annulus_lower"] = "35"
        self.resign(payload)
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_digest_mutation_rejected(self):
        payload = self.payload()
        payload["local_radius"] = "2"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_boolean_rejected(self):
        payload = self.payload()
        payload["residue_modulus_sq"] = True
        self.resign(payload)
        with self.assertRaises(module.CertificateError):
            module.verify(payload)


if __name__ == "__main__":
    unittest.main()
