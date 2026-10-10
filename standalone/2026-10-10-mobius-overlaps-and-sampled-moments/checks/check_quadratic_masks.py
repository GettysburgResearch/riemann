#!/usr/bin/env python3
"""Exact finite guards for the quadratic square-part argument; not a sieve proof."""
import argparse
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


COUNTS = Counter()


def require(ok, category, detail=""):
    COUNTS[category] += 1
    if not ok:
        raise RuntimeError(category + ": " + detail)


def mul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c-b*d)


def power(x, n):
    answer = (1, 0)
    while n:
        if n & 1:
            answer = mul(answer, x)
        x = mul(x, x)
        n //= 2
    return answer


def norm(x):
    a, b = x
    return a*a-a*b+b*b


PRIMES = ((7, 4, (-2, -3)), (13, 9, (1, -3)))
UNITS = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1))


def local_quad(u, panel):
    q, omega, _ = panel
    value = (u[0] + omega*u[1]) % q
    if value == 0:
        return 0
    result = pow(value, (q-1)//2, q)
    if result == 1:
        return 1
    if result == q-1:
        return -1
    raise RuntimeError("Euler criterion did not produce a sign")


def symbol(u, support):
    result = 1
    for j, panel in enumerate(PRIMES):
        if support & (1 << j):
            result *= local_quad(u, panel)
    return result


def run():
    for q, omega, generator in PRIMES:
        require(norm(generator) == q, "native_prime_ideals")
        require((omega*omega+omega+1) % q == 0, "native_prime_ideals")
        require((generator[0]+omega*generator[1]) % q == 0, "native_prime_ideals")
    for unit in UNITS:
        require(norm(unit) == 1, "units")

    # Actual Eisenstein elements, including square bases that meet the remainder.
    overlap_cases = 0
    for e0, e1 in itertools.product(range(9), repeat=2):
        exponents = (e0, e1)
        v, a, u0 = (1, 0), (1, 0), (1, 0)
        v_support = 0
        for j, (exponent, panel) in enumerate(zip(exponents, PRIMES)):
            generator = panel[2]
            v = mul(v, power(generator, exponent//2))
            a = mul(a, power(generator, exponent % 2))
            u0 = mul(u0, power(generator, exponent))
            if exponent//2:
                v_support |= 1 << j
        require(mul(mul(v, v), a) == u0, "literal_square_factorization")
        for unit, column in itertools.product(UNITS, range(4)):
            u = mul(unit, u0)
            lhs = symbol(u, column)
            mask = int((v_support & column) == 0)
            rhs = mask * symbol(mul(unit, a), column)
            require(lhs == rhs, "literal_quadratic_square_masks")
            if any(e >= 3 and e % 2 for e in exponents):
                overlap_cases += 1

    # Independent exact incidence reconstruction on all residue classes mod 91.
    incidence_tuples = 0
    for degree in range(1, 5):
        for columns in itertools.product(range(4), repeat=degree):
            incidence_tuples += 1
            labels = {}
            for prime_index in range(2):
                positions = tuple(i for i, c in enumerate(columns) if c & (1 << prime_index))
                if positions:
                    labels[positions] = labels.get(positions, 0) | (1 << prime_index)
            singleton = 0
            shared = []
            for positions, support in labels.items():
                if len(positions) == 1:
                    singleton |= support
                else:
                    shared.append((len(positions), support))
            for integer_row in range(1, 92):
                u = (integer_row, 0)
                lhs = 1
                for column in columns:
                    lhs *= symbol(u, column)
                rhs = symbol(u, singleton)
                for multiplicity, support in shared:
                    rhs *= symbol(u, support)**multiplicity
                require(lhs == rhs, "native_incidence_character_identity")

    # Negative controls: an even or sixth power is still zero at a nonunit.
    u = PRIMES[0][2]
    require(symbol(u, 1)**2 == 0 and symbol(u, 1)**2 != 1, "adversarial_principal_mask")
    require(symbol(u, 1)**6 == 0 and symbol(u, 1)**6 != 1, "adversarial_principal_mask")

    # Exact dyadic sums, including switches below and above the physical range.
    switch_locations = Counter()
    for h, p, r in itertools.product(range(9), range(9), range(-4, 13)):
        root_h, product, pointwise = F(2)**h, F(2)**p, F(2)**r
        height = root_h**2
        switch = root_h*pointwise/product
        location = "below" if switch < 1 else "above" if switch > root_h else "inside"
        switch_locations[location] += 1
        dyads = [F(2)**v for v in range(h+1)]
        energy = sum(min(v*product**2, height*pointwise**2/v) for v in dyads)
        require(energy <= 4*root_h*product*pointwise, "dyadic_switch_budget")
        require(sum(height*product/v for v in dyads) <= 2*height*product, "geometric_diagonal_budget")

    # Affine h dependence: endpoint certificates cover every 1 <= h <= 11/10.
    certificates = []
    for h in (F(1), F(11, 10)):
        gamma = F(9, 17)
        first_margin = (h+3) - (6*F(7, 8) + h + gamma*(1-6*F(7, 8)))
        second_margin = (h+3) - (6*F(7, 8) + h/2 + gamma*(1-5*F(7, 8)))
        require(first_margin == 0, "degree_three_cutoff_certificate")
        require(second_margin > 0, "degree_three_cutoff_certificate")
        certificates.append({"h": str(h), "first_margin": str(first_margin), "second_margin": str(second_margin)})

    return {
        "status": "PASS",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "exact integers and fractions; primitive quadratic symbols over F_7 and F_13",
        "native_prime_ideals": [{"norm": q, "omega": w, "generator": list(g)} for q, w, g in PRIMES],
        "row_valuation_range": [0, 8],
        "square_mask_cases_with_overlapping_base": overlap_cases,
        "incidence_tuple_count": incidence_tuples,
        "incidence_degrees": [1, 2, 3, 4],
        "complete_integer_residue_classes": 91,
        "dyadic_switch_locations": dict(sorted(switch_locations.items())),
        "degree_three_affine_endpoint_certificates": certificates,
        "checks": dict(sorted(COUNTS.items())),
        "total_checks": sum(COUNTS.values()),
        "scope": "Finite primitive identities and exact exponent guards only. No pointwise cancellation, reciprocal-L premise, large sieve, infinite moment, or zero-free theorem is tested."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(result)
    else:
        print(result, end="")
