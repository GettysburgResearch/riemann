#!/usr/bin/env python3
import importlib.util
import unittest
from fractions import Fraction as Q
from pathlib import Path

P=Path(__file__).resolve().parents[1]/'verify.py'
S=importlib.util.spec_from_file_location('x27206',P); V=importlib.util.module_from_spec(S); S.loader.exec_module(V)

class Tests(unittest.TestCase):
    def test_full_suite(self):
        self.assertEqual(V.run()['classification'],'EXACT_DYADIC_DIVERGENCE_COMMUTATOR_INTERFACES_VERIFIED')
    def test_divergence(self):
        Y=19; a=Q(3,5); wY,wX=V.targets(Y,a,8); rY=V.divergence(wY,Y); rX=V.divergence(wX,2*Y)
        self.assertEqual(V.rhs(rY,rX,wX[2],Y,a),rX)
    def test_flow_columns(self):
        Y=23; a=Q(7,11); wY,wX=V.targets(Y,a,2); rY=V.divergence(wY,Y); rX=V.divergence(wX,2*Y)
        d=V.upper_flow(V.tree_flow(rY,Y),rX,wX[2],Y,a)
        self.assertEqual(V.boundary(d,2*Y),rX); self.assertEqual(V.loads(d,2*Y),wX)
    def test_missing_bottom_fails(self):
        Y=17; a=Q(2,7); wY,wX=V.targets(Y,a,3); rY=V.divergence(wY,Y); rX=V.divergence(wX,2*Y)
        self.assertNotEqual(V.rhs(rY,rX,wX[2],Y,a,omit_bottom=True),rX)
    def test_missing_commutator_fails(self):
        Y=29; a=Q(5,8); wY,wX=V.targets(Y,a,1); rY=V.divergence(wY,Y); rX=V.divergence(wX,2*Y)
        self.assertNotEqual(V.rhs(rY,rX,wX[2],Y,a,omit=11),rX)
    def test_increment(self):
        X=47; w={q:(Q(13,17*q) if q<X else Q(0)) for q in range(2,X+1)}; r=V.divergence(w,X); d=V.tree_flow(r,X)
        self.assertEqual(V.loads(d,X),w)

if __name__=='__main__': unittest.main()
