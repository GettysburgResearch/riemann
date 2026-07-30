#!/usr/bin/env python3
"""Exact checker for the target-pinned diagonal completion in T-15103."""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15102-target-pinned-completion.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer, not Boolean")
    return value


def rational(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not rational") from exc
    if isinstance(value, list) and len(value) == 2:
        numerator = integer(value[0], name + "[0]")
        denominator = integer(value[1], name + "[1]")
        if denominator == 0:
            raise CertificateError(f"{name} has zero denominator")
        return Fraction(numerator, denominator)
    raise CertificateError(f"{name} has unsupported rational encoding")


def vector(raw: Any, name: str) -> list[Fraction]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty list")
    return [rational(value, f"{name}[{i}]") for i, value in enumerate(raw)]


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty matrix")
    rows = [vector(row, f"{name}[{i}]") for i, row in enumerate(raw)]
    n = len(rows)
    if any(len(row) != n for row in rows):
        raise CertificateError(f"{name} must be square")
    if any(rows[i][j] != rows[j][i] for i in range(n) for j in range(n)):
        raise CertificateError(f"{name} must be symmetric")
    return rows


def dot(x: list[Fraction], y: list[Fraction]) -> Fraction:
    if len(x) != len(y):
        raise CertificateError("vector dimensions differ")
    return sum(a * b for a, b in zip(x, y))


def matvec(a: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    if len(a) != len(x):
        raise CertificateError("matrix/vector dimensions differ")
    return [sum(row[j] * x[j] for j in range(len(x))) for row in a]


def canonical_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def connected(weights: list[list[Fraction]]) -> bool:
    n = len(weights)
    seen = {0}
    queue = deque([0])
    while queue:
        i = queue.popleft()
        for j in range(n):
            if j not in seen and weights[i][j] > 0:
                seen.add(j)
                queue.append(j)
    return len(seen) == n


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    d = vector(payload.get("frequencies"), "frequencies")
    eta = vector(payload.get("boundary"), "boundary")
    beta = vector(payload.get("beta"), "beta")
    p = vector(payload.get("target"), "target")
    q = matrix(payload.get("weil_matrix"), "weil_matrix")
    c = rational(payload.get("c"), "c")
    n = len(q)
    if any(len(item) != n for item in (d, eta, beta, p)):
        raise CertificateError("dimension mismatch")
    if any(value == 0 for value in p):
        raise CertificateError("every target coordinate must be nonzero")
    if dot(eta, p) != 1:
        raise CertificateError("target boundary normalization is not one")

    for i in range(n):
        for j in range(n):
            left = (d[i] - d[j]) * q[i][j]
            right = beta[i] * eta[j] - eta[i] * beta[j]
            if left != right:
                raise CertificateError("input special commutator identity failed")

    qp = matvec(q, p)
    diagonal = [(c * eta[i] - qp[i]) / p[i] for i in range(n)]
    t = [
        [
            q[i][j]
            + (diagonal[i] if i == j else 0)
            - c * eta[i] * eta[j]
            for j in range(n)
        ]
        for i in range(n)
    ]
    if matvec(t, p) != [Fraction(0)] * n:
        raise CertificateError("completed matrix does not annihilate the target")

    beta_new = [beta[i] - c * d[i] * eta[i] for i in range(n)]
    for i in range(n):
        for j in range(n):
            left = (d[i] - d[j]) * t[i][j]
            right = beta_new[i] * eta[j] - eta[i] * beta_new[j]
            if left != right:
                raise CertificateError("completed special commutator identity failed")

    weights = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            weight = -(q[i][j] - c * eta[i] * eta[j]) * p[i] * p[j]
            if weight < 0:
                raise CertificateError("a graph-SOS edge weight is negative")
            weights[i][j] = weights[j][i] = weight
    if not connected(weights):
        raise CertificateError("positive graph-SOS edges are not connected")

    reconstructed = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            weight = weights[i][j]
            reconstructed[i][i] += weight / (p[i] * p[i])
            reconstructed[j][j] += weight / (p[j] * p[j])
            reconstructed[i][j] -= weight / (p[i] * p[j])
            reconstructed[j][i] = reconstructed[i][j]
    if reconstructed != t:
        raise CertificateError("graph-SOS reconstruction does not equal completion")

    # Optional exact reversal-parity audit.
    if payload.get("check_reversal_parity", True) is not True:
        raise CertificateError("reversal parity gate must be enabled")
    for i in range(n):
        ri = n - 1 - i
        if d[ri] != -d[i] or eta[ri] != eta[i] or p[ri] != p[i]:
            raise CertificateError("vector reversal parity failed")
        for j in range(n):
            if q[ri][n - 1 - j] != q[i][j]:
                raise CertificateError("matrix reversal parity failed")

    result: dict[str, Any] = {
        "schema": SCHEMA,
        "classification": "EXACT_TARGET_PINNED_GRAPH_SOS",
        "dimension": n,
        "c": str(c),
        "diagonal_completion": [str(value) for value in diagonal],
        "completed_matrix": [[str(value) for value in row] for row in t],
        "updated_beta": [str(value) for value in beta_new],
        "positive_edge_count": sum(
            1 for i in range(n) for j in range(i + 1, n) if weights[i][j] > 0
        ),
        "graph_connected": True,
        "kernel_vector": [str(value) for value in p],
        "proof_boundary": (
            "The checker proves the finite diagonal completion, graph-SOS PSD, "
            "one-dimensional kernel, parity, and special commutator algebra. The "
            "CCM theorem converting these gates into a real-zero transform remains "
            "an imported analytic dependency."
        ),
    }
    result["exact_proof_object_sha256"] = canonical_digest(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify(payload)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {"schema": SCHEMA, "classification": "REJECTED", "reason": str(exc)}
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
