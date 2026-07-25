#!/usr/bin/env python3
"""Generate the PR #71 exact-ordinate direct-xi C producer from X-7501."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

OLD = "20225875608343121406355"
NEW = "20225875608341108140435"
EXPECTED_OCCURRENCES = 3


def patch_source(source: str) -> tuple[str, dict[str, object]]:
    count = source.count(OLD)
    if count != EXPECTED_OCCURRENCES:
        raise ValueError(
            f"expected {EXPECTED_OCCURRENCES} exact ordinate occurrences, found {count}"
        )
    if NEW in source:
        raise ValueError("PR #71 ordinate already present in source")
    output = source.replace(OLD, NEW)
    if output.replace(NEW, OLD) != source:
        raise ValueError("source patch changed more than the exact ordinate")
    return output, {
        "old_ordinate_numerator": OLD,
        "new_ordinate_numerator": NEW,
        "denominator": 1 << 32,
        "occurrences_replaced": count,
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "patched_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "X-7501-xi-modulus"
        / "rs_modulus.c",
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    source = args.source.read_text(encoding="utf-8")
    output, manifest = patch_source(source)
    args.output.write_text(output, encoding="utf-8")
    if args.manifest:
        args.manifest.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
