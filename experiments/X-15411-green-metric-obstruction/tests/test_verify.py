from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


class TestVerifier(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "certificates" / "synthetic.json").read_text())

    def test_valid(self):
        out = verify.verify(copy.deepcopy(self.data))
        self.assertEqual(out["status"], "EXACT_GREEN_METRIC_SIMILARITY_OBSTRUCTION")
        self.assertTrue(out["quotient_isometry"])

    def test_false_T(self):
        bad = copy.deepcopy(self.data)
        bad["claimed_T"][0][1]["numerator"] = "1"
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)

    def test_bad_right_inverse(self):
        bad = copy.deepcopy(self.data)
        bad["E"][0][0]["numerator"] = "1"
        bad["E"][0][0]["denominator"] = "3"
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)

    def test_nonunitary_K(self):
        bad = copy.deepcopy(self.data)
        bad["K"][0][1]["numerator"] = "2"
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)

    def test_false_physical_norm(self):
        bad = copy.deepcopy(self.data)
        bad["claimed_physical_norm_squared"]["numerator"] = "3"
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)

    def test_false_quotient_gram(self):
        bad = copy.deepcopy(self.data)
        bad["claimed_quotient_gram"][0][0]["numerator"] = "1"
        bad["claimed_quotient_gram"][0][0]["denominator"] = "5"
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)

    def test_boolean_rejected(self):
        bad = copy.deepcopy(self.data)
        bad["C"][0][0]["numerator"] = True
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)


if __name__ == "__main__":
    unittest.main()
