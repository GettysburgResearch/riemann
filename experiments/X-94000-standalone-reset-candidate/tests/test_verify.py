from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x94000_verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VERIFY)
BASE = json.loads((ROOT / "certificates" / "control.json").read_text())


class StandaloneResetCandidateTests(unittest.TestCase):
    def test_control_passes(self):
        result = VERIFY.validate_control(copy.deepcopy(BASE))
        self.assertEqual(result["verdict"], "PASS_T94000_STANDALONE_RESET_CANDIDATE_ALGEBRA")

    def test_rejects_schema_drift(self):
        bad = copy.deepcopy(BASE)
        bad["schema"] = "bad"
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_affine_mean_drift(self):
        bad = copy.deepcopy(BASE)
        bad["affine"]["u_bar"] = "3/4"
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_hybrid_identity_drift(self):
        bad = copy.deepcopy(BASE)
        bad["hybrid"]["native"][0] = "4"
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_detail_drift(self):
        bad = copy.deepcopy(BASE)
        bad["observations"]["detail"] = "11"
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_K_drift(self):
        bad = copy.deepcopy(BASE)
        bad["capacity"]["K"] += 1
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_derivative_causality(self):
        bad = copy.deepcopy(BASE)
        bad["firewalls"]["derivative_causal_calls"] = 1
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_rough_lift_parent(self):
        bad = copy.deepcopy(BASE)
        bad["firewalls"]["rough_lift_parent_uses"] = 1
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_bulk_quantizer(self):
        bad = copy.deepcopy(BASE)
        bad["firewalls"]["bulk_quantizers"] = 1
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_forbidden_claim_import(self):
        bad = copy.deepcopy(BASE)
        bad["firewalls"]["imports_L91763"] = 1
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_pr509_dependency(self):
        bad = copy.deepcopy(BASE)
        bad["firewalls"]["pr509_dependency"] = True
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_wrong_endpoint_orientation(self):
        bad = copy.deepcopy(BASE)
        bad["firewalls"]["finite_dual_orientation"] = "F_Lambda>=native_deficit"
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_negative_witness(self):
        self.assertLess(VERIFY.witness_interval()[1], 0)


if __name__ == "__main__":
    unittest.main()
