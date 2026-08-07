from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x22801_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class CriticalLocalBohrTests(unittest.TestCase):
    def certificate(self):
        return {
            "schema": module.SCHEMA,
            "max_D": 16,
            "ratio_upper": [9, 4],
            "expected_max_D": 10,
            "expected_max_ratio": [32421033, 18019750],
        }

    def test_exact_replay(self):
        result = module.verify(self.certificate())
        self.assertEqual(result["maximum_ratio_D"], 10)
        self.assertEqual(result["maximum_ratio"], "32421033/18019750")
        self.assertEqual(result["coefficient_identity_checks"], 1234)

    def test_wrong_schema_rejected(self):
        payload = self.certificate()
        payload["schema"] = "wrong"
        with self.assertRaises(module.VerificationError):
            module.verify(payload)

    def test_boolean_dimension_rejected(self):
        payload = self.certificate()
        payload["max_D"] = True
        with self.assertRaises(module.VerificationError):
            module.verify(payload)

    def test_understated_ratio_rejected(self):
        payload = self.certificate()
        payload["ratio_upper"] = [7, 4]
        with self.assertRaises(module.VerificationError):
            module.verify(payload)

    def test_wrong_maximum_location_rejected(self):
        payload = self.certificate()
        payload["expected_max_D"] = 9
        with self.assertRaises(module.VerificationError):
            module.verify(payload)

    def test_wrong_maximum_ratio_rejected(self):
        payload = self.certificate()
        payload["expected_max_ratio"] = [1, 1]
        with self.assertRaises(module.VerificationError):
            module.verify(payload)

    def test_oversized_regression_rejected(self):
        payload = self.certificate()
        payload["max_D"] = 65
        with self.assertRaises(module.VerificationError):
            module.verify(payload)

    def test_coefficient_formula(self):
        self.assertGreater(module.check_reduced_coefficient_formula(12), 0)


if __name__ == "__main__":
    unittest.main()
