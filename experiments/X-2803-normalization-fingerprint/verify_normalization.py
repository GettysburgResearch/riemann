#!/usr/bin/env python3
"""Fail-closed normalization fingerprint for T-2801 / D-0801."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.d0801-normalization.v1"
EXPECTED = {
    "schema": SCHEMA,
    "fourier": {
        "forward": "integral g(t)*exp(-2*pi*i*t*xi) dt",
        "inverse": "integral hat_g(xi)*exp(+2*pi*i*z*xi) dxi",
    },
    "zero_coordinate": "(rho-1/2)/i",
    "prime": {
        "frequency": "log(q)/(2*pi)",
        "coefficient": "-Lambda(q)/(pi*sqrt(q))",
        "support_rule": "q<=c; endpoint q=c has zero autocorrelation",
    },
    "pole": "+2*g(i/2)",
    "archimedean": "+integral (Re(digamma(1/4+i*t/2))-log(pi))*g(t) dt/(2*pi)",
    "normalized_assembly": "A+R-h*S_K",
    "rh_coordinate_rule": "RH implies every zero coordinate is real",
}


class FingerprintError(ValueError):
    pass


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def verify(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise FingerprintError("top-level JSON must be an object")
    if value != EXPECTED:
        for key in EXPECTED:
            if value.get(key) != EXPECTED[key]:
                raise FingerprintError(f"normalization mismatch at {key}")
        extras = sorted(set(value) - set(EXPECTED))
        raise FingerprintError(f"unexpected normalization fields: {extras}")
    digest = hashlib.sha256(canonical_bytes(value)).hexdigest()
    return {
        "schema": SCHEMA,
        "verified": True,
        "canonical_sha256": digest,
        "exact_assembly": "zero_sum = A + R - h*S_K",
        "scope": "Integrity binding for T-2801; analytic truth still requires proof review.",
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fingerprint", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        value = json.loads(args.fingerprint.read_text(encoding="utf-8"))
        result = verify(value)
    except (OSError, json.JSONDecodeError, FingerprintError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2))
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
