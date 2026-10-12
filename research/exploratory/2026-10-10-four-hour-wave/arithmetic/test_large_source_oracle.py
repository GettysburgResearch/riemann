#!/usr/bin/env python3
"""Literal integer-factor source oracle for the parameterized large builder.

Avoids its sieve, labels, subset recursion, final-label prefixes and caches.
Projected multiplicities at67 are counted directly from integer factors.
"""
from fractions import Fraction as Q
import unittest
from flint import arb, ctx
from check_threshold_arb import mobius_sieve
from exclusion_power_data import build_power_data
from verify_horizon_stitch import as_arb

ctx.prec = 192


def source_factors(n):
    factors = []
    multiplicity = 1
    divisor = 2
    while divisor*divisor <= n:
        exponent = 0
        while n % divisor == 0:
            n //= divisor
            exponent += 1
        if exponent:
            if exponent > (2 if divisor == 67 else 1):
                return None
            factors.extend([divisor]*exponent)
            if divisor == 67 and exponent == 1:
                multiplicity *= 2
        divisor += 1
    if n > 1:
        factors.append(n)
        if n == 67:
            multiplicity *= 2
    return factors, multiplicity


class LargeSourceOracle(unittest.TestCase):
    def test_selected_moments_from_independent_integer_factors(self):
        cutoff = 40000
        for power in (Q(19, 15), Q(19, 10)):
            a = (power+1)/2
            data = build_power_data(power, mobius_sieve(80), cutoff, [1, cutoff])
            direct = {k: ([arb(0)]*7, [arb(0)]*7) for k in (2, 4, 6)}
            counts = {k: 0 for k in direct}
            for n in range(1, cutoff+1):
                source = source_factors(n)
                if source is None:
                    continue
                factors, multiplicity = source
                level = len(factors)
                if level not in direct:
                    continue
                counts[level] += multiplicity
                used = sum((arb(p)**(-as_arb(a)) for p in factors), arb(0))
                mass = multiplicity*arb(n)**(-as_arb(a))
                root = arb(n).sqrt()
                for j in range(7):
                    direct[level][0][j] += mass
                    direct[level][1][j] += mass*used
                    mass *= root
            self.assertGreater(counts[6], 0)
            self.assertEqual(source_factors(134), ([2, 67], 2))
            self.assertEqual(source_factors(4489), ([67, 67], 1))
            self.assertIsNone(source_factors(67**3))
            for level, vector in data['selected'].items():
                for j in range(7):
                    self.assertTrue(vector.ordinary[j].overlaps(direct[level][0][j]))
                    self.assertTrue(vector.marked[j].overlaps(direct[level][1][j]))

    def test_real_kernel_bounds_and_complete_odd_tail(self):
        power = Q(19, 15)
        a = (power+1)/2
        endpoints = [1, 67, 134, 4489, 30030, 40000]
        data = build_power_data(power, mobius_sieve(80), 40000, endpoints)
        sources = [(n, source_factors(n)) for n in range(1, endpoints[-1]+1)]
        for endpoint in endpoints:
            direct = {k: [arb(0), arb(0)] for k in (1, 2, 3, 4, 6)}
            denominator = 4*arb(endpoint).sqrt()-3
            for n, source in sources:
                if n > endpoint:
                    break
                if source is None:
                    continue
                factors, multiplicity = source
                level = len(factors)
                if level not in direct:
                    continue
                ratio = (4*(arb(endpoint)/n).sqrt()-3)/denominator
                value = multiplicity*ratio**as_arb(power)/arb(n).sqrt()
                direct[level][0] += value
                direct[level][1] += value*sum((arb(p)**(-as_arb(a)) for p in factors), arb(0))
            row = data['finite'][endpoint]
            # At endpoints above N/2, the finite single-label source oracle
            # includes actual larger primes and the builder prices their full tail.
            self.assertTrue(bool(row['odd'] >= direct[1][0]))
            self.assertTrue(bool(row['triple'] >= direct[3][0]))
            for level in (2, 4, 6):
                self.assertTrue(bool(row[level][0] <= direct[level][0]))
                self.assertTrue(bool(row[level][1] <= direct[level][1]))


if __name__ == '__main__':
    unittest.main()
