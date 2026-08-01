#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFY = ROOT / "verify.py"
CERT = ROOT / "certificates" / "synthetic.json"


def run_case(data: dict) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "certificates").mkdir()
        (root / "results").mkdir()
        (root / "verify.py").write_text(VERIFY.read_text())
        (root / "certificates" / "synthetic.json").write_text(
            json.dumps(data, sort_keys=True, separators=(",", ":")) + "\n"
        )
        return subprocess.run(
            [sys.executable, str(root / "verify.py")],
            text=True,
            capture_output=True,
            check=False,
        )


def main() -> None:
    original = json.loads(CERT.read_text())
    passed = run_case(original)
    assert passed.returncode == 0
    assert "PASS_EXACT_L15630_CONDITIONING_SPLIT" in passed.stdout

    mutations = []

    x = copy.deepcopy(original)
    x["K_diag"][0]["numerator"] = "10"
    mutations.append(("unwhitened envelope", x))

    x = copy.deepcopy(original)
    for i in (1, 2, 3):
        x["D_diag"][i] = {"numerator": "1", "denominator": "100"}
    mutations.append(("empty dangerous complement", x))

    x = copy.deepcopy(original)
    x["D_diag"][1] = {"numerator": "1", "denominator": "1"}
    mutations.append(("empty soft sector", x))

    x = copy.deepcopy(original)
    x["source_synthesis_matrix"][0][0] = {
        "numerator": "0",
        "denominator": "1",
    }
    mutations.append(("right inverse", x))

    x = copy.deepcopy(original)
    x["D_diag"][2] = {"numerator": "-1", "denominator": "1"}
    mutations.append(("negative Gram", x))

    for name, data in mutations:
        result = run_case(data)
        assert result.returncode != 0, name

    print("6/6 central and adversarial tests pass")


if __name__ == "__main__":
    main()
