#!/usr/bin/env python3
"""Reconstruct the exact zero-anchor response-1 conditioning factor."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction


def coefficients(nodes: list[Fraction]) -> list[Fraction]:
    output: list[Fraction] = []
    for i, node in enumerate(nodes):
        denominator = Fraction(1)
        for j, other in enumerate(nodes):
            if i != j:
                denominator *= other - node
        output.append(-1 / denominator)
    return output


def main() -> None:
    nodes = [Fraction(0)] + [Fraction(1, 2 ** (2 * k)) for k in range(20, 4, -1)]
    beta = coefficients(nodes)
    condition = sum(abs(value) for value in beta)
    result = {
        "schema": "riemann.x9310-zero-anchor-conditioning.v1",
        "node_count": len(nodes),
        "positive_node_exponents": [2 * k for k in range(20, 4, -1)],
        "beta_zero": {
            "numerator": str(beta[0].numerator),
            "denominator": str(beta[0].denominator),
        },
        "l1_condition": {
            "numerator": str(condition.numerator),
            "denominator": str(condition.denominator),
        },
        "bound_power_of_two": 402,
        "verified_l1_below_bound": condition < 2**402,
        "verified_beta_zero_equals_minus_2_power_400": beta[0] == -(2**400),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode("ascii")
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    if not result["verified_l1_below_bound"] or not result["verified_beta_zero_equals_minus_2_power_400"]:
        raise SystemExit(1)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
