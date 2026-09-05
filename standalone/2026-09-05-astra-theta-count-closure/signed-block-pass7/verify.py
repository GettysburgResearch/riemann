#!/usr/bin/env python3
"""Finite exact controls only. No actual prime sum or all-rank sign computation."""
from fractions import Fraction as F
from math import comb
from collections import Counter
from pathlib import Path
from dataclasses import dataclass
import argparse
import hashlib
import json

COUNTS = Counter()


def need(ok, group):
    if not ok:
        raise ArithmeticError('failed: '+group)
    COUNTS[group] += 1


@dataclass(frozen=True)
class C:
    r: F = F(0)
    i: F = F(0)
    def __add__(self, b):
        b = b if isinstance(b, C) else C(F(b))
        return C(self.r+b.r, self.i+b.i)
    __radd__ = __add__
    def __neg__(self): return C(-self.r, -self.i)
    def __sub__(self, b): return self+-coerce(b)
    def __rsub__(self, b): return coerce(b)+-self
    def __mul__(self, b):
        b = coerce(b)
        return C(self.r*b.r-self.i*b.i, self.r*b.i+self.i*b.r)
    __rmul__ = __mul__
    def __truediv__(self, b):
        b = coerce(b); q = b.r*b.r+b.i*b.i
        if not q: raise ZeroDivisionError
        return self*C(b.r/q, -b.i/q)
    def __rtruediv__(self, b): return coerce(b)/self
    def __pow__(self, n):
        if n < 0: return (C(F(1))/self)**(-n)
        v, a = C(F(1)), self
        while n:
            if n & 1: v = v*a
            a, n = a*a, n//2
        return v
    def norm2(self): return self.r*self.r+self.i*self.i
    def conj(self): return C(self.r, -self.i)


def coerce(x): return x if isinstance(x, C) else C(F(x))


def peval(coeff, z):
    v = coerce(0) if isinstance(z, C) else F(0)
    for a in reversed(coeff): v = v*z+a
    return v


def rising(x, n):
    v = F(1)
    for j in range(n): v *= x+j
    return v


def moment(m, n): return rising(F(1,2), n)/rising(2*m, n)


def beta_poly(m, coeff):
    return sum((a*b*moment(m,i+j) for i,a in enumerate(coeff)
                for j,b in enumerate(coeff)), F(0))


def pd(mat):
    a = [list(r) for r in mat]
    for j in range(len(a)):
        v = a[j][j]
        if v <= 0: return False
        for r in range(j+1,len(a)):
            for s in range(j+1,len(a)):
                a[r][s] -= a[r][j]*a[j][s]/v
    return True


def det3(a):
    a = [[coerce(x) for x in row] for row in a]
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def schur3(v,w,x,y,z):
    return sum((z**(v+w-3-r-s)*(x*y)**s*
                sum((x**(r-s-k)*y**k for k in range(r-s+1)), C())
                for r in range(v-1,w-1) for s in range(v)), C())


def strict_load(path):
    def pairs(items):
        d = {}
        for k,v in items:
            if k in d: raise ValueError('duplicate JSON key')
            d[k]=v
        return d
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs)


def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)


def compute():
    COUNTS.clear()
    base = 6*F(11,10)**4*F(678**4*10000**3,196**2*141**4)
    theta5=base*F(678,10000)**10
    need(theta5<F(1,3),'three_zero_reservoir_constant')
    for M in range(5,25):
        need(base*F(678,10000)**(2*(M+1)) ==
             base*F(678,10000)**(2*M)*F(678,10000)**2,
             'reservoir_ratio_identity')
    # Exact Jacobi-weight moment matrices. These are finite controls of
    # the analytic all-parameter energy argument, not substitutes for it.
    for D in range(1,7):
        for m in (256*D,300*D):
            beta=F(4*m-3,2)
            G=[[moment(m,i+j) for j in range(D+1)] for i in range(D+1)]
            Y=[[F(5,4)*rising(F(1,2),i+j+1)/
                (beta*rising(2*m,i+j)) for j in range(D+1)] for i in range(D+1)]
            need(pd(G),'beta_gram_pd')
            need(pd([[F(12*D,m)*G[i][j]-Y[i][j] for j in range(D+1)]
                     for i in range(D+1)]),'full_signed_variance_matrix')
            # Jacobi integration-by-parts symmetry on each monomial pair.
            for i in range(D+1):
                for j in range(D+1):
                    energy=F(0) if i*j==0 else i*j*(moment(m,i+j-1)-moment(m,i+j))
                    rhs=j*(j+beta+F(1,2))*moment(m,i+j)
                    if j: rhs-=j*(j-F(1,2))*moment(m,i+j-1)
                    need(energy==rhs,'jacobi_energy_identity')
            alpha=2*m-2
            need(F(4,alpha)+F(8*D,alpha**2)<F(3,m),'original_metric_escape_constant')
    # Rational source formula and endpoint-zero change of basis.
    for D in range(1,6):
        for A in (C(F(1)),C(F(3),F(1)),C(F(200),F(10))):
            t=(A-F(1,4))/(A+1)
            need(t.norm2()<1,'invariant_disk_geometry')
            for j in range(D):
                m=256*D
                lhs=(F(5,4)/(A+1))**m*(t+F(1,4))*(1-t)**j
                rhs=F(5,4)**(m+j+1)*A/(A+1)**(m+j+1)
                need(lhs==rhs,'signed_block_transform')
    # Finite Lagrange reconstruction with unrestricted signed coefficients.
    nodes=[F(1,201),F(1,451),F(1,651)]
    polys=[[F(1),F(-2),F(3)], [F(-7),F(11),F(-5)], [F(0),F(1),F(-1)]]
    for z in (C(F(1,10001)),C(F(1,20001),F(1,40001)),C(F(-1,20000))):
        ls=[]
        for i,zi in enumerate(nodes):
            l=C(F(1))
            for j,zj in enumerate(nodes):
                if i!=j: l=l*(z-zj)/(zi-zj)
            ls.append(l)
            need(l.norm2() < (F(11,10)**2*F(678**2,141**2))**2,
                 'lagrange_tail_envelope')
        for P in polys:
            need(peval(P,z)==sum((peval(P,nodes[i])*ls[i] for i in range(3)),C()),
                 'signed_lagrange_reconstruction')
    # Exponent-gap-independent generalized cardinal bound.
    for v,w in [(1,2),(1,4),(2,5),(4,7),(1,100),(17,100)]:
        matrix=[[coerce(z)**e for e in (0,v,w)] for z in nodes]
        den=det3(matrix)
        need(den.norm2()>0,'generalized_vandermonde_invertible')
        for z in [C(F(1,20000)),C(F(1,30000),F(1,40000))]:
            ls=[]
            for i in range(3):
                mat=[list(row) for row in matrix]
                mat[i]=[z**e for e in (0,v,w)]
                li=det3(mat)/den;ls.append(li)
                need(li.norm2() < (F(11,10)**2*F(678**2,141**2))**2,
                     'all_gap_cardinal_bound')
            coeff=[F(-7),F(11),F(-5)]
            actual=sum((b*z**e for b,e in zip(coeff,(0,v,w))),C())
            recon=sum((ls[i]*sum((b*nodes[i]**e for b,e in zip(coeff,(0,v,w))),F(0))
                       for i in range(3)),C())
            need(actual==recon,'all_gap_signed_interpolation')
        if w<=7:
            x,y,z=C(F(2)),C(F(3)),C(F(1,2),F(1,3))
            need(det3([[a**e for e in (0,v,w)] for a in (x,y,z)]) ==
                 (y-x)*(z-x)*(z-y)*schur3(v,w,x,y,z),
                 'explicit_positive_schur_factor')
    # Source-budget-compatible countermodel, with a negative signed block
    # at arbitrarily shifted orders. Coefficients are exact, not fitted.
    a=C(F(100)); b=C(F(200),F(10)); one=C(F(1)); ii=C(F(0),F(1))
    need(F(1,100)+F(2,200)==F(1,50),'countermodel_budget')
    need(b.i*b.i<=b.r,'countermodel_parabolic_strip')
    witnesses=[]
    for M in (2,5,20,769):
        W=ii*(b+1)**(M+2)/(b*(b-a))
        u=W.i/10; v=W.r-200*u
        def R(z): return z*(z-a)*(u*z+v)/(z+1)**(M+2)
        need(R(a)==C() and R(b)==ii and R(b.conj())==-ii,
             'countermodel_exact_interpolation')
        Q=R(a)**2+R(b)**2+R(b.conj())**2
        need(Q==C(F(-2)),'countermodel_full_form_negative')
        witnesses.append({'M':M,'quadratic_value':-2,
                          'coefficient_digest':hashlib.sha256((str(u)+';'+str(v)).encode()).hexdigest()})
    for D in range(1,11):
        need((D+1)<=2**D,'evaluation_envelope_constant')
    need(F(8,5)**5>9 and F(8,3)**5>100 and F(8,3)**2>7,
         'logarithm_certificates')
    need(F(1,8)+F(17,200)-F(4,5)==-F(59,100),'evaluation_exponent')
    need(F(204,256)<1 and F(12,256)<1,'archimedean_variance_budget')
    need(F(256,255)*2+F(256,255)**2/F(128)<3,'escape_endpoint')
    return {'status':'PASS_FINITE_SIGNED_BLOCK_CONTROLS',
            'arithmetic':'EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL',
            'rh_proved':False,'analytic_proofs_machine_checked':False,
            'actual_prime_sums_computed':False,
            'controls':sum(COUNTS.values()),'categories':dict(sorted(COUNTS.items())),
            'theta5':str(theta5),'theta5_upper':'1/3',
            'synthetic_witnesses':witnesses}


def main():
    p=argparse.ArgumentParser();p.add_argument('--check',type=Path)
    args=p.parse_args(); r=compute()
    if args.check and canonical(strict_load(args.check))!=canonical(r):
        raise ArithmeticError('saved result differs in value or numeric type')
    print(json.dumps(r,indent=2,sort_keys=True))


if __name__=='__main__': main()
