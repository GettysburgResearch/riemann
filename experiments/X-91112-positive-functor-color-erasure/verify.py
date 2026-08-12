#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


def ceil_fraction(x: Fraction) -> int:
    return -((-x.numerator) // x.denominator)


def beta_bar(n: int, q: Fraction) -> Fraction:
    M = n + 1
    a = ceil_fraction(Fraction(M, 1) / q) - 1
    if a < 0:
        a = 0
    return Fraction(a * ((a + 1) * q - M), M)


def verify() -> dict:
    affine_checks = 0
    nonmultiple_checks = 0

    for n in range(80):
        for m in (2, 3, 5, 7, 11, 67, 71):
            N = m * (n + 1) - 1
            for Q in range(1, min(400, N + 20)):
                lhs = beta_bar(N, Fraction(Q, 1))
                rhs = beta_bar(n, Fraction(Q, m))
                assert lhs == rhs, (n, m, Q, lhs, rhs)
                affine_checks += 1
                if Q % m:
                    nonmultiple_checks += 1

    # Synthetic branch sums. Each branch port has
    # [[V,B],[B,V]] >= (1/9)V I, while the correction uses tau=1/10.
    # Positive physical-column weights are exact beta_bar values.
    port_checks = 0
    for Q in range(1, 120):
        V_total = Fraction(0)
        B_total = Fraction(0)
        correction_total = Fraction(0)

        for index, (n, m) in enumerate(
            ((2, 67), (3, 71), (5, 73), (8, 79), (13, 83))
        ):
            physical_weight = beta_bar(m * (n + 1) - 1, Fraction(Q, 1))
            V = Fraction(index + 1, 17) * physical_weight
            ratio = Fraction(7, 9) if index % 2 == 0 else Fraction(-5, 6)
            B = ratio * V

            V_total += V
            B_total += B
            correction_total += Fraction(1, 10) * V

        # The two eigenvalues after diagonal correction are
        # V_total-correction_total +/- B_total.
        assert V_total - correction_total >= abs(B_total)
        port_checks += 1

    # tau_p = 1/sqrt(p)-1/p decreases for p>=4. At p=67,
    # tau_p < 1/9 is equivalent to 81*67 < (67+9)^2 = 76^2.
    assert 81 * 67 < 76**2

    return {
        "classification": "PASS_POSITIVE_FUNCTOR_COLOR_ERASURE",
        "affine_real_column_checks": affine_checks,
        "nonmultiple_physical_column_checks": nonmultiple_checks,
        "synthetic_branch_port_checks": port_checks,
        "rough_threshold": {
            "first_prime": 67,
            "certificate": "81*67 < 76^2",
            "conclusion": "1/sqrt(p)-1/p < 1/9 for p>=67",
        },
        "scope": (
            "Exact Fraction arithmetic. Synthetic port checks illustrate the "
            "general PSD-preservation proof; the theorem itself is "
            "linear-algebraic."
        ),
    }


if __name__ == "__main__":
    result = verify()
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)
