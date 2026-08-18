from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_replay() -> None:
    out = subprocess.check_output([sys.executable, str(ROOT / "verify.py")], text=True)
    data = json.loads(out)
    assert data["verdict"] == "PASS_X98610_ZMCSCBI_INTERFACE_CORRECTION"
    assert data["tao_update"]["reserve"] != "0"
    assert data["two_level_countermodel"] == {
        "completed_root": "1",
        "local_current": "-1",
        "future_repair": "2",
    }
    assert data["rh_established"] is False
