from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SPEC = importlib.util.spec_from_file_location("x14201_verify", ROOT / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text(encoding="utf-8"))


class DyadicFirTests(unittest.TestCase):
    def test_committed_certificate(self) -> None:
        output = MODULE.verify_certificate(copy.deepcopy(CERT))
        self.assertEqual(output["cases"][0]["status"], "NEGATIVE")
        self.assertEqual(output["cases"][0]["form"]["numerator"], "-25")
        self.assertEqual(output["cases"][0]["form"]["denominator"], "128")

    def test_refinement_preserves_physical_form(self) -> None:
        output = MODULE.verify_certificate(copy.deepcopy(CERT))
        self.assertEqual(output["cases"][0]["form"], output["cases"][0]["refinement"]["form"])

    def test_nonzero_sum_rejected(self) -> None:
        mutated = copy.deepcopy(CERT)
        mutated["cases"][0]["coefficients"][-1]["numerator"] = 0
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify_certificate(mutated)

    def test_false_status_rejected(self) -> None:
        mutated = copy.deepcopy(CERT)
        mutated["cases"][0]["expected_status"] = "POSITIVE"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify_certificate(mutated)

    def test_false_expected_value_rejected(self) -> None:
        mutated = copy.deepcopy(CERT)
        mutated["cases"][0]["expected_form"]["numerator"] = -24
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify_certificate(mutated)

    def test_boolean_integer_rejected(self) -> None:
        mutated = copy.deepcopy(CERT)
        mutated["cases"][0]["refinement"]["factor"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify_certificate(mutated)

    def test_invalid_refinement_rejected(self) -> None:
        mutated = copy.deepcopy(CERT)
        mutated["cases"][0]["refinement"]["factor"] = 1
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify_certificate(mutated)


if __name__ == "__main__":
    unittest.main()
