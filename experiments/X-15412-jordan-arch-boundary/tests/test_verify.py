from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify import CertificateError, verify  # noqa: E402


class VerifyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads((ROOT / "certificates" / "synthetic.json").read_text())

    def test_committed_certificate(self) -> None:
        result = verify(copy.deepcopy(self.data))
        self.assertEqual(result["status"], "EXACT_JORDAN_ARCHIMEDEAN_BOUNDARY_ALGEBRA")

    def test_false_jordan_norm_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["jordan"]["claimed_norm_squared"]["numerator"] = "1"
        with self.assertRaises(CertificateError):
            verify(data)

    def test_missing_divisor_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        del data["jordan"]["conditional"]["values"]["6"]
        with self.assertRaises(CertificateError):
            verify(data)

    def test_false_arch_score_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["archimedean"]["claimed_score"]["numerator"] = "2"
        with self.assertRaises(CertificateError):
            verify(data)

    def test_false_boundary_trace_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["cauchy_boundary"]["claimed_endpoint_trace"]["numerator"] = "0"
        with self.assertRaises(CertificateError):
            verify(data)

    def test_false_pole_limit_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["pole_zero"]["claimed_signed_limit"]["denominator"] = "29"
        with self.assertRaises(CertificateError):
            verify(data)

    def test_boolean_integer_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["jordan"]["parents"][0]["n"] = True
        with self.assertRaises(CertificateError):
            verify(data)

    def test_wrong_omega_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["jordan"]["omega"]["numerator"] = "2"
        with self.assertRaises(CertificateError):
            verify(data)


if __name__ == "__main__":
    unittest.main()
