#!/usr/bin/env python3
"""Bounded algebra/rounding tests; not a proof of Lee--Yang or all-order synthesis."""
from fractions import Fraction as F
from math import comb, factorial
from itertools import product
from pathlib import Path
import sys, json, tempfile, unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
import certify_seed as c

class SeedTests(unittest.TestCase):
    def test_interval_operations(self):
        for a in [F(-7,3),F(-1,3),F(0),F(2,7),F(11,10)]:
            for b in [F(-9,5),F(1,3),F(7,2)]:
                A=c.I.point(a);B=c.I.point(b)
                self.assertTrue((A+B).contains(a+b))
                self.assertTrue((A*B).contains(a*b))
                self.assertTrue((A/B).contains(a/b))
        for r in [F(1,3),F(2),F(13,10)]:
            self.assertTrue(c.I.point(r*r).sqrt().contains(r))

    def test_exponentials_against_fraction_series(self):
        for x in [F(-1,3),F(-1,8),F(0),F(1,8),F(1,3)]:
            p=sum((x**j/factorial(j) for j in range(101)),F(0))
            rem=2*abs(x)**101/factorial(101)
            I=c.exp(c.I.point(x))
            self.assertLessEqual(F(I.lo,c.S),p-rem)
            self.assertGreaterEqual(F(I.hi,c.S),p+rem)

    def test_derivative_bounds(self):
        self.assertEqual(c.derivative_L1_bounds(),
                         [F(60),F(366),F(3135),F(71463,2),F(2044911,4)])
        # These elementary series inequalities are used in the physical tail.
        self.assertGreater(sum(F(4)**k/factorial(k) for k in range(8)),50)
        self.assertLess(F(6,5)**4/F(2)**33,F(1,2))
        self.assertLess(F(16)/F(2)**450,F(1,2))

    def test_peano_kernel(self):
        for i in range(33):
            t=F(i,32)
            kernel=(2-t)**4/24-(4*(1-t)**3+(2-t)**3)/18
            self.assertEqual(kernel,-t**3*(4-3*t)/72)
            self.assertLessEqual(kernel,0)
            self.assertGreaterEqual(kernel,F(-1,72))
        # Simpson exactness through degree three; exact fourth-order error.
        for k in range(4):
            integ=F(2**(k+1),k+1)
            quad=F(1,3)*((1 if k==0 else 0)+4+2**k)
            self.assertEqual(integ,quad)
        self.assertEqual(F(32,5)-F(20,3),F(-4,15))

    def test_graph_vs_binomial(self):
        for q in [F(1),F(11,10),F(1101,1000),F(5,4)]:
            # Independent graph calculation: penalties for all 28 disagreeing edges.
            Z=F(0);mom={j:F(0) for j in [2,4,6]}
            for spin in product([-1,1],repeat=8):
                disagree=sum(spin[i]!=spin[j] for i in range(8) for j in range(i+1,8))
                w=q**(-disagree);Z+=w
                for j in mom:mom[j]+=w*sum(spin)**j
            mom={j:v/Z for j,v in mom.items()}
            exact=[mom[2],mom[4]-3*mom[2]**2,
                   mom[6]-15*mom[4]*mom[2]+30*mom[2]**3]
            intervals=c.cluster(q)
            for a,b in zip(intervals,exact):self.assertTrue(a.contains(b))

    def test_finite_bath_cumulants(self):
        for L in range(1,10):
            mu={j:sum(F(comb(L,k),2**L)*(2*k-L)**j for k in range(L+1))
                for j in [2,4,6]}
            self.assertEqual(mu[2],L)
            self.assertEqual(mu[4]-3*mu[2]**2,-2*L)
            self.assertEqual(mu[6]-15*mu[4]*mu[2]+30*mu[2]**3,16*L)
        # A positive solution of the algebraic variance/kurtosis repair.
        L=16;v=F(4);d=F(8);t=F(3,20);g=1-v*t
        A=d*t*t+2*g*g/L;D=d+2*v*v/L
        calc=(c.I.point(2*v/L)+(c.I.point(D*A-2*d/L)).sqrt())/D
        self.assertTrue(calc.contains(t))
        self.assertEqual((d+2*v*v/L)*t*t-4*v*t/L+F(2,L)-A,0)

    def test_raw_phase_and_mixture_control(self):
        # A positive mixture of LY laws need not be LY: (q^2+6q+1)/(8q).
        # Roots have product 1, sum -6 and positive discriminant 32,
        # so they are distinct negative real numbers, not both unit modulus.
        self.assertEqual(6**2-4,32)
        self.assertGreater(6,2)
        # Cycle current conservation leaves exactly one integer flow.
        for flow in product(range(-2,3),repeat=3):
            div=[flow[0]-flow[2],flow[1]-flow[0],flow[2]-flow[1]]
            self.assertEqual(all(x==0 for x in div),len(set(flow))==1)

    def test_strict_receipt_types(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'result.json'
            for txt in ['{"schema":1,"schema":2}','{"schema":1.0}','{"a":NaN}']:
                p.write_text(txt)
                with self.assertRaises(ValueError):c.strict_json(p)
        self.assertNotEqual(json.dumps({'schema':True},sort_keys=True),
                            json.dumps({'schema':1},sort_keys=True))

if __name__=='__main__':unittest.main(verbosity=2)
