#!/usr/bin/env python3
"""Reproducible checks for the dynamics lane; standard-library only.

Exact checks use Fraction/integer Sturm chains. Decimal-looking output from
cmath/math is exploratory floating point, never an interval certificate.
"""
from __future__ import annotations

import argparse
import cmath
from fractions import Fraction
import json
from math import comb, factorial, gcd, lcm, pi
from pathlib import Path


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def primitive(p):
    """Clear denominators and divide by POSITIVE content, preserving signs."""
    p = trim([Fraction(x) for x in p])
    denominator = lcm(*(x.denominator for x in p))
    ints = [int(x * denominator) for x in p]
    content = gcd(*ints)
    return [x // content for x in ints] if content else [0]


def derivative(p):
    return trim([i * p[i] for i in range(1, len(p))] or [0])


def remainder(a, b):
    a = trim([Fraction(x) for x in a])
    b = trim([Fraction(x) for x in b])
    while len(a) >= len(b) and a != [0]:
        coefficient = a[-1] / b[-1]
        shift = len(a) - len(b)
        for j in range(len(b)):
            a[j + shift] -= coefficient * b[j]
        a = trim(a)
    return a


def sign(x):
    return (x > 0) - (x < 0)


def variations(values):
    values = [x for x in values if x]
    return sum(a != b for a, b in zip(values, values[1:]))


def sturm_counts(p):
    chain = [primitive(p), primitive(derivative(p))]
    while chain[-1] != [0]:
        rem = remainder(chain[-2], chain[-1])
        if rem == [0]:
            break
        chain.append(primitive([-x for x in rem]))
    at_minus_inf = [sign(q[-1]) * (-1) ** (len(q) - 1) for q in chain]
    at_plus_inf = [sign(q[-1]) for q in chain]
    at_zero = [sign(q[0]) for q in chain]
    total = variations(at_minus_inf) - variations(at_plus_inf)
    negative = variations(at_minus_inf) - variations(at_zero)
    return {
        "distinct_real_roots": total,
        "distinct_negative_roots": negative,
        "squarefree": len(chain[-1]) == 1,
        "chain_degrees": [len(q) - 1 for q in chain],
    }


def gamma(n, constant=Fraction(6, 5)):
    return constant if n == 0 else Fraction(factorial(n - 1), factorial(2 * n - 2))


def jensen(d, n=0, constant=Fraction(6, 5)):
    return [comb(d, j) * gamma(n + j, constant) for j in range(d + 1)]


def first_critical_scaled(d):
    """Root near -pi^2/4 of d/dw[J_d^0(w/d)], via bisection."""
    def h(w):
        term = total = 1.0
        for j in range(d - 1):
            term *= (d - 1 - j) / (j + 1) * (w / d) / (4 * (j + 0.5))
            total += term
            if abs(term) < 1e-24:
                break
        return total

    lo, hi = -5.0, -1.0
    assert h(lo) < 0 < h(hi)
    for _ in range(80):
        mid = (lo + hi) / 2
        if h(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def first_critical_threshold(d):
    w = first_critical_scaled(d)
    x = w / d
    term = total = d * x
    for j in range(1, d):
        term *= (d - j) / (j + 1) * x / (4 * (j - 0.5))
        total += term
        if abs(term) < 1e-24:
            break
    threshold = -total
    return {
        "degree": d,
        "scaled_critical_point": w,
        "threshold_C_d": threshold,
        "d_times_threshold_excess": d * (threshold - (pi - 2)),
    }


def bad_root(constant=1.2):
    z = pi / 2 + 0.2j
    for _ in range(30):
        f = constant + 2 - 2 * z * cmath.sin(z) - 2 * cmath.cos(z)
        derivative_f = -2 * z * cmath.cos(z)
        z -= f / derivative_f
    residual = abs(constant + 2 - 2 * z * cmath.sin(z) - 2 * cmath.cos(z))
    return {"real": z.real, "imag": z.imag, "residual": residual}


def heat_coefficients(p, t):
    """Exact coefficients of exp(-t D^2)p."""
    p = [Fraction(x) for x in p]
    out = [Fraction(0) for _ in p]
    for n, coefficient in enumerate(p):
        for k in range(n // 2 + 1):
            out[n - 2 * k] += coefficient * (-t) ** k * factorial(n) / (
                factorial(k) * factorial(n - 2 * k)
            )
    return trim(out)


def heat_bath_checks():
    rows = []
    for m in [0, 1, 2, 4, 8]:
        p = [0] * (2 * m + 3)
        p[2 * m] = p[2 * m + 2] = 1  # a=1
        collision = Fraction(1, 4 * m + 2)
        before = sturm_counts(heat_coefficients(p, collision * Fraction(9, 10)))
        after = sturm_counts(heat_coefficients(p, collision * Fraction(11, 10)))
        assert before["distinct_real_roots"] == 2 * m
        assert after["distinct_real_roots"] == 2 * m + 2
        at = heat_coefficients(p, collision)
        assert at[0] == at[1] == 0 and at[2] != 0
        rows.append({"m": m, "collision_time_exact": str(collision),
                     "real_roots_before": before["distinct_real_roots"],
                     "real_roots_after": after["distinct_real_roots"]})
    return rows


def run():
    exact_jensen = []
    for d in range(1, 25):
        counts = sturm_counts(jensen(d))
        assert counts["squarefree"]
        exact_jensen.append({"degree": d, **counts})
    # Every shift n>=1 is covered by the analytic Laguerre identity. These
    # finite exact samples check the normalization, not the infinite theorem.
    shifted_samples = []
    for n, d in [(1, 8), (1, 18), (2, 12), (10, 8)]:
        counts = sturm_counts(jensen(d, n))
        assert counts["distinct_negative_roots"] == d
        shifted_samples.append({"shift": n, "degree": d, **counts})
    return {
        "constant_exact": "6/5",
        "exact_jensen_sturm": exact_jensen,
        "exact_shifted_samples": shifted_samples,
        "exact_heat_bath_sturm": heat_bath_checks(),
        "floating_point_only": {
            "countermodel_quartet_positive_root": bad_root(),
            "C_star": pi - 2,
            "threshold_limit_coefficient": pi ** 3 / 32,
            "first_critical_thresholds": [first_critical_threshold(d) for d in
                                         [2, 3, 4, 8, 16, 17, 18, 32, 64, 128, 256, 1024]],
        },
        "scope": "Countermodels and polynomial heat flow; no computation of zeta zeros or RH proof.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    first_failure = next(row["degree"] for row in result["exact_jensen_sturm"]
                         if row["distinct_real_roots"] < row["degree"])
    print(json.dumps({"status": "PASS", "first_nonhyperbolic_degree_at_shift_0": first_failure,
                      "exact_heat_cases": len(result["exact_heat_bath_sturm"]),
                      "output": str(args.output)}, indent=2))
