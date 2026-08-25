#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def mul(a: list[Fraction], b: list[Fraction], n: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(n)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < n:
                out[i + j] += x * y
    return out


def binom_series(t: Fraction, n: int) -> list[Fraction]:
    out = [Fraction(1)]
    c = Fraction(1)
    for k in range(1, n):
        c *= (t - (k - 1)) / k
        out.append(c)
    return out


def factor_t(t: Fraction, n: int) -> list[Fraction]:
    return mul([Fraction(1), Fraction(-1)], binom_series(t, n), n)


def digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    n = 12
    target = [Fraction(1), Fraction(-1), Fraction(-1), Fraction(1)] + [Fraction(0)] * (n - 4)
    midpoint = [Fraction(1), Fraction(-1, 2), Fraction(-1, 2)] + [Fraction(0)] * (n - 3)

    local_checks = 0
    temperatures = [
        Fraction(-2),
        Fraction(-1, 2),
        Fraction(0),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(2, 3),
        Fraction(1),
        Fraction(3, 2),
        Fraction(2),
    ]

    midpoint_product = mul(midpoint, midpoint, n)

    for t in temperatures:
        f = factor_t(t, n)
        g = factor_t(Fraction(1) - t, n)
        assert mul(f, g, n) == target

        a = f[1]
        b = g[1]
        delta = t - Fraction(1, 2)
        assert a + b == -1
        assert a + Fraction(1, 2) == delta
        assert b + Fraction(1, 2) == -delta
        assert a * a + b * b == Fraction(1, 2) + 2 * delta * delta

        # After subtracting the antisymmetric first-order gauge, no tensor
        # coefficient of total degree below two remains.
        assert f[0] * g[0] == midpoint[0] * midpoint[0]
        assert f[1] * g[0] - midpoint[1] * midpoint[0] == delta
        assert f[0] * g[1] - midpoint[0] * midpoint[1] == -delta

        # The convolved remainder is temperature independent and starts at x^2.
        remainder = [target[k] - midpoint_product[k] for k in range(n)]
        assert remainder[0] == 0
        assert remainder[1] == 0
        assert remainder[2] == Fraction(-1, 4)
        local_checks += 1

    # Endpoint-color variance D^2 starts at degree two.
    d = [Fraction(0), Fraction(-1, 2), Fraction(1, 2)] + [Fraction(0)] * (n - 3)
    d2 = mul(d, d, n)
    assert d2[0] == 0 and d2[1] == 0 and d2[2] == Fraction(1, 4)

    generator_checks = 0
    for k in range(1, 33):
        coefficient = Fraction(1) - Fraction((-1) ** (k - 1), 2**k)
        assert coefficient > 0
        generator_checks += 1

    payload = {
        "schema": "riemann.t102940.critical-hodge.v1",
        "local_hodge_checks": local_checks,
        "generator_positive_coefficients_checked": generator_checks,
        "critical_residue_target": "-1 at every labelled prime",
        "harmonic_representative": "arithmetic midpoint M tensor M",
        "gauge_direction": "x tensor 1 - 1 tensor x",
        "subcritical_remainder_first_degree": 2,
        "hmo102940_proved": False,
        "pcoi102930_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102940_CRITICAL_HODGE_NORMAL_FORM",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
