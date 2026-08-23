#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = (ROOT / "formal" / "blueprint" / "src" / "content.tex").read_text(encoding="utf-8")
REQUIRED = {
    "CONSUMER.MELLIN.TWO\\_ROW",
    "CONSUMER.MELLIN.FIVE\\_THREE",
    "API.MELLIN.SUBPOWER\\_NEGATIVE\\_MASS",
    "OPEN.ARITH.CV",
    "OPEN.ARITH.XD",
    "OPEN.ARITH.BPOE",
    "OPERATOR.XI.PICK\\_ORDER3",
}
missing = sorted(x for x in REQUIRED if x not in CONTENT)
if missing:
    raise SystemExit(f"blueprint is missing semantic IDs: {missing}")
print("PASS_FORMAL_BLUEPRINT_SCAFFOLD")
