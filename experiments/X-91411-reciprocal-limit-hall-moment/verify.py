#!/usr/bin/env python3
"""Exact P61 reciprocal-limit shifted-eight transport moment certificate."""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from math import isqrt, prod
import json
from pathlib import Path

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
DEN = 10**30


def divisors_with_mu():
    values = [(1, 1)]
    for prime in PRIMES:
        values += [(d * prime, -mu) for d, mu in list(values)]
    return sorted(values)


def sqrt_bounds(n):
    scaled = n * DEN * DEN
    lower = isqrt(scaled)
    upper = lower if lower * lower == scaled else lower + 1
    return lower, upper


def fstr(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main():
    divisors = divisors_with_mu()
    assert len(divisors) == 2**18
    modulus = prod(PRIMES)
    evens = [{"d": d, "cap": modulus // d} for d, mu in divisors if mu == 1]
    odds = [{"d": d, "dem": modulus // d} for d, mu in divisors if mu == -1]

    even_index = 0
    capacity = 0
    demand = 0
    minimum_margin = None
    minimum_threshold = None
    for odd in odds:
        while even_index < len(evens) and evens[even_index]["d"] <= odd["d"] + 8:
            capacity += modulus // evens[even_index]["d"]
            even_index += 1
        demand += odd["dem"]
        margin = capacity - demand
        if minimum_margin is None or margin < minimum_margin:
            minimum_margin = margin
            minimum_threshold = odd["d"]
    assert minimum_margin is not None and minimum_margin > 0
    hall_margin = Fraction(minimum_margin, modulus)
    assert hall_margin > Fraction(1, 100)

    evens = [{"d": d, "cap": modulus // d} for d, mu in divisors if mu == 1]
    odds = [{"d": d, "dem": modulus // d} for d, mu in divisors if mu == -1]
    available = deque()
    even_index = 0
    coefficients = {}
    flow_edges = 0
    max_upward = 0
    upward_units = 0
    for odd in odds:
        while even_index < len(evens) and evens[even_index]["d"] <= odd["d"] + 8:
            available.append(evens[even_index])
            even_index += 1
        remaining = odd["dem"]
        while remaining:
            while available and available[0]["cap"] == 0:
                available.popleft()
            assert available
            even = available[0]
            take = min(remaining, even["cap"])
            coefficients[odd["d"]] = coefficients.get(odd["d"], 0) + take
            coefficients[even["d"]] = coefficients.get(even["d"], 0) - take
            if even["d"] > odd["d"]:
                upward_units += take
                max_upward = max(max_upward, even["d"] - odd["d"])
            even["cap"] -= take
            remaining -= take
            flow_edges += 1

    lower_numerator = 0
    upper_numerator = 0
    for d, coefficient in coefficients.items():
        lower, upper = sqrt_bounds(d)
        if coefficient >= 0:
            lower_numerator += coefficient * lower
            upper_numerator += coefficient * upper
        else:
            lower_numerator += coefficient * upper
            upper_numerator += coefficient * lower
    moment_lower = Fraction(lower_numerator, modulus * DEN)
    moment_upper = Fraction(upper_numerator, modulus * DEN)
    assert moment_lower > 18

    result = {
        "classification": "PASS_P61_RECIPROCAL_LIMIT_HALL_MOMENT",
        "divisor_states": len(divisors),
        "common_denominator": str(modulus),
        "minimum_shift8_hall_margin": fstr(hall_margin),
        "minimum_shift8_hall_margin_decimal": float(hall_margin),
        "minimum_margin_threshold": minimum_threshold,
        "flow_edges": flow_edges,
        "largest_upward_edge": max_upward,
        "upward_mass": fstr(Fraction(upward_units, modulus)),
        "moment_lower": fstr(moment_lower),
        "moment_upper": fstr(moment_upper),
        "moment_lower_decimal": float(moment_lower),
        "moment_upper_decimal": float(moment_upper),
        "certified_moment_above": "18",
        "scope": "Exact integer common-denominator flow and directed radical interval for the reciprocal limiting score measures. The analytic finite-parameter transfer is separate and RH is not proved.",
    }
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
