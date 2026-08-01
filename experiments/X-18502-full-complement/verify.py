#!/usr/bin/env python3
r"""Fraction-only verifier for a full complementary selected-zero frame.

The certificate proves, on one finite metric packet U=R \oplus_G W,

    W^*(K-tau G)W > 0,
    R^*(epsilon G-K)R > 0,
    epsilon < tau,

and therefore the generalized evaluation count below tau is exactly dim R.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x18502-full-complement-frame.v1"


class Reject(ValueError):
    pass


def integer(x: Any, name: str) -> int:
    if isinstance(x, bool) or not isinstance(x, int):
        raise Reject(f"{name} must be an integer")
    return x


def rat(x: Any, name: str) -> Q:
    if not isinstance(x, dict):
        raise Reject(f"{name} must be a rational object")
    a = integer(x.get("numerator"), name + ".numerator")
    b = integer(x.get("denominator"), name + ".denominator")
    if b <= 0:
        raise Reject(f"{name}.denominator must be positive")
    return Q(a, b)


def matrix(x: Any, name: str) -> list[list[Q]]:
    if not isinstance(x, list) or not x or not all(isinstance(row, list) for row in x):
        raise Reject(f"{name} must be a nonempty matrix")
    out = [[rat(v, f"{name}[{i}][{j}]") for j, v in enumerate(row)] for i, row in enumerate(x)]
    widths = {len(row) for row in out}
    if len(widths) != 1 or next(iter(widths)) == 0:
        raise Reject(f"{name} is ragged or empty")
    return out


def shape(a: list[list[Q]]) -> tuple[int, int]:
    return len(a), len(a[0])


def transpose(a: list[list[Q]]) -> list[list[Q]]:
    return [list(row) for row in zip(*a)]


def add(a: list[list[Q]], b: list[list[Q]], scale: Q = Q(1)) -> list[list[Q]]:
    if shape(a) != shape(b):
        raise Reject("matrix addition shape mismatch")
    return [[a[i][j] + scale * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scalar(a: Q, m: list[list[Q]]) -> list[list[Q]]:
    return [[a * x for x in row] for row in m]


def mul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    if len(a[0]) != len(b):
        raise Reject("matrix multiplication shape mismatch")
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def contract(basis: list[list[Q]], form: list[list[Q]]) -> list[list[Q]]:
    return mul(transpose(basis), mul(form, basis))


def hstack(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    if len(a) != len(b):
        raise Reject("horizontal stack row mismatch")
    return [a[i] + b[i] for i in range(len(a))]


def symmetric(a: list[list[Q]]) -> bool:
    n, m = shape(a)
    return n == m and all(a[i][j] == a[j][i] for i in range(n) for j in range(n))


def rank(a: list[list[Q]]) -> int:
    m = [row[:] for row in a]
    nr, nc = shape(m)
    row = 0
    for col in range(nc):
        pivot = next((i for i in range(row, nr) if m[i][col] != 0), None)
        if pivot is None:
            continue
        m[row], m[pivot] = m[pivot], m[row]
        p = m[row][col]
        m[row] = [z / p for z in m[row]]
        for i in range(nr):
            if i != row and m[i][col] != 0:
                c = m[i][col]
                m[i] = [m[i][j] - c * m[row][j] for j in range(nc)]
        row += 1
        if row == nr:
            break
    return row


def pd_pivots(a: list[list[Q]], name: str) -> list[Q]:
    if not symmetric(a):
        raise Reject(f"{name} must be symmetric")
    n = len(a)
    ell = [[Q(0) for _ in range(n)] for _ in range(n)]
    pivots: list[Q] = []
    for i in range(n):
        d = a[i][i] - sum(ell[i][k] * ell[i][k] * pivots[k] for k in range(i))
        if d <= 0:
            raise Reject(f"{name} has nonpositive LDL pivot {i}")
        pivots.append(d)
        ell[i][i] = Q(1)
        for j in range(i + 1, n):
            ell[j][i] = (
                a[j][i] - sum(ell[j][k] * ell[i][k] * pivots[k] for k in range(i))
            ) / d
    return pivots


def zero_matrix(a: list[list[Q]]) -> bool:
    return all(x == 0 for row in a for x in row)


def outq(x: Q) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def digest(x: Any) -> str:
    payload = json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise Reject("schema mismatch")

    g = matrix(data.get("metric"), "metric")
    k = matrix(data.get("evaluation_gram"), "evaluation_gram")
    if shape(g) != shape(k) or shape(g)[0] != shape(g)[1]:
        raise Reject("metric/evaluation matrix shape mismatch")
    n = len(g)
    gp = pd_pivots(g, "metric")
    if not symmetric(k):
        raise Reject("evaluation_gram must be symmetric")

    r_basis = matrix(data.get("radical_basis"), "radical_basis")
    w_basis = matrix(data.get("complement_basis"), "complement_basis")
    if len(r_basis) != n or len(w_basis) != n:
        raise Reject("basis ambient dimension mismatch")
    r = len(r_basis[0])
    d = len(w_basis[0])
    if rank(r_basis) != r:
        raise Reject("radical_basis is rank deficient")
    if rank(w_basis) != d:
        raise Reject("complement_basis is rank deficient")
    if r + d != n or rank(hstack(r_basis, w_basis)) != n:
        raise Reject("radical and complement bases do not form a full packet")

    cross = mul(transpose(r_basis), mul(g, w_basis))
    if not zero_matrix(cross):
        raise Reject("radical/complement split is not metric orthogonal")

    tau = rat(data.get("threshold"), "threshold")
    eps = rat(data.get("radical_evaluation_upper"), "radical_evaluation_upper")
    if tau <= 0:
        raise Reject("threshold must be positive")
    if eps < 0 or eps >= tau:
        raise Reject("radical evaluation endpoint must satisfy 0 <= epsilon < threshold")

    high = contract(w_basis, add(k, scalar(tau, g), Q(-1)))
    high_pivots = pd_pivots(high, "strict complement frame")

    radical_moat = contract(r_basis, add(scalar(eps, g), k, Q(-1)))
    radical_pivots = pd_pivots(radical_moat, "strict radical evaluation upper moat")

    result: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "CERTIFIED_FULL_COMPLEMENT_AND_SHARP_COUNT",
        "ambient_dimension": n,
        "radical_rank": r,
        "complement_rank": d,
        "threshold": outq(tau),
        "radical_evaluation_upper": outq(eps),
        "count_lower": r,
        "count_upper": r,
        "angle_squared_upper": outq(eps / tau),
        "metric_ldl_pivots": [outq(x) for x in gp],
        "complement_frame_ldl_pivots": [outq(x) for x in high_pivots],
        "radical_moat_ldl_pivots": [outq(x) for x in radical_pivots],
    }
    result["proof_object_sha256"] = digest(result)

    expected = data.get("expected")
    if not isinstance(expected, dict):
        raise Reject("expected result block missing")
    for key in ("status", "count_lower", "count_upper", "radical_rank", "complement_rank"):
        if expected.get(key) != result[key]:
            raise Reject(f"expected {key} mismatch")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text())
        result = verify(data)
        code = 0
    except Exception as exc:
        result = {"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
