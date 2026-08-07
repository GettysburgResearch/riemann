#!/usr/bin/env python3
"""Exact checker for the regular endpoint/tail Gram correction."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15413-regular-endpoint-tail.synthetic.v1"


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


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def matrix_entries(f, x: Fraction, y: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    return f(x), f((x + y) / 2), f(y)


def determinant(entries: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    a, b, c = entries
    return a * c - b * b


def supplied_entries(raw: Any, name: str) -> tuple[Fraction, Fraction, Fraction]:
    if not isinstance(raw, list) or len(raw) != 3:
        raise CertificateError(f"{name} must contain three entries")
    return tuple(frac(value, f"{name}[{i}]") for i, value in enumerate(raw))  # type: ignore[return-value]


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    nodes = data.get("nodes")
    claimed = data.get("claimed")
    if not isinstance(nodes, dict) or not isinstance(claimed, dict):
        raise CertificateError("nodes and claimed must be objects")
    x = frac(nodes.get("x"), "nodes.x")
    y = frac(nodes.get("y"), "nodes.y")
    if not Fraction(0) < x < y:
        raise CertificateError("nodes must satisfy 0 < x < y")
    midpoint = (x + y) / 2
    if frac(claimed.get("midpoint"), "claimed.midpoint") != midpoint:
        raise CertificateError("claimed midpoint mismatch")

    raw = lambda q: q / (q + 1)
    endpoint = lambda q: 1 / (q + 1)
    one_green = endpoint
    total = lambda q: Fraction(1)
    anchored_cross = lambda q: endpoint(q) - 1

    actual = {
        "raw_entries": matrix_entries(raw, x, y),
        "endpoint_entries": matrix_entries(endpoint, x, y),
        "one_green_entries": matrix_entries(one_green, x, y),
        "total_entries": matrix_entries(total, x, y),
        "anchored_cross_entries": matrix_entries(anchored_cross, x, y),
    }
    for name, entries in actual.items():
        if supplied_entries(claimed.get(name), f"claimed.{name}") != entries:
            raise CertificateError(f"claimed {name} mismatch")

    raw_det = determinant(actual["raw_entries"])
    endpoint_det = determinant(actual["endpoint_entries"])
    green_det = determinant(actual["one_green_entries"])
    if raw_det >= 0:
        raise CertificateError("raw-tail determinant must be negative")
    if endpoint_det <= 0 or green_det <= 0:
        raise CertificateError("endpoint and one-Green determinants must be positive")
    if frac(claimed.get("raw_determinant"), "claimed.raw_determinant") != raw_det:
        raise CertificateError("claimed raw determinant mismatch")
    if frac(claimed.get("endpoint_determinant"), "claimed.endpoint_determinant") != endpoint_det:
        raise CertificateError("claimed endpoint determinant mismatch")
    if frac(claimed.get("one_green_determinant"), "claimed.one_green_determinant") != green_det:
        raise CertificateError("claimed one-Green determinant mismatch")

    for r, e, t, c in zip(
        actual["raw_entries"], actual["endpoint_entries"],
        actual["total_entries"], actual["anchored_cross_entries"]
    ):
        if r + e != t:
            raise CertificateError("endpoint plus raw tail must equal total")
        if c + r != 0:
            raise CertificateError("anchored endpoint cross must cancel raw tail")

    return {
        "schema": SCHEMA,
        "status": "EXACT_REGULAR_ENDPOINT_TAIL_CORRECTION",
        "nodes": {"x": fj(x), "y": fj(y), "midpoint": fj(midpoint)},
        "raw": {"entries": [fj(v) for v in actual["raw_entries"]], "determinant": fj(raw_det)},
        "endpoint": {"entries": [fj(v) for v in actual["endpoint_entries"]], "determinant": fj(endpoint_det)},
        "one_green": {"entries": [fj(v) for v in actual["one_green_entries"]], "determinant": fj(green_det)},
        "total": {"entries": [fj(v) for v in actual["total_entries"]]},
        "anchored_cross": {"entries": [fj(v) for v in actual["anchored_cross_entries"]]},
        "proof_boundary": "exact rational model only; the zeta-specific smoothed Jordan derivative inequality remains open",
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
