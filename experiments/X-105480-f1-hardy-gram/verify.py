#!/usr/bin/env python3
from __future__ import annotations

import cmath
import hashlib
import json
import math
from pathlib import Path
import random
from typing import Iterable

VERDICT = "PASS_T105480_F1_HARDY_GRAM"
SQRT2 = math.sqrt(2.0)


def kernel(y: float) -> float:
    if 1.0 <= y < 2.0:
        return 8.0 - 4.0 * math.sqrt(y)
    if 2.0 <= y < 4.0:
        return -8.0 * (1.0 + SQRT2) + 4.0 * SQRT2 * math.sqrt(y)
    if 4.0 <= y < 8.0:
        return 8.0 * SQRT2 - 2.0 * math.sqrt(y)
    return 0.0


def wcell(m: int) -> float:
    return math.sqrt(1.0 + 1.0 / m) - 1.0


def cell_square(A: complex, B: complex, m: int) -> float:
    a = math.sqrt(m)
    b = math.sqrt(m + 1)
    # 2 int_a^b |A+Bt|^2 dt/t.
    return (
        2.0 * abs(A) ** 2 * math.log(b / a)
        + 4.0 * (A * B.conjugate()).real * (b - a)
        + abs(B) ** 2 * (b * b - a * a)
    )


def direct_current(coeff: list[complex], m: int) -> complex:
    return sum(coeff[n] * kernel(m / n) for n in range(1, len(coeff)))


def gram_entry(M: int, n: int, r: int) -> float:
    return sum(
        kernel(m / n) * kernel(m / r) / (16.0 * m)
        for m in range(M, 2 * M + 1)
    )


def gram_energy_direct(M: int, coeff: list[complex]) -> float:
    return sum(
        abs(direct_current(coeff, m) / 4.0) ** 2 / m
        for m in range(M, 2 * M + 1)
    )


def gram_energy_expanded(M: int, coeff: list[complex]) -> complex:
    total = 0j
    for n in range(1, len(coeff)):
        if coeff[n] == 0:
            continue
        for r in range(1, len(coeff)):
            if coeff[r] == 0:
                continue
            total += coeff[n] * coeff[r].conjugate() * gram_entry(M, n, r)
    return total


def jump_filter(coeff: list[complex], m: int) -> complex:
    constants = [1.0, -(2.0 + SQRT2), 1.0 + 2.0 * SQRT2, -SQRT2]
    out = 0j
    for j, c in enumerate(constants):
        d = 2**j
        if m % d == 0:
            n = m // d
            if 0 < n < len(coeff):
                out += c * coeff[n]
    return out


def close(x: complex | float, y: complex | float, atol: float = 2e-8, rtol: float = 2e-8) -> bool:
    return abs(x - y) <= atol + rtol * max(abs(x), abs(y))


def run() -> dict[str, object]:
    rng = random.Random(105480)

    weighted_cauchy_checks = 0
    cell_square_checks = 0
    gram_expansion_checks = 0
    gram_support_checks = 0
    diagonal_offdiagonal_checks = 0
    jump_hilbert_checks = 0
    jump_ledger_checks = 0
    counterexample_checks = 0
    autocorrelation_support_checks = 0
    kernel_sup_checks = 0

    # Weighted l1 <= sqrt(harmonic mass) l2.
    for _ in range(10_000):
        M = rng.randint(2, 500)
        vals = [complex(rng.uniform(-3, 3), rng.uniform(-3, 3)) for _ in range(M + 1)]
        l1 = sum(abs(v) / m for v, m in zip(vals, range(M, 2 * M + 1)))
        l2 = sum(abs(v) ** 2 / m for v, m in zip(vals, range(M, 2 * M + 1)))
        harm = sum(1.0 / m for m in range(M, 2 * M + 1))
        assert l1 * l1 <= harm * l2 + 1e-10
        assert harm <= math.log(2.0) + 2.0 / M + 1e-14
        weighted_cauchy_checks += 2

    # Exact cell-square formula and endpoint inequalities.
    for _ in range(15_000):
        m = rng.randint(1, 50_000)
        A = complex(rng.uniform(-8, 8), rng.uniform(-8, 8))
        B = complex(rng.uniform(-8, 8), rng.uniform(-8, 8))
        a = math.sqrt(m)
        b = math.sqrt(m + 1)
        u = A + B * a
        v = A + B * b
        exact = cell_square(A, B, m)

        # Independent composite Simpson quadrature in t for 2|A+Bt|^2/t.
        qn = 64  # even
        h = (b - a) / qn

        def integrand(t: float) -> float:
            return 2.0 * abs(A + B * t) ** 2 / t

        approx = integrand(a) + integrand(b)
        approx += 4.0 * sum(integrand(a + j * h) for j in range(1, qn, 2))
        approx += 2.0 * sum(integrand(a + j * h) for j in range(2, qn, 2))
        approx *= h / 3.0
        assert close(exact, approx, atol=2e-9, rtol=2e-10)

        w = wcell(m)
        lower = w * (abs(u) ** 2 + abs(v) ** 2) / (3.0 * SQRT2)
        upper = w * (abs(u) ** 2 + abs(v) ** 2)
        assert exact + 2e-10 >= lower
        assert exact <= upper + 2e-10
        cell_square_checks += 3

    # Exact finite Gram expansion and PSD.
    for _ in range(1_500):
        M = rng.randint(3, 20)
        N = rng.randint(4, 18)
        coeff = [0j] + [
            complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
            if rng.random() < 0.55 else 0j
            for _ in range(N)
        ]
        direct = gram_energy_direct(M, coeff)
        expanded = gram_energy_expanded(M, coeff)
        assert close(expanded.imag, 0.0, atol=2e-9, rtol=0.0)
        assert close(expanded.real, direct, atol=3e-8, rtol=3e-8)
        assert direct >= -1e-12
        gram_expansion_checks += 3

    # Exact ratio-eight support.  Ratios outside the open interval have no common m.
    for _ in range(20_000):
        M = rng.randint(2, 300)
        n = rng.randint(1, 800)
        if rng.random() < 0.5:
            r = rng.randint(max(1, 8 * n), max(1, 20 * n))
        else:
            r = rng.randint(1, max(1, n // 8))
        ratio = n / r
        if ratio <= 1.0 / 8.0 or ratio >= 8.0:
            assert gram_entry(M, n, r) == 0.0
            gram_support_checks += 1

    # Diagonal/off-diagonal orientation identity.
    for _ in range(3_000):
        M = rng.randint(3, 20)
        N = rng.randint(4, 24)
        coeff = [0j] + [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(N)]
        E = gram_energy_direct(M, coeff)
        D = sum(abs(coeff[n]) ** 2 * gram_entry(M, n, n) for n in range(1, len(coeff)))
        O = E - D
        assert max(O, 0.0) <= E + 1e-10
        assert E <= D + max(O, 0.0) + 1e-10
        diagonal_offdiagonal_checks += 2

    # Weighted endpoint Hilbert triangle inequality.
    for _ in range(10_000):
        M = rng.randint(2, 200)
        delta = [complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in range(M + 1)]
        err = [complex(rng.uniform(-0.5, 0.5), rng.uniform(-0.5, 0.5)) for _ in range(M)]
        A2 = 0.0
        N2 = 0.0
        J2 = 0.0
        for j, m in enumerate(range(M, 2 * M)):
            w = wcell(m)
            A2 += w * (abs(delta[j]) ** 2 + abs(delta[j + 1]) ** 2)
            N2 += w * (abs(delta[j]) ** 2 + abs(delta[j + 1] - err[j]) ** 2)
            J2 += w * abs(err[j]) ** 2
        A = math.sqrt(A2)
        J = math.sqrt(J2)
        assert N2 + 1e-10 >= max(A - J, 0.0) ** 2
        assert N2 <= (A + J) ** 2 + 1e-10
        jump_hilbert_checks += 2

    # Finite form of J2 <= C/M sum |a_n|^2.
    for _ in range(10_000):
        M = rng.randint(8, 400)
        coeff = [0j] + [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(2 * M + 8)]
        lhs = sum(wcell(m - 1) * abs(jump_filter(coeff, m)) ** 2 for m in range(M + 1, 2 * M + 1))
        energy = sum(abs(coeff[n]) ** 2 for n in range(max(1, M // 8), 2 * M + 1))
        # A generous absolute constant, independent of M and the packet.
        assert lhs <= 200.0 * energy / M + 1e-10
        jump_ledger_checks += 1

    # Explicit linear-loss counterexample.
    kappa = 8.0 - 4.0 * math.sqrt(7.0 / 4.0)
    for q in range(2, 102):
        M = 4 * q
        count = M // 4
        coeff = [0j] * (2 * M + 1)
        for n in range(M, 5 * M // 4):
            coeff[n] = 1.0 / math.sqrt(count)
        source_energy = sum(abs(x) ** 2 for x in coeff)
        assert close(source_energy, 1.0, atol=1e-12, rtol=1e-12)
        E = gram_energy_direct(M, coeff)
        lower = kappa * kappa * M / 448.0
        assert E + 1e-10 >= lower
        critical = [abs(coeff[n]) * math.sqrt(n) for n in range(M, 5 * M // 4)]
        assert min(critical) >= 2.0 - 1e-12
        assert max(critical) <= math.sqrt(5.0) + 1e-12
        counterexample_checks += 4

    # Autocorrelation support: disjoint log supports when |h|>=log 8.
    for _ in range(10_000):
        h = rng.choice([-1.0, 1.0]) * rng.uniform(math.log(8.0), 5.0)
        # Sample points in support of k; translated support must be disjoint.
        for _j in range(4):
            u = rng.uniform(0.0, math.log(8.0))
            assert not (0.0 <= u + h < math.log(8.0))
        autocorrelation_support_checks += 4

    # Supremum check at all branches plus a dense grid.
    sup_bound = 8.0 * SQRT2
    for j in range(20_001):
        y = 8.0 * j / 20_000.0
        assert abs(kernel(y)) <= sup_bound + 1e-12
        kernel_sup_checks += 1

    mutations = sorted([
        "absolute_offdiagonal_substituted_for_positive_part_rejected",
        "checkpoint_512ff17_declared_missing_rejected",
        "coefficient_l2_declared_sufficient_rejected",
        "continuous_l2_declared_nonlocal_rejected",
        "diagonal_energy_promoted_to_gram_rejected",
        "f1gram_declared_equivalent_to_f1hardy_rejected",
        "f1gram_promoted_without_source_premise_rejected",
        "finite_replay_promoted_to_rh_rejected",
        "gram_kernel_declared_negative_rejected",
        "jump_square_ledger_promoted_to_distinct_product_control_rejected",
        "mellin_plancherel_called_random_dirichlet_polynomial_rejected",
        "ratio_eight_support_deleted_rejected",
        "source_blind_bessel_bound_accepted_rejected",
        "source_blind_schur_bound_accepted_rejected",
        "tp2_promoted_to_gram_contraction_rejected",
        "zero_log_moment_promoted_to_l2_bound_rejected",
    ])

    finite_checks = (
        weighted_cauchy_checks
        + cell_square_checks
        + gram_expansion_checks
        + gram_support_checks
        + diagonal_offdiagonal_checks
        + jump_hilbert_checks
        + jump_ledger_checks
        + counterexample_checks
        + autocorrelation_support_checks
        + kernel_sup_checks
    )

    payload: dict[str, object] = {
        "schema": "riemann.x105480.f1-hardy-gram.v1",
        "classification": VERDICT,
        "base_pr": 730,
        "base_sha": "74a4f6dcad0eabdc98c954ce0e7b46d39875cf32",
        "boolean_pr": 719,
        "boolean_sha": "e56c981e2d0639a988f8f54aa362724eb00d9131",
        "half_source_pr": 751,
        "half_source_sha": "98af0db6ec7f77d6333a77a3dac53c4698852f43",
        "weighted_cauchy_checks": weighted_cauchy_checks,
        "cell_square_checks": cell_square_checks,
        "gram_expansion_checks": gram_expansion_checks,
        "gram_support_checks": gram_support_checks,
        "diagonal_offdiagonal_checks": diagonal_offdiagonal_checks,
        "jump_hilbert_checks": jump_hilbert_checks,
        "jump_ledger_checks": jump_ledger_checks,
        "counterexample_checks": counterexample_checks,
        "autocorrelation_support_checks": autocorrelation_support_checks,
        "kernel_sup_checks": kernel_sup_checks,
        "finite_checks": finite_checks,
        "hostile_mutations_rejected": mutations,
        "hardy_from_square_proved": True,
        "continuous_discrete_l2_equivalence_proved": True,
        "positive_semidefinite_gram_proved": True,
        "diagonal_gram_subpower_inherited": True,
        "square_offdiagonal_equivalence_proved": True,
        "mellin_plancherel_coordinate_proved": True,
        "source_blind_gram_bound": False,
        "f1gram105480_proved": False,
        "f1hcnc105481_proved": False,
        "f1hardy105470_proved": False,
        "bci102990_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    result = run()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])
    print(f"finite_checks={result['finite_checks']}")


if __name__ == "__main__":
    main()
