"""Independent finite rational controls, not an all-order source proof."""
from fractions import Fraction as F
from itertools import product
from math import factorial, comb
import copy
import json
from pathlib import Path
import unittest

import certify_graft as c

def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def exact_power_polynomial(xs):
    p=[F(1)]
    for x in xs: p=poly_mul(p,[-x,F(1)])
    return p

def solve(matrix,rhs):
    a=[list(row)+[v] for row,v in zip(matrix,rhs)]
    n=len(a)
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j])
        a[j],a[k]=a[k],a[j]
        pivot=a[j][j];a[j]=[v/pivot for v in a[j]]
        for k in range(n):
            if k!=j:
                v=a[k][j];a[k]=[u-v*w for u,w in zip(a[k],a[j])]
    return [row[-1] for row in a]

def moments_and_derivatives(a,b,q,tau,order):
    # Complete DIRECT eight-configuration sum, independent of formal quotient.
    m=[];dm=[]
    for n in range(order+1):
        total=change=F(0)
        for s,t,e in product([-1,1],repeat=3):
            base=F(1,4)/(1+q)*(1 if s==t else q)
            value=(a*F(s+t,2)+b*e)**n
            total+=base*(1+tau*s*e)*value
            change+=base*s*e*value
        m.append(total);dm.append(change)
    return m,dm

def cumulant_derivative(m,dm):
    k=c.cumulants(m)
    dk=[F(0)]*len(m)
    for n in range(1,len(m)):
        dk[n]=dm[n]-sum(comb(n-1,j-1)*(dk[j]*m[n-j]+k[j]*dm[n-j]) for j in range(1,n))
    return dk

class GraftTests(unittest.TestCase):
    def test_full_graph_merger_and_series_derivative(self):
        for a,b,q in [(F(1,3),F(2,5),F(2,3)),(F(2,7),F(3,8),F(1,4)),(F(4,9),F(1,2),F(1))]:
            u=c.sinh_quotient(q,8);t=c.sinh_quotient(F(0),8)
            m,dm=moments_and_derivatives(a,b,q,F(0),16)
            derivative=cumulant_derivative(m,dm)
            for r in range(1,9):
                expected=factorial(2*r)*a*b*sum(u[k]*t[r-1-k]*a**(2*k)*b**(2*(r-1-k)) for k in range(r))
                self.assertEqual(derivative[2*r],expected)
            for tau in [F(0),F(1,7),F(4,5)]:
                mt,_=moments_and_derivatives(a,b,q,tau,16)
                for n in range(17): self.assertEqual(mt[n],m[n]+tau*dm[n])
                self.assertEqual(mt[0],1)

    def test_annihilator_matches_full_linear_solve(self):
        csign=c.cumulants([F(k%2==0) for k in range(17)])
        dimer=c.cumulants([F(1)]+[F(3,5) if k%2==0 else F(0) for k in range(1,17)])
        ar=[None]+[dimer[2*r]/csign[2*r] for r in range(1,9)]
        for n in range(1,7):
            xs=[F(j+1,j+5)**2 for j in range(n)]; y=F(2,3)**2
            nu=[j+1 for j in range(n)]
            P=exact_power_polynomial(xs)
            ell=sum(P[k]*ar[k+1]*y**k for k in range(n+1))
            self.assertNotEqual(ell,0)
            z=sum(P[k]*ar[k+2]*y**(k+1) for k in range(n+1))/ell
            Q=[(n+2)*v for v in poly_mul(P,[-z,F(1)])]
            lam=[-Q[r-1]/r for r in range(1,n+2)]
            J=[[r*nu[j]*xs[j]**(r-1) for j in range(n)]+[r*ar[r]*y**(r-1)] for r in range(1,n+2)]
            last=[(n+2)*nu[j]*xs[j]**(n+1) for j in range(n)]+[(n+2)*ar[n+2]*y**(n+1)]
            for j in range(n+1): self.assertEqual(sum(lam[i]*J[i][j] for i in range(n+1)),last[j])
            rhs=[F((i+1)**3,17) for i in range(n+1)]
            answer=solve(J,rhs)
            self.assertEqual(sum(lam[i]*rhs[i] for i in range(n+1)),sum(last[j]*answer[j] for j in range(n+1)))

    def test_directed_arithmetic_and_actual_box(self):
        for a,b in [(F(-7,9),F(4,7)),(F(1,10),F(9,11)),(F(-2),F(-3,4))]:
            for result,truth in [(c.I(a)+c.I(b),a+b),(c.I(a)*c.I(b),a*b),(c.I(a)/c.I(b),a/b)]:
                self.assertLessEqual(F(result.lo,c.DEN),truth)
                self.assertGreaterEqual(F(result.hi,c.DEN),truth)
        for x in [F(1,7),F(4,9),F(17,13)]:
            root=c.I(x).sqrt()
            self.assertLessEqual(F(root.lo,c.DEN)**2,x)
            self.assertGreaterEqual(F(root.hi,c.DEN)**2,x)
        data=json.loads(Path(__file__).with_name('seed-box.json').read_text())
        c.validate_seed(data);c.validate(c.evaluate_box(data))
        bad=copy.deepcopy(data);bad['q']=[1,2]
        with self.assertRaises(ValueError): c.validate_seed(bad)
        bad=c.evaluate_box(data);bad['rows'][0]['standardized_moment16_slope']=[0,0]
        with self.assertRaises(ArithmeticError):c.validate(bad)

if __name__=='__main__':unittest.main()
