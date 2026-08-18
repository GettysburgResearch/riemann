#!/usr/bin/env python3
"""Exact finite countermodels and algebraic interface checks for PRs #565/#566."""
from fractions import Fraction
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "results" / "interface_verification.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

# PR #565 source-type firewall.  A_p is a same-channel physical embedding;
# the rough-history parity swap belongs to recursive observation, not to the
# positive restriction.  Use a formal positive test coefficient r rather than suppressing it; the symbolic proof covers r=p^{-1/2}.
r = Fraction(1, 9)
parent = (Fraction(1), Fraction(0))
child = (Fraction(1), Fraction(0))
true_restriction = (parent[0] - r * child[0], parent[1] - r * child[1])
swapped_restriction = (parent[0] - r * child[1], parent[1] - r * child[0])
assert true_restriction == (Fraction(8, 9), Fraction(0))
assert swapped_restriction == (Fraction(1), Fraction(-1, 9))
assert min(true_restriction) >= 0 and min(swapped_restriction) < 0

# One-prime scalar coefficient check for PR #565.  With s=1-r, lambda=r,
# alpha=r^2 and swapped current observation F+rF_y, its own recurrence is
# (1-r)F + r(F+rF_y) - r^2 F_y = F.  The native Euler factor is F-rF_y.
F = Fraction(7, 5)
Fy = Fraction(11, 10)
s = 1 - r
lam = r
alpha = r * r
pr565_one_prime = s * F + lam * (F + r * Fy) - alpha * Fy
native_one_prime = F - r * Fy
assert pr565_one_prime == F
assert native_one_prime == F - r * Fy
assert pr565_one_prime - native_one_prime == r * Fy > 0

# The tautological causal identity itself has zero net child coefficient.
causal_child_coefficient = -lam * r + alpha
assert causal_child_coefficient == 0
assert -r != 0

# PR #566 statement-to-use countermodel.  Injection into R does not compare H to R.
alpha_reserve = Fraction(1, 10)
child_scalar = Fraction(10)
reserve_scalar = Fraction(1)
hall_complement_scalar = Fraction(1, 2)
assert reserve_scalar == alpha_reserve * child_scalar
assert hall_complement_scalar < alpha_reserve * child_scalar

# Mass and first moment are not a Hall/Lorenz certificate.  For e<=o transport,
# every lower prefix of demand must be no larger than the corresponding supply prefix.
supply = {Fraction(0): Fraction(1, 2), Fraction(2): Fraction(1, 2)}
demand = {Fraction(1): Fraction(1)}
assert sum(supply.values()) == sum(demand.values()) == 1
assert sum(x * m for x, m in supply.items()) == sum(x * m for x, m in demand.items()) == 1
threshold = Fraction(1)
supply_prefix = sum(m for x, m in supply.items() if x <= threshold)
demand_prefix = sum(m for x, m in demand.items() if x <= threshold)
assert demand_prefix > supply_prefix

# Corrected 1/42 and factor-67 arithmetic margin.
# Since 65^2=4225 < 64*67=4288, one has 1/sqrt(67)<8/65.  Therefore
# (1-8/sqrt(67))/42 > (1-64/65)/42 = 1/2730.
h = Fraction(8, 65)
margin = Fraction(1, 42) * (1 - 8 * h)
assert margin == Fraction(1, 2730)
# Cross-check the exact algebraic expression numerically.
import decimal
decimal.getcontext().prec = 80
D = decimal.Decimal
sqrt67 = D(67).sqrt()
exact_margin = (D(1) - D(8) / sqrt67) / D(42)
assert exact_margin > D(1) / D(2730)

result = {
    "schema": "riemann.x97610.factor67-source-interface-firewalls.v2",
    "pr565": {
        "formal_positive_test_r": str(r),
        "same_channel_positive_restriction": [str(x) for x in true_restriction],
        "swapped_non_source": [str(x) for x in swapped_restriction],
        "one_prime_claimed_recurrence": str(pr565_one_prime),
        "one_prime_native_euler_value": str(native_one_prime),
        "one_prime_missing_term": str(pr565_one_prime - native_one_prime),
        "causal_child_coefficient": str(causal_child_coefficient),
        "native_one_prime_child_coefficient": str(-r),
    },
    "pr566": {
        "reserve_injection_exact": str(reserve_scalar),
        "hall_complement_scalar": str(hall_complement_scalar),
        "claimed_child_payment": str(alpha_reserve * child_scalar),
        "hall_prefix_counterexample": {
            "supply_mass": "1",
            "demand_mass": "1",
            "supply_first_moment": "1",
            "demand_first_moment": "1",
            "threshold": str(threshold),
            "supply_prefix": str(supply_prefix),
            "demand_prefix": str(demand_prefix),
        },
    },
    "repaired_bias_contraction": {
        "exact_decimal_margin": format(exact_margin, "f"),
        "convenient_lower_bound": "1/2730",
    },
    "classification": "PASS_FACTOR67_SOURCE_INTERFACE_FIREWALLS",
    "rh_established": False,
}
OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, indent=2, sort_keys=True))
print("PASS_FACTOR67_SOURCE_INTERFACE_FIREWALLS")
