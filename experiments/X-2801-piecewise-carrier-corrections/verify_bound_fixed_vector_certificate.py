#!/usr/bin/env python3
"""Normalization-bound wrapper for the exact L-2804 fixed-vector checker."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any, Sequence

from verify_fixed_vector_certificate import CertificateError, verify as verify_numeric

NORMALIZATION_SHA256 = "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("normalization_sha256") != NORMALIZATION_SHA256:
        raise CertificateError(
            "normalization_sha256 must equal the canonical T-2801 fingerprint"
        )
    result = verify_numeric(data)
    result["normalization_sha256"] = NORMALIZATION_SHA256
    result["logical_gate"] = (
        "Quantitative certificate is bound to T-2801 / "
        "riemann.d0801-normalization.v1. Independent theorem review remains required."
    )
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level JSON must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["certified_positive"] or result["certified_negative"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
