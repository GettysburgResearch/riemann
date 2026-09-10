#!/usr/bin/env python3
"""Finite arithmetic/source controls, not independent mathematical review."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import copy, sys, unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
import check
from intervals import I,C,S,exp_i,exp_c,log_i,pi_i_cached,gamma_prefactor,bernoulli_numbers

class Controls(unittest.TestCase):
    def test_rational_arithmetic(self):
        for a in [F(-7,5),F(-1,9),F(0),F(2,3),F(11,4)]:
            for b in [F(-2,7),F(1,3),F(5,2)]:
                self.assertTrue((I.point(a)+I.point(b)).contains(a+b))
                self.assertTrue((I.point(a)*I.point(b)).contains(a*b))
                self.assertTrue((I.point(a)/I.point(b)).contains(a/b))
    def test_elementary_function_identities(self):
        for x in [F(1,8),F(3,2),F(7),F(101,10)]:
            self.assertTrue(log_i(exp_i(I.point(x))).contains(x))
        z=exp_c(C(I.point(0),pi_i_cached()))
        self.assertTrue(z.re.contains(-1));self.assertTrue(z.im.contains(0))
        self.assertLess(F(128,127)**25,2)
    def test_gamma_exact_value(self):
        p,_=gamma_prefactor(C.point(0))
        self.assertTrue(p.re.contains(1));self.assertTrue(p.im.contains(0))
    def test_gamma_recurrence(self):
        q=C.point(F(-5,4),F(2));p,h=gamma_prefactor(q)
        p1,h1=gamma_prefactor(q+C.point(1))
        from intervals import log_i
        c=pi_i_cached()/6
        e=p1-(p*(-q)).scale(c)
        self.assertTrue(e.re.contains(0));self.assertTrue(e.im.contains(0))
        e=h1-h-C.point(1)/q
        self.assertTrue(e.re.contains(0));self.assertTrue(e.im.contains(0))
    def test_independent_source_moments(self):
        b=bernoulli_numbers(42)
        expected=[(-1)**n*6**(n+1)*2**(2*n+1)*b[2*n+2]/factorial(2*n+2) for n in range(21)]
        self.assertEqual(check.moments(20),expected)
        for m in (3,10):
            x,w,beta,A,p,d=check.seed(m)
            self.assertTrue(A.contains(m*(2*m+3)))
        self.assertEqual(check.seed(3)[5],F(64,876750875))
    def test_bad_primitive_bracket_refused(self):
        old=copy.deepcopy(check.BRACKETS['3'])
        check.seed.cache_clear()
        try:
            check.BRACKETS['3'][0]=['1/1000','2/1000']
            with self.assertRaises(ArithmeticError):check.seed(3)
        finally:
            check.BRACKETS['3']=old;check.seed.cache_clear()
    def test_lower_modulus(self):
        self.assertLessEqual(check.lower_modulus(C.point(3,4)),5)
        self.assertGreater(check.lower_modulus(C.point(3,4)),F(4999,1000))

if __name__=='__main__':unittest.main()
