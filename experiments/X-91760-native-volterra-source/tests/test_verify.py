from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VERIFY)
BASE = json.loads((ROOT / "certificates" / "control.json").read_text())


class NativeVolterraTests(unittest.TestCase):
    def test_control_passes(self):
        result = VERIFY.verify(copy.deepcopy(BASE))
        self.assertEqual(result["verdict"], "PASS_NATIVE_VOLTERRA_RANK_ONE_COMMON_PARENT_SOURCE")

    def test_rejects_boolean_rational(self):
        bad = copy.deepcopy(BASE)
        bad["positive_weights"][0] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_nonpositive_density(self):
        bad = copy.deepcopy(BASE)
        bad["negative_weights"] = ["30"]
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_finite_mismatch_failure(self):
        bad = copy.deepcopy(BASE)
        bad["finite_seed"][0] = "8/3"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_source_duplication(self):
        bad = copy.deepcopy(BASE)
        bad["retained_mass"] = "15"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_root_reaching_67(self):
        bad = copy.deepcopy(BASE)
        bad["root_labels"].append(67)
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_rough_below_67(self):
        bad = copy.deepcopy(BASE)
        bad["rough_labels"][0] = 61
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_bad_volterra_order(self):
        bad = copy.deepcopy(BASE)
        bad["volterra_cases"][0]["sqrt_n"] = "7"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_rough_scale_beyond_parent(self):
        bad = copy.deepcopy(BASE)
        bad["rough_square_scales"].append({"sqrt_m": "7"})
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)


    def test_rejects_non_subcritical_child_mass(self):
        bad = copy.deepcopy(BASE)
        bad["causal_child_coefficients"] = ["1/8"]
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_signed_correction_overrun(self):
        bad = copy.deepcopy(BASE)
        bad["signed_correction"] = ["6", "-2", "3"]
        bad["expected_residual"] = ["-1", "9", "6"]
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

if __name__ == "__main__":
    unittest.main()
