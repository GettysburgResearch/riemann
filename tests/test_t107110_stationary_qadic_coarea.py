from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class T107110ReplayTest(unittest.TestCase):
    def test_replay(self) -> None:
        root = Path(__file__).resolve().parents[1]
        script = root / "experiments/X-107110-stationary-qadic-coarea/verify.py"
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "verification.json"
            completed = subprocess.run(
                [sys.executable, "-B", str(script), "--output", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("PASS_T107110_STATIONARY_QADIC_COAREA", completed.stdout)
            result = json.loads(output.read_text())
            self.assertEqual(result["checks"], 4026)
            self.assertFalse(result["high_primitive_estimate_proved"])
            self.assertFalse(result["rh_established"])
            self.assertEqual(
                result["proof_object"],
                "f5e71155375fc5bbb78993e1e5f3b4995c666accd9935c3401df0bc4d55324d9",
            )


if __name__ == "__main__":
    unittest.main()
