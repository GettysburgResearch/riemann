#!/usr/bin/env python3
"""Independent finite controls for the four-label SHARP proof."""
from collections import Counter
from fractions import Fraction as Q
import unittest

from flint import arb, ctx

from test_two_label import kernel_weight, recursive_levels, trial_mu
from verify_four_label import labelled_levels
from verify_horizon_stitch import as_arb, primes_through


class FourLabelControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ctx.prec = 192

    def test_enumeration_and_native_projection(self):
        x = 1000  # the first five-label activation is 2310, so levels <=4 suffice
        levels = labelled_levels(x, primes_through(x))
        recursive = recursive_levels(x)
        coefficients = Counter({1: 1})
        for k, values in levels.items():
            self.assertEqual(Counter(values), Counter(recursive[k]))
            for n in values:
                coefficients[n] += (-1)**k
        for n in range(1, x+1):
            beta = trial_mu(n)-(trial_mu(n//67) if n % 67 == 0 else 0)
            self.assertEqual(coefficients[n], beta)

    def test_newton_third_against_positive_elementary_update(self):
        for aq in [Q(6, 5), Q(5, 4), Q(7, 5)]:
            a = as_arb(aq)
            weights = [arb(p)**(-a) for p in primes_through(100)]+[arb(67)**(-a)]
            elementary = [arb(1), arb(0), arb(0), arb(0)]
            for weight in weights:
                for k in range(3, 0, -1):
                    elementary[k] += weight*elementary[k-1]
            powers = [sum((w**j for w in weights), arb(0)) for j in [1, 2, 3]]
            newton = (powers[0]**3-3*powers[0]*powers[1]+2*powers[2])/6
            self.assertTrue((newton-elementary[3]).contains(0))
            self.assertTrue(bool(newton > 0))

    def test_four_label_lower_bound_against_native_sum(self):
        for x in [1000, 4489]:
            recursive = recursive_levels(x)
            for m in [Q(7, 5), Q(3, 2)]:
                masses = {k: sum((kernel_weight(n, x, m) for n in values), arb(0))
                          for k, values in recursive.items()}
                native = arb(0)
                for n in range(1, x+1):
                    beta = trial_mu(n)-(trial_mu(n//67) if n % 67 == 0 else 0)
                    if beta:
                        native += beta*kernel_weight(n, x, m)
                removal = masses[1]/masses[0]
                lower = (masses[0]-masses[1]+masses[2]-masses[3]
                         +(1-removal/5)*masses[4])
                self.assertTrue(bool(native-lower > 0))


if __name__ == '__main__':
    unittest.main()
