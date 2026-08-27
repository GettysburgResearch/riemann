#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).with_name("audit_axiom_output.py")


def run_case(name: str, sources: dict[str, str], output: str, should_pass: bool) -> None:
    with tempfile.TemporaryDirectory(prefix=f"axiom-audit-{name}-") as tmp:
        root = Path(tmp)
        source_paths: list[str] = []
        for filename, content in sources.items():
            path = root / filename
            path.write_text(content, encoding="utf-8", newline="\n")
            source_paths.append(str(path))
        output_path = root / "output.txt"
        output_path.write_text(output, encoding="utf-8", newline="\n")
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), str(output_path), *source_paths],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            check=False,
        )
        passed = completed.returncode == 0
        if passed != should_pass:
            raise SystemExit(
                f"case {name} expected pass={should_pass}, got {passed}:\n{completed.stdout}"
            )


SOURCES = {
    "one.lean": "#print axioms Demo.one\n",
    "two.lean": "#print axioms Demo.two\n",
}
GOOD = (
    "'Demo.one' depends on axioms: [propext, Classical.choice, Quot.sound]\n"
    "'Demo.two' does not depend on any axioms\n"
)

run_case("good", SOURCES, GOOD, True)
run_case("crlf_and_repeat", SOURCES, (GOOD + GOOD.splitlines()[0] + "\n").replace("\n", "\r\n"), True)
run_case("missing", SOURCES, "'Demo.one' depends on axioms: [propext]\n", False)
run_case("unexpected", SOURCES, GOOD + "'Demo.extra' does not depend on any axioms\n", False)
run_case(
    "sorry_ax",
    SOURCES,
    "'Demo.one' depends on axioms: [propext, sorryAx]\n"
    "'Demo.two' does not depend on any axioms\n",
    False,
)
run_case(
    "forbidden",
    SOURCES,
    "'Demo.one' depends on axioms: [Project.unreviewed]\n"
    "'Demo.two' does not depend on any axioms\n",
    False,
)
run_case(
    "unterminated",
    SOURCES,
    "'Demo.one' depends on axioms: [propext,\n"
    "'Demo.two' does not depend on any axioms\n",
    False,
)
print("PASS_FORMAL_AXIOM_AUDIT_REGRESSION cases=7 duplicate_prints_allowed=true")
