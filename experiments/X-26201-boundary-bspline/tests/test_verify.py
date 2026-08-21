import importlib.util
import pathlib
import unittest
from fractions import Fraction

P=pathlib.Path(__file__).parents[1]/'verify.py'
spec=importlib.util.spec_from_file_location('x26201_verify',P)
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)

class TestBoundaryBSpline(unittest.TestCase):
    def test_base_polynomial(self):
        R=v.pmul([v.Q2(1),v.Q2(-2)],v.ppow([v.Q2(1),-v.SQ2],2))
        self.assertEqual(R,[v.Q2(1),-(v.Q2(2)+2*v.SQ2),v.Q2(2)+4*v.SQ2,v.Q2(-4)])

    def test_eta_convolution(self):
        R=v.pmul([v.Q2(1),v.Q2(-2)],v.ppow([v.Q2(1),-v.SQ2],2))
        D=v.pmul([v.Q2(1),v.Q2(-2)],R)
        for n in range(1,80):
            got=v.dirichlet_conv_eps_b(n,R)
            j=n.bit_length()-1 if n&(n-1)==0 else None
            want=D[j] if j is not None and j<len(D) else v.Q2(0)
            self.assertEqual(got,want)

    def test_mutated_polynomial_rejected(self):
        R=v.pmul([v.Q2(1),v.Q2(-2)],v.ppow([v.Q2(1),-v.SQ2],2))
        R[2]=R[2]+v.Q2(Fraction(1,100))
        D=v.pmul([v.Q2(1),v.Q2(-2)],R)
        canonical=v.pmul([v.Q2(1),v.Q2(-2)],v.pmul([v.Q2(1),v.Q2(-2)],v.ppow([v.Q2(1),-v.SQ2],2)))
        self.assertNotEqual(D,canonical)

    def test_euler_identity(self):
        seq=[Fraction(3,7),Fraction(-2,5),Fraction(11,13),Fraction(1,9)]
        for R in range(1,7):
            self.assertEqual(*v.euler_transform(seq,R))

    def test_eta_reserve(self):
        self.assertGreater(v.eta_lower_24(),Fraction(1,2))

if __name__=='__main__': unittest.main()
