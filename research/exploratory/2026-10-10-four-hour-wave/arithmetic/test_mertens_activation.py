#!/usr/bin/env python3
"""Explicit scalar guards and finite-source controls of the activation estimate.

Finite beta truncations below test the general partial-summation bound;
they do not certify a native infinite Mertens hypothesis or zero-free line.
"""
from fractions import Fraction as Q
import unittest
from flint import arb,ctx
from verify_horizon_stitch import as_arb

ctx.prec=192

def mobius(n):
    sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    return -sign if n>1 else sign


class MertensActivationControls(unittest.TestCase):
    def test_exact_rational_constants(self):
        eta=Q(7,8)
        K1=Q(1,4)+1/(1-eta)+Q(9,8)/(eta-Q(1,2))
        K15=Q(1,8)+Q(5,4)/(Q(5,4)-eta)+Q(63,32)/(eta-Q(3,4))
        self.assertEqual(K1,Q(45,4));self.assertEqual(K15,Q(461,24))
        factor=K15*Q(67,66)*Q(5,2)
        self.assertEqual(factor,Q(154435,3168));self.assertLess(factor,49)
        self.assertEqual(Q(45)/Q(3,8),120)
        # theta_ext<7/8 iff sqrt(921)>485/16.
        self.assertGreater(921*256,485**2)

    def test_finite_signed_source_piecewise_error(self):
        eta=Q(7,8);N=5000
        beta=[0]+[mobius(n)-(mobius(n//67) if n%67==0 else 0) for n in range(1,N+1)]
        prefix=0;constant=arb(0)
        for n,value in enumerate(beta[1:],1):
            prefix+=value;candidate=(abs(prefix)/arb(n)**as_arb(eta)).upper()
            if bool(candidate>constant):constant=candidate
        self.assertTrue(constant.is_exact());self.assertTrue(bool(constant>=1))
        for m in [Q(1),Q(19,15),Q(3,2),Q(7,4),Q(19,10),Q(21,10)]:
            a=(m+1)/2
            main=sum((value*arb(n)**(-as_arb(a)) for n,value in enumerate(beta[1:],1) if value),arb(0))
            for x in [Q(1),Q(67),Q(134),Q(269,2),Q(4489),Q(5000),Q(10000)]:
                endpoint=as_arb(x);actual=arb(0)
                for n,value in enumerate(beta[1:],1):
                    if n*x.denominator>x.numerator:break
                    if value:
                        actual+=value*arb(n)**(-as_arb(a))*(1-3*(arb(n)/endpoint).sqrt()/4)**as_arb(m)
                d=eta-m/2
                L=endpoint.log() if d==0 else (endpoint**as_arb(d)-1)/as_arb(d)
                error=constant*((arb(4)**(-as_arb(m))+as_arb(a/(a-eta)))
                    *endpoint**as_arb(eta-a)+as_arb(3*m*(2*a+1)/8)*L/endpoint.sqrt())
                self.assertTrue(bool(abs(actual-main)<error))

    def test_native_jump_coefficient(self):
        self.assertEqual(mobius(67)-mobius(1),-2)
        self.assertEqual(mobius(4489)-mobius(67),1)
        # T(1)=1 gives scaled h_m(1)=4^-m; this includes the endpoint atom.
        for m in [Q(1),Q(19,15),Q(3,2)]:
            self.assertTrue(((1-arb(3)/4)**as_arb(m)).overlaps(arb(4)**(-as_arb(m))))

if __name__=='__main__':unittest.main()
