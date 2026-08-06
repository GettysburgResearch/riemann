from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x22101_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
CERTIFICATE = ROOT / "certificates" / "synthetic.json"


class PrimeRampWaveletTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def test_central_replay(self):
        result = MODULE.verify(copy.deepcopy(self.payload))
        self.assertEqual(result["pole_model_factor"], "0")
        self.assertEqual(result["narrow_l2_prefactor"], "20/3")
        self.assertEqual(result["diagonal_hardy_exponent"], "1/2")
        self.assertEqual(
            result["proof_object_sha256"],
            "bc8da6a56ff84ed48d33706d2c4478837b6dc9169f784d7d93afec6ff4705a71",
        )

    def test_coefficient_mutation_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["expected_coefficients"][3]["coefficient"] = "5"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)

    def test_duplicate_shift_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["expected_coefficients"][1] = copy.deepcopy(
            payload["expected_coefficients"][0]
        )
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)

    def test_wrong_pole_eigenvalue_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["pole_shift_eigenvalue"] = "2/3"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)

    def test_wrong_triangular_norm_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["phi_l2_sq"] = "1"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)

    def test_wrong_component_vector_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["component_coefficients"][-1] = "1"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)

    def test_false_diagonal_exponent_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["claimed_diagonal_hardy_exponent"] = "0"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)

    def test_boolean_rational_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["resolution_exponent"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)


if __name__ == "__main__":
    unittest.main()
