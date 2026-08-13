#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
import json
import random
import sympy as sp


def run():
    checks = 0
    r, U, V = sp.symbols("r U V", positive=True)
    lhs = 4*(1-r**2)*U - 3*(1-r)*V
    rhs = (1-r)*(4*r*U-3*V) + 4*(1-r)*U
    assert sp.expand(lhs-rhs) == 0
    checks += 1

    rng = random.Random(91424)
    max_level_mass = Fraction(0)
    for _ in range(100):
        level = [Fraction(1)]
        for depth in range(10):
            nxt = []
            for mass in level:
                k = rng.randint(0, 2)
                raw = [Fraction(rng.randint(0, 40), 100) for _ in range(k)]
                total = sum(raw, Fraction(0))
                if total > 1:
                    raw = [q/total for q in raw]
                nxt.extend(mass*q for q in raw)
            level = nxt
            total_level = sum(level, Fraction(0))
            assert total_level <= 1
            max_level_mass = max(max_level_mass, total_level)
            checks += 1

    assert Fraction(1,67) < Fraction(1844367547103, 10**14)
    checks += 1

    return {
        "verdict": "PASS_X_91424_SUBSTOCHASTIC_LEAST_PRIME_TELESCOPE",
        "checks": checks,
        "maximum_level_mass": str(max_level_mass),
        "scope": "finite algebra/tree controls only; the complete RH proof proposal requires independent verification",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
