from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_log_loewner", ROOT / "verify_log_loewner.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
CERT = ROOT / "certificates" / "synthetic-log-loewner.json"


class LogLoewnerTests(unittest.TestCase):
    def load(self):
        return json.loads(CERT.read_text(encoding="utf-8"))

    def test_synthetic_controls(self):
        result = MODULE.verify(self.load())
        self.assertEqual(result["verdict"], "SYNTHETIC_NEGATIVE_CONTROL")
        rows = {row["id"]: row for row in result["rows"]}
        self.assertEqual(
            rows["online-positive-control"]["status"], "CERTIFIED_NONNEGATIVE"
        )
        self.assertEqual(
            rows["offline-negative-control"]["status"], "CERTIFIED_NEGATIVE"
        )
        self.assertEqual(result["certified_negative_rows"], 1)

    def test_log2_enclosure(self):
        value = MODULE._log2_interval(40)
        self.assertLess(value.lower, Fraction(7, 10))
        self.assertGreater(value.upper, Fraction(69, 100))
        self.assertLess(value.upper - value.lower, Fraction(1, 10**35))

    def test_higher_terms_narrow(self):
        low = MODULE._log2_interval(20)
        high = MODULE._log2_interval(40)
        self.assertLessEqual(low.lower, high.lower)
        self.assertLessEqual(high.upper, low.upper)

    def test_reordered_nodes_rejected(self):
        data = self.load()
        data["rows"][0]["row_points"].reverse()
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_cross_collision_rejected(self):
        data = self.load()
        data["rows"][0]["column_points"][0] = data["rows"][0]["row_points"][0]
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_zero_lower_h_rejected(self):
        data = self.load()
        data["points"][0]["h_interval"]["lower"] = {
            "numerator": 0,
            "denominator": 1,
        }
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_boolean_series_count_rejected(self):
        data = self.load()
        data["log_series_terms"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()
