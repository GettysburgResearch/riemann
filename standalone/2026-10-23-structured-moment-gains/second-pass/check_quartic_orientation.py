#!/usr/bin/env python3
"""Exact finite diagnostics for the quartic numerator orientation.

Compute the original finite Gauss sums in Z[i][x]/Phi_p(x), with x an
abstract primitive p-th root. No floating point or analytic moment bound
is used. The tests cover both primitive quartic characters and every row
of the listed prime fields, including the zero row. They do not certify
an infinite mean-value estimate, its automorphic realization, or a
zero-free half-plane.
"""

from fractions import Fraction
import json


PRIMES = (5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97)
ZERO = (0, 0)
ONE = (1, 0)
UNITS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def bar(a):
    return (a[0], -a[1])


def canonical(a):
    # 1+x+...+x^(p-1)=0; retain the basis 1,...,x^(p-2).
    return tuple(sub(v, a[-1]) for v in a[:-1])


def conjugate(a):
    p = len(a) + 1
    result = [ZERO] * p
    for j, v in enumerate(a):
        result[-j % p] = bar(v)
    return canonical(result)


def scalar(a, z):
    return tuple(mul(v, z) for v in a)


def product(a, b):
    p = len(a) + 1
    result = [ZERO] * p
    for j, v in enumerate(a):
        for k, w in enumerate(b):
            i = (j + k) % p
            result[i] = add(result[i], mul(v, w))
    return canonical(result)


def quartic_character(p, orientation):
    require(p % 4 == 1 and all(p % d for d in range(2, p)),
            "The declared field is not a prime field of order 1 mod 4")
    generator = next(g for g in range(2, p)
                     if len({pow(g, j, p) for j in range(p - 1)}) == p - 1)
    chi = [ZERO] * p
    for j in range(p - 1):
        chi[pow(generator, j, p)] = UNITS[(orientation * j) % 4]
    return chi


def gauss(p, chi, k):
    coefficients = [ZERO] * p
    for d in range(p):
        j = k * d % p
        coefficients[j] = add(coefficients[j], chi[d])
    return canonical(coefficients)


def main():
    rows = 0
    norm_checks = 0
    wrong_transfer_counterexamples = 0
    first_counterexample = None
    for p in PRIMES:
        for orientation in (1, 3):
            chi = quartic_character(p, orientation)
            g = gauss(p, chi, 1)
            gbar = conjugate(g)
            require(product(g, gbar) == ((p, 0),) + (ZERO,) * (p - 2),
                    "Gauss norm failed")
            norm_checks += 1
            for k in range(p):
                direct = gauss(p, chi, k)
                require(direct == scalar(g, bar(chi[k])),
                        "Direct Gauss change of variables failed")
                physical = scalar(gbar, bar(chi[k]))
                cube = conjugate(gauss(p, chi, pow(k, 3, p)))
                require(physical == cube, "Correct cube transfer failed")
                wrong = conjugate(direct)
                if physical != wrong:
                    wrong_transfer_counterexamples += 1
                    if first_counterexample is None:
                        first_counterexample = {
                            "prime": p, "orientation": orientation, "row": k,
                            "character_value": chi[k],
                        }
                require((physical == wrong) == (chi[k][1] == 0),
                        "Unexpected agreement of the incorrect transfer")
                rows += 1

    delta = Fraction(1, 7)
    beta = Fraction(7, 8)
    diagonal_regular_exponent = 1 - 3 * delta + 2 * delta * beta
    conditional_full_inverse_boundary = Fraction(1, 2) + 5 * beta / 12
    require(diagonal_regular_exponent == Fraction(23, 28),
            "Diagonal scale conversion failed")
    require(diagonal_regular_exponent < beta,
            "The regular diagonal does not fit the stated target")
    require(conditional_full_inverse_boundary == Fraction(83, 96),
            "Conditional sixth-power consumer conversion failed")
    # (H/D) * (D^2/H)^3 = D^5/H^2. To make it <= H needs H>=D^(5/3).
    naive_quartic_raw_threshold = Fraction(5, 3)
    naive_quartic_boundary = Fraction(1, 2) + 3 * naive_quartic_raw_threshold / 8
    require(naive_quartic_boundary == Fraction(9, 8),
            "Cube-inclusion loss was understated")
    require(wrong_transfer_counterexamples > 0,
            "The test did not distinguish the invalid transfer")
    print(json.dumps({
        "status": "passed",
        "arithmetic": "exact Gaussian integers modulo the cyclotomic polynomial",
        "prime_fields": list(PRIMES),
        "quartic_character_instances": 2 * len(PRIMES),
        "all_rows_checked": rows,
        "gauss_norm_checks": norm_checks,
        "incorrect_first_power_transfer_counterexamples": wrong_transfer_counterexamples,
        "first_counterexample": first_counterexample,
        "diagonal_regular_exponent_at_H_equals_D_to_7_over_8": str(diagonal_regular_exponent),
        "boundary_if_the_full_sextic_inverse_target_were_proved": str(conditional_full_inverse_boundary),
        "naive_cube_inclusion_quartic_boundary": str(naive_quartic_boundary),
        "global_zero_free_improvement_certified": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
