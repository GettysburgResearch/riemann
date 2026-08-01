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
    def test_exact_control(self):
        out = VERIFY.verify(copy.deepcopy(BASE))
        self.assertEqual(out["CKE"], "5")
        self.assertEqual(out["green_euler_residual"], "0")

    def test_rejects_boolean(self):
        bad = copy.deepcopy(BASE)
        bad["C"][0] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_noncontractive_k(self):
        bad = copy.deepcopy(BASE)
        bad["K_diagonal"][1] = "6/5"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_wrong_q(self):
        bad = copy.deepcopy(BASE)
        bad["expected_Q"][0][0] = "23/25"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_nonstationary_green_vector(self):
        bad = copy.deepcopy(BASE)
        bad["green_trace_one"][0] = "-3/4"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_wrong_cayley_coordinates(self):
        bad = copy.deepcopy(BASE)
        bad["raw_coordinates"][0] = "1/2"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_nonrefuting_target(self):
        bad = copy.deepcopy(BASE)
        bad["expected_CKE"] = "1"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)


if __name__ == "__main__":
    unittest.main()
