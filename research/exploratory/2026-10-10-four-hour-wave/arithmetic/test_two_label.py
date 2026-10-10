#!/usr/bin/env python3
"""Independent finite source/level controls for the two-label certificate."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction as Q
import unittest

from flint import arb, ctx

from verify_horizon_stitch import as_arb, primes_through, removal_mass
from verify_two_label import two_label_mass, two_label_products


def trial_mu(n):
    result = 1
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            result = -result
            if n % p == 0:
                return 0
        p += 1
    return -result if n > 1 else result


def recursive_levels(endpoint):
    labels = sorted(primes_through(endpoint)+([67] if endpoint >= 67 else []))
    result = defaultdict(list)

    def visit(start, product, level):
        result[level].append(product)
        for j in range(start, len(labels)):
            new_product = product*labels[j]
            if new_product > endpoint:
                break
            visit(j+1, new_product, level+1)

    visit(0, 1, 0)
    return result


def kernel_weight(n, x, m):
    return (4*(arb(x)/n).sqrt()-3)**as_arb(m)/arb(n).sqrt()


class IndependentControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ctx.prec = 192

    def test_full_recursive_label_projection(self):
        for x in [67, 134, 4489]:
            coefficients = Counter()
            for k, products in recursive_levels(x).items():
                for n in products:
                    coefficients[n] += (-1)**k
            for n in range(1, x+1):
                beta = trial_mu(n)-(trial_mu(n//67) if n % 67 == 0 else 0)
                self.assertEqual(coefficients[n], beta)
        self.assertEqual(coefficients[67], -2)
        self.assertEqual(coefficients[134], 2)
        self.assertEqual(coefficients[4489], 1)

    def test_pair_enumeration_against_recursive_subsets(self):
        for x in [10, 134, 1000, 4489]:
            recursive = recursive_levels(x)
            products = two_label_products(x, primes_through(x))
            self.assertEqual(Counter(products), Counter(recursive[2]))

    def test_native_signed_sum_and_level_sum(self):
        for x in [67, 134, 500, 4489]:
            levels = recursive_levels(x)
            for m in [Q('1.5'), Q('1.81')]:
                native = arb(0)
                for n in range(1, x+1):
                    beta = trial_mu(n)-(trial_mu(n//67) if n % 67 == 0 else 0)
                    if beta:
                        native += beta*kernel_weight(n, x, m)
                by_level = sum(((-1)**k*sum(
                    (kernel_weight(n, x, m) for n in values), arb(0))
                    for k, values in levels.items()), arb(0))
                self.assertTrue((native-by_level).contains(0))

    def test_two_label_mass_and_removal_guard(self):
        x = 4489
        primes = primes_through(x)
        levels = recursive_levels(x)
        for m in [Q('1.5'), Q('1.81')]:
            masses = {k: sum((kernel_weight(n, x, m) for n in values), arb(0))
                      for k, values in levels.items()}
            normalized = two_label_mass(m, x, two_label_products(x, primes))
            self.assertTrue((normalized-masses[2]/masses[0]).contains(0))
            removal = removal_mass(m, x, primes)
            for k in range(1, max(masses)+1):
                slack = removal*masses[k-1]-k*masses[k]
                if k == 1:  # R is exactly M1/M0, so this level is equality.
                    self.assertTrue(slack.contains(0))
                else:
                    self.assertTrue(bool(slack > 0))


if __name__ == '__main__':
    unittest.main()
