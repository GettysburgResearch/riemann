#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFY = ROOT / "verify.py"
PASS = ROOT / "certificates" / "pass.json"
DIRECT = ROOT / "certificates" / "direct-only.json"

class TestMoat(unittest.TestCase):
    def run_cert(self, data):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "c.json"
            p.write_text(json.dumps(data))
            cp = subprocess.run([sys.executable, str(VERIFY), str(p)],
                                text=True, capture_output=True)
            return cp.returncode, json.loads(cp.stdout)

    def load(self, path):
        return json.loads(path.read_text())

    def test_pass(self):
        code, out = self.run_cert(self.load(PASS))
        self.assertEqual(code, 0)
        self.assertEqual(out["status"], "CERTIFIED_GAUSSIAN_FRAME_TAIL_MOAT")

    def test_direct_only(self):
        code, out = self.run_cert(self.load(DIRECT))
        self.assertEqual(code, 0)
        self.assertEqual(out["status"], "CERTIFIED_DIRECT_VISIBLE_FLOOR_ONLY")

    def test_schema(self):
        d = self.load(PASS); d["schema"] = "bad"
        code, out = self.run_cert(d)
        self.assertEqual(code, 2); self.assertEqual(out["status"], "REJECTED")

    def test_boolean_rejected(self):
        d = self.load(PASS); d["frame_floor"]["numerator"] = True
        code, out = self.run_cert(d)
        self.assertEqual(code, 2); self.assertEqual(out["status"], "REJECTED")

    def test_nonpositive_frame(self):
        d = self.load(PASS); d["frame_floor"]["numerator"] = 0
        code, out = self.run_cert(d)
        self.assertEqual(code, 2); self.assertEqual(out["status"], "REJECTED")

    def test_negative_budget(self):
        d = self.load(PASS); d["omitted_zero_budget"]["numerator"] = -1
        code, out = self.run_cert(d)
        self.assertEqual(code, 2); self.assertEqual(out["status"], "REJECTED")

    def test_expected_status_mutation(self):
        d = self.load(PASS); d["expected"]["status"] = "CERTIFIED_DIRECT_VISIBLE_FLOOR_ONLY"
        code, out = self.run_cert(d)
        self.assertEqual(code, 2); self.assertEqual(out["status"], "REJECTED")

    def test_expected_boolean_mutation(self):
        d = self.load(PASS); d["expected"]["gaussian_interval_feasible"] = False
        code, out = self.run_cert(d)
        self.assertEqual(code, 2); self.assertEqual(out["status"], "REJECTED")

    def test_denominator(self):
        d = self.load(PASS); d["radical_endpoint"]["denominator"] = 0
        code, out = self.run_cert(d)
        self.assertEqual(code, 2); self.assertEqual(out["status"], "REJECTED")

if __name__ == "__main__":
    unittest.main()
