import json
import subprocess
import sys
from pathlib import Path


def test_exact_verifier() -> None:
    root = Path(__file__).resolve().parents[1]
    subprocess.run([sys.executable, str(root / "verify.py")], check=True)
    data = json.loads((root / "results" / "verification.json").read_text())
    assert data["verdict"] == "PASS_EXACT_BROWNIAN_GAMMA_NORLUND_ALGEBRA"
    assert all(data["mutations"].values())
