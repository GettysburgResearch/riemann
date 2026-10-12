#!/usr/bin/env python3
"""Directed subset moments marked by the sum of used static label weights.

Analytic contract: EXCLUSION_PAIRS.md. The underlying labels and finite
weighted moments are imported unchanged from weighted_moments.py.
"""
from __future__ import annotations

from bisect import bisect_right
from dataclasses import dataclass
from fractions import Fraction as Q

from flint import arb

from verify_horizon_stitch import require
from weighted_moments import WeightedMoments, MomentVector, MOMENT_ORDER


@dataclass(frozen=True)
class ExclusionVector:
    ordinary: MomentVector
    marked: MomentVector


class ExclusionMoments(WeightedMoments):
    def __init__(self, exponent: Q, max_product: int, moment_order=MOMENT_ORDER):
        super().__init__(exponent, max_product, moment_order)
        self.marked_prefix = [[arb(0)] for _ in range(moment_order+1)]
        for i, weight in enumerate(self.weights):
            value = weight*weight
            for j in range(moment_order+1):
                self.marked_prefix[j].append(self.marked_prefix[j][-1]+value)
                value *= self.roots[i]
        self.exclusion_cache = {}

    def marked_cumulative(self, level: int, limit: int):
        require(type(level) is int and level in [2, 4, 6], 'even exclusion level domain')
        require(type(limit) is int and 0 <= limit <= self.max_product,
                'marked product cutoff domain')
        key = (level, limit)
        if key in self.exclusion_cache:
            return self.exclusion_cache[key]
        ordinary = [arb(0) for _ in range(self.moment_order+1)]
        marked = [arb(0) for _ in range(self.moment_order+1)]

        def visit(start, quotient, remaining, base_weight, root_product, used_sum):
            if remaining == 1:
                stop = bisect_right(self.labels, quotient)
                if stop <= start:
                    return
                factor = base_weight
                for j in range(self.moment_order+1):
                    mass = self.prefix[j][stop]-self.prefix[j][start]
                    ordinary[j] += factor*mass
                    marked[j] += factor*(used_sum*mass
                        +self.marked_prefix[j][stop]-self.marked_prefix[j][start])
                    factor *= root_product
                return
            for i in range(start, len(self.labels)-remaining+1):
                minimum = 1
                for j in range(i, i+remaining):
                    minimum *= self.labels[j]
                if minimum > quotient:
                    break
                visit(i+1, quotient//self.labels[i], remaining-1,
                      base_weight*self.weights[i], root_product*self.roots[i],
                      used_sum+self.weights[i])

        visit(0, limit, level, arb(1), arb(1), arb(0))
        result = ExclusionVector(
            MomentVector(self.exponent, limit, level, tuple(ordinary)),
            MomentVector(self.exponent, limit, level, tuple(marked)))
        self.exclusion_cache[key] = result
        return result
