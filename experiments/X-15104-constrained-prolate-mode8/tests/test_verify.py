from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("mode8_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)

CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class Mode8VerifierTests(unittest.TestCase):
    def test_exact_certificate(self):
        result = module.verify(copy.deepcopy(CERT))
        self.assertEqual(
            result["classification"], "CERTIFIED_EXACT_FINITE_PROLATE_ALGEBRA"
        )
        proof = result["proof_object"]
        self.assertEqual(proof["centered_mode_next_floor"], "6197/12500")
        self.assertEqual(proof["residual_squared"], "729/78125000")
        self.assertEqual(proof["fuchs_4_to_8_rational_coefficient"], "105/4096")

    def test_boolean_rejected(self):
        payload = copy.deepcopy(CERT)
        payload["next_index"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_target_drift_rejected(self):
        payload = copy.deepcopy(CERT)
        payload["complement_basis"][0][0] = "4"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_incomplete_complement_rejected(self):
        payload = copy.deepcopy(CERT)
        payload["complement_basis"] = payload["complement_basis"][:1]
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_nonmonotone_defects_rejected(self):
        payload = copy.deepcopy(CERT)
        payload["defects"][2] = "1/2000"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_functional_norm_rejected(self):
        payload = copy.deepcopy(CERT)
        payload["functional_norm2"] = "25"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_floor_rejected(self):
        payload = copy.deepcopy(CERT)
        payload["claimed"]["centered_floor"] = "1/2"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_residual_rejected(self):
        payload = copy.deepcopy(CERT)
        payload["claimed"]["residual_squared"] = "1/100"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_fuchs_constant_rejected(self):
        payload = copy.deepcopy(CERT)
        payload["fuchs_ratio"]["rational_coefficient"] = "105/2048"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_fuchs_exponent_rejected(self):
        payload = copy.deepcopy(CERT)
        payload["fuchs_ratio"]["lambda_power"] = -7
        with self.assertRaises(module.CertificateError):
            module.verify(payload)


if __name__ == "__main__":
    unittest.main()
