#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
PRINT_RE = re.compile(r"^\s*#print\s+axioms\s+([A-Za-z0-9_.]+)\s*$")
OUTPUT_NAME_RE = re.compile(r"['‘’]?([A-Za-z0-9_.]+)['‘’]?")


def expected_declarations() -> set[str]:
    formal = Path(__file__).resolve().parents[1]
    files = [
        formal / "RiemannFormal" / "AxiomAudit.lean",
        formal / "RiemannFormal" / "Analysis" / "AxiomAudit.lean",
    ]
    files.extend(sorted((formal / "comparator" / "PrintAxioms").glob("*.lean")))
    expected: set[str] = set()
    for path in files:
        if not path.is_file():
            raise SystemExit(f"missing axiom-print source: {path}")
        for line in path.read_text(encoding="utf-8").splitlines():
            match = PRINT_RE.match(line)
            if match:
                expected.add(match.group(1))
    if not expected:
        raise SystemExit("no #print axioms declarations discovered")
    return expected


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: audit_axiom_output.py AXIOM_OUTPUT")
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    if "sorryAx" in text:
        raise SystemExit("axiom audit contains sorryAx")

    expected = expected_declarations()
    seen: set[str] = set()
    for line in text.splitlines():
        if "depends on axioms:" not in line and "does not depend on any axioms" not in line:
            continue
        head = line.split("depends on axioms:", 1)[0].split("does not depend", 1)[0]
        matches = OUTPUT_NAME_RE.findall(head)
        if matches:
            seen.add(matches[-1])
        if "depends on axioms:" in line:
            payload = line.split("depends on axioms:", 1)[1].strip()
            if not (payload.startswith("[") and payload.endswith("]")):
                raise SystemExit(f"unparsed axiom line: {line}")
            names = {x.strip() for x in payload[1:-1].split(",") if x.strip()}
            extra = names - ALLOWED
            if extra:
                raise SystemExit(f"forbidden axioms {sorted(extra)} in line: {line}")

    missing = expected - seen
    if missing:
        raise SystemExit(f"missing #print axioms output for {sorted(missing)}")
    print(f"PASS_FORMAL_AXIOM_OUTPUT declarations={len(seen)} expected={len(expected)}")


if __name__ == "__main__":
    main()
