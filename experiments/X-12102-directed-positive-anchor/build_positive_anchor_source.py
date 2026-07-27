#!/usr/bin/env python3
"""Patch a generated direct-xi C producer to emit only x=1, hence u=1."""
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
    "static const int X_BITS[X_COUNT] = {0};\n"
)


def patch(source: str) -> tuple[str, dict[str, object]]:
    matches = list(GRID_PATTERN.finditer(source))
    if len(matches) != 1:
        raise ValueError(
            f"expected one x-grid declaration, found {len(matches)}"
        )
    output = GRID_PATTERN.sub(GRID_REPLACEMENT, source, count=1)
    if output.replace(GRID_REPLACEMENT, matches[0].group(0)) != source:
        raise ValueError("x=1 patch changed unexpected text")
    manifest = {
        "schema": "riemann.x12102-positive-anchor-source-patch.v1",
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "patched_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
        "x_coordinate": {"numerator": 1, "denominator": 1},
        "u_coordinate": {"numerator": 1, "denominator": 1},
        "xbits": 0,
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
