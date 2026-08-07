#!/usr/bin/env python3
"""Exact regression for the centered Heath-Brown / scale-contraction proposal.

Standard library only. This is a finite algebra checker, not a Riemann-data
certificate and not a proof of the open centered packet estimate CP(K).
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Tuple

Vector = Tuple[int, ...]


def primes_up_to(n: int) -> List[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for q in range(p * p, n + 1, p):
                sieve[q] = False
    return [i for i, ok in enumerate(sieve) if ok]


def factor_exponents(n: int, primes: List[int]) -> Vector:
    out = []
    x = n
    for p in primes:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        out.append(e)
    if x != 1:
        raise ValueError(f"prime basis too short for {n}")
    return tuple(out)


def mobius(n: int, primes: List[int]) -> int:
    exps = factor_exponents(n, primes)
    if any(e > 1 for e in exps):
        return 0
    return -1 if sum(exps) % 2 else 1


def vec_add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))


def vec_scale(c: int, a: Vector) -> Vector:
    return tuple(c * x for x in a)


def zero_vec(dim: int) -> Vector:
    return (0,) * dim


def conv_scalar(a: List[int], b: List[int], limit: int) -> List[int]:
    out = [0] * (limit + 1)
    for d in range(1, limit + 1):
        if a[d] == 0:
            continue
        for e in range(1, limit // d + 1):
            if b[e]:
                out[d * e] += a[d] * b[e]
    return out


def conv_vector(
    a: List[int], b: List[Vector], limit: int, dim: int
) -> List[Vector]:
    out = [zero_vec(dim) for _ in range(limit + 1)]
    for d in range(1, limit + 1):
        if a[d] == 0:
            continue
        for e in range(1, limit // d + 1):
            if b[e] != zero_vec(dim):
                out[d * e] = vec_add(out[d * e], vec_scale(a[d], b[e]))
    return out


def hb_identity(K: int, V: int) -> Dict[str, object]:
    X = V**K
    primes = primes_up_to(X)
    dim = len(primes)
    mu = [0] * (X + 1)
    mu_v = [0] * (X + 1)
    one = [0] + [1] * X
    logv = [zero_vec(dim) for _ in range(X + 1)]
    for n in range(1, X + 1):
        mu[n] = mobius(n, primes)
        if n <= V:
            mu_v[n] = mu[n]
        logv[n] = factor_exponents(n, primes)

    lhs = conv_vector(mu, logv, X, dim)
    rhs = [zero_vec(dim) for _ in range(X + 1)]
    mu_power = [0] * (X + 1)
    mu_power[1] = 1
    one_power = [0] * (X + 1)
    one_power[1] = 1
    row_digests = []

    for j in range(1, K + 1):
        mu_power = conv_scalar(mu_power, mu_v, X)
        if j > 1:
            one_power = conv_scalar(one_power, one, X)
        row = conv_vector(mu_power, logv, X, dim)
        if j > 1:
            tmp = [zero_vec(dim) for _ in range(X + 1)]
            for d in range(1, X + 1):
                if one_power[d] == 0:
                    continue
                for e in range(1, X // d + 1):
                    if row[e] != zero_vec(dim):
                        tmp[d * e] = vec_add(
                            tmp[d * e], vec_scale(one_power[d], row[e])
                        )
            row = tmp
        coeff = ((-1) ** (j - 1)) * math.comb(K, j)
        for n in range(1, X + 1):
            rhs[n] = vec_add(rhs[n], vec_scale(coeff, row[n]))
        row_digests.append(
            hashlib.sha256(repr((j, coeff, row)).encode()).hexdigest()
        )

    mismatches = [n for n in range(1, X + 1) if lhs[n] != rhs[n]]
    return {
        "K": K,
        "V": V,
        "X": X,
        "prime_basis_size": dim,
        "mismatches": mismatches,
        "row_digests": row_digests,
        "sample_lambda_vectors": {
            str(n): list(lhs[n]) for n in [2, 4, 6, 12, X] if n <= X
        },
    }


def matmul(
    A: List[List[Fraction]], B: List[List[Fraction]]
) -> List[List[Fraction]]:
    return [
        [
            sum(A[i][k] * B[k][j] for k in range(len(B)))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]


def transpose(A: List[List[Fraction]]) -> List[List[Fraction]]:
    return [list(row) for row in zip(*A)]


def qform(
    v: List[Fraction], K: List[List[Fraction]], w: List[Fraction]
) -> Fraction:
    return sum(
        v[i] * K[i][j] * w[j]
        for i in range(len(v))
        for j in range(len(w))
    )


def null_quotient_check() -> Dict[str, object]:
    B = [
        [Fraction(1), Fraction(-2), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(-2), Fraction(1)],
    ]
    K = matmul(transpose(B), B)
    n0 = [Fraction(1), Fraction(1), Fraction(1), Fraction(1)]
    n1 = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
    rows = [
        [Fraction(2), Fraction(-1), Fraction(0), Fraction(3)],
        [Fraction(-1), Fraction(4), Fraction(1), Fraction(-2)],
        [Fraction(0), Fraction(1), Fraction(-3), Fraction(2)],
    ]
    companions = [
        [2 * n0[i] - n1[i] for i in range(4)],
        [-n0[i] + 3 * n1[i] for i in range(4)],
        [4 * n0[i] + 2 * n1[i] for i in range(4)],
    ]
    centered = [
        [rows[a][i] - companions[a][i] for i in range(4)]
        for a in range(3)
    ]
    total = [sum(row[i] for row in rows) for i in range(4)]
    direct = qform(total, K, total)
    recombined = sum(
        qform(centered[a], K, centered[b])
        for a in range(3)
        for b in range(3)
    )
    energies = [qform(v, K, v) for v in centered]
    cauchy_bound = len(rows) * sum(energies)
    return {
        "null_n0": str(qform(n0, K, n0)),
        "null_n1": str(qform(n1, K, n1)),
        "direct": str(direct),
        "recombined": str(recombined),
        "row_energies": [str(x) for x in energies],
        "finite_vector_bound": str(cauchy_bound),
        "bound_pass": direct <= cauchy_bound,
    }


def scale_system_check() -> Dict[str, object]:
    max_j = 90
    E = [[0] * (max_j + 1) for _ in range(3)]
    for j in range(1, max_j + 1):
        cutoff = (2 * j) // 3
        prev = max(E[h][k] for h in range(3) for k in range(cutoff + 1))
        E[0][j] = (j + 1) ** 2 + (j + 1) * prev
        E[1][j] = (j + 1) ** 3 + (2 * j + 1) * prev
        E[2][j] = (j + 1) ** 4 + (3 * j + 1) * prev
    ratios = []
    for j in [30, 45, 60, 75, 90]:
        m = max(E[h][j] for h in range(3))
        ratios.append(
            {"J": j, "digits": len(str(m)), "log_over_J": repr(math.log(m) / j)}
        )
    return {
        "delta": "1/3",
        "components": 3,
        "max_J": max_j,
        "tail_ratios": ratios,
        "last_values": [str(E[h][max_j]) for h in range(3)],
    }


def build_result() -> Dict[str, object]:
    hb = hb_identity(3, 4)
    nq = null_quotient_check()
    sc = scale_system_check()
    verdict = (
        not hb["mismatches"]
        and nq["null_n0"] == "0"
        and nq["null_n1"] == "0"
        and nq["direct"] == nq["recombined"]
        and nq["bound_pass"]
    )
    core = {
        "schema": "X-15125-v1",
        "classification": "EXACT_ALGEBRAIC_REGRESSION_ONLY",
        "heath_brown": hb,
        "null_quotient": nq,
        "scale_system": sc,
        "verdict": "PASS" if verdict else "FAIL",
        "proof_boundary": (
            "Checks the exact finite Heath-Brown identity on a symbolic "
            "completely-additive log basis, the rowwise null-mode quotient, "
            "and a synthetic scale-contraction system. It does not prove the "
            "open centered packet estimate CP(K)."
        ),
    }
    digest_payload = json.dumps(
        core, sort_keys=True, separators=(",", ":")
    ).encode()
    core["proof_sha256"] = hashlib.sha256(digest_payload).hexdigest()
    return core


def main() -> int:
    result = build_result()
    if len(sys.argv) == 2:
        expected = json.loads(Path(sys.argv[1]).read_text())
        if expected != result:
            print(json.dumps(result, indent=2, sort_keys=True))
            return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
