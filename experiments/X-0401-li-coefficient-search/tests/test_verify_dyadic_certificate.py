from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "li_verify", ROOT / "verify_dyadic_certificate.py"
)
assert SPEC and SPEC.loader
li_verify = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = li_verify
SPEC.loader.exec_module(li_verify)


class LiDyadicVerifierTests(unittest.TestCase):
    def load(self, name: str) -> dict:
        return json.loads((ROOT / "certificates" / name).read_text(encoding="utf-8"))

    def test_strict_local_negative_is_accepted(self) -> None:
        result = li_verify.verify(self.load("synthetic-local-negative.json"))
        self.assertTrue(result["certified_negative"])
        self.assertLess(result["lambda_interval"]["upper"]["numerator"], 0)

    def test_local_zero_touch_is_rejected(self) -> None:
        result = li_verify.verify(self.load("synthetic-local-zero-touch.json"))
        self.assertFalse(result["certified_negative"])
        self.assertEqual(result["lambda_interval"]["upper"]["numerator"], 0)

    def test_strict_cauchy_negative_is_accepted(self) -> None:
        result = li_verify.verify(self.load("synthetic-cauchy-negative.json"))
        self.assertTrue(result["certified_negative"])
        self.assertEqual(
            result["details"]["alias_bound"],
            {"numerator": 1, "denominator": 390},
        )

    def test_cauchy_alias_widening_can_reject(self) -> None:
        result = li_verify.verify(self.load("synthetic-cauchy-zero-touch.json"))
        self.assertFalse(result["certified_negative"])
        self.assertGreaterEqual(result["lambda_interval"]["upper"]["numerator"], 0)

    def test_missing_local_input_is_rejected(self) -> None:
        data = self.load("synthetic-local-negative.json")
        data["local"]["B"].pop()
        with self.assertRaises(li_verify.CertificateError):
            li_verify.verify(data)

    def test_invalid_radii_are_rejected(self) -> None:
        data = self.load("synthetic-cauchy-negative.json")
        data["cauchy_dft"]["radius_outer"] = {"numerator": 1, "scale_bits": 1}
        with self.assertRaises(li_verify.CertificateError):
            li_verify.verify(data)

    def test_imaginary_interval_must_contain_zero(self) -> None:
        data = self.load("synthetic-cauchy-negative.json")
        data["cauchy_dft"]["dft_imag"] = {
            "lower_num": 1,
            "upper_num": 2,
            "scale_bits": 20,
        }
        with self.assertRaises(li_verify.CertificateError):
            li_verify.verify(data)

    def test_negative_outer_bound_is_rejected(self) -> None:
        data = self.load("synthetic-cauchy-negative.json")
        data["cauchy_dft"]["outer_max_abs_upper"] = {
            "numerator": -1,
            "scale_bits": 7,
        }
        with self.assertRaises(li_verify.CertificateError):
            li_verify.verify(data)

    def test_sample_count_must_reach_index(self) -> None:
        data = self.load("synthetic-cauchy-negative.json")
        data["n"] = 5
        with self.assertRaises(li_verify.CertificateError):
            li_verify.verify(data)

    def test_schema_is_strict(self) -> None:
        data = self.load("synthetic-local-negative.json")
        data["schema"] = "wrong"
        with self.assertRaises(li_verify.CertificateError):
            li_verify.verify(data)


if __name__ == "__main__":
    unittest.main()
