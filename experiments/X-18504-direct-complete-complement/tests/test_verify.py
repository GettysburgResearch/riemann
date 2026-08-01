import copy
import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify import verify  # noqa: E402


class TestDirectShorting(unittest.TestCase):
    def setUp(self):
        self.cert = json.loads((ROOT / "certificates/synthetic.json").read_text())

    def test_central(self):
        out = verify(self.cert)
        self.assertEqual(out["certified_direct_floor"], "9/10")
        self.assertEqual(out["exact_schur_floor"], "9/10")
        self.assertEqual(out["separated_floor"], "0")
        self.assertEqual(out["joint_improvement"], "9/10")

    def test_bad_low_decomposition(self):
        c = copy.deepcopy(self.cert); c["low_block"] = "2"
        with self.assertRaises(ValueError): verify(c)

    def test_bad_coercivity(self):
        c = copy.deepcopy(self.cert); c["coercivity_h"] = "2"
        with self.assertRaises(ValueError): verify(c)

    def test_bad_verdict(self):
        c = copy.deepcopy(self.cert); c["declared_verdict"] = "UNRESOLVED_OR_NEGATIVE_COMPLETE_COMPLEMENT"
        with self.assertRaises(ValueError): verify(c)

    def test_boolean_rejected(self):
        c = copy.deepcopy(self.cert); c["ambient_cross"] = True
        with self.assertRaises(TypeError): verify(c)

    def test_negative_metric_rejected(self):
        c = copy.deepcopy(self.cert); c["packet_metric"] = "-1"
        with self.assertRaises(ValueError): verify(c)

    def test_exact_solve(self):
        c = copy.deepcopy(self.cert); c["trial_harmonic_solve"] = "1"
        out = verify(c)
        self.assertEqual(out["residual"], "0")
        self.assertEqual(out["certified_direct_floor"], "9/10")

    def test_zero_trial_still_lower(self):
        c = copy.deepcopy(self.cert); c["trial_harmonic_solve"] = "0"
        out = verify(c)
        self.assertEqual(out["certified_direct_floor"], "9/10")


if __name__ == "__main__":
    unittest.main()
