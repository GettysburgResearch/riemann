#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
EXPECTED = {
    "RiemannFormal.rh_iff_mathlib",
    "RiemannFormal.Upstream.projectRH_is_mathlib",
    "RiemannFormal.Upstream.zeta23_bridge_preserves_RH",
    "RiemannFormal.Release20260822.researchCutoff_eq",
    "RiemannFormal.Release20260822.semanticClaimCount_eq",
    "rh_statement_exact",
}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: audit_axiom_output.py AXIOM_OUTPUT")
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    if "sorryAx" in text:
        raise SystemExit("axiom audit contains sorryAx")

    seen: set[str] = set()
    theorem_pat = re.compile(r"['\u2018\u2019]?([A-Za-z0-9_.]+)['\u2018\u2019]?")
    for line in text.splitlines():
        if "depends on axioms:" not in line and "does not depend on any axioms" not in line:
            continue
        head = line.split("depends on axioms:", 1)[0].split("does not depend", 1)[0]
        matches = theorem_pat.findall(head)
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

    missing = EXPECTED - seen
    if missing:
        raise SystemExit(f"missing #print axioms output for {sorted(missing)}")
    print(f"PASS_FORMAL_AXIOM_OUTPUT declarations={len(seen)}")


if __name__ == "__main__":
    main()
