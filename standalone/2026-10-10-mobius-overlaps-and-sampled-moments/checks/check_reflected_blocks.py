#!/usr/bin/env python3
"""Exact finite diagnostics for JOINT_REFLECTED_BLOCKS.md.

Arithmetic: exact integers in Z[omega], and exact rational exponents.
This program does not verify either analytic large sieve, theta reflection,
infinite Euler-product convergence, an infinite moment estimate, or RH.
Every acceptance predicate uses an explicit exception rather than assert.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import itertools
import json
from math import gcd, isqrt
from pathlib import Path


ZERO = (0, 0)
ONE = (1, 0)
ZETA6 = (1, 1)
COUNTS: Counter[str] = Counter()


def require(condition, category, detail):
    COUNTS[category] += 1
    if not condition:
        raise RuntimeError(f"FAIL [{category}]: {detail}")


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    # omega^2 + omega + 1 = 0.
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def power(x, n):
    result = ONE
    while n:
        if n & 1:
            result = mul(result, x)
        x = mul(x, x)
        n //= 2
    return result


def norm(x):
    return x[0] ** 2 - x[0] * x[1] + x[1] ** 2


def scale(x, n):
    return (n * x[0], n * x[1])


ROOTS = tuple(power(ZETA6, j) for j in range(6))
# Each generator is 1 modulo 3 and defines the indicated actual split
# prime ideal. The selected omega residue identifies which prime is used.
PRIMES = (
    (7, (-2, -3), 4),
    (13, (1, -3), 9),
    (19, (-2, 3), 7),
    (31, (-5, -6), 25),
)


def build_local_tables():
    result = []
    for q, generator, omega_residue in PRIMES:
        require(q > 3 and all(q % d for d in range(2, isqrt(q) + 1)),
                "primitive_fields", ("prime", q))
        require(norm(generator) == q, "primitive_fields", ("norm", q))
        require(generator[0] % 3 == 1 and generator[1] % 3 == 0,
                "primitive_fields", ("primary", q))
        require((omega_residue**2 + omega_residue + 1) % q == 0,
                "primitive_fields", ("omega", q))
        require((generator[0] + generator[1] * omega_residue) % q == 0,
                "primitive_fields", ("selected_ideal", q))
        residues = tuple((x[0] + x[1] * omega_residue) % q for x in ROOTS)
        require(len(set(residues)) == 6, "primitive_fields", ("six_roots", q))
        exponent_of = {residue: j for j, residue in enumerate(residues)}
        table = [ZERO]
        for r in range(1, q):
            finite_value = pow(r, (q - 1) // 6, q)
            require(finite_value in exponent_of, "primitive_fields",
                    ("sextic_residue", q, r))
            table.append(ROOTS[exponent_of[finite_value]])
        require(set(table[1:]) == set(ROOTS), "primitive_fields",
                ("order_six", q))
        result.append(tuple(table))
    return tuple(result)


LOCAL = build_local_tables()
MASKS = tuple(range(1 << len(PRIMES)))


@lru_cache(None)
def element(mask):
    z = ONE
    for i, (_, generator, _) in enumerate(PRIMES):
        if mask & (1 << i):
            z = mul(z, generator)
    return z


@lru_cache(None)
def symbol(mask, z, exponent=1):
    value = ONE
    for i, (q, _, omega_residue) in enumerate(PRIMES):
        if mask & (1 << i):
            r = (z[0] + z[1] * omega_residue) % q
            value = mul(value, LOCAL[i][r])
    # A principal power is still zero at a nonunit of the modulus.
    return ZERO if value == ZERO else power(value, exponent % 6)


def rho(mask, z):
    return symbol(mask, z, 3)


def divisors(mask):
    return tuple(r for r in MASKS if r & mask == r)


def mu(mask):
    return -1 if mask.bit_count() % 2 else 1


PRODUCTS = {(g, n): mul(element(g), element(n))
            for g in MASKS for n in MASKS}


def kernel(k, g, e, n, moving_mask=True):
    if g & e or (moving_mask and k & e):
        return ZERO
    return mul(rho(k, PRODUCTS[g, n]), symbol(n, element(e), 4))


def finite_primitive_checks():
    # Full multiplicative residue checks at every selected prime field.
    for i, (q, _, _) in enumerate(PRIMES):
        for a, b in itertools.product(range(q), repeat=2):
            require(symbol(1 << i, (a * b, 0)) ==
                    mul(symbol(1 << i, (a, 0)),
                        symbol(1 << i, (b, 0))),
                    "local_multiplicativity", (q, a, b))
        for a in range(q):
            expected = ZERO if a == 0 else ONE
            require(symbol(1 << i, (a, 0), 6) == expected,
                    "principal_power_zero", (q, a))
    # CRT product ideal of norms 7 and 13, all 91 integer residue classes,
    # with all ordered pairs, independently using integer multiplication.
    for a, b in itertools.product(range(91), repeat=2):
        require(symbol(3, (a * b, 0)) ==
                mul(symbol(3, (a, 0)), symbol(3, (b, 0))),
                "crt_91_multiplicativity", (a, b))
    for a in range(91):
        require(symbol(3, (a, 0), 6) ==
                (ONE if gcd(a, 91) == 1 else ZERO),
                "crt_91_zero_extension", a)


def exact_kernel_checks():
    for k, g, e, n in itertools.product(MASKS, repeat=4):
        common = g & n
        gp, np = g ^ common, n ^ common
        reduced = mul(rho(k, PRODUCTS[gp, np]),
                      mul(symbol(common, element(e), 4),
                          symbol(np, element(e), 4)))
        if k & common or g & e or k & e:
            reduced = ZERO
        require(kernel(k, g, e, n) == reduced,
                "gcd_kernel_identity", (k, g, e, n))

        mobius_sum = sum(mu(r) for r in divisors(k & e))
        require(kernel(k, g, e, n) ==
                scale(kernel(k, g, e, n, False), mobius_sum),
                "moving_mask_identity", (k, g, e, n))

        # This is the factorization used after writing k=r*k', e=r*e'.
        for r in divisors(k & e):
            kp, ep = k ^ r, e ^ r
            direct = mul(rho(k, PRODUCTS[g, n]), symbol(n, element(e), 4))
            factored = mul(
                mul(rho(r, element(g)), rho(r, element(n))),
                mul(rho(kp, PRODUCTS[g, n]),
                    mul(symbol(n, element(r), 4),
                        symbol(n, element(ep), 4))))
            require(direct == factored, "row_divisor_phase_factorization",
                    (k, g, e, n, r))


def coefficient_cases():
    return (
        ("separate_unit_phases",
         tuple(ROOTS[(2 * g + 1) % 6] for g in MASKS),
         tuple(ROOTS[(3 * e + 2) % 6] for e in MASKS),
         tuple(ROOTS[(5 * n + 3) % 6] for n in MASKS)),
        ("mobius_and_fixed_masks",
         tuple(ZERO if g & 8 else scale(ROOTS[g % 6], mu(g))
               for g in MASKS),
         tuple(ZERO if e & 4 else scale(ROOTS[(2 * e) % 6], mu(e))
               for e in MASKS),
         tuple(ZERO if n & 2 else ROOTS[(3 * n) % 6]
               for n in MASKS)),
    )


def full_sum_checks():
    panels = []
    # This independent incidence enumeration has, at each prime, the four
    # states: neither, g only, n only, or common. It does not start by
    # computing gcd on a previously enumerated ordered pair.
    incidence = []
    for states in itertools.product(range(4), repeat=len(PRIMES)):
        c = gp = np = 0
        for i, state in enumerate(states):
            if state == 1:
                gp |= 1 << i
            elif state == 2:
                np |= 1 << i
            elif state == 3:
                c |= 1 << i
        incidence.append((c, gp, np))
    require(len(incidence) == 256 and len(set(incidence)) == 256,
            "incidence_coverage", len(incidence))
    require({(c | gp, c | np) for c, gp, np in incidence} ==
            set(itertools.product(MASKS, repeat=2)),
            "incidence_coverage", "all_ordered_pairs")

    for name, ag, be, cn in coefficient_cases():
        row_values = []
        # Group the coprime column product m independently of any row.
        beta = {m: ZERO for m in MASKS}
        for g, n in itertools.product(MASKS, repeat=2):
            if g & n:
                continue
            inner = ZERO
            for e in MASKS:
                if not g & e:
                    inner = add(inner, mul(be[e], symbol(n, element(e), 4)))
            beta[g | n] = add(beta[g | n], mul(mul(ag[g], cn[n]), inner))

        for k in MASKS:
            direct = regrouped = temporary = ZERO
            for g, e, n in itertools.product(MASKS, repeat=3):
                coefficient = mul(mul(ag[g], be[e]), cn[n])
                direct = add(direct, mul(coefficient, kernel(k, g, e, n)))
                if not g & n:
                    temporary = add(
                        temporary,
                        mul(coefficient, kernel(k, g, e, n, False)))
            for c, gp, np in incidence:
                g, n = c | gp, c | np
                for e in MASKS:
                    if (k & c) or (g & e) or (k & e):
                        continue
                    phase = mul(rho(k, PRODUCTS[gp, np]),
                                mul(symbol(c, element(e), 4),
                                    symbol(np, element(e), 4)))
                    coefficient = mul(mul(ag[g], be[e]), cn[n])
                    regrouped = add(regrouped, mul(coefficient, phase))
            require(direct == regrouped, "full_signed_gcd_sums", (name, k))
            product_sum = ZERO
            for m in MASKS:
                product_sum = add(product_sum, mul(beta[m], rho(k, element(m))))
            require(temporary == product_sum, "coprime_product_column_sums",
                    (name, k))
            row_values.append(list(direct))
        panels.append({"name": name, "row_values_in_Zomega": row_values})
    return panels


# Polynomials in monomials with rational exponents, no floating point.
NVARS = 5


def monomial(*exponents):
    require(len(exponents) == NVARS, "symbolic_dimensions", exponents)
    return {tuple(map(F, exponents)): F(1)}


def psum(*polys):
    out = {}
    for poly in polys:
        for powers, coefficient in poly.items():
            out[powers] = out.get(powers, F(0)) + coefficient
    return {p: c for p, c in out.items() if c}


def pmul(*polys):
    out = {(F(0),) * NVARS: F(1)}
    for poly in polys:
        new = {}
        for p, a in out.items():
            for q, b in poly.items():
                powers = tuple(x + y for x, y in zip(p, q))
                new[powers] = new.get(powers, F(0)) + a * b
        out = new
    return out


def exponent_checks():
    # Variable order H,E,G,U,R.
    row = pmul(
        monomial(0, 0, 0, 0, -1),
        psum(monomial(1, 0, -1, -1, -1), monomial(0, 0, 0, 0, 0)),
        psum(monomial(0, 1, 0, 0, -1), monomial(0, 0, 0, 1, 0),
             monomial(0, F(2, 3), 0, F(2, 3), F(-2, 3))))
    expected_row = psum(
        monomial(1, 1, -1, -1, -3),
        monomial(1, 0, -1, 0, -2),
        monomial(1, F(2, 3), -1, F(-1, 3), F(-8, 3)),
        monomial(0, 1, 0, 0, -2),
        monomial(0, 0, 0, 1, -1),
        monomial(0, F(2, 3), 0, F(2, 3), F(-5, 3)))
    require(row == expected_row, "row_mask_six_monomials", row)

    # Variable order H,E,G,U,C.
    common = pmul(
        monomial(0, 0, 0, 0, -1),
        psum(monomial(1, 0, -1, -1, 2), monomial(0, 0, 0, 0, 0)),
        psum(monomial(0, 1, 0, 0, 0), monomial(0, 0, 0, 1, -1),
             monomial(0, F(2, 3), 0, F(2, 3), F(-2, 3))))
    expected_common = psum(
        monomial(1, 1, -1, -1, 1),
        monomial(1, 0, -1, 0, 0),
        monomial(1, F(2, 3), -1, F(-1, 3), F(1, 3)),
        monomial(0, 1, 0, 0, -1),
        monomial(0, 0, 0, 1, -2),
        monomial(0, F(2, 3), 0, F(2, 3), F(-5, 3)))
    require(common == expected_common, "gcd_six_monomials", common)

    # Independently evaluate the ratios of the actual squared normalizers
    # on six exact integer norm choices; no square roots are approximated.
    for r in (1, 7, 13, 19, 31, 91):
        eg, gg, uu = F(49), F(91 * r), F(169 * r)
        gp, up = gg / r, uu / r
        require(gp**2 * eg * up / (gg**2 * eg * uu) == F(1, r**3),
                "normalizers", ("common_divisor_squared_ratio", r))
        ep = eg / r
        require(gg**2 * ep * uu / (gg**2 * eg * uu) == F(1, r),
                "normalizers", ("row_divisor_squared_ratio", r))
    for ee, ff, gg, uu, cc in ((17, 23, 31, 43, 47),
                               (1, 1, 1, 1, 1), (49, 91, 13, 169, 7)):
        aa = ee * ff * gg
        physical_squared = F(1, aa * ff * gg * uu * cc**2)
        theorem_squared = F(1, gg**2 * ee * uu)
        frozen_label_squared = F(1, ff**2 * cc**2)
        require(physical_squared == frozen_label_squared * theorem_squared,
                "normalizers", ("physical_squared_prefactor", ee, ff, gg, uu, cc))

    examples = []
    for theta in (F(0), F(1, 4), F(49, 100)):
        h, e, g, u, m = 3 - theta, F(1, 2), F(1, 2), F(2), F(1, 2)
        cube = F(3, 2) - 2 * theta / 3
        u0 = 2 * h + e + 2 * g - 1 - 3 * cube
        require(u0 == 2, "physical_scale_exponents", str(theta))
        sf = (h + e + m - g - u, h - g,
              h + F(2, 3) * e + m / 3 - g - u / 3,
              e, u, F(2, 3) * (e + u))
        lam = min(F(0), (g - u0) / 3)
        all_rows = (h + e - g + lam, h - g,
                    h + F(2, 3) * e - g + lam,
                    e + h / 2, u0, F(2, 3) * (e + u0))
        old = (h + e - u, h, h + F(2, 3) * e - u / 3,
               e, u, F(2, 3) * (e + u))
        require(max(sf) == F(5, 2) - theta,
                "long_dual_squarefree_exponents", str(theta))
        require(max(all_rows) == F(5, 2) - theta,
                "long_dual_all_row_exponents", str(theta))
        require(max(old) - g / 6 - max(sf) == F(5, 12),
                "old_block_comparison", str(theta))
        examples.append({
            "theta": str(theta), "cube_exponent": str(cube),
            "U0_exponent": str(u0),
            "squarefree_six_exponents": list(map(str, sf)),
            "all_row_six_exponents": list(map(str, all_rows)),
            "new_maximum": str(max(sf)),
            "old_angular_squarefree_maximum": str(max(old) - g / 6),
        })
    return {
        "row_mask_powers": ["3", "2", "8/3", "2", "1", "5/3"],
        "gcd_dyad_powers": ["1", "0", "1/3", "-1", "-2", "-5/3"],
        "long_dual_examples": examples,
    }


def all_row_local_checks():
    tested_eta = (F(0), F(1, 6), F(1, 4), F(13, 42), F(1, 3) - F(1, 1000))
    for eta, a, eps in itertools.product(tested_eta, range(1, 31), (0, 1)):
        j = (2 * a + eps) % 6
        active_choices = (0, 1) if j == 0 else (1,)
        for active in active_choices:
            q4_power = 1 if j == 4 else 0
            exact = (q4_power + a * (4 * eta - 2) - 2 * eta * active
                     + eps * (2 * eta - 1))
            if a == 1:
                majorant = 2 * eta - 2
            elif a == 2:
                majorant = 6 * eta - 3
            elif a == 3:
                majorant = 12 * eta - 6
            else:
                majorant = 1 + a * (4 * eta - 2)
            require(exact <= majorant, "all_row_local_majorants",
                    (str(eta), a, eps, j, active))
            require(majorant < -1, "all_row_local_prime_summability_exponents",
                    (str(eta), a, eps, j, active))
            require(j != 4 or (eps == 0 and a % 3 == 2 and a >= 2),
                    "j4_valuation_gate", (a, eps, j))
            require(a not in (1, 2) or active == 1,
                    "small_valuation_activity", (a, eps, j, active))
    endpoint = 6 * F(1, 3) - 3
    require(endpoint == -1, "endpoint_obstruction", endpoint)
    require(6 * (F(1, 3) + F(1, 1000)) - 3 > -1,
            "endpoint_obstruction", "beyond_endpoint")
    require(12 * F(1, 3) - 6 == -2,
            "inactive_cubic_square_part", "a3_j0_inactive")
    return {
        "eta_values": list(map(str, tested_eta)),
        "valuations_tested": [1, 30],
        "epsilon_values": [0, 1],
        "active_choices": "both for j=0; active only for j!=0",
        "a2_j4_exponent_at_eta_one_third": str(endpoint),
        "a3_j0_inactive_exponent_at_eta_one_third": "-2",
        "infinite_tail_status": "not computationally checked; proved in note",
    }


def mutation_guards():
    witnesses = []
    for i in range(len(PRIMES)):
        p = 1 << i
        direct = rho(p, PRODUCTS[p, p])
        omitted_gcd_mask = rho(p, PRODUCTS[0, 0])
        require(direct == ZERO and omitted_gcd_mask == ONE and
                direct != omitted_gcd_mask,
                "mutation_drop_gcd_row_zero", i)
        witnesses.append({"mutation": "drop common-divisor row zero",
                          "prime_norm": PRIMES[i][0],
                          "correct": list(direct),
                          "mutant": list(omitted_gcd_mask)})
    require(kernel(1, 0, 1, 0) == ZERO and
            kernel(1, 0, 1, 0, False) == ONE,
            "mutation_drop_moving_mask", "k=e=prime7,g=n=unit")
    # Replacing a repeated product by its radical loses a real quadratic sign.
    true_square = rho(1, PRODUCTS[2, 2])
    wrong_radical = rho(1, element(2))
    require(true_square == ONE and wrong_radical == (-1, 0),
            "mutation_replace_square_by_radical", (true_square, wrong_radical))
    witnesses.append({"mutation": "replace gn by its radical",
                      "k_norm": 7, "g_norm": 13, "n_norm": 13,
                      "correct": list(true_square),
                      "mutant": list(wrong_radical)})
    return witnesses


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    finite_primitive_checks()
    exact_kernel_checks()
    panels = full_sum_checks()
    exponents = exponent_checks()
    local = all_row_local_checks()
    mutations = mutation_guards()
    result = {
        "status": "PASS",
        "arithmetic_class": "EXACT_INTEGER_AND_RATIONAL_DIAGNOSTIC",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "strict_acceptance": "Every declared predicate passed; explicit exceptions, no assert.",
        "primitive_fields": [
            {"norm": q, "primary_generator_a_plus_b_omega": list(gen),
             "omega_residue": w} for q, gen, w in PRIMES],
        "coverage": {
            "squarefree_ideal_masks": list(MASKS),
            "ordered_k_g_e_n_tuples": len(MASKS) ** 4,
            "common_prime_states": "none, g only, n only, or shared",
            "complete_integer_residue_pairs_mod_91": 91 ** 2,
            "row_scope": "16 selected squarefree ideals, not all rows of any height",
            "coefficient_panels": len(panels),
        },
        "checks_by_category": dict(sorted(COUNTS.items())),
        "total_predicates": sum(COUNTS.values()),
        "signed_row_panels": panels,
        "rational_exponent_checks": exponents,
        "all_row_local_diagnostics": local,
        "mutation_witnesses": mutations,
        "does_not_verify": [
            "analytic quadratic or cubic large sieve",
            "theta reflection or exact support theorem",
            "infinite Euler-product convergence",
            "angular reciprocal-L input",
            "infinite moments or RH",
            "all prime ideals, row norms, or valuation exponents",
        ],
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
        print(f"PASS {result['total_predicates']} exact predicates; output {args.output}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
