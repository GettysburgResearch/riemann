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
        self.assertEqual(out["status"], "EXACT_CUMULATIVE_WEYL_GREEN_JORDAN_ALGEBRA")

    def test_false_flow_factor(self):
        bad = copy.deepcopy(self.data)
        bad["flow_control"]["claimed_weyl_weight"]["numerator"] = "30"
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)

    def test_bad_right_inverse(self):
        bad = copy.deepcopy(self.data)
        bad["green_control"]["E"][0][0]["numerator"] = "0"
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)

    def test_noncontraction(self):
        bad = copy.deepcopy(self.data)
        bad["green_control"]["K"][0][0] = {"numerator": "2", "denominator": "1"}
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)

    def test_incomplete_divisors(self):
        bad = copy.deepcopy(self.data)
        bad["jordan_control"]["divisors"].pop()
        bad["jordan_control"]["values"].pop()
        bad["jordan_control"]["claimed_jordan"].pop()
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)

    def test_false_jordan_variance(self):
        bad = copy.deepcopy(self.data)
        bad["jordan_control"]["claimed_variance"]["numerator"] = "1"
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)

    def test_boolean_rejected(self):
        bad = copy.deepcopy(self.data)
        bad["jordan_control"]["n"] = True
        with self.assertRaises(verify.CertificateError):
            verify.verify(bad)


if __name__ == "__main__":
    unittest.main()
