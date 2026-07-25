from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_modulus_certificate", ROOT / "verify_modulus_certificate.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

CERT = ROOT / "certificates" / "synthetic-modulus-witnesses.json"


class ModulusCertificateTests(unittest.TestCase):
    def load(self):
        return json.loads(CERT.read_text(encoding="utf-8"))

    def test_committed_synthetic_controls(self):
        result = MODULE.verify(self.load())
        self.assertEqual(result["verdict"], "SYNTHETIC_NEGATIVE_CONTROL")
        self.assertEqual(result["certified_negative_rows"], 2)
        statuses = {row["id"]: row["status"] for row in result["rows"]}
        self.assertEqual(statuses["online-monotonicity"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(statuses["online-second-divided-difference"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(statuses["offline-monotonicity-control"], "CERTIFIED_NEGATIVE")
        self.assertEqual(statuses["synthetic-log-concavity-control"], "CERTIFIED_NEGATIVE")

    def test_square_interval_crossing_zero(self):
        value = MODULE.Interval(Fraction(-2), Fraction(3))
        self.assertEqual(MODULE.square_interval(value), MODULE.Interval(Fraction(0), Fraction(9)))

    def test_normalization_mutation_rejected(self):
        data = self.load()
        data["normalization_id"] = "wrong"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reversed_monotonicity_nodes_rejected(self):
        data = self.load()
        row = data["rows"][0]
        row["left"], row["right"] = row["right"], row["left"]
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_boolean_rational_rejected(self):
        data = self.load()
        data["ordinate"]["numerator"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_point_digest_mutation_rejected(self):
        data = self.load()
        data["points"][0]["point_sha256"] = "0" * 64
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_offline_midpoint_mutation_removes_that_negative(self):
        data = self.load()
        point = next(item for item in data["points"] if item["id"] == "offline-1")
        point["xi_rectangle"]["real"]["lower"] = {"numerator": -4, "denominator": 5}
        point["xi_rectangle"]["real"]["upper"] = {"numerator": -4, "denominator": 5}
        result = MODULE.verify(data)
        statuses = {row["id"]: row["status"] for row in result["rows"]}
        self.assertEqual(statuses["offline-monotonicity-control"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(result["certified_negative_rows"], 1)


if __name__ == "__main__":
    unittest.main()
