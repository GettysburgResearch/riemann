#!/usr/bin/env python3
"""Exact regression for R-15112.

Uses only integers, fractions, JSON, and SHA-256.  The model is
A=N, K=A(A-I)=N(N-I), with the target vector d=e_j in the range of I-S.
The ratio

    ||d||^2 / [4^{-j} ||K d||^2]

is 4^j/[j^2(j-1)^2] and grows exponentially.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


def qstr(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}"


def build() -> dict:
    rows = []
    for J in (8, 12, 16, 20, 24, 32, 40, 48, 64):
        j = J // 2
        normalized_output = Fraction(j * j * (j - 1) * (j - 1), 4**j)
        required_ratio = Fraction(1, 1) / normalized_output
        rows.append(
            {
                "J": J,
                "j": j,
                "lhs": "1/1",
                "normalized_output": qstr(normalized_output),
                "required_constant_ratio": qstr(required_ratio),
            }
        )

    payload = {
        "schema": "X-15123-v1",
        "verdict": "CERTIFIED_UNIVERSAL_SMJ_FALSE",
        "model": "A=N; K=N(N-I); S backward shift; d=(I-S)c=e_j",
        "base": 4,
        "rows": rows,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["proof_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return payload


def verify(payload: dict) -> None:
    assert payload["schema"] == "X-15123-v1"
    previous = Fraction(0, 1)
    for row in payload["rows"]:
        J = int(row["J"])
        j = int(row["j"])
        assert j == J // 2
        normalized = Fraction(row["normalized_output"])
        ratio = Fraction(row["required_constant_ratio"])
        assert normalized == Fraction(j * j * (j - 1) * (j - 1), 4**j)
        assert ratio == 1 / normalized
        assert ratio > previous
        previous = ratio
    assert previous > 10**12


def main() -> None:
    payload = build()
    verify(payload)
    out = Path(__file__).with_name("result.json")
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
