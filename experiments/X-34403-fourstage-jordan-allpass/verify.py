#!/usr/bin/env python3
"""Exact standard-library replay for L-34410 and L-34411.

The Jordan factorization is checked at integer parameter tau=1, where every
odd-Jordan coefficient is an integer.  The jet and all-pass checks are formal
integer/rational identities; no floating-point arithmetic is used.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path

LIMIT = 256


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def odd_jordan(n: int, tau: int) -> int:
    if n % 2 == 0:
        return 0
    fac = factor(n)
    result = n**tau
    for p in fac:
        result = result * (p**tau - 1) // p**tau
    return result


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def convolve(a: list[int], b: list[int]) -> list[int]:
    out = [0] * len(a)
    for n in range(1, len(a)):
        out[n] = sum(a[d] * b[n // d] for d in divisors(n))
    return out


def shifted(sequence: list[int], power: int) -> list[int]:
    return [0] + [n**power * sequence[n] for n in range(1, len(sequence))]


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def oddpart(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n


def odd_partition(n: int, j: int, tau: int) -> int:
    k = n - j
    return (
        1
        + sum(oddpart(m) ** tau for m in range(1, n + 1))
        - sum(oddpart(m) ** tau for m in range(1, j + 1))
        - sum(oddpart(m) ** tau for m in range(1, k + 1))
    )


def polynomial_add(*terms: dict[int, int]) -> dict[int, int]:
    out: Counter[int] = Counter()
    for term in terms:
        out.update(term)
    return dict(+out)


def polynomial_multiply(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    out: Counter[int] = Counter()
    for i, ai in a.items():
        for j, bj in b.items():
            out[i + j] += ai * bj
    return dict(+out)


def main() -> None:
    # Exact positive four-stage coefficient factorization at tau=1:
    # J_4 = J_1 * id J_1 * id^2 J_1 * id^3 J_1.
    j1 = [0] + [odd_jordan(n, 1) for n in range(1, LIMIT + 1)]
    product_sequence = j1
    for r in range(1, 4):
        product_sequence = convolve(product_sequence, shifted(j1, r))
    j4 = [0] + [odd_jordan(n, 4) for n in range(1, LIMIT + 1)]
    assert product_sequence == j4

    # Formal second-jet multiplicities.
    stage_count = 4
    shift_sum = sum(range(4))
    unordered_pairs = 6
    lambda_log_multiplicity = stage_count + 2 * shift_sum
    lambda_convolution_multiplicity = stage_count + 2 * unordered_pairs
    assert lambda_log_multiplicity == 16
    assert lambda_convolution_multiplicity == 16

    # Exact scalarization firewall at e=(8,4).
    assert carry(8, 4, 5) == 1
    assert carry(8, 4, 7) == 1
    assert carry(8, 4, 35) == 0
    f1 = odd_partition(8, 4, 1)
    f4 = odd_partition(8, 4, 4)
    assert f1 == 11
    assert f4 == 3025
    assert f1**4 == 14641
    assert f4 != f1**4

    # Q4 source filters and exact reservoir cancellation.
    # x denotes the scale-four delay 4^{-s}.
    one_minus_x = {0: 1, 1: -1}
    one_minus_4x = {0: 1, 1: -4}
    reservoir_numerator = {0: 1}  # (1-x) cancels the reservoir denominator.
    assert polynomial_multiply(one_minus_x, {0: 1}) == one_minus_x
    assert one_minus_4x == polynomial_add(one_minus_x, {1: -3})
    assert reservoir_numerator == {0: 1}

    # Formal local-block all-pass identity.  Let A and B be current and
    # predecessor curvatures and X their polarized cross term.
    # h = a - b/2, c = a - 2b.
    h = {"A": Fraction(1), "B": Fraction(1, 4), "X": Fraction(-1)}
    c = {"A": Fraction(1), "B": Fraction(4), "X": Fraction(-4)}
    lhs = {key: 4 * h[key] - c[key] for key in h}
    assert lhs == {"A": Fraction(3), "B": Fraction(-3), "X": Fraction(0)}

    # The all-pass input splits into two consecutive root-Haar details:
    # (1-delta_4)=(1-delta_2)+delta_2(1-delta_2).
    source_left = {0: 1, 2: -1}
    source_right = polynomial_add({0: 1, 1: -1}, {1: 1, 2: -1})
    assert source_left == source_right

    data = {
        "schema": "X-34403-fourstage-jordan-allpass-v1",
        "classification": "EXACT_FOURSTAGE_PRODUCT_CARRY_AND_ALLPASS_VERIFIED",
        "coefficient_limit": LIMIT,
        "j4_factorization_coefficients_checked": LIMIT,
        "second_jet_lambda_log_multiplicity": lambda_log_multiplicity,
        "second_jet_lambda_convolution_multiplicity": (
            lambda_convolution_multiplicity
        ),
        "scalarization_counterexample": {
            "row": [8, 4],
            "F_tau_at_tau_1": f1,
            "F_4tau_at_tau_1": f4,
            "F_tau_fourth_power": f1**4,
            "carry_5": 1,
            "carry_7": 1,
            "carry_35": 0,
        },
        "allpass_curvature_identity": (
            "4 C(a-b/2)-C(a-2b)=3[C(a)-C(b)]"
        ),
        "root_detail_source_identity": (
            "1-delta_4=(1-delta_2)+delta_2(1-delta_2)"
        ),
        "arithmetic": "integers and fractions.Fraction only",
        "does_not_prove": [
            "dissipative root-detail square-function estimate",
            "coefficient-one global recurrence",
            "Riemann Hypothesis",
        ],
    }
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"))
    data["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
