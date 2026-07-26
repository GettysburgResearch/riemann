#!/usr/bin/env python3
"""Patch a generated direct-xi C producer to emit only the exact anchor x=0."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

GRID_PATTERN = re.compile(
    r"#define X_COUNT [0-9]+\n"
    r"static const int X_BITS\[X_COUNT\] = \{[^\n]+\};\n"
)
GRID_REPLACEMENT = (
    "#define X_COUNT 1\n"
    "static const int X_BITS[X_COUNT] = {-1};\n"
)

SET_X_NEEDLE = """    arb_one(x);
    arb_mul_2exp_si(x, x, -xbits);
"""
SET_X_REPLACEMENT = """    if (xbits < 0)
    {
        arb_zero(x);
    }
    else
    {
        arb_one(x);
        arb_mul_2exp_si(x, x, -xbits);
    }
"""

DENOMINATOR_NEEDLE = "    ulong denominator = UWORD(1) << xbits;\n"
DENOMINATOR_REPLACEMENT = (
    "    ulong denominator = xbits < 0 ? UWORD(1) : (UWORD(1) << xbits);\n"
)

PRINT_NEEDLE = """    flint_printf("{\\\"id\\\":\\\"x-%d\\\",", xbits);
    flint_printf("\\\"x\\\":{\\\"numerator\\\":1,\\\"denominator\\\":%wu},", denominator);
"""
PRINT_REPLACEMENT = """    if (xbits < 0)
    {
        flint_printf("{\\\"id\\\":\\\"x-critical-line\\\",");
        flint_printf("\\\"x\\\":{\\\"numerator\\\":0,\\\"denominator\\\":1},");
    }
    else
    {
        flint_printf("{\\\"id\\\":\\\"x-%d\\\",", xbits);
        flint_printf("\\\"x\\\":{\\\"numerator\\\":1,\\\"denominator\\\":%wu},", denominator);
    }
"""


def replace_once(source: str, needle: str, replacement: str, name: str) -> str:
    count = source.count(needle)
    if count != 1:
        raise ValueError(f"expected one {name} patch target, found {count}")
    output = source.replace(needle, replacement)
    if output.replace(replacement, needle) != source:
        raise ValueError(f"{name} patch changed unexpected text")
    return output


def patch(source: str) -> tuple[str, dict[str, object]]:
    matches = list(GRID_PATTERN.finditer(source))
    if len(matches) != 1:
        raise ValueError(f"expected one x-grid declaration, found {len(matches)}")
    output = GRID_PATTERN.sub(GRID_REPLACEMENT, source, count=1)
    output = replace_once(output, SET_X_NEEDLE, SET_X_REPLACEMENT, "zero-coordinate")
    output = replace_once(
        output,
        DENOMINATOR_NEEDLE,
        DENOMINATOR_REPLACEMENT,
        "sentinel denominator",
    )
    output = replace_once(output, PRINT_NEEDLE, PRINT_REPLACEMENT, "zero-point JSON")
    manifest = {
        "schema": "riemann.x9309-zero-anchor-source-patch.v1",
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "patched_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
        "x_coordinate": {"numerator": 0, "denominator": 1},
        "u_coordinate": {"numerator": 0, "denominator": 1},
        "sentinel_xbits": -1,
        "emitted_point_count": 1,
    }
    return output, manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()

    source = args.source.read_text(encoding="utf-8")
    output, manifest = patch(source)
    args.output.write_text(output, encoding="utf-8")
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
