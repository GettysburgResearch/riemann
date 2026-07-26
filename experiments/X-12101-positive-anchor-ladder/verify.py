#!/usr/bin/env python3
"""Exact verifier for positive-anchor Christoffel moment ladders."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.positive-anchor-moment-ladder.v1"
VERIFY_SCHEMA = "riemann.positive-anchor-moment-ladder.verification.v1"


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must be an integer, not bool")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a base-10 integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = parse_int(value.get("numerator"), name + ".numerator")
    denominator = parse_int(value.get("denominator"), name + ".denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def canonical_sha(data: Any) -> str:
    encoded = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def divided_transform(
    anchors: list[Fraction], scalars: list[Fraction]
) -> Fraction:
    """Return integral prod_j (y+w_j)^-1 from the one-anchor values."""
    values = list(scalars)
    count = len(anchors)
    for level in range(1, count):
        values = [
            (values[index + 1] - values[index])
            / (anchors[index + level] - anchors[index])
            for index in range(len(values) - 1)
        ]
    return (-1) ** (count - 1) * values[0]


def transform_moments(
    old: list[Fraction],
    anchors: list[Fraction],
    scalars: list[Fraction],
) -> list[Fraction]:
    previous = list(old)
    for index, anchor in enumerate(anchors):
        zeroth = divided_transform(
            anchors[: index + 1], scalars[: index + 1]
        )
        current = [zeroth]
        for moment in previous:
            current.append(moment - anchor * current[-1])
        previous = current
    return previous


def hankel(
    moments: list[Fraction], degree: int
) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    h0_size = degree // 2 + 1
    h1_size = (degree - 1) // 2 + 1
    h0 = [
        [moments[row + column] for column in range(h0_size)]
        for row in range(h0_size)
    ]
    h1 = [
        [moments[row + column + 1] for column in range(h1_size)]
        for row in range(h1_size)
    ]
    return h0, h1


def quadratic(
    matrix: list[list[Fraction]], vector: list[Fraction]
) -> Fraction:
    if len(matrix) != len(vector):
        raise CertificateError("vector dimension does not match matrix")
    return sum(
        vector[row] * matrix[row][column] * vector[column]
        for row in range(len(vector))
        for column in range(len(vector))
    )


def ldl_pivots(matrix: list[list[Fraction]]) -> list[Fraction]:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise CertificateError("matrix is not square")
    if any(
        matrix[row][column] != matrix[column][row]
        for row in range(size)
        for column in range(size)
    ):
        raise CertificateError("matrix is not symmetric")
    lower = [
        [Fraction(0) for _ in range(size)] for _ in range(size)
    ]
    pivots: list[Fraction] = []
    for column in range(size):
        pivot = matrix[column][column] - sum(
            lower[column][prior]
            * lower[column][prior]
            * pivots[prior]
            for prior in range(column)
        )
        if pivot == 0:
            raise CertificateError("zero LDL pivot")
        pivots.append(pivot)
        lower[column][column] = Fraction(1)
        for row in range(column + 1, size):
            lower[row][column] = (
                matrix[row][column]
                - sum(
                    lower[row][prior]
                    * lower[column][prior]
                    * pivots[prior]
                    for prior in range(column)
                )
            ) / pivot
    return pivots


def parse_vector(raw: Any, name: str) -> list[Fraction]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty array")
    vector = [
        parse_fraction(value, f"{name}[{index}]")
        for index, value in enumerate(raw)
    ]
    if all(value == 0 for value in vector):
        raise CertificateError(f"{name} must be nonzero")
    return vector


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    old_degree = parse_int(data.get("old_degree"), "old_degree")
    if old_degree < 0:
        raise CertificateError("old_degree must be nonnegative")

    raw_old = data.get("old_moments")
    raw_anchors = data.get("anchors")
    raw_scalars = data.get("anchor_scalars")
    raw_checks = data.get("checks")
    declared = data.get("declared_check_ids")
    if not isinstance(raw_old, list) or len(raw_old) != old_degree + 1:
        raise CertificateError(
            "old_moments length must equal old_degree+1"
        )
    if not isinstance(raw_anchors, list) or not raw_anchors:
        raise CertificateError("anchors must be a nonempty array")
    if not isinstance(raw_scalars, list) or len(raw_scalars) != len(
        raw_anchors
    ):
        raise CertificateError("anchor_scalars length mismatch")
    if not isinstance(raw_checks, list):
        raise CertificateError("checks must be an array")
    if not isinstance(declared, list) or not all(
        isinstance(value, str) for value in declared
    ):
        raise CertificateError(
            "declared_check_ids must be an array of strings"
        )

    old = [
        parse_fraction(value, f"old_moments[{index}]")
        for index, value in enumerate(raw_old)
    ]
    anchors = [
        parse_fraction(value, f"anchors[{index}]")
        for index, value in enumerate(raw_anchors)
    ]
    scalars = [
        parse_fraction(value, f"anchor_scalars[{index}]")
        for index, value in enumerate(raw_scalars)
    ]
    if any(anchor <= 0 for anchor in anchors):
        raise CertificateError("anchors must be positive")
    if anchors != sorted(anchors) or len(set(anchors)) != len(anchors):
        raise CertificateError("anchors must be strictly increasing")

    moments = transform_moments(old, anchors, scalars)
    reverse_moments = transform_moments(
        old, list(reversed(anchors)), list(reversed(scalars))
    )
    if moments != reverse_moments:
        raise CertificateError("anchor-order invariance failed")

    final_degree = old_degree + len(anchors)
    h0, h1 = hankel(moments, final_degree)
    summaries: list[dict[str, Any]] = []
    seen: set[str] = set()
    negative: list[str] = []
    positive_cone = False

    for index, check in enumerate(raw_checks):
        if not isinstance(check, dict):
            raise CertificateError(f"checks[{index}] must be an object")
        identifier = check.get("id")
        kind = check.get("kind")
        if (
            not isinstance(identifier, str)
            or not identifier
            or identifier in seen
        ):
            raise CertificateError(
                "check IDs must be nonempty and unique"
            )
        seen.add(identifier)

        if kind in ("h0-vector", "h1-vector"):
            matrix = h0 if kind == "h0-vector" else h1
            vector = parse_vector(
                check.get("vector"), f"checks[{index}].vector"
            )
            value = quadratic(matrix, vector)
            claimed = check.get("claimed_value")
            if claimed is not None and parse_fraction(
                claimed, "claimed_value"
            ) != value:
                raise CertificateError(
                    f"{identifier}: claimed quadratic mismatch"
                )
            status = (
                "CERTIFIED_NEGATIVE"
                if value < 0
                else "CERTIFIED_POSITIVE"
                if value > 0
                else "EXACT_ZERO"
            )
            if value < 0:
                negative.append(identifier)
            summaries.append(
                {
                    "id": identifier,
                    "kind": kind,
                    "status": status,
                    "value": fraction_json(value),
                    "vector": [fraction_json(x) for x in vector],
                }
            )
        elif kind == "full-cone-positive":
            h0_pivots = ldl_pivots(h0)
            h1_pivots = ldl_pivots(h1)
            if any(value <= 0 for value in h0_pivots + h1_pivots):
                raise CertificateError(
                    f"{identifier}: matrix is not positive definite"
                )
            positive_cone = True
            summaries.append(
                {
                    "id": identifier,
                    "kind": kind,
                    "status": "CERTIFIED_POSITIVE_FULL_HALF_LINE_CONE",
                    "h0_pivots": [
                        fraction_json(value) for value in h0_pivots
                    ],
                    "h1_pivots": [
                        fraction_json(value) for value in h1_pivots
                    ],
                }
            )
        else:
            raise CertificateError(
                f"{identifier}: unsupported check kind"
            )

    if declared != [item["id"] for item in summaries]:
        raise CertificateError(
            "declared_check_ids must exactly match ordered check IDs"
        )

    if negative:
        status = "CERTIFIED_NEGATIVE_HALF_LINE_RESPONSE"
    elif positive_cone:
        status = "CERTIFIED_POSITIVE_FULL_HALF_LINE_CONE"
    else:
        status = "NO_DECISIVE_CHECK"

    result: dict[str, Any] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": status,
        "old_degree": old_degree,
        "anchor_count": len(anchors),
        "final_degree": final_degree,
        "anchors": [fraction_json(value) for value in anchors],
        "transformed_moments": [
            fraction_json(value) for value in moments
        ],
        "checks": summaries,
        "negative_checks": negative,
        "proof_boundary": (
            "This verifies finite rational Christoffel recurrences and "
            "Hankel quadratic forms. It does not establish any Riemann-xi "
            "primitive, count-deflation gate, or analytic RH implication."
        ),
    }
    result["verification_sha256"] = canonical_sha(result)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {
            "schema": VERIFY_SCHEMA,
            "verified": False,
            "status": "REJECTED",
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
