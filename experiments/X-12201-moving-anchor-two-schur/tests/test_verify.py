from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x12201_verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)
CERTIFICATE = ROOT / "certificates" / "synthetic-two-schur.json"


def as_fraction(value):
    return Fraction(int(value["numerator"]), int(value["denominator"]))


class MovingAnchorTwoSchurTests(unittest.TestCase):
    def load(self):
        return json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def test_committed_certificate(self):
        result = VERIFY.verify_certificate(self.load())
        self.assertEqual(result["status"], "EXACT_SYNTHETIC_TWO_SCHUR_REPLAY")
        self.assertEqual(as_fraction(result["theta0"]), Fraction(101, 135))
        self.assertEqual(as_fraction(result["upper"]), Fraction(541, 720))
        self.assertEqual(as_fraction(result["admissible_width"]), Fraction(7, 2160))
        statuses = {case["id"]: case["status"] for case in result["cases"]}
        self.assertEqual(statuses["interior"], "INTERIOR_ADMISSIBLE")
        self.assertEqual(statuses["lower-witness"], "LOWER_SQUARE_VIOLATION")
        self.assertEqual(statuses["upper-witness"], "UPPER_SHIFTED_SQUARE_VIOLATION")

    def test_exact_witness_values(self):
        result = VERIFY.verify_certificate(self.load())
        cases = {case["id"]: case for case in result["cases"]}
        self.assertEqual(
            as_fraction(cases["interior"]["lower_square_value"]), Fraction(1, 540)
        )
        self.assertEqual(
            as_fraction(cases["interior"]["upper_shifted_square_value"]),
            Fraction(1, 360),
        )
        self.assertEqual(
            as_fraction(cases["lower-witness"]["lower_square_value"]),
            Fraction(-13, 270),
        )
        self.assertEqual(
            as_fraction(cases["upper-witness"]["upper_shifted_square_value"]),
            Fraction(-7, 72),
        )

    def test_width_identity(self):
        result = VERIFY.verify_certificate(self.load())
        self.assertEqual(as_fraction(result["old_width_value"]), Fraction(7, 1080))
        self.assertEqual(
            as_fraction(result["old_width_value"]),
            Fraction(2) * as_fraction(result["admissible_width"]),
        )
        polynomial = [as_fraction(value) for value in result["old_width_polynomial"]]
        self.assertEqual(len(polynomial), 5)

    def test_claimed_threshold_mutation_rejected(self):
        data = self.load()
        data["claimed"]["theta0"]["numerator"] = "102"
        with self.assertRaisesRegex(VERIFY.CertificateError, "theta0 mismatch"):
            VERIFY.verify_certificate(data)

    def test_status_mutation_rejected(self):
        data = self.load()
        data["cases"][1]["expected_status"] = "INTERIOR_ADMISSIBLE"
        with self.assertRaisesRegex(VERIFY.CertificateError, "expected status mismatch"):
            VERIFY.verify_certificate(data)

    def test_nonpositive_anchor_rejected(self):
        data = self.load()
        data["t"] = {"numerator": "0", "denominator": "1"}
        with self.assertRaisesRegex(VERIFY.CertificateError, "must be positive"):
            VERIFY.verify_certificate(data)

    def test_boolean_is_not_integer(self):
        data = self.load()
        data["old_moments"][0]["numerator"] = True
        with self.assertRaisesRegex(VERIFY.CertificateError, "must not be Boolean"):
            VERIFY.verify_certificate(data)

    def test_boundary_is_not_promoted(self):
        result = VERIFY.verify_certificate(self.load())
        cases = {case["id"]: case for case in result["cases"]}
        self.assertEqual(cases["lower-boundary"]["status"], "LOWER_BOUNDARY")
        self.assertEqual(cases["upper-boundary"]["status"], "UPPER_BOUNDARY")
        self.assertEqual(
            as_fraction(cases["lower-boundary"]["lower_square_value"]), Fraction(0)
        )
        self.assertEqual(
            as_fraction(cases["upper-boundary"]["upper_shifted_square_value"]),
            Fraction(0),
        )


if __name__ == "__main__":
    unittest.main()
