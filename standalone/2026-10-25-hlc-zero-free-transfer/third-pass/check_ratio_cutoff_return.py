#!/usr/bin/env python3
"""Finite exact checks for RATIO_CUTOFF_RETURN.md.

Uses the free-prime integer model and rational cutoff of
check_gcd_native.py. It does not verify an analytic functional equation
or a zero-free premise. Acceptance predicates survive python -O.
"""

from fractions import Fraction as F
from pathlib import Path
from math import gcd
import importlib.util
import json


spec = importlib.util.spec_from_file_location(
    "gcd_algebra", Path(__file__).with_name("check_gcd_native.py"))
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
require = base.require


def selector(value, which):
    if which == "all":
        return F(1)
    if which == "head":
        return base.cutoff(value)
    if which == "tail":
        return 1 - base.cutoff(value)
    raise ValueError(which)


def transform_coefficient(m, mask, outer, b0, which, *, drop_k_mask=False):
    bound = max(outer, default=0) // m
    total = F(0)
    for k in range(1, bound + 1):
        if not base.mu(k) or (not drop_k_mask and gcd(k, mask) != 1):
            continue
        # C_(km)(P); the original gcd mask remains even in the negative control.
        coefficient = sum(
            (value / (r // (k * m))
             for r, value in outer.items()
             if r % (k * m) == 0 and gcd(r // (k * m), mask) == 1), F(0))
        total += F(base.mu(k), k) * coefficient * selector(F(k * m) / b0, which)
    return total


def divisor_coefficient(m, mask, outer, b0, which):
    total = F(0)
    for r, value in outer.items():
        if r % m:
            continue
        v = r // m
        if gcd(v, mask) != 1:
            continue
        inner = sum((base.mu(k) * selector(F(k * m) / b0, which)
                     for k in base.divisors(v)), F(0))
        total += value * inner / v
    return total


def test_coefficient_inversion():
    identities = support_negative = mask_negative = 0
    for y1, y2 in ((F(2), F(3)), (F(3), F(4)), (F(3), F(5))):
        outer = base.outer_coefficient(y1, y2)
        for mask in (1, 2, 3, 5, 6, 10, 30):
            for b0 in (F(2), F(3), F(4)):
                for m in range(1, max(outer) + 2):
                    if gcd(m, mask) != 1:
                        continue
                    values = {}
                    for which in ("all", "head", "tail"):
                        values[which] = transform_coefficient(m, mask, outer, b0, which)
                        expected = divisor_coefficient(m, mask, outer, b0, which)
                        require(values[which] == expected,
                                "two finite return formulas disagree")
                        identities += 1
                    require(values["all"] == outer.get(m, F(0)),
                            "full harmonic Möbius inversion failed")
                    require(values["head"] + values["tail"] == values["all"],
                            "exact complementary selectors failed")
                    require(m < 2 * b0 or values["head"] == 0,
                            "head return upper support failed")
                    identities += 3
                    if m <= b0:
                        support_negative += values["tail"] != 0
                    mask_negative += values["tail"] != transform_coefficient(
                        m, mask, outer, b0, "tail", drop_k_mask=True)
    require(support_negative > 0, "false preservation of high support was not detected")
    require(mask_negative > 0, "omission of the natural k mask was not detected")
    one_prime = {1: F(1), 7: F(-1)}
    require(transform_coefficient(1, 1, one_prime, F(7, 3), "tail") == F(1, 7),
            "explicit low-unit leakage example failed")
    return {"exact_predicates": identities + 1,
            "negative_false_high_support": support_negative,
            "negative_deleted_k_mask": mask_negative}


def original_filtered_reflection(y1, y2, natural_mask, order, b0, which):
    dscale = y1 * y2 / 2
    result = (F(0), F(0))
    for r, coefficient in base.outer_coefficient(y1, y2).items():
        if gcd(r, natural_mask) != 1:
            continue
        for e in base.divisors(natural_mask):
            phase0 = base.multiply(base.character(r, order), base.character(e, order))
            if not base.mu(e) or phase0 == (0, 0):
                continue
            bound = int(F(5 * r * e) / dscale)
            for n in range(1, bound + 1):
                reduced_numerator = r // gcd(r, n)
                weight = selector(F(reduced_numerator) / b0, which)
                if not weight:
                    continue
                phase = base.multiply(phase0, base.conjugate(base.character(n, order)))
                value = coefficient * F(base.mu(e), r * e) * weight
                value *= base.ratio_kernel(F(n) * dscale / (5 * r * e))
                result = base.add_scaled(result, phase, value)
    return result


def returned_reflection(y1, y2, natural_mask, order, b0, which):
    dscale = y1 * y2 / 2
    outer = base.outer_coefficient(y1, y2)
    mask = 5 * natural_mask
    result = (F(0), F(0))
    for m in range(1, max(outer) + 1):
        if gcd(m, mask) != 1:
            continue
        coefficient = transform_coefficient(m, mask, outer, b0, which)
        if not coefficient:
            continue
        for e in base.divisors(natural_mask):
            phase0 = base.multiply(base.character(m, order), base.character(e, order))
            if not base.mu(e) or phase0 == (0, 0):
                continue
            bound = int(F(5 * m * e) / dscale)
            for n in range(1, bound + 1):
                phase = base.multiply(phase0, base.conjugate(base.character(n, order)))
                value = coefficient * F(base.mu(e), m * e)
                value *= base.ratio_kernel(F(n) * dscale / (5 * m * e))
                result = base.add_scaled(result, phase, value)
    return result


def test_masked_reflected_return():
    count = 0
    for y1, y2 in ((F(2), F(3)), (F(3), F(4))):
        for natural_mask in (1, 2, 3, 6, 10):
            for order in (1, 2, 3):
                for b0 in (F(2), F(4)):
                    for which in ("head", "tail"):
                        expected = original_filtered_reflection(
                            y1, y2, natural_mask, order, b0, which)
                        actual = returned_reflection(
                            y1, y2, natural_mask, order, b0, which)
                        require(expected == actual,
                                "primitive/natural reflected return failed")
                        count += 1
    return count


def test_squarefree_and_exponents():
    count = 0
    for y1, y2 in ((F(2), F(12)), (F(3), F(20))):
        outer = base.outer_coefficient(y1, y2)
        for m in range(1, int(y2) + 1):
            if base.mu(m) == 0:
                continue
            multiplicity = sum((base.cutoff(F(a) / y1) for a in base.divisors(m)), F(0))
            require(outer[m] == base.mu(m) * multiplicity,
                    "squarefree asymmetric coefficient formula failed")
            require(multiplicity >= 1, "unit short divisor disappeared")
            count += 2
    rlo, rhi, b0 = F(29, 25), F(117, 100), F(7, 9)
    beta, alpha = F(22, 25), F(2, 125)
    require(rlo - b0 == F(86, 225), "ratio-length gap failed")
    require((rlo - b0) * (1 - beta) == F(86, 1875), "coefficient decay exponent failed")
    require(F(86, 1875) - F(1, 25) == F(11, 1875) > 0,
            "reserved subpower margin failed")
    require(b0 - alpha == F(857, 1125), "claimed long-factor threshold failed")
    critical_b_hi = F(745700, 1000000)
    require(critical_b_hi < b0 - alpha < b0 < 1, "critical scale not below proposed threshold")
    require(critical_b_hi < rlo - alpha, "long asymmetric cutoff omits critical scale")
    gap = (1 + 5 * rlo) / 6 - (F(179, 126) - rlo / 4)
    require(gap == F(17, 6300) > F(1, 1000), "new head exponent gap failed")
    require(rhi > rlo, "licensed interval reversed")
    return count + 8


def main():
    print(json.dumps({
        "finite_inversion": test_coefficient_inversion(),
        "masked_reflected_returns": test_masked_reflected_return(),
        "squarefree_and_scale_predicates": test_squarefree_and_exponents(),
        "scope": "finite exact algebra only; no row-mean lower bound or analytic certification",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
