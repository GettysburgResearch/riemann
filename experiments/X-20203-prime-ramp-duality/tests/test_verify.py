from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x20203_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class VerifyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads(
            (ROOT / "certificates" / "synthetic.json").read_text(encoding="utf-8")
        )

    def test_committed_certificate(self) -> None:
        result = MODULE.verify(copy.deepcopy(self.base))
        self.assertTrue(result["verified"])
        self.assertEqual(
            result["verdict"],
            "EXACT_PRIME_RAMP_AUTOCORRELATION_IDENTITIES_VERIFIED",
        )
        self.assertEqual(result["half_ratio"], {"numerator": "1", "denominator": "6"})

    def test_reject_lambda_mutation(self) -> None:
        data = copy.deepcopy(self.base)
        data["lambda"][0]["numerator"] = "31"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_ramp_sample_mutation(self) -> None:
        data = copy.deepcopy(self.base)
        data["samples"][3]["value"]["numerator"] = "-2"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_half_ratio_mutation(self) -> None:
        data = copy.deepcopy(self.base)
        data["half_ratio"] = {"numerator": "1", "denominator": "5"}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_zero_factor(self) -> None:
        data = copy.deepcopy(self.base)
        data["q"] = [
            {"numerator": "0", "denominator": "1"},
            {"numerator": "0", "denominator": "1"},
            {"numerator": "0", "denominator": "1"},
        ]
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_boolean_integer(self) -> None:
        data = copy.deepcopy(self.base)
        data["q"][0]["numerator"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_out_of_support_sample(self) -> None:
        data = copy.deepcopy(self.base)
        data["samples"][0]["s"] = {"numerator": "7", "denominator": "2"}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()
