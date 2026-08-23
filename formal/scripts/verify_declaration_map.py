#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"
DELTA = FORMAL / "registry" / "deltas" / "C.tsv"
DECL_RE_TEMPLATE = r"\b(?:theorem|lemma|def|structure|inductive|abbrev)\s+{name}\b"

PROVED = {"PROVED", "UPSTREAM_PROVED", "REFUTED_FORMALIZED"}
CONDITIONAL = {"PROVED_CONDITIONAL"}
BLOCKED = {"BLOCKED_LIBRARY", "BLOCKED_MATHEMATICS"}


def module_path(module: str) -> Path:
    return FORMAL / (module.replace(".", "/") + ".lean")


def declaration_exists(path: Path, declaration: str) -> bool:
    leaf = declaration.rsplit(".", 1)[-1]
    pattern = re.compile(DECL_RE_TEMPLATE.format(name=re.escape(leaf)))
    return bool(pattern.search(path.read_text(encoding="utf-8")))


def main() -> None:
    with DELTA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if not rows:
        raise SystemExit("Reviewer C declaration delta is empty")

    semantic_ids = [row["semantic_id"].strip() for row in rows]
    duplicates = [key for key, count in Counter(semantic_ids).items() if count > 1]
    if duplicates:
        raise SystemExit(f"duplicate Reviewer C semantic IDs: {duplicates}")

    counts: Counter[str] = Counter()
    for line_no, row in enumerate(rows, start=2):
        semantic_id = row["semantic_id"].strip()
        declaration = row["lean_declaration"].strip()
        module = row["lean_module"].strip()
        status = row["formal_status"].strip()
        blocked_on = row["blocked_on"].strip()
        notes = row["notes"].strip()

        if not semantic_id or not declaration or not module or not status:
            raise SystemExit(f"C.tsv:{line_no}: missing required field")
        path = module_path(module)
        if not path.is_file():
            raise SystemExit(f"C.tsv:{line_no}: module path does not exist: {path}")
        if not declaration_exists(path, declaration):
            raise SystemExit(
                f"C.tsv:{line_no}: declaration {declaration} not found in {path}"
            )

        if status in CONDITIONAL:
            if not blocked_on:
                raise SystemExit(
                    f"C.tsv:{line_no}: conditional theorem lacks blocked_on inputs"
                )
            if "EXPLICIT_HYPOTHESES" not in notes:
                raise SystemExit(
                    f"C.tsv:{line_no}: conditional theorem lacks explicit-hypothesis marker"
                )
        elif status in PROVED:
            if blocked_on:
                raise SystemExit(
                    f"C.tsv:{line_no}: proved declaration still has blocked_on={blocked_on!r}"
                )
        elif status in BLOCKED:
            if not blocked_on:
                raise SystemExit(
                    f"C.tsv:{line_no}: blocked declaration lacks a named blocker"
                )
        else:
            raise SystemExit(f"C.tsv:{line_no}: unsupported Reviewer C status {status}")

        counts[status] += 1

    rendered = " ".join(f"{key}={counts[key]}" for key in sorted(counts))
    print(f"PASS_REVIEWER_C_DECLARATION_MAP rows={len(rows)} {rendered}")


if __name__ == "__main__":
    main()
