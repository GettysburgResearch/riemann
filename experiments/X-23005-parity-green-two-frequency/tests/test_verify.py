import copy
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFY = ROOT / "verify.py"
CERT = ROOT / "certificates" / "synthetic.json"


def run(payload):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "c.json"
        p.write_text(json.dumps(payload))
        return subprocess.run(["python3", str(VERIFY), str(p)], text=True, capture_output=True)


class VerifyTests(unittest.TestCase):
    def setUp(self):
        self.base = json.loads(CERT.read_text())

    def test_central(self):
        r = run(self.base)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("EXACT_PARITY_GREEN", r.stdout)

    def test_bad_schema(self):
        p = copy.deepcopy(self.base); p["schema"] = "bad"
        self.assertNotEqual(run(p).returncode, 0)

    def test_small_limit(self):
        p = copy.deepcopy(self.base); p["mobius_limit"] = 32
        self.assertNotEqual(run(p).returncode, 0)

    def test_bad_base(self):
        p = copy.deepcopy(self.base); p["digit_bases"] = [1]
        self.assertNotEqual(run(p).returncode, 0)

    def test_bad_dyadic_order(self):
        p = copy.deepcopy(self.base); p["dyadic_orders"] = [0]
        self.assertNotEqual(run(p).returncode, 0)

    def test_bad_poincare_order(self):
        p = copy.deepcopy(self.base); p["poincare_orders"] = [0]
        self.assertNotEqual(run(p).returncode, 0)

    def test_missing_boundary(self):
        p = copy.deepcopy(self.base); del p["proof_boundary"]
        self.assertNotEqual(run(p).returncode, 0)

    def test_digital_limit_overflow(self):
        p = copy.deepcopy(self.base); p["digital_recurrence_limit"] = 1000
        self.assertNotEqual(run(p).returncode, 0)


if __name__ == "__main__":
    unittest.main()
