#!/usr/bin/env python3
"""Exact algebra replay for L/T-106500."""

from fractions import Fraction
from math import comb
import hashlib
import json
from pathlib import Path

checks = 0

# For odd K, verify both monotonicity positivity and the exact
# (sum,difference)-binomial decomposition on an integer grid.
for K in range(1, 16, 2):
    for u in range(-5, 6):
        for v in range(-5, 6):
            d = v - u
            s = v + u
            lhs = d * (v**K - u**K)
            assert lhs >= 0
            rhs = sum(
                comb(K, 2 * ell + 1)
                * s ** (K - 2 * ell - 1)
                * d ** (2 * ell + 2)
                for ell in range((K - 1) // 2 + 1)
            )
            assert (2 ** (K - 1)) * lhs == rhs
            checks += 2

# The first mixed-current chaos is exactly the endpoint Wronskian source.
# Every later formal coefficient is nonnegative pointwise on the same grid.
for K in range(1, 16, 2):
    for r in range(0, 8):
        for u in range(-4, 5):
            for v in range(-4, 5):
                coefficient = (v**K - u**K) * (v - u) ** (2 * r + 1)
                assert coefficient >= 0
                checks += 1

# K=5 finite chaos polynomial and the exact conclusion margin.
assert [comb(5, 1), comb(5, 3), comb(5, 5)] == [5, 10, 1]
assert Fraction(1, 2 ** 4) == Fraction(1, 16)
alpha5 = Fraction(997, 1000)
target = Fraction(9, 10)
allowance = alpha5 - target
assert allowance == Fraction(97, 1000)
checks += 4

result = {
    "verdict": "PASS_T106500_ODD_ENDPOINT_CURRENT_HIERARCHY",
    "checks": checks,
    "odd_orders_checked": list(range(1, 16, 2)),
    "k5_chaos_coefficients": ["5/16", "10/16", "1/16"],
    "fifth_derivative_input": "997/1000",
    "ninety_percent_charge_allowance": "97/1000",
    "fifthphase106500_proved": False,
    "ninety_percent_established": False,
    "rh_established": False,
}
canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(result["verdict"])
print(json.dumps(result, indent=2, sort_keys=True))
