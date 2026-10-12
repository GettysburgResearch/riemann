#!/usr/bin/env python3
"""Independent native-source controls for the parameterized certificate builder."""
from fractions import Fraction as Q
import unittest
from flint import arb,ctx
from check_threshold_arb import mobius_sieve
from exclusion_power_data import build_power_data
from verify_horizon_stitch import as_arb

ctx.prec=192

def trial_mobius(n):
    sign=1;divisor=2
    while divisor*divisor<=n:
        if n%divisor==0:
            n//=divisor;sign=-sign
            if n%divisor==0:return 0
        divisor+=1
    return -sign if n>1 else sign


def native_value(power,endpoint):
    denominator=4*arb(endpoint).sqrt()-3
    result=arb(0)
    for n in range(1,endpoint+1):
        beta=trial_mobius(n)-(trial_mobius(n//67) if n%67==0 else 0)
        if beta:
            ratio=(4*(arb(endpoint)/n).sqrt()-3)/denominator
            result+=beta*ratio**as_arb(power)/arb(n).sqrt()
    return result

class ParametricControls(unittest.TestCase):
    def test_bounded_four_level_margin_against_native_source(self):
        endpoints=[1,10,67,134,210,1000]
        for power in [Q(19,15),Q('1.9')]:
            result=build_power_data(power,mobius_sieve(80),1000,endpoints)
            for endpoint,row in result['finite'].items():
                lower=1-row['odd']+row[2][0]-row['triple']+(1-row['odd']/5)*row[4][0]
                native=native_value(power,endpoint)
                self.assertTrue(bool(native>=lower))
                self.assertTrue(bool(native>0))

    def test_cutoff_and_source_metadata(self):
        result=build_power_data(Q(19,15),mobius_sieve(80),1000,[1,1000])
        self.assertEqual(result['one'].cutoff,500)
        self.assertEqual(result['one'].exponent,Q(17,15))
        for k,vector in result['selected'].items():
            self.assertEqual(vector.ordinary.level,k)
            self.assertEqual(vector.marked.level,k)
            self.assertEqual(vector.ordinary.cutoff,1000)
            self.assertEqual(vector.marked.cutoff,1000)
        self.assertTrue(bool(result['infinite_one']-result['one'][0]>0))

    def test_invalid_parametric_domains(self):
        mu=mobius_sieve(80)
        with self.assertRaises(ValueError):build_power_data(Q(1),mu,1000,[1000])
        with self.assertRaises(ValueError):build_power_data(Q('1.3'),mu,100,[100])
        with self.assertRaises(ValueError):build_power_data(Q('1.3'),mu,1000,[1001])
        with self.assertRaises(ValueError):build_power_data(Q('1.3'),mu,1000,[0])

if __name__=='__main__':unittest.main()
