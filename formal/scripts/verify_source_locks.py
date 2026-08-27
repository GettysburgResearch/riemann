#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"
LOCK = FORMAL / "registry" / "SOURCE_LOCKS.json"
SHA = re.compile(r"^[0-9a-f]{40}$")


def main() -> None:
    data = json.loads(LOCK.read_text(encoding="utf-8"))
    checks = [
        data["riemann"]["scientific_commit"],
        data["riemann"]["scientific_tree"],
        data["riemann"]["canonical_claims_blob"],
        data["mathlib"]["commit"],
        data["zeta23"]["previously_audited_commit"],
        data["zeta23"]["selected_commit"],
        data["formal_conjectures"]["reference_commit"],
    ]
    bad = [x for x in checks if not SHA.fullmatch(x)]
    if bad:
        raise SystemExit(f"malformed locked SHA(s): {bad}")

    if data["riemann"]["canonical_claim_count"] != 139:
        raise SystemExit("canonical claim count lock must be 139")
    if data["riemann"]["research_terminal_pr"] != 707:
        raise SystemExit("research cutoff must remain PR #707 for formal-v0.1")
    if data["formal_conjectures"]["proof_dependency"] is not False:
        raise SystemExit("Formal Conjectures must not be a proof dependency")
    if data["zeta23"]["theorem_bearing_Zeta23_directory_changed"] is not False:
        raise SystemExit("the selected Zeta23 update requires a new theorem-bearing audit")

    toolchain = (FORMAL / "lean-toolchain").read_text(encoding="utf-8").strip()
    if toolchain != data["lean"]["toolchain"]:
        raise SystemExit("lean-toolchain drift from SOURCE_LOCKS.json")

    lakefile = (FORMAL / "lakefile.toml").read_text(encoding="utf-8")
    for rev in (data["mathlib"]["commit"], data["zeta23"]["selected_commit"]):
        if rev not in lakefile:
            raise SystemExit(f"lakefile.toml does not contain locked revision {rev}")

    manifest = json.loads((FORMAL / "lake-manifest.json").read_text(encoding="utf-8"))
    packages = {p["name"]: p for p in manifest["packages"]}
    expected = {
        "mathlib": data["mathlib"]["commit"],
        "Zeta23": data["zeta23"]["selected_commit"],
    }
    for name, rev in expected.items():
        package = packages.get(name)
        if package is None:
            raise SystemExit(f"lake-manifest.json lacks {name}")
        if package.get("rev") != rev or package.get("inherited") is not False:
            raise SystemExit(f"lake-manifest.json drift for {name}")

    claims = ROOT / data["riemann"]["canonical_claims_path"]
    with claims.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if len(rows) != data["riemann"]["canonical_claim_count"]:
        raise SystemExit("canonical claims file no longer matches the frozen claim-count lock")

    print(
        "PASS_FORMAL_SOURCE_LOCKS "
        f"claims={len(rows)} mathlib={expected['mathlib'][:8]} zeta23={expected['Zeta23'][:8]}"
    )


if __name__ == "__main__":
    main()
