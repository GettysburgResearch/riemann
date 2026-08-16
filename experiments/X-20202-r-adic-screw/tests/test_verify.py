from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x20202_verify", ROOT / "verify.py")
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
            result["verdict"], "EXACT_R_ADIC_RENORMALIZATION_ALGEBRA_VERIFIED"
        )
        self.assertEqual(
            result["negative_prefix_exponent"],
            {"numerator": "1", "denominator": "3"},
        )

    def test_reject_small_dilation(self) -> None:
        data = copy.deepcopy(self.base)
        data["r"] = 1
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_boolean_integer(self) -> None:
        data = copy.deepcopy(self.base)
        data["r"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_bad_prime_sign(self) -> None:
        data = copy.deepcopy(self.base)
        data["prime_exponents"][0]["sign"] = "positive"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_nonpositive_lerch_node(self) -> None:
        data = copy.deepcopy(self.base)
        data["lerch_y"][0] = {"numerator": "0", "denominator": "1"}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_mixture_residue_mutation(self) -> None:
        data = copy.deepcopy(self.base)
        data["mixture"]["descendant_multiplicities"][1] = 2
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_cocycle_mutation(self) -> None:
        data = copy.deepcopy(self.base)
        data["cocycle"]["psi_rst"] = {"numerator": "18", "denominator": "19"}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_reject_bad_schema(self) -> None:
        data = copy.deepcopy(self.base)
        data["schema"] = "wrong"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()
