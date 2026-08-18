#!/usr/bin/env python3
"""Deterministic replay for T-98010.

The infinite monotonicity theorem is analytic.  The Decimal scan below is a
finite hostile diagnostic, while the zero-marginal convexity fixtures are exact
Fraction arithmetic.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product

getcontext().prec = 80
D = Decimal


def qstar(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 15
    if n == 3:
        return 6
    if n == 4:
        return 3
    return 6


def positive_part(x: Fraction) -> Fraction:
    return x if x > 0 else Fraction(0)


def slack(even, odd, lam: Fraction) -> Fraction:
    t_odd = sum(a * t for a, t, _ in odd)
    r_odd = sum(a * r for a, _, r in odd)
    return lam * t_odd + sum(
        a * positive_part(r - lam * t) for a, t, r in even
    ) - r_odd


def exact_zero_marginal_fixtures() -> int:
    """Check the convex theorem on a broad exact finite family."""
    checked = 0
    atom_options = [
        (Fraction(1), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(1), Fraction(1)),
        (Fraction(1), Fraction(2), Fraction(1)),
        (Fraction(2), Fraction(1), Fraction(3)),
        (Fraction(1), Fraction(3), Fraction(2)),
    ]

    for e_idx in product(range(len(atom_options)), repeat=2):
        even = [atom_options[i] for i in e_idx]
        for o_idx in product(range(len(atom_options)), repeat=2):
            odd = [atom_options[i] for i in o_idx]
            t_e = sum(a * t for a, t, _ in even)
            t_ep = sum(a * t for a, t, r in even if r > 0)
            t_o = sum(a * t for a, t, _ in odd)
            sandwich = t_ep <= t_o <= t_e

            ratios = {Fraction(0)}
            for _, t, r in even:
                ratios.add(r / t)
            probes = sorted(
                ratios
                | {Fraction(-2), Fraction(-1), Fraction(1, 2), Fraction(4)}
            )
            d0 = slack(even, odd, Fraction(0))
            zero_is_min = all(slack(even, odd, lam) >= d0 for lam in probes)
            if zero_is_min != sandwich:
                raise AssertionError(
                    (even, odd, sandwich, zero_is_min, d0, probes)
                )
            checked += 1
    return checked


def decimal_monotonicity_scan(limit: int = 100_000):
    """Finite diagnostic for B_N/A_N > c(N+1)."""
    A = D(0)
    B = D(0)
    minimum = None
    minimum_n = None

    for n in range(2, limit + 1):
        root_n = D(n).sqrt()
        w = D(qstar(n)) / root_n
        A += w
        B += w * D(n).ln()

        y = D(n + 1)
        c = y.ln() - D(2) + D(3) / (D(2) * y.sqrt())
        margin = B - c * A
        if margin <= 0:
            raise AssertionError((n, margin))
        if minimum is None or margin < minimum:
            minimum = margin
            minimum_n = n

    return minimum_n, minimum


def ordered_ratio_scan(endpoint: int = 50_000, count: int = 2_000) -> int:
    """Check that theta(X/k) decreases with k on a finite source sample."""

    def q_value(y: Decimal) -> Decimal:
        total = D(0)
        nmax = int(y)
        for n in range(2, nmax + 1):
            total += D(qstar(n)) / D(n).sqrt() * (y / D(n)).ln()
        return total

    previous = None
    checked = 0
    for k in range(1, count + 1):
        y = D(endpoint) / D(k)
        if y <= 2:
            break
        theta = q_value(y) / (D(4) * y.sqrt() - D(3))
        if previous is not None and theta > previous:
            raise AssertionError((k, previous, theta))
        previous = theta
        checked += 1
    return checked


def main() -> None:
    fixtures = exact_zero_marginal_fixtures()
    min_n, min_margin = decimal_monotonicity_scan()
    ordered = ordered_ratio_scan()

    # Exact signs used in the exceptional-dictionary correction.
    if not Fraction(225, 4) > Fraction(81, 2):
        raise AssertionError("15/2 <= 9/sqrt(2) mutation")
    if not 81 > 18:
        raise AssertionError("9/sqrt(2) <= 3 mutation")

    print("PASS_X_98010_ZERO_MARGINAL_LORENZ")
    print("exact_zero_marginal_fixtures=", fixtures)
    print("decimal_cell_scan_limit=", 100_000)
    print("minimum_decimal_margin_cell=", min_n)
    print("minimum_decimal_margin=", min_margin)
    print("ordered_source_ratios_checked=", ordered)


if __name__ == "__main__":
    main()
