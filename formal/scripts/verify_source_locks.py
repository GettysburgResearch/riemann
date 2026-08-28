#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"
LOCK = FORMAL / "registry" / "SOURCE_LOCKS.json"
CANONICAL = ROOT / "canonical" / "2026-08-22" / "claims.tsv"
UPSTREAM_LEDGER = FORMAL / "registry" / "deltas" / "A_UPSTREAM_REUSE.tsv"
SOURCE_LOCKS_LEAN = FORMAL / "RiemannFormal" / "Upstream" / "SourceLocks.lean"
SHA = re.compile(r"^[0-9a-f]{40}$")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def split_paths(value: str) -> set[str]:
    return {part.strip() for part in value.split("|") if part.strip()}


def split_claim_ids(value: str) -> set[str]:
    return {part.strip() for part in value.split("/") if part.strip()}


def require_sha(value: str, label: str) -> None:
    if not SHA.fullmatch(value):
        raise SystemExit(f"malformed SHA for {label}: {value!r}")


def main() -> None:
    data = json.loads(LOCK.read_text(encoding="utf-8"))
    if data.get("schema_version") != 2:
        raise SystemExit("SOURCE_LOCKS.json schema_version must be 2")

    base_shas = [
        ("riemann.scientific_commit", data["riemann"]["scientific_commit"]),
        ("riemann.scientific_tree", data["riemann"]["scientific_tree"]),
        ("riemann.canonical_claims_blob", data["riemann"]["canonical_claims_blob"]),
        ("mathlib.commit", data["mathlib"]["commit"]),
        ("zeta23.previously_audited_commit", data["zeta23"]["previously_audited_commit"]),
        ("zeta23.selected_commit", data["zeta23"]["selected_commit"]),
        ("formal_conjectures.reference_commit", data["formal_conjectures"]["reference_commit"]),
    ]
    for label, value in base_shas:
        require_sha(value, label)

    if data["riemann"]["canonical_claim_count"] != 139:
        raise SystemExit("canonical claim count lock must be 139")
    if data["riemann"]["research_terminal_pr"] != 707:
        raise SystemExit("research cutoff must remain PR #707 for formal-v0.1")
    if data["formal_conjectures"]["proof_dependency"] is not False:
        raise SystemExit("Formal Conjectures must not be a proof dependency")
    if data["zeta23"]["theorem_bearing_Zeta23_directory_changed"] is not False:
        raise SystemExit("selected Zeta23 update requires a theorem-bearing audit")

    toolchain = (FORMAL / "lean-toolchain").read_text(encoding="utf-8").strip()
    if toolchain != data["lean"]["toolchain"]:
        raise SystemExit("lean-toolchain drift from SOURCE_LOCKS.json")

    lakefile = (FORMAL / "lakefile.toml").read_text(encoding="utf-8")
    for rev in (data["mathlib"]["commit"], data["zeta23"]["selected_commit"]):
        if rev not in lakefile:
            raise SystemExit(f"lakefile.toml does not contain locked revision {rev}")

    manifest = json.loads((FORMAL / "lake-manifest.json").read_text(encoding="utf-8"))
    packages = {p["name"]: p for p in manifest["packages"]}
    expected_packages = {
        "mathlib": data["mathlib"]["commit"],
        "Zeta23": data["zeta23"]["selected_commit"],
    }
    for name, rev in expected_packages.items():
        package = packages.get(name)
        if package is None:
            raise SystemExit(f"lake-manifest.json lacks {name}")
        if package.get("rev") != rev or package.get("inherited") is not False:
            raise SystemExit(f"lake-manifest.json drift for {name}")

    canonical_rows = read_tsv(CANONICAL)
    if len(canonical_rows) != data["riemann"]["canonical_claim_count"]:
        raise SystemExit("canonical claims file no longer matches the frozen claim-count lock")
    canonical = {row["semantic_id"]: row for row in canonical_rows}

    analysis_locks = data.get("analysis_scientific_claims", [])
    if not analysis_locks:
        raise SystemExit("analysis_scientific_claims is empty")
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for index, lock in enumerate(analysis_locks):
        sid = str(lock.get("semantic_id", ""))
        if sid not in canonical:
            raise SystemExit(f"analysis lock {index} has unknown semantic_id {sid!r}")
        require_sha(str(lock.get("source_sha", "")), f"analysis lock {sid}")
        if not isinstance(lock.get("source_pr"), int):
            raise SystemExit(f"analysis lock {sid} source_pr is not an integer")
        if not str(lock.get("source_path", "")).strip():
            raise SystemExit(f"analysis lock {sid} has no source_path")
        if not str(lock.get("source_claim_id", "")).strip():
            raise SystemExit(f"analysis lock {sid} has no source_claim_id")
        decls = lock.get("lean_declarations")
        if not isinstance(decls, list) or not decls or not all(isinstance(x, str) and x for x in decls):
            raise SystemExit(f"analysis lock {sid} has invalid lean_declarations")
        row = canonical[sid]
        if str(lock["source_pr"]) != row["source_pr"]:
            raise SystemExit(f"source PR drift for {sid}")
        if lock["source_sha"] != row["source_head_sha"]:
            raise SystemExit(f"source SHA drift for {sid}")
        grouped[sid].append(lock)

    for sid, locks in grouped.items():
        row = canonical[sid]
        locked_paths = {str(lock["source_path"]) for lock in locks}
        if locked_paths != split_paths(row["source_path"]):
            raise SystemExit(
                f"source path coverage drift for {sid}: locked={sorted(locked_paths)} "
                f"canonical={sorted(split_paths(row['source_path']))}"
            )
        locked_ids = {str(lock["source_claim_id"]) for lock in locks}
        canonical_ids = split_claim_ids(row["source_claim_id"])
        if canonical_ids and locked_ids != canonical_ids:
            raise SystemExit(
                f"source claim-ID coverage drift for {sid}: locked={sorted(locked_ids)} "
                f"canonical={sorted(canonical_ids)}"
            )

    owned_sources = "\n".join(
        path.read_text(encoding="utf-8")
        for directory in (
            FORMAL / "RiemannFormal" / "Analysis",
            FORMAL / "RiemannFormal" / "Upstream",
        )
        for path in directory.rglob("*.lean")
        if path.name != "SourceLocks.lean"
    )
    for lock in analysis_locks:
        for decl in lock["lean_declarations"]:
            short = decl.rsplit(".", 1)[-1]
            if short not in owned_sources:
                raise SystemExit(f"locked Lean declaration not found in owned source: {decl}")

    ledger = read_tsv(UPSTREAM_LEDGER)
    ledger_index: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in ledger:
        project = row["upstream_project"].lower()
        for token in row["exact_commit"].split(";"):
            commit = token.strip()
            if SHA.fullmatch(commit):
                for decl in row["exact_declaration"].split(";"):
                    ledger_index[(project, commit)].add(decl.strip())

    upstream_locks = data.get("analysis_upstream_declarations", [])
    if not upstream_locks:
        raise SystemExit("analysis_upstream_declarations is empty")
    project_commit = {
        "mathlib": data["mathlib"]["commit"],
        "zeta23": data["zeta23"]["selected_commit"],
    }
    for lock in upstream_locks:
        project = str(lock.get("project", "")).lower()
        commit = str(lock.get("commit", ""))
        require_sha(commit, f"upstream {project}")
        if project not in project_commit or commit != project_commit[project]:
            raise SystemExit(f"upstream pin drift for {project}")
        if not str(lock.get("source_path", "")).strip():
            raise SystemExit(f"upstream lock for {project} has no source_path")
        declarations = lock.get("declarations")
        if not isinstance(declarations, list) or not declarations:
            raise SystemExit(f"upstream lock for {project} has no declarations")
        available = ledger_index[(project, commit)]
        missing = [decl for decl in declarations if decl not in available]
        if missing:
            raise SystemExit(f"upstream declarations absent from A_UPSTREAM_REUSE.tsv: {missing}")

    lean_lock_text = SOURCE_LOCKS_LEAN.read_text(encoding="utf-8")
    for _, value in base_shas:
        if value not in lean_lock_text and value not in {
            data["riemann"]["scientific_tree"],
            data["riemann"]["canonical_claims_blob"],
            data["formal_conjectures"]["reference_commit"],
        }:
            raise SystemExit(f"SourceLocks.lean does not consume pinned SHA {value}")
    for lock in analysis_locks:
        for key in ("semantic_id", "source_sha", "source_path", "source_claim_id"):
            value = str(lock[key])
            if value not in lean_lock_text:
                raise SystemExit(f"SourceLocks.lean omits analysis lock value {value}")
    for lock in upstream_locks:
        if str(lock["source_path"]) not in lean_lock_text:
            raise SystemExit(f"SourceLocks.lean omits upstream path {lock['source_path']}")
        for decl in lock["declarations"]:
            if decl not in lean_lock_text:
                raise SystemExit(f"SourceLocks.lean omits upstream declaration {decl}")

    print(
        "PASS_FORMAL_SOURCE_LOCKS "
        f"claims={len(canonical_rows)} analysis_locks={len(analysis_locks)} "
        f"upstream_locks={len(upstream_locks)} "
        f"mathlib={data['mathlib']['commit'][:8]} zeta23={data['zeta23']['selected_commit'][:8]}"
    )


if __name__ == "__main__":
    main()
