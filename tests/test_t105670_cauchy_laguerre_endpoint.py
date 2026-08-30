from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class T105670ReplayTest(unittest.TestCase):
    def test_replay(self) -> None:
        root = Path(__file__).resolve().parents[1]
        script = root / "experiments/X-105670-cauchy-laguerre-endpoint/verify.py"
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "verification.json"
            completed = subprocess.run(
                [sys.executable, "-B", str(script), "--output", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("PASS_T105670_CAUCHY_LAGUERRE_ENDPOINT", completed.stdout)
            result = json.loads(output.read_text())
            self.assertEqual(result["checks"], 97)
            self.assertTrue(result["laguerre_limit_exact"])
            self.assertFalse(result["global_cti_proved"])
            self.assertFalse(result["rh_established"])
            self.assertEqual(
                result["proof_object"],
                "28e5db953aaccd25a328f7380b9d8162407c54ada77dc640c895531aff54eaaa",
            )


if __name__ == "__main__":
    unittest.main()
