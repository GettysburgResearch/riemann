#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GEN = ROOT / "generate.py"
RESULT = ROOT / "results" / "verification.json"
CERTS = ROOT / "results" / "certificates"


def canonical_hash(x: object) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def run(out: Path, certs: Path) -> dict:
    subprocess.run(
        [sys.executable, str(GEN), "--output", str(out), "--certificate-dir", str(certs)],
        check=True,
    )
    return json.loads(out.read_text())


def audit(d: dict, certs: Path) -> dict:
    assert d["classification"] == "PASS_LIVE_ENDPOINT_SOURCE_TREE_AND_JOINT_CANCELLATION_GATE"
    assert d["schema"].endswith(".v2")
    assert d["frozen_base"]["head"] == "4ae97dffd1f76ed3244b8f3028560ffa80663caf"
    assert d["actual_terminal_leaf"]["active_p61_atoms"] == 229
    assert d["actual_terminal_leaf"]["p"] == 67 and d["actual_terminal_leaf"]["y"] == 13
    assert d["outer_two_channel_certificate"]["E_global_lower_decimal"] > 0.318
    assert d["outer_two_channel_certificate"]["R_global_lower_decimal"] >= 0
    assert d["finite_endpoint_registry"]["anchored_adapter_exact_witness"]["finite_log_coefficient"] == 0
    assert d["finite_endpoint_registry"]["finite_endpoint_occurrences"] == 2473
    assert d["native_source_registry"]["squarefree_source_atoms"] == 327
    assert d["finite_forcing_causal_allocation"]["terminal_prime_count"] == 132
    assert d["finite_forcing_causal_allocation"]["scope"].startswith("allocates the P61")
    assert d["q2_branchwise_child_obstruction"]["elementary_lower_bound"] == "1/9"
    assert d["rh_established_by_replay"] is False

    expected_files = {
        "native_source_registry_536.json": 327,
        "finite_endpoint_registry_536.json": 2473,
        "terminal_leaf_67_13.json": 229,
        "causal_weights_871.json": 132,
        "outer_two_channel_cells.json": 66,
    }
    for name, expected_len in expected_files.items():
        path = certs / name
        assert path.exists(), name
        assert hashlib.sha256(path.read_bytes()).hexdigest() == d["certificate_file_sha256"][name]
        assert len(json.loads(path.read_text())) == expected_len

    source = json.loads((certs / "native_source_registry_536.json").read_text())
    assert len({a["k"] for a in source}) == len(source)
    for atom in source:
        prod = atom["small_divisor"]
        for p in atom["rough_history"]:
            prod *= p
        assert prod == atom["k"]
        assert atom["first_owner"] == ("root" if not atom["rough_history"] else str(atom["rough_history"][0]))

    endpoint = json.loads((certs / "finite_endpoint_registry_536.json").read_text())
    witness = [o for o in endpoint if o["endpoint_cell"] == 8 and o["k"] == 67]
    assert len(witness) == 1 and witness[0]["zero_boundary"] is True

    leaf = json.loads((certs / "terminal_leaf_67_13.json").read_text())
    assert sum(r["child_active"] for r in leaf) == 9
    assert all(r["owner"] == 67 for r in leaf)

    weights = json.loads((certs / "causal_weights_871.json").read_text())
    assert weights[0]["p"] == 67
    assert all(int(r["p"]) >= 67 for r in weights)

    mutations = {
        "drop_orientation": not d["q2_branchwise_child_obstruction"]["actual_oriented_child_ordinary"].startswith(">="),
        "declare_child_nonnegative": "impossible" in d["q2_branchwise_child_obstruction"]["conclusion"],
        "identify_log_with_paired_atom": d["finite_endpoint_registry"]["anchored_adapter_exact_witness"]["paired_E_coefficient"] != "0",
        "duplicate_owner": d["native_source_registry"]["finite_forcing_atoms"] + d["native_source_registry"]["actual_rough_child_atoms"] == d["native_source_registry"]["squarefree_source_atoms"],
        "omit_p61_leaf": d["actual_terminal_leaf"]["active_p61_atoms"] != 0,
        "lose_parent_allocation": abs(float(d["finite_forcing_causal_allocation"]["beta_sum"]) - 1) < 1e-60,
        "child_mass_not_subcritical": float(d["finite_forcing_causal_allocation"]["gamma_sum"]) < 0.125,
        "promote_to_rh": d["joint_gate_status"].startswith("OPEN") and not d["rh_established_by_replay"],
        "erase_common_q4_contract": all("ordinary 4q occurrence" in o["coordinate_contract"] for o in endpoint),
    }
    assert all(mutations.values()), mutations
    return mutations


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=RESULT)
    args = ap.parse_args()
    with tempfile.TemporaryDirectory(prefix="x94020-") as td:
        tmp = Path(td)
        fresh = run(tmp / "fresh.json", tmp / "certificates")
        mutations = audit(fresh, tmp / "certificates")
    # Regenerate retained proof objects only after the fresh audit passes.
    retained = run(args.output, CERTS)
    audit(retained, CERTS)
    payload = dict(retained)
    payload["mutation_checks"] = mutations
    payload["generator_sha256"] = hashlib.sha256(GEN.read_bytes()).hexdigest()
    payload["verification_scope"] = (
        "full deterministic source/owner and endpoint occurrence files, outer two-channel cell certificate, "
        "real P61 terminal leaf, complete causal parent weights, common q/4q coordinate contract, and q=2 "
        "obstruction; the joint native coupling remains open"
    )
    payload["verification_sha256"] = canonical_hash(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(payload["verification_sha256"])


if __name__ == "__main__":
    main()
