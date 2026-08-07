#!/usr/bin/env python3
"""Exact checker for the same-matrix cyclic identity and grading coherence.

The verifier uses only integers and fractions.Fraction. It certifies finite
linear-algebra identities. It never evaluates xi and does not certify RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.same-matrix-cyclic.v1"


def rat(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, dict) and set(value) == {"numerator", "denominator"}:
        n, d = value["numerator"], value["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise ValueError("boolean numerator/denominator")
        if not isinstance(n, int) or not isinstance(d, int) or d == 0:
            raise ValueError("malformed rational")
        return Fraction(n, d)
    raise ValueError(f"unsupported rational: {value!r}")


def dump_rat(value: Fraction) -> Any:
    if value.denominator == 1:
        return value.numerator
    return {"numerator": value.numerator, "denominator": value.denominator}


def matrix(value: Any) -> list[list[Fraction]]:
    if not isinstance(value, list) or not value or any(not isinstance(row, list) for row in value):
        raise ValueError("matrix must be a nonempty list of rows")
    out = [[rat(x) for x in row] for row in value]
    width = len(out[0])
    if width == 0 or any(len(row) != width for row in out):
        raise ValueError("ragged matrix")
    return out


def zeros(n: int, m: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(m)] for _ in range(n)]


def eye(n: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(a[0]) != len(b):
        raise ValueError("matrix multiplication dimension mismatch")
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matadd(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("matrix addition dimension mismatch")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matsub(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("matrix subtraction dimension mismatch")
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matscale(c: Fraction, a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[c * x for x in row] for row in a]


def trace(a: list[list[Fraction]]) -> Fraction:
    if len(a) != len(a[0]):
        raise ValueError("trace requires square matrix")
    return sum(a[i][i] for i in range(len(a)))


def matpow(a: list[list[Fraction]], exponent: int) -> list[list[Fraction]]:
    if exponent < 0 or len(a) != len(a[0]):
        raise ValueError("invalid matrix power")
    result = eye(len(a))
    base = [row[:] for row in a]
    e = exponent
    while e:
        if e & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        e >>= 1
    return result


def inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("inverse requires square matrix")
    identity = eye(n)
    aug = [a[i][:] + identity[i] for i in range(n)]
    for k in range(n):
        pivot = next((r for r in range(k, n) if aug[r][k] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        if pivot != k:
            aug[k], aug[pivot] = aug[pivot], aug[k]
        p = aug[k][k]
        aug[k] = [x / p for x in aug[k]]
        for r in range(n):
            if r == k or aug[r][k] == 0:
                continue
            factor = aug[r][k]
            aug[r] = [aug[r][c] - factor * aug[k][c] for c in range(2 * n)]
    return [row[n:] for row in aug]


def is_symmetric(a: list[list[Fraction]]) -> bool:
    return len(a) == len(a[0]) and a == transpose(a)


def ldl_positive(a: list[list[Fraction]]) -> list[Fraction]:
    if not is_symmetric(a):
        raise ValueError("positive matrix must be symmetric")
    n = len(a)
    ell = zeros(n, n)
    pivots: list[Fraction] = []
    for i in range(n):
        ell[i][i] = Fraction(1)
        d = a[i][i] - sum(ell[i][k] * ell[i][k] * pivots[k] for k in range(i))
        if d <= 0:
            raise ValueError(f"nonpositive LDL pivot {i}: {d}")
        pivots.append(d)
        for j in range(i + 1, n):
            ell[j][i] = (
                a[j][i]
                - sum(ell[j][k] * ell[i][k] * pivots[k] for k in range(i))
            ) / d
    return pivots


def direct_cubic(b: list[list[Fraction]], ginv: list[list[Fraction]]) -> Fraction:
    n = len(b)
    return sum(
        b[a][bb] * ginv[bb][c] * b[c][d] * ginv[d][e] * b[e][f] * ginv[f][a]
        for a in range(n)
        for bb in range(n)
        for c in range(n)
        for d in range(n)
        for e in range(n)
        for f in range(n)
    )


def require_square_same_size(*items: list[list[Fraction]]) -> int:
    n = len(items[0])
    if any(len(a) != n or any(len(row) != n for row in a) for a in items):
        raise ValueError("matrix size mismatch")
    return n


def verify_graded(data: dict[str, Any]) -> dict[str, Any]:
    g, b, j, c = (matrix(data[name]) for name in ("gram", "seam", "grading", "basis_change"))
    n = require_square_same_size(g, b, j, c)
    if not is_symmetric(g) or not is_symmetric(b):
        raise ValueError("Gram and seam matrices must be symmetric")
    gram_pivots = ldl_positive(g)
    cinv = inverse(c)
    ginv = inverse(g)

    if matmul(j, j) != eye(n):
        raise ValueError("grading is not an involution")
    if matmul(transpose(j), g) != matmul(g, j):
        raise ValueError("grading is not Gram-self-adjoint")
    if matmul(transpose(j), matmul(b, j)) != matscale(Fraction(-1), b):
        raise ValueError("seam is not grading odd")

    t = matmul(ginv, b)
    max_order = data.get("max_order")
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 3:
        raise ValueError("max_order must be an integer at least 3")
    supplied = {int(k): rat(v) for k, v in data["trace_moments"].items()}
    if set(supplied) != set(range(2, max_order + 1)):
        raise ValueError("trace_moments must contain every order")
    moments: dict[int, Fraction] = {}
    for order in range(2, max_order + 1):
        value = trace(matpow(t, order))
        moments[order] = value
        if supplied[order] != value:
            raise ValueError(f"trace mismatch at order {order}")
        if order % 2 == 1 and value != 0:
            raise ValueError(f"odd trace does not vanish at order {order}")

    cubic = direct_cubic(b, ginv)
    if cubic != moments[3]:
        raise ValueError("direct six-index cubic does not match trace")
    if rat(data["normalized_cl3"]) != cubic:
        raise ValueError("normalized order-three scalar mismatch")

    gp = matmul(transpose(c), matmul(g, c))
    bp = matmul(transpose(c), matmul(b, c))
    jp = matmul(cinv, matmul(j, c))
    if gp != matrix(data["transformed_gram"]):
        raise ValueError("transformed Gram mismatch")
    if bp != matrix(data["transformed_seam"]):
        raise ValueError("transformed seam mismatch")
    if jp != matrix(data["transformed_grading"]):
        raise ValueError("transformed grading mismatch")
    if matmul(jp, jp) != eye(n):
        raise ValueError("transformed grading is not involutive")
    if matmul(transpose(jp), gp) != matmul(gp, jp):
        raise ValueError("transformed grading lost Gram self-adjointness")
    if matmul(transpose(jp), matmul(bp, jp)) != matscale(Fraction(-1), bp):
        raise ValueError("transformed seam lost oddness")
    tp = matmul(inverse(gp), bp)
    if tp != matmul(cinv, matmul(t, c)):
        raise ValueError("represented operator does not transform by similarity")
    transformed = {order: trace(matpow(tp, order)) for order in range(2, max_order + 1)}
    if transformed != moments:
        raise ValueError("cyclic coefficients are not basis invariant")

    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return {
        "status": "CERTIFIED_GRADED_SAME_MATRIX_ALL_ORDERS",
        "dimension": n,
        "gram_ldl_pivots": [dump_rat(x) for x in gram_pivots],
        "trace_moments": {str(k): dump_rat(v) for k, v in moments.items()},
        "direct_order_three": dump_rat(cubic),
        "basis_invariance": "PASS",
        "certificate_sha256": hashlib.sha256(canonical).hexdigest(),
        "scope": "finite operator-side identity only; no classical xi pullback",
    }


def verify_gram_obstruction(data: dict[str, Any]) -> dict[str, Any]:
    g, b = matrix(data["gram"]), matrix(data["seam"])
    require_square_same_size(g, b)
    ldl_positive(g)
    if not is_symmetric(b):
        raise ValueError("seam must be symmetric")
    true_cubic = trace(matpow(matmul(inverse(g), b), 3))
    naive_cubic = trace(matpow(b, 3))
    if true_cubic != rat(data["true_cubic"]):
        raise ValueError("true cubic mismatch")
    if naive_cubic != rat(data["naive_cubic"]):
        raise ValueError("naive cubic mismatch")
    if true_cubic == naive_cubic:
        raise ValueError("certificate does not exhibit Gram omission")
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return {
        "status": "CERTIFIED_INVERSE_GRAM_IS_LOAD_BEARING",
        "true_gram_cyclic_cubic": dump_rat(true_cubic),
        "naive_seam_cubic": dump_rat(naive_cubic),
        "certificate_sha256": hashlib.sha256(canonical).hexdigest(),
    }


def verify_compression_obstruction(data: dict[str, Any]) -> dict[str, Any]:
    k, gamma, p = (matrix(data[name]) for name in ("operator", "grading", "projection"))
    n = require_square_same_size(k, gamma, p)
    if not is_symmetric(k) or not is_symmetric(gamma) or not is_symmetric(p):
        raise ValueError("operator, grading, and projection must be symmetric")
    if matmul(gamma, gamma) != eye(n):
        raise ValueError("grading is not involutive")
    if matmul(gamma, matmul(k, gamma)) != matscale(Fraction(-1), k):
        raise ValueError("original operator is not grading odd")
    if matmul(p, p) != p:
        raise ValueError("P is not a projection")
    if matmul(p, gamma) == matmul(gamma, p):
        raise ValueError("projection unexpectedly preserves grading")

    kp = matmul(p, matmul(k, p))
    gp = matmul(p, matmul(gamma, p))
    cubic = trace(matpow(kp, 3))
    square_defect = matsub(matmul(gp, gp), p)
    anti_defect = matadd(matmul(gp, kp), matmul(kp, gp))
    if cubic != rat(data["compressed_cubic"]):
        raise ValueError("compressed cubic mismatch")
    if cubic == 0:
        raise ValueError("compression does not break odd trace")
    if kp != matrix(data["compressed_operator"]):
        raise ValueError("compressed operator mismatch")
    if gp != matrix(data["compressed_grading"]):
        raise ValueError("compressed grading mismatch")
    if square_defect != matrix(data["grading_square_defect"]):
        raise ValueError("grading square defect mismatch")
    if anti_defect != matrix(data["anticommutator_defect"]):
        raise ValueError("anticommutator defect mismatch")

    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return {
        "status": "CERTIFIED_NONINVARIANT_COMPRESSION_CREATES_CUBIC_TRACE",
        "compressed_cubic": dump_rat(cubic),
        "grading_square_defect": [[dump_rat(x) for x in row] for row in square_defect],
        "anticommutator_defect": [[dump_rat(x) for x in row] for row in anti_defect],
        "certificate_sha256": hashlib.sha256(canonical).hexdigest(),
    }


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("wrong schema")
    mode = data.get("mode")
    if mode == "graded-cyclic-pass":
        return verify_graded(data)
    if mode == "gram-omission-obstruction":
        return verify_gram_obstruction(data)
    if mode == "compression-leakage-obstruction":
        return verify_compression_obstruction(data)
    raise ValueError("unknown mode")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    print(json.dumps(verify(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
