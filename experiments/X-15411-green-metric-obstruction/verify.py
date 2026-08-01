#!/usr/bin/env python3
"""Exact checker for the Green quotient versus physical metric obstruction."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15411-green-metric-obstruction.synthetic.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def frac(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    n = integer(value.get("numerator"), f"{name}.numerator")
    d = integer(value.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def fj(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty matrix")
    out = []
    width = None
    for i, row in enumerate(raw):
        if not isinstance(row, list) or not row:
            raise CertificateError(f"{name}[{i}] must be a nonempty row")
        parsed = [frac(v, f"{name}[{i}][{j}]") for j, v in enumerate(row)]
        if width is None:
            width = len(parsed)
        elif len(parsed) != width:
            raise CertificateError(f"{name} rows must have equal length")
        out.append(parsed)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    if len(a[0]) != len(b):
        raise CertificateError("matrix shape mismatch")
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def diag(entries):
    return [[entries[i] if i == j else Fraction(0)
             for j in range(len(entries))] for i in range(len(entries))]


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    c = matrix(data.get("C"), "C")
    e = matrix(data.get("E"), "E")
    k = matrix(data.get("K"), "K")
    if len(c) != 2 or len(c[0]) != 2 or len(e) != 2 or len(e[0]) != 2:
        raise CertificateError("control matrices must be 2 by 2")
    identity = diag([Fraction(1), Fraction(1)])
    if matmul(c, e) != identity:
        raise CertificateError("C E must equal I")
    if matmul(transpose(k), k) != identity:
        raise CertificateError("K must be unitary")
    t = matmul(matmul(c, k), e)
    tstar_t = matmul(transpose(t), t)
    expected_t = matrix(data.get("claimed_T"), "claimed_T")
    expected_tstar_t = matrix(data.get("claimed_TstarT"), "claimed_TstarT")
    if t != expected_t or tstar_t != expected_tstar_t:
        raise CertificateError("claimed physical matrices mismatch")
    physical_norm_squared = max(tstar_t[0][0], tstar_t[1][1])
    if frac(data.get("claimed_physical_norm_squared"), "claimed norm") != physical_norm_squared:
        raise CertificateError("claimed physical norm mismatch")
    if physical_norm_squared <= 1:
        raise CertificateError("control does not expand the physical metric")

    quotient_gram = matmul(transpose(e), e)
    lhs = matmul(matmul(transpose(t), quotient_gram), t)
    if lhs != quotient_gram:
        raise CertificateError("T is not an exact quotient isometry")
    claimed_q = matrix(data.get("claimed_quotient_gram"), "claimed_quotient_gram")
    if claimed_q != quotient_gram:
        raise CertificateError("claimed quotient Gram mismatch")

    return {
        "schema": SCHEMA,
        "status": "EXACT_GREEN_METRIC_SIMILARITY_OBSTRUCTION",
        "T": [[fj(x) for x in row] for row in t],
        "TstarT_physical": [[fj(x) for x in row] for row in tstar_t],
        "physical_norm_squared": fj(physical_norm_squared),
        "quotient_gram": [[fj(x) for x in row] for row in quotient_gram],
        "quotient_isometry": True,
        "proof_boundary": (
            "exact rational similarity counterexample only; a source-specific "
            "physical Green identity may still hold"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(f"ERROR: {exc}")
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
