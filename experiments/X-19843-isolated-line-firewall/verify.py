#!/usr/bin/env python3
"""Exact replay for R-19848 and L-19867's finite algebra."""

from fractions import Fraction
import json


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def poly_mul(p, q):
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return out


def poly_add(p, q):
    n = max(len(p), len(q))
    out = [Fraction(0)] * n
    for i, x in enumerate(p):
        out[i] += x
    for i, x in enumerate(q):
        out[i] += x
    return out


def main():
    A = [
        [Fraction(0), Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(0)],
    ]
    nodes = [Fraction(-1), Fraction(0), Fraction(1)]
    b = [Fraction(-1), Fraction(0), Fraction(1)]
    diag = [Fraction(0), Fraction(2), Fraction(0)]

    for i in range(3):
        assert A[i][i] == diag[i]
        for j in range(3):
            if i != j:
                assert A[i][j] == (b[i] - b[j]) / (nodes[i] - nodes[j])

    odd = [Fraction(1), Fraction(0), Fraction(-1)]
    target = [Fraction(1), Fraction(-1), Fraction(1)]
    upper = [Fraction(1), Fraction(2), Fraction(1)]
    assert matvec(A, odd) == [-x for x in odd]
    assert matvec(A, target) == [Fraction(0)] * 3
    assert matvec(A, upper) == [3 * x for x in upper]
    assert dot(odd, target) == dot(upper, target) == dot(odd, upper) == 0

    # P(z)=sum_i xi_i product_{j != i}(z-d_j), coefficients ascending.
    P = [Fraction(0)]
    for i, coeff in enumerate(target):
        term = [Fraction(1)]
        for j, node in enumerate(nodes):
            if i != j:
                term = poly_mul(term, [-node, Fraction(1)])
        term = [coeff * x for x in term]
        P = poly_add(P, term)
    assert P == [Fraction(1), Fraction(0), Fraction(1)]

    # Generic residual-Gram control for L-19867.
    m = Fraction(1, 16)
    C = [Fraction(2), Fraction(3)]
    bb = [Fraction(1, 4), Fraction(1, 4)]
    theta = sum(bb[i] * bb[i] / C[i] for i in range(2))
    assert theta == Fraction(5, 96)
    assert theta <= m
    target_residual_sq = m * m + theta
    assert target_residual_sq <= m + m * m

    result = {
        "verdict": "PASS_ISOLATED_INTERIOR_CCM_FIREWALL",
        "ccm_divided_difference": True,
        "eigenvalues": [-1, 0, 3],
        "target_residual": "0",
        "orthogonal_singular_moat": "1",
        "transform_numerator": ["1", "0", "1"],
        "nonreal_roots": ["+i", "-i"],
        "residual_gram_theta": str(theta),
        "residual_gram_target_bound": str(m + m * m),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
