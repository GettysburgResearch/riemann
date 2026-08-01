import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify_mod", ROOT / "verify.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
BASE = json.loads((ROOT / "certificates" / "synthetic-quartic-transgression.json").read_text())


class Tests(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(mod.verify(copy.deepcopy(BASE))["status"], "CERTIFIED_TARGET_TRANSGRESSION_IDENTITY")

    def test_bad_quartic_defect(self):
        d = copy.deepcopy(BASE)
        d["target_defects"]["4"] = 0
        with self.assertRaises(ValueError):
            mod.verify(d)

    def test_bad_quartic_ratio_sign(self):
        d = copy.deepcopy(BASE)
        d["log_ratio_coefficients"]["4"] = {"numerator": 5, "denominator": 28}
        with self.assertRaises(ValueError):
            mod.verify(d)

    def test_bad_linear_coefficient(self):
        d = copy.deepcopy(BASE)
        d["linear_coefficients"]["6"] = 154
        with self.assertRaises(ValueError):
            mod.verify(d)

    def test_radius_too_small(self):
        d = copy.deepcopy(BASE)
        d["hilbert_schmidt_radius"] = 3
        with self.assertRaises(ValueError):
            mod.verify(d)

    def test_difference_bound_too_small(self):
        d = copy.deepcopy(BASE)
        d["difference_s2_upper"] = 1
        with self.assertRaises(ValueError):
            mod.verify(d)

    def test_boolean_injection(self):
        d = copy.deepcopy(BASE)
        d["linear_coefficients"]["4"] = True
        with self.assertRaises(ValueError):
            mod.verify(d)

    def test_missing_order_four(self):
        d = copy.deepcopy(BASE)
        d["orders"] = [2, 6, 8]
        for key in ("linear_coefficients", "target_defects", "log_ratio_coefficients"):
            d[key].pop("4")
        with self.assertRaises(ValueError):
            mod.verify(d)


if __name__ == "__main__":
    unittest.main()
