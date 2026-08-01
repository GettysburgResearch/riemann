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


class ThetaMixedSchurTests(unittest.TestCase):
    def test_control(self):
        out = VERIFY.verify(copy.deepcopy(BASE))
        self.assertEqual(out["verdict"], "PASS")
        self.assertEqual(out["pair_channel"], "8")

    def test_rejects_boolean(self):
        bad = copy.deepcopy(BASE)
        bad["probabilities"][0] = True
        with self.assertRaises(ValueError): VERIFY.verify(bad)

    def test_rejects_probability_sum(self):
        bad = copy.deepcopy(BASE)
        bad["probabilities"] = ["1/2", "2/3"]
        with self.assertRaises(ValueError): VERIFY.verify(bad)

    def test_rejects_no_mode_mixing(self):
        bad = copy.deepcopy(BASE)
        bad["mode_coordinates"] = ["2", "2"]
        bad["expected_mu"] = "4"
        bad["expected_scalar_channel"] = "4"
        bad["expected_pair_channel"] = "0"
        with self.assertRaises(ValueError): VERIFY.verify(bad)

    def test_rejects_false_pair_channel(self):
        bad = copy.deepcopy(BASE)
        bad["expected_pair_channel"] = "7"
        with self.assertRaises(ValueError): VERIFY.verify(bad)

    def test_rejects_false_mu(self):
        bad = copy.deepcopy(BASE)
        bad["expected_mu"] = "49"
        with self.assertRaises(ValueError): VERIFY.verify(bad)

    def test_rejects_bad_operator_dimensions(self):
        bad = copy.deepcopy(BASE)
        bad["mixer"] = [["1/2"]]
        with self.assertRaises(ValueError): VERIFY.verify(bad)

    def test_rejects_false_schur_identity_via_dimension(self):
        bad = copy.deepcopy(BASE)
        bad["trace_schur"] = [["3/5", "0"], ["0", "1"]]
        with self.assertRaises(ValueError): VERIFY.verify(bad)


if __name__ == "__main__":
    unittest.main()
