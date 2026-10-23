#!/usr/bin/env python3
"""Finite algebra checks for SHORT_CORE_CUBIC_TRANSFER.md.

These checks do not certify the analytic functional equations, contour
arguments, uniform Mobius estimates, or any zero-free half-plane.
No external packages or network access are required.
"""

from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import product
from math import gcd, prod
import json


def combine(*terms):
    out = {}
    for weight, vector in terms:
        for name, exponent in vector.items():
            out[name] = out.get(name, F(0)) + weight * exponent
    return {name: exponent for name, exponent in out.items() if exponent}


def expect(actual, expected):
    if actual != expected:
        raise RuntimeError(f"Mismatch: actual={actual!r}; expected={expected!r}")


def demand(condition, message):
    if not condition:
        raise RuntimeError(message)


def local_digit_check():
    cost = [F(0), F(1), F(1), F(1), F(1, 2), F(1)]
    changes = [cost[(j + 4) % 6] - cost[j] for j in range(6)]
    expect(changes, [F(1, 2), F(0), F(-1), F(0), F(1, 2), F(0)])
    demand(max(changes) == F(1, 2), "Fourth-power label costs more than q^(1/2)")
    # A six-divisible exponent still has a natural nonunit zero.
    for j in range(6):
        for in_label in (0, 1):
            raw_exponent = j + 4 * in_label
            for n_divisible in (False, True):
                actual_zero = n_divisible and raw_exponent > 0
                primitive_zero = n_divisible and raw_exponent % 6 != 0
                residual_zero = n_divisible and raw_exponent > 0 and raw_exponent % 6 == 0
                demand(actual_zero == (primitive_zero or residual_zero),
                       "Primitive reduction erased a natural nonunit zero")
    expect([cost[j] - F(j, 6) - F(11 * j, 6) for j in range(2, 6)],
           [F(-3), F(-5), F(-15, 2), F(-9)])
    expect([-F(j, 6) - F(5 * j, 6) for j in range(2, 6)],
           [F(-2), F(-3), F(-4), F(-5)])
    # Exact evaluations of the matching-prime local majorant at square norms.
    for root in (2, 3, 5, 7, 11):
        q = root * root
        local = 1 + F(q - 1, q) + F(q - 1) * (1 + F(1, q)) / (root**5 - 1)
        expect(local, 2 - F(q * (root - 1), root**5 - 1))
        demand(local < 2, "Matching-prime local majorant is not below two")
    return [str(x) for x in changes]


def selector_check():
    primes = (2, 3, 5)
    checks = 0
    for digits in product(range(6), repeat=len(primes)):
        core = prod(p**j for p, j in zip(primes, digits))
        for epowers in product((0, 1), repeat=len(primes)):
            sixth_root = prod(p**j for p, j in zip(primes, epowers))
            k = core * sixth_root**6
            for apowers in product((0, 1), repeat=len(primes)):
                a = prod(p**j for p, j in zip(primes, apowers))
                b = gcd(a, core)
                demand((k % a == 0) == (sixth_root % (a // b) == 0),
                       "Sixth-power row divisibility failed its exact selector")
                if k % a == 0:
                    demand(core % b == 0 and sixth_root % (a // b) == 0,
                           "Divisor assignment failed with shared core/root primes")
                checks += 1
    return checks


def reassembly_check(beta):
    x = {"D": F(2), "d": F(2), "H": F(-1), "C": F(-2)}
    outside = {"H": F(1), "D": F(-1), "d": F(-1), "S": F(-1)}
    label = {"d": F(1), "S": F(1)}
    one_component = combine((1, outside), (F(1, 6), x),
                            (F(1, 2), label), (1, {"L": F(11, 6)}))
    expect(one_component, {"H": F(5, 6), "D": F(-2, 3), "C": F(-1, 3),
                           "d": F(-1, 6), "S": F(-1, 2), "L": F(11, 6)})
    # Sum C and s, and bound the convergent/divisor d-weight by a subpower.
    A = dict(one_component)
    del A["d"]
    A = combine((1, A), (1, {"C": F(1), "S": F(1)}))
    expect(A, {"H": F(5, 6), "D": F(-2, 3), "C": F(2, 3),
               "S": F(1, 2), "L": F(11, 6)})

    base = {"H": F(1), "D": F(-1), "d": F(-1)}
    columns = {"D": F(1), "C": F(-1), "S": F(-1)}
    signed_s = {"S": beta - 1}
    short_count = combine((F(1, 6), x), (1, {"d": F(-1), "L": F(5, 6)}))
    short_fixed = combine((1, base), (1, columns), (1, signed_s), (1, short_count))
    expect(short_fixed, {"H": F(5, 6), "D": F(1, 3), "C": F(-4, 3),
                         "d": F(-5, 3), "S": beta - 2, "L": F(5, 6)})
    del short_fixed["d"]
    Bshort = combine((1, short_fixed), (1, {"C": F(1)}))
    full_count = combine((1, x), (1, {"d": F(-1)}))
    Bfull = combine((1, base), (1, columns), (1, signed_s), (1, full_count),
                    (1, {"C": F(1)}))
    expect(Bfull, {"D": F(2), "C": F(-2), "S": beta - 2})

    denom = 5 - 2 * beta
    a = (4 - 2 * beta) / denom
    b = (4 * beta - 2) / (5 * denom)
    c = (7 - 4 * beta) / (5 * denom)
    demand(min(a, b, c) >= 0 and a + b + c == 1,
           "Interpolation weights are not a convex combination")
    result = combine((a, A), (b, Bshort), (c, Bfull))
    expect(result, {"H": (3 - beta) / denom, "L": (7 - 3 * beta) / denom})
    cutoff = (2 - beta) / (7 - 3 * beta)
    expect(result["H"] + cutoff * result["L"], F(1))
    return result, cutoff


def main():
    changes = local_digit_check()
    selectors = selector_check()
    betas = sorted({F(1, 2), F(2, 3), F(3, 4), F(7, 8), F(1)} |
                   {F(j, 100) for j in range(50, 101)})
    for beta in betas:
        reassembly_check(beta)
    endpoint, cutoff = reassembly_check(F(1))
    expect(endpoint, {"H": F(2, 3), "L": F(4, 3)})
    expect(cutoff, F(1, 4))
    old_example = F(6, 7) / 6 + F(5, 6)
    new_example = F(6, 7) * F(5, 6) - F(2, 3) + F(1, 2) * F(11, 6)
    expect(old_example, F(41, 42))
    expect(new_example, F(27, 28))
    expect(old_example - new_example, F(1, 84))

    imported_beta = F("0.874886647039964")
    imported, imported_cutoff = reassembly_check(imported_beta)
    with localcontext() as context:
        context.prec = 35
        decimal = lambda q: str(Decimal(q.numerator) / Decimal(q.denominator))
        result = {
            "status": "all finite checks passed",
            "analytic_certification": False,
            "local_label_cost_changes": changes,
            "divisibility_selector_cases": selectors,
            "rational_beta_reassembly_cases": len(betas) + 1,
            "unconditional_H_exponent": str(endpoint["H"]),
            "unconditional_L_exponent": str(endpoint["L"]),
            "unconditional_cutoff_exponent": str(cutoff),
            "imported_beta_approximation": str(float(imported_beta)),
            "imported_H_exponent": decimal(imported["H"]),
            "imported_L_exponent": decimal(imported["L"]),
            "imported_cutoff_exponent": decimal(imported_cutoff),
            "trivial_overlap_example_gain": str(old_example - new_example),
        }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
