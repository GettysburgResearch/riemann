#!/usr/bin/env python3
"""Exact rational verifier for the structured growing D-0001 zero frame."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.x20703.structured-frame.certificate.v1"


class VerificationError(RuntimeError):
    pass


def q(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise VerificationError("booleans are not rational values")
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, dict) or set(value) != {"numerator", "denominator"}:
        raise VerificationError("rational must have numerator and denominator")
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def out(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def det(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    a = [list(row) for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise VerificationError("determinant requires a square matrix")
    answer = Fraction(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            answer = -answer
        value = a[k][k]
        answer *= value
        for j in range(k, n):
            a[k][j] /= value
        for i in range(k + 1, n):
            factor = a[i][k]
            if factor:
                for j in range(k, n):
                    a[i][j] -= factor * a[k][j]
    return answer


def matmul(a, b):
    if len(a[0]) != len(b):
        raise VerificationError("matrix product mismatch")
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction())
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def transpose(a):
    return [list(row) for row in zip(*a)]


def inverse(a):
    n = len(a)
    augmented = [
        list(a[i]) + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for k in range(n):
        pivot = next((i for i in range(k, n) if augmented[i][k]), None)
        if pivot is None:
            raise VerificationError("singular matrix")
        augmented[k], augmented[pivot] = augmented[pivot], augmented[k]
        value = augmented[k][k]
        augmented[k] = [entry / value for entry in augmented[k]]
        for i in range(n):
            if i == k:
                continue
            factor = augmented[i][k]
            if factor:
                augmented[i] = [
                    augmented[i][j] - factor * augmented[k][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in augmented]


def vandermonde_product(values):
    answer = Fraction(1)
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            answer *= values[j] - values[i]
    return answer


def cauchy_vandermonde(nodes, poles):
    return [[Fraction(1)] + [Fraction(1, x - a) for a in poles] for x in nodes]


def raw_rows(nodes, poles, scalars):
    return [
        [s] + [s * 2 * x / (x - a) for a in poles]
        for x, s in zip(nodes, scalars)
    ]


def transformed_from_raw(raw, poles, scalars):
    rows = []
    for row, scalar in zip(raw, scalars):
        normalized = [entry / scalar for entry in row]
        rows.append(
            [normalized[0]]
            + [
                (normalized[n + 1] / 2 - normalized[0]) / poles[n]
                for n in range(len(poles))
            ]
        )
    return rows


def structured_solve(nodes, poles, data):
    def polynomial(x):
        answer = Fraction(1)
        for a in poles:
            answer *= x - a
        return answer

    leading = Fraction()
    for i, x in enumerate(nodes):
        denominator = Fraction(1)
        for j, z in enumerate(nodes):
            if i != j:
                denominator *= x - z
        leading += data[i] * polynomial(x) / denominator

    coefficients = [leading]
    for a in poles:
        h_value = Fraction()
        for i, x in enumerate(nodes):
            lagrange = Fraction(1)
            for j, z in enumerate(nodes):
                if i != j:
                    lagrange *= Fraction(a - z, x - z)
            h_value += data[i] * polynomial(x) * lagrange
        derivative = Fraction(1)
        for b in poles:
            if b != a:
                derivative *= a - b
        coefficients.append(h_value / derivative)
    return coefficients


def newton_evaluation(nodes, poles):
    dimension = len(poles) + 1
    matrix = []
    pivots = []
    for i, x in enumerate(nodes):
        row = []
        for k in range(dimension):
            if k == 0:
                value = Fraction(1)
            else:
                value = Fraction(1)
                for j in range(k):
                    value *= x - nodes[j]
                for j in range(1, k + 1):
                    value /= x - poles[j - 1]
            row.append(value)
        matrix.append(row)
        pivots.append(row[i])
    return matrix, pivots


def schur(block_rr, block_rw, block_ww):
    correction = matmul(matmul(block_rw, inverse(block_ww)), transpose(block_rw))
    return [
        [block_rr[i][j] - correction[i][j] for j in range(len(block_rr))]
        for i in range(len(block_rr))
    ]


def canonical_digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def verify(certificate):
    if certificate.get("schema") != SCHEMA:
        raise VerificationError("unexpected schema")
    nodes = [q(x) for x in certificate["nodes"]]
    poles = [q(x) for x in certificate["poles"]]
    scalars = [q(x) for x in certificate["row_scalars"]]
    if len(nodes) != len(poles) + 1 or len(scalars) != len(nodes):
        raise VerificationError("dimension mismatch")
    if len(set(nodes)) != len(nodes) or len(set(poles)) != len(poles):
        raise VerificationError("duplicate node or pole")
    if any(x == a for x in nodes for a in poles) or any(s == 0 for s in scalars):
        raise VerificationError("resonant node or zero row scalar")

    cauchy = cauchy_vandermonde(nodes, poles)
    raw = raw_rows(nodes, poles, scalars)
    if transformed_from_raw(raw, poles, scalars) != cauchy:
        raise VerificationError("column transform failed")

    n = len(poles)
    formula = (
        (-1) ** (n * (n + 1) // 2)
        * vandermonde_product(nodes)
        * vandermonde_product(poles)
    )
    for x in nodes:
        for a in poles:
            formula /= x - a
    if det(cauchy) != formula or formula == 0:
        raise VerificationError("Cauchy-Vandermonde determinant failed")

    data = [q(x) for x in certificate["interpolation_data"]]
    coefficients = structured_solve(nodes, poles, data)
    reproduced = [
        sum(cauchy[i][j] * coefficients[j] for j in range(n + 1))
        for i in range(n + 1)
    ]
    if reproduced != data:
        raise VerificationError("structured inverse failed")

    newton, pivots = newton_evaluation(nodes, poles)
    if any(newton[i][j] for i in range(n + 1) for j in range(i + 1, n + 1)):
        raise VerificationError("Newton matrix is not lower triangular")
    product = Fraction(1)
    for pivot in pivots:
        product *= pivot
    if det(newton) != product or any(pivot == 0 for pivot in pivots):
        raise VerificationError("Newton pivot product failed")

    operator = [[q(x) for x in row] for row in certificate["schur_model"]]
    radical_dimension = int(certificate["radical_dimension"])
    rr = [row[:radical_dimension] for row in operator[:radical_dimension]]
    rw = [row[radical_dimension:] for row in operator[:radical_dimension]]
    ww = [row[radical_dimension:] for row in operator[radical_dimension:]]
    if det(ww) <= 0:
        raise VerificationError("positive-sector control not positive")
    base_schur = schur(rr, rw, ww)

    graph = [[q(x) for x in row] for row in certificate["graph_coefficients"]]
    identity_r = [
        [Fraction(int(i == j)) for j in range(radical_dimension)]
        for i in range(radical_dimension)
    ]
    zero_rw = [[Fraction() for _ in range(len(ww))] for _ in range(radical_dimension)]
    identity_w = [
        [Fraction(int(i == j)) for j in range(len(ww))]
        for i in range(len(ww))
    ]
    transform = [identity_r[i] + zero_rw[i] for i in range(radical_dimension)]
    transform += [graph[i] + identity_w[i] for i in range(len(ww))]
    transformed = matmul(matmul(transpose(transform), operator), transform)
    rr2 = [row[:radical_dimension] for row in transformed[:radical_dimension]]
    rw2 = [row[radical_dimension:] for row in transformed[:radical_dimension]]
    ww2 = [row[radical_dimension:] for row in transformed[radical_dimension:]]
    graph_schur = schur(rr2, rw2, ww2)
    if graph_schur != base_schur:
        raise VerificationError("graph Schur invariance failed")

    result = {
        "schema": "riemann.x20703.structured-frame.result.v1",
        "dimension": n + 1,
        "cauchy_determinant": out(formula),
        "structured_coefficients": [out(x) for x in coefficients],
        "newton_pivots": [out(x) for x in pivots],
        "base_schur": [[out(x) for x in row] for row in base_schur],
        "graph_schur": [[out(x) for x in row] for row in graph_schur],
        "verdict": "CERTIFIED_STRUCTURED_CAUCHY_FRAME_AND_SCHUR_INVARIANCE",
    }
    result["proof_object_sha256"] = canonical_digest(result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text())
    result = verify(certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
