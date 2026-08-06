#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "X-15121-v1"


def frac(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"unsupported rational value: {value!r}")


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def kappa(y: Fraction, a: Fraction, b: Fraction) -> Fraction:
    threshold = max(a, b)
    if threshold >= y:
        return Fraction(0)
    return Fraction(1, 1) / threshold - Fraction(1, 1) / y


def kernel(y: Fraction, scale: Fraction, m: Fraction, n: Fraction) -> Fraction:
    return (
        kappa(y, m, n)
        - scale * kappa(y, scale * m, n)
        - scale * kappa(y, m, scale * n)
        + scale * scale * kappa(y, scale * m, scale * n)
    )


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    a = [row[:] for row in matrix]
    det = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        p = a[col][col]
        det *= p
        for r in range(col + 1, n):
            if a[r][col] == 0:
                continue
            factor = a[r][col] / p
            for c in range(col, n):
                a[r][c] -= factor * a[col][c]
    return det


def verify(cert: dict[str, Any]) -> dict[str, Any]:
    if cert.get("schema") != SCHEMA:
        raise ValueError("wrong schema")
    scale = frac(cert["scale"])
    y = frac(cert["Y"])
    if scale <= 1 or y <= 1:
        raise ValueError("require scale>1 and Y>1")

    rows = cert.get("weights")
    if not isinstance(rows, list) or not rows:
        raise ValueError("weights must be a nonempty list")
    nodes: list[Fraction] = []
    weights: list[Fraction] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("malformed weight row")
        node = frac(row["n"])
        weight = frac(row["weight"])
        if node < 1 or node >= y:
            raise ValueError("node outside [1,Y)")
        if weight < 0:
            raise ValueError("weights must be nonnegative")
        nodes.append(node)
        weights.append(weight)
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate nodes")

    gram = [[kernel(y, scale, m, n) for n in nodes] for m in nodes]
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if gram[i][j] != gram[j][i]:
                raise AssertionError("Gram is not symmetric")

    principal_minors = [
        determinant([row[:k] for row in gram[:k]])
        for k in range(1, len(nodes) + 1)
    ]
    if any(value < 0 for value in principal_minors):
        raise AssertionError("Gram failed positive-semidefinite control")

    energy = sum(
        weights[i] * gram[i][j] * weights[j]
        for i in range(len(nodes))
        for j in range(len(nodes))
    )
    diagonal = sum(
        weights[i] * weights[i] * gram[i][i]
        for i in range(len(nodes))
    )
    off_diagonal = energy - diagonal

    thresholds = {Fraction(1), y}
    for node in nodes:
        if node < y:
            thresholds.add(node)
        if scale * node < y:
            thresholds.add(scale * node)
    ordered = sorted(thresholds)
    replay = Fraction(0)
    for left, right in zip(ordered, ordered[1:]):
        if right <= left:
            continue
        coefficient = sum(
            weight
            * (
                (1 if left >= node else 0)
                - scale * (1 if left >= scale * node else 0)
            )
            for node, weight in zip(nodes, weights)
        )
        replay += coefficient * coefficient * (
            Fraction(1, 1) / left - Fraction(1, 1) / right
        )
    if replay != energy:
        raise AssertionError("cell replay disagrees with Gram contraction")

    normalized = {
        "schema": SCHEMA,
        "scale": fstr(scale),
        "Y": fstr(y),
        "nodes": [fstr(value) for value in nodes],
        "weights": [fstr(value) for value in weights],
        "gram": [[fstr(value) for value in row] for row in gram],
        "principal_minors": [fstr(value) for value in principal_minors],
        "energy": fstr(energy),
        "diagonal": fstr(diagonal),
        "off_diagonal": fstr(off_diagonal),
        "independent_cell_energy": fstr(replay),
    }
    encoded = json.dumps(
        normalized, sort_keys=True, separators=(",", ":")
    ).encode()
    normalized["proof_sha256"] = hashlib.sha256(encoded).hexdigest()
    normalized["verdict"] = "CERTIFIED_EXACT_DILATION_GRAM_IDENTITY"
    return normalized


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: verify.py CERTIFICATE.json RESULT.json")
    cert = json.loads(Path(sys.argv[1]).read_text())
    result = verify(cert)
    Path(sys.argv[2]).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
