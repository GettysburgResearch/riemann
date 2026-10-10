#!/usr/bin/env python3
"""Exact directed weighted subset moments, using a last-label prefix sum.

Analytic contract: WEIGHTED_MOMENTS.md. Finite product sums only; no
convergence hypothesis is needed on their real weight exponent.
"""
from __future__ import annotations

from bisect import bisect_right
from dataclasses import dataclass
from fractions import Fraction as Q

from flint import arb

from verify_horizon_stitch import as_arb, primes_through, require

MOMENT_ORDER = 6


@dataclass(frozen=True)
class MomentVector:
    exponent: Q
    cutoff: int
    level: int
    values: tuple

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return iter(self.values)

    def __getitem__(self, index):
        return self.values[index]


class WeightedMoments:
    def __init__(self, exponent: Q, max_product: int, moment_order: int = MOMENT_ORDER):
        require(type(max_product) is int and max_product >= 4, 'product cap domain')
        require(type(moment_order) is int and 0 <= moment_order <= MOMENT_ORDER,
                'moment order domain')
        self.moment_order = moment_order
        self.exponent = Q(exponent)
        self.max_product = max_product
        self.prime_cap = max_product//2
        self.primes = primes_through(self.prime_cap)
        self.labels = sorted(self.primes+([67] if self.prime_cap >= 67 else []))
        self.roots = []
        self.weights = []
        self.prefix = [[arb(0)] for _ in range(moment_order+1)]
        a = as_arb(self.exponent)
        for q in self.labels:
            root = arb(q).sqrt() if moment_order else arb(1)
            value = arb(q)**(-a)
            require(bool(root > 0) and bool(value > 0), 'positive finite label weight')
            self.roots.append(root)
            self.weights.append(value)
            for j in range(moment_order+1):
                self.prefix[j].append(self.prefix[j][-1]+value)
                value *= root
        self.cache = {}

    def cumulative(self, level: int, limit: int):
        require(type(level) is int and 1 <= level <= 4, 'moment level domain')
        require(type(limit) is int and 0 <= limit <= self.max_product, 'moment cutoff domain')
        require(level != 1 or limit <= self.prime_cap, 'single-label completeness cap')
        key = (level, limit)
        if key in self.cache:
            return self.cache[key]
        result = [arb(0) for _ in range(self.moment_order+1)]

        def visit(start, quotient, remaining, base_weight, root_product):
            if remaining == 1:
                stop = bisect_right(self.labels, quotient)
                if stop <= start:
                    return
                factor = base_weight
                for j in range(self.moment_order+1):
                    result[j] += factor*(self.prefix[j][stop]-self.prefix[j][start])
                    factor *= root_product
                return
            last_start = len(self.labels)-remaining
            for i in range(start, last_start+1):
                minimum = 1
                for j in range(i, i+remaining):
                    minimum *= self.labels[j]
                if minimum > quotient:
                    break
                visit(i+1, quotient//self.labels[i], remaining-1,
                      base_weight*self.weights[i], root_product*self.roots[i])

        visit(0, limit, level, arb(1), arb(1))
        self.cache[key] = MomentVector(self.exponent, limit, level, tuple(result))
        return self.cache[key]


def binomial_coefficients(m: Q):
    m = Q(m)
    require(1 < m < 2, 'positive binomial-tail domain')
    coefficients = [Q(1), -m, m*(m-1)/2]
    for k in range(3, MOMENT_ORDER+1):
        coefficients.append(coefficients[-1]*(k-1-m)/k)
    require(all(c > 0 for c in coefficients[2:]), 'positive higher binomial coefficients')
    require(all(coefficients[k+1] < coefficients[k]
                for k in range(2, MOMENT_ORDER)), 'decreasing higher binomial coefficients')
    return coefficients


def normalized_level_bounds(m: Q, endpoint: int, moments):
    require(type(endpoint) is int and endpoint >= 1, 'endpoint domain')
    require(len(moments) == MOMENT_ORDER+1, 'moment vector size')
    require(isinstance(moments, MomentVector), 'guarded moment-vector metadata')
    require(moments.exponent == (Q(m)+1)/2, 'kernel and moment exponent match')
    require(moments.cutoff <= endpoint, 'all selected products are active')
    coefficients = binomial_coefficients(m)
    c = 3/(4*arb(endpoint).sqrt())
    denominator = (1-c)**as_arb(m)
    require(bool(denominator > 0), 'positive normalization denominator')
    power = arb(1)
    polynomial = arb(0)
    for j in range(MOMENT_ORDER):
        polynomial += as_arb(coefficients[j])*power*moments[j]
        power *= c
    lower = polynomial/denominator
    upper = (polynomial+4*as_arb(coefficients[MOMENT_ORDER])
             *power*moments[MOMENT_ORDER])/denominator
    return lower, upper
