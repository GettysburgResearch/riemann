#!/usr/bin/env python3
"""Exact rational replay for L-105323.

Checks the centered-root temperature and first-residue carrier identities on
finite polynomial derivative chains. It does not replay Xi exhaustion, the
low-order variance budget, the moving saddle, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def derivative(a):
    return trim([Fraction(i) * a[i] for i in range(1, len(a))] or [Fraction(0)])


def scale(a, c):
    return trim([c * x for x in a])


def polynomial_from_roots(roots):
    out = [Fraction(1)]
    for root in roots:
        out = mul(out, [Fraction(-root), Fraction(1)])
    return out


def centered_v2(poly):
    poly = trim(poly)
    degree = len(poly) - 1
    assert degree >= 2 and poly[-1] == 1
    root_sum = -poly[-2]
    e2 = poly[-3]
    return Fraction(degree - 1, degree) * root_sum * root_sum - 2 * e2


def temperature(poly):
    degree = len(trim(poly)) - 1
    return centered_v2(poly) / Fraction(degree * (degree - 1))


def first_residue_mass(poly):
    degree = len(trim(poly)) - 1
    return centered_v2(poly) / Fraction(degree * degree)


def run():
    fixtures = [
        (-4, -1, 2),
        (-5, -2, 1, 4),
        (-7, -3, 0, 2, 8),
        (-9, -4, -1, 3, 6, 11),
    ]
    checks = 0
    chains = []

    for roots in fixtures:
        current = polynomial_from_roots(roots)
        invariant = temperature(current)
        chain = []

        while len(current) - 1 >= 3:
            degree = len(current) - 1
            mass = first_residue_mass(current)
            chain.append(
                {
                    "degree": degree,
                    "temperature": str(invariant),
                    "first_mass": str(mass),
                }
            )

            nxt = scale(derivative(current), Fraction(1, degree))
            assert temperature(nxt) == invariant
            checks += 1

            next_mass = first_residue_mass(nxt)
            expected_ratio = Fraction(
                degree * (degree - 2), (degree - 1) * (degree - 1)
            )
            assert next_mass == expected_ratio * mass
            checks += 1
            current = nxt

        chains.append(chain)

    result = {
        "verdict": "PASS_X_105323_RESIDUE_TEMPERATURE",
        "arithmetic_class": "EXACT_RATIONAL",
        "checks": checks,
        "chains": chains,
        "xi_canonical_product_passage_replayed": False,
        "low_order_variance_budget_proved": False,
        "rh_established": False,
    }
    result["proof_object"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object"])
    print("RH_UNPROVEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
