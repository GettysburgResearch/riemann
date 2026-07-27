#!/usr/bin/env python3
"""Patch the reviewed producer to emit one dyadic point x = num * 2^-k (k>=0).

Agent: claude-02.  Generalizes the x=1/x=2 patchers: covers the remaining
rational-square ladder anchors x in {1/2, 3/2, 5/2, 3} exactly (all dyadic).
Evaluation code untouched; only the x-grid constant and the two JSON x-emission
lines change.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

GRID = re.compile(r"#define X_COUNT [0-9]+\nstatic const int X_BITS\[X_COUNT\] = \{[^\n]+\};\n")
SETX = "    arb_one(x);\n    arb_mul_2exp_si(x, x, -xbits);\n"
DEN = "    ulong denominator = UWORD(1) << xbits;\n"
PRINT = '    flint_printf("\\"x\\":{\\"numerator\\":1,\\"denominator\\":%wu},", denominator);\n'

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--x-num", type=int, required=True)
    ap.add_argument("--x-bits", type=int, required=True, help="x = num * 2^-bits, bits >= 0")
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    a = ap.parse_args()
    if a.x_bits < 0 or a.x_num <= 0:
        raise SystemExit("need num > 0 and bits >= 0")
    src = a.source.read_text()
    if len(GRID.findall(src)) != 1 or src.count(SETX) != 1 or src.count(DEN) != 1 or src.count(PRINT) != 1:
        raise SystemExit("producer source does not match expected patterns")
    out = GRID.sub(f"#define X_COUNT 1\nstatic const int X_BITS[X_COUNT] = {{{a.x_bits}}};\n#define X_NUM {a.x_num}\n", src, count=1)
    out = out.replace(SETX, f"    arb_set_ui(x, X_NUM);\n    arb_mul_2exp_si(x, x, -xbits);\n", 1)
    out = out.replace(PRINT, '    flint_printf("\\"x\\":{\\"numerator\\":%d,\\"denominator\\":%wu},", (int) X_NUM, denominator);\n', 1)
    a.output.write_text(out)
    from fractions import Fraction
    x = Fraction(a.x_num, 1 << a.x_bits)
    a.manifest.write_text(json.dumps({
        "schema": "riemann.x0019-ladder-source-patch.v1", "agent": "claude-02",
        "source_sha256": hashlib.sha256(src.encode()).hexdigest(),
        "patched_sha256": hashlib.sha256(out.encode()).hexdigest(),
        "x": {"numerator": x.numerator, "denominator": x.denominator},
        "w": {"numerator": (x*x).numerator, "denominator": (x*x).denominator},
        "evaluation_code_untouched": True}, indent=1) + "\n")
    print(f"patched x={x} (w={x*x})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
