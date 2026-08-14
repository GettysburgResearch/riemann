#!/usr/bin/env python3
"""Exact Fraction replay for L-92204."""
from fractions import Fraction as F
from itertools import combinations, permutations
import json
from pathlib import Path


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def determinant(A):
    n = len(A)
    total = F(0)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = F(-1 if inversions % 2 else 1)
        for i in range(n):
            term *= A[i][perm[i]]
        total += term
    return total


def reciprocal_coefficients(A, length):
    B = [F(0)] * length
    B[0] = F(1) / A[0]
    for n in range(1, length):
        B[n] = -sum(A[k] * B[n - k] for k in range(1, n + 1)) / A[0]
    return B


# A deliberately non-Stieltjes but positive-at-the-base formal series.
A = [F(7, 3), F(5, 2), F(11, 4), F(13, 5), F(17, 6), F(19, 7), F(23, 8), F(29, 9), F(31, 10)]
B = reciprocal_coefficients(A, len(A))

max_error = F(0)
determinant_errors = []
for n in range(1, 5):
    HA = [[A[i + j + 1] for j in range(n)] for i in range(n)]
    HB = [[B[i + j + 1] for j in range(n)] for i in range(n)]
    T = [[B[i - j] if i >= j else F(0) for j in range(n)] for i in range(n)]
    D = [[F((-1) ** i) if i == j else F(0) for j in range(n)] for i in range(n)]
    L = [[F((-1) ** (i + j + 1)) * HB[i][j] for j in range(n)] for i in range(n)]
    RHS = matmul(matmul(matmul(D, T), HA), matmul(transpose(T), D))
    for i in range(n):
        for j in range(n):
            max_error = max(max_error, abs(L[i][j] - RHS[i][j]))
    det_error = determinant(L) - determinant(HA) / (A[0] ** (2 * n))
    determinant_errors.append(det_error)
    assert det_error == 0
assert max_error == 0

# Finite squared-pole Cauchy-Binet control.
t = F(3, 2)
poles = [(F(2), F(5)), (F(3), F(7)), (F(5), F(11)), (F(7), F(17)), (F(11), F(23))]
for n in range(1, 5):
    moments = [sum(w / (t + s) ** (k + 1) for w, s in poles) for k in range(2 * n)]
    H = [[moments[i + j + 1] for j in range(n)] for i in range(n)]
    subset_sum = F(0)
    for subset in combinations(poles, n):
        numerator = F(1)
        denominator = F(1)
        weight = F(1)
        for w, s in subset:
            weight *= w
            denominator *= (t + s) ** (2 * n)
        for i in range(n):
            for j in range(i + 1, n):
                numerator *= (subset[i][1] - subset[j][1]) ** 2
        subset_sum += weight * numerator / denominator
    assert determinant(H) == subset_sum

result = {
    "status": "PASS_RECIPROCAL_LOEWNER_HANKEL",
    "maximum_congruence_error": str(max_error),
    "determinant_errors": [str(x) for x in determinant_errors],
    "orders_checked": [1, 2, 3, 4],
    "cauchy_binet_poles": [[str(w), str(s)] for w, s in poles],
}
out = Path(__file__).resolve().parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
print(result["status"])
print(json.dumps(result, indent=2, sort_keys=True))
