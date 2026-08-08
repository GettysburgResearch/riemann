#!/usr/bin/env python3
"""Exact rational certificate for L-30502's 9/10 reserve."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    # Upper/lower radical certificates used in the two explicit pairs.
    checks = {
        "sqrt_2_over_3_upper": 3 * 817 * 817 > 2 * 1000 * 1000,
        "inv_sqrt3_lower": 3 * 577 * 577 < 1000 * 1000,
        "inv_sqrt3_upper": 3 * 578 * 578 > 1000 * 1000,
        "sqrt_2_over_7_upper": 7 * 535 * 535 > 2 * 1000 * 1000,
        "inv_sqrt5_lower": 5 * 447 * 447 < 1000 * 1000,
        "inv_sqrt5_upper": 5 * 448 * 448 > 1000 * 1000,
        "sqrt_2_over_11_upper": 11 * 427 * 427 > 2 * 1000 * 1000,
    }
    assert all(checks.values())

    pair_1 = Fraction(817 - 577, 1000) + Fraction(578, 8000)
    pair_2 = Fraction(535 - 447, 1000) + Fraction(448 * 3, 1000 * 56)
    tail = Fraction(15, 16) * Fraction(13, 11) * Fraction(427, 1000)
    total = pair_1 + pair_2 + tail
    assert total == Fraction(157933, 176000)
    assert total < Fraction(9, 10)

    result = {
        "schema": "X-30502-shifted-log-transport-reserve-v1",
        "classification": "EXACT_SHIFTED_LOG_TRANSPORT_RESERVE",
        "radical_square_checks": checks,
        "pair_1_upper": str(pair_1),
        "pair_2_upper": str(pair_2),
        "tail_upper": str(tail),
        "complete_upper": str(total),
        "reserve": "9/10",
        "does_not_prove": [
            "all-jet contraction",
            "signed objective control",
            "RH",
        ],
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out = Path(__file__).with_name("results") / "transport-verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
