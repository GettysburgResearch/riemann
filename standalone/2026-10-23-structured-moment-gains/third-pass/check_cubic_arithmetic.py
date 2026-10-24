#!/usr/bin/env python3
"""Exact finite checks for the cubic Möbius adapter and Fourier orientation.

These checks do not prove a character mean or a zero-free region. They use
integer arithmetic in Q(zeta_6,zeta_p), and a finite free ideal monoid.
"""

from itertools import product
from math import prod
import json


Z6 = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def demand(condition, label):
    if not condition:
        raise AssertionError(label)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def multiply(a, b):
    # zeta_6^2 = zeta_6 - 1.
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def scale(values, coefficient):
    return [multiply(value, coefficient) for value in values]


def canonical(values):
    # Phi_p(X)=1+...+X^(p-1) is irreducible over Q(zeta_6), p>3.
    last = values[-1]
    return tuple((a - last[0], b - last[1]) for a, b in values[:-1])


def cyclic_product(left, right):
    p = len(left)
    result = [(0, 0)] * p
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            index = (i + j) % p
            result[index] = add(result[index], multiply(a, b))
    return result


def conjugate(values):
    result = [(0, 0)] * len(values)
    for index, (a, b) in enumerate(values):
        # bar(zeta_6)=1-zeta_6 and bar(zeta_p)=zeta_p^(-1).
        result[-index % len(values)] = (a + b, -b)
    return result


def gauss_checks():
    records = []
    count = 0
    for p in (13, 37, 61, 73):
        generator = next(g for g in range(2, p)
                         if len({pow(g, i, p) for i in range(p - 1)}) == p - 1)
        logarithm = {pow(generator, i, p): i % 6 for i in range(p - 1)}

        def gauss(exponent, frequency=1):
            result = [(0, 0)] * p
            for x in range(1, p):
                index = frequency * x % p
                result[index] = add(result[index], Z6[exponent * logarithm[x] % 6])
            return result

        constant_p = [(p, 0)] + [(0, 0)] * (p - 1)
        for exponent in (1, 2, 3, 4, 5):
            g = gauss(exponent)
            demand(canonical(cyclic_product(g, conjugate(g))) == canonical(constant_p),
                   "primitive Gauss norm")
            demand(not any(a or b for a, b in canonical(gauss(exponent, 0))),
                   "natural zero at a zero frequency")
            count += 2

        # p*g_1 = bar(chi_6(4))*g_3*g_2^2.  This is the unnormalized
        # Hasse-Davenport identity corresponding to gamma_1=G*gamma_2^2.
        lhs = scale(gauss(1), (p, 0))
        rhs = scale(cyclic_product(gauss(3), cyclic_product(gauss(2), gauss(2))),
                    Z6[-logarithm[4] % 6])
        demand(canonical(lhs) == canonical(rhs), "Gauss coefficient conversion")
        count += 1

        rejected_square = 0
        for k in range(1, p):
            phase = Z6[-2 * logarithm[k] % 6]
            demand(canonical(gauss(2, k)) == canonical(scale(gauss(2), phase)),
                   "cubic Poisson conjugates the frequency character")
            target = canonical(scale(gauss(-1), phase))
            demand(canonical(gauss(-1, pow(k, 4, p))) == target,
                   "physical sextic numerator is the fourth power")
            if canonical(gauss(-1, pow(k, 2, p))) != target:
                rejected_square += 1
            count += 2
        demand(rejected_square == 2 * (p - 1) // 3,
               "the square substitution fails on both nontrivial cubic classes")
        count += 1
        records.append({"prime": p, "primitive_root": generator,
                        "square_substitution_rejections": rejected_square})
    return count, records


def mobius(vector):
    return 0 if max(vector, default=0) > 1 else (-1) ** sum(vector)


def monoid_checks():
    # Distinct formal prime ideals may have the same norm.
    norms = (7, 7, 13, 19)
    angular_digits = (1, 2, 5, 3)
    zero = (0,) * len(norms)
    count = 0
    records = []
    for cutoff in (49, 50, 169, 343, 1000, 2401):
        limits = []
        for q in norms:
            exponent, power = 0, 1
            while power * q <= cutoff:
                exponent, power = exponent + 1, power * q
            limits.append(exponent)
        ideals = [v for v in product(*(range(e + 1) for e in limits))
                  if prod(q ** e for q, e in zip(norms, v)) <= cutoff]

        def norm(v):
            return prod(q ** e for q, e in zip(norms, v))

        def truncated(v):
            return mobius(v) if norm(v) ** 2 <= cutoff else 0

        for n in ideals:
            convolution = 0
            twisted = {(ramified, punctured): (0, 0)
                       for ramified, punctured in ((0, 0), (1, 2), (4, 1), (2, 2))}

            def character(v, ramified, punctured):
                if any(e and ((ramified | punctured) >> i) & 1
                       for i, e in enumerate(v)):
                    return 0, 0
                return Z6[sum(e * d for e, d in zip(v, angular_digits)) % 6]

            # Independently enumerate all a*b*c=n, including repeated primes.
            for a in product(*(range(e + 1) for e in n)):
                for b in product(*(range(e - f + 1) for e, f in zip(n, a))):
                    c = tuple(e - f - g for e, f, g in zip(n, a, b))
                    coefficient = truncated(a) * truncated(b)
                    convolution += coefficient
                    for masks in twisted:
                        value = multiply(multiply(character(a, *masks),
                                                  character(b, *masks)),
                                         character(c, *masks))
                        twisted[masks] = add(twisted[masks],
                                             (coefficient * value[0], coefficient * value[1]))
            demand(mobius(n) == 2 * truncated(n) - convolution,
                   "exact finite short Mobius identity")
            count += 1
            for masks, value in twisted.items():
                chi = character(n, *masks)
                demand((mobius(n) * chi[0], mobius(n) * chi[1]) ==
                       (2 * truncated(n) * chi[0] - value[0],
                        2 * truncated(n) * chi[1] - value[1]),
                       "short identity retains angular phases and both zero masks")
                count += 1
        demand(zero in ideals, "identity ideal retained")
        records.append({"cutoff": cutoff, "ideal_count": len(ideals)})
    return count, {"formal_prime_norms": norms, "cutoffs": records}


def main():
    gauss_count, gauss_records = gauss_checks()
    monoid_count, monoid_records = monoid_checks()
    print(json.dumps({"arithmetic": "EXACT_INTEGER_CYCLOTOMIC_AND_MONOID",
                      "analytic_certification": False,
                      "checks": gauss_count + monoid_count,
                      "gauss_checks": gauss_count, "gauss_fields": gauss_records,
                      "monoid_checks": monoid_count, "monoid": monoid_records,
                      "scope": "Finite identities and rejection of the square-index substitution only"},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
