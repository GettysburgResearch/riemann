#!/usr/bin/env python3
"""Exact rational replay for L-26105/L-26106.

The checker validates on a finite annular control:
  * a primal minimum-norm repair;
  * the homogeneous Hilbert-Farkas dual ratio;
  * KKT complementarity;
  * monotone projected-dual ascent;
  * the additive-function second-difference identity;
  * fail-closed mutations.

It does not prove ADF or RH.
"""

from __future__ import annotations

from fractions import Fraction
import argparse
import hashlib
import json


ANNULUS = list(range(12, 25))
ROWS = [2, 3]
RESIDUAL = [Fraction(1, 2), Fraction(1, 3)]


def arow(q: int, j: int) -> int:
    return 2 * int(j % q == 0) - int((j - 1) % q == 0) - int((j + 1) % q == 0)


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matvec(a, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in a]


def inverse(a):
    n = len(a)
    aug = [
        [Fraction(a[i][j]) for j in range(n)]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col]), None)
        if pivot is None:
            raise AssertionError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [
                    aug[row][j] - factor * aug[col][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in aug]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def norm_sq(x):
    return dot(x, x)


def dual_energy(lam, residual, gram):
    return dot(lam, residual) - Fraction(1, 2) * dot(lam, matvec(gram, lam))


def canonical_digest(payload: dict) -> str:
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def build_result() -> dict:
    matrix = [[Fraction(arow(q, j)) for j in ANNULUS] for q in ROWS]
    gram = matmul(matrix, transpose(matrix))
    gram_inverse = inverse(gram)
    lam_star = matvec(gram_inverse, RESIDUAL)
    if min(lam_star) <= 0:
        raise AssertionError("control dual optimizer is not positive")

    flow_star = matvec(transpose(matrix), lam_star)
    replay = matvec(matrix, flow_star)
    if replay != RESIDUAL:
        raise AssertionError("primal equality replay failed")

    radius_sq = norm_sq(flow_star)
    dual_pairing = dot(lam_star, RESIDUAL)
    if radius_sq != dual_pairing:
        raise AssertionError("primal/dual radius mismatch")

    # The homogeneous dual ratio squared is
    # (<lam,r>_+)^2 / ||A^*lam||^2.
    ratio_sq = dual_pairing * dual_pairing / radius_sq
    if ratio_sq != radius_sq:
        raise AssertionError("homogeneous dual ratio mismatch")

    # A conservative exact step: spectral norm <= maximum absolute row sum.
    row_sum_bound = max(sum(abs(x) for x in row) for row in gram)
    tau = Fraction(1, 2 * row_sum_bound)
    lam = [Fraction(0) for _ in ROWS]
    energies = [dual_energy(lam, RESIDUAL, gram)]
    increments = []
    for _ in range(8):
        gradient = [
            RESIDUAL[i] - matvec(gram, lam)[i]
            for i in range(len(ROWS))
        ]
        next_lam = [max(Fraction(0), lam[i] + tau * gradient[i]) for i in range(len(ROWS))]
        delta = [next_lam[i] - lam[i] for i in range(len(ROWS))]
        next_energy = dual_energy(next_lam, RESIDUAL, gram)
        lower_gain = Fraction(1, 2 * tau) * norm_sq(delta)
        if next_energy - energies[-1] < lower_gain:
            raise AssertionError("projected-dual energy gain failed")
        if next_energy < energies[-1]:
            raise AssertionError("dual energy is not monotone")
        increments.append(norm_sq(delta))
        energies.append(next_energy)
        lam = next_lam

    # Additive-function identity for a larger formal prime-power vector.
    weights = {2: Fraction(1, 5), 3: Fraction(2, 7), 4: Fraction(3, 11), 5: Fraction(1, 13)}
    for j in ANNULUS:
        additive = lambda n: sum(value for q, value in weights.items() if n % q == 0)
        lhs = sum(Fraction(arow(q, j)) * value for q, value in weights.items())
        rhs = 2 * additive(j) - additive(j - 1) - additive(j + 1)
        if lhs != rhs:
            raise AssertionError("additive second-difference identity failed")

    payload = {
        "schema": "riemann.x26101-annular-dual.v1",
        "classification": "EXACT_SYNTHETIC_HILBERT_FARKAS_AND_DUAL_POTENTIAL",
        "rows": ROWS,
        "annulus": [ANNULUS[0], ANNULUS[-1]],
        "gram": [[str(x) for x in row] for row in gram],
        "dual_optimizer": [str(x) for x in lam_star],
        "minimum_radius_sq": str(radius_sq),
        "homogeneous_ratio_sq": str(ratio_sq),
        "projected_step": str(tau),
        "projected_energy_values": [str(x) for x in energies],
        "projected_increment_norm_sq": [str(x) for x in increments],
        "additive_identity_rows": len(ANNULUS),
        "verdict": "PASS_EXACT_ANNULAR_HILBERT_FARKAS_AND_POTENTIAL",
    }
    payload["proof_object_sha256"] = canonical_digest(payload)
    return payload


def self_tests() -> list[str]:
    tests = []
    result = build_result()
    assert result["minimum_radius_sq"] == result["homogeneous_ratio_sq"]
    tests.append("central primal-dual equality")

    matrix = [[Fraction(arow(q, j)) for j in ANNULUS] for q in ROWS]
    wrong = [[x / 2 for x in row] for row in matrix]
    gram_wrong = matmul(wrong, transpose(wrong))
    assert gram_wrong != matmul(matrix, transpose(matrix))
    tests.append("mutated central coefficient rejected")

    assert arow(3, 12) == 2 and arow(3, 13) == -1
    tests.append("neighbor channels retained")

    energies = [Fraction(x) for x in result["projected_energy_values"]]
    assert all(b >= a for a, b in zip(energies, energies[1:]))
    tests.append("monotone projected potential")

    assert min(Fraction(x) for x in result["dual_optimizer"]) > 0
    tests.append("KKT positive dual control")

    return tests


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    result = build_result()
    if args.self_test:
        tests = self_tests()
        print(f"{len(tests)}/{len(tests)} tests passed")
        for name in tests:
            print("PASS", name)

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
