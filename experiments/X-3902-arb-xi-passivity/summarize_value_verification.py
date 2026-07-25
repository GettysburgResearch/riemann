#!/usr/bin/env python3
"""Create a compact exact summary of a value-ball verification JSON."""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


def fraction(value: dict[str, str]) -> Fraction:
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("verification", type=Path)
    parser.add_argument("--certificate", type=Path)
    parser.add_argument("--time-file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    data = json.loads(args.verification.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not data.get("verified"):
        raise ValueError("verification is absent or rejected")
    channels = data.get("channels")
    if not isinstance(channels, list):
        raise ValueError("channels missing")

    counts = Counter()
    tight: dict[str, tuple[Fraction, dict[str, Any]]] = {}
    for channel in channels:
        kind = str(channel["kind"])
        status = str(channel["status"])
        counts[(kind, status)] += 1
        interval = channel["interval"]
        upper = fraction(interval["upper"])
        current = tight.get(kind)
        if current is None or upper < current[0]:
            tight[kind] = (upper, channel)

    file_hashes = {args.verification.name: sha256(args.verification)}
    if args.certificate:
        file_hashes[args.certificate.name] = sha256(args.certificate)
    if args.time_file:
        file_hashes[args.time_file.name] = sha256(args.time_file)

    summary: dict[str, Any] = {
        "schema": "riemann.xi-passivity.value-grid-summary.v1",
        "status": data["status"],
        "verified": True,
        "point_count": data["point_count"],
        "channel_count": data["channel_count"],
        "negative_channels": data["negative_channels"],
        "unresolved_channels": data["unresolved_channels"],
        "counts": [
            {"kind": kind, "status": status, "count": count}
            for (kind, status), count in sorted(counts.items())
        ],
        "tightest_upper_by_kind": {
            kind: {
                "id": channel["id"],
                "status": channel["status"],
                "interval": channel["interval"],
                "upper_orientation_decimal": format(float(upper), ".17g"),
            }
            for kind, (upper, channel) in sorted(tight.items())
        },
        "verification_sha256": data.get("verification_sha256"),
        "file_sha256": file_hashes,
        "proof_boundary": (
            "This compact summary is derived from the exact checker output. The full "
            "primitive rectangles and all reconstructed channels remain in the workflow "
            "artifact and must be regenerated for independent acceptance."
        ),
    }
    args.output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
