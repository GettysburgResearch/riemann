#!/usr/bin/env python3
"""Verify retained interval nesting, strict negativity, and source bindings."""

from __future__ import annotations

from decimal import Decimal, getcontext
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
getcontext().prec = 220

PATTERN = re.compile(r"A63_(lo|hi)=([^\n]+)")


def parse(path: Path) -> tuple[Decimal, Decimal, str]:
    text = path.read_text()
    vals = {k: Decimal(v.strip()) for k, v in PATTERN.findall(text)}
    if set(vals) != {"lo", "hi"}:
        raise AssertionError(f"missing interval fields in {path}")
    if "CERTIFIED_NEGATIVE=YES" not in text:
        raise AssertionError(f"missing verdict in {path}")
    return vals["lo"], vals["hi"], text


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def proof_object() -> dict:
    lo256, hi256, _ = parse(ROOT / "results" / "certificate-256.txt")
    lo512, hi512, _ = parse(ROOT / "results" / "certificate-512.txt")
    assert lo256 <= lo512 <= hi512 <= hi256
    assert hi256 < 0 and hi512 < 0
    assert lo256 <= hi256 and lo512 <= hi512
    obj = {
        "schema": "riemann.x27202.ternary-negative.v1",
        "X": 10_000_000,
        "n": 63,
        "y_max": 158_730,
        "nonzero_path_differences": 484_235,
        "maximum_path_count": 14_387,
        "precision_bits": [256, 512],
        "interval_256": [str(lo256), str(hi256)],
        "interval_512": [str(lo512), str(hi512)],
        "strictly_negative": True,
        "nested": True,
        "source_sha256": sha256(ROOT / "certify.c"),
        "certificate_256_sha256": sha256(ROOT / "results" / "certificate-256.txt"),
        "certificate_512_sha256": sha256(ROOT / "results" / "certificate-512.txt"),
        "classification": "CERTIFIED_COUNTEREXAMPLE_TO_PURE_TERNARY_FRAGMENTATION_POSITIVITY",
        "scope": (
            "Refutes TFP only. Does not refute MFT, Pascal-cycle repairs, "
            "subpower negative-part variants, or RH."
        ),
    }
    return obj


def main() -> None:
    obj = proof_object()
    out = ROOT / "results" / "verification.json"
    out.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    print(json.dumps(obj, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
