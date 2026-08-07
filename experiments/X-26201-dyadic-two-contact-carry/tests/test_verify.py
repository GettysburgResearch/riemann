from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def run_script(name: str) -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, str(ROOT / name)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def test_exact_dyadic_carry_bridge() -> None:
    result = run_script("verify.py")
    assert (
        result["sha256_without_digest"]
        == "dd6f66f1e026178c1277f2fa634671d8868219e0303db505d9f0547df5eb0715"
    )
    assert result["checks"]["average_rank_one_collapse"]["cases"] == 12879
    assert (
        result["checks"]["pointwise_two_contact"]["pointwise_cases"]
        == 13038
    )
    assert all(
        row["energy"] == 5
        for row in result["checks"]["unprojected_green_two_charge"]["instances"]
    )


def test_exact_bottom_charge_and_flow_invisibility() -> None:
    result = run_script("verify_bottom_charge.py")
    assert (
        result["sha256_without_digest"]
        == "395a7a89ea2267cfa5a3b805ead2646fa46a1761408f6ff048fed7b2e218757f"
    )
    assert (
        result["classification"]
        == "PASS_EXACT_DYADIC_BOTTOM_CHARGE_AND_FLOW_INVISIBILITY"
    )
    assert all(
        row["high_index_flow_delta"] == {"numerator": 0, "denominator": 1}
        for row in result["rows"]
    )
