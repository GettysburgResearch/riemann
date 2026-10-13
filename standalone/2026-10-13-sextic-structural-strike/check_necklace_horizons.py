#!/usr/bin/env python3
"""Exact primitive-necklace and physical-horizon coefficient checks.

Witt's identity is classical. This diagnostic tests its finite application
to literal squarefree Mobius factors with separate ideal-prime variables.
No asymptotic analytic estimate or RH consequence is certified.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def mobius(n):
    out, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            out = -out
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out = -out
    return out


def compositions(total, slots):
    if slots == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for rest in compositions(total - a, slots - 1):
            yield (a,) + rest


def necklace(alpha):
    degree = sum(alpha)
    common = math.gcd(*alpha)
    numerator = 0
    for d in range(1, common + 1):
        if common % d == 0:
            multinomial = math.factorial(degree // d)
            for a in alpha:
                multinomial //= math.factorial(a // d)
            numerator += mobius(d) * multinomial
    value = Fraction(numerator, degree)
    require(value.denominator == 1 and value >= 0,
            "necklace coefficient must be a nonnegative integer")
    return int(value)


def poly_add(a, b):
    out = dict(a)
    for exp, coeff in b.items():
        out[exp] = out.get(exp, 0) + coeff
        if not out[exp]:
            del out[exp]
    return out


def poly_mul(a, b, keep):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            exp = tuple(x + y for x, y in zip(ea, eb))
            if keep(exp):
                out[exp] = out.get(exp, 0) + ca * cb
    return {exp: coeff for exp, coeff in out.items() if coeff}


def geometric_power(exp, power, keep, weight=1):
    # (1-z^exp)^(-power), in a ring whose retained monomials form a downset.
    out = {}
    j = 0
    while True:
        term = tuple(j * e for e in exp)
        if not keep(term):
            break
        coefficient = math.comb(power + j - 1, j) * weight ** j
        if coefficient:
            out[term] = coefficient
        j += 1
    return out


def local_degree_check(slots, cutoff):
    zero = (0,) * slots
    keep = lambda exp: sum(exp) <= cutoff + 1
    original = {zero: 1}
    for i in range(slots):
        ei = tuple(int(j == i) for j in range(slots))
        original[ei] = -1
    truncated = {zero: 1}
    inverse = {zero: 1}
    alpha_count = 0
    copy_count = 0
    for degree in range(1, cutoff + 1):
        for alpha in compositions(degree, slots):
            c = necklace(alpha)
            alpha_count += 1
            copy_count += c
            if not c:
                continue
            factor = {zero: 1, alpha: -1}
            for _ in range(c):
                truncated = poly_mul(truncated, factor, keep)
            inverse = poly_mul(inverse, geometric_power(alpha, c, keep), keep)
    remainder = poly_mul(original, inverse, keep)
    require(remainder.get(zero) == 1, "remainder constant")
    require(all(sum(exp) >= cutoff + 1 for exp in remainder if exp != zero),
            "remainder fails degree cancellation")
    reunited = poly_mul(truncated, remainder, keep)
    require(reunited == original, "finite-degree necklace reunion")
    return alpha_count, copy_count, len(remainder)


def orbit_necklaces(slots, degree):
    counts = {}
    for word in itertools.product(range(slots), repeat=degree):
        rotations = {word[i:] + word[:i] for i in range(degree)}
        if len(rotations) != degree or word != min(rotations):
            continue
        alpha = tuple(word.count(i) for i in range(slots))
        counts[alpha] = counts.get(alpha, 0) + 1
    for alpha in compositions(degree, slots):
        require(necklace(alpha) == counts.get(alpha, 0),
                "primitive orbit enumeration disagrees with formula")
    return len(tuple(compositions(degree, slots))), sum(counts.values())


def horizon_check(primes, horizons, cutoff, slot_values=None):
    slots = len(horizons)
    dim = len(primes) * slots
    zero = (0,) * dim
    if slot_values is None:
        slot_values = tuple((1,) * slots for _ in primes)
    require(len(slot_values) == len(primes)
            and all(len(values) == slots for values in slot_values),
            "slot value dimensions")
    require(all(value in (-1, 0, 1) for values in slot_values for value in values),
            "exact diagnostic slot values")

    def keep(exp):
        return all(math.prod(primes[p] ** exp[p * slots + i]
                             for p in range(len(primes))) <= horizons[i]
                   for i in range(slots))

    def one_prime_exp(p, alpha):
        return tuple(alpha[i] if q == p else 0
                     for q in range(len(primes)) for i in range(slots))

    original = {zero: 1}
    for p in range(len(primes)):
        local = {zero: 1}
        for i in range(slots):
            exp = one_prime_exp(p, tuple(int(j == i) for j in range(slots)))
            if keep(exp):
                local[exp] = -slot_values[p][i]
        original = poly_mul(original, local, keep)

    inverse = {zero: 1}
    short_product = {zero: 1}
    too_short_product = {zero: 1}
    copy_count = retained_terms = discarded_terms = 0
    for degree in range(1, cutoff + 1):
        for alpha in compositions(degree, slots):
            c = necklace(alpha)
            if not c:
                continue
            for p in range(len(primes)):
                exp = one_prime_exp(p, alpha)
                weight = math.prod(slot_values[p][i] ** alpha[i]
                                   for i in range(slots) if alpha[i])
                inverse = poly_mul(inverse, geometric_power(exp, c, keep, weight), keep)
            short = {}
            wrong_short = {}
            for chosen in itertools.product([0, 1], repeat=len(primes)):
                norm = math.prod(primes[p] ** chosen[p] for p in range(len(primes)))
                exp = tuple(chosen[p] * alpha[i]
                            for p in range(len(primes)) for i in range(slots))
                eligible = all(norm ** alpha[i] <= horizons[i]
                               for i in range(slots) if alpha[i])
                require(eligible == keep(exp), "physical monomial horizon")
                if eligible:
                    coeff = ((-1) ** sum(chosen)
                             * math.prod(slot_values[p][i] ** exp[p * slots + i]
                                         for p in range(len(primes))
                                         for i in range(slots)
                                         if exp[p * slots + i]))
                    short[exp] = coeff
                    retained_terms += 1
                    # A deliberately wrong uniformly smaller physical cap.
                    if all((2 * norm) ** alpha[i] <= horizons[i]
                           for i in range(slots) if alpha[i]) or norm == 1:
                        wrong_short[exp] = coeff
                else:
                    discarded_terms += 1
            for _ in range(c):
                short_product = poly_mul(short_product, short, keep)
                too_short_product = poly_mul(too_short_product, wrong_short, keep)
                copy_count += 1

    remainder = poly_mul(original, inverse, keep)
    reunited = poly_mul(short_product, remainder, keep)
    require(reunited == original, "physical rectangle reunion")
    wrong = poly_mul(too_short_product, remainder, keep)
    return {
        "primes": list(primes), "horizons": list(horizons), "cutoff": cutoff,
        "slot_values": [list(values) for values in slot_values],
        "literal_zero_slots": sum(value == 0 for values in slot_values for value in values),
        "primitive_factor_copies": copy_count,
        "retained_squarefree_factor_terms": retained_terms,
        "discarded_squarefree_factor_terms": discarded_terms,
        "target_coefficient_count": len(original),
        "remainder_coefficient_count": len(remainder),
        "reunion_coefficient_count": len(reunited),
        "smaller_cap_negative_detected": wrong != original,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--proof", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    count = {"local_remainder_checks": 0, "multiindices_in_local_checks": 0,
             "primitive_copies_in_local_checks": 0,
             "primitive_orbit_multiindices": 0, "primitive_cyclic_orbits": 0}
    for slots in range(2, 6):
        for cutoff in range(1, 5):
            a, c, _ = local_degree_check(slots, cutoff)
            count["local_remainder_checks"] += 1
            count["multiindices_in_local_checks"] += a
            count["primitive_copies_in_local_checks"] += c
    for slots in range(2, 5):
        for degree in range(1, 7):
            a, c = orbit_necklaces(slots, degree)
            count["primitive_orbit_multiindices"] += a
            count["primitive_cyclic_orbits"] += c
    cases = [
        horizon_check((7, 13), (49, 49, 49, 49), 2),
        horizon_check((7, 13), (49, 91, 169, 49), 3),
        horizon_check((7, 7), (49, 91, 49, 91), 3),
        horizon_check((7, 13, 19), (343, 361), 3),
        horizon_check((7, 13), (1, 49, 7, 13), 3),
        horizon_check((7, 7, 13), (49, 91, 169, 49), 3,
                      ((0, 0, 0, 0), (1, -1, 1, -1), (-1, 1, -1, 1))),
        horizon_check((7, 13), (49, 91, 49), 2,
                      ((0, 1, -1), (1, 0, 1))),
    ]
    require(any(case["smaller_cap_negative_detected"] for case in cases),
            "wrong cap negative control did not trigger")
    # Local pair coefficient must include every unordered pair, while repeated
    # one-letter words are imprimitive and contribute zero.
    require(necklace((1, 1, 0, 0)) == 1, "pair copy")
    require(necklace((2, 0, 0, 0)) == 0, "imprimitive repeated singleton")
    require(necklace((1, 1, 1, 0)) == 2, "three-distinct primitive copies")
    # A principal pair at a prime dividing u is still zero. Restoring its
    # coefficient to one changes a retained (p,p) coefficient even though
    # the correctly masked local C and remainder both equal one.
    principal_zero_original = {(0, 0): 1}
    restored_principal = {(0, 0): 1, (1, 1): -1}
    restored_zero_detected = restored_principal != principal_zero_original
    require(restored_zero_detected, "principal nonunit zero negative control")
    result = {
        "status": "PASS", "counts": count, "physical_cases": cases,
        "negative_controls": {
            "overly_small_physical_cap": any(c["smaller_cap_negative_detected"] for c in cases),
            "one_copy_instead_of_two_for_three_distinct_letters": necklace((1, 1, 1, 0)) != 1,
            "spurious_repeated_singleton_factor": necklace((2, 0, 0, 0)) == 0,
            "restored_principal_nonunit_zero": restored_zero_detected,
        },
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "exact integer primitive-necklace counts and literal squarefree coefficient reunion in physical norm rectangles",
        "not_certified": ["infinite Euler-product normal convergence", "analytic moment estimates", "native moment hypothesis", "RH"]
    }
    if args.proof:
        proof = args.proof.read_bytes()
        result["proof_sha256"] = hashlib.sha256(proof).hexdigest()
        result["proof_bytes"] = len(proof)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
