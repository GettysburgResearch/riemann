#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"
REPORT = FORMAL / "reports" / "C_OPERATOR_QA.tsv"


def read(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def theorem_signature(text: str, theorem: str) -> str:
    match = re.search(
        rf"\btheorem\s+{re.escape(theorem)}\b(?P<body>.*?)(?::=\s*by|:=)",
        text,
        flags=re.S,
    )
    if not match:
        raise SystemExit(f"cannot extract theorem signature for {theorem}")
    signature = f"theorem {theorem}" + match.group("body")
    signature = re.sub(r"/--.*?-\/", "", signature, flags=re.S)
    signature = re.sub(r"--.*", "", signature)
    return re.sub(r"\s+", " ", signature).strip()


def compile_module(module: str, theorem: str, statement: str | None) -> str:
    lines = [f"import {module}", f"#check {theorem}"]
    if statement:
        lines.append(f"#check ({theorem} : {statement})")
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
                f"comparator type check failed for {module}:\n{completed.stdout}"
            )
        return completed.stdout
    finally:
        source.unlink(missing_ok=True)


def main() -> None:
    rows = read(REPORT)
    checked = [row for row in rows if row["comparator_topic"] != "NOT_APPLICABLE"]
    outputs: list[str] = []
    for row in checked:
        topic = row["comparator_topic"]
        challenge = FORMAL / "comparator" / "Challenge" / f"{topic}.lean"
        solution = FORMAL / "comparator" / "Solution" / f"{topic}.lean"
        if not challenge.is_file() or not solution.is_file():
            raise SystemExit(f"missing comparator pair for {topic}")
        ctext = challenge.read_text(encoding="utf-8")
        stext = solution.read_text(encoding="utf-8")
        c_theorems = re.findall(r"\btheorem\s+([A-Za-z0-9_]+)", ctext)
        s_theorems = re.findall(r"\btheorem\s+([A-Za-z0-9_]+)", stext)
        common = [name for name in c_theorems if name in set(s_theorems)]
        if len(common) != 1:
            raise SystemExit(f"{topic}: expected one shared theorem name, found {common}")
        theorem = common[0]
        if theorem_signature(ctext, theorem) != theorem_signature(stext, theorem):
            raise SystemExit(f"{topic}: Challenge/Solution theorem signatures differ")
        placeholder_count = len(re.findall(r"\b(?:sorry|admit)\b", ctext))
        solution_placeholders = len(re.findall(r"\b(?:sorry|admit)\b", stext))
        if placeholder_count != 1 or solution_placeholders != 0:
            raise SystemExit(
                f"{topic}: invalid placeholder boundary "
                f"challenge={placeholder_count} solution={solution_placeholders}"
            )
        statement = row["comparator_statement"].strip() or None
        outputs.append(compile_module(f"Challenge.{topic}", theorem, statement))
        outputs.append(compile_module(f"Solution.{topic}", theorem, statement))

    generated = FORMAL / "reports" / "generated"
    generated.mkdir(parents=True, exist_ok=True)
    (generated / "C_COMPARATOR_TYPES.txt").write_text("\n".join(outputs), encoding="utf-8")
    print(f"PASS_REVIEWER_C_COMPARATOR_FIDELITY topics={len(checked)}")


if __name__ == "__main__":
    main()
