from pathlib import Path
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(root / "verify.py")], cwd=root, check=True)
data = json.loads((root / "results/verification.json").read_text())
assert data["verdict"] == "PASS_ANNULAR_SHARP_CANDIDATE_REGRESSION"
assert data["rh_established"] is False
assert all(float(x["minimum_annular_row"]) >= -1e-40 for x in data["endpoint_checks"])
assert all(float(x["minimum"]) < 0 for x in data["negative_controls"])
