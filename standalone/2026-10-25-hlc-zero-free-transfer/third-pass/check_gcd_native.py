#!/usr/bin/env python3
"""Finite algebra for GCD_NATIVE_COEFFICIENT.md; no analytic certification.

The tests use the free-prime monoid of positive integers. Unique
factorization makes these identities the same formal identities for
ideals. The rational cutoff is C^2, not the C^infinity cutoff used in
the analytic argument; its only role here is to test exact weighted
factorization. All predicates survive python -O.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd
import json


def require(condition, description):
    if not condition:
        raise RuntimeError(description)


@lru_cache(None)
def factor(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                n //= p
                exponent += 1
            result.append((p, exponent))
        p += 1
    if n > 1:
        result.append((n, 1))
    return tuple(result)


@lru_cache(None)
def mu(n):
    fs = factor(n)
    return 0 if any(e > 1 for _, e in fs) else (-1) ** len(fs)


def divisors(n):
    result = [1]
    for p, exponent in factor(n):
        result = [d * p**j for d in result for j in range(exponent + 1)]
    return sorted(result)


def cutoff(x):
    """An exact rational weighted cutoff, used only for finite algebra."""
    x = F(x)
    if x <= 1:
        return F(1)
    if x >= 2:
        return F(0)
    z = x - 1
    return 1 - 10 * z**3 + 15 * z**4 - 6 * z**5


@lru_cache(None)
def weighted_mobius(y):
    return {
        n: F(mu(n)) * cutoff(F(n) / y)
        for n in range(1, int(2 * y) + 1)
        if mu(n) and cutoff(F(n) / y)
    }


@lru_cache(None)
def outer_coefficient(y1, y2):
    values = {}
    for a, ma in weighted_mobius(y1).items():
        for b, mb in weighted_mobius(y2).items():
            values[a * b] = values.get(a * b, F(0)) + ma * mb
    return {n: c for n, c in values.items() if c}


@lru_cache(None)
def harmonic(mask, scale):
    return sum(
        (F(mu(n), n) * cutoff(F(n) / scale)
         for n in range(1, int(2 * scale) + 1)
         if gcd(n, mask) == 1),
        F(0),
    )


def direct_coefficient(a, mask, y1, y2, *, drop_mask=False, truncate=None):
    return sum(
        (coefficient / (r // a)
         for r, coefficient in outer_coefficient(y1, y2).items()
         if r % a == 0
         and (drop_mask or gcd(r // a, mask) == 1)
         and (truncate is None or r <= truncate)),
        F(0),
    )


def allocated_coefficient(a, mask, y1, y2, *, drop_both=False):
    require(gcd(a, mask) == 1, "allocation only licensed on natural support")
    if any(exponent >= 3 for _, exponent in factor(a)):
        return F(0)
    simple = [p for p, exponent in factor(a) if exponent == 1]
    square_root = 1
    for p, exponent in factor(a):
        if exponent == 2:
            square_root *= p
    total = F(0)
    slots = (0, 1) if drop_both else (0, 1, 2)
    for assignment in product(slots, repeat=len(simple)):
        left = right = both = 1
        for p, slot in zip(simple, assignment):
            if slot == 0:
                left *= p
            elif slot == 1:
                right *= p
            else:
                both *= p
        dl = square_root * left * both
        dr = square_root * right * both
        total += harmonic(mask * dl, y1 / dl) * harmonic(mask * dr, y2 / dr) / both
    return (-1) ** len(simple) * total


def test_weighted_hb():
    count = 0
    for y in (F(3, 2), F(2), F(5, 2), F(3), F(4), F(5), F(6)):
        outer = outer_coefficient(y, y)
        for n in range(1, int(y * y) + 1):
            rhs = 2 * mu(n) * cutoff(F(n) / y)
            rhs -= sum((outer.get(d, F(0)) for d in divisors(n)), F(0))
            require(rhs == mu(n), f"weighted HB failure at y={y}, n={n}")
            count += 1
    return count


def test_allocation():
    count = repeated = subunit = 0
    wrong_both = wrong_mask = wrong_truncation = 0
    scales = (F(3, 2), F(2), F(5, 2), F(3), F(4))
    for y1 in scales:
        for y2 in scales:
            bound = int(4 * y1 * y2) + 4
            for mask in (1, 2, 3, 5, 6, 10, 30):
                for a in range(1, bound + 1):
                    if gcd(a, mask) != 1:
                        continue
                    direct = direct_coefficient(a, mask, y1, y2)
                    allocated = allocated_coefficient(a, mask, y1, y2)
                    require(direct == allocated,
                            f"allocation failure at a={a}, mask={mask}, y={y1},{y2}")
                    count += 1
                    repeated += any(e == 2 for _, e in factor(a))
                    subunit += a > max(y1, y2)
                    wrong_both += direct != allocated_coefficient(
                        a, mask, y1, y2, drop_both=True)
                    wrong_mask += direct != direct_coefficient(
                        a, mask, y1, y2, drop_mask=True)
                    wrong_truncation += direct != direct_coefficient(
                        a, mask, y1, y2, truncate=y1 * y2)
    require(wrong_both > 0, "dropping both-divisible allocations was not detected")
    require(wrong_mask > 0, "dropping gcd zero factors was not detected")
    require(wrong_truncation > 0, "truncating the complete smooth coefficient was not detected")
    return {
        "identities": count,
        "repeated_prime_cases": repeated,
        "cases_with_a_above_both_cutoff_scales": subunit,
        "negative_drop_both_allocation": wrong_both,
        "negative_drop_gcd_mask": wrong_mask,
        "negative_truncate_smooth_outer_support": wrong_truncation,
    }


PHASE = ((1, 0), (0, 1), (-1, 0), (0, -1))
LOG_MOD_5 = {1: 0, 2: 1, 4: 2, 3: 3}


def character(n, order):
    return PHASE[order * LOG_MOD_5[n % 5] % 4] if n % 5 else (0, 0)


def multiply(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def conjugate(z):
    return z[0], -z[1]


def add_scaled(z, phase, value):
    return z[0] + phase[0] * value, z[1] + phase[1] * value


def ratio_kernel(x):
    return (1 - x)**2 if x < 1 else F(0)


def original_return(y, natural_mask, order):
    """Finite exact reflection model with compact ratio kernel, q=5."""
    dscale = y * y / 2
    result = (F(0), F(0))
    for r, coefficient in outer_coefficient(y, y).items():
        if gcd(r, natural_mask) != 1:
            continue
        row_phase = character(r, order)
        for e in divisors(natural_mask):
            if not mu(e):
                continue
            fixed_phase = multiply(row_phase, character(e, order))
            if fixed_phase == (0, 0):
                continue
            bound = int(F(5 * r * e) / dscale)
            for n in range(1, bound + 1):
                phase = multiply(fixed_phase, conjugate(character(n, order)))
                value = coefficient * F(mu(e), r * e)
                value *= ratio_kernel(F(n) * dscale / (5 * r * e))
                result = add_scaled(result, phase, value)
    return result


def grouped_return(y, natural_mask, order, *, wrong_dual_mask=False, wrong_gcd_mask=False):
    dscale = y * y / 2
    result = (F(0), F(0))
    mask = 5 * natural_mask
    for a in range(1, int(4 * y * y) + 1):
        if gcd(a, mask) != 1:
            continue
        coefficient = direct_coefficient(a, mask, y, y, drop_mask=wrong_gcd_mask)
        if not coefficient:
            continue
        row_phase = character(a, order)
        for e in divisors(natural_mask):
            if not mu(e):
                continue
            fixed_phase = multiply(row_phase, character(e, order))
            if fixed_phase == (0, 0):
                continue
            bound = int(F(5 * a * e) / dscale)
            for b in range(1, bound + 1):
                if gcd(a, b) != 1:
                    continue
                if wrong_dual_mask and gcd(b, natural_mask) != 1:
                    continue
                phase = multiply(fixed_phase, conjugate(character(b, order)))
                value = coefficient * F(mu(e), a * e)
                value *= ratio_kernel(F(b) * dscale / (5 * a * e))
                result = add_scaled(result, phase, value)
    return result


def test_grouping():
    count = wrong_dual = wrong_gcd = 0
    for y in (F(4), F(5)):
        for natural_mask in (1, 2, 3, 6, 10):
            for order in (1, 2, 3):
                expected = original_return(y, natural_mask, order)
                actual = grouped_return(y, natural_mask, order)
                require(expected == actual,
                        f"gcd grouping failure at y={y}, Q={natural_mask}, order={order}")
                count += 1
                wrong_dual += expected != grouped_return(
                    y, natural_mask, order, wrong_dual_mask=True)
                wrong_gcd += expected != grouped_return(
                    y, natural_mask, order, wrong_gcd_mask=True)
    require(wrong_dual > 0, "false dual Q mask was not detected")
    require(wrong_gcd > 0, "missing primitive/natural gcd mask was not detected")
    return {"masked_character_identities": count,
            "negative_false_dual_Q_mask": wrong_dual,
            "negative_missing_gcd_mask": wrong_gcd}


def euler_product(n):
    value = F(1)
    for p, _ in factor(n):
        # A rational stand-in for the variable p^(-s).
        value /= 1 - F(1, p + 1)
    return value


def test_mask_separation():
    masks = [1]
    for p in (2, 3, 5, 7):
        masks += [p * m for m in masks]
    valid = overlapping_negative = 0
    for p_mask in masks:
        for d in masks:
            lhs = euler_product(p_mask * d)
            rhs = euler_product(p_mask) * euler_product(d)
            if gcd(p_mask, d) == 1:
                require(lhs == rhs, "coprime Euler mask factorization failed")
                valid += 1
            else:
                overlapping_negative += lhs != rhs
    require(overlapping_negative > 0, "overlapping masks were not detected")
    return {"coprime_factorizations": valid,
            "negative_overlapping_Euler_masks": overlapping_negative}


def test_exponents():
    count = 0
    beta = F(7, 8)
    for numerator in range(1100, 1501, 10):
        r = F(numerator, 1000)
        for b100 in range(51):
            b = F(b100, 100)
            full = (2 - 2 * beta) * (b - r) + 1 + b - r
            full += max(F(1), b, F(2, 3) * (1 + b))
            reduced = 2 + F(5, 4) * (b - r)
            require(full == reduced, "short ratio exponent simplification failed")
            count += 1
    require(2 + F(5, 4) * (F(1, 2) - F(7, 5)) == F(7, 8),
            "r=7/5 numerical consequence failed")
    for numerator in range(1160, 1171):
        r = F(numerator, 1000)
        gap = (1 + 5 * r) / 6 - (2 + F(5, 4) * (F(9, 20) - r))
        require(gap == (100 * r - 115) / 48 and gap >= F(1, 48),
                "uniform critical-band gap failed")
        volume_b = r - F(4, 5)
        require(0 <= volume_b <= F(1, 2), "volume cutoff outside licensed range")
        require(2 + F(5, 4) * (volume_b - r) == 1, "volume exponent failed")
        count += 3
    for r in (F(29, 25), F(117, 100), F(7, 5)):
        gap = (1 + 5 * r) / 6 - (F(31, 12) - F(5, 4) * r)
        require(gap == (25 * r - 29) / 12, "7/15 cutoff gap failed")
        count += 1
    critical_lo = F(1163953576509, 10**12)
    critical_hi = critical_lo + F(1, 10**12)
    require((25 * critical_lo - 29) / 12 > F(8, 1000),
            "imported critical interval does not imply the displayed positive gap")
    require(critical_hi < F(117, 100), "critical interval above the stated band")
    return {"rational_predicates": count + 3,
            "critical_interval_role": "imported decimal enclosure; source root not reproved here"}


def main():
    result = {
        "weighted_HB_identities": test_weighted_hb(),
        "allocation": test_allocation(),
        "gcd_grouping": test_grouping(),
        "row_mask_separation": test_mask_separation(),
        "exponents": test_exponents(),
        "scope": "finite exact algebra only; no analytic theorem or zero-free certification",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
