#!/usr/bin/env python3
"""Exact finite replay for T-105655.

This script authenticates the binding two-factor correction, the complete
one-factor phase/reserve theorem on a declared rational grid, and a large
collinear two-factor CTI regression.  It does not prove the general complex
multipacket inequality or RH.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def mmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def inv2(a):
    d = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    assert d != 0
    return [[a[1][1] / d, -a[0][1] / d],
            [-a[1][0] / d, a[0][0] / d]]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def g2(a, b, s):
    return [[F(1, 2 * a + s), F(1, a + b + s)],
            [F(1, a + b + s), F(1, 2 * b + s)]]


def model_overlap_two(a, b, h):
    g0 = g2(a, b, 0)
    g2h = g2(a, b, 2 * h)
    g4h = g2(a, b, 4 * h)
    return tr(mmul(mmul(mmul(inv2(g0), g2h), inv2(g4h)), g2h))


def source_trace_two(a, b, h):
    return tr(mmul(inv2(g2(a, b, 0)), g2(a, b, h)))


def bprime_coeff(depths, i):
    d = depths[i]
    out = -F(1, 2 * d)
    for k, e in enumerate(depths):
        if k != i:
            out *= F(d - e, d + e)
    return out


def inner_derivative_coeff(depths, d):
    value = F(1)
    logarithmic = F(0)
    for c in depths:
        value *= F(d - c, d + c)
        logarithmic += -F(2 * c, d * d - c * c)
    return value * logarithmic


def cross_dirichlet_two(a, b, h):
    shallow = [a, b]
    deep = [a + 2 * h, b + 2 * h]
    return sum(inner_derivative_coeff(deep, d) / bprime_coeff(shallow, i)
               for i, d in enumerate(shallow))


def main():
    checks = 0

    # Binding counterexample.
    overlap = model_overlap_two(1, 2, 1)
    cross = cross_dirichlet_two(1, 2, 1)
    charge = F(2) - overlap
    old_phase_value = F(2) - cross
    assert overlap == F(147, 100); checks += 1
    assert cross == F(49, 60); checks += 1
    assert overlap != cross; checks += 1
    assert charge == F(53, 100); checks += 1
    assert old_phase_value == F(71, 60); checks += 1

    # Complete one-factor theorem on a declared exact grid.
    for delta in range(1, 81):
        for h in range(1, 81):
            overlap1 = F(delta * (delta + 2 * h), (delta + h) ** 2)
            defect = F(h * h, (delta + h) ** 2)
            reserve = F(h, 2 * delta + h)
            margin = F(h * delta * delta,
                       (delta + h) ** 2 * (2 * delta + h))
            assert F(1) - overlap1 == defect; checks += 1
            assert reserve - defect == margin; checks += 1
            assert margin > 0; checks += 1
            assert defect < reserve; checks += 1
            assert overlap1 > F(2 * delta, 2 * delta + h); checks += 1

    # Exact collinear two-factor CTI regression.
    minimum_margin = None
    minimum_fixture = None
    for a in range(1, 21):
        for b in range(1, 21):
            if a == b:
                continue
            for h in range(1, 21):
                source_reserve = F(2) - source_trace_two(a, b, h)
                phase_defect = F(2) - model_overlap_two(a, b, h)
                margin = source_reserve - phase_defect
                assert margin > 0
                checks += 1
                if minimum_margin is None or margin < minimum_margin:
                    minimum_margin = margin
                    minimum_fixture = [a, b, h]

    result = {
        "verdict": "PASS_X_105655_CAUCHY_TRANSLATION_TRACE_CORRECTION",
        "arithmetic_class": "EXACT_RATIONAL",
        "checks": checks,
        "binding_overlap": str(overlap),
        "binding_cross_dirichlet": str(cross),
        "binding_charge": str(charge),
        "rank_one_grid_complete": True,
        "collinear_two_factor_regression_complete": True,
        "minimum_collinear_margin": str(minimum_margin),
        "minimum_collinear_fixture": minimum_fixture,
        "general_complex_packet_cti_proved": False,
        "entire_xi_transfer_proved": False,
        "rh_established": False,
    }
    out = Path(__file__).with_name("results") / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(f"checks={checks}")


if __name__ == "__main__":
    main()
