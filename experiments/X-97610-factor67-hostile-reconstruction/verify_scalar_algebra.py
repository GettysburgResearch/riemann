#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def matadd(A, B, sign=1):
    return [[A[i][j] + sign * B[i][j] for j in range(len(A))] for i in range(len(A))]


def ident(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="results/scalar_algebra_verification.json")
    args = ap.parse_args()

    # Row dictionaries from the canonical component formula.
    q2 = {2: Fraction(3), 3: Fraction(0), 4: Fraction(1), 5: Fraction(1)}
    q3 = {2: Fraction(0), 3: Fraction(2), 4: Fraction(-2, 3), 5: Fraction(1, 3)}
    qstar = {n: 5 * q2[n] + 3 * q3[n] for n in q2}
    assert qstar == {2: 15, 3: 6, 4: 3, 5: 6}

    # Polynomial factorization after writing x=2^{-z} and y=3^{-z}.
    # 5 P2 + 3 P3 has reciprocal-zeta numerator
    # -3(1-x)(2-x) = -6 + 9x - 3x^2.
    numerator_coeff = [Fraction(-6), Fraction(9), Fraction(-3)]
    factor_coeff = [Fraction(-3) * 2, Fraction(-3) * (-3), Fraction(-3)]
    assert numerator_coeff == factor_coeff

    # Exact causal identities for symbolic rational stand-ins r_i. These check
    # only the algebraic split, not source faithfulness.
    rs = [Fraction(1, 9), Fraction(1, 11), Fraction(1, 13)]
    s = Fraction(1)
    lambdas = []
    alphas = []
    for r in rs:
        lam = r * s
        lambdas.append(lam)
        alphas.append(r * lam)
        s *= 1 - r
    assert s + sum(lambdas) == 1
    # Coefficient of each formal child in lambda(P-rA child)+alpha A child.
    assert all(-lam * r + alpha == 0 for r, lam, alpha in zip(rs, lambdas, alphas))

    # Exact finite positive-operator identity on a nontrivial nilpotent T.
    T = [
        [Fraction(0), Fraction(1, 5), Fraction(1, 7), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1, 6), Fraction(1, 9)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1, 8)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
    ]
    I = ident(4)
    T2 = matmul(T, T)
    T4 = matmul(T2, T2)
    assert T4 == [[Fraction(0) for _ in range(4)] for _ in range(4)]
    inv_even = matadd(I, T2)  # (I-T^2)^-1 = I+T^2 here because T^4=0.
    lhs = matmul(matadd(I, T, sign=-1), inv_even)
    # Direct finite Neumann inverse I-T+T^2-T^3.
    T3 = matmul(T2, T)
    rhs = matadd(matadd(matadd(I, T, sign=-1), T2), T3, sign=-1)
    assert lhs == rhs
    assert matmul(matadd(I, T), rhs) == I

    result = {
        "schema": "riemann.x97610.scalar-algebra.v1",
        "classification": "PASS_FACTOR67_SCALAR_AND_OPERATOR_ALGEBRA",
        "qstar": {str(k): str(v) for k, v in qstar.items()},
        "tail_qstar": "6",
        "scalar_numerator": "-3*(1-2^-z)*(2-2^-z)",
        "causal_parent_mass": str(s + sum(lambdas)),
        "causal_formal_child_coefficients": [str(-lam*r+a) for r,lam,a in zip(rs,lambdas,alphas)],
        "operator_identity": "(I+T)^-1=(I-T)(I-T^2)^-1",
        "operator_identity_exact": True,
        "source_faithfulness_proved_by_this_script": False,
        "RH_established": False,
    }
    raw = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(raw).hexdigest()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
