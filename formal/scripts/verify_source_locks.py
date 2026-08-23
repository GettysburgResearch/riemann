#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCK = ROOT / "formal" / "registry" / "SOURCE_LOCKS.json"
SHA = re.compile(r"^[0-9a-f]{40}$")


def main() -> None:
    data = json.loads(LOCK.read_text(encoding="utf-8"))
    checks = [
        data["riemann"]["scientific_commit"],
        data["riemann"]["scientific_tree"],
        data["riemann"]["canonical_claims_blob"],
        data["mathlib"]["commit"],
        data["zeta23"]["previously_audited_commit"],
        data["zeta23"]["selected_commit"],
        data["formal_conjectures"]["reference_commit"],
    ]
    bad = [x for x in checks if not SHA.fullmatch(x)]
    if bad:
        raise SystemExit(f"malformed locked SHA(s): {bad}")
    if data["riemann"]["canonical_claim_count"] != 139:
        raise SystemExit("canonical claim count lock must be 139")
    if data["riemann"]["research_terminal_pr"] != 707:
        raise SystemExit("research cutoff must remain PR #707 for formal-v0.1")
    if data["formal_conjectures"]["proof_dependency"] is not False:
        raise SystemExit("Formal Conjectures must not be a proof dependency")
    print("PASS_FORMAL_SOURCE_LOCKS")


if __name__ == "__main__":
    main()
