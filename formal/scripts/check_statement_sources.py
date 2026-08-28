#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"
CANONICAL = ROOT / "canonical" / "2026-08-22" / "claims.tsv"
DELTA = FORMAL / "registry" / "deltas" / "C.tsv"
API = FORMAL / "registry" / "deltas" / "C_API.tsv"
LOCKS = FORMAL / "registry" / "deltas" / "C_EXTERNAL_SOURCE_LOCKS.tsv"
REPORT = FORMAL / "reports" / "C_OPERATOR_QA.tsv"
SHARED = (
    FORMAL / "comparator" / "ChallengeDeps" /
    "RiemannComparatorChallengeDeps" / "XiPickOrderThreeConditional.lean"
)
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def run_script(name: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(FORMAL / "scripts" / name)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise SystemExit(f"{name} failed:\n{completed.stdout}")
    return completed.stdout.strip()


def main() -> None:
    canonical_rows = load(CANONICAL)
    delta_rows = load(DELTA)
    api_rows = load(API)
    lock_rows = load(LOCKS)
    report_rows = load(REPORT)
    canonical = {row["semantic_id"]: row for row in canonical_rows}
    report = {row["semantic_id"]: row for row in report_rows}
    locks = {row["lock_id"]: row for row in lock_rows}

    if len(report) != len(report_rows):
        raise SystemExit("duplicate semantic IDs in C_OPERATOR_QA.tsv")
    if len(locks) != len(lock_rows):
        raise SystemExit("duplicate external source-lock IDs")
    if set(report) != {row["semantic_id"] for row in delta_rows}:
        raise SystemExit("C_OPERATOR_QA.tsv and C.tsv semantic-ID sets differ")

    shared_text = SHARED.read_text(encoding="utf-8")
    checked_sources = 0
    checked_locks: set[str] = set()
    for row in delta_rows:
        sid = row["semantic_id"]
        source = canonical.get(sid)
        qa = report[sid]
        if source is None:
            raise SystemExit(f"Reviewer C semantic ID is not canonical: {sid}")
        expected = {
            "declaration": row["lean_declaration"],
            "module": row["lean_module"],
            "formal_verdict": row["formal_status"],
            "scientific_verdict": source["final_verdict"],
            "source_sha": source["source_head_sha"],
            "source_path": source["source_path"],
        }
        for field, value in expected.items():
            if qa[field] != value:
                raise SystemExit(
                    f"{sid}: QA {field}={qa[field]!r}, expected {value!r}"
                )
        if not SHA40.fullmatch(qa["source_sha"]):
            raise SystemExit(f"{sid}: malformed source SHA {qa['source_sha']!r}")
        if not qa["source_path"]:
            raise SystemExit(f"{sid}: empty source path")
        checked_sources += 1

        status = row["formal_status"]
        hypotheses = qa["explicit_hypotheses"].strip()
        if status == "PROVED_CONDITIONAL" and not hypotheses:
            raise SystemExit(f"{sid}: conditional theorem lacks explicit hypotheses")
        if status in {"PROVED", "REFUTED_FORMALIZED"} and row["blocked_on"]:
            raise SystemExit(f"{sid}: proved row has a blocker")
        if status.startswith("BLOCKED") and not row["blocked_on"]:
            raise SystemExit(f"{sid}: blocked row lacks blocker")
        if qa["axiom_audit_mode"] != "GENERATED_FROM_C_TSV":
            raise SystemExit(f"{sid}: axiom evidence is not registry-generated")

        external_ids = [x.strip() for x in qa["external_lock_ids"].split(";") if x.strip()]
        for lock_id in external_ids:
            lock = locks.get(lock_id)
            if lock is None:
                raise SystemExit(f"{sid}: unknown external lock {lock_id}")
            consumers = {
                x.strip() for x in lock["consumer_semantic_ids"].split(";") if x.strip()
            }
            if sid not in consumers:
                raise SystemExit(f"{sid}: external lock {lock_id} does not name consumer")
            checked_locks.add(lock_id)

    statement_dir = FORMAL / "registry" / "deltas" / "C_EXTERNAL_SOURCE_STATEMENTS"
    for lock_id, lock in locks.items():
        if not SHA256.fullmatch(lock["normalized_statement_sha256"]):
            raise SystemExit(f"{lock_id}: malformed normalized statement SHA-256")
        statement_file = statement_dir / f"{lock_id}.txt"
        if not statement_file.is_file():
            raise SystemExit(f"{lock_id}: missing normalized external statement record")
        actual_statement_hash = hashlib.sha256(statement_file.read_bytes()).hexdigest()
        if actual_statement_hash != lock["normalized_statement_sha256"]:
            raise SystemExit(
                f"{lock_id}: normalized external statement hash mismatch "
                f"{actual_statement_hash}"
            )
        if not SHA256.fullmatch(lock["artifact_sha256"]):
            raise SystemExit(f"{lock_id}: malformed artifact SHA-256")
        if lock["artifact_sha256"] != actual_statement_hash:
            raise SystemExit(f"{lock_id}: artifact hash does not bind normalized record")
        if lock["simplicity_required"] not in {"true", "false"}:
            raise SystemExit(f"{lock_id}: simplicity_required must be true/false")
        if lock["exact_height"] != "3000175332800":
            raise SystemExit(f"{lock_id}: unexpected verified height")
        literals = [
            lock["source_title"], lock["authors"], lock["journal"], lock["doi"],
            lock["arxiv"], lock["artifact_identifier"], lock["artifact_hash_scope"],
            lock["artifact_sha256"], lock["normalized_statement_sha256"],
            lock["exact_height"],
            lock["lean_lock"].rsplit(".", 1)[-1],
            lock["lean_theorem_shape"].rsplit(".", 1)[-1],
        ]
        missing = [literal for literal in literals if literal not in shared_text]
        if missing:
            raise SystemExit(f"{lock_id}: Lean source-lock object lacks {missing}")
        if lock["simplicity_required"] == "false" and \
                "Simplicity is deliberately not included" not in shared_text:
            raise SystemExit(f"{lock_id}: non-use of simplicity is undocumented in Lean")

    api_ids = [row["formal_api_id"] for row in api_rows]
    if len(api_ids) != len(set(api_ids)):
        raise SystemExit("duplicate formal API IDs")
    for row in api_rows:
        if row["source_semantic_id"] not in canonical:
            raise SystemExit(
                f"{row['formal_api_id']}: unknown canonical source semantic ID"
            )

    comparator_output = run_script("verify_comparator_fidelity.py")
    usage_output = run_script("check_external_input_usage.py")
    static_output = run_script("verify_c_repair_static.py")

    evidence = {
        "canonical_rows": len(canonical_rows),
        "reviewer_c_rows": len(delta_rows),
        "api_rows": len(api_rows),
        "source_rows_checked": checked_sources,
        "external_locks_checked": sorted(checked_locks),
        "comparator": comparator_output,
        "external_usage": usage_output,
        "static_replay": static_output,
        "report_sha256": hashlib.sha256(REPORT.read_bytes()).hexdigest(),
        "rh_proved": False,
    }
    generated = FORMAL / "reports" / "generated"
    generated.mkdir(parents=True, exist_ok=True)
    (generated / "C_SOURCE_AND_COMPARATOR_EVIDENCE.json").write_text(
        json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        "PASS_REVIEWER_C_STATEMENT_SOURCES "
        f"rows={len(delta_rows)} api={len(api_rows)} locks={len(checked_locks)}"
    )


if __name__ == "__main__":
    main()
