import copy
import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def base():
    return json.loads((ROOT / "certificates" / "scaled-exact-pass.json").read_text())


class ScaleOptimizedTests(unittest.TestCase):
    def test_exact_scaled_pass(self):
        out = VERIFY.verify(base())
        self.assertEqual(out["status"], "CERTIFIED_SCALE_OPTIMIZED_ARITHMETIC_COMPLETION")
        self.assertEqual(out["scaled_difference_row_bound"], 0)
        self.assertEqual(out["canonical_source"], [3, 0, -3])

    def test_unscaled_comparison_really_fails(self):
        out = VERIFY.verify(base())
        value = VERIFY.rat(out["unscaled_difference_row_bound"])
        moat = VERIFY.rat(out["canonical_moat_lower"])
        self.assertGreater(value, moat)

    def test_wrong_scale_rejected(self):
        data = base()
        data["canonical_scale"] = 1
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_bad_boundary_scalar_rejected(self):
        data = base()
        data["boundary_scalar"] = -10
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_false_moat_rejected(self):
        data = base()
        data["canonical_moat_lower"] = 10
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_boolean_rejected(self):
        data = base()
        data["canonical_scale"] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_zero_target_coordinate_rejected(self):
        data = base()
        data["p"] = [0, 1, 0]
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_bad_normalization_rejected(self):
        data = base()
        data["p"][0] = {"numerator": 1, "denominator": 2}
        with self.assertRaises(ValueError):
            VERIFY.verify(data)


if __name__ == "__main__":
    unittest.main()
