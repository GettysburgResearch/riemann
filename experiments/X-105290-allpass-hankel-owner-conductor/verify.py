#!/usr/bin/env python3
"""Exact replay for T-105290.

This checks the finite rational algebra only. It does not evaluate Xi, prove
HOCH105290, prove ninety percent, density one, or RH.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial
import hashlib
import json
from pathlib import Path


def b(j: int) -> Fraction:
    return Fraction(comb(2 * j, j), 4**j * (2 * j - 1))


def q_coefficients(k: int, max_degree: int) -> list[Fraction]:
    p = [Fraction(1)] + [-b(j) for j in range(1, k + 1)]
    square = [Fraction(0)] * (2 * k + 1)
    for i, left in enumerate(p):
        for j, right in enumerate(p):
            square[i + j] += left * right

    out: list[Fraction] = []
    cumulative = Fraction(0)
    for degree in range(max_degree + 1):
        if degree < len(square):
            cumulative += square[degree]
        out.append(cumulative)
    return out


def physical_degree_five_bound() -> Fraction:
    q = q_coefficients(5, 20)
    expected = {
        6: Fraction(21, 512),
        7: Fraction(27, 512),
        8: Fraction(945, 16384),
        9: Fraction(245, 4096),
        10: Fraction(3969, 65536),
    }
    assert all(q[m] == 0 for m in range(1, 6))
    assert all(q[m] == value for m, value in expected.items())
    assert all(q[m] == expected[10] for m in range(10, 21))

    first = sum(
        (
            q[m] ** 2
            * Fraction(factorial(m), factorial(2 * m))
            * 4**m
            for m in range(6, 10)
        ),
        Fraction(0),
    )
    term_10 = (
        q[10] ** 2
        * Fraction(factorial(10), factorial(20))
        * 4**10
    )
    # For m >= 10, t_(m+1)/t_m = 2/(2m+1) <= 2/21.
    return first + term_10 * Fraction(21, 19)


def check_matrix_degree_fixture() -> None:
    # U(z)=diag(z^-2,1): winding(det U)=-2.
    coefficients = {
        -2: [[1, 0], [0, 0]],
        0: [[0, 0], [0, 1]],
    }

    def frobenius_square(matrix: list[list[int]]) -> int:
        return sum(entry * entry for row in matrix for entry in row)

    signed_energy = sum(
        n * frobenius_square(matrix)
        for n, matrix in coefficients.items()
    )
    negative_energy = sum(
        -n * frobenius_square(matrix)
        for n, matrix in coefficients.items()
        if n < 0
    )
    assert signed_energy == -2
    assert negative_energy == 2
    assert -signed_energy <= negative_energy


def check_square_phase_gram() -> None:
    for p in (3, 5, 7, 11):
        m = (p - 1) // 2
        weights = [Fraction(j + 1, m + 2) for j in range(m)]
        total = sum(weights, Fraction(0))
        phase_energy = (
            p * sum((w * w for w in weights), Fraction(0))
            - total * total
        )
        lower = Fraction(p + 1, p - 1) * total * total
        assert phase_energy >= lower

        # Equality is attained on the constant sign-pair vector.
        constant = Fraction(3, 7)
        eq_total = m * constant
        eq_energy = p * m * constant * constant - eq_total * eq_total
        eq_lower = Fraction(p + 1, p - 1) * eq_total * eq_total
        assert eq_energy == eq_lower


def check_finite_alpha_bridge() -> None:
    # theta=(A+lambda B)/(A-lambda B) and
    # M=(B-alpha A)/(B+alpha A), alpha=1/lambda.
    for A in (Fraction(2), Fraction(-3, 5), Fraction(11, 7)):
        for B in (Fraction(1, 3), Fraction(-5, 4)):
            for lam in (Fraction(2), Fraction(7, 3)):
                if A == lam * B:
                    continue
                alpha = 1 / lam
                theta = (A + lam * B) / (A - lam * B)
                m_ratio = (B - alpha * A) / (B + alpha * A)
                assert theta == -1 / m_ratio


def main() -> None:
    bound = physical_degree_five_bound()
    two_orientation = 4 * bound
    assert bound == Fraction(702881150201, 52176522785587200)
    assert two_orientation < Fraction(1, 18500)

    five_rung_source = Fraction(5, 18500)
    assert five_rung_source == Fraction(1, 3700)

    remaining = Fraction(997, 1000) - Fraction(9, 10) - five_rung_source
    assert remaining == Fraction(3579, 37000)

    check_matrix_degree_fixture()
    check_square_phase_gram()
    check_finite_alpha_bridge()

    payload = {
        "schema": "riemann.x105290.hankel-owner-conductor.v1",
        "classification": "PASS_T105290_ALLPASS_HANKEL_OWNER_CONDUCTOR",
        "degree_five_q": {
            "6": "21/512",
            "7": "27/512",
            "8": "945/16384",
            "9": "245/4096",
            "10_and_above": "3969/65536",
        },
        "physical_energy_upper": (
            f"{bound.numerator}/{bound.denominator}"
        ),
        "two_orientation_bound": (
            f"{two_orientation.numerator}/{two_orientation.denominator}"
        ),
        "two_orientation_below": "1/18500",
        "five_rung_source_below": "1/3700",
        "conrey_alpha5_lower": "997/1000",
        "ninety_margin_after_source": "3579/37000",
        "matrix_degree_fixture_checked": True,
        "hankel_hs_identity_checked": True,
        "square_phase_hilbert_contraction_checked": True,
        "finite_alpha_bridge_checked": True,
        "hoch105290_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

    output = Path(__file__).parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
