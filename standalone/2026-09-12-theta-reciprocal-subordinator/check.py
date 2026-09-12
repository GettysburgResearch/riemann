#!/usr/bin/env python3
"""Native theta signs and exact controls; NOT a full low-zero census or RH proof.
Dyadic primitive design adapted from the frozen theta-cumulant packet.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json
import sys

BITS = 192
SCALE = 1 << BITS
ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md','README.md','REVIEW.md','SOURCES.json','VALIDATION.md',
         'check.py','result.json','SHA256SUMS'}

def need(ok, message):
    if not ok:
        raise ValueError(message)

def up(a, b):
    return -((-a)//b)

class I:
    __slots__ = ('lo','hi')
    def __init__(self, lo, hi=None):
        self.lo = int(lo)
        self.hi = int(lo if hi is None else hi)
        need(self.lo <= self.hi, 'reversed interval')
    @staticmethod
    def point(x):
        x=F(x)
        return I(x.numerator*SCALE//x.denominator, up(x.numerator*SCALE,x.denominator))
    @staticmethod
    def bounds(a,b):
        a,b=F(a),F(b)
        need(a<=b,'reversed bounds')
        return I(a.numerator*SCALE//a.denominator,up(b.numerator*SCALE,b.denominator))
    def __add__(self,y):
        y=as_i(y);return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,y):return self+-as_i(y)
    def __rsub__(self,y):return as_i(y)+-self
    def __mul__(self,y):
        y=as_i(y);a=[self.lo*y.lo,self.lo*y.hi,self.hi*y.lo,self.hi*y.hi]
        return I(min(a)//SCALE,up(max(a),SCALE))
    __rmul__=__mul__
    def inv(self):
        need(not self.lo<=0<=self.hi,'division through zero')
        return I(SCALE*SCALE//self.hi,up(SCALE*SCALE,self.lo))
    def __truediv__(self,y):return self*as_i(y).inv()
    def __pow__(self,n):
        need(type(n) is int and n>=0,'invalid power')
        out,a=I.point(1),self
        while n:
            if n&1:out=out*a
            n//=2
            if n:a=a*a
        return out
    def widen(self,r):
        r=F(r);need(r>=0,'negative radius');k=up(r.numerator*SCALE,r.denominator)
        return I(self.lo-k,self.hi+k)
    def decimal(self,digits=18):
        d=10**digits
        def fmt(a):return ('-' if a<0 else '')+str(abs(a)//d)+'.'+str(abs(a)%d).zfill(digits)
        return [fmt(self.lo*d//SCALE),fmt(up(self.hi*d,SCALE))]
    def contains(self,q):
        q=F(q);return F(self.lo,SCALE)<=q<=F(self.hi,SCALE)
    def abs_upper(self):return F(max(abs(self.lo),abs(self.hi)),SCALE)

def as_i(x):return x if isinstance(x,I) else I.point(x)

def exp_endpoint(x):
    if x==0:return I.point(1)
    if x<=-BITS*SCALE:return I(0,1)
    r=max(0,(8*abs(x)).bit_length()-BITS)
    while 8*abs(x)>SCALE*(1<<r):r+=1
    y=I(x//(1<<r),up(x,1<<r))
    need(max(abs(y.lo),abs(y.hi))*8<=SCALE,'exp range')
    term=I.point(1);total=term
    for j in range(1,49):
        term=term*y/j;total=total+term
    total=total.widen(F(2,8**49*factorial(49)))
    need(total.lo>0,'exp positivity')
    for _ in range(r):total=total*total
    return total

def exp_i(x):
    x=as_i(x)
    if x.hi<=-BITS*SCALE:return I(0,1)
    if x.hi<=0:
        a=exp_endpoint(x.lo)
        return I(a.lo,min(SCALE,a.hi+x.hi-x.lo))
    return I(exp_endpoint(x.lo).lo,exp_endpoint(x.hi).hi)

def cos_i(x):
    x=as_i(x)
    need(max(abs(x.lo),abs(x.hi))<=32*SCALE,'cos input outside cover')
    y=x/32;term=I.point(1);total=term
    for j in range(1,33):
        term=-term*y*y/((2*j-1)*(2*j));total=total+term
    total=total.widen(F(1,factorial(66)))
    for _ in range(5):total=2*total*total-1
    return I(max(-SCALE,total.lo),min(SCALE,total.hi))

def pi_i():
    def atan_inv(k):
        x=F(1,k)
        a=sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(96)),F(0))
        return I.bounds(a,a+x**193/193)
    p=16*atan_inv(5)-4*atan_inv(239)
    need(p.lo>3*SCALE and p.hi<I.point(F(16,5)).lo,'pi bounds')
    return p

def derivative_polynomials(n):
    p={1:F(-6),2:F(4)};ans=[]
    for _ in range(n+1):
        ans.append(p);q={}
        for k,c in p.items():
            q[k]=q.get(k,F(0))+(2*k+F(1,2))*c
            q[k+1]=q.get(k+1,F(0))-2*c
        p={k:c for k,c in q.items() if c}
    return ans

def theta_signs(cells=4096):
    need(type(cells) is int and cells>=1024 and cells%2==0,'mesh guard')
    p=pi_i();h=F(2,cells)
    sums={0:I.point(0),14:I.point(0),15:I.point(0)}
    for j in range(cells+1):
        t=I.point(h*j);e2t,ehalf=exp_i(2*t),exp_i(t/2)
        density=I.point(0)
        for n in range(1,5):
            q=p*n*n*e2t
            density=density+ehalf*(4*q*q-6*q)*exp_i(-q)
        mult=1 if j in (0,cells) else 4 if j%2 else 2
        for z in sums:sums[z]=sums[z]+mult*density*(1 if z==0 else cos_i(z*t))
    B=[6*sum((abs(c)*factorial(k-1) for k,c in q.items()),F(0))
       for q in derivative_polynomials(4)]
    need(B==[F(60),F(366),F(3135),F(71463,2),F(2044911,4)],'L1 derivatives')
    index_tail=8*(75**2+2*75+2)*exp_i(-75)
    space_tail=8*(150**2+2*150+2)*exp_i(-150)
    need(exp_i(4).lo>50*SCALE,'outer threshold')
    report={}
    for z in sums:
        C=sum((F(comb(4,j))*z**(4-j)*B[j] for j in range(5)),F(0))
        err=2*h**4*C/72
        total=(sums[z]*(2*h/3)).widen(err+index_tail.abs_upper()+space_tail.abs_upper())
        report[str(z)]={'enclosure':total.decimal(), 'quadrature_error':str(err)}
        need(total.lo>0 if z in (0,14) else total.hi<0,'native sign '+str(z))
    return {'cells':cells,'terms':4,'physical_interval':[0,2],'bits':BITS,
            'pi':p.decimal(40),'values':report,
            'index_tail_upper':index_tail.decimal(36)[1],
            'time_tail_upper':space_tail.decimal(64)[1],
            'scope':'Sign change in (14,15); not uniqueness, first-zero status or a full census.'}

def controls():
    # The four all-time estimates are reduced analytically to these rational endpoints.
    ratios=[F(2112,2**24),F(1864,2**21),F(2232848,196*2**24),F(1739762,196*2**21)]
    need(all(0<x<F(1,2) for x in ratios),'heat positivity budgets')
    need(-32+F(901,128)<-24,'small-time exponent')
    need(-F(2699,128)<-21,'large-time exponent')
    v=F(32)
    need(2*(v**4+2*v**3+F(9,4)*v*v+v/4)==2232848,'weighted small tail')
    need(2*(30**4+2*30**2*32+2*32**2+F(1,4)*(30**2+32))==1739762,'weighted large tail')
    # Exact complex rational arithmetic, with no numerical roots.
    def mul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
    def add(z,w):return(z[0]+w[0],z[1]+w[1])
    def power(z,n):
        q=(F(1),F(0))
        for _ in range(n):q=mul(q,z)
        return q
    lam=(F(2,5),F(-1,5))
    pl=add(add(mul((F(35),F(0)),power(lam,2)),mul((F(-48),F(0)),lam)),(F(13),F(0)))
    need(mul(lam,pl)==(F(0),F(2)),'synthetic interpolation')
    qs={n:2+2*power(lam,n)[0] for n in range(1,8)}
    c=[F(13),F(-48),F(35)]
    witness=sum((c[i]*c[j]*qs[i+j+2] for i in range(3) for j in range(3)),F(0))
    need(witness==-8,'synthetic signed witness')
    need(F(1,6)-F(1,4)==F(-1,12),'inverse factorial obstruction')
    need(all(q>0 for q in qs.values()),'synthetic scalar controls')
    for k in range(1,9):
        # Integrals of t^(k-1) e^(-a t): factorial normalization.
        a=F(k+2)
        need(F(factorial(k-1),1)/a**k/factorial(k-1)==a**(-k),'Laplace moment')
    for x in [F(0),F(1,2),F(-1,2),F(1),F(-1),F(4),F(-4)]:
        need((exp_i(x)*exp_i(-x)).contains(1),'exp reciprocal enclosure')
    need(cos_i(0).contains(1),'cos zero')
    need((exp_i(0)).contains(1),'exp zero')
    return {'all_time_tail_ratio_bounds':[str(x) for x in ratios],
            'synthetic_q_1_to_7':[str(qs[k]) for k in range(1,8)],
            'synthetic_negative_witness':str(witness),
            'inverse_factorial_determinant':'-1/12',
            'description':'Finite algebra and endpoint inequalities, not analytic theorem proofs.'}

def reconstruct():
    return {'schema':1,'status':'PROPOSED_COMPONENT_PROOFS_NOT_RH',
            'parent_head':'aa281cc871637f287ff91457e5608b5b5f694c25',
            'native_anchor':theta_signs(), 'controls':controls(),
            'external_census':'Platt--Trudgian Theorem 1; only 0<gamma<=30 used; not rerun',
            'rh_proved':False,'heat_complete_monotonicity_proved':False,
            'subordinator_is_original_theta_law':False,
            'analytic_theorems_machine_proved':False}

def strict_load(path):
    def pairs(items):
        d={}
        for k,v in items:
            need(k not in d,'duplicate JSON key');d[k]=v
        return d
    def reject(s):raise ValueError('noninteger JSON numeric literal')
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,
                      parse_float=reject,parse_constant=reject)

def authenticate():
    need({p.name for p in ROOT.iterdir()}==FILES,'inventory')
    need(all((ROOT/n).is_file() and not (ROOT/n).is_symlink() for n in FILES),'regular files')
    entries={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        h,n=line.split('  ',1)
        need(n in FILES-{'SHA256SUMS'} and n not in entries,'manifest path')
        entries[n]=h
    need(set(entries)==FILES-{'SHA256SUMS'},'manifest coverage')
    for n,h in entries.items():need(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h,'hash '+n)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit',action='store_true')
    group.add_argument('--check',type=Path)
    group.add_argument('--mesh',type=int)
    group.add_argument('--controls',action='store_true')
    args=ap.parse_args()
    if args.controls:out=controls()
    elif args.mesh:out=theta_signs(args.mesh)
    else:
        if args.check:authenticate()
        out=reconstruct()
        if args.check:
            # Typed canonical JSON: bool and int cannot alias.
            got=strict_load(args.check)
            need(json.dumps(got,sort_keys=True)==json.dumps(out,sort_keys=True),'fresh result mismatch')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,TypeError,KeyError) as e:
        print('REJECT: '+str(e),file=sys.stderr);sys.exit(1)
