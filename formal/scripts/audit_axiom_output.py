#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
PRINT_RE = re.compile(r"^\s*#print\s+axioms\s+([A-Za-z0-9_.]+)\s*$")
THEOREM_RE = re.compile(r"['\u2018\u2019]?([A-Za-z0-9_.]+)['\u2018\u2019]?")


def expected_from_sources(paths: list[Path]) -> set[str]:
    expected: set[str] = set()
    for path in paths:
        if not path.is_file():
            raise SystemExit(f"axiom audit source does not exist: {path}")
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
    for line in text.splitlines():
        if "depends on axioms:" not in line and "does not depend on any axioms" not in line:
            continue
        head = line.split("depends on axioms:", 1)[0].split("does not depend", 1)[0]
        matches = THEOREM_RE.findall(head)
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
        raise SystemExit(
            "usage: audit_axiom_output.py AXIOM_OUTPUT AXIOM_SOURCE [AXIOM_SOURCE ...]"
        )
    output = Path(sys.argv[1])
    sources = [Path(x) for x in sys.argv[2:]]
    expected = expected_from_sources(sources)
    seen, dependencies = parse_output(output.read_text(encoding="utf-8"))

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
