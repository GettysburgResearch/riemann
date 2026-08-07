import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify_mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(verify_mod)

BASE = json.loads((ROOT / "certificates" / "graded-order4-obstruction.json").read_text())


class ContactWardTests(unittest.TestCase):
    def test_exact_obstruction(self):
        result = verify_mod.verify(copy.deepcopy(BASE))
        self.assertEqual(result["status"], "CERTIFIED_QUARTIC_CONTACT_ANOMALY")
        self.assertEqual(
            result["required_nonlinear_counterterm_order4"],
            {"numerator": -8064, "denominator": 625},
        )

    def test_exact_ward_repair(self):
        data = copy.deepcopy(BASE)
        data["linear_counterterm_order4"] = {"numerator": -8064, "denominator": 625}
        result = verify_mod.verify(data)
        self.assertEqual(result["status"], "CERTIFIED_CONTACT_FREE_QUARTIC_WARD")
        self.assertEqual(result["scalar_minus_cyclic_order4"], 0)

    def test_wrong_schema(self):
        data = copy.deepcopy(BASE)
        data["schema"] = "bad"
        with self.assertRaises(ValueError):
            verify_mod.verify(data)

    def test_boolean_counterterm_rejected(self):
        data = copy.deepcopy(BASE)
        data["linear_counterterm_order4"] = True
        with self.assertRaises(ValueError):
            verify_mod.verify(data)

    def test_broken_grading_rejected(self):
        data = copy.deepcopy(BASE)
        data["renormalized_spectrum"][1] = {"numerator": -10, "denominator": 5}
        with self.assertRaises(ValueError):
            verify_mod.verify(data)

    def test_overlapping_grading_pairs_rejected(self):
        data = copy.deepcopy(BASE)
        data["grading_pairs"] = [[0, 1], [1, 2]]
        with self.assertRaises(ValueError):
            verify_mod.verify(data)

    def test_quadratic_mismatch_rejected(self):
        data = copy.deepcopy(BASE)
        data["renormalized_spectrum"][2] = {"numerator": 3, "denominator": 5}
        data["renormalized_spectrum"][3] = {"numerator": -3, "denominator": 5}
        with self.assertRaises(ValueError):
            verify_mod.verify(data)

    def test_odd_trace_mismatch_rejected(self):
        data = copy.deepcopy(BASE)
        data["grading_pairs"] = [[0, 2], [1, 3]]
        with self.assertRaises(ValueError):
            verify_mod.verify(data)

    def test_bad_rational_rejected(self):
        data = copy.deepcopy(BASE)
        data["renormalized_spectrum"][0] = {"numerator": 11, "denominator": 0}
        with self.assertRaises(ValueError):
            verify_mod.verify(data)


if __name__ == "__main__":
    unittest.main()
