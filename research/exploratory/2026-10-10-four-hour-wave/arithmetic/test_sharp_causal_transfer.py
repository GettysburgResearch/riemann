#!/usr/bin/env python3
"""Symbolic and rational controls of the SHARP causal transfer."""
from math import isqrt
import unittest
import sympy as s


class CausalControls(unittest.TestCase):
    def test_exact_differential_forcing_and_boundary(self):
        u = s.Symbol('u', real=True)
        m = s.Symbol('m', real=True)
        z = s.Symbol('z', positive=True)
        g = 4*s.exp(u/2)-3
        # D=(z/2)d/dz, so D(D-1/2)=(z^2/4)d^2/dz^2.
        derivative = z*z*s.diff((4*z-3)**m, z, 2)/4
        expected = 4*m*(m-1)*z*z*(4*z-3)**(m-2)
        self.assertEqual(s.simplify(derivative-expected), 0)
        self.assertEqual((g**m).subs(u, 0), 1)
        self.assertEqual(s.diff(g**m, u).subs(u, 0), 2*m)

    def test_integer_kernel_convolution_and_horizon_integral(self):
        u = s.Symbol('u', nonnegative=True)
        z = s.Symbol('z', positive=True)
        g = 4*s.exp(u/2)-3
        kernels = {2: s.Rational(16, 5)*s.exp(u)-s.Rational(6, 5)*s.exp(-3*u/2),
                   3: 32*s.exp(3*u/2)-s.Rational(144, 5)*s.exp(u)+s.Rational(4, 5)*s.exp(-3*u/2)}
        for m, k in kernels.items():
            forcing = 4*m*(m-1)*s.exp(u)*g**(m-2)
            self.assertEqual(s.simplify(s.diff(k, u)+3*k/2-forcing), 0)
            self.assertEqual(k.subs(u, 0), 2*(m-1))
            # Exact exponential integration, in z=e^(u/2), avoids a
            # symbolic integrator's unnecessary branch-case search.
            terms = ((s.Rational(16,5),s.Integer(1)),(s.Rational(-6,5),s.Rational(-3,2))) if m==2 else (
                (s.Integer(32),s.Rational(3,2)),(s.Rational(-144,5),s.Integer(1)),(s.Rational(4,5),s.Rational(-3,2)))
            convolution = sum(c*(4*(z-z**(2*lam))/(s.Rational(1,2)-lam)
                                      -3*(1-z**(2*lam))/(-lam)) for c,lam in terms)
            self.assertEqual(s.cancel((4*z-3)+convolution-(4*z-3)**m), 0)
        K = s.Rational(16, 5)*s.exp(u)+s.Rational(4, 5)*s.exp(-3*u/2)-4
        self.assertEqual(s.diff(K, u), kernels[2])
        self.assertEqual(K.subs(u, 0), 0)

    def test_exact_two_atom_method_counterexample(self):
        q, C = 16, 62
        self.assertEqual(q*q, 256)
        self.assertEqual(4*q-3-C, -1)
        self.assertLess(C*C, q**3)
        self.assertEqual(isqrt(q**3), 64)
        self.assertEqual(64**2, q**3)
        self.assertGreater(-3, -3*q)
        self.assertEqual(-C*q, -992)


if __name__ == '__main__':
    unittest.main()
