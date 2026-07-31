from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("zero_obstruction_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


def load() -> dict:
    return json.loads((ROOT / "certificates" / "synthetic.json").read_text(encoding="utf-8"))


class ZeroEvaluationObstructionTests(unittest.TestCase):
    def test_exact_control(self) -> None:
        result = verify.verify(load())
        self.assertEqual(result["status"], "CERTIFIED_POSITIVE_RADICAL_APPROXIMATION_OBSTRUCTION")
        self.assertEqual(
            result["verification_sha256"],
            "475f0f5955170c08c6cf2477d0d60f90dde71ea3539e21593ea8704bcf87d054",
        )
        self.assertEqual(result["distance_lower"], {"numerator": "2", "denominator": "5"})

    def test_false_singular_floor_rejected(self) -> None:
        data = load()
        data["sigma_lower_squared"] = {"numerator": "2", "denominator": "1"}
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_oversized_quotient_rejected(self) -> None:
        data = load()
        data["quotient_lower"] = {"numerator": "3", "denominator": "4"}
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_nonpositive_obstruction_rejected(self) -> None:
        data = load()
        data["tail_upper"] = {"numerator": "1", "denominator": "2"}
        data["distance_lower"] = {"numerator": "0", "denominator": "1"}
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_metric_mismatch_rejected(self) -> None:
        data = load()
        data["metric_gram"][0][1] = {"numerator": "1", "denominator": "3"}
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_missing_zero_gate_rejected(self) -> None:
        data = load()
        data["certified_zero_gate"] = False
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_boolean_rejected(self) -> None:
        data = load()
        data["tail_upper"]["numerator"] = True
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)


if __name__ == "__main__":
    unittest.main()
