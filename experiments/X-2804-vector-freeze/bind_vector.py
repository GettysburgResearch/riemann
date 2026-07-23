#!/usr/bin/env python3
"""Bind an X-2804 dyadic vector to the exact checker-compatible digest."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def canonical_sha(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def bind(data: dict[str, Any]) -> dict[str, Any]:
    raw = data.get("dyadic_vector")
    if not isinstance(raw, dict):
        raise ValueError("dyadic_vector missing")
    bits = raw.get("scale_bits")
    real = raw.get("real_numerators")
    imag = raw.get("imag_numerators")
    if (
        isinstance(bits, bool)
        or not isinstance(bits, int)
        or bits < 0
        or not isinstance(real, list)
        or not isinstance(imag, list)
        or len(real) != len(imag)
        or not real
        or any(isinstance(x, bool) or not isinstance(x, int) for x in real + imag)
    ):
        raise ValueError("malformed dyadic vector")
    canonical_vector = {
        "imag_numerators": imag,
        "real_numerators": real,
        "scale_bits": bits,
    }
    out = dict(data)
    out["vector_sha256"] = canonical_sha(canonical_vector)
    artifact_without_digest = dict(out)
    artifact_without_digest.pop("artifact_sha256", None)
    out["artifact_sha256"] = canonical_sha(artifact_without_digest)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vector", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.vector.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("vector file must contain a JSON object")
    args.output.write_text(
        json.dumps(bind(data), indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
