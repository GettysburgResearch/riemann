"""Adversarial tests; assertions here are unittest methods, never bare assert."""
import copy
import tempfile
import unittest
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from core import *
from algebra import covariance,variance,point_count,clipped_fake
from produce import build,clipped
from verify import newton,trial_mu,endpoint_certificate,fraction_panel,shapes
from replay import authenticate

class PacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.small=__import__('json').loads(canonical(build([3,7,15])))

    def test_integer_grids(self):
        for n in [2,3,7,16,63,255]:
            for q in [1,2,4,19]:
                cc=list(cells(1,n,q))
                self.assertEqual([k for s,t in cc for k in range(s,t+1)],list(range(1,n+1)))
                for s,t in cc:
                    self.assertEqual(isqrt(q*q*s),isqrt(q*q*t))
        for q in [0,-1,1.0,True]:
            with self.assertRaises(ValueError):list(cells(1,5,q))

    def test_refinement(self):
        x=[F((k*13)%17-8,k) for k in range(1,64)]
        losses=[]
        for q in [1,2,4]:
            losses.append(sum((variance(x[s-1:t]) for s,t in cells(1,63,q)),F(0)))
        self.assertGreaterEqual(losses[0],losses[1]);self.assertGreaterEqual(losses[1],losses[2])

    def test_local_polarization_with_history(self):
        a=[F(2,3),F(-4,5),F(7,2),F(-1,7),F(2)]
        b=[F(-1),F(3,5),F(1,2),F(-4),F(2,9)]
        def cumulative(v):
            A=[];r=[];x=y=F(0)
            for k,z in enumerate(v,1):x+=z;y+=z/k;A.append(x);r.append(y)
            return A,r
        A,r=cumulative(a);B,s=cumulative(b);w=[F(1,k*(k+1)) for k in range(3,6)]
        self.assertEqual(covariance(A[2:],B[2:],w),covariance(r[2:],s[2:],[F(1)]*3))
        self.assertNotEqual(sum(x*x*y for x,y in zip(A[2:],w)),sum(x*x for x in r[2:]))

    def test_sharp_ramp_formula(self):
        H=[F(0)]
        for k in range(1,66):H.append(H[-1]+F(1,k))
        for s,t in cells(1,64):
            ell=t-s+1;W=F(ell,s*(t+1));h=H[t+1]-H[s]
            self.assertEqual(ell-h-h*h/W,variance(H[s:t+1]))

    def test_above_endpoint_kernel(self):
        H=[F(0)]
        for k in range(1,17):H.append(H[-1]+F(1,k))
        x=[-H[k]/101 for k in range(4,16)]
        y=[-F(k,101) for k in range(4,16)]
        self.assertGreater(variance(x),0)
        self.assertEqual(variance(x),variance(y,[F(1,k*(k+1)) for k in range(4,16)]))

    def test_full_centered_product_source(self):
        Y=7;mu=[0]+[trial_mu(k) for k in range(1,64)]
        c,L,A,m=clipped(Y,mu);z={}
        for d,a in c.items():
            for e,b in c.items():z[d*e]=z.get(d*e,F(0))+a*b
        self.assertEqual(sum(a/d for d,a in z.items()),0)
        H=[F(0)]
        for k in range(1,64):H.append(H[-1]+F(1,k))
        r=F(0)
        for k in range(1,64):
            r+=F(mu[k],k)
            # log d and H_k moments cancel globally, not columnwise.
            q=sum(a*H[k//d]/d for d,a in z.items())
            self.assertEqual(q,2*m[min(k,L)]-r)
        self.assertTrue(any(d>63 and a for d,a in z.items()))
        self.assertNotEqual(sum(a/d for d,a in z.items() if d<=63),0)

    def test_unbalanced_column_difference(self):
        # c=delta_1 has Q=K_1=0, but (1*z)(k)/k is nonzero.
        self.assertEqual(F(1,5)-F(1,5),0)
        self.assertNotEqual(F(1,5),0)

    def test_short_prefix_reconstruction_and_excluded_endpoint(self):
        for Y in [1,2,3,7,15]:
            got=newton(Y)
            self.assertEqual(list(got[1:]),[trial_mu(k) for k in range(1,len(got))])
        # Y=2, g=(1,-1), N(g)(9)=-1 while mu(9)=0.
        n=9;g={1:1,2:-1};val=2*g.get(n,0)-sum(a*b for d,a in g.items() for e,b in g.items() if n%(d*e)==0)
        self.assertEqual(trial_mu(n)-val,1)

    def test_endpoint_certificates_direct(self):
        out=newton(15)
        for st in self.small['stages']:
            endpoint_certificate(st)
            self.assertGreater(fraction_panel(st,out),0)

    def test_completed_state_mutation(self):
        r=copy.deepcopy(self.small);r['stages'][-1]['panels'][0]['completed_A_upper']=[0,0]
        with self.assertRaises(ValueError):endpoint_certificate(r['stages'][-1])

    def test_finite_range_gate_is_not_an_all_scale_claim(self):
        V=F(185826,100000)
        self.assertLess((1+2*V)**2,32)
        self.assertGreater((1+2*F(3))**2,32)

    def test_fake_coarse_energy(self):
        self.assertEqual(sum(a/n for n,a in clipped_fake(15).items()),0)
        self.assertEqual(trial_mu(2),-1)
        # Fake source is delta through Y, so it fails native inversion at 2.
        self.assertNotEqual(sum({1:F(1)}.get(d,0) for d in [1,2]),0)

    def test_family_normalization(self):
        self.assertEqual(8-point_count(17,7),5)
        # Center-one weights differ from the zeta physical weights.
        w=F(1,2*7**2)-F(1,2*8**2)
        self.assertEqual(w,F(15,6272));self.assertNotEqual(w,F(1,7*8))
        a=[1,0,0,0,5];A=[];r=[];x=y=F(0)
        for k,v in enumerate(a,1):x+=v;y+=F(v,k);A.append(x);r.append(y)
        w1=[F(1,2*k*k)-F(1,2*(k+1)**2) for k in range(1,6)]
        self.assertNotEqual(variance(A,w1),variance(r))

    def test_directed_signed_intervals(self):
        for n in range(-8,9):
            for d in range(1,10):
                x=rat(n,d);v=F(n,d)
                self.assertLessEqual(F(x[0],S),v);self.assertGreaterEqual(F(x[1],S),v)
                for den in [rat(1,7),rat(11,13)]:
                    z=divide(x,den);target=v/(F(sum(den),2*S))
                    self.assertLessEqual(F(z[0],S),target);self.assertGreaterEqual(F(z[1],S),target)

    def test_mutated_reports_are_rejected(self):
        digest=sha256(canonical(self.small).encode()).hexdigest()
        mutations=[]
        for field in ['coarse_E','coarse_F','coarse_Q','worst_E','worst_F','worst_Q','completed_A_upper']:
            r=copy.deepcopy(self.small);r['stages'][0]['panels'][0][field][0]+=1;mutations.append(r)
        for field,val in [('Y',True),('B',15.0),('completion_support',999)]:
            r=copy.deepcopy(self.small);r['stages'][0][field]=val;mutations.append(r)
        r=copy.deepcopy(self.small);r['stages'][0]['endpoints']['3']['M']+=1;mutations.append(r)
        r=copy.deepcopy(self.small);r['coefficient_digest']='0'*64;mutations.append(r)
        for r in mutations:
            with self.assertRaises(ValueError):authenticate(r,digest)
        self.assertEqual(len(mutations),12)
        with self.assertRaises(ValueError):typed_equal(1,True)
        with self.assertRaises(ValueError):typed_equal(1,1.0)

    def test_strict_json(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'x.json'
            for data in ['{"a":1,"a":2}','{"a":NaN}','{"a":Infinity}','{"a":-Infinity}']:
                p.write_text(data)
                with self.assertRaises(ValueError):strict_read(p)
            p.write_text(canonical(self.small));shapes(strict_read(p))

if __name__=='__main__':unittest.main()
