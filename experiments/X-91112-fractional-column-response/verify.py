#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path


def ceil_frac(x: Fraction) -> int:
    return -((-x.numerator) // x.denominator)


def beta_bar(n: int, q: Fraction) -> Fraction:
    M = n + 1
    a = ceil_frac(Fraction(M, 1) / q) - 1
    if a < 0:
        a = 0
    return Fraction(a, 1) * (Fraction(a + 1, 1) * q - M) / M


def row_from_seed(F: dict[int, Fraction], nmax: int) -> dict[int, Fraction]:
    def f(n: int) -> Fraction:
        return F.get(n, Fraction(0))
    def A(n: int) -> Fraction:
        return Fraction(0) if n <= 1 else f(n) / (n - 1)
    return {
        n: Fraction(n + 1) * (A(n) - 2 * A(n + 1) + A(n + 2))
        for n in range(2, nmax + 1)
    }


def direct_response(F: dict[int, Fraction], q: Fraction, nmax: int) -> Fraction:
    d = row_from_seed(F, nmax)
    return sum((d[n] * beta_bar(n, q) for n in d), Fraction(0))


def formula_response(F: dict[int, Fraction], q: Fraction, nmax: int) -> Fraction:
    def f(n: int) -> Fraction:
        return F.get(n, Fraction(0))
    def A(n: int) -> Fraction:
        return Fraction(0) if n <= 1 else f(n) / (n - 1)
    total = Fraction(0)
    j = 1
    while Fraction(j, 1) * q <= nmax + 2:
        x = Fraction(j, 1) * q
        k = x.numerator // x.denominator
        theta = x - k
        if k >= 2:
            total += f(k) - f(k + 1) + 2 * theta * (A(k) - A(k + 1))
        j += 1
    return total


def affine_response(F: dict[int, Fraction], q: Fraction, nmax: int, m: int) -> Fraction:
    # Unnormalized affine row lift n -> m(n+1)-1. The common scalar m^-1/2
    # is omitted from both sides.
    child = row_from_seed(F, nmax)
    Q = q * m
    total = Fraction(0)
    for n, coeff in child.items():
        N = m * (n + 1) - 1
        total += coeff * beta_bar(N, Q)
    return total


def main() -> None:
    seeds = [
        {2: Fraction(7, 3), 3: Fraction(5, 4), 4: Fraction(-2, 5), 6: Fraction(11, 7)},
        {2: Fraction(1), 5: Fraction(3, 2), 8: Fraction(4, 9)},
        {3: Fraction(-5, 6), 4: Fraction(13, 10), 7: Fraction(2)},
    ]
    qs = [Fraction(2), Fraction(5, 2), Fraction(7, 3), Fraction(11, 4), Fraction(13, 5)]
    checks = 0
    for F in seeds:
        nmax = max(F) + 4
        for q in qs:
            lhs = direct_response(F, q, nmax)
            rhs = formula_response(F, q, nmax)
            assert lhs == rhs, (F, q, lhs, rhs)
            checks += 1
            for m in (4, 9):
                aff = affine_response(F, q, nmax, m)
                assert aff == lhs, (F, q, m, aff, lhs)
                checks += 1

    C_total = Fraction(81, 2)
    ordinary_coeff = 89 * C_total
    detail_coeff = 112 * C_total
    assert detail_coeff == 4536
    assert ordinary_coeff == Fraction(7209, 2)
    relative_coeff = detail_coeff * Fraction(3, 4)
    assert relative_coeff == 3402

    W = 100000
    omission_lower = Fraction(W * 7, 12) - 800
    terminal_error_upper = ordinary_coeff * 8
    assert terminal_error_upper == 28836
    assert omission_lower > terminal_error_upper

    out = {
        "classification": "PASS_FRACTIONAL_COLUMN_RESPONSE_AND_CONTINUOUS_RESET_CONSTANTS",
        "exact_identity_checks": checks,
        "combined_seed_difference_constant": str(C_total),
        "ordinary_response_coefficient": str(ordinary_coeff),
        "detail_response_coefficient": str(detail_coeff),
        "interior_relative_coefficient": str(relative_coeff),
        "continuous_top_omission_width": W,
        "terminal_omission_lower": str(omission_lower),
        "terminal_error_upper": str(terminal_error_upper),
        "scope": "Exact Fraction replay of the fractional-column Green identity and affine covariance. Analytic decay hypotheses are proved in L-91114/L-91111 and combined in L-91324."
    }
    path = Path(__file__).resolve().parent / "results" / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(out["classification"])


if __name__ == "__main__":
    main()
