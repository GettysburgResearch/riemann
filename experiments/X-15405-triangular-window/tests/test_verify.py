from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("x15405verify", ROOT / "verify.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
assert spec.loader is not None
spec.loader.exec_module(module)
CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class TriangularWindowTests(unittest.TestCase):
    def test_committed_certificate(self):
        out = module.verify(copy.deepcopy(CERT))
        self.assertEqual(out["status"], "EXACT_SYNTHETIC_TRIANGULAR_WINDOW_ALGEBRA")
        self.assertEqual(out["normalized_l2_square"], {"numerator": "8", "denominator": "3"})
        self.assertEqual(out["direct_evaluation"], {"numerator": "1", "denominator": "15"})

    def test_false_coefficient_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["claimed"]["difference_coefficients"][2]["numerator"] = 6
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_false_norm_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["claimed"]["normalized_l2_square"]["numerator"] = 7
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_false_value_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["claimed"]["evaluation"]["numerator"] = 2
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_wrong_q_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["q"] = {"numerator": 3, "denominator": 1}
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_nonpositive_weight_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["events"][0]["weight"] = {"numerator": 0, "denominator": 1}
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_boolean_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["q"]["numerator"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_malformed_events_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["events"] = []
        with self.assertRaises(module.CertificateError):
            module.verify(bad)


if __name__ == "__main__":
    unittest.main()
