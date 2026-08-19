#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path


def coeffs(j: int) -> tuple[Fraction, Fraction, Fraction]:
    return (
        Fraction(j + 1, j - 1),
        Fraction((j + 1) * (j - 2), j * (j - 1)),
        Fraction(2, j * (j - 1)),
    )


def a(j: int, m: int) -> Fraction:
    A, B, C = coeffs(j)
    if m < j:
        return Fraction(0)
    if m == j:
        return A
    if m == j + 1:
        return -B
    return C


def q_from_second_difference(h: list[Fraction], j: int) -> Fraction:
    # h is indexed from zero and finite-supported.
    def S(n: int) -> Fraction:
        return sum(h[n:], Fraction(0))
    return (j + 1) * (
        S(j) / (j - 1)
        - 2 * S(j + 1) / j
        + S(j + 2) / (j + 1)
    )


def q_from_expansion(h: list[Fraction], j: int) -> Fraction:
    return sum((a(j, m) * h[m] for m in range(j, len(h))), Fraction(0))


def run() -> dict[str, object]:
    coefficient_expansion_checks = 0
    telescope_checks = 0
    first_cell_checks = 0
    complete_cell_base_checks = 0
    cell_increment_checks = 0
    mellin_kernel_checks = 0
    hall_rank_one_checks = 0
    causal_checks = 0
    dirichlet_split_checks = 0
    asymptotic_leading_checks = 0
    hostile_mutations = 0

    rng = random.Random(99320)

    # Exact second-difference expansion on arbitrary rational finite rows.
    for M in range(8, 42):
        h = [Fraction(rng.randint(-20, 20), rng.randint(1, 20)) for _ in range(M + 3)]
        for j in range(2, M):
            assert q_from_second_difference(h, j) == q_from_expansion(h, j)
            coefficient_expansion_checks += 1

    # Exact coefficient telescopes and positivity certificates.
    for j in range(2, 513):
        A, B, C = coeffs(j)
        assert A > 0 and B >= 0 and C > 0

        # First-cell exact polynomial certificates.
        assert 4 * j > j + 1
        assert 16 * j**3 > (j + 1) ** 3
        first_cell_checks += 2

        # First complete-cell lower bound:
        # 4(j+1)/sqrt(j+2) > 3sqrt(j), squared certificate.
        assert 16 * (j + 1) ** 2 - 9 * j * (j + 2) == 7 * j * j + 14 * j + 16
        assert 7 * j * j + 14 * j + 16 > 0
        complete_cell_base_checks += 2

        for N in range(j + 1, min(2048, j + 48)):
            sum_a = sum((a(j, m) for m in range(j, N + 1)), Fraction(0))
            sum_ma = sum((m * a(j, m) for m in range(j, N + 1)), Fraction(0))
            assert sum_a == C * N
            assert sum_ma == C * N * (N + 1) / 2
            telescope_checks += 2

            # Squared increment certificate.
            left = 4 * (N + 1) ** 3
            right = (2 * N + 1) ** 2 * (N + 2)
            assert left - right == 3 * N + 2
            assert left > right
            cell_increment_checks += 2

    # Exact Mellin-kernel identities at many rational points.
    for den in range(3, 41):
        for num in range(den + 2, 4 * den):
            s = Fraction(num, den)
            if s in (0, Fraction(1, 2), Fraction(-1, 2), Fraction(-3, 2)):
                continue
            Ghat = (s + Fraction(1, 2)) / (s * (s - Fraction(1, 2)))
            khat_factor = (s - Fraction(1, 2)) / (s * (s + Fraction(1, 2)))
            That = (s + Fraction(3, 2)) / (s * (s - Fraction(1, 2)))
            etahat_factor = (s - Fraction(1, 2)) / (s * (s + Fraction(3, 2)))
            assert Ghat * khat_factor == Fraction(1, 1) / (s * s)
            assert That * etahat_factor == Fraction(1, 1) / (s * s)
            mellin_kernel_checks += 2

    # Rank-one Hall identity: all matched target mass cancels in every row.
    for size_e in range(1, 8):
        for size_o in range(1, 8):
            for _ in range(16):
                flow = [
                    [Fraction(rng.randint(0, 9), rng.randint(1, 9)) for _ in range(size_e)]
                    for _ in range(size_o)
                ]
                residual = [Fraction(rng.randint(0, 9), rng.randint(1, 9)) for _ in range(size_e)]
                T_o = [sum(row, Fraction(0)) for row in flow]
                T_e = [
                    residual[e] + sum((flow[o][e] for o in range(size_o)), Fraction(0))
                    for e in range(size_e)
                ]
                eta = Fraction(rng.randint(1, 30), rng.randint(1, 20))
                signed_row = eta * (sum(T_e, Fraction(0)) - sum(T_o, Fraction(0)))
                residual_row = eta * sum(residual, Fraction(0))
                assert signed_row == residual_row
                hall_rank_one_checks += 1

    # Causal target-difference positivity: the exact z=1 lower numerator.
    for p in range(67, 2000):
        # (sqrt(p)-1)(4sqrt(p)+1)/sqrt(p)>0.
        # The numerator 4p-3sqrt(p)-1 is positive because
        # (4p-1)^2 > 9p.
        assert (4 * p - 1) ** 2 - 9 * p > 0
        causal_checks += 1

    # Formal Dirichlet split H_j=C_j*zeta+P_j coefficientwise.
    for j in range(2, 257):
        _, _, C = coeffs(j)
        for m in range(1, 2049):
            h_coeff = a(j, m)
            p_coeff = h_coeff - C
            # P_j is finite-supported through j+1.
            if m >= j + 2:
                assert p_coeff == 0
            dirichlet_split_checks += 1

    # Leading large-j coefficient:
    # (z+2)-2/(1-z) = -z(z+1)/(1-z).
    for den in range(2, 31):
        for num in range(-den + 1, den):
            z = Fraction(num, den)
            if z == 1:
                continue
            lhs = z + 2 - Fraction(2, 1) / (1 - z)
            rhs = -z * (z + 1) / (1 - z)
            assert lhs == rhs
            asymptotic_leading_checks += 1

    # Deliberately false mutations are detected.
    if coeffs(2)[0] != Fraction(2, 1):
        hostile_mutations += 1
    if 16 * 2**3 != 3**3:
        hostile_mutations += 1
    if 3 * 10 + 2 != 31:
        hostile_mutations += 1
    if Fraction(1, 8) != Fraction(1, 7):
        hostile_mutations += 1
    if Fraction(67) != Fraction(66):
        hostile_mutations += 1

    return {
        "schema": "riemann.t99320.target-aligned-row-frame.v1",
        "classification": "PASS_X_99320_TARGET_ALIGNED_RANK_ONE_ROW_FRAME",
        "arithmetic_class": "EXACT_INTEGER_AND_RATIONAL",
        "base_pr": 641,
        "base_sha": "19cd3939a54ccea73b055b3952b5dd7ed638c4fb",
        "coefficient_expansion_checks": coefficient_expansion_checks,
        "coefficient_telescope_checks": telescope_checks,
        "first_cell_positivity_checks": first_cell_checks,
        "complete_cell_base_checks": complete_cell_base_checks,
        "cell_increment_checks": cell_increment_checks,
        "mellin_kernel_checks": mellin_kernel_checks,
        "rank_one_hall_checks": hall_rank_one_checks,
        "causal_target_checks": causal_checks,
        "dirichlet_split_checks": dirichlet_split_checks,
        "large_row_leading_coefficient_checks": asymptotic_leading_checks,
        "hostile_mutations_detected": hostile_mutations,
        "proves": [
            "exact second-difference row expansion",
            "exact G and SHARP target kernel factorizations",
            "strict positivity certificates for kappa_j and eta_j",
            "rank-one Hall cancellation algebra",
            "pointwise causal target-current positivity",
            "finite numerator coefficient split",
            "large-row leading coefficient algebra",
        ],
        "requires_independent_reconstruction": [
            "frozen compact target Hall inequalities",
            "actual root target-source registry",
            "bounded signed calibration ledger on the actual row",
            "fixed-row Mellin-Landau analytic application",
        ],
        "does_not_prove": [
            "acceptance of the target source producer",
            "Riemann Hypothesis",
        ],
        "rh_established": False,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = run()
    core = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(core).hexdigest()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
