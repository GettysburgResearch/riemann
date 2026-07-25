from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x8301_verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)
CERT = ROOT / "certificates" / "synthetic-green-cases.json"


class EndpointGreenTests(unittest.TestCase):
    def load(self):
        return json.loads(CERT.read_text(encoding="utf-8"))

    def test_committed_certificate(self):
        out = VERIFY.verify_certificate(self.load())
        self.assertEqual(out["status"], "EXACT_SYNTHETIC_GREEN_CERTIFICATES_RECONSTRUCTED")
        statuses = {case["id"]: case["status"] for case in out["cases"]}
        self.assertEqual(statuses["leading-vector-misses-crossing"], "ROBUST_CROSSING")
        self.assertEqual(statuses["robust-no-crossing"], "ROBUST_POSITIVE")
        self.assertEqual(statuses["exact-boundary-is-unresolved"], "UNRESOLVED_MOAT")

    def test_leading_vector_can_miss_crossing(self):
        out = VERIFY.verify_certificate(self.load())
        case = next(x for x in out["cases"] if x["id"] == "leading-vector-misses-crossing")
        self.assertEqual(case["leading_susceptibility"]["numerator"], "0")
        self.assertEqual(case["lambda_interval"]["lower"], {"numerator": "10", "denominator": "1"})
        self.assertEqual(case["determinant_ratio"], {"numerator": "-11", "denominator": "25"})

    def test_complex_phase_orientation(self):
        out = VERIFY.verify_certificate(self.load())
        case = next(x for x in out["cases"] if x["id"] == "complex-phase-crossing")
        self.assertEqual(case["green"]["r"], {"numerator": "1", "denominator": "2"})
        self.assertEqual(case["lambda_interval"]["lower"], {"numerator": "5", "denominator": "2"})
        self.assertEqual(case["status"], "ROBUST_CROSSING")

    def test_nonunit_phase_rejected(self):
        data = self.load()
        data["cases"][0]["phase"] = {"re": "1", "im": "1/100"}
        with self.assertRaisesRegex(VERIFY.CertificateError, "unit modulus"):
            VERIFY.verify_certificate(data)

    def test_mutated_status_rejected(self):
        data = self.load()
        data["cases"][1]["expected_status"] = "ROBUST_CROSSING"
        with self.assertRaisesRegex(VERIFY.CertificateError, "reconstructed"):
            VERIFY.verify_certificate(data)

    def test_duplicate_id_rejected(self):
        data = self.load()
        data["cases"].append(copy.deepcopy(data["cases"][0]))
        with self.assertRaisesRegex(VERIFY.CertificateError, "duplicate"):
            VERIFY.verify_certificate(data)

    def test_claimed_floor_rejected_when_too_large(self):
        data = self.load()
        data["cases"][0]["mu"] = "11/100"
        with self.assertRaisesRegex(VERIFY.CertificateError, "spectral floor"):
            VERIFY.verify_certificate(data)

    def test_residual_green_enclosure_contains_exact_entries(self):
        h = [
            [VERIFY.GQ(Fraction(1, 10)), VERIFY.GQ(), VERIFY.GQ()],
            [VERIFY.GQ(), VERIFY.GQ(Fraction(1, 100)), VERIFY.GQ()],
            [VERIFY.GQ(), VERIFY.GQ(), VERIFY.GQ(Fraction(1, 10))],
        ]
        yu = [VERIFY.GQ(Fraction(9999, 1000)), VERIFY.GQ(), VERIFY.GQ()]
        yw = [VERIFY.GQ(), VERIFY.GQ(), VERIFY.GQ(Fraction(10001, 1000))]
        enc = VERIFY.residual_green_enclosure(h, 0, 2, Fraction(1, 100), yu, yw)
        exact = VERIFY.endpoint_green(h, 0, 2, VERIFY.GQ(1))
        self.assertLessEqual(abs(exact["a"] - enc["a_center"]), enc["a_radius"])
        self.assertLessEqual(abs(exact["d"] - enc["d_center"]), enc["d_radius"])
        self.assertLessEqual((exact["b"] - enc["b_center"]).abs2(), enc["b_radius"] ** 2)

    def test_irrational_sqrt_bounds(self):
        lo, hi = VERIFY.sqrt_bounds(Fraction(20), 80)
        self.assertLessEqual(lo * lo, 20)
        self.assertGreaterEqual(hi * hi, 20)
        self.assertLess(hi - lo, Fraction(1, 2**79))


if __name__ == "__main__":
    unittest.main()
