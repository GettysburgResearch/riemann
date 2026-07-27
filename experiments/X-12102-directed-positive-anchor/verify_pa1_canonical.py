#!/usr/bin/env python3
"""Canonical X-13202 wrapper around the legacy-path PA-1 verifier."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any

import verify_pa1 as legacy

SCHEMA = "riemann.x13202-directed-positive-anchor-pa1.v1"


def canonical_sha(data: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            data,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        ).encode("ascii")
    ).hexdigest()


def verify(
    old_certificate: Path,
    old_basis: Path,
    anchor_low: Path,
    anchor_high: Path,
    log_terms: int,
    delta: Fraction,
) -> dict[str, Any]:
    result = legacy.verify(
        old_certificate,
        old_basis,
        anchor_low,
        anchor_high,
        log_terms,
        delta,
    )
    result["legacy_schema"] = result.get("schema")
    result["schema"] = SCHEMA
    result["experiment_id"] = "X-13202"
    result["analytic_claim"] = "L-13201"
    result["canonical_id_migration"] = {
        "legacy_path": "experiments/X-12102-directed-positive-anchor/",
        "temporary_claim": "L-12101",
        "canonical_claim": "L-13201",
    }
    result.pop("canonical_result_sha256", None)
    result["canonical_result_sha256"] = canonical_sha(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-certificate", type=Path, required=True)
    parser.add_argument("--old-basis", type=Path, required=True)
    parser.add_argument("--anchor-low", type=Path, required=True)
    parser.add_argument("--anchor-high", type=Path, required=True)
    parser.add_argument("--log-terms", type=int, default=240)
    parser.add_argument(
        "--delta", type=Fraction, default=Fraction(1, 1_000_000)
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(
            args.old_certificate,
            args.old_basis,
            args.anchor_low,
            args.anchor_high,
            args.log_terms,
            args.delta,
        )
        code = 1 if result["verdict"].startswith("CERTIFIED_NEGATIVE") else 0
    except (
        OSError,
        json.JSONDecodeError,
        legacy.CertificateError,
    ) as exc:
        result = {
            "schema": SCHEMA,
            "classification": "REJECTED",
            "reason": str(exc),
        }
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
