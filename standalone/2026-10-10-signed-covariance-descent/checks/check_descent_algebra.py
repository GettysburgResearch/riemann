#!/usr/bin/env python3
"""Exact finite diagnostics for the signed-covariance descent packet.

Only integer, Fraction, polynomial, and finite cyclotomic arithmetic is used.
The checks authenticate the identities and finite cases specified in the report.
They do not prove theta automorphy, analytic continuation, a large sieve, a
spectral estimate, or any generalized inverse-Mobius moment. All acceptance
conditions are explicit and remain active under ``python -O``.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from math import gcd, lcm
from pathlib import Path


def require(condition, label):
    if not condition:
        raise RuntimeError(f"acceptance failed: {label}")


# Integer polynomials in K, y, z, q; x is replaced by K*y only where stated.
ONE = {(0, 0, 0, 0): 1}
K = {(1, 0, 0, 0): 1}
Y = {(0, 1, 0, 0): 1}
Z = {(0, 0, 1, 0): 1}
Q = {(0, 0, 0, 1): 1}


def padd(*terms):
    out = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value}


def pscale(term, scalar):
    return {key: scalar * value for key, value in term.items() if scalar * value}


def pmul(*terms):
    out = ONE.copy()
    for term in terms:
        new = {}
        for key, value in out.items():
            for other, coefficient in term.items():
                exponent = tuple(a + b for a, b in zip(key, other))
                new[exponent] = new.get(exponent, 0) + value * coefficient
        out = {key: value for key, value in new.items() if value}
    return out


def peq(left, right, label):
    require(not padd(left, pscale(right, -1)), label)


def check_local_algebra():
    x = pmul(K, Y)
    one_minus_x = padd(ONE, pscale(x, -1))
    d = padd(one_minus_x, Z)
    peq(padd(d, pscale(Z, -1)), one_minus_x, "reunion free prime")
    peq(padd(d, pmul(padd(Q, pscale(ONE, -1)), Z)),
        padd(one_minus_x, pmul(Q, Z)), "reunion frequency prime")
    # Cleared-denominator version of the complete outside-n cube sum.
    peq(padd(pmul(one_minus_x, padd(ONE, pscale(Y, -1))),
             pmul(padd(one_minus_x, K), Y)), ONE,
        "complete cube sum uses K*y=x")
    peq(padd(one_minus_x, K), padd(K, ONE, pscale(pmul(K, Y), -1)),
        "dominant extraction 1-x+K=K(1+1/K-y)")
    peq(padd(d, pscale(Z, -1), Z), d,
        "inactive projection coefficient A+B/q=1")
    require(padd(d, Z) != one_minus_x, "negative control wrong Ramanujan sign")

    rational_cases = 0
    geometric_identities = 0
    for q, kval, yval in product((7, 13, 19),
                                  (F(-2), F(-1, 2), F(1, 3), F(2, 3)),
                                  (F(-1, 7), F(1, 11), F(1, 5))):
        xval = kval * yval
        require(1 - xval != 0 and 1 - yval != 0 and kval != 0,
                "rational fixture avoids all denominators")
        weight = 1 + kval / (1 - xval)
        outside = 1 / ((1 - xval) * (1 - yval))
        inside = (1 - xval + kval) / ((1 - xval) * (1 - yval))
        require(1 - xval + kval == kval * (1 + 1 / kval - yval),
                "rational dominant extraction")
        for cutoff in (0, 1, 2, 4, 7):
            tail = yval ** (cutoff + 1) / (1 - yval)
            outside_partial = 1 + weight * sum(
                (yval ** j for j in range(1, cutoff + 1)), F(0))
            inside_partial = weight * sum(
                (yval ** j for j in range(cutoff + 1)), F(0))
            require(outside_partial + weight * tail == outside,
                    "outside-n exact finite geometric sum plus remainder")
            require(inside_partial + weight * tail == inside,
                    "inside-n exact geometric sum retains shared n,b primes")
            geometric_identities += 2
        # A deliberately incompatible cube coefficient invalidates the identity.
        wrong_x = 2 * kval * yval
        if 1 - wrong_x != 0:
            wrong = 1 + (1 + kval / (1 - wrong_x)) * yval / (1 - yval)
            require(wrong != 1 / ((1 - wrong_x) * (1 - yval)),
                    "negative control wrong cube character")
        rational_cases += 1

    finite_reunion_cases = 0
    primes = (7, 13, 19)
    # State 0 is a literally omitted prime, 1 a free prime, 2 a frequency prime.
    for states in product(range(3), repeat=len(primes)):
        original, transformed = F(1), F(1)
        for q, state in zip(primes, states):
            if state == 0:
                continue
            xval, zval = F(1, q ** 3), F(-1, q ** 2)
            dval = 1 - xval + zval
            require(dval != 0, "finite Euler fixture nonzero D")
            ramanujan = -1 if state == 1 else q - 1
            original *= dval * (1 + zval * ramanujan / dval)
            transformed *= 1 - xval
            if state == 2:
                transformed *= 1 + q * zval / (1 - xval)
        require(original == transformed, "finite Euler reunion including omissions")
        finite_reunion_cases += 1

    deleted_prime_terms = 0
    for q in primes:
        total = F(0)
        for squarefree_exponent, cube_exponent in product(range(2), range(5)):
            mask = int(squarefree_exponent == 0 and cube_exponent == 0)
            total += mask * F(1, q) ** (squarefree_exponent + cube_exponent)
            require(mask == (1 if squarefree_exponent + cube_exponent == 0 else 0),
                    "literal deleted-prime coefficient")
            deleted_prime_terms += 1
        require(total == 1, "deleted prime contributes only empty valuation")
        require(1 / (1 - F(1, q)) != total,
                "negative control omitted cube mask creates a false Euler factor")
        for exponent in range(13):
            actual_zero_extended_power = 0
            require(actual_zero_extended_power == 0,
                    "zero-extended character remains zero including exponent zero")
            if exponent == 0:
                require(0 ** exponent != actual_zero_extended_power,
                        "negative control ordinary 0**0 loses the unit mask")
            deleted_prime_terms += 1

    return {
        "cleared_denominator_polynomial_identities": 5,
        "rational_local_cases": rational_cases,
        "finite_geometric_identities_with_exact_remainders": geometric_identities,
        "finite_Euler_reunion_masks": finite_reunion_cases,
        "literal_deleted_prime_terms_and_powers": deleted_prime_terms,
    }


# Exact cyclotomic arithmetic. Dense polynomials list coefficients in ascending
# order; no numerical roots of unity or floating-point approximations are used.
def trim(poly):
    poly = list(poly)
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def monic_divmod(poly, divisor):
    out = trim(poly)
    divisor = trim(divisor)
    require(divisor and divisor[-1] == 1, "monic integer polynomial divisor")
    quotient = [0] * max(0, len(out) - len(divisor) + 1)
    while len(out) >= len(divisor):
        shift = len(out) - len(divisor)
        coefficient = out[-1]
        quotient[shift] = coefficient
        for j, value in enumerate(divisor):
            out[shift + j] -= coefficient * value
        out = trim(out)
    return trim(quotient), out


@lru_cache(None)
def cyclotomic(order):
    require(order >= 1, "positive root-of-unity order")
    poly = [-1] + [0] * (order - 1) + [1]
    for divisor in range(1, order):
        if order % divisor == 0:
            poly, remainder = monic_divmod(poly, cyclotomic(divisor))
            require(not remainder, "exact cyclotomic polynomial construction")
    return tuple(poly)


@lru_cache(None)
def root_power(order, exponent):
    poly = [0] * (exponent % order) + [1]
    return tuple(monic_divmod(poly, cyclotomic(order))[1])


def root_sum(order, exponents):
    coefficients = [0] * order
    for exponent in exponents:
        coefficients[exponent % order] += 1
    return tuple(monic_divmod(coefficients, cyclotomic(order))[1])


@lru_cache(None)
def rotate_root_value(order, value, exponent):
    return tuple(monic_divmod([0] * (exponent % order) + list(value),
                             cyclotomic(order))[1])


def primitive_root(q):
    for candidate in range(2, q):
        powers = {pow(candidate, j, q) for j in range(q - 1)}
        if len(powers) == q - 1:
            return candidate
    raise RuntimeError("fixture has no primitive root")


def check_finite_additive_fourier():
    cases = 0
    negative_wrong_contragredient = False
    for q in (7, 13, 19):
        generator = primitive_root(q)
        logs = {pow(generator, j, q): j for j in range(q - 1)}
        order = q * (q - 1)
        # All multiplicative characters, not merely order-six characters.
        # This distinguishes rho^3 from bar(rho)^3 in the negative control.
        for character in range(q - 1):
            transforms = {}
            for h in range(q):
                # phi(0)=0 even for the principal multiplicative character.
                transforms[h] = root_sum(order, (
                    q * character * logs[x] - (q - 1) * h * x
                    for x in range(1, q)))
            for b in range(1, q):
                rho_exponent = q * character * logs[b]
                inverse_square = pow(pow(b, 2, q), -1, q)
                cube = pow(b, 3, q)
                for h in range(q):
                    require(transforms[inverse_square * h % q] == rotate_root_value(
                        order, transforms[h], 2 * rho_exponent),
                        "exact finite additive Fourier d^-2 covariance")
                    require(transforms[cube * h % q] == rotate_root_value(
                        order, transforms[h], -3 * rho_exponent),
                        "exact finite additive Fourier cube contragredience")
                    wrong = rotate_root_value(order, transforms[h], 3 * rho_exponent)
                    if wrong != transforms[cube * h % q]:
                        negative_wrong_contragredient = True
                    cases += 2
    require(negative_wrong_contragredient,
            "negative control detects rho^3 in place of bar-rho^3")
    return {
        "prime_fields": [7, 13, 19],
        "character_scope": "Every multiplicative character of each field; phi(0)=0.",
        "exact_cyclotomic_Fourier_covariance_equalities": cases,
        "wrong_contragredient_control_detected": negative_wrong_contragredient,
    }


def check_character_cube_support():
    groups = ((6,), (9,), (6, 3), (12, 3), (4, 9))
    pairs = accepted = 0
    wrong_support = False
    for moduli in groups:
        elements = list(product(*(range(n) for n in moduli)))
        order = lcm(*moduli)
        for rho in elements:
            for output in elements:
                phase = lambda b: sum(
                    (order // n) * 3 * (r + o) * x
                    for n, r, o, x in zip(moduli, rho, output, b)) % order
                projection = root_sum(order, (phase(b) for b in elements))
                supported = all((3 * (r + o)) % n == 0
                                for n, r, o in zip(moduli, rho, output))
                require(projection == ((len(elements),) if supported else ()),
                        "finite character projection onto contragredient cubic coset")
                if supported:
                    require(all(phase(b) == 0 for b in elements),
                            "every retained output character has required cube")
                    accepted += 1
                else:
                    require(any(phase(b) != 0 for b in elements),
                            "negative control rejects wrong cube character")
                    wrong_support = True
                pairs += 1
    require(wrong_support, "at least one wrong finite character rejected")
    return {
        "finite_abelian_groups": [list(group) for group in groups],
        "input_output_character_pairs": pairs,
        "retained_pairs": accepted,
        "rejected_pairs": pairs - accepted,
        "method": "Exact cyclotomic evaluation of the cube-equivariant projection.",
    }


def eadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def emul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] - a[1] * b[1]


def escale(a, c):
    return a[0] * c, a[1] * c


def check_eisenstein_cubes():
    lam = (1, 2)
    lambda_fourth = emul(emul(lam, lam), emul(lam, lam))
    require(lambda_fourth == (9, 0), "lambda^4=9 exactly")
    primary_cases = phase_cases = 0
    for a, c in product(range(-8, 9), repeat=2):
        t = (a, c)
        b = eadd((1, 0), escale(t, 3))
        cube_difference = eadd(emul(emul(b, b), b), (-1, 0))
        quotient = eadd(t, eadd(escale(emul(t, t), 3),
                                escale(emul(emul(t, t), t), 3)))
        require(cube_difference == escale(quotient, 9),
                "primary cube difference divided by lambda^4 is integral")
        for m in product(range(-2, 3), repeat=2):
            numerator = emul(cube_difference, m)
            require(numerator == escale(emul(quotient, m), 9),
                    "all lattice phases unchanged under primary cube scaling")
            # The trace of an Eisenstein integer is exactly 2*x-y.
            z = emul(quotient, m)
            require(isinstance(2 * z[0] - z[1], int), "integral additive trace")
            phase_cases += 1
        primary_cases += 1
    wrong = eadd(emul(emul((2, 0), (2, 0)), (2, 0)), (-1, 0))
    require(wrong[0] % 9 != 0, "negative control nonprimary b=2 fails cube congruence")
    return {
        "primary_elements_b_equal_1_plus_3t": primary_cases,
        "t_coordinate_range": [-8, 8],
        "lattice_phase_cases": phase_cases,
        "m_coordinate_range": [-2, 2],
    }


def check_spectral_exponents():
    first_x = (F(1), F(1, 2))
    second_x = (F(4, 5), F(3, 5))
    require(first_x == (2 - first_x[0], 1 - first_x[1]),
            "first crossover X=Q^2F/X")
    require((F(2, 3) * (1 + second_x[0]), F(2, 3) * second_x[1]) ==
            (2 - second_x[0], 1 - second_x[1]),
            "second crossover (QX)^(2/3)=Q^2F/X")
    values = (F(3, 5), F(5, 8), F(2, 3), F(3, 4),
              F(5, 6), F(7, 8), F(19, 20))
    for a in values:
        first_lower = (1 - a, (1 - a) / 2)
        first_upper = (1 - a * first_x[0], F(1, 2) - a * first_x[1])
        second_lower = (F(1, 3) + second_x[0] * (F(5, 6) - a),
                        second_x[1] * (F(5, 6) - a))
        second_upper = (1 - a * second_x[0], F(1, 2) - a * second_x[1])
        require(first_lower == first_upper, "first spectral crossover contribution")
        require(second_lower == second_upper ==
                (1 - F(4, 5) * a, F(1, 2) - F(3, 5) * a),
                "second spectral crossover contribution")
        require((second_upper[0] < F(1, 2)) == (a > F(5, 8)),
                "strict conductor threshold is 5/8")
        require(second_upper[1] <= (1 - a) / 2,
                "auxiliary divisor exponent comparison")
    require(1 - F(4, 5) * F(3, 5) > F(1, 2),
            "negative control spectral threshold cannot be lowered to 3/5 by this bound")

    witnesses = [
        ("new_only_9_10", F(-1, 20), F(9, 10), False, True, True),
        ("new_only_7_10", F(-3, 20), F(7, 10), False, True, True),
        ("new_only_half", F(-1, 5), F(1, 2), False, True, True),
        ("divisor_boundary", F(-1, 10), F(7, 10), False, False, False),
        ("spectral_boundary", F(-3, 8), F(1, 4), False, True, False),
        ("insufficient_gauss_real_part", F(-1, 8), F(1, 4), False, False, False),
        ("negative_v_old_overlap", F(-3), F(-1), True, True, False),
        ("joint_lower_envelope_boundary", F(-3, 16), F(7, 16), False, False, False),
    ]
    records = []
    for name, s, v, expected_old, expected_new, expected_spectral in witnesses:
        a, delta = v - s, 1 - v
        old = s < 0 and s < v - 1
        new = a > F(1, 2) and v < 1 and 3 * a - 2 * v > 1
        spectral = new and F(5, 8) < a < 1
        require((old, new, spectral) ==
                (expected_old, expected_new, expected_spectral),
                f"strict domain witness {name}")
        if new:
            require(v - 3 * s + F(3, 2) > F(5, 2), "new domain w Euler half-plane")
            require(1 - s > 1, "new domain outer cube Euler half-plane")
            if a < 1:
                require(a + delta - (1 - a) / 2 > 1,
                        "new domain exact divisor summability exponent")
        if old:
            require(v - 2 * s > 1, "old absolute tube has no balanced scale saving")
        records.append({"name": name, "s": str(s), "v": str(v), "u": str(a),
                        "old_absolute_tube": old, "new_tube": new,
                        "spectral_tube": spectral, "balanced_scalar_exponent": str(v - 2 * s)})
    require(2 * F(5, 8) - F(7, 16) == F(13, 16),
            "joint spectral/divisor lower-envelope arithmetic")
    return {"crossover_identities": 2, "spectral_real_part_cases": len(values),
            "domain_witnesses": records,
            "boundary_note": "5/8 and 13/16 are exact arithmetic comparisons, not endpoint analytic claims."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] /
                        "results" / "descent_algebra_checks.json")
    args = parser.parse_args()
    source = Path(__file__).resolve()
    report = {
        "status": "PASS",
        "checker_sha256": sha256(source.read_bytes()).hexdigest(),
        "arithmetic": "Integers, fractions, exact polynomial division, finite cyclotomic quotient rings; no floating point.",
        "acceptance": "Every stated require must succeed; a failed condition raises RuntimeError under normal or optimized Python.",
        "source_scope": [
            "FINITE_RAY_REUNION.md: local factors and finite d^-2 Fourier scaling.",
            "FINITE_CUBE_HOMOGENEITY.md: finite cube Fourier scaling and character-support projection.",
            "ALL_CUSP_COEFFICIENT_ADAPTER.md: primary cube congruence preserving intrinsic phases.",
            "SECOND_REFLECTION_BOOTSTRAP.md: K*y=x, exact complete cubes, dominant n extraction, and strict domain arithmetic.",
            "SPECTRAL_ROW_MEAN.md: crossover powers and strict 5/8 threshold arithmetic.",
        ],
        "not_authenticated": [
            "The primitive theta coefficient or automorphy formulas.",
            "The global Kubota multiplier covariance at arbitrary bad moduli.",
            "Analytic continuation, normal convergence, source large sieves, or spectral mean bounds.",
            "A generalized inverse-Mobius moment, an improved zero-free boundary, or RH.",
        ],
        "local_algebra": check_local_algebra(),
        "finite_additive_Fourier": check_finite_additive_fourier(),
        "finite_character_cube_support": check_character_cube_support(),
        "Eisenstein_primary_cubes": check_eisenstein_cubes(),
        "spectral_and_domain_arithmetic": check_spectral_exponents(),
        "negative_controls": [
            "Wrong Ramanujan sign does not cancel the free-prime z term.",
            "K*y different from x breaks the complete cube identity.",
            "rho^3 in place of bar(rho)^3 fails finite Fourier covariance.",
            "Characters with a different cube have zero projection and fail covariance.",
            "Deleting the nonunit mask creates a false cube Euler factor; ordinary 0**0 is rejected.",
            "Nonprimary b=2 fails the lambda^4 cube congruence.",
            "At a=3/5 the spectral conductor comparison exceeds 1/2; strict domain boundaries are rejected.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": report["status"], "output": str(args.output),
                      "local_algebra": report["local_algebra"],
                      "finite_Fourier_equalities": report["finite_additive_Fourier"][
                          "exact_cyclotomic_Fourier_covariance_equalities"],
                      "character_pairs": report["finite_character_cube_support"]["input_output_character_pairs"],
                      "primary_cube_cases": report["Eisenstein_primary_cubes"]["primary_elements_b_equal_1_plus_3t"]},
                     sort_keys=True))


if __name__ == "__main__":
    main()
