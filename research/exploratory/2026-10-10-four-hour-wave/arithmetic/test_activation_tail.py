#!/usr/bin/env python3
"""Independent prime activation and complete-bin arithmetic controls."""
from fractions import Fraction as Q
import unittest
from flint import arb,ctx
from activation_tail import kernel_upper,prime_tail_bins,numerator_polynomial
from check_threshold_arb import mobius_sieve
from verify_four_label import prime_power_sum
from verify_horizon_stitch import as_arb,primes_through
from weighted_moments import WeightedMoments

ctx.prec=192

class ActivationControls(unittest.TestCase):
    def test_kernel_envelopes_against_literal_numerators(self):
        N=1000
        for m in [Q(9,7),Q('1.3'),Q('1.9')]:
            for C in [500,750,1000,1250,1500]:
                polynomial=kernel_upper(m,C,N)
                for ratio in [Q(0),Q(1,10),Q(1,2),Q(9,10),Q(1)]:
                    z=as_arb(ratio)/arb(N).sqrt()
                    upper=sum((c*z**j for j,c in enumerate(polynomial)),arb(0))
                    literal=(1-3*arb(C).sqrt()*z/4)**as_arb(m)
                    self.assertTrue(bool(upper>=literal) if ratio==0 else bool(upper>literal))

    def test_complete_prime_bins_against_independent_sums(self):
        N=1000; a=Q('1.15');engine=WeightedMoments(a,N)
        selected=engine.cumulative(1,500);mu=mobius_sieve(80)
        V=prime_power_sum(a,1,mu)
        bins=prime_tail_bins(a,selected,V,N)
        self.assertEqual([edge for edge,mass in bins],[500,750,1000,1250,1500])
        ctx.prec=256
        independent_primes=primes_through(1500)
        actual=[]
        for left,right in zip([500,750,1000,1250],[750,1000,1250,1500]):
            mass=sum((arb(q)**(-as_arb(a)) for q in independent_primes if left<q<=right),arb(0))
            actual.append(mass)
        high_V=prime_power_sum(a,1,mu)
        high_selected=sum((arb(q)**(-as_arb(a)) for q in independent_primes if q<=500),arb(0))
        high_selected+=arb(67)**(-as_arb(a))
        actual.append(high_V-high_selected-sum(actual,arb(0)))
        for (_,upper),value in zip(bins,actual):
            self.assertTrue(bool(upper>value))
        ctx.prec=192

    def test_activation_bound_including_inactive_representatives(self):
        m=Q(9,7);N=1000;C=1500
        for x,q in [(1000,1511),(1400,1511),(1500,1511),(2000,1511),(10000,1511)]:
            numerator=(1-3*(arb(C)/x).sqrt()/4)**as_arb(m)
            upper=numerator/(1-3/(4*arb(x).sqrt()))**as_arb(m)
            actual=arb(0) if q>x else ((1-3*(arb(q)/x).sqrt()/4)/(1-3/(4*arb(x).sqrt())))**as_arb(m)
            self.assertTrue(bool(upper>actual))

    def test_invalid_activation_domains(self):
        with self.assertRaises(ValueError):kernel_upper(Q(1),500,1000)
        with self.assertRaises(ValueError):kernel_upper(Q('1.3'),2000,1000)
        engine=WeightedMoments(Q('1.15'),1000);selected=engine.cumulative(1,500)
        V=prime_power_sum(Q('1.15'),1,mobius_sieve(80))
        with self.assertRaises(ValueError):prime_tail_bins(Q('1.15'),selected,V,1000,[2,3,5])
        with self.assertRaises(ValueError):numerator_polynomial(Q('1.3'),Q('1.4'),selected,{},V,1000)

if __name__=='__main__':unittest.main()
