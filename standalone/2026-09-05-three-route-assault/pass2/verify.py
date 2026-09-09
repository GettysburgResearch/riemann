"""Fresh exact finite checks for all three routes. No analytic theorem is inferred
from a finite test. The actual-xi interval certificate is separately proof-bound.
Python standard library only; all acceptance failures survive python -O.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import json
import unittest
from source_certificate import Ball, certify, log_rational

@dataclass(frozen=True)
class Q:
    re:F=F(0)
    im:F=F(0)
    def __post_init__(self):
        object.__setattr__(self,'re',F(self.re)); object.__setattr__(self,'im',F(self.im))
    @staticmethod
    def of(x): return x if isinstance(x,Q) else Q(F(x))
    def __add__(self,x):
        x=self.of(x);return Q(self.re+x.re,self.im+x.im)
    __radd__=__add__
    def __neg__(self): return Q(-self.re,-self.im)
    def __sub__(self,x):return self+-self.of(x)
    def __rsub__(self,x):return self.of(x)+-self
    def __mul__(self,x):
        x=self.of(x);return Q(self.re*x.re-self.im*x.im,self.re*x.im+self.im*x.re)
    __rmul__=__mul__
    def conj(self):return Q(self.re,-self.im)
    def norm2(self):return self.re*self.re+self.im*self.im
    def __truediv__(self,x):
        x=self.of(x); d=x.norm2()
        if not d:raise ZeroDivisionError('Gaussian rational zero')
        z=self*x.conj();return Q(z.re/d,z.im/d)
    def __rtruediv__(self,x):return self.of(x)/self
    def __pow__(self,n):
        if type(n)is not int or n<0:raise ValueError('integer power')
        v=Q(1)
        for _ in range(n):v=v*self
        return v
    def __bool__(self):return bool(self.re or self.im)
I=Q(0,1)

def prod(xs):
    v=Q(1)
    for x in xs:v=v*x
    return v

def adj(A):return [[A[i][j].conj() for i in range(len(A))] for j in range(len(A[0]))]
def mul(A,B):
    if not A or not B or len(A[0])!=len(B):raise ValueError('matrix shape')
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q()) for j in range(len(B[0]))] for i in range(len(A))]
def sub(A,B):return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
def inv(A):
    n=len(A)
    if not n or any(len(r)!=n for r in A):raise ValueError('square nonempty required')
    B=[row[:]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        p=next((j for j in range(i,n) if B[j][i]),None)
        if p is None:raise ValueError('singular matrix')
        B[i],B[p]=B[p],B[i];v=B[i][i];B[i]=[x/v for x in B[i]]
        for j in range(n):
            if j!=i:
                v=B[j][i];B[j]=[x-v*y for x,y in zip(B[j],B[i])]
    return [row[n:] for row in B]
def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def elementary(xs):
    out=[F(1)]
    for x in xs:
        out.append(F(0))
        for k in range(len(out)-1,0,-1):out[k]+=x*out[k-1]
    return out

def mobius(n):
    sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    return -sign if n>1 else sign

class Check:
    def __init__(self):self.counts={}
    def __call__(self,group,ok):
        if not ok:raise ArithmeticError('failed exact control: '+group)
        self.counts[group]=self.counts.get(group,0)+1

def run():
    ck=Check(); cert=certify()
    for value in cert['checks'].values():ck('actual_xi_strict_interval_signs',value)
    for n in range(1,13):
        xs=[F(k+1,10*(n+1)) for k in range(n)]
        es=elementary(xs);C=sum(xs);p2=sum(x*x for x in xs);p3=sum(x**3 for x in xs)
        for k,v in enumerate(es):ck('positive_coefficient_bound',v<=C**k/F(factorial(k)))
        if n>=2:ck('newton_identity',C*C-2*es[2]==p2)
        if n>=3:ck('newton_identity',C**3-3*C*es[2]+3*es[3]==p3)
        if n>=2:
            e=elementary([F(1,n)]*n)
            ck('trace_escape',e[1]==1 and e[2]==F(n-1,2*n))
    for r in range(2,12):
        x=F(1,100);y=F(r+1,100);C=(r-1)*x+y;p=(r-1)*x*x+y*y
        ck('two_moment_completion',(r*p-C*C)/(r-1)==(y-x)**2)
        ck('sharp_cubic_bound',(r-1)*x**3+y**3==(y+2*x)*p-(x*x+2*x*y)*C+r*x*x*y)
    # Generic finite-prefix energy: integrate in exp(-2 sigma x) coordinates.
    for n in range(2,9):
        heights=[F(n+2-j,n+2) for j in range(n)]+[F(1,2*(n+2))]
        sigma=F(2,3);coeff=[Q(F((-1)**j,j+1),F(1,j+2)) for j in range(n)]
        prefix=Q();left=F(0)
        for j in range(n):
            prefix+=coeff[j];left+=(heights[j]-heights[j+1])*prefix.norm2()/(2*sigma)
        right=sum((coeff[i]*coeff[j].conj()*(min(heights[i],heights[j])-heights[-1])/(2*sigma)
                   for i in range(n) for j in range(n)),Q())
        ck('causal_cutoff_kernel',right==Q(left))
    for q in (3,67):
        for n in range(1,129):
            value=0;power=1;j=0
            while n%power==0:
                k=n//power
                value+=(-1)**j*sum(mobius(d) for d in range(1,k+1) if k%(d*d)==0)
                if power>n//q:break
                power*=q;j+=1
            ck('q_free_diagonal_euler_factor',value==mobius(n)**2*int(n%q!=0))
    am=F(1)
    for m in range(1,13):
        ck('pole_multiplicity_constant',am==F(comb(2*m-2,m-1),4**(m-1)))
        am*=F(2*m-1,2*m)
    # Finite Cauchy screening, with actual complex phases retained.
    for a in (F(1),F(3,2)):
      for b in (F(1),F(2)):
       for center in (F(0),F(3,2)):
        for y in (F(1,4),F(1,3)):
         target=[Q(center,y),Q(center,-y)]
         background=[Q(-2),Q(0),Q(4),Q(5,F(1,5)),Q(5,F(-1,5))]
         p=lambda z:Q(a)+I*z.conj()
         s=lambda z:1/(Q(b)-I*z)
         gram=lambda z,w:s(z).conj()*s(w)*2*a/(p(z)+p(w).conj())
         BG=[[gram(z,w) for w in background] for z in background]
         cross=[[gram(z,w) for w in background] for z in target]
         G0=[[gram(z,w) for w in target] for z in target]
         G=sub(G0,mul(mul(cross,inv(BG)),adj(cross)))
         blas=lambda u:prod((u-p(z))/(u+p(z).conj()) for z in background)
         H=[[gram(z,w)*blas(p(z))*blas(p(w)).conj() for w in target] for z in target]
         ck('cauchy_schur_vs_blaschke',G==H)
         exactdet=(s(target[0])*s(target[1])*blas(p(target[0]))*blas(p(target[1]))).norm2()*y*y/(a*a-y*y)
         ck('isolated_pair_determinant',det2(G)==Q(exactdet) and exactdet>0)
         ck('residual_hermitian',G==adj(G))
         v=[[Q(1)],[Q(-1)]];w=mul(inv(G),v)
         norm=mul(mul(adj(v),inv(G)),v)[0][0]
         ck('witness_positive_norm',norm.im==0 and norm.re>0)
         for mass in (1,2,3):
            J=[[Q(),Q(mass)],[Q(mass),Q()]]
            val=mul(mul(mul(mul(adj(w),G),J),G),w)[0][0]
            ck('negative_witness',val==Q(-2*mass))
         # Safe-source transform, all +/- and conjugate locations, finite model.
         zs=target+[-z for z in target]+[Q(3),Q(-3)]
         L=lambda r:sum((Q(r)/(Q(r*r)+z*z) for z in zs),Q())
         for r in (F(3),F(4)):
            lhs=sum((Q(r)/((Q(r*r)+z*z)*(Q(b*b)+z*z)) for z in zs),Q())
            rhs=(L(r)-F(r,b)*L(b))/(b*b-r*r)
            ck('safe_source_factor_and_sign',lhs==rhs)
         Lprime=sum(((z*z-Q(b*b))/(Q(b*b)+z*z)**2 for z in zs),Q())
         atb=-(Lprime-L(b)/b)/(2*b)
         ck('safe_source_removable_diagonal',atb==sum((Q(b)/(Q(b*b)+z*z)**2 for z in zs),Q()))
    for a in (F(1),F(2)):
      for yy in (F(1,4),F(-1,4)):
       pp=Q(a+yy,F(3,2))
       for height in (20,40,80,160):
        rr=Q(a+F(1,3),height)
        loss=4*pp.re*rr.re/(pp+rr.conj()).norm2()
        ck('blaschke_tail_exact_identity',((pp-rr)/(pp+rr.conj())).norm2()==1-loss)
        ck('blaschke_tail_bound',0<=loss<=F(1,2) and loss<=16*pp.re*(a+F(1,2))/height**2)
        logarithm=-log_rational(1-loss)
        ck('blaschke_tail_log_bound',logarithm.hi<=2*loss)
    return {'status':'PASS_THREE_ROUTES_PASS2','counts':ck.counts,
      'total_finite_controls':sum(ck.counts.values()),
      'actual_xi_certificate_status':cert['status'],
      'analytic_proofs_machine_checked':False,'RH_proved':False,
      'arithmetic':['EXACT_RATIONAL','EXACT_GAUSSIAN_RATIONAL','RATIONAL_INTERVAL']}

class UnitTests(unittest.TestCase):
    def test_gaussian_inverse(self):self.assertEqual((Q(2,3)/Q(4,-1))*Q(4,-1),Q(2,3))
    def test_gaussian_zero(self):
        with self.assertRaises(ZeroDivisionError):1/Q()
    def test_matrix_inverse(self):
        A=[[Q(2),Q(0,1)],[Q(0,-1),Q(3)]]
        self.assertEqual(mul(A,inv(A)),[[Q(1),Q()],[Q(),Q(1)]])
    def test_singular_rejected(self):
        with self.assertRaises(ValueError):inv([[Q(1),Q(1)],[Q(1),Q(1)]])
    def test_interval_order(self):
        with self.assertRaises(ValueError):Ball(2,1)
    def test_interval_division(self):
        with self.assertRaises(ValueError):Ball(1)/Ball(-1,1)
    def test_negative_sqrt(self):
        with self.assertRaises(ValueError):Ball(-1).sqrt()
    def test_log_domain(self):
        with self.assertRaises(ValueError):log_rational(F(0))
    def test_log_additivity(self):
        a=log_rational(F(6));b=log_rational(F(2))+log_rational(F(3))
        self.assertLessEqual(max(a.lo,b.lo),min(a.hi,b.hi))
    def test_sqrt_enclosure(self):
        a=Ball(2).sqrt();self.assertLessEqual(a.lo*a.lo,F(2));self.assertGreaterEqual(a.hi*a.hi,F(2))
    def test_escape(self):self.assertEqual(elementary([F(1,4)]*4)[2],F(3,8))
    def test_mobius(self):self.assertEqual([mobius(n) for n in range(1,11)],[1,-1,-1,0,-1,1,-1,0,0,1])
    def test_every_control(self):self.assertEqual(run()['status'],'PASS_THREE_ROUTES_PASS2')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--tests',action='store_true');args=p.parse_args()
    if args.tests:unittest.main(argv=['verify.py'],verbosity=2)
    else:
        out=run();text=json.dumps(out,indent=2,sort_keys=True)+'\n';path=Path(__file__).with_name('RESULTS.json')
        if args.write:path.write_text(text)
        elif path.read_text()!=text:raise SystemExit('stored finite results mismatch')
        print(out['status']);print('finite controls:',out['total_finite_controls']);print('ANALYTIC_REVIEW_REQUIRED; RH_UNPROVED')
