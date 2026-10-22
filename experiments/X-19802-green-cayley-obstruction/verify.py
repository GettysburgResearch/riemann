#!/usr/bin/env python3
"""Exact Fraction-only verifier for R-19803."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent


def rat(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("booleans are not rationals")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"unsupported rational: {value!r}")


def dot(a: list[Fraction], b: list[Fraction]) -> Fraction:
    if len(a) != len(b):
        raise ValueError("dimension mismatch")
    return sum((x * y for x, y in zip(a, b)), Fraction())


def mat_vec(a: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    if any(len(row) != len(x) for row in a):
        raise ValueError("matrix dimension mismatch")
    return [dot(row, x) for row in a]


def quad(a: list[list[Fraction]], x: list[Fraction], y: list[Fraction]) -> Fraction:
    return dot(x, mat_vec(a, y))


def verify(data: dict[str, Any]) -> dict[str, Any]:
    c = [rat(x) for x in data["C"]]
    k = [rat(x) for x in data["K_diagonal"]]
    if len(c) != 2 or len(k) != 2:
        raise ValueError("control is exactly two-dimensional")
    if any(abs(x) > 1 for x in k):
        raise ValueError("K is not pointwise contractive")

    ck = [ci * ki for ci, ki in zip(c, k)]
    q = [
        [c[i] * c[j] - ck[i] * ck[j] for j in range(2)]
        for i in range(2)
    ]

    expected_q = [[rat(x) for x in row] for row in data["expected_Q"]]
    if q != expected_q:
        raise ValueError("Q matrix mismatch")

    n = [Fraction(1), Fraction(0)]
    trace_zero_floor = quad(q, n, n)
    if trace_zero_floor <= 0:
        raise ValueError("trace-zero fiber is not positive")

    z = [rat(x) for x in data["green_trace_one"]]
    if z[1] != 1:
        raise ValueError("Green vector must have trace one")
    if quad(q, z, n) != 0:
        raise ValueError("Green Euler stationarity fails")

    plus = dot(c, z)
    minus = dot(ck, z)
    if plus == 0:
        raise ValueError("observed plus coordinate vanishes")
    cke = minus / plus

    expected_cke = rat(data["expected_CKE"])
    if cke != expected_cke:
        raise ValueError("CKE mismatch")
    if abs(cke) <= 1:
        raise ValueError("control does not refute contraction")

    r = [rat(x) for x in data["raw_coordinates"]]
    for ki, ri in zip(k, r):
        if (1 - ri) / (1 + ri) != ki:
            raise ValueError("K entry is not the declared Cayley value")
        if ri < 0:
            raise ValueError("raw Volterra coordinate must be nonnegative")

    canonical = {
        "C": [str(x) for x in c],
        "K_diagonal": [str(x) for x in k],
        "Q": [[str(x) for x in row] for row in q],
        "trace_zero_floor": str(trace_zero_floor),
        "green_trace_one": [str(x) for x in z],
        "green_euler_residual": str(quad(q, z, n)),
        "observed_plus": str(plus),
        "observed_minus": str(minus),
        "CKE": str(cke),
        "K_operator_norm": str(max(abs(x) for x in k)),
        "raw_coordinates": [str(x) for x in r],
        "verdict": "GREEN_STATIONARITY_DOES_NOT_IMPLY_CKE_CONTRACTION",
    }
    payload = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    canonical["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    return canonical


def main() -> None:
    cert = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "certificates" / "synthetic.json"
    result = verify(json.loads(cert.read_text()))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
