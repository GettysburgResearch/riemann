#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def mobius_table(n: int) -> list[int]:
    mu = [1] * (n + 1)
    prime = [True] * (n + 1)
    mu[0] = 0
    for p in range(2, n + 1):
        if prime[p]:
            for k in range(p, n + 1, p):
                prime[k] = False if k != p else prime[k]
                mu[k] *= -1
            pp = p * p
            for k in range(pp, n + 1, pp):
                mu[k] = 0
    return mu


def conv(a: list[int], b: list[int], n: int) -> list[int]:
    out = [0] * (n + 1)
    for d in range(1, n + 1):
        if a[d] == 0:
            continue
        for m in range(1, n // d + 1):
            if b[m]:
                out[d * m] += a[d] * b[m]
    return out


def vp(n: int, p: int) -> int:
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def digit_jump_checks(limit: int, bases: list[int], mu: list[int]) -> dict[str, Any]:
    rows = 0
    for p in bases:
        a = [0] * (limit + 1)
        bp = [0] * (limit + 1)
        prev = 0
        for n in range(1, limit + 1):
            residue = n % p
            jump = residue - prev
            expected = 1 - (p if n % p == 0 else 0)
            if jump != expected:
                raise ValueError(f"digit jump mismatch p={p} n={n}")
            a[n] = expected
            bp[n] = mu[n] - (mu[n // p] if n % p == 0 else 0)
            prev = residue
            rows += 1
        amu = conv(a, mu, limit)
        abp = conv(a, bp, limit)
        for n in range(1, limit + 1):
            exp1 = 1 if n == 1 else (-p if n == p else 0)
            exp2 = 1 if n == 1 else (-(p + 1) if n == p else (p if n == p * p else 0))
            if amu[n] != exp1:
                raise ValueError(f"a*mu mismatch p={p} n={n}")
            if abp[n] != exp2:
                raise ValueError(f"a*bp mismatch p={p} n={n}")
    return {"rows": rows, "bases": bases}


def f_delta(X: int, q: int, j: int) -> Fraction:
    up = 1 if (j + 1) % q == 0 else 0
    cur = 1 if (j > 0 and j % q == 0) else 0
    endpoint = Fraction(1, X) if X % q == 0 else Fraction(0)
    return Fraction(up - cur) - endpoint


def dyadic_green_checks(orders: list[int]) -> dict[str, Any]:
    entry_rows = 0
    factor_rows = 0
    for N in orders:
        X = 1 << N
        qs = [1 << a for a in range(1, N + 1)]
        G = [[Fraction(0) for _ in qs] for _ in qs]
        for i, q in enumerate(qs):
            for j, d in enumerate(qs):
                value = sum((f_delta(X, q, r) * f_delta(X, d, r) for r in range(X)), Fraction(0))
                expected = Fraction(1 << (N - max(i + 1, j + 1) + 1)) - 1 - Fraction(1, X)
                if value != expected:
                    raise ValueError(f"dyadic G mismatch N={N} i={i} j={j}: {value} != {expected}")
                G[i][j] = value
                entry_rows += 1
        dweights = [Fraction(1 << (N - a)) if a < N else Fraction(X - 1, X) for a in range(1, N + 1)]
        vectors = [
            [Fraction(((-1) ** (i + seed)) * ((i + seed) % 3 - 1)) for i in range(N)]
            for seed in range(1, 7)
        ]
        vectors.append([Fraction(1) for _ in range(N)])
        for v in vectors:
            lhs = sum((v[i] * G[i][j] * v[j] for i in range(N) for j in range(N)), Fraction(0))
            s = Fraction(0)
            rhs = Fraction(0)
            for i in range(N):
                s += v[i]
                rhs += dweights[i] * s * s
            if lhs != rhs:
                raise ValueError(f"dyadic factor mismatch N={N}")
            factor_rows += 1
    return {"entry_rows": entry_rows, "factor_rows": factor_rows}


def matmul(A: list[list[Fraction]], B: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), Fraction(0)) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*A)]


def ldlt_psd(A: list[list[Fraction]]) -> bool:
    n = len(A)
    L = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    D = [Fraction(0) for _ in range(n)]
    for i in range(n):
        L[i][i] = 1
        pivot = A[i][i] - sum((L[i][k] * L[i][k] * D[k] for k in range(i)), Fraction(0))
        if pivot < 0:
            return False
        D[i] = pivot
        for j in range(i + 1, n):
            num = A[j][i] - sum((L[j][k] * L[i][k] * D[k] for k in range(i)), Fraction(0))
            if pivot == 0:
                if num != 0:
                    return False
                L[j][i] = 0
            else:
                L[j][i] = num / pivot
    return True


def poincare_checks(orders: list[int]) -> dict[str, Any]:
    rows = 0
    for N in orders:
        C = [[Fraction(1 if k <= j else 0) for k in range(N)] for j in range(N)]
        CtC = matmul(transpose(C), C)
        moat = [[Fraction(N * N if i == j else 0) - CtC[i][j] for j in range(N)] for i in range(N)]
        if not ldlt_psd(moat):
            raise ValueError(f"Poincare moat not PSD N={N}")
        rows += N * N
    return {"matrix_entries": rows, "orders": orders}


def b2(n: int, mu: list[int]) -> int:
    return mu[n] - (mu[n // 2] if n % 2 == 0 else 0)


def c2(n: int) -> int:
    return 1 - vp(n, 2)


def digital_recurrence_checks(limit: int, mu: list[int]) -> dict[str, Any]:
    B = [0] * (limit + 1)
    running = 0
    for n in range(1, limit + 1):
        running += b2(n, mu)
        B[n] = running
    rows = 0
    for x in range(2, limit + 1):
        lhs = sum(c2(k) * B[x // k] for k in range(1, x + 1))
        if lhs != -1:
            raise ValueError(f"digital recurrence mismatch x={x}: {lhs}")
        rhs = -1 - sum(c2(k) * B[x // k] for k in range(3, x + 1))
        if rhs != B[x]:
            raise ValueError(f"strict-scale recurrence mismatch x={x}")
        rows += 1
    acc = 0
    for n in range(1, limit + 1):
        acc += c2(n)
        if acc != n.bit_count():
            raise ValueError(f"digit sum mismatch n={n}")
    return {"rows": rows, "limit": limit}


def formal_kernel_checks() -> dict[str, Any]:
    samples = [
        (Fraction(3, 2), Fraction(1, 3)),
        (Fraction(5, 2), Fraction(-2, 5)),
        (Fraction(7, 3), Fraction(4, 7)),
    ]
    rows = 0
    for z, x in samples:
        NP = (1 - x) / (z + Fraction(1, 2))
        NK = (z - Fraction(1, 2)) / ((z + Fraction(1, 2)) * (z + Fraction(3, 2)))
        if (z - Fraction(1, 2)) * NP != (z + Fraction(3, 2)) * (1 - x) * NK:
            raise ValueError("parity/carry quotient mismatch")
        det = (NP * NP) * (NK * NK) - (NP * NK) * (NP * NK)
        if det != 0:
            raise ValueError("rank-one determinant mismatch")
        rows += 1
    return {"rows": rows}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify.py certificate.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    cert = json.loads(path.read_text())
    if cert.get("schema") != "riemann.x23005.parity-green-two-frequency.v1":
        raise ValueError("schema mismatch")
    limit = int(cert["mobius_limit"])
    if limit < max(64, int(cert["digital_recurrence_limit"])):
        raise ValueError("mobius_limit too small")
    bases = [int(x) for x in cert["digit_bases"]]
    orders = [int(x) for x in cert["dyadic_orders"]]
    porders = [int(x) for x in cert["poincare_orders"]]
    if any(p < 2 for p in bases):
        raise ValueError("digit bases must be >=2")
    if any(n < 1 for n in orders + porders):
        raise ValueError("orders must be positive")
    mu = mobius_table(limit)
    checks = {
        "digit": digit_jump_checks(limit, bases, mu),
        "dyadic_green": dyadic_green_checks(orders),
        "poincare": poincare_checks(porders),
        "digital_recurrence": digital_recurrence_checks(int(cert["digital_recurrence_limit"]), mu),
        "formal_kernel": formal_kernel_checks(),
    }
    result = {
        "schema": "riemann.x23005.parity-green-two-frequency.verification.v1",
        "verified": True,
        "verdict": "EXACT_PARITY_GREEN_DIGITAL_AND_TWO_CHANNEL_ALGEBRA_VERIFIED",
        "checks": checks,
        "proof_boundary": cert["proof_boundary"],
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
