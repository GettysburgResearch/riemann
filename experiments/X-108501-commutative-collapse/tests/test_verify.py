import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestX108501(unittest.TestCase):
    def test_verify_passes(self):
        r = subprocess.run([sys.executable, os.path.join(HERE, "verify.py")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("PASS_108501_COMMUTATIVE_COLLAPSE", r.stdout)

    def test_results_json_shape(self):
        import json
        with open(os.path.join(HERE, "results", "verification.json")) as f:
            data = json.load(f)
        self.assertIs(data["rh_established"], False)
        self.assertTrue(data["all_ok"])
        names = [c["name"] for c in data["checks"]]
        self.assertIn("C2_sum_exchange_identity", names)
        # the floating check must be labelled as reconnaissance
        c4 = [c for c in data["checks"] if c["name"].startswith("C4")][0]
        self.assertIn("FLOATING_RECONNAISSANCE", c4["detail"])


if __name__ == "__main__":
    unittest.main()
