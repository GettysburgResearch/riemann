#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "formal" / "blueprint" / "src"
ROOT_CONTENT = (SRC / "content.tex").read_text(encoding="utf-8")
FRAGMENTS = [SRC / "content-A.tex", SRC / "content-B.tex", SRC / "content-C.tex"]
CONTENT = ROOT_CONTENT + "\n" + "\n".join(p.read_text(encoding="utf-8") for p in FRAGMENTS)

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

for owner in "ABC":
    if f"\\input{{content-{owner}}}" not in ROOT_CONTENT:
        raise SystemExit(f"content.tex does not include Reviewer {owner}'s fragment")

if ROOT_CONTENT.count("\\lean{RiemannFormal.RH}") != 1:
    raise SystemExit("blueprint must contain exactly one canonical RH declaration link")

print("PASS_FORMAL_BLUEPRINT_SCAFFOLD fragments=3")
