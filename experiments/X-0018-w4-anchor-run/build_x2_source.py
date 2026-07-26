#!/usr/bin/env python3
"""Patch the reviewed PR #103 completed-xi producer to emit only x=2 (u=w=4).

Agent: claude-02.  Executes step 1 of the PR #128 / X-9312 CANDIDATE_HANDOFF:
"Patch the reviewed PR #103 completed-xi producer to emit one point at x=2."

The reviewed producer represents x = 2^-xbits; xbits = -1 gives x = 2 exactly
through arb_mul_2exp_si (an exact power-of-two scaling), and Re s = 1/2 + x
= 5/2.  Two mechanical fixes are required for negative xbits, both confined
to JSON emission (never touching evaluation):

  * `UWORD(1) << xbits` is undefined for xbits < 0; emit the x rational as
    numerator/denominator with the shift applied on the correct side;
  * the emitted numerator becomes 2 rather than 1.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

GRID = re.compile(r"#define X_COUNT [0-9]+\nstatic const int X_BITS\[X_COUNT\] = \{[^\n]+\};\n")
GRID_NEW = "#define X_COUNT 1\nstatic const int X_BITS[X_COUNT] = {-1};\n"
DEN = "    ulong denominator = UWORD(1) << xbits;\n"
DEN_NEW = ("    ulong numerator = (xbits >= 0) ? UWORD(1) : (UWORD(1) << (ulong) (-xbits));\n"
           "    ulong denominator = (xbits >= 0) ? (UWORD(1) << (ulong) xbits) : UWORD(1);\n")
PRINT = '    flint_printf("\\"x\\":{\\"numerator\\":1,\\"denominator\\":%wu},", denominator);\n'
PRINT_NEW = '    flint_printf("\\"x\\":{\\"numerator\\":%wu,\\"denominator\\":%wu},", numerator, denominator);\n'

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    a = ap.parse_args()
    src = a.source.read_text()
    if len(GRID.findall(src)) != 1 or src.count(DEN) != 1 or src.count(PRINT) != 1:
        raise SystemExit("producer source does not match expected patterns")
    out = GRID.sub(GRID_NEW, src, count=1).replace(DEN, DEN_NEW, 1).replace(PRINT, PRINT_NEW, 1)
    a.output.write_text(out)
    a.manifest.write_text(json.dumps({
        "schema": "riemann.x0018-w4-anchor-source-patch.v1",
        "agent": "claude-02",
        "source_sha256": hashlib.sha256(src.encode()).hexdigest(),
        "patched_sha256": hashlib.sha256(out.encode()).hexdigest(),
        "x_coordinate": {"numerator": 2, "denominator": 1},
        "u_coordinate": {"numerator": 4, "denominator": 1},
        "xbits": -1,
        "emitted_point_count": 1,
        "evaluation_code_untouched": True,
    }, indent=1) + "\n")
    print("patched ok")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
