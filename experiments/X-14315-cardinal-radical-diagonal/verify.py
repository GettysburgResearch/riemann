#!/usr/bin/env python3
"""Exact verifier for T-14306 finite-section cardinal/radical algebra."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

F = Fraction
Matrix = list[list[F]]


class VerificationError(ValueError):
    pass


def frac(x: Any) -> F:
    if isinstance(x, bool):
        raise VerificationError("booleans are not rational scalars")
    if isinstance(x, int):
        return F(x)
    if isinstance(x, str):
        try:
            return F(x)
        except (ValueError, ZeroDivisionError) as exc:
            raise VerificationError(f"invalid fraction: {x!r}") from exc
    raise VerificationError(f"unsupported rational scalar: {x!r}")


def matrix(x: Any, name: str) -> Matrix:
    if not isinstance(x, list) or not x or not all(isinstance(r, list) for r in x):
        raise VerificationError(f"{name} must be a nonempty matrix")
    width = len(x[0])
    if width == 0 or any(len(r) != width for r in x):
        raise VerificationError(f"{name} must be rectangular")
    return [[frac(v) for v in r] for r in x]


def shape(a: Matrix) -> tuple[int, int]:
    return len(a), len(a[0])


def zeros(n: int, m: int) -> Matrix:
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n: int) -> Matrix:
    a = zeros(n, n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def transpose(a: Matrix) -> Matrix:
    n, m = shape(a)
    return [[a[i][j] for i in range(n)] for j in range(m)]


def mm(a: Matrix, b: Matrix) -> Matrix:
    n, k = shape(a)
    k2, m = shape(b)
    if k != k2:
        raise VerificationError("matrix dimension mismatch")
    return [[sum((a[i][t] * b[t][j] for t in range(k)), F(0)) for j in range(m)] for i in range(n)]


def add(a: Matrix, b: Matrix) -> Matrix:
    if shape(a) != shape(b):
        raise VerificationError("matrix shape mismatch")
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def sub(a: Matrix, b: Matrix) -> Matrix:
    if shape(a) != shape(b):
        raise VerificationError("matrix shape mismatch")
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scale(c: F, a: Matrix) -> Matrix:
    return [[c * x for x in r] for r in a]


def hstack(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b):
        raise VerificationError("hstack row mismatch")
    return [ra + rb for ra, rb in zip(a, b)]


def is_zero(a: Matrix) -> bool:
    return all(x == 0 for r in a for x in r)


def equal(a: Matrix, b: Matrix, msg: str) -> None:
    if a != b:
        raise VerificationError(msg)


def inverse(a: Matrix) -> Matrix:
    n, m = shape(a)
    if n != m:
        raise VerificationError("inverse requires square matrix")
    ident = eye(n)
    aug = [a[i][:] + ident[i] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise VerificationError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            q = aug[r][col]
            if q:
                aug[r] = [x - q * y for x, y in zip(aug[r], aug[col])]
    return [r[n:] for r in aug]


def rank(a: Matrix) -> int:
    b = [r[:] for r in a]
    n, m = shape(b)
    row = 0
    for col in range(m):
        pivot = next((r for r in range(row, n) if b[r][col] != 0), None)
        if pivot is None:
            continue
        b[row], b[pivot] = b[pivot], b[row]
        p = b[row][col]
        b[row] = [x / p for x in b[row]]
        for r in range(n):
            if r != row and b[r][col] != 0:
                q = b[r][col]
                b[r] = [x - q * y for x, y in zip(b[r], b[row])]
        row += 1
        if row == n:
            break
    return row


def require_symmetric(a: Matrix, name: str) -> None:
    if a != transpose(a):
        raise VerificationError(f"{name} is not symmetric")


def ldl_positive(a: Matrix, name: str) -> list[F]:
    """Unpivoted exact LDL; the supplied certificate must be strictly positive."""
    require_symmetric(a, name)
    b = [r[:] for r in a]
    n, m = shape(b)
    if n != m:
        raise VerificationError(f"{name} must be square")
    pivots: list[F] = []
    for k in range(n):
        p = b[k][k]
        if p <= 0:
            raise VerificationError(f"{name} has nonpositive LDL pivot {p} at {k}")
        pivots.append(p)
        for i in range(k + 1, n):
            for j in range(i, n):
                b[j][i] -= b[i][k] * b[j][k] / p
                b[i][j] = b[j][i]
    return pivots


def fs(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def ms(a: Matrix) -> list[list[str]]:
    return [[fs(x) for x in r] for r in a]


def canonical_digest(obj: Any) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != "riemann.cardinal-radical-finite-section.v1":
        raise VerificationError("wrong schema")
    q = matrix(data["Q"], "Q")
    v = matrix(data["V"], "V")
    c = matrix(data["C"], "C")
    r = matrix(data["R"], "R")
    p = matrix(data["P"], "P")
    h = matrix(data["H"], "H")
    eps = frac(data["claimed_schur_floor_loss"])
    if eps <= 0:
        raise VerificationError("claimed loss must be positive")

    n, nq = shape(q)
    if n != nq:
        raise VerificationError("Q must be square")
    for name, a in [("C", c), ("R", r), ("H", h), ("P", p)]:
        if len(a) != n:
            raise VerificationError(f"{name} ambient dimension mismatch")
    if shape(p) != (n, n):
        raise VerificationError("P must be square")
    if shape(v)[1] != n:
        raise VerificationError("V ambient dimension mismatch")
    require_symmetric(q, "Q")

    kdim = shape(c)[1]
    mdim = shape(r)[1]
    equal(mm(v, c), eye(kdim), "V C != I")
    equal(mm(transpose(c), q), v, "C^T Q != V cardinal identity")
    if not is_zero(mm(q, r)):
        raise VerificationError("R is not in the exact radical")
    if not is_zero(mm(v, r)):
        raise VerificationError("V R != 0")

    a = mm(mm(v, p), c)
    ainv = inverse(a)
    ctilde = mm(mm(p, c), ainv)
    b = mm(mm(v, p), r)
    k = sub(mm(p, r), mm(ctilde, b))
    dc = sub(ctilde, c)
    e = sub(k, r)

    equal(mm(v, ctilde), eye(kdim), "repaired cardinal interpolation failed")
    if not is_zero(mm(v, k)):
        raise VerificationError("repaired radical packet is not in ker V")
    if rank(hstack(ctilde, k)) != kdim + mdim:
        raise VerificationError("repaired packet direct sum is rank deficient")

    lhs_cc = mm(mm(transpose(ctilde), q), ctilde)
    rhs_cc = add(eye(kdim), mm(mm(transpose(dc), q), dc))
    equal(lhs_cc, rhs_cc, "quadratic cardinal error identity failed")

    lhs_kk = mm(mm(transpose(k), q), k)
    rhs_kk = mm(mm(transpose(e), q), e)
    equal(lhs_kk, rhs_kk, "radical error identity failed")

    lhs_ck = mm(mm(transpose(ctilde), q), k)
    rhs_ck = mm(mm(transpose(dc), q), e)
    equal(lhs_ck, rhs_ck, "cardinal-radical cross identity failed")

    u = hstack(ctilde, k)
    low = mm(mm(transpose(u), q), u)
    comp = mm(mm(transpose(h), q), h)
    comp_pivots = ldl_positive(comp, "complement block")
    cross = mm(mm(transpose(h), q), u)
    schur = sub(low, mm(mm(transpose(cross), inverse(comp)), cross))
    gram = mm(transpose(u), u)
    moat = add(schur, scale(eps, gram))
    moat_pivots = ldl_positive(moat, "Schur floor moat")

    result = {
        "schema": data["schema"],
        "A": ms(a),
        "A_inverse": ms(ainv),
        "C_tilde": ms(ctilde),
        "K": ms(k),
        "Delta_C": ms(dc),
        "E": ms(e),
        "low_block": ms(low),
        "complement_block": ms(comp),
        "cross_block": ms(cross),
        "schur_corrected_low_block": ms(schur),
        "packet_gram": ms(gram),
        "claimed_schur_floor_loss": fs(eps),
        "complement_ldl_pivots": [fs(x) for x in comp_pivots],
        "floor_moat_ldl_pivots": [fs(x) for x in moat_pivots],
        "direct_sum_rank": rank(u),
        "verdict": "PASS",
    }
    result["proof_object_sha256"] = canonical_digest(result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate", type=Path)
    ap.add_argument("--output", type=Path)
    ns = ap.parse_args()
    data = json.loads(ns.certificate.read_text())
    result = verify(data)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if ns.output:
        ns.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
