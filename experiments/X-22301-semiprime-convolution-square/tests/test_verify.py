from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x22301_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)

CERTIFICATE = ROOT / "certificates" / "synthetic.json"


class ConvolutionSquareTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def test_central_replay(self):
        result = module.verify(copy.deepcopy(self.payload))
        self.assertEqual(
            result["proof_object_sha256"],
            "4db99b1c11db3400fa0256102217228716c945d4a10305fc338b1a741408f500",
        )
        self.assertEqual(result["direct_convolution"], result["grouped_product_convolution"])
        self.assertEqual(result["h2_norm_sq"], result["h1_square_norm"])

    def test_window_mutation_changes_result(self):
        payload = copy.deepcopy(self.payload)
        payload["window"]["1"] = "-3"
        result = module.verify(payload)
        self.assertNotEqual(
            result["proof_object_sha256"],
            "4db99b1c11db3400fa0256102217228716c945d4a10305fc338b1a741408f500",
        )

    def test_false_h2_claim_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["claimed"]["h2_norm_sq"] = "3"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_h1_claim_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["claimed"]["h1_square_norm"] = "3"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_identity_growth_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["claimed"]["identity_point_evaluation_sq"] = "15"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_duplicate_atom_name_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["atoms"][1]["name"] = payload["atoms"][0]["name"]
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_boolean_block_size_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["identity_orbit_block_size"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_zero_window_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["window"] = {"0": "0"}
        with self.assertRaises(module.CertificateError):
            module.verify(payload)


if __name__ == "__main__":
    unittest.main()
