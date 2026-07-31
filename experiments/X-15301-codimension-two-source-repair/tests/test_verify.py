from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("source_repair_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


def load() -> dict:
    return json.loads((ROOT / "certificates" / "synthetic.json").read_text(encoding="utf-8"))


class SourceRepairTests(unittest.TestCase):
    def test_exact_control(self) -> None:
        result = verify.verify(load())
        self.assertEqual(result["status"], "EXACT_CODIMENSION_TWO_SOURCE_REPAIR_VERIFIED")
        self.assertEqual(
            result["verification_sha256"],
            "365a4d600bd0e7a0029f53c595c7ec521cf8202ca95aff60cbd8fdb9e2b50b49",
        )
        self.assertEqual(result["finite_fourier"]["normalized_defect_squared"], {
            "numerator": "79", "denominator": "295"
        })

    def test_integral_drift_rejected(self) -> None:
        data = load()
        data["integrals"][1] = {"numerator": "17", "denominator": "10"}
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_proportional_functionals_rejected(self) -> None:
        data = load()
        data["finite_fourier_eigenvalues"] = [
            {"numerator": "1", "denominator": "2"}
            for _ in range(3)
        ]
        data["integrals"] = [
            {"numerator": "1", "denominator": "2"},
            {"numerator": "1", "denominator": "1"},
            {"numerator": "3", "denominator": "2"},
        ]
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_bad_eigenvalue_rejected(self) -> None:
        data = load()
        data["finite_fourier_eigenvalues"][0] = {
            "numerator": "11", "denominator": "10"
        }
        data["integrals"][0] = {"numerator": "11", "denominator": "10"}
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_boolean_integer_rejected(self) -> None:
        data = load()
        data["values_at_zero"][0]["numerator"] = True
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_missing_orthonormal_gate_rejected(self) -> None:
        data = load()
        data["declares_orthonormal_modes"] = False
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)


if __name__ == "__main__":
    unittest.main()
