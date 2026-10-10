#!/usr/bin/env python3
"""Directed polynomial tail proof from finite weighted label moments.

Analytic contract and parity scope: WEIGHTED_MOMENTS.md.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb

from flint import arb

from verify_horizon_stitch import as_arb, require
from weighted_moments import MOMENT_ORDER, MomentVector, binomial_coefficients


def add(*polynomials):
    result = [arb(0)]*max(map(len, polynomials))
    for p in polynomials:
        for j, c in enumerate(p):
            result[j] += c
    return result


def scale(polynomial, factor):
    return [factor*c for c in polynomial]


def multiply(first, second):
    result = [arb(0)]*(len(first)+len(second)-1)
    for i, c in enumerate(first):
        for j, d in enumerate(second):
            result[i+j] += c*d
    return result


def kernel_polynomials(m: Q, moments=None):
    coefficients = binomial_coefficients(m)
    if moments is not None:
        require(isinstance(moments, MomentVector) and len(moments) == MOMENT_ORDER+1,
                'guarded moment vector')
        require(moments.exponent == (Q(m)+1)/2, 'kernel-moment exponent match')
    # The lower kernel polynomial is decreasing on [0,3/4], since its
    # derivative is the exact kernel derivative minus a positive tail.
    at_boundary = sum((coefficients[j]*Q(3, 4)**j
                       for j in range(MOMENT_ORDER)), Q(0))
    require(at_boundary > 0, 'positive lower kernel polynomial on activation domain')
    lower = [as_arb(coefficients[j]*Q(3, 4)**j)
             *(moments[j] if moments is not None else 1)
             for j in range(MOMENT_ORDER)]+[arb(0)]
    upper = list(lower)
    upper[MOMENT_ORDER] = (4*as_arb(coefficients[MOMENT_ORDER]*Q(3, 4)**MOMENT_ORDER)
                          *(moments[MOMENT_ORDER] if moments is not None else 1))
    return lower, upper


def numerator_polynomial(low: Q, high: Q, low_one, low_three,
                         high_two, high_four, infinite_one, infinite_three):
    require(1 < low <= high < 2, 'tail slab domain')
    require(low_one.level == 1 and low_three.level == 3
            and high_two.level == 2 and high_four.level == 4, 'retained level metadata')
    require(low_three.cutoff == high_two.cutoff == high_four.cutoff,
            'common retained product cutoff')
    require(low_one.cutoff <= low_three.cutoff, 'one-label retained cutoff')
    tail_one = (infinite_one-low_one[0]).upper()
    tail_three = (infinite_three-low_three[0]).upper()
    require(tail_one.is_exact() and bool(tail_one > 0), 'directed positive odd label tail')
    require(tail_three.is_exact() and bool(tail_three > 0), 'directed positive odd triple tail')
    removal_upper = infinite_one.upper()
    require(removal_upper.is_exact() and bool(removal_upper < 5), 'global removal majorant')
    constant = 1-tail_one-tail_three
    coefficient_four = 1-removal_upper/5
    require(bool(constant > 0) and bool(coefficient_four > 0),
            'positive denominator-substitution coefficients')
    d_low_lower, _ = kernel_polynomials(low)
    d_high_lower, d_high_upper = kernel_polynomials(high)
    _, odd_one_upper = kernel_polynomials(low, low_one)
    _, odd_three_upper = kernel_polynomials(low, low_three)
    even_two_lower, _ = kernel_polynomials(high, high_two)
    even_four_lower, _ = kernel_polynomials(high, high_four)
    numerator = add(
        scale(multiply(d_low_lower, d_high_lower), constant),
        scale(multiply(add(odd_one_upper, odd_three_upper), d_high_upper), arb(-1)),
        multiply(add(even_two_lower, scale(even_four_lower, coefficient_four)), d_low_lower),
    )
    return numerator, {'odd_one_tail_upper': str(tail_one),
                       'odd_three_tail_upper': str(tail_three),
                       'global_removal_upper': str(removal_upper),
                       'denominator_substitution_constant': str(constant),
                       'four_label_coefficient_lower': str(coefficient_four)}


def bernstein_coefficients(polynomial, left, right):
    require(left.is_exact() and right.is_exact() and bool(left >= 0) and bool(right > left),
            'exact Bernstein interval domain')
    degree = len(polynomial)-1
    width = right-left
    shifted = [width**k*sum((polynomial[j]*comb(j, k)*left**(j-k)
                            for j in range(k, degree+1)), arb(0))
               for k in range(degree+1)]
    return [sum((shifted[k]*Q(comb(i, k), comb(degree, k)).numerator
                 /Q(comb(i, k), comb(degree, k)).denominator
                 for k in range(i+1)), arb(0)) for i in range(degree+1)]


def certify_positive_tail(polynomial, product_cutoff: int, max_depth=14):
    require(type(product_cutoff) is int and product_cutoff >= 4, 'tail product cutoff')
    upper = (1/arb(product_cutoff).sqrt()).upper()
    require(upper.is_exact() and bool(upper > 0) and bool(upper < 1),
            'exact directed tail-coordinate cap')
    pending = [(arb(0), upper, 0)]
    leaves = []
    while pending:
        left, right, depth = pending.pop()
        coefficients = bernstein_coefficients(polynomial, left, right)
        if all(bool(c > 0) for c in coefficients):
            minimum = coefficients[0].lower()
            for coefficient in coefficients[1:]:
                lower = coefficient.lower()
                require(lower.is_exact(), 'exact Bernstein reported lower endpoint')
                if bool(lower < minimum):
                    minimum = lower
            leaves.append({'z_interval': [str(left), str(right)], 'depth': depth,
                           'positive_bernstein_lower_scale': str(minimum),
                           'all_entire_bernstein_balls_positive': True})
            continue
        require(depth < max_depth and len(pending)+len(leaves) < 1024,
                'Bernstein subdivision did not certify the tail')
        middle = (left+right)/2
        require(middle.is_exact(), 'exact tail bisection midpoint')
        pending.extend([(middle, right, depth+1), (left, middle, depth+1)])
    return {'polynomial_degree': len(polynomial)-1,
            'z_domain': ['0', str(upper)],
            'tail_endpoint_interval': [product_cutoff, 'infinity'],
            'bernstein_leaf_count': len(leaves), 'leaves': leaves,
            'entire_unbounded_tail_certified': True}
