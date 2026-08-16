from pathlib import Path
import json
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as directory:
    output = Path(directory) / "verification.json"
    subprocess.run(
        [sys.executable, str(root / "verify.py"), "--limit", "100000", "--output", str(output)],
        cwd=root,
        check=True,
    )
    result = json.loads(output.read_text())

assert result["verdict"] == "PASS_TWO_ROW_ANNULAR_MELLIN_HARDENING_96100"
assert result["rh_established"] is False
assert all(item["minimum"] >= -2e-9 for item in result["row_scans"])
assert result["negative_controls"]["unsmoothed_step_minimum"] < 0
assert result["negative_controls"]["native_gap_at_X3"] < 0
