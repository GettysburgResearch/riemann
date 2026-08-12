#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable, List, Tuple

Q = Fraction


def matmul(a: List[List[Q]], b: List[List[Q]]) -> List[List[Q]]:
    bt = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def matadd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def diag(v: Iterable[Q]) -> List[List[Q]]:
    v = list(v)
    return [[v[i] if i == j else Q(0) for j in range(len(v))] for i in range(len(v))]


def inv_diag(a: List[List[Q]]) -> List[List[Q]]:
    return [[1/a[i][i] if i == j else Q(0) for j in range(len(a))] for i in range(len(a))]


def canonical_digest(payload: dict) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def moment(atoms: List[Tuple[Q, Q]], k: int) -> Q:
    return sum(p * (y ** k) for p, y in atoms)


def integral_exp_pair(y1: Q, y2: Q, ri: int, rj: int) -> Q:
    n = ri + rj
    d = ri - rj
    sqrt_prod = _rational_sqrt(y1 * y2)
    sqrt_ratio = _rational_sqrt(y1 / y2)
    pref = sqrt_ratio ** d
    return pref * (sqrt_prod ** n - sqrt_prod ** (-n)) / Q(n)


def _rational_sqrt(x: Q) -> Q:
    import math
    an = math.isqrt(x.numerator)
    ad = math.isqrt(x.denominator)
    if an * an != x.numerator or ad * ad != x.denominator:
        raise ValueError(f"not a rational square: {x}")
    return Q(an, ad)


def beta_expect_monomial(k: int) -> Q:
    if k % 2:
        return Q(0)
    return Q(3, 2) * (Q(1, k + 1) - Q(1, k + 3))


def verify() -> dict:
    checks = 0

    # Exact Cayley anticommutator congruence.
    rs = [Q(2), Q(3), Q(5), Q(8)]
    ds = [Q(1, 2), Q(2, 3), Q(3, 5), Q(5, 8)]
    ls = [(1-d)/(1+d) for d in ds]
    C = [[1/(ri+rj) for rj in rs] for ri in rs]
    D = diag(ds)
    L = diag(ls)
    invIplusL = inv_diag(diag([1+x for x in ls]))
    lhs = matsub(C, matmul(matmul(D, C), D))
    rhs = matmul(matmul(invIplusL, [[2*x for x in row] for row in matadd(matmul(L, C), matmul(C, L))]), invIplusL)
    if lhs != rhs:
        raise AssertionError("Cayley anticommutator identity failed")
    checks += len(rs) ** 2

    # Exact Mellin-symmetric two-copy reflection identity.
    atoms = [(Q(1, 4), Q(4)), (Q(1, 4), Q(1, 4)), (Q(1, 4), Q(9)), (Q(1, 4), Q(1, 9))]
    for k in range(-6, 7):
        if moment(atoms, k) != moment(atoms, -k):
            raise AssertionError("synthetic law is not Mellin-symmetric")
        checks += 1

    a = 1
    rvals = [2, 3, 4]
    coeffs = [Q(2), Q(-3), Q(1)]
    K = []
    for ri in rvals:
        row = []
        for rj in rvals:
            val = (moment(atoms, ri+a)*moment(atoms, rj+a)
                   - moment(atoms, ri-a)*moment(atoms, rj-a)) / Q(ri+rj)
            row.append(val)
        K.append(row)
    q_direct = sum(coeffs[i]*coeffs[j]*K[i][j] for i in range(3) for j in range(3))

    q_reflect = Q(0)
    for p1, y1 in atoms:
        for p2, y2 in atoms:
            prod = y1*y2
            sinh_aS = (prod**a - prod**(-a))/2
            inner = Q(0)
            for i, ri in enumerate(rvals):
                for j, rj in enumerate(rvals):
                    inner += coeffs[i]*coeffs[j]*integral_exp_pair(y1, y2, ri, rj)
            q_reflect += p1*p2*sinh_aS*inner
    if q_direct != q_reflect:
        raise AssertionError(f"two-copy reflection identity failed: {q_direct} != {q_reflect}")
    checks += len(atoms) ** 2 * len(rvals) ** 2

    for r in rvals:
        ell_ratio = (moment(atoms, r+a)-moment(atoms, r-a))/(moment(atoms, r+a)+moment(atoms, r-a))
        num = sum(p*(y**r)*(y**a-y**(-a))/2 for p, y in atoms)
        den = sum(p*(y**r)*(y**a+y**(-a))/2 for p, y in atoms)
        if ell_ratio != num/den:
            raise AssertionError("impedance regression identity failed")
        checks += 1

    # Beta(2,2) Stein identity through degree 12.
    for k in range(0, 13):
        left = beta_expect_monomial(k+1)
        right = Q(k, 4) * (beta_expect_monomial(k-1) - beta_expect_monomial(k+1)) if k else Q(0)
        if left != right:
            raise AssertionError(f"Beta Stein identity failed at degree {k}")
        checks += 1

    samples = [(Q(3), Q(5)), (Q(7, 2), Q(11, 3)), (Q(13, 5), Q(17, 7))]
    for x, y in samples:
        g = x+y
        u = x/g
        v = 2*u-1
        if g*(1+v)/2 != x or g*(1-v)/2 != y:
            raise AssertionError("beta-gamma reconstruction failed")
        checks += 2

    # Theta Gibbs variance and supersymmetric-potential algebra.
    probs = [Q(1, 6), Q(1, 3), Q(1, 2)]
    ys = [Q(2), Q(4), Q(7)]
    mean = sum(p*y for p, y in zip(probs, ys))
    mean2 = sum(p*y*y for p, y in zip(probs, ys))
    var = mean2-mean*mean
    aa = mean-Q(1, 4)
    aprime = mean-var
    mu1 = 4*aa*aa-4*aprime-Q(1, 4)
    mu2 = 4*(aa-Q(5, 4))*(aa+Q(1, 4))+4*var
    pair = 2*sum(probs[i]*probs[j]*(ys[i]-ys[j])**2 for i in range(3) for j in range(3))
    if mu1 != mu2 or pair != 4*var:
        raise AssertionError("theta variance/SUSY algebra failed")
    checks += 2

    result = {
        "schema": "riemann.brownian-theta-passive-network.v1",
        "checks": checks,
        "cayley_dimension": len(rs),
        "synthetic_atoms": len(atoms),
        "reflection_quadratic": str(q_direct),
        "beta_stein_max_degree": 12,
        "theta_mean": str(mean),
        "theta_variance": str(var),
        "theta_mu": str(mu1),
        "verdict": "PASS_BROWNIAN_THETA_PASSIVE_NETWORK",
    }
    result["proof_object_sha256"] = canonical_digest(result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = verify()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
