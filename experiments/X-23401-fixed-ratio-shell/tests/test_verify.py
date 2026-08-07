#!/usr/bin/env python3
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x23401_verify", ROOT / "verify.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class FixedRatioShellTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.central = json.loads((ROOT / "certificates" / "exact-c23.json").read_text())

    def mutate(self, field, value):
        item = copy.deepcopy(self.central)
        item.pop("expected_proof_object_sha256", None)
        item[field] = value
        return item

    def assert_rejected(self, certificate):
        with self.assertRaises(MOD.VerificationError):
            MOD.verify(certificate)

    def test_central_certificate(self):
        result = MOD.verify(self.central)
        self.assertTrue(result["verified"])
        self.assertEqual(result["verdict"], "EXACT_FIXED_RATIO_MERTENS_SHELL_ALGEBRA_VERIFIED")

    def test_reject_half_ratio_barrier(self):
        self.assert_rejected(self.mutate("c", {"numerator": "1", "denominator": "2"}))

    def test_reject_wrong_kernel_reciprocal(self):
        self.assert_rejected(self.mutate("kernel_reciprocal_scale", {"numerator": "4", "denominator": "3"}))

    def test_reject_wrong_divisor_sign(self):
        self.assert_rejected(self.mutate("divisor_recurrence_sign", 1))

    def test_reject_wrong_prime_renewal_sign(self):
        self.assert_rejected(self.mutate("prime_renewal_sign", -1))

    def test_reject_wrong_binomial_orientation(self):
        self.assert_rejected(self.mutate("binomial_sign_base", 1))

    def test_reject_wrong_mellin_numerator(self):
        self.assert_rejected(self.mutate("mellin_c_term_sign", 1))

    def test_reject_short_mobius_table(self):
        self.assert_rejected(self.mutate("max_n", 12))

    def test_reject_wrong_digest(self):
        item = copy.deepcopy(self.central)
        item["expected_proof_object_sha256"] = "00" * 32
        self.assert_rejected(item)


if __name__ == "__main__":
    unittest.main()
