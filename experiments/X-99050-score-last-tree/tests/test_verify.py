from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
assert SPEC and SPEC.loader
verify = importlib.util.module_from_spec(SPEC)
sys.modules["verify"] = verify
SPEC.loader.exec_module(verify)


class ScoreLastTests(unittest.TestCase):
    def test_coefficients(self):
        self.assertTrue(verify.verify_coefficients()["sqrt67_discount_below_one_eighth"])

    def test_tree_isometry(self):
        result = verify.verify_tree()
        self.assertEqual(result["classification"], "PASS_FINITE_CAUSAL_TREE_LITERAL_SCORE_ISOMETRY")

    def test_double_bonus_rejected(self):
        self.assertTrue(verify.verify_tree()["double_hall_bonus_mutation_rejected"])

    def test_finite_depth(self):
        self.assertEqual(verify.verify_depth()["classification"], "PASS_ACTUAL_CHILD_SCALE_HAS_FINITE_DEPTH")

    def test_root_cost(self):
        self.assertEqual(verify.verify_root_cost()["total_score_loss_upper"], 852)

    def test_status(self):
        payload = verify.main_payload()
        self.assertFalse(payload["rh_established"])
        self.assertFalse(payload["heavy_inherited_campaigns_replayed"])
        self.assertFalse(payload["declared_score_used_in_final_tree"])


if __name__ == "__main__":
    unittest.main()
