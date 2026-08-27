#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
PRINT_RE = re.compile(r"^\s*#print\s+axioms\s+([A-Za-z0-9_.]+)\s*$")
OUTPUT_RE = re.compile(
    r"(?m)^['‘’]?([A-Za-z0-9_.]+)['‘’]?\s+"
    r"(?:does not depend on any axioms|depends on axioms:\s*\[([^\]]*)\])\s*$"
)


def expected_declarations(paths: list[Path]) -> set[str]:
    expected: set[str] = set()
    for path in paths:
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
    if len(sys.argv) < 3:
        raise SystemExit("usage: audit_axiom_output.py AXIOM_OUTPUT PRINT_SOURCE...")
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    if "sorryAx" in text:
        raise SystemExit("axiom audit contains sorryAx")

    expected = expected_declarations([Path(arg) for arg in sys.argv[2:]])
    seen: set[str] = set()
    for match in OUTPUT_RE.finditer(text):
        seen.add(match.group(1))
        payload = match.group(2)
        if payload is not None:
            names = {x.strip() for x in payload.split(",") if x.strip()}
            extra = names - ALLOWED
            if extra:
                raise SystemExit(
                    f"forbidden axioms {sorted(extra)} for {match.group(1)}"
                )

    missing = expected - seen
    if missing:
        raise SystemExit(f"missing #print axioms output for {sorted(missing)}")
    print(f"PASS_FORMAL_AXIOM_OUTPUT declarations={len(seen)} expected={len(expected)}")


if __name__ == "__main__":
    main()
