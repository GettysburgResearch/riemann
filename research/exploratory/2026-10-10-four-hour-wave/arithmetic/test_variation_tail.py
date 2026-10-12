#!/usr/bin/env python3
"""Exact finite coefficient and ac/atom separation controls for C-V1--C-V3."""
from fractions import Fraction as Q
from math import factorial
import unittest
import sympy as s


def literal_mu(n):
    value = 1
    divisor = 2
    while divisor*divisor <= n:
        exponent = 0
        while n % divisor == 0:
            n //= divisor
            exponent += 1
        if exponent > 1:
            return 0
        if exponent:
            value = -value
        divisor += 1
    return -value if n > 1 else value


class VariationTailControls(unittest.TestCase):
    def test_exact_absolute_native_coefficients_and_prefix_counts(self):
        prefix_abs = prefix_squarefree = 0
        squarefree = [0]
        for n in range(1, 10001):
            mu = literal_mu(n)
            shifted = literal_mu(n//67) if n % 67 == 0 else 0
            self.assertEqual(abs(mu-shifted), mu*mu+shifted*shifted)
            prefix_abs += abs(mu-shifted)
            prefix_squarefree += mu*mu
            squarefree.append(prefix_squarefree)
            self.assertEqual(prefix_abs, squarefree[n]+squarefree[n//67])
        for n in (67**3, 2*67**2, 3*67**4, 67**2*5**2):
            mu = literal_mu(n)
            shifted = literal_mu(n//67)
            self.assertEqual(abs(mu-shifted), mu*mu+shifted*shifted)
        self.assertEqual(abs(literal_mu(67)-literal_mu(1)), 2)
        self.assertEqual(abs(literal_mu(67**2)-literal_mu(67)), 1)

    def test_exact_native_ac_derivative_and_tail_pole_constants(self):
        u = s.symbols('u', real=True)
        phi = 16-24*s.exp(-u/2)+9*s.exp(-u)
        self.assertEqual(phi.subs(u, 0), 1)
        self.assertEqual(s.simplify(s.diff(phi, u)-3*s.exp(-u)*(4*s.exp(u/2)-3)), 0)
        # Boundary has its separate atom of mass one; the ac derivative
        # integrates from phi(0)=1 to phi(infinity)=16.
        self.assertEqual(s.integrate(s.diff(phi, u), (u, 0, s.oo)), 15)
        for c in (Q(1, 10), Q(3, 8), Q(49, 100)):
            for r in range(1, 6):
                negative_mass_constant = 1/(2*c*factorial(r-1))
                negative_ac_tail_constant = 3/(2*(1-c)*factorial(r-1))
                self.assertEqual((1-c)*negative_ac_tail_constant/3,
                                 c*negative_mass_constant)
                self.assertEqual((1-c)*negative_ac_tail_constant*factorial(r-1), Q(3, 2))


if __name__ == '__main__':
    unittest.main()
