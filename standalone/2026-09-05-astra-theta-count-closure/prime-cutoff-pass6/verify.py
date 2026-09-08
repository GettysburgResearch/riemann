#!/usr/bin/env python3
"""Finite exact checks for prime-cutoff-pass6, NOT a proof of RH or analysis.
Python standard library only. Execute normally and with -O.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import io
import json
import unittest

D, C = F(1, 4), F(5, 4)

@dataclass(frozen=True)
class G:
    re: F
    im: F = F(0)
    def __add__(self, other):
        o = other if isinstance(other, G) else G(F(other))
        return G(self.re + o.re, self.im + o.im)
    __radd__ = __add__
    def __neg__(self):
        return G(-self.re, -self.im)
    def __sub__(self, other):
        return self + (-other if isinstance(other, G) else -F(other))
    def __rsub__(self, other):
        return -self + other
    def __mul__(self, other):
        o = other if isinstance(other, G) else G(F(other))
        return G(self.re*o.re-self.im*o.im, self.re*o.im+self.im*o.re)
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = other if isinstance(other, G) else G(F(other))
        d = o.re*o.re + o.im*o.im
        if not d:
            raise ZeroDivisionError('Gaussian-rational division by zero')
        return G((self.re*o.re+self.im*o.im)/d,
                 (self.im*o.re-self.re*o.im)/d)
    def __pow__(self, n):
        if type(n) is not int or n < 0:
            raise ValueError('nonnegative integer exponent required')
        out, b = G(F(1)), self
        while n:
            if n & 1:
                out = out*b
            b = b*b
            n //= 2
        return out
    def conjugate(self):
        return G(self.re, -self.im)


def ratios(m):
    m = F(m)
    return (C/(4*m-3), 3*C*C/((4*m-3)*(4*m-5)),
            15*C**3/((4*m-3)*(4*m-5)*(4*m-7)))


def variance(m):
    m = F(m)
    return 5*(2*m*m+9*m+25)/(4*(4*m-7)*(2*m*m+m+5))


def beta_coefficient(m, j):
    """J_j/(pi sqrt(C)), an exact rational for integer m,j."""
    if type(m) is not int or type(j) is not int or m < 2 or not 0 <= j <= 3:
        raise ValueError('unsupported test parameters')
    return (C**(j-2*m) * F(factorial(2*j), 4**j*factorial(j))
            * F(factorial(4*m-2*j-2),
                4**(2*m-j-1)*factorial(2*m-j-1)*factorial(2*m-1)))


def norm_formula(m):
    return (4*C**m)**2 * F(factorial(2*m-4),
                2**(2*m-2)*(m-1)*factorial(m-2)**2)


def poly_norm(m):
    p = {m-2: (4*C**m)/factorial(m-2),
         m-1: -(4*C**m)/factorial(m-1)}
    return sum((v*w*F(factorial(i+j), 2**(i+j+1))
                for i,v in p.items() for j,w in p.items()), F(0))


def exp_lower(x, degree=9):
    return sum((F(x)**j/factorial(j) for j in range(degree+1)), F(0))


class ExactChecks(unittest.TestCase):
    def test_beta_second_moment(self):
        for m in range(2, 41):
            j0,j1,j2,j3 = [beta_coefficient(m,j) for j in range(4)]
            self.assertEqual((j3+2*D*j2+D*D*j1)/(j2+2*D*j1+D*D*j0),
                             variance(m))

    def test_rational_ratio_identity(self):
        for m in [F(j,2) for j in range(4,81)]:
            r1,r2,r3=ratios(m)
            self.assertEqual((r3+2*D*r2+D*D*r1)/(r2+2*D*r1+D*D),variance(m))

    def test_uniform_polynomial_identity(self):
        # Both are explicitly degree-three polynomials; four distinct inputs
        # suffice for their identity. Positivity of coefficients is separate.
        for k in [F(0),F(1,2),F(2),F(9)]:
            m=k+5
            self.assertEqual(22*m**3-85*m*m-73*m-140,
                             22*k**3+245*k*k+727*k+120)
        self.assertTrue(all(x>0 for x in [22,245,727,120]))

    def test_variance_upper_instances(self):
        for m in [F(j,2) for j in range(10,129)]:
            self.assertLess(variance(m),1/m)

    def test_archimedean_constants(self):
        self.assertLess(F(64)+F(3,2),4*17)
        self.assertLessEqual(F(17,17),1)
        self.assertEqual(sum((F(1,j) for j in range(1,9)),F(0))-F(11,5),F(29,56))
        self.assertGreater(F(29,56),F(1,2))
        self.assertGreater(exp_lower(F(11,5)),9)

    def test_explicit_cutoff_witness(self):
        self.assertGreater(exp_lower(5),100)
        self.assertLess(variance(25),F(1,25))
        self.assertGreater(1-F(25,2)*variance(25),F(1,2))
        self.assertLess(-5+17*variance(25),-4)

    def test_linear_frequency_bound(self):
        for N in range(24, 201):
            lo=F(N-1)/(F(2*N-1,2)/C+F(N*N,16)/F(2*N-3,2))
            self.assertGreater(lo,F(9,8))
            k=N-24
            self.assertEqual(19*N*N-448*N+528,19*k*k+464*k+720)
        for N in range(84, 201):
            q=1-2*F(9,8)+F(N-2,N-1)*F(9,8)**2
            self.assertEqual(q,F(N-82,64*(N-1)))
            self.assertGreater(q,0)
            self.assertLess(F(N-1,N-2),F(9,8))

    def test_exponential_cutoff_instance(self):
        self.assertGreater(exp_lower(1,5),F(27,10))
        self.assertGreater(F(27,10)**42,10**18)
        self.assertLess(-5+17*variance(42),-4)
        self.assertEqual(F(84-82,64*(84-1)),F(1,2656))

    def test_inverse_laplace(self):
        for m in [2,3,17,25]:
            for A in [F(0),F(1,4),F(1),F(3,2),F(10)]:
                integ=(4*C**m)*(1/(A+1)**(m-1)-1/(A+1)**m)
                self.assertEqual(integ,(4*C**m)*A/(A+1)**m)
        self.assertEqual((4*C**25)*D/(D+1)**25,1)

    def test_original_metric_norm(self):
        for m in [2,3,5,17,25,40]:
            self.assertEqual(poly_norm(m),norm_formula(m))
            self.assertGreater(norm_formula(m),0)

    def test_integral_normalization(self):
        for m in [2,3,17,25,40]:
            r1,r2,_=ratios(m)
            lhs=(4*C**m)**2*(beta_coefficient(m,2)+2*D*beta_coefficient(m,1)+D*D*beta_coefficient(m,0))
            rhs=F(comb(4*m-2,2*m-1),4**(2*m-1))*(1+8*r1+16*r2)
            self.assertEqual(lhs,rhs)
            self.assertGreater(rhs,0)

    def test_entire_zero_tail_margin(self):
        base=F(227**6,196**2*10000**3)
        self.assertLess(base,F(1,16))
        self.assertLess(F(227,10000),1)
        for s in range(6,41):
            ratio=F(227**s,196**2*10000**(s-3))
            self.assertEqual(ratio,base*F(227,10000)**(s-6))
            self.assertLess(ratio,F(1,16))

    def test_full_source_normalization(self):
        for m,n in [(3,3),(3,4),(17,25),(25,25)]:
            self.assertEqual((4*C**m)*(4*C**n)*F(15,16)*F(196**2,227**(m+n)),
                             15*196**2*F(5,908)**(m+n))

    def test_arbitrary_high_mode_synthetic_witness(self):
        I=G(F(0),F(1)); A=G(F(2),F(1))
        for M in [3,17,25,50]:
            Z=I*(A+1)**(M+2)/(A*(A-1))
            U,V=Z.im,Z.re-2*Z.im
            def R(z):
                return z*(z-1)*(U*z+V)/(z+1)**(M+2)
            self.assertEqual(R(G(F(1))),G(F(0)))
            self.assertEqual(R(A),I)
            self.assertEqual(R(A.conjugate()),-I)
            self.assertEqual(R(G(F(1)))**2+R(A)**2+R(A.conjugate())**2,G(F(-2)))
            for z in [A,G(F(1)),G(F(3,2))]:
                expanded=U*z/(z+1)**M+(V-3*U)*z/(z+1)**(M+1)+2*(U-V)*z/(z+1)**(M+2)
                self.assertEqual(expanded,R(z))

    def test_positive_entries_do_not_imply_psd(self):
        A=G(F(2),F(1))
        for s in range(6,81):
            val=G(F(1,2**s))+A**2/(A+1)**s+A.conjugate()**2/(A.conjugate()+1)**s
            self.assertEqual(val.im,0)
            self.assertGreater(val.re,0)
        self.assertEqual(10*F(2,5)**3,F(16,25))

    def test_parameter_rejections(self):
        for bad in [-1,F(1,2),True]:
            with self.assertRaises(ValueError):
                G(F(1))**bad
        with self.assertRaises(ZeroDivisionError):
            G(F(1))/G(F(0))


def reject_duplicate(pairs):
    d={}
    for k,v in pairs:
        if k in d:
            raise ValueError('duplicate JSON key: '+k)
        d[k]=v
    return d


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',type=Path)
    args=ap.parse_args()
    report_stream=io.StringIO()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactChecks)
    run=unittest.TextTestRunner(stream=report_stream,verbosity=0).run(suite)
    if not run.wasSuccessful():
        raise RuntimeError(report_stream.getvalue())
    result={
        'status':'PASS_FINITE_EXACT_CUTOFF_CONTROLS',
        'tests':run.testsRun,
        'arithmetic':'EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL',
        'scope':'finite identities, constants, norm and synthetic controls only',
        'analytic_proofs_machine_checked':False,
        'actual_prime_sums_evaluated':False,
        'rh_proved':False,
        'unrestricted_matrix_sign_proved':False,
        'witness':{'m':42,'prime_cutoff':10**18,'variance':str(variance(42)),
                   'second_moment_bound':'1/42','fourier_ratio_margin':'1/2656',
                   'zero_tail_ratio_at_s6':str(F(227**6,196**2*10000**3))}}
    canonical=json.dumps(result,sort_keys=True,separators=(',',':'))
    if args.check:
        saved=json.loads(args.check.read_text(),object_pairs_hook=reject_duplicate)
        if json.dumps(saved,sort_keys=True,separators=(',',':'))!=canonical:
            raise ValueError('saved result differs from freshly computed result')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
