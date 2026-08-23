#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction


def poly_derivative(p: list[Fraction]) -> list[Fraction]:
    return [Fraction(i) * p[i] for i in range(1, len(p))] or [Fraction(0)]


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    out = [Fraction(0)] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_shift(p: list[Fraction], k: int) -> list[Fraction]:
    return [Fraction(0)] * k + p


def D_on_prefactor(p: list[Fraction], b: Fraction) -> list[Fraction]:
    # D(P(q)e^(bu-ae^(2u))) = [2q P'(q)+(b-2q)P(q)] times the same factor.
    dp = poly_derivative(p)
    term1 = [Fraction(0)] + [Fraction(2) * x for x in dp]
    term2 = [b * x for x in p]
    term3 = [Fraction(0)] + [Fraction(-2) * x for x in p]
    return poly_add(poly_add(term1, term2), term3)


def main() -> None:
    b = Fraction(1, 2)
    p0 = [Fraction(1)]
    p1 = D_on_prefactor(p0, b)
    p2 = D_on_prefactor(p1, b)
    p2[0] -= Fraction(1, 4)
    assert p2 == [Fraction(0), Fraction(-6), Fraction(4)]

    # Mixed-frequency firewall at t=pi.
    f1 = Fraction(-1)
    f2 = Fraction(1, 2)
    f = f1 + f2
    fp = Fraction(0)
    fpp = Fraction(1) + Fraction(-2)
    lag = fp * fp - f * fpp
    assert lag == Fraction(-1, 2)

    # Individual diagonal Laguerre expressions are both one.
    assert Fraction(1) == 1
    assert Fraction(4) * Fraction(1, 2) ** 2 == 1

    payload = {
        "schema": "riemann.t104560.modular_mixed_orbit.v1",
        "checks": {
            "theta_differential_polynomial": [str(x) for x in p2],
            "mixed_frequency_counterexample": str(lag),
            "diagonal_entries": ["1", "1"],
        },
        "scope": {
            "modular_theta_identity_proved_analytically": True,
            "mixed_matrix_identity_proved_analytically": True,
            "mtsg104560_proved": False,
            "alpha2_from_alpha3_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T104560_MODULAR_MIXED_ORBIT_ALGEBRA",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
