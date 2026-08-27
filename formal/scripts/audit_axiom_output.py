#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
PRINT_RE = re.compile(r"^\s*#print\s+axioms\s+([A-Za-z0-9_.]+)\s*$")
OUTPUT_NAME_RE = re.compile(r"['‘’]?([A-Za-z0-9_.]+)['‘’]?")
AXIOM_PAYLOAD_RE = re.compile(
    r"^\[\s*(?P<body>(?:[A-Za-z0-9_.]+\s*(?:,\s*[A-Za-z0-9_.]+\s*)*)?)\]$"
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
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if "sorryAx" in text:
        raise SystemExit("axiom audit contains sorryAx")

    expected = expected_declarations([Path(arg) for arg in sys.argv[2:]])
    seen: set[str] = set()
    lines = text.splitlines()
    line_index = 0
    while line_index < len(lines):
        line = lines[line_index]
        if "depends on axioms:" not in line and "does not depend on any axioms" not in line:
            line_index += 1
            continue
        head = line.split("depends on axioms:", 1)[0].split("does not depend", 1)[0]
        matches = OUTPUT_NAME_RE.findall(head)
        if not matches:
            raise SystemExit(f"unparsed axiom declaration: {line}")
        declaration = matches[-1]
        if declaration in seen:
            raise SystemExit(f"duplicate #print axioms output for {declaration}")
        if "depends on axioms:" in line:
            payload = line.split("depends on axioms:", 1)[1].strip()
            if not payload.startswith("["):
                raise SystemExit(f"unparsed axiom line: {line}")
            while "]" not in payload:
                line_index += 1
                if line_index >= len(lines):
                    raise SystemExit(f"unterminated axiom list for {declaration}")
                continuation = lines[line_index].strip()
                if (
                    "depends on axioms:" in continuation
                    or "does not depend on any axioms" in continuation
                ):
                    raise SystemExit(f"unterminated axiom list for {declaration}")
                payload = f"{payload} {continuation}"
            payload_match = AXIOM_PAYLOAD_RE.fullmatch(payload)
            if not payload_match:
                raise SystemExit(f"unparsed axiom payload for {declaration}: {payload}")
            body = payload_match.group("body")
            names = {x.strip() for x in body.split(",") if x.strip()}
            extra = names - ALLOWED
            if extra:
                raise SystemExit(f"forbidden axioms {sorted(extra)} for {declaration}")
        seen.add(declaration)
        line_index += 1

    missing = expected - seen
    unexpected = seen - expected
    if missing:
        raise SystemExit(f"missing #print axioms output for {sorted(missing)}")
    if unexpected:
        raise SystemExit(f"unexpected #print axioms output for {sorted(unexpected)}")
    print(f"PASS_FORMAL_AXIOM_OUTPUT declarations={len(seen)} expected={len(expected)}")


if __name__ == "__main__":
    main()
