from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x16201_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)

BASE = json.loads((ROOT / "certificate.json").read_text())


class ExactAuditTests(unittest.TestCase):
    def test_complete_control(self):
        result = module.verify(copy.deepcopy(BASE))
        self.assertEqual(
            result["affine_falsifiers"]["combined_residual_lower_bound"], "3/4"
        )
        self.assertTrue(result["radical_tail"]["factorization_exact"])
        self.assertEqual(
            result["radical_tail"]["scalar_residual"], [["0", "0"], ["0", "0"]]
        )
        self.assertEqual(
            result["tail_scalarization"]["optimal_relative_remainder_squared"],
            "1/25",
        )

    def test_boolean_rational_rejected(self):
        payload = copy.deepcopy(BASE)
        payload["sector_gap"]["source_gap"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_bad_radical_rejected(self):
        payload = copy.deepcopy(BASE)
        payload["radical_tail"]["J"][0][0] = "2"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_nonprojection_rejected(self):
        payload = copy.deepcopy(BASE)
        payload["radical_tail"]["P"][0][0] = "2"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_full_gap_rejected(self):
        payload = copy.deepcopy(BASE)
        payload["sector_gap"]["claimed_full_gap"] = "2"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_blocking_gate_rejected(self):
        payload = copy.deepcopy(BASE)
        payload["logical_gates"]["no_rh_claim"] = False
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_scalarization_claim_rejected(self):
        payload = copy.deepcopy(BASE)
        payload["tail_scalarization"]["claimed_relative_square"] = "1/24"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_nonpositive_tail_gram_rejected(self):
        payload = copy.deepcopy(BASE)
        payload["tail_scalarization"]["D"] = [["1", "2"], ["2", "1"]]
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_schema_rejected(self):
        payload = copy.deepcopy(BASE)
        payload["schema"] = "wrong"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)


if __name__ == "__main__":
    unittest.main()
