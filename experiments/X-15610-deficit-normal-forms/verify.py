#!/usr/bin/env python3
"""Exact Fraction-only regression for L-15624 and L-15625."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F


def det2(matrix: list[list[F]]) -> F:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def fj(value: F) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def main() -> int:
    # Packet-adapted Schur completion.
    G = F(3)
    alpha = F(0)
    Gamma = F(2)
    t = F(1, 2)
    A = [[F(0), F(1, 10)], [F(1, 10), F(2)]]
    D = [[F(4), F(-1, 10)], [F(-1, 10), F(2)]]

    K = G - A[0][0]
    X = A[1][0]
    D_sharp = [
        [K, -X],
        [-X, D[1][1] + X * X / K],
    ]
    R_sharp = [
        [
            A[i][j] + D_sharp[i][j] - (G if i == j else F(0))
            for j in range(2)
        ]
        for i in range(2)
    ]

    assert K > 0
    assert D_sharp[0][0] > 0 and det2(D_sharp) > 0
    assert R_sharp[0][0] == 0
    assert R_sharp[0][1] == R_sharp[1][0] == 0
    assert R_sharp[1][1] > 0

    beta_squared = X * X
    clipping_upper = (4 * alpha * alpha + beta_squared) / (Gamma - alpha)

    # Here D_sharp-(G-Gamma)I is positive definite, so the clipped operator is
    # exactly this shifted matrix and its Q-compression is the lower-right row.
    theta = G - Gamma
    E_shift = [
        [
            D_sharp[i][j] - (theta if i == j else F(0))
            for j in range(2)
        ]
        for i in range(2)
    ]
    assert E_shift[0][0] > 0 and det2(E_shift) > 0
    uncaptured_clipped_trace = E_shift[1][1]
    four_defect_upper = uncaptured_clipped_trace + clipping_upper + 2 * alpha
    assert four_defect_upper < Gamma - t
    assert A[1][1] >= Gamma

    # Exact spectral-deficit normal form: one pass and one additional-low-mode
    # failure.  All matrices are diagonal, so functional calculus is rational.
    G2 = F(3)
    Gamma2 = F(2)
    t2 = F(1)

    A_pass = [F(0), F(0), F(5, 2), F(4)]
    D_sp_pass = [max(G2 - value, F(0)) for value in A_pass]
    E_pass = [max(value - (G2 - Gamma2), F(0)) for value in D_sp_pass]
    assert E_pass == [max(Gamma2 - value, F(0)) for value in A_pass]
    pass_uncaptured = sum(E_pass[2:], F(0))
    assert pass_uncaptured == 0
    assert pass_uncaptured < Gamma2 - t2

    A_fail = [F(0), F(0), F(1, 2), F(4)]
    D_sp_fail = [max(G2 - value, F(0)) for value in A_fail]
    E_fail = [max(value - (G2 - Gamma2), F(0)) for value in D_sp_fail]
    fail_uncaptured = sum(E_fail[2:], F(0))
    assert fail_uncaptured == F(3, 2)
    assert fail_uncaptured > Gamma2 - t2

    result = {
        "schema": "riemann.x15610-deficit-normal-forms.v1",
        "packet_adapted": {
            "D_sharp": [[fj(value) for value in row] for row in D_sharp],
            "R_sharp": [[fj(value) for value in row] for row in R_sharp],
            "cross_beta_squared": fj(beta_squared),
            "clipping_upper": fj(clipping_upper),
            "uncaptured_clipped_trace": fj(uncaptured_clipped_trace),
            "four_defect_upper": fj(four_defect_upper),
            "gap": fj(Gamma - t),
            "classification": "EXACT_PACKET_ADAPTED_COMPLETION_PASSES",
        },
        "spectral_normal_form": {
            "pass_uncaptured_trace": fj(pass_uncaptured),
            "extra_low_uncaptured_trace": fj(fail_uncaptured),
            "gap": fj(Gamma2 - t2),
            "classification": "EXACT_EXTRA_LOW_MODE_IS_ONLY_REMAINING_DEFECT",
        },
        "verdict": "PASS_EXACT_L15624_L15625_REGRESSION",
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["proof_object_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
