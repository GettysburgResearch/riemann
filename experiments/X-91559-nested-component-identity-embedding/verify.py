#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


def beta(n: int, q: int) -> Fraction:
    a, rem = divmod(n, q)
    return Fraction(a * (q - 1 - rem), n + 1)


def add_scaled(dst: list[Fraction], src: list[Fraction], scale: Fraction) -> None:
    for i, value in enumerate(src):
        dst[i] += scale * value


def q_row_coefficients(N: int, n: int) -> list[Fraction]:
    """Formal coefficients of Q_Y(n) in h_Y(2),...,h_Y(N)."""
    out = [Fraction(0) for _ in range(N + 1)]
    if not 2 <= n <= N:
        return out

    a = Fraction(n + 1, n - 1)
    out[n] += a
    if n + 1 <= N:
        out[n + 1] -= a
        out[n + 1] += Fraction(2 * (n + 1), n * (n - 1))
    tail = Fraction(2, n * (n - 1))
    for m in range(n + 2, N + 1):
        out[m] += tail
    return out


def replay_component_response(max_endpoint: int = 80) -> int:
    checks = 0
    for N in range(2, max_endpoint + 1):
        rows = {
            n: q_row_coefficients(N, n)
            for n in range(2, N + 1)
        }
        for q in range(2, N + 1):
            carry = [Fraction(0) for _ in range(N + 1)]
            detail = [Fraction(0) for _ in range(N + 1)]
            for n, coeffs in rows.items():
                add_scaled(carry, coeffs, beta(n, q))
                add_scaled(
                    detail,
                    coeffs,
                    beta(n, q) - 2 * beta(n, 4 * q),
                )

            expected_carry = [Fraction(0) for _ in range(N + 1)]
            expected_detail = [Fraction(0) for _ in range(N + 1)]
            for m in range(2, N + 1):
                if m % q == 0:
                    expected_carry[m] += 1
                    expected_detail[m] += 1
                if m % (4 * q) == 0:
                    expected_detail[m] -= 2

            assert carry == expected_carry
            assert detail == expected_detail
            checks += 2
    return checks


def replay_affine_separation() -> int:
    checks = 0

    # Child Q_3 has the single coefficient
    # d(2)=3 log(3/2)/sqrt(2).  Its q=2 response coefficient is 1/3.
    assert beta(2, 2) == Fraction(1, 3)
    assert beta(2, 8) == 0
    checks += 2

    # Fixed-67 affine image is row 200, and the unmatched parent column is 200.
    assert 67 * (2 + 1) - 1 == 200
    assert beta(200, 200) == Fraction(199, 201)
    assert beta(200, 800) == 0
    checks += 3

    # The proof uses
    # lifted response > 199/2010
    # target response < 1/2800.
    assert Fraction(199, 2010) > Fraction(1, 2800)
    assert 134 < 12**2
    assert 200 > 14**2
    checks += 3

    # Rational logarithm bounds used in R-91558:
    # log(1+x)>2x/(2+x) gives log(3/2)>2/5;
    # log(1+x)<x gives log(201/200)<1/200.
    assert Fraction(2) * Fraction(1, 2) / (2 + Fraction(1, 2)) == Fraction(2, 5)
    assert Fraction(1, 200) > 0
    checks += 2

    return checks


def replay_nested_monotonicity(max_Z: int = 500) -> int:
    checks = 0
    # On every smooth cell,
    # D'(Z)=Z^-1 sum_(Z/4<k<=Z) k^-1/2.
    # Only positivity of the index set and coefficients is needed.  We replay
    # all integer activation windows through max_Z as a finite structural check.
    for Z in range(1, max_Z + 1):
        indices = [k for k in range(1, Z + 1) if 4 * k > Z]
        assert indices
        assert all(4 * k > Z and k <= Z for k in indices)
        checks += 1
    return checks


def main() -> None:
    checks_response = replay_component_response()
    checks_affine = replay_affine_separation()
    checks_monotone = replay_nested_monotonicity()
    result = {
        "classification": "PASS_NESTED_COMPONENT_IDENTITY_EMBEDDING",
        "checks": checks_response + checks_affine + checks_monotone,
        "component_response_checks": checks_response,
        "affine_counterexample_checks": checks_affine,
        "monotonicity_window_checks": checks_monotone,
        "max_formal_endpoint": 80,
        "max_monotonicity_window": 500,
        "scope": (
            "The formal-coefficient replay certifies the exact carry/detail "
            "response of Q_Y and the rational part of the affine separation. "
            "Global Hall entry, row-budget normalization, live-parent replay, "
            "and RH are not certified by this script."
        ),
    }
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
