#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFY = ROOT / "verify.py"
CERT = ROOT / "certificates" / "synthetic.json"


class TestVerifier(unittest.TestCase):
    def run_cert(self, obj):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(obj, f)
            name = f.name
        process = subprocess.run(
            ["python3", str(VERIFY), name], text=True, capture_output=True
        )
        Path(name).unlink(missing_ok=True)
        return process

    def base(self):
        return json.loads(CERT.read_text())

    def test_retained_passes(self):
        process = subprocess.run(
            ["python3", str(VERIFY), str(CERT)], text=True, capture_output=True
        )
        self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
        self.assertIn("PASS_AFFINE_HYBRID_EXACT", process.stdout)

    def test_break_complement_floor(self):
        obj = self.base()
        obj["residual_vectors"][1] = ["1/20", "1/10", "0", "0", "0"]
        self.assertNotEqual(self.run_cert(obj).returncode, 0)

    def test_break_affine_lmi(self):
        obj = self.base()
        obj["extra_psd_diag"][1] = "-1/10"
        self.assertNotEqual(self.run_cert(obj).returncode, 0)

    def test_break_target_upper(self):
        obj = self.base()
        obj["target_upper_coefficient"] = "2"
        self.assertNotEqual(self.run_cert(obj).returncode, 0)

    def test_break_separation(self):
        obj = self.base()
        obj["gap_floor"] = "1/1000"
        self.assertNotEqual(self.run_cert(obj).returncode, 0)


if __name__ == "__main__":
    unittest.main()
