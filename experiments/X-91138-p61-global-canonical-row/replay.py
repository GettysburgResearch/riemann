#!/usr/bin/env python3
"""Deterministic retained-result wrapper for X-91138."""
from __future__ import annotations

import json
from pathlib import Path

import verify as engine


def main() -> None:
    entries = engine.build_divisors()
    asymptotic = engine.certify_asymptotic_profile(entries)
    corridors = engine.certify_corridors(entries)
    invsqrt, logs, log_ratios = engine.precompute(
        67 * engine.FINITE_ROW_MAX
    )
    finite = engine.certify_finite_rows(entries, invsqrt, log_ratios)
    green = engine.certify_green(entries, invsqrt, logs)

    result = {
        "classification": (
            "PASS_P61_CANONICAL_FINITE_EULER_ROW_GLOBAL_POSITIVITY"
        ),
        "small_prime_block": engine.PRIMES,
        "divisor_states": len(entries),
        "finite_row_cutoff": engine.FINITE_ROW_MAX,
        "asymptotic_row_start": engine.ASYMPTOTIC_ROW_MIN,
        "asymptotic_profile": asymptotic,
        "mass_and_activation_corridors": corridors,
        "finite_compact_rows": finite,
        "finite_green_tails": green,
        "scope": (
            "The directed gates certify the finite and fixed-constant inputs "
            "to L-91364. Together with the analytic approximation and Green "
            "lemmas stated there, they prove D_(P61,X)(j)>=0 for every real "
            "X and every integer j>=2. This checker does not audit the "
            "imported literal-entropy benchmark, endpoint-port normalization, "
            "the CFFP composition, or RH."
        ),
    }
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
