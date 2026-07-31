from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x18501_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RightInverseCountTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads((ROOT / "certificates" / "synthetic.json").read_text())

    def test_valid_certificate(self) -> None:
        out = MODULE.verify(copy.deepcopy(self.base))
        self.assertTrue(out["verified"])
        self.assertEqual(out["count_upper_bound"], 2)
        self.assertEqual(out["spectral_gap_lower"], {"numerator": 1, "denominator": 2})
        self.assertEqual(out["threshold"], {"numerator": 1, "denominator": 4})

    def test_bad_right_inverse_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["right_inverse"][0][0] = 0
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_bad_kernel_basis_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["kernel_basis"][0][0] = 1
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_incomplete_dimension_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["kernel_basis"] = [[0], [1], [0]]
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_false_full_gram_domination_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["full_certified_zero_gram"][0][0] = {"numerator": 9, "denominator": 10}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_threshold_at_gap_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["omitted_zero_tail_budget"] = {"numerator": 1, "denominator": 4}
        data["beta"] = {"numerator": 1, "denominator": 4}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_false_right_inverse_gram_upper_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["right_inverse_gram_upper"] = 1
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_nonpositive_metric_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["metric_gram"][2][2] = 0
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_boolean_rational_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["beta"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()
