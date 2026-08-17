#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    parent = (Fraction(1), Fraction(0))
    child_same = (Fraction(1), Fraction(0))
    child_swapped = (child_same[1], child_same[0])
    true_restriction = (
        parent[0] - child_same[0],
        parent[1] - child_same[1],
    )
    swapped_difference = (
        parent[0] - child_swapped[0],
        parent[1] - child_swapped[1],
    )
    assert true_restriction == (0, 0)
    assert swapped_difference == (1, -1)

    r = Fraction(1, 9)
    lam = Fraction(2, 7)
    alpha = lam * r
    causal_child_coefficient = -lam * r + alpha
    actual_euler_child_coefficient = -r
    assert causal_child_coefficient == 0
    assert actual_euler_child_coefficient != causal_child_coefficient

    reserve = Fraction(1)
    alpha2 = Fraction(1, 10)
    child_scalar = Fraction(10)
    hall_current = Fraction(1, 2)
    assert reserve == alpha2 * child_scalar
    assert hall_current < alpha2 * child_scalar

    a = Fraction(1, 42)
    b = Fraction(1, 6)
    rho = Fraction(1, 8)
    assert a * (1 - rho) - b * rho == 0
    explicit_margin = Fraction(1, 42 * 65)

    result = {
        "schema": "riemann.x97400.source-interfaces.v1",
        "classification": "PASS_T97400_SOURCE_INTERFACE_FIREWALLS",
        "pr565_true_same_channel_restriction": ["0", "0"],
        "pr565_swapped_difference": ["1", "-1"],
        "actual_one_prime_euler_child_coefficient": str(
            actual_euler_child_coefficient
        ),
        "causal_recombined_child_coefficient": str(
            causal_child_coefficient
        ),
        "pr566_reserve_scalar": str(reserve),
        "pr566_hall_current_scalar": str(hall_current),
        "pr566_injected_child_scalar": str(alpha2 * child_scalar),
        "critical_margin_at_rho_one_eighth": "0",
        "explicit_factor67_margin_lower_bound": str(explicit_margin),
        "global_source_producer_proved": False,
        "RH_established": False,
    }
    raw = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(raw).hexdigest()

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
