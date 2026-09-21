#!/usr/bin/env python3
"""Exact verifier for the algebraic layer of a Weil Rayleigh certificate.

The verifier uses only Python integers and fractions.  It accepts a symmetric
matrix whose upper-triangular entries are dyadic intervals and a dyadic vector,
then computes an exact rational interval containing v^T Q v.  Exit status 0 is
returned only when the exact upper endpoint is strictly negative.

IMPORTANT: this verifier checks the interval arithmetic *after* matrix-entry
balls have been generated.  A complete RH counterexample also requires an
independently audited proof that those intervals enclose the precisely defined
cutoff-free Weil matrix D-0001.  See M-0001 and the experiment README.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.weil-rayleigh-dyadic.v1"


class CertificateError(ValueError):
    """Raised when the certificate is malformed or incomplete."""


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError(
                f"invalid interval [{self.lower}, {self.upper}]: lower > upper"
            )

    def __add__(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def scale(self, scalar: Fraction) -> "Interval":
        if scalar >= 0:
            return Interval(scalar * self.lower, scalar * self.upper)
        return Interval(scalar * self.upper, scalar * self.lower)


def _exact_int(value: Any, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer")
    return value


def dyadic(numerator: Any, scale_bits: Any, name: str) -> Fraction:
    n = _exact_int(numerator, f"{name}.numerator")
    bits = _exact_int(scale_bits, f"{name}.scale_bits")
    if bits < 0:
        raise CertificateError(f"{name}.scale_bits must be nonnegative")
    return Fraction(n, 1 << bits)


def parse_certificate(data: dict[str, Any]) -> tuple[list[list[Interval]], list[Fraction]]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")

    matrix = data.get("matrix")
    vector = data.get("vector")
    if not isinstance(matrix, dict) or not isinstance(vector, dict):
        raise CertificateError("matrix and vector objects are required")

    dimension = _exact_int(matrix.get("dimension"), "matrix.dimension")
    if dimension < 1:
        raise CertificateError("matrix.dimension must be positive")

    entries = matrix.get("entries_upper")
    if not isinstance(entries, list):
        raise CertificateError("matrix.entries_upper must be a list")

    table: dict[tuple[int, int], Interval] = {}
    for position, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise CertificateError(f"matrix.entries_upper[{position}] must be an object")
        i = _exact_int(entry.get("i"), f"entry[{position}].i")
        j = _exact_int(entry.get("j"), f"entry[{position}].j")
        if not (0 <= i <= j < dimension):
            raise CertificateError(
                f"entry[{position}] index must satisfy 0 <= i <= j < {dimension}"
            )
        key = (i, j)
        if key in table:
            raise CertificateError(f"duplicate matrix entry {key}")
        bits = _exact_int(entry.get("scale_bits"), f"entry[{position}].scale_bits")
        lo = dyadic(entry.get("lower_num"), bits, f"entry[{position}].lower")
        hi = dyadic(entry.get("upper_num"), bits, f"entry[{position}].upper")
        table[key] = Interval(lo, hi)

    expected = dimension * (dimension + 1) // 2
    if len(table) != expected:
        missing = [
            (i, j)
            for i in range(dimension)
            for j in range(i, dimension)
            if (i, j) not in table
        ]
        raise CertificateError(
            f"expected {expected} upper-triangular entries; missing {missing[:8]}"
        )

    vector_nums = vector.get("numerators")
    vector_bits = _exact_int(vector.get("scale_bits"), "vector.scale_bits")
    if not isinstance(vector_nums, list) or len(vector_nums) != dimension:
        raise CertificateError(
            f"vector.numerators must be a list of length {dimension}"
        )
    v = [
        dyadic(num, vector_bits, f"vector.numerators[{i}]")
        for i, num in enumerate(vector_nums)
    ]
    if all(x == 0 for x in v):
        raise CertificateError("the witness vector must be nonzero")

    Q = [[Interval(Fraction(0), Fraction(0)) for _ in range(dimension)] for _ in range(dimension)]
    for (i, j), interval in table.items():
        Q[i][j] = interval
        Q[j][i] = interval
    return Q, v


def rayleigh_interval(Q: list[list[Interval]], v: list[Fraction]) -> Interval:
    dimension = len(v)
    total = Interval(Fraction(0), Fraction(0))
    for i in range(dimension):
        total = total + Q[i][i].scale(v[i] * v[i])
        for j in range(i + 1, dimension):
            total = total + Q[i][j].scale(2 * v[i] * v[j])
    return total


def fraction_json(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def verify(data: dict[str, Any]) -> dict[str, Any]:
    Q, v = parse_certificate(data)
    enclosure = rayleigh_interval(Q, v)
    certified_negative = enclosure.upper < 0
    return {
        "schema": SCHEMA,
        "certified_negative": certified_negative,
        "rayleigh_interval": {
            "lower": fraction_json(enclosure.lower),
            "upper": fraction_json(enclosure.upper),
        },
        "interpretation": (
            "The supplied entry intervals imply v^T Q v < 0 exactly."
            if certified_negative
            else "The supplied entry intervals do not prove v^T Q v < 0."
        ),
        "scope_warning": (
            "This verifies exact dyadic interval propagation only; analytic enclosure "
            "of the cutoff-free Weil matrix must be independently established."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level JSON must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["certified_negative"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
