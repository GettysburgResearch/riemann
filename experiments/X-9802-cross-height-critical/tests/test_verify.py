from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x9802_verify", HERE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)


class VerifyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads(
            (HERE / "certificates" / "synthetic-negative.json").read_text()
        )

    def test_synthetic_negative_and_response_certificate(self) -> None:
        result = VERIFY.verify(copy.deepcopy(self.base))
        self.assertEqual(result["verdict"], "SYNTHETIC_STRICT_SEPARATION")
        self.assertEqual(result["response_certificate"]["derivative_degree"], 9)
        self.assertEqual(
            result["response_certificate"]["distinct_real_derivative_roots"], 5
        )
        self.assertTrue(
            all(
                VERIFY.rational(row["response_interval"]["lower"], "lower") > 0
                for row in result["response_certificate"]["critical_points"]
            )
        )

    def test_height_sum_mutation_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["terms"][0]["beta"]["numerator"] -= 1
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_missing_root_interval_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["critical_certificate"]["root_intervals"].pop()
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_overlapping_root_intervals_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["critical_certificate"]["root_intervals"][1] = copy.deepcopy(
            data["critical_certificate"]["root_intervals"][0]
        )
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_reversed_response_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        for term in data["terms"]:
            term["beta"]["numerator"] *= -1
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_nonpositive_modulus_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["heights"][0]["points"][0]["h_interval"]["lower"]["numerator"] = 0
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_bad_critical_gate_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["critical_certificate"]["status"] = "GRID_ONLY"
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_missing_production_digest_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["classification"] = VERIFY.PRODUCTION
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)


if __name__ == "__main__":
    unittest.main()
