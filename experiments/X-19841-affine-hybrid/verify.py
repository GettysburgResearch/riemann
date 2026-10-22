#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path


def F(x: str) -> Fraction:
    return Fraction(x)


def canonical_digest(obj: object) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def gram(vectors):
    return matmul(vectors, transpose(vectors))


def sub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def diag(values):
    n = len(values)
    return [[values[i] if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def ldl_psd(a):
    n = len(a)
    L = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    d = [Fraction(0) for _ in range(n)]
    for j in range(n):
        d[j] = a[j][j] - sum(L[j][k] * L[j][k] * d[k] for k in range(j))
        if d[j] < 0:
            return False, d
        if d[j] == 0:
            for i in range(j + 1, n):
                residual = a[i][j] - sum(L[i][k] * L[j][k] * d[k] for k in range(j))
                if residual != 0:
                    return False, d
            continue
        for i in range(j + 1, n):
            L[i][j] = (
                a[i][j] - sum(L[i][k] * L[j][k] * d[k] for k in range(j))
            ) / d[j]
    return True, d


def main(path: str) -> int:
    cert = json.loads(Path(path).read_text())
    vectors = [[F(x) for x in row] for row in cert["residual_vectors"]]
    D = gram(vectors)
    n = len(D)
    I = diag([Fraction(1)] * n)
    sigma = F(cert["sigma"])
    cminus = F(cert["c_minus"])
    cupper = F(cert["target_upper_coefficient"])
    gap = F(cert["gap_floor"])
    P = diag([F(x) for x in cert["extra_psd_diag"]])
    Q = add(scale(sigma, I), add(scale(cminus, D), P))

    complement = [row[1:] for row in D[1:]]
    comp_ok, comp_pivots = ldl_psd(
        sub(complement, diag([gap] * (n - 1)))
    )

    affine_remainder = sub(sub(Q, scale(sigma, I)), scale(cminus, D))
    affine_ok, affine_pivots = ldl_psd(affine_remainder)

    target_energy = D[0][0]
    target_excess = Q[0][0] - sigma
    target_ok = target_excess <= cupper * target_energy
    separation_ok = cupper * target_energy < cminus * gap

    verdict = (
        "PASS_AFFINE_HYBRID_EXACT"
        if comp_ok and affine_ok and target_ok and separation_ok
        else "FAIL"
    )
    result = {
        "schema": "riemann.x19841-affine-hybrid.result.v1",
        "verdict": verdict,
        "certificate_sha256": canonical_digest(cert),
        "target_energy": str(target_energy),
        "target_excess": str(target_excess),
        "complement_gap_floor": str(gap),
        "affine_lower_coefficient": str(cminus),
        "target_upper_coefficient": str(cupper),
        "separation_margin": str(cminus * gap - cupper * target_energy),
        "complement_ldl_pivots": [str(x) for x in comp_pivots],
        "affine_remainder_ldl_pivots": [str(x) for x in affine_pivots],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if verdict.startswith("PASS") else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py certificate.json")
    raise SystemExit(main(sys.argv[1]))
