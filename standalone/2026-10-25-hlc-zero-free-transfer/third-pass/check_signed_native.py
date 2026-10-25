#!/usr/bin/env python3
"""Exact finite controls for SIGNED_NATIVE.md; not an analytic proof.

The factorization checks use ordinary positive integers as a free-prime
model. The local additive check uses actual Eisenstein residue coordinates.
No output is evidence for an infinite character moment or zero-free claim.
"""

from fractions import Fraction as F
from math import gcd, isqrt
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def mobius(n):
    ans = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            ans = -ans
            if n % p == 0:
                return 0
        p += 1
    return -ans if n > 1 else ans


def divisors(n):
    return [d for d in range(1, isqrt(n) + 1) if n % d == 0]


def all_divisors(n):
    out = []
    for d in divisors(n):
        out.append(d)
        if d * d != n:
            out.append(n // d)
    return out


def coefficient(r, y, coprime_only=False):
    return sum(
        mobius(a) * mobius(r // a)
        for a in all_divisors(r)
        if a <= y and r // a <= y
        and (not coprime_only or gcd(a, r // a) == 1)
    )


def hb_controls():
    checked = 0
    failures_beyond = 0
    repeated_prime_mutations = 0
    for y in (2, 3, 5, 8, 17, 31):
        for n in range(1, y * y + 1):
            rhs = (2 * mobius(n) if n <= y else 0)
            rhs -= sum(coefficient(r, y) for r in all_divisors(n))
            require(rhs == mobius(n), ("HB coefficient", y, n, rhs))
            checked += 1
        for n in range(y * y + 1, (y + 4) ** 2 + 1):
            rhs = (2 * mobius(n) if n <= y else 0)
            rhs -= sum(coefficient(r, y) for r in all_divisors(n))
            failures_beyond += rhs != mobius(n)
        for n in range(1, y * y + 1):
            wrong = (2 * mobius(n) if n <= y else 0)
            wrong -= sum(coefficient(r, y, True) for r in all_divisors(n))
            repeated_prime_mutations += wrong != mobius(n)
    require(failures_beyond > 0, "support mutation was not detected")
    require(repeated_prime_mutations > 0, "coprimality mutation was not detected")
    return checked, failures_beyond, repeated_prime_mutations


# Exact Q(zeta_6) with zeta_6^2=zeta_6-1.
ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
LOG7 = {pow(3, j, 7): j for j in range(6)}


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def scale(a, x):
    return a * x[0], a * x[1]


def multiply(x, y):
    return x[0] * y[0] - x[1] * y[1], (
        x[0] * y[1] + x[1] * y[0] + x[1] * y[1]
    )


def character(n, u, puncture):
    if gcd(n, 7 * u * puncture) != 1:
        return (0, 0)
    return ROOTS[(LOG7[n % 7] * (u % 6)) % 6]


def row_controls():
    count = 0
    dropped_repeated = 0
    for d in (7, 13, 29, 47):
        y = isqrt(2 * d)
        coeff = [coefficient(r, y) for r in range(1, 2 * d)]
        for u in (5, 8, 9, 11, 16, 25, 27, 32, 35):
            for puncture in (1, 2, 15):
                lhs = (0, 0)
                full = (0, 0)
                short = (0, 0)
                long = (0, 0)
                wrong = (0, 0)
                for n in range(d + 1, 2 * d):
                    weight = (n - d) * (2 * d - n)
                    lhs = add(lhs, scale(mobius(n) * weight,
                                         character(n, u, puncture)))
                for r in range(1, 2 * d):
                    ar = coeff[r - 1]
                    if ar == 0:
                        continue
                    for c in range(1, (2 * d - 1) // r + 1):
                        n = r * c
                        if not d < n < 2 * d:
                            continue
                        weight = (n - d) * (2 * d - n)
                        term = scale(-ar * weight, multiply(
                            character(r, u, puncture),
                            character(c, u, puncture)))
                        full = add(full, term)
                        if r <= isqrt(u):
                            short = add(short, term)
                        else:
                            long = add(long, term)
                        if mobius(r) != 0:
                            wrong = add(wrong, term)
                require(full == lhs, ("native finite identity", d, u, puncture))
                require(add(short, long) == lhs, "short/long split lost a term")
                dropped_repeated += wrong != lhs
                count += 1
    require(dropped_repeated > 0, "discarded nonsquarefree outer terms undetected")
    return count, dropped_repeated


def inversion_controls():
    count = 0
    for a in range(1, 101):
        for b in range(1, 101):
            s = sum(mobius(d) for d in all_divisors(gcd(a, b)))
            require(s == int(gcd(a, b) == 1), ("gcd inversion", a, b))
            count += 1
    return count


def prime_divisors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def prime_mark_controls():
    count = 0
    overlap_errors = 0
    unweighted_errors = 0
    for mode in range(3):
        def weight(p):
            if mode == 0:
                return 1
            if mode == 1:
                return p - 4 if 5 <= p <= 17 else 0
            return 1 if p % 3 == 1 else -1
        for n in range(1, 501):
            primes = prime_divisors(n)
            lhs = sum(mobius(n // p) * weight(p) for p in primes
                      if gcd(n // p, p) == 1)
            rhs = -mobius(n) * sum(weight(p) for p in primes)
            require(lhs == rhs, ("weighted unitary prime mark", mode, n))
            unrestricted = sum(mobius(n // p) * weight(p) for p in primes)
            overlap_errors += unrestricted != rhs
            unweighted_errors += lhs != -mobius(n) * len(primes)
            count += 1
    require(overlap_errors > 0, "prime-overlap mutation undetected")
    require(unweighted_errors > 0, "restricted mark changed to log mark undetected")
    return count, overlap_errors, unweighted_errors


def additive_controls():
    """e0((a+b omega)/3)=zeta_3^b; exact cancellation uses counts.

    Inert prime p: the ideal (p) has nonunit condition a=b=0 mod p.
    Split prime 7 with omega=2: its selected ideal has a+2b=0 mod 7.
    A square integer modulus is a containing period, which suffices for
    the exact CRT class count and its primary-class negative control.
    """
    cases = [(), ((5, None),), ((11, None),), ((7, 2),),
             ((5, None), (7, 2)), ((7, 2), (11, None))]
    primary_failures = 0
    for primes in cases:
        pprod = 1
        for p, _ in primes:
            pprod *= p
        modulus = 3 * pprod
        full = [0, 0, 0]
        primary = [0, 0, 0]
        for a in range(modulus):
            for b in range(modulus):
                excluded = any(
                    (a % p == 0 and b % p == 0) if root is None
                    else (a + root * b) % p == 0
                    for p, root in primes
                )
                if excluded:
                    continue
                full[b % 3] += 1
                if a % 3 == 1 and b % 3 == 0:
                    primary[b % 3] += 1
        require(full[0] == full[1] == full[2], ("Eisenstein CRT sum", primes))
        primary_failures += not (primary[0] == primary[1] == primary[2])
    require(primary_failures == len(cases), "primary-class mutation undetected")
    return len(cases), primary_failures


def polynomial_at(coeff, x):
    out = F(0)
    for c in reversed(coeff):
        out = out * x + c
    return out


def lagrange_at(nodes, values, target):
    out = F(0)
    for j, node in enumerate(nodes):
        term = values[j]
        for k, other in enumerate(nodes):
            if k != j:
                term *= (target - other) / (node - other)
        out += term
    return out


def interpolation_controls():
    count = 0
    target = F(-1)
    for degree in range(1, 17):
        coeff = [F((-1) ** j * (j + 1), j + 2) for j in range(degree + 1)]
        nodes = [F(1) + F(j, 5 * degree) for j in range(degree + 1)]
        values = [polynomial_at(coeff, x) for x in nodes]
        require(lagrange_at(nodes, values, target) == polynomial_at(coeff, target),
                ("fixed-interval interpolation", degree))
        count += 1
    return count


def exponent_controls():
    count = 0
    for r in (F(13, 10), F(7, 5), F(10, 7), F(3, 2)):
        old = (1 + 5 * r) / 6
        short = F(5, 2) - r
        require(old - short == (11 * r - 14) / 6, "native gain algebra")
        rho = r - 1
        require(2 + rho - r == 1, "natural cutoff volume algebra")
        quarter = F(9, 4) - r
        require(old - quarter == (22 * r - 25) / 12,
                "quarter-row product gain algebra")
        count += 3
    for iv in range(13):
        v = F(iv, 12)
        for ip in range(iv + 1):
            p = F(ip, 24)
            require(p <= v / 2, "powerful radical range")
            require(p - 3 * v / 2 <= -v, "first powerful term")
            require(p - v / 2 <= 0, "second powerful term")
            require(p - 7 * v / 6 <= -2 * v / 3, "third powerful term")
            count += 3
    # Logarithmic exponents of (D,q,R,E) in the amplitude of (17).
    outside = (F(1, 2), F(-1, 2), F(-1), F(-1))
    dual_count = (F(-1), F(1), F(1), F(1))
    coefficient_energy_root = (F(0), F(0), F(1, 2), F(0))
    total = tuple(sum(v[i] for v in (outside, dual_count,
                                    coefficient_energy_root)) for i in range(4))
    require(total == (F(-1, 2), F(1, 2), F(1, 2), F(0)),
            "puncture prefactor failed to cancel")
    count += 1
    return count


def main():
    hb, beyond, repeats = hb_controls()
    rows, dropped = row_controls()
    gcd_checks = inversion_controls()
    prime_marks, overlap_errors, unweighted_errors = prime_mark_controls()
    crt, primary = additive_controls()
    interpolations = interpolation_controls()
    exponents = exponent_controls()
    print(json.dumps({
        "scope": "exact finite algebra only; no asymptotic moment verification",
        "hb_coefficients": hb,
        "native_masked_row_identities": rows,
        "complete_gcd_inversions": gcd_checks,
        "weighted_prime_mark_identities": prime_marks,
        "eisenstein_additive_class_sums": crt,
        "fixed_interval_interpolations": interpolations,
        "exact_exponent_predicates": exponents,
        "negative_controls": {
            "beyond_licensed_support": beyond,
            "wrong_coprime_outer_identity": repeats,
            "dropped_nonsquarefree_outer_terms": dropped,
            "wrong_primary_frequency_restriction": primary,
            "discarded_prime_overlap_terms": overlap_errors,
            "restricted_mark_replaced_by_full_log_mark": unweighted_errors,
        },
        "status": "PASS",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
