"""Exact small-graph controls and numerical derivative checks, not a theta certificate."""
import itertools,math,json,unittest
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from models import MomentModel
ROOT=Path(__file__).resolve().parent
AN=list(map(float,json.loads((ROOT/'target.json').read_text())['an']))

def exact_law(weights,edges):
    out=[]
    for s in itertools.product((-1,1),repeat=len(weights)):
        w=math.prod((1+q*s[i]*s[j]) for i,j,q in edges)
        y=sum(a*v for a,v in zip(weights,s))
        out.append((s,w,y))
    Z=sum(w for _,w,_ in out)
    return [(s,w/Z,y) for s,w,y in out]

def gaussian_moment(y,var,r):
    return sum(F(math.comb(r,2*j)*math.factorial(2*j),2**j*math.factorial(j))
               *var**j*y**(r-2*j) for j in range(r//2+1))

class TestModels(unittest.TestCase):
    def test_group_compression_exact(self):
        a,b=F(1,5),F(2,7);q0,q1,q2=F(1,7),F(1,9),F(1,11)
        law=exact_law([a,a,b,b],[(0,1,q0),(2,3,q1)]+[(i,j,q2) for i in (0,1) for j in (2,3)])
        compressed=[]
        for u,v in itertools.product(range(3),repeat=2):
            m,n=2*u-2,2*v-2
            # Exactly count aligned and opposed pairs in each block.
            e0=math.comb(u,2)+math.comb(2-u,2);e1=math.comb(v,2)+math.comb(2-v,2)
            cross=u*v+(2-u)*(2-v)
            w=(math.comb(2,u)*math.comb(2,v)*(1+q0)**e0*(1-q0)**(1-e0)
               *(1+q1)**e1*(1-q1)**(1-e1)*(1+q2)**cross*(1-q2)**(4-cross))
            compressed.append((w,a*m+b*n))
        Z=sum(w for w,_ in compressed)
        for r in range(21):
            self.assertEqual(sum(w*y**r for _,w,y in law),sum(w*y**r for w,y in compressed)/Z)

    def test_full_dense_and_gaussian(self):
        weights=[F(1,5),F(1,4),F(1,3)];qs=[F(1,7),F(1,9),F(1,11)]
        edges=[(i,j,q) for (i,j),q in zip(itertools.combinations(range(3),2),qs)]
        law=exact_law(weights,edges);sd=F(1,4)
        expected=[float(sum(w*gaussian_moment(y,sd*sd,r) for _,w,y in law)) for r in range(21)]
        model=MomentModel([1]*3,AN,gaussian=True)
        z=np.r_[list(map(float,weights)),float(sd),np.arctanh(list(map(float,qs)))]
        np.testing.assert_allclose(model.raw_moments(z),expected,rtol=1e-10,atol=1e-10)

    def test_hidden_spin_sum(self):
        weights=[F(1,5),F(1,4),F(1,3),F(0),F(0)]
        qs=[F(1,k) for k in range(7,13)]
        edges=[(i,3+h,qs[3*h+i]) for h in range(2) for i in range(3)]
        law=exact_law(weights,edges)
        expected=[float(sum(w*y**r for _,w,y in law)) for r in range(21)]
        model=MomentModel([1]*3,AN,gaussian=False,hidden=2,pair_edges=False)
        z=np.r_[list(map(float,weights[:3])),np.arctanh(list(map(float,qs)))]
        np.testing.assert_allclose(model.raw_moments(z),expected,rtol=1e-10,atol=1e-12)

    def test_covariance_derivative_exact(self):
        weights=[F(1,3),F(1,5),F(1,7)];q=F(1,4);r=F(1,6)
        data=[]
        for s in itertools.product((-1,1),repeat=3):
            w=(1+q*s[0]*s[1])*(1+r*s[1]*s[2]);dw=s[0]*s[1]*(1+r*s[1]*s[2])
            y=sum(a*t for a,t in zip(weights,s));data.append((w,dw,y,s[0]*s[1]))
        Z=sum(v[0] for v in data);dZ=sum(v[1] for v in data)
        for k in range(21):
            ex=sum(w*y**k for w,_,y,_ in data)/Z
            derivative=sum(dw*y**k for _,dw,y,_ in data)/Z-ex*dZ/Z
            cov=sum(w*y**k*b for w,_,y,b in data)/Z-ex*sum(w*b for w,_,_,b in data)/Z
            self.assertEqual(derivative,cov/(1-q*q))

    def test_numerical_full_jacobian(self):
        model=MomentModel([1]*3,AN,gaussian=True,hidden=1)
        z=np.r_[.2,.3,.4,.35,.04,.08,.06,.1,.15,.2]
        f,j=model.evaluate(z);h=1e-6
        num=np.column_stack([(model.evaluate(z+h*np.eye(len(z))[i])[0]-
                              model.evaluate(z-h*np.eye(len(z))[i])[0])/(2*h) for i in range(len(z))])
        np.testing.assert_allclose(j,num,rtol=1e-5,atol=2e-8)

    def test_reject_negative_coupling(self):
        model=MomentModel([1]*2,AN,gaussian=False)
        self.assertFalse(model.admissibility(np.array([.2,.3,-.1]))['passes_parameter_sign_conditions'])

    def test_reject_negative_weight(self):
        model=MomentModel([1]*2,AN,gaussian=False)
        self.assertFalse(model.admissibility(np.array([-.2,.3,.1]))['passes_parameter_sign_conditions'])

    def test_no_automatic_certificate(self):
        model=MomentModel([1]*2,AN,gaussian=False)
        self.assertFalse(model.admissibility(np.array([.2,.3,.1]))['root_certified'])

    def test_input_guards(self):
        with self.assertRaises(ValueError):MomentModel([1,0],AN,gaussian=False)
        with self.assertRaises(ValueError):MomentModel([2],AN,gaussian=False,hidden=1)
        m=MomentModel([1]*2,AN,gaussian=False)
        with self.assertRaises(ValueError):m.evaluate(np.array([1.,2.]))
        with self.assertRaises(ValueError):m.evaluate(np.array([1.,2.,np.nan]))

if __name__=='__main__':unittest.main()
