#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"
CANONICAL = ROOT / "canonical" / "2026-08-22" / "claims.tsv"
DELTA = FORMAL / "registry" / "deltas" / "C.tsv"
REPORT = FORMAL / "reports" / "C_OPERATOR_QA.tsv"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
BOOL = {"true", "false"}


def load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    canonical_rows = load(CANONICAL)
    delta_rows = load(DELTA)
    report_rows = load(REPORT)
    canonical = {row["semantic_id"]: row for row in canonical_rows}
    report = {row["semantic_id"]: row for row in report_rows}

    if len(report) != len(report_rows):
        raise SystemExit("duplicate semantic IDs in C_OPERATOR_QA.tsv")

    for row in delta_rows:
        sid = row["semantic_id"]
        source = canonical.get(sid)
        qa = report.get(sid)
        if source is None:
            raise SystemExit(f"Reviewer C semantic ID is not canonical: {sid}")
        if qa is None:
            raise SystemExit(f"QA report lacks Reviewer C row: {sid}")

        expected_pairs = {
            "declaration": row["lean_declaration"],
            "formal_verdict": row["formal_status"],
            "scientific_verdict": source["final_verdict"],
            "source_sha": source["source_head_sha"],
            "source_path": source["source_path"],
        }
        for field, expected in expected_pairs.items():
            if qa[field] != expected:
                raise SystemExit(
                    f"{sid}: QA {field}={qa[field]!r}, expected {expected!r}"
                )

        if not SHA_RE.fullmatch(qa["source_sha"]):
            raise SystemExit(f"{sid}: malformed source SHA {qa['source_sha']!r}")
        if not qa["source_path"]:
            raise SystemExit(f"{sid}: empty source path")

        for field in (
            "statement_exists", "proved", "proved_conditionally",
            "source_locked", "comparator_checked", "axiom_audited",
        ):
            if qa[field] not in BOOL:
                raise SystemExit(f"{sid}: {field} must be true/false")

        if qa["statement_exists"] != "true":
            raise SystemExit(f"{sid}: declaration is not marked as existing")
        if qa["source_locked"] != "true":
            raise SystemExit(f"{sid}: source is not locked")
        if qa["axiom_audited"] != "true":
            raise SystemExit(f"{sid}: axiom audit is not required by the report")

        status = row["formal_status"]
        if status == "PROVED_CONDITIONAL":
            if qa["proved"] != "false" or qa["proved_conditionally"] != "true":
                raise SystemExit(f"{sid}: conditional status is misrepresented")
            if not qa["explicit_hypotheses"]:
                raise SystemExit(f"{sid}: conditional theorem lacks explicit hypotheses")
        elif status in {"PROVED", "UPSTREAM_PROVED", "REFUTED_FORMALIZED"}:
            if qa["proved"] != "true" or qa["proved_conditionally"] != "false":
                raise SystemExit(f"{sid}: proved/refuted status is misrepresented")
        else:
            if qa["proved"] != "false":
                raise SystemExit(f"{sid}: blocked statement cannot be marked proved")

    extra = sorted(set(report) - {row["semantic_id"] for row in delta_rows})
    if extra:
        raise SystemExit(f"QA report contains rows outside C.tsv: {extra}")

    print(
        "PASS_REVIEWER_C_STATEMENT_SOURCES "
        f"rows={len(delta_rows)} canonical_claims={len(canonical_rows)}"
    )


if __name__ == "__main__":
    main()
