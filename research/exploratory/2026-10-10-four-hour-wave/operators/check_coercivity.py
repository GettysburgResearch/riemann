#!/usr/bin/env python3
"""Exact arithmetic checker for the proposed codimension-18 source bound.

No floating-point operation participates in acceptance.  Every logarithm bound
comes from an explicit rational atanh series.  Classical pi bounds 3 < pi < 22/7
and gamma < H_n - log n are named mathematical inputs, not numerically inferred.
The source Fourier identity is imported from OPERATOR_AUDIT.md, sections O1-O3.
"""

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

def require(condition, detail="arithmetic acceptance failed"):
    if not condition:
        raise ArithmeticError(detail)


def log_rational_bounds(r: Q, n: int = 32):
    """Bounds log(r), r >= 1, using positive atanh terms and geometric tail."""
    require(r >= 1, "log bound requires r>=1")
    z = (r - 1) / (r + 1)
    lower = 2 * sum((z ** (2 * j + 1) / (2 * j + 1) for j in range(n)), Q())
    remainder = 2 * z ** (2 * n + 1) / ((2 * n + 1) * (1 - z * z))
    return lower, lower + remainder


def certify():
    log2_lo, log2_hi = log_rational_bounds(Q(2))
    require(log2_hi < Q(139, 200), "log2<139/200")
    require(log2_hi < Q(7, 10), "log2<7/10")
    harmonic128 = sum((Q(1, j) for j in range(1, 129)), Q())
    require(harmonic128 - 7 * log2_lo < Q(7, 12), "gamma<7/12")
    _, logpi_hi = log_rational_bounds(Q(22, 7), n=64)
    require(logpi_hi < Q(23, 20), "logpi<23/20")
    require(Q(7, 12) + Q(11, 7) + 3 * Q(139, 200) + Q(23, 20) < Q(27, 5), "Omega(0)>-27/5")
    require(Q(7, 5) ** 2 < 2, "sqrt2>7/5")  # hence Q_2 < 1/2.
    # exp(1)<3, hence log(3)>1.  The n>=3 factorial tail is <=1/4.
    require(1 + 1 + Q(1, 2) + Q(1, 4) < 3, "exp(1)<3")

    fixed_scale = 2 ** 80

    def v_lower(x: int):
        # For x>=0 each term is nonnegative; floor is directed downward.
        term_floors = sum(
            (fixed_scale * 16 * x) // ((4 * k + 1) * ((4 * k + 1) ** 2 + 4 * x))
            for k in range(65)
        )
        return -Q(32, 5) + Q(term_floors, fixed_scale)

    def p(x: int):
        return (Q(x) + Q(1, 4)) ** 2 / (Q(x) + Q(9, 4))

    minimum = None
    minimum_cell = None
    for left in range(4096):
        right = left + 1
        vl = v_lower(left)
        # V and P are increasing.  If vl<0 use the larger P, preserving a
        # lower bound even when the actual V crosses zero within the cell.
        product_lower = (p(right) if vl < 0 else p(left)) * vl
        margin = product_lower - right + 448
        require(margin > 0, ("frequency cell failed", left, str(margin)))
        if minimum is None or margin < minimum:
            minimum, minimum_cell = margin, left

    # For x>=4096, V(x)>=V(4096)>1 and P(x)>=x-7/4.  Therefore
    # P(x)V(x)>=x-7/4>x-448.  This proves the unbounded frequency tail.
    tail_v = v_lower(4096)
    require(tail_v > 1, "unbounded tail V(4096)>1")
    # On the 15-mode complement, ||phi||² <= ||phi'||²/(16²*pi²).
    # pi>3 gives a strict >=6/5 coercivity constant after multiplication b=3/2.
    require(Q(3, 2) * (1 - Q(448, 9 * 16 ** 2)) >= Q(6, 5), "primitive constant >=6/5")

    return {
        "status": "EXACT_ARITHMETIC_ACCEPT",
        "scope": "source multiplier lower bound and codimension-18 primitive coercivity at L=1",
        "gamma_prefix_last_index": 64,
        "frequency_variable": "x=omega^2",
        "covered_cells": 4096,
        "covered_compact": "[0,4096]",
        "unbounded_tail": "x>=4096 by monotonicity and V(4096)>1",
        "strict_smallest_cell_margin": {"cell": minimum_cell, "lower": str(minimum)},
        "tail_v_lower": str(tail_v),
        "classical_inputs": ["3<pi<22/7", "gamma<H_128-log(128)", "digamma partial fraction identity"],
        "not_authenticated": ["xi/Weil terminal source adapter", "effective matrix positivity", "all-window positivity"],
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))
