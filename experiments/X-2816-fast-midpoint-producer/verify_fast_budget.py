#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json

U80 = Fraction(1, 2**64)
MAX_TERMS = 4_200_000_000
TERM_ULPS = 2**12
PAIRWISE_DEPTH = 64
WEIGHT_BOUND = 11_000_001
QUAD_PHASE = Fraction(1, 10**12)
PHASE_GRID = Fraction(1, 20_000_000_000)
ALGEBRAIC = Fraction(1, 90_000_000_000_000)


def fjson(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def verify() -> dict[str, object]:
    term = MAX_TERMS * TERM_ULPS * U80
    gamma = PAIRWISE_DEPTH * U80 / (1 - PAIRWISE_DEPTH * U80)
    pair = gamma * WEIGHT_BOUND
    total = term + pair + QUAD_PHASE + PHASE_GRID + ALGEBRAIC

    assert term < Fraction(1, 1_070_000)
    assert pair < Fraction(1, 25_000_000_000)
    assert total < Fraction(1, 1_000_000)

    return {
        "schema": "riemann.fast-midpoint-hardware-budget.v1",
        "status": "EXACT_GLOBAL_MOAT_VERIFIED",
        "contract": {
            "radix": 2,
            "long_double_mantissa_bits": 64,
            "quad_mantissa_bits": 113,
            "rounding": "nearest",
            "contraction": "disabled",
            "maximum_terms": MAX_TERMS,
            "per_term_absolute_rounding_ulps": TERM_ULPS,
            "pairwise_depth": PAIRWISE_DEPTH,
            "absolute_weight_bound": WEIGHT_BOUND,
        },
        "components": {
            "term_evaluation": fjson(term),
            "pairwise_summation": fjson(pair),
            "quad_phase_arithmetic": fjson(QUAD_PHASE),
            "phase_grid_taylor": fjson(PHASE_GRID),
            "segment_algebraic": fjson(ALGEBRAIC),
            "total": fjson(total),
        },
        "compact": {
            "term_evaluation_lt": "1/1070000",
            "pairwise_summation_lt": "1/25000000000",
            "total_lt": "1/1000000",
        },
        "proof_boundary": (
            "The exact arithmetic here checks the global composition once the "
            "L-2818 per-term 4096-ulps audit and the platform contract are verified."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
