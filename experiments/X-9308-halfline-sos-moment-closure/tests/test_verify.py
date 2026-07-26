from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x9308_verify", ROOT / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
REAL = ROOT.parents[0] / "X-9306-real-log-portfolio-search" / "results" / "basis.json"


class HalfLineMomentClosureTests(unittest.TestCase):
    def write_basis(self, intervals):
        payload = {
            "schema": MODULE.SCHEMA,
            "classification": "SYNTHETIC_MODEL",
            "basis_row_count": len(intervals),
            "basis_rows": [
                {
                    "degree": degree,
                    "lower_exact_decimal": str(lower),
                    "upper_exact_decimal": str(upper),
                }
                for degree, (lower, upper) in enumerate(intervals)
            ],
        }
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(payload, handle)
        handle.close()
        self.addCleanup(Path(handle.name).unlink)
        return Path(handle.name)

    def test_real_pr103_certificate_digest(self):
        result = MODULE.verify(REAL, Fraction(1, 100000))
        self.assertEqual(
            result["verdict"],
            "CERTIFIED_POSITIVE_FULL_HALF_LINE_NONNEGATIVE_POLYNOMIAL_CONE",
        )
        self.assertEqual(result["h0_dimension"], 8)
        self.assertEqual(result["h1_dimension"], 7)
        self.assertEqual(
            result["exact_proof_object_sha256"],
            "7028c2688bcd8ca783e98977bd2da6247fd70bc59f4d6f78b7df7f05a5c6096b",
        )

    def test_positive_factorial_moments(self):
        moments = [1, 1, 2, 6, 24]
        path = self.write_basis([(value, value) for value in moments])
        result = MODULE.verify(path, Fraction(1, 100))
        self.assertEqual(result["degree_bound"], 4)
        self.assertEqual(result["h0_dimension"], 3)
        self.assertEqual(result["h1_dimension"], 2)

    def test_indefinite_hankel_rejected(self):
        path = self.write_basis([(1, 1), (0, 0), (-1, -1), (0, 0), (1, 1)])
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(path, Fraction(1, 100000))

    def test_wide_interval_box_rejected(self):
        moments = [(Fraction(1, 2), Fraction(3, 2)), (1, 1), (2, 2), (6, 6), (24, 24)]
        path = self.write_basis(moments)
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(path, Fraction(1, 100))

    def test_reversed_interval_rejected(self):
        path = self.write_basis([(2, 1), (1, 1)])
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(path, Fraction(1, 100))

    def test_nonconsecutive_degree_rejected(self):
        payload = {
            "schema": MODULE.SCHEMA,
            "classification": "SYNTHETIC_MODEL",
            "basis_row_count": 2,
            "basis_rows": [
                {"degree": 0, "lower_exact_decimal": "1", "upper_exact_decimal": "1"},
                {"degree": 2, "lower_exact_decimal": "1", "upper_exact_decimal": "1"},
            ],
        }
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(payload, handle)
        handle.close()
        self.addCleanup(Path(handle.name).unlink)
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(Path(handle.name), Fraction(1, 100))

    def test_boolean_degree_rejected(self):
        payload = {
            "schema": MODULE.SCHEMA,
            "classification": "SYNTHETIC_MODEL",
            "basis_row_count": 2,
            "basis_rows": [
                {"degree": False, "lower_exact_decimal": "1", "upper_exact_decimal": "1"},
                {"degree": 1, "lower_exact_decimal": "1", "upper_exact_decimal": "1"},
            ],
        }
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(payload, handle)
        handle.close()
        self.addCleanup(Path(handle.name).unlink)
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(Path(handle.name), Fraction(1, 100))


if __name__ == "__main__":
    unittest.main()
