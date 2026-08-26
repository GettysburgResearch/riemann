from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_cyclic_sheaf_invariant_audit.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
NOTE = SCRIPT.with_name("FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md")


def load_module():
    spec = importlib.util.spec_from_file_location("cyclic_sheaf_audit", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_canonical_fixture_replays() -> None:
    subprocess.run([sys.executable, str(SCRIPT), "--check"], check=True, cwd=ROOT)


def test_payload_hash_and_resource_caps() -> None:
    module = load_module()
    envelope = json.loads(FIXTURE.read_text(encoding="utf-8"))
    payload = envelope["payload"]
    assert (
        envelope["payload_sha256"]
        == module.hashlib.sha256(module.canonical_bytes(payload)).hexdigest()
    )
    ledger = payload["resource_ledger"]
    assert ledger["exact_operations"] <= ledger["max_exact_operations"]
    assert FIXTURE.stat().st_size <= ledger["max_output_bytes"]


def test_all_ternary_two_point_masks_are_rigid() -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))["payload"]
    rows = payload["ternary_mask_fourier"]["rows"]
    assert len(rows) == 3
    assert all(row["mode_squared_norms"] == {"1": "1/4", "2": "1/4"} for row in rows)


def test_same_characteristic_control() -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))["payload"]
    panel = payload["same_characteristic_control"]
    assert panel["base_field"] == "F_7"
    assert panel["hard_leverage"] == "1/2"
    assert panel["complete_leverage"] == "9/16"
    assert panel["soft_complete_metric_leverage"] == "513/784"
    assert panel["wick_atomic_residual"] == "63/4"


def test_declared_invariant_multiplicities() -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))["payload"]
    rows = payload["invariant_test"]["connected_monomial_subtorus_rows"]
    by_alignment: dict[str, dict[str, int]] = {}
    for row in rows:
        assert len(set(row["mode_geometrically_trivial"].values())) == 1
        by_alignment.setdefault(row["alignment"], {})[row["stratum"]] = row[
            "selected_rank_two_invariant_multiplicity"
        ]
    expected = {
        "generic_pair_torus": 0,
        "x_collision_only": 0,
        "y_collision_only": 0,
        "aligned_compensating_resonance": 2,
        "opposite_compensating_resonance": 0,
        "double_physical_collision": 2,
        "atomic_diagonal_physical_image": 2,
    }
    assert by_alignment == {"product": expected, "quotient": expected}


def test_scope_firewalls_and_note_front_door() -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))["payload"]
    assert all(value is False for value in payload["scope"]["enumeration"].values())
    assert "CYSEL" in payload["scope"]["not_constructed"]
    note = NOTE.read_text(encoding="utf-8")
    normalized_note = " ".join(note.split())
    assert "varying-closed-place source complex and `CYSEL` remain open" in note
    assert "one function-field sheaf over a common finite base" in normalized_note
    assert "Rotating the hard mask therefore cannot null" in normalized_note
    assert "No external novelty or priority claim is made." in note
