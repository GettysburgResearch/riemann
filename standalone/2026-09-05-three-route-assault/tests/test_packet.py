"""Bounded exact algebra and rejection tests; not a formal analytic proof."""
import importlib.util
from fractions import Fraction as F
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'code'))
from exact import det, inverse, matrix, mul, eye, projection, positive_definite
from verify import Checks, companion, discrete_abel, hilbert_packet, route1, route2, route3, run_all

class ExactAlgebra(unittest.TestCase):
    def test_inverse(self):
        a=matrix([[2,1,0],[1,3,1],[0,1,2]])
        self.assertEqual(mul(a,inverse(a)),eye(3))
    def test_singular_rejected(self):
        with self.assertRaises(ValueError): inverse(matrix([[1,1],[1,1]]))
    def test_ragged_rejected(self):
        with self.assertRaises(ValueError): matrix([[1],[1,2]])
    def test_nonunit_companion_rejected(self):
        with self.assertRaises(ValueError): companion([F(2),F(3)])
    def test_false_assertion_still_rejected(self):
        with self.assertRaises(ArithmeticError): Checks().require('mutation',False,'deliberate failure')
    def test_source_covariance(self):
        a,b,joint=F(1,2),F(1,4),F(1,4)
        self.assertGreater(joint-a*b,0)
        self.assertLess(a*b,joint)
    def test_abel_length_rejected(self):
        with self.assertRaises(ValueError): discrete_abel([F(1)],[F(1),F(2)])
    def test_source_pair_symmetry_rejected(self):
        with self.assertRaises(ValueError): hilbert_packet([F(2)],{F(2):1},2,Checks())
    def test_duplicate_source_rejected(self):
        with self.assertRaises(ValueError): hilbert_packet([F(1),F(1)],{F(1):1},2,Checks())
    def test_projection_idempotent(self):
        p=projection([[F(1),F(2),F(3)]],3)
        self.assertEqual(mul(p,p),p)
    def test_psd_is_not_pd(self):
        self.assertFalse(positive_definite(matrix([[1,1],[1,1]])))
    def test_single_pair_sharp_and_wrong_factor_rejected(self):
        row=hilbert_packet([F(2),F(1,2)],{F(2):1,F(1,2):1},2,Checks())
        h=F(row['horizontal_trace']); delta=F(row['surplus'])
        self.assertEqual(delta,8*h+8*h*h)
        self.assertNotEqual(delta,4*h+8*h*h)
    def test_all_real_has_no_horizontal_charge(self):
        row=hilbert_packet([F(1),F(-1)],{F(1):3,F(-1):1},2,Checks())
        self.assertEqual(row['horizontal_trace'],'0')
    def test_route1(self): route1(Checks())
    def test_route2(self): route2(Checks())
    def test_route3(self): route3(Checks())
    def test_global_claims_stay_open(self):
        result=run_all()
        self.assertFalse(result['rh_proved'])
        self.assertFalse(result['analytic_proofs_machine_verified'])
        self.assertFalse(result['route2']['new_power_saving'])
        self.assertFalse(result['route3']['arithmetic_horizontal_bound'])

if __name__=='__main__': unittest.main()
