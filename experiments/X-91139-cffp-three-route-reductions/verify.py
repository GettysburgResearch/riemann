#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

def activation_strip_checks():
    assert 7 * 320 * 320 > 8 * 297 * 297
    checks = 0
    minimum = None
    for j in range(7, 100_001):
        margin = Fraction(2 * (j - 6), 5 * j * (j - 1))
        assert margin > 0
        if minimum is None or margin < minimum:
            minimum = margin
        checks += 1
    return checks, minimum

def subcritical_checks():
    theta = Fraction(1, 8)
    partial = Fraction(0)
    power = Fraction(1)
    for _ in range(100):
        partial += power
        power *= theta
    exact = Fraction(1, 1) / (1 - theta)
    tail = power / (1 - theta)
    assert partial < exact
    assert exact == Fraction(8, 7)
    assert exact - partial == tail
    assert tail > 0
    return exact

def butterfly_dual_checks():
    instances = [
        (Fraction(7, 5), Fraction(11, 7), Fraction(13, 8),
         Fraction(2, 5), Fraction(3, 2), Fraction(7, 4), Fraction(5, 2)),
        (Fraction(5, 3), Fraction(9, 4), Fraction(8, 3),
         Fraction(7, 11), Fraction(4, 3), Fraction(17, 9), Fraction(23, 8)),
    ]
    checks = 0
    for alpha_m, alpha_0, alpha_p, theta, g_m, g_0, g_p in instances:
        c_m = alpha_0 * theta / alpha_m
        c_p = alpha_0 * (1 - theta) / alpha_p
        y_m = alpha_m * g_m
        y_0 = alpha_0 * g_0
        y_p = alpha_p * g_p
        lhs = c_m * y_m - y_0 + c_p * y_p
        rhs = alpha_0 * (theta * g_m + (1 - theta) * g_p - g_0)
        assert lhs == rhs
        checks += 1
    return checks

def main():
    strip_checks, minimum_strip = activation_strip_checks()
    geometric_exact = subcritical_checks()
    butterfly_checks = butterfly_dual_checks()
    result = {
        "classification": "PASS_CFFP_THREE_ROUTE_REDUCTIONS",
        "activation_strip_integer_checks": strip_checks,
        "minimum_sampled_activation_margin": str(minimum_strip),
        "subcritical_geometric_factor": str(geometric_exact),
        "subcritical_tail_after_100_positive": True,
        "butterfly_dual_identity_checks": butterfly_checks,
        "scope": (
            "Exact rational regression for L-91370, T-91311 and L-91372. "
            "The universal conclusions use the algebraic proofs in those files. "
            "This replay does not certify L-91364, PR #437, CFFP, or RH."
        ),
    }
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)

if __name__ == "__main__":
    main()
