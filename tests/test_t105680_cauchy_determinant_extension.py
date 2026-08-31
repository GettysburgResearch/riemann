from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CauchyDeterminantExtensionReplayTest(unittest.TestCase):
    def test_replay(self) -> None:
        root = Path(__file__).resolve().parents[1]
        verifier = root / "experiments/X-105680-cauchy-determinant-extension/verify.py"
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "verification.json"
            completed = subprocess.run(
                [sys.executable, "-B", str(verifier), "--output", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn(
                "PASS_T105680_CAUCHY_DETERMINANT_AND_EXTENSION",
                completed.stdout,
            )
            result = json.loads(output.read_text())
            self.assertEqual(result["checks"], 231)
            self.assertTrue(result["determinant_strength_cti_exact"])
            self.assertTrue(result["rank_extension_identity_exact"])
            self.assertFalse(result["return_compensation_proved"])
            self.assertFalse(result["rh_established"])


if __name__ == "__main__":
    unittest.main()
