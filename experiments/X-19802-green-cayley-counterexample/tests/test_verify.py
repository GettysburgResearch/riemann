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
BASE = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class GreenCayleyTests(unittest.TestCase):
    def test_control(self):
        out = VERIFY.verify(copy.deepcopy(BASE))
        self.assertEqual(out["verdict"], "PASS_EXACT_COUNTEREXAMPLE")
        self.assertEqual(out["K_norm"], "9/10")
        self.assertEqual(out["CKE_norm"], "3/2")

    def test_rejects_boolean_rational(self):
        bad = copy.deepcopy(BASE)
        bad["K"][0][0] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_euler_cross_mutation(self):
        bad = copy.deepcopy(BASE)
        bad["G_minus"][0][1] = "9/10"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_nonexpanding_observed_map(self):
        bad = copy.deepcopy(BASE)
        bad["E"] = [["1"], ["0"]]
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_bad_right_inverse(self):
        bad = copy.deepcopy(BASE)
        bad["E"][1][0] = "-1/4"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_noncontractive_lifted_multiplier(self):
        bad = copy.deepcopy(BASE)
        bad["K"][0][0] = "1"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_nondiagonal_lifted_multiplier(self):
        bad = copy.deepcopy(BASE)
        bad["K"][0][1] = "1/10"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_nonpositive_kernel_block(self):
        bad = copy.deepcopy(BASE)
        bad["G_plus"][0][1] = "1/2"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)


if __name__ == "__main__":
    unittest.main()
