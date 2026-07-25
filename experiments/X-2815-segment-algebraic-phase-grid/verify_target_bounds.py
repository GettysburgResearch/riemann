#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json

SEGMENT_SIZE = 20_000_000
FIRST_SEGMENT = 2000
LOW = 2 + FIRST_SEGMENT * SEGMENT_SIZE
MID = LOW + SEGMENT_SIZE // 2
HALF = SEGMENT_SIZE // 2
T = Fraction(94_184_072_727_073, 20)


def atanh_tail(zeta: Fraction, J: int) -> Fraction:
    if not (Fraction(0) <= zeta < 1) or J < 0:
        raise ValueError("require 0<=zeta<1 and J>=0")
    return Fraction(2) * zeta ** (2 * J + 3) / ((2 * J + 3) * (1 - zeta * zeta))


def invsqrt_relative_tail(beta: Fraction, J: int) -> Fraction:
    if not (Fraction(0) <= beta < 1) or J < 0:
        raise ValueError("require 0<=beta<1 and J>=0")
    return beta ** (J + 1) / (1 - beta)


def fjson(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def verify() -> dict[str, object]:
    zeta = Fraction(HALF, 2 * MID - HALF)
    beta = Fraction(HALF, MID)
    assert zeta < Fraction(1, 8000)
    assert beta < Fraction(1, 4000)

    log_tail = atanh_tail(zeta, 3)
    phase_tail = T * log_tail
    assert phase_tail < Fraction(1, 10**23)

    sqrt_rel_tail = invsqrt_relative_tail(beta, 5)
    sqrt_abs_tail = Fraction(1, 200_000) * sqrt_rel_tail
    sqrt_rayleigh_tail = 10**11 * 9 * 2 * sqrt_abs_tail
    assert sqrt_rayleigh_tail < Fraction(1, 10**14)

    log_amplitude_tail = 10**11 * 2 * Fraction(1, 3) * Fraction(1, 200_000) * log_tail
    assert log_amplitude_tail < Fraction(1, 10**30)

    phase_rayleigh_tail = 11_000_000 * phase_tail
    assert phase_rayleigh_tail < Fraction(1, 9 * 10**15)

    algebraic_total = sqrt_rayleigh_tail + log_amplitude_tail + phase_rayleigh_tail
    assert algebraic_total < Fraction(1, 90_000_000_000_000)

    phase_grid_remainder = Fraction(1, 20_000_000_000)
    total_acceleration_moat = phase_grid_remainder + algebraic_total
    assert total_acceleration_moat < Fraction(1, 19_995_000_000)
    nonprime_gate = Fraction(1, 4_000_000_000)
    assert total_acceleration_moat < nonprime_gate / 4

    return {
        "schema": "riemann.segment-algebraic-phase-grid.v1",
        "status": "EXACT_TARGET_BOUNDS_VERIFIED",
        "target": {
            "cutoff": "100000000000",
            "carrier": fjson(T),
            "segment_size": SEGMENT_SIZE,
            "first_accelerated_segment": FIRST_SEGMENT,
            "first_low": LOW,
            "first_midpoint": MID,
            "half_width": HALF,
        },
        "series": {
            "atanh_order_J": 3,
            "reciprocal_sqrt_order_J": 5,
            "zeta": fjson(zeta),
            "beta": fjson(beta),
        },
        "proved": {
            "zeta_less_than": "1/8000",
            "beta_less_than": "1/4000",
            "log_tail": fjson(log_tail),
            "phase_tail": fjson(phase_tail),
            "sqrt_relative_tail": fjson(sqrt_rel_tail),
            "sqrt_rayleigh_tail": fjson(sqrt_rayleigh_tail),
            "log_amplitude_tail": fjson(log_amplitude_tail),
            "phase_rayleigh_tail": fjson(phase_rayleigh_tail),
            "algebraic_total": fjson(algebraic_total),
            "phase_grid_remainder": fjson(phase_grid_remainder),
            "total_acceleration_moat": fjson(total_acceleration_moat),
            "nonprime_gate": fjson(nonprime_gate),
        },
        "comparison": {
            "algebraic_total_lt": "1/90000000000000",
            "total_acceleration_moat_lt": "1/19995000000",
            "total_acceleration_moat_lt_quarter_nonprime_gate": True,
        },
        "proof_boundary": (
            "Exact rational verification of analytic truncation budgets only; "
            "implementation bin assignment, interval arithmetic, and complete prime coverage remain separate."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
