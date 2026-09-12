#!/usr/bin/env python3
"""RGT26: bounded exact checks, not an RH/analytic-proof verifier.

No author module, network, zero table, floating arithmetic, or special-function
oracle is used. --check authenticates this packet then reconstructs the receipt.
--emit is a producer; it does not authenticate a pre-existing expected result.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json
from math import comb, factorial, isqrt
from pathlib import Path
import sys

# Imported CG4 lower margin, not a fresh Fourier-integral primitive.
PARENT_MARGIN = Q('1963816046413587375735998000747928327019770581189416995995754155796255642214238632285580922950473968192889118936307817613777186424685567953056921578976916517233337031/4910085911844212805019784545241398728324963069064597184224937052144200694607011832324905138488856235726330026191340106513825884818828089579992791384064000000000000000000000000000000000000')

BITS = 320
UNIT = 1 << BITS
ROOT = Path(__file__).resolve().parent
EXPECTED = {'PROOF.md','README.md','REVIEW.md','SOURCES.json','VALIDATION.md',
            'check.py','test_check.py','result.json','SHA256SUMS'}


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def ceilq(x: Q) -> int:
    return -((-x.numerator)//x.denominator)


@dataclass(frozen=True)
class Iv:
    lo: Q
    hi: Q
    def __post_init__(self):
        need(self.lo <= self.hi, 'inverted interval')
    @staticmethod
    def at(x):
        x=Q(x); return Iv(x,x)
    @staticmethod
    def rounded(lo,hi):
        return Iv(Q((Q(lo)*UNIT).__floor__(), UNIT), Q(ceilq(Q(hi)*UNIT), UNIT))
    @staticmethod
    def of(x):
        return x if isinstance(x,Iv) else Iv.at(x)
    def __add__(self,x):
        x=Iv.of(x); return Iv.rounded(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self): return Iv(-self.hi,-self.lo)
    def __sub__(self,x): return self+-Iv.of(x)
    def __rsub__(self,x): return Iv.of(x)+-self
    def __mul__(self,x):
        x=Iv.of(x); a=[self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi]
        return Iv.rounded(min(a),max(a))
    __rmul__=__mul__
    def inv(self):
        need(not self.lo <= 0 <= self.hi,'zero divisor')
        return Iv.rounded(1/self.hi,1/self.lo)
    def __truediv__(self,x): return self*Iv.of(x).inv()
    def __rtruediv__(self,x): return Iv.of(x)*self.inv()
    def __pow__(self,n):
        need(type(n) is int and n>=0,'invalid power')
        out=Iv.at(1); x=self
        while n:
            if n&1: out=out*x
            x=x*x; n//=2
        return out
    def sqrt(self):
        need(self.lo>=0,'negative radical')
        L=(self.lo*UNIT*UNIT).__floor__()
        H=ceilq(self.hi*UNIT*UNIT)
        a=isqrt(L); b=isqrt(H)
        if b*b<H: b+=1
        return Iv(Q(a,UNIT),Q(b,UNIT))
    def overlaps(self,x):
        x=Iv.of(x); return max(self.lo,x.lo)<=min(self.hi,x.hi)
    def contains(self,x): return self.lo<=x<=self.hi
    def receipt(self, places=22):
        s=10**places
        return {'lower':str((self.lo*s).__floor__()),'upper':str(ceilq(self.hi*s)),
                'denominator':str(s)}


@dataclass(frozen=True)
class C:
    re: Q
    im: Q=Q(0)
    def __post_init__(self):
        object.__setattr__(self,'re',Q(self.re));object.__setattr__(self,'im',Q(self.im))
    @staticmethod
    def of(x): return x if isinstance(x,C) else C(Q(x))
    def __add__(self,x):
        x=C.of(x);return C(self.re+x.re,self.im+x.im)
    __radd__=__add__
    def __neg__(self):return C(-self.re,-self.im)
    def __sub__(self,x):return self+-C.of(x)
    def __rsub__(self,x):return C.of(x)+-self
    def __mul__(self,x):
        x=C.of(x);return C(self.re*x.re-self.im*x.im,self.re*x.im+self.im*x.re)
    __rmul__=__mul__
    def inv(self):
        a=self.re*self.re+self.im*self.im;need(a!=0,'complex zero divisor')
        return C(self.re/a,-self.im/a)
    def __truediv__(self,x):return self*C.of(x).inv()
    def __rtruediv__(self,x):return C.of(x)*self.inv()
    def __pow__(self,n):
        need(type(n)is int and n>=0,'complex power')
        out=C(1);x=self
        while n:
            if n&1:out=out*x
            x=x*x;n//=2
        return out


def peval(p,x):
    ans=0
    for a in reversed(p):ans=ans*x+a
    return ans


def pmul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def solve(A,b):
    n=len(b);t=[[Q(v)for v in row]+[Q(b[i])]for i,row in enumerate(A)]
    for j in range(n):
        k=next((k for k in range(j,n)if t[k][j]),None)
        need(k is not None,'singular exact system')
        t[j],t[k]=t[k],t[j];a=t[j][j];t[j]=[v/a for v in t[j]]
        for k in range(n):
            if k==j:continue
            a=t[k][j];t[k]=[v-a*u for v,u in zip(t[k],t[j])]
    return [row[-1]for row in t]


def radau_from_moments(m,r):
    need(len(m)>=2*r+2,'moment coverage')
    p=solve([[m[i+j+1]for j in range(r)]for i in range(r)],
            [-m[i+r+1]for i in range(r)])+[Q(1)] if r else [Q(1)]
    # (-s)^r p(-1/s) = product(1+s*x_j); constant term is 1.
    den=[(-1)**k*p[r-k]for k in range(r+1)]
    num=[sum(den[j]*(-1)**(k-j)*m[k-j]for j in range(k+1))for k in range(r+1)]
    p2=pmul(p,p)
    E=sum(a*m[j+1]for j,a in enumerate(p2))
    return p,num,den,E


def quotient_series(num,den,length):
    need(den[0]==1,'unnormalized quotient')
    c=[]
    for k in range(length):
        c.append((num[k]if k<len(num)else 0)-sum(den[j]*c[k-j]for j in range(1,min(k,len(den)-1)+1)))
    return c


def atan_bound(inv,terms=200):
    x=Q(1,inv); total=sum((-1)**j*x**(2*j+1)/Q(2*j+1)for j in range(terms))
    next_term=(-1)**terms*x**(2*terms+1)/Q(2*terms+1)
    return Iv.rounded(min(total,total+next_term),max(total,total+next_term))


def pi_bound():
    return 16*atan_bound(5)-4*atan_bound(239)


def bernoulli(length):
    B=[Q(1)]
    for m in range(1,length+1):B.append(-sum(Q(comb(m+1,j))*B[j]for j in range(m))/Q(m+1))
    return B


def tail_moment(N,j,pi,B):
    k=j+1
    z=((2*pi)**(2*k)) * Q((-1)**(k+1)*B[2*k],2*factorial(2*k))
    prefix=sum(Q(1,n**(2*k))for n in range(1,N+1))
    return 2*(z-prefix)


def em_tail(N,p,terms=12):
    # Tail from n=N+1. Complete periodic-Bernoulli remainder, using zeta(2q)<2,
    # hence sup|B_(2q)(x)|/(2q)! <=4/6^(2q), with 2*pi>6.
    B=bernoulli(2*terms)
    out=Q(1,(p-1)*N**(p-1))-Q(1,2*N**p)
    rising=1
    for k in range(1,2*terms):
        rising*=p+k-1
        if k%2:
            j=(k+1)//2;out+=B[2*j]*rising/Q(factorial(2*j)*N**(p+2*j-1))
    rem=Q(4,6**(2*terms))*Q(rising,N**(p+2*terms-1))
    return Iv(out-rem,out+rem)*2


def gamma_moments(shapes,scales,maxk):
    # Cumulant recursion, independent of the product-series calculation below.
    cumul=[Q(0)]+[factorial(k-1)*sum(a*x**k for a,x in zip(shapes,scales))for k in range(1,maxk+1)]
    m=[Q(1)]
    for k in range(1,maxk+1):m.append(sum(Q(comb(k-1,j-1))*cumul[j]*m[k-j]for j in range(1,k+1)))
    return m


def product_gamma_moments(shapes,scales,maxk):
    p=[Q(1)]+[Q(0)]*maxk
    for a,x in zip(shapes,scales):
        terms=[Q(1)]
        for k in range(1,maxk+1):terms.append(terms[-1]*(a+k-1)*x/k)
        p=pmul(p,terms)[:maxk+1]
    return [a*factorial(k)for k,a in enumerate(p)]


def reconstruction():
    groups={};finite=[];panels=0;matches=0;rescalings=0
    for start in range(1,5):
        nodes=[Q(1,n*n)for n in range(start,start+9)]
        weights=[2*x for x in nodes]
        m=[sum(w*x**k for x,w in zip(nodes,weights))for k in range(14)]
        for r in range(5):
            p,num,den,E=radau_from_moments(m,r)
            need(E>0 and E<=m[2*r+1], 'orthogonal energy budget')
            for j in range(r):
                need(sum(p[k]*m[k+j+1]for k in range(r+1))==0,'orthogonality')
            c=quotient_series(num,den,2*r+3)
            for k in range(2*r+1):
                need(c[k]==(-1)**k*m[k],'cumulant match');matches+=1
            need(m[2*r+1]-(-1)**(2*r+1)*c[2*r+1]==E,'first missing cumulant')
            for s in [C(Q(1,4)),C(1),C(3),C(Q(-1,2),1),C(0,2),C(2,-3)]:
                exact=sum((w/(1+s*x)for x,w in zip(nodes,weights)),C(0))
                approx=peval(num,s)/peval(den,s)
                rhs=s**(2*r+1)*sum((w*x*peval(p,x)**2/(1+s*x)for x,w in zip(nodes,weights)),C(0))/peval(den,s)**2
                need(approx-exact==rhs,'complete Radau resolvent identity');panels+=1
                if s.im==0 and s.re>0:need((approx-exact).re>0,'positive real ordering')
            for eta in [Q(1,8),Q(2,5),Q(7,10)]:
                mm=[eta**(k+1)*v for k,v in enumerate(m)]
                pp,nn,dd,ee=radau_from_moments(mm,r)
                need(pp==[eta**(r-k)*v for k,v in enumerate(p)],'scaled Radau nodes')
                need(ee==eta**(2*r+2)*E,'scaled first missing cumulant')
                for zz in [Q(1,3),Q(2)]:
                    need(peval(nn,zz)/peval(dd,zz)==eta*peval(num,eta*zz)/peval(den,eta*zz),'scaled Radau resolvent')
                rescalings+=1
            finite.append({'first_n':start,'r':r,'p':[str(a)for a in p],'E':str(E)})
    groups['finite_radau']={'measures':4,'orders_per_measure':5,'rational_or_complex_resolvent_panels':panels,
                            'matched_moment_entries':matches,
                            'rows_sha256':digest(finite),'positive_scale_rescaling_panels':rescalings}
    pi=pi_bound();B=bernoulli(14);native=[];cross=0
    need(pi.lo>Q(314159265358979323846,10**20)and pi.hi<Q(314159265358979323847,10**20),'pi enclosure')
    for N in [2,4,8,16,32,64]:
        m=[tail_moment(N,j,pi,B)for j in range(6)]
        for j,v in enumerate(m):
            need(v.lo>0,'positive actual tail moment')
            need(v.lo>=Q(2,(2*j+1)*(N+1)**(2*j+1))and v.hi<=Q(2,(2*j+1)*N**(2*j+1)), 'complete integral tail bounds')
            need(v.overlaps(em_tail(N,2*j+2)), 'independent complete Euler-Maclaurin overlap');cross+=1
        tau,v,w,z=m[:4];x=w/v;W=v*v/w;d=tau-W;a=W/x;E=z-w*w/v
        need(d.lo>0 and a.lo>0 and x.lo>0 and x.hi<Q(1,(N+1)**2),'actual one-node parameters')
        need(E.lo>0,'actual omitted fourth cumulant')
        for lhs,rhs in [(d+a*x,tau),(a*x*x,v),(a*x**3,w)]:
            need(lhs.overlaps(rhs),'actual three cumulants')
        native.append({'N':N,'drift':d.receipt(),'scale':x.receipt(),'shape':a.receipt(),
                       'first_omitted_cumulant_gap':(6*E).receipt(),
                       'mean':tau.receipt()})
    groups['actual_one_node']={'complete_moment_intervals':36,'independent_EM_overlaps':cross,'rows':native}
    # Actual r=2 from full infinite moments: quadratic roots, weights, endpoint drift.
    two=[]
    for N in [8,16]:
        m=[tail_moment(N,j,pi,B)for j in range(7)]
        det=m[1]*m[3]-m[2]*m[2]
        c0=(m[2]*m[4]-m[3]*m[3])/det
        c1=(m[2]*m[3]-m[1]*m[4])/det
        disc=(c1*c1-4*c0).sqrt();x=(-c1-disc)/2;y=(-c1+disc)/2
        W1=(m[1]*y-m[2])/(x*(y-x));W2=(m[2]-m[1]*x)/(y*(y-x));d=m[0]-W1-W2
        need(0<x.lo<x.hi<y.lo<y.hi<Q(1,(N+1)**2),'two-node separation')
        need(min(d.lo,W1.lo,W2.lo)>0,'two-node positive weights')
        for k in range(5):
            lhs=(d if k==0 else Iv.at(0))+W1*x**k+W2*y**k
            need(lhs.overlaps(m[k]),'actual five cumulants')
        two.append({'N':N,'drift':d.receipt(),'scales':[x.receipt(),y.receipt()],
                    'shapes':[(W1/x).receipt(),(W2/y).receipt()]})
    groups['actual_two_node']={'rows':two,'matched_cumulants':5}
    # Large-order bounds are evaluated, not large-order Radau parameter solves.
    budgets=[]
    for N in [24,32,64,128,256,512,1024]:
        r=N//4;J=r+2;M=2*r+2
        eps=Q(128*J**(4*J-2),M*(4*r+3)*N**(4*r+3))
        need(eps<=Q(16*N**3,3**N),'uniform exponential density bound')
        # R=0,k=0: (2^40 *8 *sqrt(eps))^2.
        squared=(1<<86)*eps
        digits=0
        while squared<Q(1,10**(2*digits+2)):digits+=1
        budgets.append({'N':N,'r':r,'density_epsilon':str(eps),
                        'R0_transform_upper_decimal_power': -digits if digits else None})
    for N in range(1024,2049):
        # Analytic log(N+3)<=sqrt(N) and log3>1,42log2<30 supplied in proof.
        # Squaring verifies 3N/16-30 >= (7/2)sqrt(N) uniformly at these panels.
        q=Q(3*N,16)-30;need(q>0 and q*q>=Q(49*N,4),'growing-strip final budget')
    groups['uniform_error_bounds']={'rows':budgets,'integer_threshold_panels':1025,
                                    'computed_large_order_nodes':False,'computed_transform_values':False}
    gm=0
    for shapes,scales in [([Q(2),Q(2)],[Q(1),Q(1,4)]),
                         ([Q(2),Q(3,2),Q(5,3)],[Q(1),Q(1,7),Q(2,19)]),
                         ([Q(1,3),Q(7,2)],[Q(2,5),Q(1,11)])]:
        m1=gamma_moments(shapes,scales,16);m2=product_gamma_moments(shapes,scales,16)
        need(m1==m2,'gamma convolution / cumulant mismatch');gm+=17
    groups['gamma_algebra']={'complete_moments':gm}
    # Exact test against dropping the Radau endpoint drift.
    m=[Q(3),Q(2),Q(2),Q(3)]
    x=m[2]/m[1];W=m[1]**2/m[2];d=m[0]-W
    need(d==1 and W*x!=m[0], 'drift omission control')
    # A positive error kernel with an even derivative is not a positive density generator.
    # d^4/dx^4 exp(-x^2) at x=0 is 12; at x=1 it is -20/e.
    need(12>0 and 16-48+12<0,'signed derivative control')
    need(Q(4,25*27**4)>Q(1,10**7),'inherited-disk defect lower budget')
    need(PARENT_MARGIN>Q(1,10**22),'inherited margin lower bound')
    need(Q(48,2**128)<Q(1,10**30),'complete changed-source integral perturbation')
    groups['misinterpretation_controls']={'omitted_drift_rejected':True,'even_derivative_changes_sign':True,'changed_source_defect_lower_budget':str(Q(4,25*27**4)),
                                          'new_changed_source_zero_computed':False,
                                          'analytic_zero_transfer_eta':str(Q(1,2**256)),
                                          'parent_certificate_independently_replayed':False}
    return {'schema':'RGT26-1','rh_proved':False,'analytic_proofs_machine_verified':False,
            'original_source':'shape-two integer-square gamma tail',
            'acceptance_arithmetic':'integers, Fractions, outward 320-bit dyadics',
            'groups':groups}


def digest(obj): return hashlib.sha256(canonical(obj)).hexdigest()


def canonical(obj):return (json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode()


def strict_load(data):
    def pairs(items):
        d={}
        for k,v in items:
            need(k not in d,'duplicate JSON key');d[k]=v
        return d
    def bad(x):raise ValueError('noninteger JSON number')
    return json.loads(data,object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)


def authenticate(root):
    need(not root.is_symlink(),'symlink root')
    names=set()
    for p in root.iterdir():
        need(not p.is_symlink(),'symlink input')
        need(p.is_file(),'unexpected directory')
        names.add(p.name)
    need(names==EXPECTED,'packet inventory differs')
    manifest=(root/'SHA256SUMS').read_text().splitlines();seen=set()
    for line in manifest:
        parts=line.split('  ');need(len(parts)==2,'malformed checksum row')
        h,name=parts;need(name in EXPECTED-{'SHA256SUMS'}and name not in seen,'bad manifest path')
        need(len(h)==64 and hashlib.sha256((root/name).read_bytes()).hexdigest()==h,'hash mismatch: '+name)
        seen.add(name)
    need(seen==EXPECTED-{'SHA256SUMS'},'incomplete manifest')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--emit',type=Path);g.add_argument('--check',type=Path)
    a=p.parse_args()
    if a.check:
        authenticate(ROOT)
        received=strict_load(a.check.read_bytes())
        result=reconstruction()
        need(canonical(received)==canonical(result),'reconstructed receipt differs')
        print('PASS_RGT26_BOUNDED_RECONSTRUCTION '+digest(result))
    else:
        result=reconstruction();a.emit.write_bytes(canonical(result));print('PRODUCED '+digest(result))

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,ZeroDivisionError,TypeError)as e:
        print('FAIL_RGT26: '+str(e),file=sys.stderr);sys.exit(1)
