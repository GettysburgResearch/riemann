import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestX108500(unittest.TestCase):
    def test_verify_passes_and_is_exact(self):
        r = subprocess.run([sys.executable, os.path.join(HERE, "verify.py")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("PASS_108500_TRANSFORM_DEFECTS", r.stdout)

    def test_results_json_shape(self):
        import json
        with open(os.path.join(HERE, "results", "verification.json")) as f:
            data = json.load(f)
        self.assertIs(data["rh_established"], False)
        self.assertTrue(data["all_ok"])
        self.assertEqual(len(data["checks"]), 7)
        self.assertEqual(data["arithmetic_class"], "EXACT_RATIONAL")

    def test_no_float_literals_in_verify(self):
        with open(os.path.join(HERE, "verify.py")) as f:
            src = f.read()
        self.assertNotIn("float(", src)
        self.assertNotIn("math.", src)


if __name__ == "__main__":
    unittest.main()
