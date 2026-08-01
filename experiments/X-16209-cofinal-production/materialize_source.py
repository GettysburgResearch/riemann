#!/usr/bin/env python3
"""Reassemble the immutable gamma=32768 DIRECTED_INTERVAL_ODE primitive."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def materialize(output: Path) -> str:
    manifest = json.loads((HERE / "source-gzip-parts/manifest.json").read_text())
    chunks: list[bytes] = []
    for item in manifest["parts"]:
        data = (HERE / item["path"]).read_bytes()
        if len(data) != item["bytes"] or sha(data) != item["sha256"]:
            raise ValueError(f"source gzip chunk mismatch: {item['path']}")
        chunks.append(data)
    compressed = b"".join(chunks)
    if sha(compressed) != manifest["gzip_sha256"]:
        raise ValueError("combined gzip SHA-256 mismatch")
    payload = gzip.decompress(compressed)
    if sha(payload) != manifest["raw_sha256"]:
        raise ValueError("decompressed source SHA-256 mismatch")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(payload)
    return manifest["raw_sha256"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=Path("/tmp/source-gamma32768.json"))
    args = ap.parse_args()
    print(json.dumps({"output": str(args.output), "sha256": materialize(args.output)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
