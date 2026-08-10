#!/usr/bin/env python3
"""Exact regressions for L-90301--L-90304 and R-90301.

Standard-library only. The finite exhaustive loops verify algebraic identities;
the cofinal analytic estimates remain in the markdown proofs.
"""
from fractions import Fraction
from itertools import product
import hashlib, json
from pathlib import Path


def outer(x, y):
    return [[x[i] * y[j] for j in range(2)] for i in range(2)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def scale(c, A):
    return [[c * A[i][j] for j in range(2)] for i in range(2)]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def tr(A):
    return A[0][0] + A[1][1]


def frob2(A):
    return sum(A[i][j] * A[i][j] for i in range(2) for j in range(2))


def wedge(x, y):
    return x[0] * y[1] - x[1] * y[0]


def curvature(v, a, b):
    return add(outer(a, a), scale(Fraction(-1, 2), add(outer(v, b), outer(b, v))))


def main():
    vals = (-2, -1, 0, 1, 2)
    determinant_rows = 0
    trace_rows = 0
    for coords in product(vals, repeat=6):
        v = [Fraction(coords[0]), Fraction(coords[1])]
        a = [Fraction(coords[2]), Fraction(coords[3])]
        b = [Fraction(coords[4]), Fraction(coords[5])]
        K = curvature(v, a, b)
        rhs = wedge(v, a) * wedge(a, b) - Fraction(1, 4) * wedge(v, b) ** 2
        assert det(K) == rhs
        determinant_rows += 1
        assert frob2(K) - tr(K) ** 2 == -2 * det(K)
        trace_rows += 1

    relative_rows = 0
    for E, I, Y, R, T in product(vals, repeat=5):
        v = [Fraction(1), Fraction(Y)]
        a = [Fraction(E), Fraction(I)]
        b = [Fraction(E * E - R), Fraction(T)]
        K = curvature(v, a, b)
        D = Fraction(I - Y * E)
        C = Fraction(T - 2 * E * I + Y * (E * E + R))
        assert det(K) == R * D * D - Fraction(1, 4) * C * C
        M = [[Fraction(1), Fraction(0)], [-Fraction(Y), Fraction(1)]]
        Kc = mm(mm(M, K), transpose(M))
        assert Kc == [[Fraction(R), -C / 2], [-C / 2, D * D]]
        relative_rows += 1

    # L-90304: when Y=0 and H=R-E^2>0, the unknown-current
    # quadratic has an exact current-independent maximum T^2/(4H).
    completion_rows = 0
    for R in range(1, 6):
        for E in vals:
            H = R - E * E
            if H <= 0:
                continue
            for I, T in product(vals, repeat=2):
                lhs = Fraction((T - 2 * E * I) ** 2, 4 * R) - I * I
                rhs = (
                    Fraction(T * T, 4 * H)
                    - Fraction(H, R)
                    * (Fraction(I) + Fraction(T * E, 2 * H)) ** 2
                )
                assert lhs == rhs
                assert lhs <= Fraction(T * T, 4 * H)
                completion_rows += 1

    # Exact Q=4 all-pass cross-multiplication at many rational x.
    # phi(s)=(1/2)(x-4)/(x-1), phi(1-s)=2(x-1)/(x-4).
    allpass_rows = 0
    for num in range(-100, 101):
        for den in range(1, 18):
            x = Fraction(num, den)
            if x in (1, 4):
                continue
            p = Fraction(1, 2) * (x - 4) / (x - 1)
            q = 2 * (x - 1) / (x - 4)
            assert p * q == 1
            allpass_rows += 1

    result = {
        "schema": "X-90301-inertia-defect-v3",
        "classification": "PASS_EXACT_TWO_STATE_INERTIA_WRONSKIAN_IDENTITIES",
        "real_integer_wronskian_rows": determinant_rows,
        "trace_frobenius_determinant_rows": trace_rows,
        "relative_q4_square_vs_reserve_rows": relative_rows,
        "zero_bare_current_independent_completion_rows": completion_rows,
        "q4_allpass_rational_rows": allpass_rows,
        "proof_boundary": (
            "finite exact algebra only; analytic O(n/log n) theorem is in L-90304; "
            "no global Q4 recurrence and no RH conclusion"
        ),
    }
    raw = json.dumps(result, sort_keys=True, indent=2) + "\n"
    result["sha256_without_digest"] = hashlib.sha256(raw.encode()).hexdigest()
    out = json.dumps(result, sort_keys=True, indent=2) + "\n"
    path = Path(__file__).with_name("results") / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(out, encoding="utf-8")
    print(out, end="")


if __name__ == "__main__":
    main()
