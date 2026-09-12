#!/usr/bin/env python3
"""Exact finite controls. Synthetic spectra are NOT zeta zeros."""
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import sys, unittest, json, hashlib
sys.path.insert(0,str(Path(__file__).resolve().parent))
import intervals as iv

def need(ok,msg):
    if not ok:raise ValueError(msg)

class C:
    def __init__(self,r=0,i=0):self.r=F(r);self.i=F(i)
    def __add__(self,z):
        z=cc(z);return C(self.r+z.r,self.i+z.i)
    __radd__=__add__
    def __neg__(self):return C(-self.r,-self.i)
    def __sub__(self,z):return self+-cc(z)
    def __rsub__(self,z):return cc(z)+-self
    def __mul__(self,z):
        z=cc(z);return C(self.r*z.r-self.i*z.i,self.r*z.i+self.i*z.r)
    __rmul__=__mul__
    def conj(self):return C(self.r,-self.i)
    def __truediv__(self,z):
        z=cc(z);d=z.r*z.r+z.i*z.i
        need(d!=0,'complex division zero');v=self*z.conj();return C(v.r/d,v.i/d)
    def __pow__(self,n):
        if n<0:return (C(1)/self)**(-n)
        z=C(1)
        for _ in range(n):z=z*self
        return z
    def __eq__(self,z):
        z=cc(z);return self.r==z.r and self.i==z.i

def cc(z):return z if isinstance(z,C) else C(z)
def pmul(a,b):
    c=[C(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=c[i+j]+x*y
    return c

def padd(a,b):
    return [(a[i] if i<len(a) else C(0))+(b[i] if i<len(b) else C(0)) for i in range(max(len(a),len(b)))]
def peval(a,x):
    z=C(0)
    for v in reversed(a):z=z*x+v
    return z

def inverse(A):
    n=len(A);B=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if B[k][j]);B[j],B[k]=B[k],B[j]
        q=B[j][j];B[j]=[x/q for x in B[j]]
        for i in range(n):
            if i!=j:
                a=B[i][j];B[i]=[x-a*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B]
def mv(A,v):return [sum((x*y for x,y in zip(row,v)),F(0)) for row in A]
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def dot(u,v):return sum((x*y for x,y in zip(u,v)),F(0))

def inertia(A):
    A=[[F(x) for x in row] for row in A];pos=neg=zero=0
    while A:
        n=len(A);j=next((j for j in range(n) if A[j][j]),None)
        if j is not None:
            order=[j]+[i for i in range(n) if i!=j];A=[[A[i][k] for k in order] for i in order]
            p=A[0][0];pos+=int(p>0);neg+=int(p<0)
            A=[[A[i][j]-A[i][0]*A[0][j]/p for j in range(1,n)] for i in range(1,n)]
        else:
            pair=next(((i,j) for i in range(n) for j in range(i+1,n) if A[i][j]),None)
            if pair is None:zero+=n;break
            i,j=pair;order=[i,j]+[k for k in range(n) if k not in pair];A=[[A[i][k] for k in order] for i in order]
            b=A[0][1];pos+=1;neg+=1
            A=[[A[i][j]-(A[i][0]*A[1][j]+A[i][1]*A[0][j])/b for j in range(2,n)] for i in range(2,n)]
    return pos,neg,zero

def spectral_controls():
    rows=[]
    # Every spectrum includes an ENTIRE infinite positive geometric tail.
    for pairs, complex_tail in [(q,b) for q in [1,2,3] for b in [False,True]]:
        selected=[C(F(1,3+j),F(1,5+j)) for j in range(pairs)]
        nodes=[C(1)]+[z for a in selected for z in [a,a.conj()]]
        mult=[1]+[m for j in range(pairs) for m in [j+2,j+2]]
        tail_a=F(1,64);tail_r=F(1,2)
        power=lambda n:sum((m*(z**n).r for z,m in zip(nodes,mult)),F(0))+tail_a**n/(1-tail_r**n)+(2*(C(F(1,128),F(1,128))**n).r/(1-tail_r**n) if complex_tail else 0)
        witnesses=[];ell=2
        for k,a in enumerate(selected):
            P=[C(0)]
            for z,b in [(a,C(0,1)/a),(a.conj(),C(0,-1)/a.conj())]:
                L=[C(1)]
                for v in nodes:
                    if v!=z:L=[c/(z-v) for c in pmul(L,[-v,C(1)])]
                L=[C(0)]*ell+[c*b/(z**ell) for c in L];P=padd(P,L)
            need(all(c.i==0 for c in P),'witness not real')
            for v in nodes:
                target=C(0,1)/a if v==a else (C(0,-1)/a.conj() if v==a.conj() else C(0))
                need(peval(P,v)==target,'wrong interpolation')
            witnesses.append([c.r for c in P])
        gram=[[sum((a*b*power(i+j+2) for i,a in enumerate(P) for j,b in enumerate(Q)),F(0))
               for Q in witnesses] for P in witnesses]
        need(inertia(gram)==(0,pairs,0),'complete-tail witness not negative')
        d=max(map(len,witnesses))-1
        H=[[power(i+j+2) for j in range(d+1)] for i in range(d+1)]
        need(inertia(H)[1]>=pairs,'selected pairs not detected')
        if not complex_tail:need(inertia(H)[1]==pairs,'distinct-pair inertia mismatch')
        rows.append({'selected_pairs':pairs,'infinite_complex_tail':complex_tail,'degree':d,'negative_index':inertia(H)[1]})
    # Multiplicity changes weights but not negative dimension.
    for multiplicity in [1,2,7]:
        z=C(F(1,3),F(1,4))
        q=lambda n:2*multiplicity*(z**n).r+F(1,64)**n/(1-F(1,2)**n)
        H=[[q(i+j+2) for j in range(4)] for i in range(4)]
        need(inertia(H)[1]==1,'multiplicity counted as distinct directions')
    return rows

def quadrature_controls():
    rows=[]
    for n in range(1,7):
        nodes=[F(j+1,n+3) for j in range(n+1)];weights=[F(j+2) for j in range(n+1)]
        moments=[sum(w*x**k for w,x in zip(weights,nodes)) for k in range(2*n)]
        G=[[moments[i+j] for j in range(n)] for i in range(n)]
        J=[[moments[i+j+1] for j in range(n)] for i in range(n)]
        need(inertia(G)==inertia(J)==(n,0,0),'positive finite Gram')
        A=mm(inverse(G),J);need(mm(G,A)==J,'compression identity')
        e=[F(int(j==0)) for j in range(n)];v=e[:]
        for k in range(2*n):
            need(dot(e,mv(G,v))==moments[k],'quadrature moment reproduction')
            v=mv(A,v)
        rows.append({'dimension':n,'moments_reproduced':2*n})
    return rows

def formal_controls():
    # Independent exponential-series composition versus differential recurrence.
    order=64;ps=iv.derivative_polynomials(order);reports=[]
    for q in [F(3),F(4),F(9)]:
        a=[F(0)]+[F(int(k==1),2)-q*F(2**k,factorial(k)) for k in range(1,order+1)]
        b=[F(1)]
        for k in range(1,order+1):b.append(sum(j*a[j]*b[k-j] for j in range(1,k+1))/k)
        p=[4*q*q*F(4**k,factorial(k))-6*q*F(2**k,factorial(k)) for k in range(order+1)]
        for k in range(order+1):
            value=factorial(k)*sum(p[j]*b[k-j] for j in range(k+1))
            need(value==sum(c*q**j for j,c in ps[k].items()),'theta derivative composition')
        reports.append({'q':str(q),'orders':order+1})
    # Log/Newton formula against independent finite spectral polynomials.
    for roots in [[C(1),C(F(1,2))],[C(F(1,3),F(1,4)),C(F(1,3),F(-1,4))],
                  [C(1),C(1),C(F(2,3),F(1,5)),C(F(2,3),F(-1,5))]]:
        p=[C(1)]
        for r in roots:p=pmul(p,[1,-r])
        need(all(x.i==0 for x in p),'real divisor polynomial')
        e=[x.r*(-1)**k for k,x in enumerate(p)];qs=[]
        for n in range(1,len(e)):
            qn=(-1)**(n+1)*(n*e[n]-sum((-1)**(k+1)*qs[k-1]*e[n-k] for k in range(1,n)))
            need(qn==sum((r**n).r for r in roots),'Newton sign or multiplicity')
            qs.append(qn)
    return reports

def elementary_controls():
    need(sum(F(6**j,factorial(j)) for j in range(16))>F(1000,3),'exp6 tail threshold')
    need(sum(F(1,factorial(j)) for j in range(5))>F(8,3),'exp lower base')
    need(sum(F(1,factorial(j)) for j in range(5))+F(1,120)*F(6,5)<F(11,4),'exp upper')
    need(F(11,4)**3<25,'exp3/2 upper')
    need(243**2+2*243+2==59537,'index polynomial')
    need(1000**2+2000+2==1002002,'physical polynomial')
    need(sum(F(3,4)**j/F(factorial(j)) for j in range(4))>2,'Gaussian source envelope')
    need(F(10,20**2)+F(2,20)==F(1,8),'complete divisor square-sum ceiling')
    need(F(256)*F(9,5)/F(9,20)==1024,'Gaussian moment envelope normalization')
    for k in range(66):need(k<400<2048,'monomial monotonicity cutoff')
    # Cell coverage and integral Taylor coefficients.
    cells=128;h=F(3,2*cells)
    need(sum(2*h for _ in range(cells))==3,'complete cell coverage')
    for k in range(64):
        integ=(h**(k+1)-(-h)**(k+1))/F(k+1)
        need(integ/factorial(k)==(2*h**(k+1)/factorial(k+1) if k%2==0 else 0),'Taylor-cell integral')
    # Independent short-series intervals overlap the high-precision primitives.
    for x in [F(-1),F(-1,8),F(0),F(1,8),F(1)]:
        approx=sum(x**k/F(factorial(k)) for k in range(31));rem=F(3,factorial(31))
        I=iv.exp(iv.I.point(x))
        need(F(I.lo,iv.S)>=approx-rem and F(I.hi,iv.S)<=approx+rem,'exp enclosure')
    return {'tail_constants':9,'cell_monomials':64,'exp_controls':5}

def reconstruct():
    ans={'synthetic_infinite_tail_indices':spectral_controls(),'positive_atomic_quadratures':quadrature_controls(),
         'source_derivative_series':formal_controls(),'elementary_controls':elementary_controls(),
         'rh_proved':False,'synthetic_nodes_are_zeta_zeros':False}
    data=json.dumps(ans,sort_keys=True,separators=(',',':')).encode()
    return ans,hashlib.sha256(data).hexdigest()

class Tests(unittest.TestCase):
    def test_spectral_index(self):spectral_controls()
    def test_quadrature(self):quadrature_controls()
    def test_formal_source(self):formal_controls()
    def test_elementary(self):elementary_controls()

if __name__=='__main__':
    if '--emit' in sys.argv:
        result,digest=reconstruct();print(json.dumps({'controls':result,'sha256':digest},indent=2,sort_keys=True))
    else:
        unittest.main()
