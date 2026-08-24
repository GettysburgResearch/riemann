#!/usr/bin/env python3
from __future__ import annotations

import csv
import subprocess
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"
DELTA = FORMAL / "registry" / "deltas" / "C.tsv"
API = FORMAL / "registry" / "deltas" / "C_API.tsv"
CANONICAL = ROOT / "canonical" / "2026-08-22" / "claims.tsv"

PROVED = {"PROVED", "UPSTREAM_PROVED", "REFUTED_FORMALIZED"}
CONDITIONAL = {"PROVED_CONDITIONAL"}
BLOCKED = {"BLOCKED_LIBRARY", "BLOCKED_MATHEMATICS"}
ALLOWED = PROVED | CONDITIONAL | BLOCKED


def read(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def run_lean_checks(declarations: list[str]) -> str:
    lines = ["import RiemannFormal", ""]
    for declaration in declarations:
        lines.append(f"#check {declaration}")
        lines.append(f"#print {declaration}")
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".lean", dir=FORMAL, encoding="utf-8", delete=False
    ) as handle:
        handle.write("\n".join(lines) + "\n")
        source = Path(handle.name)
    try:
        completed = subprocess.run(
            ["lake", "env", "lean", source.name],
            cwd=FORMAL,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if completed.returncode != 0:
            raise SystemExit(
                "Lean declaration environment audit failed:\n" + completed.stdout
            )
        return completed.stdout
    finally:
        source.unlink(missing_ok=True)


def main() -> None:
    canonical_ids = {row["semantic_id"] for row in read(CANONICAL)}
    rows = read(DELTA)
    api_rows = read(API)
    if not rows:
        raise SystemExit("Reviewer C declaration delta is empty")

    semantic_ids = [row["semantic_id"].strip() for row in rows]
    duplicates = [key for key, count in Counter(semantic_ids).items() if count > 1]
    if duplicates:
        raise SystemExit(f"duplicate Reviewer C semantic IDs: {duplicates}")
    unknown = sorted(set(semantic_ids) - canonical_ids)
    if unknown:
        raise SystemExit(f"C.tsv contains noncanonical semantic IDs: {unknown}")

    declarations: list[str] = []
    counts: Counter[str] = Counter()
    for line_no, row in enumerate(rows, start=2):
        sid = row["semantic_id"].strip()
        declaration = row["lean_declaration"].strip()
        module = row["lean_module"].strip()
        status = row["formal_status"].strip()
        blocked_on = row["blocked_on"].strip()
        notes = row["notes"].strip()
        if not sid or not declaration or not module or not status or not notes:
            raise SystemExit(f"C.tsv:{line_no}: missing required field")
        if status not in ALLOWED:
            raise SystemExit(f"C.tsv:{line_no}: unsupported status {status}")
        if status in CONDITIONAL:
            if not blocked_on or "EXPLICIT_HYPOTHESES" not in notes:
                raise SystemExit(
                    f"C.tsv:{line_no}: conditional declaration lacks exact blockers/marker"
                )
        elif status in PROVED and blocked_on:
            raise SystemExit(
                f"C.tsv:{line_no}: proved declaration still has blocker {blocked_on!r}"
            )
        elif status in BLOCKED and not blocked_on:
            raise SystemExit(f"C.tsv:{line_no}: blocked declaration lacks blocker")
        deps = [x.strip() for x in row["formal_dependency_ids"].split(";") if x.strip()]
        bad_deps = sorted(set(deps) - canonical_ids)
        if bad_deps:
            raise SystemExit(f"C.tsv:{line_no}: unknown dependency IDs {bad_deps}")
        declarations.append(declaration)
        counts[status] += 1

    api_ids = [row["formal_api_id"].strip() for row in api_rows]
    api_dups = [key for key, count in Counter(api_ids).items() if count > 1]
    if api_dups:
        raise SystemExit(f"duplicate C API IDs: {api_dups}")
    for line_no, row in enumerate(api_rows, start=2):
        if not row["formal_api_id"].startswith("FORMAL.API.OPERATOR."):
            raise SystemExit(f"C_API.tsv:{line_no}: invalid API ID")
        if row["formal_status"] not in {"PROVED", "PROVED_CONDITIONAL"}:
            raise SystemExit(f"C_API.tsv:{line_no}: invalid API status")
        if row["source_semantic_id"] not in canonical_ids:
            raise SystemExit(f"C_API.tsv:{line_no}: unknown source semantic ID")
        declarations.append(row["lean_declaration"].strip())

    declarations = list(dict.fromkeys(declarations))
    output = run_lean_checks(declarations)
    for declaration in declarations:
        if declaration not in output:
            raise SystemExit(
                f"Lean output did not contain fully qualified declaration {declaration}"
            )

    generated = FORMAL / "reports" / "generated"
    generated.mkdir(parents=True, exist_ok=True)
    (generated / "C_DECLARATION_TYPES.txt").write_text(output, encoding="utf-8")

    rendered = " ".join(f"{key}={counts[key]}" for key in sorted(counts))
    print(
        "PASS_REVIEWER_C_DECLARATION_ENVIRONMENT "
        f"canonical_rows={len(rows)} api_rows={len(api_rows)} "
        f"declarations={len(declarations)} {rendered}"
    )


if __name__ == "__main__":
    main()
