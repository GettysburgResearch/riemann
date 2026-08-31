from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class BetaAdditiveChowlaReplayTest(unittest.TestCase):
    def test_replay(self) -> None:
        root = Path(__file__).resolve().parents[1]
        verifier = root / "experiments/X-107120-beta-additive-chowla/verify.py"
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "verification.json"
            completed = subprocess.run(
                [sys.executable, "-B", str(verifier), "--output", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn(
                "PASS_T107120_BETA_ADDITIVE_CHOWLA_NORMAL_FORM",
                completed.stdout,
            )
            result = json.loads(output.read_text())
            self.assertEqual(result["checks"], 352)
            self.assertFalse(result["low_frequency_estimate_proved"])
            self.assertFalse(result["rh_established"])


if __name__ == "__main__":
    unittest.main()
