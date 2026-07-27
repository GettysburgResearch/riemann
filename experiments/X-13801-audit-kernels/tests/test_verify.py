from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("audit_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)

SCHEMA = module.SCHEMA


class AuditKernelTests(unittest.TestCase):
    def chain(self):
        return {
            "schema": SCHEMA,
            "kind": "saturated-sign-chain",
            "lower": "0",
            "upper": "4",
            "total_multiplicity": 3,
            "left_endpoint_zero_free": True,
            "right_endpoint_zero_free": True,
            "samples": [
                {"t": "1/2", "sign": 1},
                {"t": "3/2", "sign": -1},
                {"t": "5/2", "sign": 1},
                {"t": "7/2", "sign": -1},
            ],
        }

    def test_saturated_chain(self):
        result = module.verify(self.chain())
        self.assertEqual(result["simple_line_zero_intervals"], 3)
        self.assertEqual(result["off_line_multiplicity_remaining"], 0)

    def test_missing_endpoint_gate_rejected(self):
        payload = self.chain()
        payload["left_endpoint_zero_free"] = False
        with self.assertRaises(module.AuditError):
            module.verify(payload)

    def test_nonalternating_chain_rejected(self):
        payload = self.chain()
        payload["samples"][2]["sign"] = -1
        with self.assertRaises(module.AuditError):
            module.verify(payload)

    def test_global_retirement_without_locality_rejected(self):
        result = module.verify(
            {
                "schema": SCHEMA,
                "kind": "candidate-retirement",
                "candidate_kind": "GLOBAL_PICK_FUNCTIONAL",
                "locality_gate_proved": False,
                "complete_complement_bound": False,
            }
        )
        self.assertEqual(result["status"], "RETIREMENT_REJECTED")

    def test_global_retirement_with_complement_allowed(self):
        result = module.verify(
            {
                "schema": SCHEMA,
                "kind": "candidate-retirement",
                "candidate_kind": "GLOBAL_WEIL_FUNCTIONAL",
                "locality_gate_proved": False,
                "complete_complement_bound": True,
            }
        )
        self.assertEqual(result["status"], "RETIREMENT_PERMITTED")

    def test_local_count_predicate_allowed(self):
        result = module.verify(
            {
                "schema": SCHEMA,
                "kind": "candidate-retirement",
                "candidate_kind": "LOCAL_COUNT_PREDICATE",
                "locality_gate_proved": False,
                "complete_complement_bound": False,
            }
        )
        self.assertEqual(result["status"], "RETIREMENT_PERMITTED")

    def test_boolean_total_rejected(self):
        payload = self.chain()
        payload["total_multiplicity"] = True
        with self.assertRaises(module.AuditError):
            module.verify(payload)


if __name__ == "__main__":
    unittest.main()
