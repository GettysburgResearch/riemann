#!/usr/bin/env python3
"""Independent exact mathematical controls for the threshold arithmetic.

The controls use the Machin identity and integer even-zeta formulas,
different prime-zeta representations, and the duplicate-67 source fibre.
They do not replace the infinite analytic derivations in POWER_THRESHOLD.md.
"""
from __future__ import annotations

from fractions import Fraction as Q
import importlib.util
from itertools import combinations
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location('arithmetic_threshold',
                                             Path(__file__).with_name('verify_power_threshold.py'))
if not SPEC or not SPEC.loader:
    raise RuntimeError('threshold module unavailable')
import sys
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


def atan_enclosure(x: Q, terms: int):
    total = sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
    next_total = total+(-1)**terms*x**(2*terms+1)/Q(2*terms+1)
    return V.Interval(min(total, next_total), max(total, next_total))


def pi_enclosure():
    return 16*atan_enclosure(Q(1, 5), 110)-4*atan_enclosure(Q(1, 239), 32)


def primes_through(n: int):
    candidates = [True]*(n+1)
    candidates[0:2] = [False, False]
    for p in range(2, n+1):
        if candidates[p]:
            for multiple in range(p*p, n+1, p):
                candidates[multiple] = False
    return [p for p, yes in enumerate(candidates) if yes]


class MathematicalControls(unittest.TestCase):
    def test_zeta_even_values_against_machin_pi(self):
        pi = pi_enclosure()
        pi2 = pi*pi
        for s, divisor in ((2, 6), (4, 90), (6, 945), (8, 9450)):
            known = V.Interval.point(1)
            for _ in range(s//2):
                known *= pi2
            known /= divisor
            computed = V.zeta_interval(Q(s))
            self.assertLessEqual(computed.lo, known.hi)
            self.assertLessEqual(known.lo, computed.hi)
            self.assertLess(computed.hi-computed.lo, Q(1, 10**30))

    def test_prime_zeta_two_against_direct_prime_sum(self):
        # Direct exact integer-square sum, with all-integer tail. This is
        # independent of Mobius-log(zeta) inversion and sufficient to catch
        # sign/index errors in that formula.
        n = 2000
        exact_prefix = sum((Q(1, p*p) for p in primes_through(n)), Q(0))
        computed = V.prime_zeta_interval(Q(2))
        self.assertGreaterEqual(computed.lo, exact_prefix)
        self.assertLessEqual(computed.hi, exact_prefix+Q(1, n))

    def test_duplicate_67_label_projection(self):
        labels = (2, 3, 67, 67)
        coefficients = {}
        for size in range(len(labels)+1):
            for indices in combinations(range(len(labels)), size):
                n = 1
                for index in indices:
                    n *= labels[index]
                coefficients[n] = coefficients.get(n, 0)+(-1)**size
        for n, coefficient in coefficients.items():
            beta = V.mobius(n)-(V.mobius(n//67) if n % 67 == 0 else 0)
            self.assertEqual(coefficient, beta)
        self.assertEqual(coefficients[67], -2)
        self.assertEqual(coefficients[67*67], 1)
        self.assertEqual(coefficients[2*67], 2)

    def test_directed_rounding_for_negative_inputs(self):
        value = -Q(1, 3)
        low, high = V.lower_round(value), V.upper_round(value)
        self.assertLessEqual(low, value)
        self.assertGreaterEqual(high, value)
        self.assertEqual(high-low, Q(1, V.DEN))

    def test_log_product_and_exponential_inverse_enclosures(self):
        # Analytic identities provide consistency checks at nonsmall inputs,
        # including range reductions in both primitive functions.
        left = V.log_point(Q(30))
        right = V.log_point(Q(2))+V.log_point(Q(3))+V.log_point(Q(5))
        self.assertLessEqual(left.lo, right.hi)
        self.assertLessEqual(right.lo, left.hi)
        exp_low = V.exp_negative_point(left.hi)
        exp_high = V.exp_negative_point(left.lo)
        self.assertLessEqual(exp_low.lo, Q(1, 30))
        self.assertGreaterEqual(exp_high.hi, Q(1, 30))

    def test_invalid_domains_fail_explicitly(self):
        for operation in (lambda: V.log_point(Q(0)),
                          lambda: V.exp_negative_point(Q(-1)),
                          lambda: V.zeta_interval(Q(1)),
                          lambda: V.Interval(Q(2), Q(1)),
                          lambda: V.Interval.point(1)/V.Interval(Q(-1), Q(1))):
            with self.assertRaises(ValueError):
                operation()


if __name__ == '__main__':
    unittest.main(verbosity=2)
