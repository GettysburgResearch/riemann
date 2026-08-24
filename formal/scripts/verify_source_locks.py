#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"
LOCK = FORMAL / "registry" / "SOURCE_LOCKS.json"
CANONICAL = ROOT / "canonical" / "2026-08-22" / "claims.tsv"
LEAN_LOCKS = FORMAL / "RiemannFormal" / "Upstream" / "SourceLocks.lean"
SHA = re.compile(r"^[0-9a-f]{40}$")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def require_sha(value: str, label: str) -> None:
    if not SHA.fullmatch(value):
        raise SystemExit(f"malformed locked SHA for {label}: {value!r}")


def declaration_is_resident(name: str) -> bool:
    short = name.rsplit(".", 1)[-1]
    needles = (f"theorem {short}", f"def {short}", f"structure {short}", f"abbrev {short}")
    for root in (FORMAL / "RiemannFormal" / "Analysis", FORMAL / "RiemannFormal" / "Upstream"):
        for path in root.rglob("*.lean"):
            text = path.read_text(encoding="utf-8")
            if any(needle in text for needle in needles):
                return True
    return False


def main() -> None:
    data = json.loads(LOCK.read_text(encoding="utf-8"))
    if data.get("schema_version") != 2:
        raise SystemExit("SOURCE_LOCKS.json schema_version must be 2")

    base_shas = {
        "riemann.scientific_commit": data["riemann"]["scientific_commit"],
        "riemann.scientific_tree": data["riemann"]["scientific_tree"],
        "riemann.canonical_claims_blob": data["riemann"]["canonical_claims_blob"],
        "mathlib.commit": data["mathlib"]["commit"],
        "zeta23.previously_audited_commit": data["zeta23"]["previously_audited_commit"],
        "zeta23.selected_commit": data["zeta23"]["selected_commit"],
        "formal_conjectures.reference_commit": data["formal_conjectures"]["reference_commit"],
    }
    for label, value in base_shas.items():
        require_sha(value, label)

    if data["riemann"]["canonical_claim_count"] != 139:
        raise SystemExit("canonical claim count lock must be 139")
    if data["riemann"]["research_terminal_pr"] != 707:
        raise SystemExit("research cutoff must remain PR #707 for formal-v0.1")
    if data["formal_conjectures"]["proof_dependency"] is not False:
        raise SystemExit("Formal Conjectures must not be a proof dependency")
    if data["zeta23"]["theorem_bearing_Zeta23_directory_changed"] is not False:
        raise SystemExit("selected Zeta23 update requires a theorem-bearing re-audit")

    toolchain = (FORMAL / "lean-toolchain").read_text(encoding="utf-8").strip()
    if toolchain != data["lean"]["toolchain"]:
        raise SystemExit("lean-toolchain drift from SOURCE_LOCKS.json")

    lakefile = (FORMAL / "lakefile.toml").read_text(encoding="utf-8")
    manifest = json.loads((FORMAL / "lake-manifest.json").read_text(encoding="utf-8"))
    packages = {p["name"]: p for p in manifest["packages"]}
    expected_packages = {
        "mathlib": data["mathlib"]["commit"],
        "Zeta23": data["zeta23"]["selected_commit"],
    }
    for name, rev in expected_packages.items():
        if rev not in lakefile:
            raise SystemExit(f"lakefile.toml does not contain locked revision {rev}")
        package = packages.get(name)
        if package is None or package.get("rev") != rev or package.get("inherited") is not False:
            raise SystemExit(f"lake-manifest.json drift for {name}")

    canonical_rows = read_tsv(CANONICAL)
    if len(canonical_rows) != data["riemann"]["canonical_claim_count"]:
        raise SystemExit("canonical claims file no longer matches the frozen claim-count lock")
    canonical = {row["semantic_id"]: row for row in canonical_rows}

    scientific = data.get("analysis_scientific_claims", [])
    if not scientific:
        raise SystemExit("analysis_scientific_claims must be nonempty")
    for index, lock in enumerate(scientific):
        label = f"analysis_scientific_claims[{index}]"
        sid = lock["semantic_id"]
        require_sha(lock["source_sha"], f"{label}.source_sha")
        row = canonical.get(sid)
        if row is None:
            raise SystemExit(f"unknown canonical semantic ID in {label}: {sid}")
        if str(lock["source_pr"]) != row["source_pr"]:
            raise SystemExit(f"source PR drift for {sid}")
        if lock["source_sha"] != row["source_head_sha"]:
            raise SystemExit(f"source SHA drift for {sid}")
        canonical_paths = {p.strip() for p in row["source_path"].split("|") if p.strip()}
        if lock["source_path"] not in canonical_paths:
            raise SystemExit(f"source path {lock['source_path']!r} is not canonical for {sid}")
        claim_ids = {x.strip() for x in row["source_claim_id"].split("/") if x.strip()}
        if lock["source_claim_id"] not in claim_ids:
            raise SystemExit(f"source claim ID drift for {sid}: {lock['source_claim_id']}")
        declarations = lock.get("lean_declarations", [])
        if not declarations:
            raise SystemExit(f"{label} has no Lean declarations")
        missing = [name for name in declarations if not declaration_is_resident(name)]
        if missing:
            raise SystemExit(f"nonresident Lean declarations for {sid}: {missing}")

    upstream = data.get("analysis_upstream_declarations", [])
    if not upstream:
        raise SystemExit("analysis_upstream_declarations must be nonempty")
    for index, lock in enumerate(upstream):
        label = f"analysis_upstream_declarations[{index}]"
        require_sha(lock["commit"], f"{label}.commit")
        project = lock["project"]
        expected = data["mathlib"]["commit"] if project == "mathlib" else data["zeta23"]["selected_commit"]
        if lock["commit"] != expected:
            raise SystemExit(f"dependency commit drift for {label}")
        if not lock["source_path"] or not lock.get("declarations"):
            raise SystemExit(f"incomplete upstream declaration lock: {label}")

    lean_text = LEAN_LOCKS.read_text(encoding="utf-8")
    for lock in scientific:
        for literal in (lock["semantic_id"], lock["source_sha"], lock["source_path"], lock["source_claim_id"]):
            if literal not in lean_text:
                raise SystemExit(f"SourceLocks.lean does not mirror {literal!r}")
    for lock in upstream:
        for literal in (lock["commit"], lock["source_path"]):
            if literal not in lean_text:
                raise SystemExit(f"SourceLocks.lean does not mirror upstream lock {literal!r}")

    print(
        "PASS_FORMAL_SOURCE_LOCKS "
        f"claims={len(canonical_rows)} scientific={len(scientific)} upstream={len(upstream)} "
        f"mathlib={expected_packages['mathlib'][:8]} zeta23={expected_packages['Zeta23'][:8]}"
    )


if __name__ == "__main__":
    main()
