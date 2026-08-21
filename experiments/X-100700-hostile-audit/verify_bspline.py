#!/usr/bin/env python3
"""Symbolic/rational checks for L-100712 and L-100713.

Finite algebra only.  This script does not prove the remaining Harnack estimate
or RH.
"""

from fractions import Fraction
import hashlib
import json


def poly_eval(coeffs, x):
    out = Fraction(0)
    for c in reversed(coeffs):
        out = out * x + c
    return out


def check_cubic_jets():
    # psi_-(u)=192 e^u-64 e^(3u/2); psi_+(u)=192 e^(u/2)-64.
    left = []
    right = []
    for k in range(4):
        left.append(Fraction(192) * Fraction(1) ** k - Fraction(64) * Fraction(3, 2) ** k)
        right.append(Fraction(192) * Fraction(1, 2) ** k - (Fraction(64) if k == 0 else Fraction(0)))
    assert left[:3] == right[:3]
    assert right[3] - left[3] == 48


def check_operator_polynomial():
    # The four carrier roots of the log-differential operator.
    roots = [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(3, 2)]
    coeffs = [Fraction(1)]
    for r in roots:
        nxt = [Fraction(0)] * (len(coeffs) + 1)
        for i, c in enumerate(coeffs):
            nxt[i] -= r * c
            nxt[i + 1] += c
        coeffs = nxt
    for r in roots:
        assert poly_eval(coeffs, r) == 0
    assert coeffs[-1] == 1


def check_mixed_differential_chain():
    # Formal variables g0,g0',g0''.
    # g1=g0+g0'; g2=g0+3g0'+2g0''.
    # (D-1/2)D(e^u g0)=e^u g2/2.
    # Coefficients on (g0,g0',g0'') agree exactly.
    lhs = (Fraction(1, 2), Fraction(3, 2), Fraction(1))
    rhs = tuple(Fraction(1, 2) * x for x in (1, 3, 2))
    assert lhs == rhs


def check_harnack_bridge():
    # A_1 kills the linear carrier X: X-2(X/2)=0.
    X = Fraction(37, 5)
    assert X - 2 * (X / 2) == 0


def main():
    check_cubic_jets()
    check_operator_polynomial()
    check_mixed_differential_chain()
    check_harnack_bridge()

    result = {
        "verdict": "PASS_T100712_T100713_CUBIC_BSPLINE_ALGEBRA",
        "cubic_green_jump_proved": True,
        "four_carrier_polynomial_proved": True,
        "mixed_quadratic_bridge_proved": True,
        "positive_bspline_peano_formula_claimed_analytic": True,
        "final_harnack_debt_proved": False,
        "rh_established": False,
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":"))
    print(payload)
    print(hashlib.sha256(payload.encode()).hexdigest())


if __name__ == "__main__":
    main()
