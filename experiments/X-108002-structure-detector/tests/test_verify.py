import json
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestX108002(unittest.TestCase):
    def test_verify_passes(self):
        r = subprocess.run([sys.executable, os.path.join(HERE, "verify.py")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("PASS_108002_STRUCTURE_DETECTOR", r.stdout)

    def test_mobius_weight_contrast(self):
        with open(os.path.join(HERE, "results", "verification.json")) as f:
            data = json.load(f)
        self.assertIs(data["rh_established"], False)
        self.assertTrue(data["all_ok"])
        # the two ontologies separated by the weight of the virtual part
        self.assertEqual(data["extra"]["ff_mobius_q2_numerator"], "[1, -2]")
        self.assertEqual(data["extra"]["ff_mobius_q3_numerator"], "[1, -3]")
        names = {c["name"] for c in data["checks"]}
        self.assertIn("B2_mobius_virtual_refusal", names)
        self.assertIn("B10_pm_roots_pure_full_pass", names)
        self.assertIn("B11_traces_mode_reconstructs", names)
        self.assertEqual(len(data["checks"]), 14)


if __name__ == "__main__":
    unittest.main()
