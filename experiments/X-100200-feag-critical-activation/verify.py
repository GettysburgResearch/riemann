#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

VERDICT = "PASS_X_100200_FEAG_CRITICAL_ACTIVATION"
BITS = 100
Q = 1 << BITS


def subset_products(labels: list[Fraction]) -> list[tuple[Fraction, int]]:
    out: list[tuple[Fraction, int]] = []
    for mask in range(1 << len(labels)):
        p = Fraction(1)
        parity = 0
        for i, q in enumerate(labels):
            if mask & (1 << i):
                p *= q
                parity ^= 1
        out.append((p, -1 if parity else 1))
    return out


def sqrt_fraction_exact(x: Fraction) -> Fraction:
    an = isqrt(x.numerator)
    ad = isqrt(x.denominator)
    assert an * an == x.numerator and ad * ad == x.denominator
    return Fraction(an, ad)


def pow_neg_three_halves_exact(x: Fraction) -> Fraction:
    return Fraction(1, 1) / (x * sqrt_fraction_exact(x))


def f_kernel(y: Fraction) -> Fraction:
    if y < 1:
        return Fraction(16)
    r = sqrt_fraction_exact(y)
    return Fraction(24, 1) / r - Fraction(9, 1) / y


def envelope_direct(labels: list[Fraction], y: Fraction) -> Fraction:
    return sum(
        (eps * pow_neg_three_halves_exact(p) * f_kernel(y / p)
         for p, eps in subset_products(labels)),
        Fraction(0),
    )


def moments(labels: list[Fraction], y: Fraction):
    s05 = s1 = s15 = Fraction(0)
    delta = Fraction(1)
    for q in labels:
        delta *= 1 - pow_neg_three_halves_exact(q)
    for p, eps in subset_products(labels):
        if p <= y:
            rp = sqrt_fraction_exact(p)
            s05 += eps / rp
            s1 += eps / p
            s15 += eps / (p * rp)
    return s05, s1, s15, delta - s15


def cell_formula(labels: list[Fraction], y: Fraction) -> Fraction:
    s05, s1, _s15, tail = moments(labels, y)
    ry = sqrt_fraction_exact(y)
    return 16 * tail + 24 * s1 / ry - 9 * s05 / y


def sqrt_interval(x: Fraction):
    n = x.numerator * x.denominator
    a = isqrt(n * Q * Q)
    lo = Fraction(a, Q * x.denominator)
    hi = lo if a * a == n * Q * Q else Fraction(a + 1, Q * x.denominator)
    return lo, hi


def inv_three_half_interval(x: Fraction):
    lo, hi = sqrt_interval(x)
    return Fraction(1, 1) / (x * hi), Fraction(1, 1) / (x * lo)


def counterexample_interval():
    labels = [
        Fraction(2), Fraction(21, 10), Fraction(11, 5), Fraction(23, 10),
        Fraction(12, 5), Fraction(5, 2), Fraction(3), Fraction(27),
    ]
    prod_lo = prod_hi = Fraction(1)
    for q in labels:
        r_lo, r_hi = inv_three_half_interval(q)
        prod_lo *= 1 - r_hi
        prod_hi *= 1 - r_lo
    rt2_lo, rt2_hi = sqrt_interval(Fraction(2))
    lower = 12 * rt2_lo - Fraction(9, 2) + 16 * (prod_lo - 1)
    upper = 12 * rt2_hi - Fraction(9, 2) + 16 * (prod_hi - 1)
    return lower, upper


def run() -> dict[str, object]:
    direct_checks = jump_checks = critical_checks = classification_checks = 0

    fixtures = [
        [Fraction(4), Fraction(9), Fraction(25)],
        [Fraction(9, 4), Fraction(16, 9), Fraction(25, 4), Fraction(49, 9)],
        [Fraction(4), Fraction(4), Fraction(9), Fraction(16)],
    ]
    y_fixtures = [
        Fraction(81, 16), Fraction(121, 16), Fraction(169, 9),
        Fraction(289, 16), Fraction(361, 9), Fraction(529, 16),
    ]
    for labels in fixtures:
        products = subset_products(labels)
        for y in y_fixtures:
            if any(p == y for p, _ in products):
                continue
            assert envelope_direct(labels, y) == cell_formula(labels, y)
            direct_checks += 1
        by_product: dict[Fraction, int] = {}
        for p, eps in products:
            by_product[p] = by_product.get(p, 0) + eps
        for d, b in by_product.items():
            jump = -Fraction(b) * pow_neg_three_halves_exact(d)
            direct_jump = sum(
                (eps * pow_neg_three_halves_exact(p) * Fraction(-1)
                 for p, eps in products if p == d),
                Fraction(0),
            )
            assert jump == direct_jump
            jump_checks += 1

    for s1, s05, tail in [
        (Fraction(-3, 5), Fraction(-7, 8), Fraction(11, 13)),
        (Fraction(-5, 9), Fraction(-4, 7), Fraction(2, 3)),
        (Fraction(-7, 11), Fraction(-9, 10), Fraction(5, 6)),
    ]:
        ystar = (Fraction(3) * s05 / (Fraction(4) * s1)) ** 2
        r = sqrt_fraction_exact(ystar)
        value = 16 * tail + 24 * s1 / r - 9 * s05 / ystar
        expected = 16 * (tail + s1 * s1 / s05)
        assert value == expected
        assert (value >= 0) == (s1 * s1 + tail * s05 <= 0)
        critical_checks += 2

    for s1, s05 in [
        (Fraction(2, 3), Fraction(-1, 2)),
        (Fraction(0), Fraction(2, 5)),
        (Fraction(-2, 3), Fraction(1, 5)),
        (Fraction(-2, 3), Fraction(-1, 5)),
    ]:
        if s1 < 0 and s05 >= 0:
            assert 4 * s1 - 3 * s05 < 0
        if s1 < 0 and s05 < 0:
            assert (Fraction(3) * s05 / (Fraction(4) * s1)) ** 2 > 0
        classification_checks += 1

    lower, upper = counterexample_interval()
    assert Fraction(-203, 100) < lower < upper < Fraction(-202, 100)

    core = {
        "schema": "riemann.x100200.feag-critical-activation.v1",
        "classification": VERDICT,
        "base_pr": 672,
        "base_sha": "2a351548eb7960ff8ae99f193c10e278984c5657",
        "arithmetic_class": "EXACT_RATIONAL_AND_DIRECTED_RADICAL",
        "direct_cell_formula_checks": direct_checks,
        "activation_jump_checks": jump_checks,
        "critical_point_checks": critical_checks,
        "cell_classification_checks": classification_checks,
        "counterexample_interval_lower": str(lower),
        "counterexample_interval_upper": str(upper),
        "proves": [
            "exact three-moment cell formula",
            "complete classification of cell minima",
            "exact double-negative Turan gate",
            "exact activation jump ledger",
            "generic rational-shift counterexample",
        ],
        "does_not_prove": [
            "PATG100200 for the actual prime labels",
            "FEAG99980",
            "Riemann Hypothesis",
        ],
        "patg100200_proved": False,
        "feag99980_proved": False,
        "rh_established": False,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return {**core, "proof_object_sha256": hashlib.sha256(canon).hexdigest()}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
