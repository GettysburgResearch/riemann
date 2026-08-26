#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
PRINT_RE = re.compile(r"^\s*#print\s+axioms\s+([A-Za-z0-9_.]+)\s*$")
OUTPUT_NAME_RE = re.compile(r"['\u2018\u2019]?([A-Za-z0-9_.]+)['\u2018\u2019]?")


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


def parse_output(text: str) -> tuple[set[str], dict[str, set[str]]]:
    if "sorryAx" in text:
        raise SystemExit("axiom audit contains sorryAx")

    seen: set[str] = set()
    dependencies: dict[str, set[str]] = {}
    lines = text.splitlines()
    logical_lines: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if "depends on axioms:" in line:
            payload = line.split("depends on axioms:", 1)[1].strip()
            if payload.startswith("[") and not payload.endswith("]"):
                fragments = [line]
                while not fragments[-1].rstrip().endswith("]"):
                    index += 1
                    if index >= len(lines):
                        raise SystemExit(f"unclosed axiom line: {' '.join(fragments)}")
                    fragments.append(lines[index].strip())
                line = " ".join(fragments)
        logical_lines.append(line)
        index += 1

    for line in logical_lines:
        if "depends on axioms:" not in line and "does not depend on any axioms" not in line:
            continue
        head = line.split("depends on axioms:", 1)[0].split("does not depend", 1)[0]
        matches = OUTPUT_NAME_RE.findall(head)
        if not matches:
            raise SystemExit(f"cannot parse declaration name from axiom line: {line}")
        declaration = matches[-1]
        seen.add(declaration)

        names: set[str] = set()
        if "depends on axioms:" in line:
            payload = line.split("depends on axioms:", 1)[1].strip()
            if not (payload.startswith("[") and payload.endswith("]")):
                raise SystemExit(f"unparsed axiom line: {line}")
            names = {x.strip() for x in payload[1:-1].split(",") if x.strip()}
            extra = names - ALLOWED
            if extra:
                raise SystemExit(
                    f"forbidden axioms {sorted(extra)} for {declaration}: {line}"
                )
        dependencies[declaration] = names
    return seen, dependencies


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit("usage: audit_axiom_output.py AXIOM_OUTPUT PRINT_SOURCE...")

    expected = expected_declarations([Path(arg) for arg in sys.argv[2:]])
    seen, dependencies = parse_output(Path(sys.argv[1]).read_text(encoding="utf-8"))

    missing = expected - seen
    if missing:
        raise SystemExit(f"missing #print axioms output for {sorted(missing)}")
    unexpected = seen - expected
    if unexpected:
        raise SystemExit(f"unexpected axiom-audit declarations: {sorted(unexpected)}")

    conditional = sum(bool(dependencies[name]) for name in expected)
    print(
        "PASS_FORMAL_AXIOM_OUTPUT "
        f"declarations={len(expected)} with_permitted_axioms={conditional}"
    )


if __name__ == "__main__":
    main()
