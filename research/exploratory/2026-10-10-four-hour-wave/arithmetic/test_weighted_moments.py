#!/usr/bin/env python3
"""Independent finite controls for weighted moments and Bernstein tails."""
from fractions import Fraction as Q
from math import comb
import unittest

from flint import arb, ctx

from polynomial_tail import bernstein_coefficients, certify_positive_tail
from test_two_label import recursive_levels
from verify_horizon_stitch import as_arb
from weighted_moments import (WeightedMoments, binomial_coefficients,
                              normalized_level_bounds)


class WeightedControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ctx.prec = 192

    def test_last_label_prefix_against_direct_subset_moments(self):
        x = 1000
        direct = recursive_levels(x)
        for a in [Q('1.15'), Q('1.16'), Q('1.2')]:
            weighted = WeightedMoments(a, x)
            for k in [2, 3, 4]:
                moments = weighted.cumulative(k, x)
                for j, value in enumerate(moments):
                    expected = sum((arb(n)**as_arb(-a+Q(j, 2))
                                    for n in direct[k]), arb(0))
                    self.assertTrue((value-expected).contains(0))
        counts = WeightedMoments(Q(0), x, moment_order=0)
        for k in [2, 3, 4]:
            self.assertEqual(counts.cumulative(k, x)[0], arb(len(direct[k])))

    def test_binomial_bounds_against_literal_kernel(self):
        for m in [Q('1.32'), Q('1.4'), Q('1.9')]:
            coefficients = binomial_coefficients(m)
            for v in [Q(0), Q(1, 10), Q(1, 2), Q(3, 4)]:
                lower = as_arb(sum((coefficients[j]*v**j for j in range(6)), Q(0)))
                upper = lower+as_arb(4*coefficients[6]*v**6)
                actual = (1-as_arb(v))**as_arb(m)
                if v == 0:
                    self.assertTrue((actual-lower).contains(0))
                else:
                    self.assertTrue(bool(actual-lower > 0))
                    self.assertTrue(bool(upper-actual > 0))

    def test_bernstein_identity_and_nontrivial_subdivision(self):
        polynomial = [as_arb(Q(17, 13)), as_arb(Q(-9, 7)),
                      as_arb(Q(4, 11)), as_arb(Q(5, 3))]
        left, right = as_arb(Q(1, 8)), as_arb(Q(3, 8))
        bernstein = bernstein_coefficients(polynomial, left, right)
        d = len(polynomial)-1
        for tq in [Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)]:
            t = as_arb(tq)
            z = left+(right-left)*t
            power_value = sum((c*z**j for j, c in enumerate(polynomial)), arb(0))
            bernstein_value = sum((b*comb(d, i)*t**i*(1-t)**(d-i)
                                   for i, b in enumerate(bernstein)), arb(0))
            self.assertTrue((power_value-bernstein_value).contains(0))
        positive = [as_arb(Q(1, 16)+Q(1, 10000)), as_arb(Q(-1, 2)), arb(1)]
        proof = certify_positive_tail(positive, 4)
        self.assertGreater(proof['bernstein_leaf_count'], 1)
        with self.assertRaises(ValueError):
            certify_positive_tail([arb('-0.1'), arb(1)], 4, max_depth=3)

    def test_metadata_and_domain_guards(self):
        weighted = WeightedMoments(Q('1.2'), 1000)
        moments = weighted.cumulative(2, 200)
        with self.assertRaises(ValueError):
            normalized_level_bounds(Q('1.32'), 200, moments)
        with self.assertRaises(ValueError):
            normalized_level_bounds(Q('1.4'), 100, moments)
        with self.assertRaises(ValueError):
            weighted.cumulative(1, 501)
        with self.assertRaises(ValueError):
            weighted.cumulative(5, 1000)
        with self.assertRaises(ValueError):
            binomial_coefficients(Q(1))


if __name__ == '__main__':
    unittest.main()
