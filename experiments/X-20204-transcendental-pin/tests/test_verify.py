from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x20204_verify", ROOT / "verify.py")
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
            result["verdict"], "EXACT_TRANSCENDENTAL_PIN_ALGEBRA_VERIFIED"
        )
        self.assertTrue(result["residue_cannot_vanish"])

    def test_reject_wrong_pin_tap(self) -> None:
        data = copy.deepcopy(self.base)
        data["pin"]["tap"] = 2
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_missing_transcendence_gate(self) -> None:
        data = copy.deepcopy(self.base)
        data["pin"]["classification"] = "FLOATING_APPROXIMATION"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_zero_parent_multiplicity(self) -> None:
        data = copy.deepcopy(self.base)
        data["residue"]["parent_multiplicity"] = 0
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_algebraic_residue_mutation(self) -> None:
        data = copy.deepcopy(self.base)
        data["residue"]["descendant_multiplicities"][1] = 4
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_ramp_mutation(self) -> None:
        data = copy.deepcopy(self.base)
        data["ramp"]["pin_coefficient"] = {"numerator": "1", "denominator": "3"}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_support_exponent_mutation(self) -> None:
        data = copy.deepcopy(self.base)
        data["critical_support"]["pin_exponent"] = {
            "numerator": "1",
            "denominator": "2",
        }
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_boolean_integer(self) -> None:
        data = copy.deepcopy(self.base)
        data["degree"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()
