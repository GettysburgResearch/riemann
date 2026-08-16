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
            "EXACT_CURVATURE_CORRECTED_TRANSPORT_ALGEBRA_VERIFIED",
        )
        self.assertEqual(
            result["rows"][0]["direct_margin"],
            {"numerator": "1", "denominator": "4"},
        )

    def test_reject_bad_schema(self) -> None:
        data = copy.deepcopy(self.base)
        data["schema"] = "wrong"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_nonconvex_barrier(self) -> None:
        data = copy.deepcopy(self.base)
        data["quadratic_barrier"]["c2"] = {"numerator": "0", "denominator": "1"}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_boolean_integer(self) -> None:
        data = copy.deepcopy(self.base)
        data["rows"][0]["A"]["numerator"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_wrong_dual_coordinate(self) -> None:
        data = copy.deepcopy(self.base)
        data["rows"][0]["tau"] = {"numerator": "4", "denominator": "1"}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_status_mutation(self) -> None:
        data = copy.deepcopy(self.base)
        data["rows"][2]["expected_status"] = "CERTIFIED_POSITIVE"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_transport_atom_binding(self) -> None:
        data = copy.deepcopy(self.base)
        data["transport_blocks"][0]["B_increment"] = {
            "numerator": "3", "denominator": "1"
        }
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_reversed_mass_interval(self) -> None:
        data = copy.deepcopy(self.base)
        data["transport_blocks"][0]["A_right"] = {
            "numerator": "1", "denominator": "1"
        }
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()
