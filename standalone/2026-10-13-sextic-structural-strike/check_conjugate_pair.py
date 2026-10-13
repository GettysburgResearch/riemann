#!/usr/bin/env python3
"""Finite diagnostics for the conjugate-pair conductor deduction.

Uses exact Eisenstein residue values at the split prime ideals
(3+omega), (4+omega), (5+2 omega), of norms 7, 13, 19.
No analytic estimate or external theorem is verified by this program.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def multiply(z, w):
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c-b*d


def power(z, exponent):
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = multiply(result, z)
        z = multiply(z, z)
        exponent //= 2
    return result


def norm(z):
    a, b = z
    return a*a-a*b+b*b


# omega -> residue_root; zeta_6 = 1+omega.
PRIMES = ((7, 4), (13, 9), (19, 7))
for p, r in PRIMES:
    need((r*r+r+1) % p == 0, "invalid Eisenstein quotient")


def local_character(z, prime_index):
    p, r = PRIMES[prime_index]
    residue = (z[0]+r*z[1]) % p
    if residue == 0:
        return None
    value = pow(residue, (p-1)//6, p)
    generator = (1+r) % p
    phases = [pow(generator, j, p) for j in range(6)]
    need(len(set(phases)) == 6, "zeta6 loses order")
    return phases.index(value)


def times(x, y):
    if x is None or y is None:
        return None
    return (x+y) % 6


def conjugate(x):
    return None if x is None else (-x) % 6


def character(z, prime_mask):
    result = 0
    for index in range(3):
        if (prime_mask >> index) & 1:
            result = times(result, local_character(z, index))
    return result


def ring_cases():
    rows = [(a, b) for a in range(-7, 8) for b in range(-7, 8)
            if 0 < norm((a, b)) <= 36]
    stats = {
        "rows": len(rows),
        "units": sum(norm(z) == 1 for z in rows),
        "conjugate_pair_identities": 0,
        "recombination_identities": 0,
        "gcd_mask_identities": 0,
        "nonunit_pair_cases": 0,
        "negative_wrong_cubic_power": 0,
        "negative_replaced_nonunit": 0,
        "negative_deleted_common_mask": 0,
    }
    for mask in range(1, 8):
        for a in rows:
            for b in rows:
                lhs = character(multiply(a, power(b, 5)), mask)
                rhs = times(character(a, mask), conjugate(character(b, mask)))
                need(lhs == rhs, "conjugate pair does not match b^5")
                stats["conjugate_pair_identities"] += 1
                if lhs is None:
                    stats["nonunit_pair_cases"] += 1
                    repaired = 0 if rhs is None else rhs
                    if repaired != lhs:
                        stats["negative_replaced_nonunit"] += 1
                wrong = character(multiply(a, power(b, 2)), mask)
                if wrong != rhs:
                    stats["negative_wrong_cubic_power"] += 1
                need(character(multiply(a, b), mask)
                     == times(character(a, mask), character(b, mask)),
                     "recombination loses a nonunit")
                stats["recombination_identities"] += 1
    for q1_mask in range(8):
        for q2_mask in range(8):
            common = q1_mask & q2_mask
            h1, h2 = q1_mask ^ common, q2_mask ^ common
            for row in rows:
                lhs = times(character(row, q1_mask),
                            conjugate(character(row, q2_mask)))
                reduced = times(character(row, h1),
                                conjugate(character(row, h2)))
                mask_is_zero = character(row, common) is None
                rhs = None if mask_is_zero else reduced
                need(lhs == rhs, "common-gcd mask not exact")
                stats["gcd_mask_identities"] += 1
                if reduced != lhs:
                    stats["negative_deleted_common_mask"] += 1
    for key in ("negative_wrong_cubic_power", "negative_replaced_nonunit",
                "negative_deleted_common_mask"):
        need(stats[key] > 0, key + " has no witnesses")
    return stats


# Monomials use exponent vectors in (A,B,Q,Delta,P).
def add(*vectors):
    return tuple(sum(parts) for parts in zip(*vectors))


def scale(coefficient, vector):
    return tuple(coefficient*x for x in vector)


def rational_strings(values):
    return [str(v) for v in values]


def exponent_cases():
    prefactor = tuple(map(F, (0, 1, -1, 1, -1)))
    u = tuple(map(F, (1, -1, 2, -2, 1)))
    v = tuple(map(F, (0, 0, 1, -1, 0)))
    records = []
    count = 0
    afe_checks = 0
    dominance_checks = 0
    for n in range(3, 25):
        nf = F(n)
        source_powers = [(F(1), F(0)), (1/nf, F(1)),
                         (1-1/nf, 2/nf), (2/nf, 1-1/nf)]
        expected = [
            (F(1), F(0), F(1), F(-1), F(0)),
            (1/nf, 1-1/nf, 2/nf, -2/nf, -1+1/nf),
            (1-1/nf, 1/nf, F(1), F(-1), -1/nf),
            (2/nf, 1-2/nf, 3/nf, -3/nf, -1+2/nf),
        ]
        for powers, wanted in zip(source_powers, expected):
            actual = add(prefactor, scale(powers[0], u), scale(powers[1], v))
            need(actual == wanted, "wrong Poisson exponent transfer")
            need(actual[3] <= 0 and actual[4] <= 0,
                 "positive auxiliary exponent erased")
            count += 1
        # Substitute Q=(RAB)^1/2 and divide by AB.
        # Result vector here is (R,A,B).
        expected_afe = [
            (1/nf, 2/nf-1, F(0)),
            (F(1, 2), F(1, 2)-1/nf, -F(1, 2)+1/nf),
            (F(3, 2)/nf, F(7, 2)/nf-1, -F(1, 2)/nf),
        ]
        for term, wanted in zip(expected[1:], expected_afe):
            a, b, q = term[:3]
            actual = (q/2, a+q/2-1, b+q/2-1)
            need(actual == wanted, "wrong moving-background exponent")
            afe_checks += 1
            # Test every ray of the cone log R>=0, log B>=log A>=0:
            # log R, log A, log(B/A). Compare to R^1/2.
            cone_powers = (actual[0]-F(1, 2),
                           actual[1]+actual[2], actual[2])
            need(all(x <= 0 for x in cone_powers),
                 "R^1/2 bound fails on a cone ray")
            dominance_checks += 3
        if n in (3, 4, 6, 12, 24):
            records.append({
                "n": n,
                "off_diagonal_monomials_A_B_Q_Delta_P":
                    [rational_strings(x) for x in expected],
                "mean_ratios_R_A_B":
                    [rational_strings(x) for x in expected_afe],
            })
    return {
        "orders_checked": list(range(3, 25)),
        "poisson_monomial_identities": count,
        "afe_monomial_identities": afe_checks,
        "uniform_R_half_cone_ray_checks": dominance_checks,
        "sample_tables": records,
    }


def incidence_case():
    h = F(21, 20)
    c, d, e, f = F(3, 40), F(17, 40), F(41, 80), F(41, 80)
    ap, am = F(33, 80), F(1, 16)
    columns = [c+e+ap, c+f+ap, d+e+am, d+f+am]
    need(columns == [1, 1, 1, 1], "physical column size mismatch")
    x, y, g, q0 = 2*ap, 2*am, c+d, e+f
    l, m, big = x+y, min(x, y), max(x, y)
    new = [
        l/2-h/2,
        l/2+g/12-m/3-h/2,
        l/2+g/4+(m-big)/6-h/2,
        l/2+g/8-F(5, 24)*m-big/24-h/2,
    ]
    old_one = [
        l/2-h/2,
        l/2+(m+g-big)/4-h/2,
        l/2+(m+g)/12-h/2,
        l/2+F(5, 24)*(m+g)-big/8-h/2,
    ]
    old_cubic = [
        l/2-h/2,
        F(3, 4)*l+(c-d)/12-h/2,
        F(2, 3)*l-min(c, d)/6-h/2,
    ]
    old_completion = l+g/2-h
    old_divisor = (4*l+g)/3-h
    old_wu = F(359, 512)*l+F(103, 512)*g-h/2
    need(max(new) == -F(1, 24), "advertised new gain is wrong")
    need(max(old_one) == F(1, 480), "old one-label comparison is wrong")
    need(max(old_cubic) == F(19, 120), "old cubic comparison is wrong")
    need(old_completion == F(3, 20), "old completion comparison is wrong")
    need(old_divisor == F(23, 60), "old divisor comparison is wrong")
    need(old_wu == F(495, 2048), "old Wu comparison is wrong")
    # Four cleared-denominator conditions from theorem (5.7).
    margins = [
        l-h,
        6*l+g-6*h-4*m,
        6*l+3*g+2*m-6*h-2*big,
        12*l+3*g-12*h-5*m-big,
    ]
    scale_factors = [2, 12, 12, 24]
    need(margins == [s*t for s, t in zip(scale_factors, new)],
         "cleared denominator region is wrong")
    need(all(z < 0 for z in margins), "example outside controlled region")
    return {
        "h": str(h),
        "column_exponents": rational_strings(columns),
        "label_exponents": {"c": str(c), "d": str(d), "e": str(e),
                            "f": str(f), "a1_a2": str(ap), "b1_b2": str(am)},
        "aggregate_exponents": {"L": str(l), "M": str(m), "N": str(big),
                               "G": str(g), "q0": str(q0)},
        "new_excesses": rational_strings(new),
        "old_one_sign_excesses": rational_strings(old_one),
        "old_cubic_excesses": rational_strings(old_cubic),
        "old_completion_excess": str(old_completion),
        "old_divisor_excess": str(old_divisor),
        "old_wu_excess": str(old_wu),
        "cleared_region_margins": rational_strings(margins),
        "new_gain": str(F(1, 24)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--proof", required=True)
    parser.add_argument("--report")
    args = parser.parse_args()
    proof = Path(args.proof).read_bytes()
    own = Path(__file__).read_bytes()
    report = {
        "schema": "conjugate-pair-conductor-finite-diagnostics-v1",
        "status": "PASS",
        "proof_sha256": hashlib.sha256(proof).hexdigest(),
        "proof_bytes": len(proof),
        "producer_sha256": hashlib.sha256(own).hexdigest(),
        "residue_identities": ring_cases(),
        "exponent_transfer": exponent_cases(),
        "feasible_incidence": incidence_case(),
        "limits": [
            "Finite residue identities and rational exponent arithmetic only.",
            "No proof of the external large sieve, Poisson summation, or AFE.",
            "No verification of full native moments, zero-free bounds, or RH.",
            "The example compares specified upper-bound formulas, not arithmetic lower bounds.",
        ],
    }
    output = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        Path(args.report).write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()

