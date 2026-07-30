from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("radical_bridge_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)

CERTIFICATE = ROOT / "certificates" / "synthetic-exact.json"


class RadicalBridgeTests(unittest.TestCase):
    def payload(self):
        return json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def test_exact_certificate(self):
        result = module.verify(self.payload())
        self.assertEqual(result["classification"], "EXACT_FINITE_ALGEBRA")
        self.assertEqual(
            result["gaussian_moments"]["two_m4_minus_three_m2"], "0"
        )
        self.assertEqual(result["radical_decomposition"]["q_local_local"], "1")
        self.assertEqual(result["radical_decomposition"]["q_tail_tail"], "1")
        self.assertEqual(result["prolate_repair"]["alpha"], "-15/434")
        self.assertEqual(result["prolate_repair"]["beta"], "-16/651")

    def test_bad_gaussian_moment_rejected(self):
        payload = self.payload()
        payload["gaussian_moments"]["normalized_fourth_moment"] = "2/3"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_radical_rejected(self):
        payload = self.payload()
        payload["radical_decomposition"]["radical"][1] = 2
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_decomposition_drift_rejected(self):
        payload = self.payload()
        payload["radical_decomposition"]["tail"][2] = 1
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_equal_signed_eigenvalues_rejected(self):
        payload = self.payload()
        payload["prolate_repair"]["theta2"] = "4/5"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_zero_mode_value_rejected(self):
        payload = self.payload()
        payload["prolate_repair"]["mode2_value"] = 0
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_nonzero_initial_integral_rejected(self):
        payload = self.payload()
        payload["prolate_repair"]["initial_integral"] = "1/100"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_boolean_as_integer_rejected(self):
        payload = self.payload()
        payload["radical_decomposition"]["local"][0] = True
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_nonsymmetric_matrix_rejected(self):
        payload = self.payload()
        payload["radical_decomposition"]["matrix"][0][1] = 0
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_result_digest_is_deterministic(self):
        first = module.verify(self.payload())
        second = module.verify(copy.deepcopy(self.payload()))
        self.assertEqual(
            first["exact_proof_object_sha256"], second["exact_proof_object_sha256"]
        )


if __name__ == "__main__":
    unittest.main()
