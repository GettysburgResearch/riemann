#!/usr/bin/env python3
"""Finite arithmetic upper-bound certificate for the BSY logarithmic integral.

This is NOT a proof of RH and does NOT prove that the bounds vanish as N grows.

Let D = (1/(2*pi))*int_R log|zeta(1/2+it)|/(1/4+t*t) dt.
For real c_2,...,c_N put
  v_n = log(n)/n,
  G_mn = sum_{k>=1} {k/m}{k/n}/(k(k+1)).
The analytic inequality proved in the accompanying chat is
  D <= (1/2)*log((c^T G c)/(c^T v)^2), provided c^T v != 0.

The default computation uses a fixed RATIONAL vector with N=20.
It encloses every arithmetic operation and logarithm with mpmath.iv.
Digamma values are NOT taken from a floating-point special-function routine:
they are enclosed using recurrence, six Bernoulli terms, and a rigorous
first-neglected-term remainder for positive arguments.

References:
  BSY identity / truncation: https://arxiv.org/abs/1306.0856
  Arithmetic Hilbert space: https://arxiv.org/abs/1812.04309
  Digamma expansion and error: https://dlmf.nist.gov/5.11
    equations 5.11.2 and the positive-real remainder statement in section ii.

Requirements: mpmath (tested with 1.3.0).
Usage:
  python rh_arithmetic_certificate.py
  python rh_arithmetic_certificate.py --output rh_certificate_result.json
  python rh_arithmetic_certificate.py --table 200

The optional table additionally needs numpy, scipy, and threadpoolctl.
That table is floating-point exploration, NOT interval certification.
No zeta zeros or direct numerical zeta evaluations are used.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from functools import lru_cache
import json
import math
from pathlib import Path
import time
from typing import Any
import mpmath as mp

COEFFICIENTS_20 = [(11589423, 12500000), (4556417, 5000000), (13043019, 100000000), (76954681, 100000000), (-55503429, 100000000), (63105287, 100000000), (1877227, 100000000), (521469, 20000000), (-7632917, 20000000), (41728427, 100000000), (-41921, 1000000), (41237717, 100000000), (-35336207, 100000000), (-30063681, 100000000), (1424341, 100000000), (30018521, 100000000), (-2134239, 50000000), (16664863, 50000000), (-1568531, 6250000)]

BERNOULLI_OVER_ORDER = (
    Fraction(1, 12), Fraction(-1, 120), Fraction(1, 252),
    Fraction(-1, 240), Fraction(1, 132), Fraction(-691, 32760),
)

def interval_fraction(value: Fraction | int) -> Any:
    """An outward-rounded interval enclosing an exact rational number."""
    value = Fraction(value)
    return mp.iv.mpf(value.numerator) / value.denominator

@lru_cache(maxsize=None)
def digamma_interval(value: Fraction) -> Any:
    """Enclose psi(value) for a strictly positive exact rational value."""
    if value <= 0:
        raise ValueError("The digamma enclosure requires a positive argument.")
    z = interval_fraction(value)
    y = z + 20
    result = mp.iv.log(y) - 1 / (2 * y)
    for j, coefficient in enumerate(BERNOULLI_OVER_ORDER, start=1):
        result -= interval_fraction(coefficient) / y ** (2 * j)
    for j in range(20):
        result -= 1 / (z + j)
    # B_14 / 14 = 1/12. For positive y the error after six terms
    # is bounded in absolute value by the first neglected term.
    radius = 1 / (12 * y ** 14)
    return result + mp.iv.mpf([-1, 1]) * radius

def gram_entry_interval(m: int, n: int) -> Any:
    """Finite, rigorously enclosed evaluation of the infinite Gram series."""
    if m < 2 or n < 2:
        raise ValueError("Indices must be at least 2.")
    period = math.lcm(m, n)
    result = mp.iv.mpf(0)
    for r in range(1, period + 1):
        numerator = (r % m) * (r % n)
        if not numerator:
            continue
        residue_product = Fraction(numerator, m * n)
        weight = (
            digamma_interval(Fraction(r + 1, period))
            - digamma_interval(Fraction(r, period))
        ) / period
        result += interval_fraction(residue_product) * weight
    return result

def certify() -> dict[str, Any]:
    """Certify the bound for the fixed rational N=20 witness."""
    mp.iv.dps = 35
    digamma_interval.cache_clear()
    coefficients = [Fraction(p, q) for p, q in COEFFICIENTS_20]
    energy = mp.iv.mpf(0)
    for m, cm in enumerate(coefficients, start=2):
        for n in range(m, 21):
            cn = coefficients[n - 2]
            factor = 1 if m == n else 2
            energy += (
                factor * interval_fraction(cm * cn)
                * gram_entry_interval(m, n)
            )
    value = sum(
        (interval_fraction(c) * mp.iv.log(n) / n
         for n, c in enumerate(coefficients, start=2)),
        mp.iv.mpf(0),
    )
    if not (value.a > 0 and energy.a > 0):
        raise ArithmeticError("The enclosures did not prove positivity.")
    bound = mp.iv.log(energy / (value * value)) / 2
    threshold = mp.iv.mpf("0.00834")
    verified = bool(bound.b < threshold.a)
    if not verified:
        raise ArithmeticError("The requested upper-bound certificate failed.")
    return {
        "status": "finite interval-arithmetic certificate; not a proof of RH",
        "N": 20,
        "coefficient_order": "n = 2,...,20",
        "rational_coefficients": COEFFICIENTS_20,
        "P_derivative_at_1_interval": str(value),
        "quadratic_energy_interval": str(energy),
        "one_sided_upper_bound_interval": str(bound),
        "proved_D_less_than": "0.00834",
        "comparison_verified": verified,
        "interval_decimal_precision": mp.iv.dps,
        "mpmath_version": mp.__version__,
        "digamma_method": (
            "shift by 20; Bernoulli terms B2 through B12; "
            "absolute remainder <= 1/(12*(x+20)^14)"
        ),
        "limitations": (
            "The result relies on the proved analytic inequality and the "
            "correctness of interval arithmetic. It is not a formal proof "
            "assistant certificate and gives no all-N decay estimate."
        ),
    }

def exploratory_table(max_n: int) -> list[dict[str, Any]]:
    """Optional floating-point evaluations. These are NOT certified."""
    if max_n < 2:
        raise ValueError("max_n must be at least 2.")
    try:
        import numpy as np
        import scipy.linalg as la
        from scipy.special import digamma
        from threadpoolctl import threadpool_limits
    except ImportError as exc:
        raise RuntimeError(
            "The optional table needs numpy, scipy, and threadpoolctl."
        ) from exc
    gram = np.empty((max_n - 1, max_n - 1), dtype=float)
    with threadpool_limits(limits=1):
        for m in range(2, max_n + 1):
            for n in range(m, max_n + 1):
                period = math.lcm(m, n)
                r = np.arange(1, period + 1, dtype=np.int64)
                weights = (
                    digamma((r + 1) / period) - digamma(r / period)
                ) / period
                value = np.dot((r % m) / m * (r % n) / n, weights)
                gram[m - 2, n - 2] = gram[n - 2, m - 2] = value
        sizes = sorted(set(
            [n for n in [2, 3, 5, 10, 20, 40, 80, 120, 200]
             if n <= max_n] + [max_n]
        ))
        rows = []
        for n in sizes:
            indices = np.arange(2, n + 1)
            vector = np.log(indices) / indices
            coefficients = la.solve(
                gram[:n - 1, :n - 1], vector, assume_a="pos"
            )
            q = float(vector @ coefficients)
            if not (0 < q <= 1):
                raise ArithmeticError(
                    "Floating-point projection norm out of range; "
                    "increase numerical precision."
                )
            rows.append({
                "N": n, "E_N_approx": 1 - q,
                "U_N_approx": -0.5 * math.log(q),
                "certified": False,
            })
    return rows

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the result as JSON.")
    parser.add_argument(
        "--table", type=int, metavar="N",
        help="Also compute an uncertified floating-point table up to N.",
    )
    args = parser.parse_args()
    start = time.monotonic()
    result = certify()
    if args.table is not None:
        result["exploratory_table"] = exploratory_table(args.table)
    result["elapsed_seconds"] = time.monotonic() - start
    text = json.dumps(result, indent=2)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
