#!/usr/bin/env python3
"""Exact interval combiner for one square-cutoff screw certificate.

This verifier does not generate transcendental intervals or prove manifest
completeness. It fail-closes unless those producer gates are explicitly bound,
then checks the final scalar interval using Fraction arithmetic only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.square-screw-level.v1"
COMPLETE = "EXTERNALLY_CERTIFIED_COMPLETE"
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def _fraction(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise ValueError(f"{name}: booleans are not rationals")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(f"{name}: invalid rational") from exc
    raise ValueError(f"{name}: expected integer or rational string")


def _interval(obj: Any, name: str, *, nonnegative: bool = False) -> tuple[Fraction, Fraction]:
    if not isinstance(obj, dict) or set(obj) != {"lower", "upper"}:
        raise ValueError(f"{name}: expected exactly lower/upper")
    lo = _fraction(obj["lower"], f"{name}.lower")
    hi = _fraction(obj["upper"], f"{name}.upper")
    if lo > hi:
        raise ValueError(f"{name}: reversed interval")
    if nonnegative and lo < 0:
        raise ValueError(f"{name}: negative lower endpoint")
    return lo, hi


def _fmt(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def _canonical_digest(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def verify(cert: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(cert, dict):
        raise ValueError("certificate must be an object")
    if cert.get("schema") != SCHEMA:
        raise ValueError("unsupported schema")

    n_raw = cert.get("N")
    if isinstance(n_raw, bool) or not isinstance(n_raw, int) or n_raw < 1:
        raise ValueError("N must be a positive integer")
    N = n_raw
    cutoff = N * N

    manifest = cert.get("manifest")
    if not isinstance(manifest, dict):
        raise ValueError("manifest must be an object")
    required_manifest = {"cutoff", "entry_count", "completeness", "sha256"}
    if set(manifest) != required_manifest:
        raise ValueError("manifest fields do not match schema")
    if manifest["cutoff"] != cutoff:
        raise ValueError("manifest cutoff must equal N^2")
    if manifest["completeness"] != COMPLETE:
        raise ValueError("manifest completeness gate is not certified")
    if isinstance(manifest["entry_count"], bool) or not isinstance(manifest["entry_count"], int):
        raise ValueError("manifest entry_count must be an integer")
    if not isinstance(manifest["sha256"], str) or not HEX64.fullmatch(manifest["sha256"]):
        raise ValueError("manifest sha256 must be lowercase hexadecimal")

    terms = cert.get("prime_terms")
    if not isinstance(terms, list):
        raise ValueError("prime_terms must be a list")
    if len(terms) != manifest["entry_count"]:
        raise ValueError("manifest entry_count mismatch")
    seen: set[int] = set()
    prior = 1
    prime_lo = Fraction(0)
    prime_hi = Fraction(0)
    normalized_terms: list[dict[str, Any]] = []
    for idx, term in enumerate(terms):
        if not isinstance(term, dict) or set(term) != {"n", "lower", "upper"}:
            raise ValueError(f"prime_terms[{idx}]: invalid fields")
        m = term["n"]
        if isinstance(m, bool) or not isinstance(m, int) or not (2 <= m <= cutoff):
            raise ValueError(f"prime_terms[{idx}].n: outside cutoff")
        if m in seen:
            raise ValueError("duplicate prime-power index")
        if m <= prior:
            raise ValueError("prime_terms must be strictly increasing")
        seen.add(m)
        prior = m
        lo, hi = _interval(
            {"lower": term["lower"], "upper": term["upper"]},
            f"prime_terms[{idx}]",
            nonnegative=True,
        )
        prime_lo += lo
        prime_hi += hi
        normalized_terms.append({"n": m, "lower": _fmt(lo), "upper": _fmt(hi)})

    linear_lo, linear_hi = _interval(cert.get("linear_term"), "linear_term")
    lerch_lo, lerch_hi = _interval(cert.get("lerch_term"), "lerch_term")

    elementary = Fraction(4) * (Fraction(N) + Fraction(1, N) - 2)
    total_lo = elementary - prime_hi + linear_lo + lerch_lo
    total_hi = elementary - prime_lo + linear_hi + lerch_hi

    claimed = cert.get("claimed_total")
    if claimed is not None:
        claim_lo, claim_hi = _interval(claimed, "claimed_total")
        if claim_lo != total_lo or claim_hi != total_hi:
            raise ValueError("claimed_total is not the exact combined interval")

    if total_lo >= 0:
        verdict = "CERTIFIED_NONNEGATIVE_SQUARE_LEVEL"
    elif total_hi < 0:
        verdict = "CERTIFIED_NEGATIVE_RH_VIOLATION"
    else:
        verdict = "UNRESOLVED_SQUARE_LEVEL"

    proof_payload = {
        "schema": SCHEMA,
        "N": N,
        "cutoff": cutoff,
        "manifest_sha256": manifest["sha256"],
        "prime_terms": normalized_terms,
        "elementary_term": _fmt(elementary),
        "prime_sum": [_fmt(prime_lo), _fmt(prime_hi)],
        "linear_term": [_fmt(linear_lo), _fmt(linear_hi)],
        "lerch_term": [_fmt(lerch_lo), _fmt(lerch_hi)],
        "total": [_fmt(total_lo), _fmt(total_hi)],
        "verdict": verdict,
    }
    return {
        **proof_payload,
        "proof_object_sha256": _canonical_digest(proof_payload),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    cert = json.loads(args.certificate.read_text(encoding="utf-8"))
    print(json.dumps(verify(cert), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
