#!/usr/bin/env python3
"""Standard-library replay for R/L-30501 and L-30502.

The exact finite checks cover the shift/divisor factorization and modified
central stage. Directed reciprocal-square-root intervals stress the macroscopic
cutoff cell. The cofinal N/100 lower bound is the analytic proof in R-30501.
"""
from __future__ import annotations

from fractions import Fraction
from math import isqrt


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def central_load(r: list[Fraction], q: int) -> Fraction:
    return sum(
        (r[n] - r[n + 1]) * carry(n, n // 2, q)
        for n in range(2, len(r) - 1)
    )


def shifted(r: list[Fraction], q: int) -> Fraction:
    nmax = len(r) - 2
    out = Fraction(0)
    k = 1
    while 2 * k * q - 1 <= nmax or (2 * k + 1) * q <= nmax:
        if 2 * k * q - 1 <= nmax:
            out += r[2 * k * q - 1]
        if (2 * k + 1) * q <= nmax:
            out -= r[(2 * k + 1) * q]
        k += 1
    return out


def unshifted(r: list[Fraction], q: int) -> Fraction:
    nmax = len(r) - 2
    out = Fraction(0)
    k = 1
    while 2 * k * q <= nmax or (2 * k + 1) * q <= nmax:
        if 2 * k * q <= nmax:
            out += r[2 * k * q]
        if (2 * k + 1) * q <= nmax:
            out -= r[(2 * k + 1) * q]
        k += 1
    return out


def reciprocal_sqrt_interval(n: int, digits: int = 32) -> tuple[Fraction, Fraction]:
    scale = 10**digits
    t = isqrt((scale * scale) // n)
    while (t + 1) * (t + 1) * n <= scale * scale:
        t += 1
    while t * t * n > scale * scale:
        t -= 1
    return Fraction(t, scale), Fraction(t + 1, scale)


def check_shift_factorization(limit: int = 96) -> tuple[int, int]:
    divisor_rows = 0
    stage_rows = 0
    for nmax in range(4, limit + 1):
        r = [Fraction(0)] * (nmax + 2)
        for n in range(2, nmax + 1):
            r[n] = Fraction(((n * n + 3 * nmax) % 97) - 48, n * (nmax + 1))

        mmax = (nmax + 1) // 2
        sigma = [Fraction(0)] * (mmax + 1)
        for m in range(1, mmax + 1):
            sigma[m] = r[2 * m - 1] - (r[2 * m] if 2 * m <= nmax else 0)

        for q in range(2, mmax + 1):
            divisor = sum(sigma[m] for m in range(q, mmax + 1, q))
            assert divisor == shifted(r, q) - unshifted(r, q)
            divisor_rows += 1

        for q in range(2, nmax + 1):
            divisor = sum(sigma[m] for m in range(q, mmax + 1, q))
            assert central_load(r, q) + shifted(r, q) == r[q]
            assert central_load(r, q) + divisor + unshifted(r, q) == r[q]
            stage_rows += 1
    return divisor_rows, stage_rows


def check_cutoff_cell() -> int:
    rows = 0
    terms = 240
    for nmax in (60, 90, 120, 180, 240):
        for q in range(nmax // 3 + 1, nmax // 2 + 1):
            lower = Fraction(0)
            upper = Fraction(0)
            for k in range(1, terms + 1):
                le, ue = reciprocal_sqrt_interval(2 * k * q - 1)
                lo, uo = reciprocal_sqrt_interval((2 * k + 1) * q)
                lower += le - uo
                upper += ue - lo

            # The omitted positive pair intervals are disjoint subsets of the
            # telescoping reciprocal-square-root tail.
            tail_upper = reciprocal_sqrt_interval(2 * (terms + 1) * q - 1)[1]
            upper += tail_upper

            finite_lower = reciprocal_sqrt_interval(2 * q - 1)[0]
            boundary_upper = upper - finite_lower
            target_upper = -reciprocal_sqrt_interval(q)[0] / 10
            assert boundary_upper < target_upper
            rows += 1
    return rows


def main() -> None:
    divisor_rows, stage_rows = check_shift_factorization()
    cutoff_rows = check_cutoff_cell()
    print("PASS_EXACT_SHIFT_FACTORIZATION_AND_CUTOFF_OBSTRUCTION")
    print("shift_divisor_rows", divisor_rows)
    print("modified_stage_rows", stage_rows)
    print("directed_cutoff_rows", cutoff_rows)
    print(
        "proof_boundary",
        "finite exact/directed replay only; cofinal lower bound is R-30501; no RH claim",
    )


if __name__ == "__main__":
    main()
