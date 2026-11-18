#!/usr/bin/env python3
"""Arb checks for the Q2-weighted vector Rolle bound."""
from fractions import Fraction
import json
from math import comb, factorial
from pathlib import Path

from flint import arb, ctx


def block_coefficient(height):
    v = arb(height)
    h = v.log()
    log_two = arb(2).log()
    pi3 = 3 * arb.pi()
    radius_ratio = 1 + (log_two + arb("1.005").log()) / h
    m_cap = arb("0.5025")
    units = []
    remainders = []
    for j in range(3):
        ratio_power = radius_ratio ** (2 * j)
        diagonal = 1 / arb(2 * j + 1)
        diagonal += (arb("1.15") + 2 * (log_two + 4 / v) * ratio_power) / h
        corrections = pi3 * (m_cap + (m_cap + 3 / v) * ratio_power) / h
        units.append(((arb("1.2") + pi3 / v) * diagonal + corrections).sqrt() / 2**j)
        remainders.append(12 * factorial(j) * 4**j * v ** (-arb(3) / 8) / (h**j * h.sqrt()))
    sqrt_two = arb(2).sqrt()
    q_norm = 1 + sqrt_two
    q_slope = sqrt_two * log_two
    q_acceleration = q_slope * log_two
    phase = arb("0.67")
    a0 = units[0] + q_norm * remainders[0]
    a1 = units[1] + phase * units[0] / h
    a1 += q_norm * remainders[1] + q_slope * remainders[0] / h
    a2 = units[2] + 2 * phase * units[1] / h + (phase**2 + 1/v) * units[0] / h**2
    a2 += q_norm * remainders[2] + 2 * q_slope * remainders[1] / h
    a2 += q_acceleration * remainders[0] / h**2
    return 2 * (a1 + 15 * a0 / (v*h)) * (a2 + 30 * a1 / (v*h) + 600 * a0 / (v*h)**2)


def tail_bound(height, blocks=8):
    total = arb(0)
    for j in range(blocks):
        start = height * 2**j
        total += block_coefficient(start) * arb(start).log()**4 / start
    cutoff = height * 2**blocks
    h, d = arb(cutoff).log(), arb(2).log()
    moments = [2, 2, 6, 26, 150]
    polynomial = sum(comb(4, j) * moments[j] * h**(4-j) * d**j for j in range(5))
    return total + block_coefficient(cutoff) * polynomial / cutoff


if __name__ == "__main__":
    ctx.prec = 128
    assert 1 + 2 / arb(200).sqrt() < arb("1.15")
    assert 2 * Fraction("0.5025") == Fraction("1.005")
    result_path = Path(__file__).resolve().parents[1] / "experiments/results/prime64_q2_partial_tail_observation_y10000.json"
    partial = json.loads(result_path.read_text())["rows"][-1]
    assert partial["height"] == 10000
    finite = partial["finite_C2_partial"]
    lo_int, lo_exp = finite["dyadic_lower"]
    hi_int, hi_exp = finite["dyadic_upper"]
    lo = Fraction(int(lo_int)) * Fraction(2) ** lo_exp
    hi = Fraction(int(hi_int)) * Fraction(2) ** hi_exp
    assert lo > Fraction("0.61649875288731141829")
    assert hi < Fraction("0.61649875288731141830")
    assert arb("0.61649875288731141830") + tail_bound(10000) < arb("2.35771")
    assert tail_bound(10000000) + arb("0.00025") < arb("0.0061649875288731141829")
    for height in (400, 10000, 10000000, 200000000):
        print(f"{height}: {tail_bound(height)}")
