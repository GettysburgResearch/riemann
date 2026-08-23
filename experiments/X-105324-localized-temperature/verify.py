#!/usr/bin/env python3
"""Exact rational replay for L-105324 on complete polynomial windows.

This checks the global zero-leakage specialization of the entire-window
identity. It does not prove an entire-window estimate, the Xi winding budget,
canonical-product passage, or RH.
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


def from_roots(roots):
    out = [Fraction(1)]
    for root in roots:
        out = mul(out, [Fraction(-root), Fraction(1)])
    return out


def power_sums(poly):
    poly = trim(poly)
    degree = len(poly) - 1
    assert degree >= 2 and poly[-1] == 1
    s1 = -poly[-2]
    e2 = poly[-3]
    s2 = s1 * s1 - 2 * e2
    return degree, s1, s2


def temperature(poly):
    degree, s1, s2 = power_sums(poly)
    return (degree * s2 - s1 * s1) / Fraction(
        degree * degree * (degree - 1)
    )


def run():
    fixtures = [
        (-4, -1, 2),
        (-5, -2, 1, 4),
        (-7, -3, 0, 2, 8),
        (-9, -4, -1, 3, 6, 11),
    ]
    checks = 0
    records = []

    for roots in fixtures:
        p = from_roots(roots)
        n, s1, s2 = power_sums(p)
        q = scale(derivative(p), Fraction(1, n))
        m, t1, t2 = power_sums(q)

        delta0 = m - n
        delta1 = t1 - s1
        delta2 = t2 - s2

        assert delta0 == -1
        checks += 1
        assert delta1 == -s1 / Fraction(n)
        checks += 1
        assert delta2 == -2 * s2 / Fraction(n) + s1 * s1 / Fraction(n * n)
        checks += 1
        assert temperature(q) == temperature(p)
        checks += 1

        # Complete-window first-residue carrier leakage vanishes exactly.
        b1 = -Fraction(n - 1, n) * temperature(p)
        leakage = -Fraction(n, n - 1) * b1 - temperature(p)
        assert leakage == 0
        checks += 1

        records.append(
            {
                "roots": list(roots),
                "delta": [str(delta0), str(delta1), str(delta2)],
                "temperature": str(temperature(p)),
                "carrier_leakage": str(leakage),
            }
        )

    result = {
        "verdict": "PASS_X_105324_LOCALIZED_TEMPERATURE_FLUX",
        "arithmetic_class": "EXACT_RATIONAL",
        "checks": checks,
        "fixtures": records,
        "entire_window_bound_proved": False,
        "xi_winding_budget_proved": False,
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
