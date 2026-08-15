from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x93920_verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VERIFY)
BASE = json.loads((ROOT / "certificates" / "control.json").read_text())


class Review503HybridDirectRowTests(unittest.TestCase):
    def test_control_passes(self):
        result = VERIFY.validate_control(copy.deepcopy(BASE))
        self.assertEqual(result["verdict"], "PASS_REVIEW503_SAFE_ANCHORED_VOLTERRA_DIRECT_ROW")

    def test_rejects_derivative_fibre_causality(self):
        bad = copy.deepcopy(BASE)
        bad["route"]["uses_derivative_fibre_causal_generator"] = True
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_l91763_reuse(self):
        bad = copy.deepcopy(BASE)
        bad["route"]["forbidden_claims"] = ["T-92910"]
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_pr509_as_confirmation(self):
        bad = copy.deepcopy(BASE)
        bad["route"]["uses_pr509_as_confirmation"] = True
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_missing_anchored_import(self):
        bad = copy.deepcopy(BASE)
        bad["route"]["anchored_target_lorenz_import"] = False
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_dropped_small_q(self):
        bad = copy.deepcopy(BASE)
        bad["route"]["small_q_included"] = False
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_branchwise_detail(self):
        bad = copy.deepcopy(BASE)
        bad["route"]["ordinary_and_4q_share_one_row"] = False
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_wrong_endpoint_orientation(self):
        bad = copy.deepcopy(BASE)
        bad["route"]["finite_dual_orientation"] = "F_Lambda>=native_deficit"
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_weak_top_anchor(self):
        bad = copy.deepcopy(BASE)
        bad["constants"]["top_anchor_sqrt_multiplier"] = 5
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_non_strict_thinning(self):
        bad = copy.deepcopy(BASE)
        bad["constants"]["thinning_shift"] = 23
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_forbidden_benchmark_bridge(self):
        bad = copy.deepcopy(BASE)
        bad["route"]["forbidden_benchmark_bridge"] = False
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)

    def test_rejects_genealogy_drift(self):
        bad = copy.deepcopy(BASE)
        bad["genealogy"]["pr495_sha"] = "0" * 40
        with self.assertRaises(ValueError):
            VERIFY.validate_control(bad)


if __name__ == "__main__":
    unittest.main()
