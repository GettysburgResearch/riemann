#!/usr/bin/env python3
"""Exact checker for the simplicial L-9309 portfolio basis."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x9307-simplicial-portfolio-basis.v1"


class CertificateError(ValueError):
    pass


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def scale(self, scalar: Fraction) -> "Interval":
        if scalar >= 0:
            return Interval(self.lower * scalar, self.upper * scalar)
        return Interval(self.upper * scalar, self.lower * scalar)


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Interval(
        rational(raw.get("lower"), f"{name}.lower"),
        rational(raw.get("upper"), f"{name}.upper"),
    )


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def ij(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fj(value.lower), "upper": fj(value.upper)}


def canonical_sha(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def polynomial_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        output[index] += value
    for index, value in enumerate(right):
        output[index] += value
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def polynomial_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] += x * y
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def response_polynomial(nodes: list[Fraction], beta: list[Fraction]) -> list[Fraction]:
    output = [Fraction(0)]
    for i, coefficient in enumerate(beta):
        term = [Fraction(1)]
        for j, node in enumerate(nodes):
            if i != j:
                term = polynomial_multiply(term, [node, Fraction(1)])
        output = polynomial_add(output, [-coefficient * value for value in term])
    return output


def basis_vector(nodes: list[Fraction], degree: int) -> list[Fraction]:
    output: list[Fraction] = []
    for i, node in enumerate(nodes):
        denominator = Fraction(1)
        for j, other in enumerate(nodes):
            if i != j:
                denominator *= other - node
        output.append(-((-node) ** degree) / denominator)
    return output


def status(value: Interval) -> str:
    if value.upper < 0:
        return "CERTIFIED_NEGATIVE"
    if value.lower >= 0:
        return "CERTIFIED_NONNEGATIVE"
    return "UNRESOLVED"


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    classification = data.get("classification")
    if classification not in ("SYNTHETIC_MODEL", "RIEMANN_XI_DIRECTED"):
        raise CertificateError("unsupported classification")

    raw_nodes = data.get("nodes")
    raw_features = data.get("feature_intervals")
    if not isinstance(raw_nodes, list) or len(raw_nodes) < 2:
        raise CertificateError("nodes must contain at least two entries")
    if not isinstance(raw_features, list) or len(raw_features) != len(raw_nodes):
        raise CertificateError("feature interval count must equal node count")

    nodes = [rational(raw, f"nodes[{index}]") for index, raw in enumerate(raw_nodes)]
    if any(value <= 0 for value in nodes):
        raise CertificateError("all nodes must be positive")
    if any(nodes[index] >= nodes[index + 1] for index in range(len(nodes) - 1)):
        raise CertificateError("nodes must be strictly increasing")
    features = [
        interval(raw, f"feature_intervals[{index}]")
        for index, raw in enumerate(raw_features)
    ]

    canonical_table = {
        "nodes": [fj(value) for value in nodes],
        "feature_intervals": [ij(value) for value in features],
    }
    computed_sha = canonical_sha(canonical_table)
    declared_sha = data.get("feature_table_sha256")
    if declared_sha is not None and declared_sha != computed_sha:
        raise CertificateError("feature table SHA-256 mismatch")

    rows = []
    for degree in range(len(nodes) - 1):
        beta = basis_vector(nodes, degree)
        if sum(beta) != 0:
            raise CertificateError("basis vector fails zero-sum identity")
        polynomial = response_polynomial(nodes, beta)
        expected = [Fraction(0)] * degree + [Fraction(1)]
        if polynomial != expected:
            raise CertificateError("basis response-polynomial identity failed")
        value = Interval(Fraction(0), Fraction(0))
        for coefficient, feature in zip(beta, features):
            value = value.add(feature.scale(coefficient))
        rows.append(
            {
                "degree": degree,
                "response_polynomial_coefficients": [fj(entry) for entry in polynomial],
                "beta": [fj(entry) for entry in beta],
                "interval": ij(value),
                "status": status(value),
            }
        )

    negative = [row for row in rows if row["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [row for row in rows if row["status"] == "UNRESOLVED"]
    if negative:
        verdict = (
            "NEGATIVE_RIEMANN_XI_BASIS_WITNESS_PENDING_REPRODUCTION_AND_REVIEW"
            if classification == "RIEMANN_XI_DIRECTED"
            else "SYNTHETIC_NEGATIVE_BASIS_WITNESS"
        )
    elif unresolved:
        verdict = "UNRESOLVED_CONE"
    else:
        verdict = "CERTIFIED_NONNEGATIVE_ENTIRE_CONE"

    return {
        "schema": SCHEMA,
        "classification": classification,
        "feature_table_sha256": computed_sha,
        "node_count": len(nodes),
        "basis_row_count": len(rows),
        "basis_rows": rows,
        "certified_negative_rows": len(negative),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "scope": (
            "By L-9309 these basis rows decide every normalized portfolio whose "
            "L-9308 response polynomial has nonnegative monomial coefficients, "
            "including every such portfolio on any subset of the declared nodes."
        ),
        "scope_warning": (
            "A Riemann-xi negative inherits the direct-xi and count-deflation analytic "
            "gates and requires independent primitive/count reproduction."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level certificate must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result["verdict"] != "UNRESOLVED_CONE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
