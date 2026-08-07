#!/usr/bin/env python3
"""Exact Fraction replay of L-20704's source-resolvent and pole-update identities."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


class VerifyError(RuntimeError):
    pass


def rational(value):
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, dict) and set(value) == {"numerator", "denominator"}:
        return Fraction(int(value["numerator"]), int(value["denominator"]))
    raise VerifyError(f"bad rational {value!r}")


def encode(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


def vector(values):
    return [rational(value) for value in values]


def matrix(values):
    return [[rational(value) for value in row] for row in values]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction())
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def matvec(a, x):
    return [
        sum((a[i][j] * x[j] for j in range(len(x))), Fraction())
        for i in range(len(a))
    ]


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Fraction())


def quadratic(x, a, y=None):
    return dot(x, matvec(a, x if y is None else y))


def subtract(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]


def outer(x, y):
    return [[a * b for b in y] for a in x]


def scale(scalar, a):
    return [[scalar * value for value in row] for row in a]


def inverse(matrix_value):
    n = len(matrix_value)
    if any(len(row) != n for row in matrix_value):
        raise VerifyError("matrix not square")
    work = [
        matrix_value[i][:] + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for k in range(n):
        pivot = next((i for i in range(k, n) if work[i][k]), None)
        if pivot is None:
            raise VerifyError("singular matrix")
        work[k], work[pivot] = work[pivot], work[k]
        divisor = work[k][k]
        work[k] = [value / divisor for value in work[k]]
        for i in range(n):
            if i == k:
                continue
            coefficient = work[i][k]
            if coefficient:
                work[i] = [
                    work[i][j] - coefficient * work[k][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in work]


def ldl_pivots(a):
    n = len(a)
    lower = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    pivots = []
    for i in range(n):
        pivot = a[i][i] - sum(
            (lower[i][k] * lower[i][k] * pivots[k] for k in range(i)),
            Fraction(),
        )
        if pivot <= 0:
            raise VerifyError(f"nonpositive pivot {i}: {pivot}")
        pivots.append(pivot)
        for j in range(i + 1, n):
            lower[j][i] = (
                a[j][i]
                - sum(
                    (lower[j][k] * lower[i][k] * pivots[k] for k in range(i)),
                    Fraction(),
                )
            ) / pivot
    return pivots


def digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def verify(certificate):
    if certificate.get("schema") != "riemann.x20706.source-resolvent.v1":
        raise VerifyError("schema")
    a = matrix(certificate["A"])
    metric = vector(certificate["metric_diagonal"])
    source = vector(certificate["source_functional"])
    complement = matrix(certificate["complement_basis"])
    n = len(a)
    if any(len(row) != n for row in a) or any(
        a[i][j] != a[j][i] for i in range(n) for j in range(n)
    ):
        raise VerifyError("A must be Hermitian/symmetric")
    if len(metric) != n or len(source) != n or len(complement) != n:
        raise VerifyError("dimension")
    if any(value <= 0 for value in metric):
        raise VerifyError("metric")

    q = [source[i] / metric[i] for i in range(n)]
    g = dot(source, q)
    for j in range(len(complement[0])):
        column = [complement[i][j] for i in range(n)]
        if dot(source, column):
            raise VerifyError("complement column not in source kernel")

    block = matmul(transpose(complement), matmul(a, complement))
    pivots = ldl_pivots(block)
    cross = matvec(transpose(complement), matvec(a, q))
    raw = quadratic(q, a)
    schur = raw - quadratic(cross, inverse(block))

    a_inverse = inverse(a)
    resolvent_mass = quadratic(source, a_inverse)
    resolvent_schur = g * g / resolvent_mass
    if schur != resolvent_schur:
        raise VerifyError("Schur/resolvent mismatch")

    tau = rational(certificate["pole_tau"])
    pole_vector = vector(certificate["pole_vector"])
    pole_free = subtract(a, scale(tau, outer(pole_vector, pole_vector)))
    pole_free_inverse = inverse(pole_free)
    pole_free_mass = quadratic(source, pole_free_inverse)
    pole_coupling = quadratic(source, pole_free_inverse, pole_vector)
    pole_self_mass = quadratic(pole_vector, pole_free_inverse)
    denominator = 1 + tau * pole_self_mass
    if not denominator:
        raise VerifyError("Sherman-Morrison denominator zero")
    updated_mass = (
        pole_free_mass - tau * pole_coupling * pole_coupling / denominator
    )
    if updated_mass != resolvent_mass:
        raise VerifyError("Sherman-Morrison mismatch")

    result = {
        "schema": "riemann.x20706.source-resolvent.result.v1",
        "verified": True,
        "g": encode(g),
        "complement_ldl_pivots": [encode(value) for value in pivots],
        "schur": encode(schur),
        "resolvent_mass": encode(resolvent_mass),
        "normalized_quotient": encode(schur / g),
        "pole_free_mass": encode(pole_free_mass),
        "pole_coupling": encode(pole_coupling),
        "pole_self_mass": encode(pole_self_mass),
        "sherman_morrison_denominator": encode(denominator),
        "verdict": "CERTIFIED_SOURCE_SCHUR_RESOLVENT_FACTORIZATION",
    }
    payload = dict(result)
    result["proof_object_sha256"] = digest(payload)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text())
    result = verify(certificate)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
