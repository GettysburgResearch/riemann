#!/usr/bin/env python3
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x23402_verify", ROOT / "verify.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class EulerAlignedShellTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.central = json.loads((ROOT / "certificates" / "exact-n192.json").read_text())

    def mutate(self, field, value):
        item = copy.deepcopy(self.central)
        item.pop("expected_proof_object_sha256", None)
        item[field] = value
        return item

    def assert_rejected(self, certificate):
        with self.assertRaises(MOD.VerificationError):
            MOD.verify(certificate)

    def test_central(self):
        result = MOD.verify(self.central)
        self.assertTrue(result["verified"])
        self.assertEqual(result["proof_object_sha256"], self.central["expected_proof_object_sha256"])

    def test_reject_wrong_two_adic_pattern(self):
        self.assert_rejected(self.mutate("expected_two_adic_pattern", [1, -1, 1, 0]))

    def test_reject_missing_extra_two_weight(self):
        self.assert_rejected(self.mutate("extra_two_von_mangoldt_copy", 0))

    def test_reject_double_extra_two_weight(self):
        self.assert_rejected(self.mutate("extra_two_von_mangoldt_copy", 2))

    def test_reject_small_limit(self):
        self.assert_rejected(self.mutate("limit", 3))

    def test_reject_bad_schema(self):
        self.assert_rejected(self.mutate("schema", "wrong"))

    def test_reject_bad_digest(self):
        item = copy.deepcopy(self.central)
        item["expected_proof_object_sha256"] = "00" * 32
        self.assert_rejected(item)


if __name__ == "__main__":
    unittest.main()
