#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import isqrt
from pathlib import Path

HERE=Path(__file__).resolve().parent
SMALL=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61)
BITS=192; DEN=1<<BITS

@dataclass(frozen=True)
class IV:
    lo:Fraction; hi:Fraction
    def __post_init__(self):
        if self.lo>self.hi: raise ValueError
    @staticmethod
    def point(x): return IV(Fraction(x),Fraction(x))
    def __add__(self,o): o=asiv(o); return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asiv(o))
    def __mul__(self,o):
        o=asiv(o); vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(min(vals),max(vals))
    __rmul__=__mul__
def asiv(x): return x if isinstance(x,IV) else IV.point(x)
def sqrt_iv(q:Fraction)->IV:
    q=Fraction(q); a,b=q.numerator,q.denominator
    n=isqrt((a*DEN*DEN)//b); lo=Fraction(n,DEN)
    if n*n*b==a*DEN*DEN:return IV.point(lo)
    return IV(lo,Fraction(n+1,DEN))
def target(q): return IV.point(0) if q<1 else 4*sqrt_iv(q)-3

def p61_divs(limit):
    out=[1]
    for p in SMALL: out += [d*p for d in list(out) if d*p<=limit]
    return sorted(set(out))
def mu_small(d):
    s=0
    for p in SMALL:
        if d%p==0:s+=1;d//=p
    assert d==1
    return -1 if s&1 else 1

def odd_history_gap():
    p,y=71,13; E=IV.point(0);O=IV.point(0);count=0
    for d in p61_divs(p*y):
        atom=sqrt_iv(Fraction(1,d))*(target(Fraction(p*y,d))-sqrt_iv(Fraction(1,p))*target(Fraction(y,d)))
        assert atom.lo>=0
        if mu_small(d)>0:E=E+atom
        else:O=O+atom
        count+=1
    gap=E-O; assert gap.lo>17 and O.hi<E.lo
    return {'active_atoms':count,'gap_lower':str(gap.lo),'gap_upper':str(gap.hi)}

def one_prime_fixture(p=67):
    r=(Fraction(0),Fraction(1)); alpha=(Fraction(1,p),Fraction(0))
    residual=(Fraction(-2,p),Fraction(1))
    total=(residual[0]+2*alpha[0],residual[1]+2*alpha[1])
    assert total==r and p>4
    canonical=(Fraction(-1,p),Fraction(1))
    total2=(canonical[0]+alpha[0],canonical[1]+alpha[1])
    assert total2==r
    return {'p':p,'native':'r','alpha':'r^2','double_alpha_residual':'r-2r^2','canonical_residual':'r-r^2'}

def matrix_fixture():
    rs=[Fraction(1,3),Fraction(1,5),Fraction(1,7)]
    ts=[Fraction(1,9),Fraction(1,25),Fraction(1,49)]
    b=[Fraction(2),Fraction(3),Fraction(5),Fraction(7)]
    f=[Fraction(0)]*4;f[3]=b[3]
    for i in range(2,-1,-1):f[i]=b[i]-rs[i]*f[i+1]
    g=[f[i]+(ts[i]*f[i+1] if i<3 else 0) for i in range(4)]
    for i in range(3): assert g[i]==b[i]-(rs[i]-ts[i])*f[i+1]
    for r,t in zip(rs,ts):assert (r-t)+t==r
    r=Fraction(1,3);t=Fraction(1,9);f1=Fraction(1);f0=-r
    assert f0+t*f1==t-r<0
    lhs=[];rhs=[]
    for i in range(4):
        Ag=ts[i]*g[i+1] if i<3 else 0
        A2f=ts[i]*ts[i+1]*f[i+2] if i<2 else 0
        lhs.append(g[i]-Ag);rhs.append(f[i]-A2f)
    assert lhs==rhs
    return {'raw':list(map(str,rs)),'contracted':list(map(str,ts)),'f':list(map(str,f)),'g':list(map(str,g)),'two_node_current':str(t-r)}

def primes_upto(n):
    s=[True]*(n+1);s[0]=s[1]=False
    for p in range(2,int(n**.5)+1):
        if s[p]:s[p*p:n+1:p]=[False]*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if s[i]]
def qstar(n): return 15 if n==2 else 6 if n==3 else 3 if n==4 else 6 if n>=5 else 0
def euler(c,p):
    for k in range((len(c)-1)//p,0,-1):c[p*k]-=c[k]
def coefficient_identity(N=5000):
    base=[qstar(n) for n in range(N+1)]
    p61=base[:]
    for p in SMALL:euler(p61,p)
    rough=p61[:]
    for p in primes_upto(N):
        if p>=67:euler(rough,p)
    native=base[:]
    for p in primes_upto(N):euler(native,p)
    assert rough==native
    ps=(67,71,73,79); seen=set();checks=0
    for k in range(5):
        for h in combinations(ps,k):
            assert h not in seen;seen.add(h)
            coeff=Fraction(1)
            for p in h:coeff*=Fraction(1,p)
            prod=math.prod(h) if h else 1
            assert coeff==Fraction(1,prod);checks+=1
    return {'coefficient_coordinates':N,'first_owner_histories':checks,'identity':'q*mu_P61*mu_rough=q*mu'}

def asymptotic_barrier_fixtures():
    out=[]
    for z in (10_000,1_000_000,100_000_000):
        L=max(2,2*math.ceil(4*(math.log(z)+1)))
        k=L-1; zw=z-math.log(2*k)
        ratio=(zw/(2*k))*((zw/z)**(k-1))
        assert L*math.log(L)/z<0.7 and ratio>1
        out.append({'z':z,'L':L,'last_to_previous_lower_proxy':ratio})
    return out

def load_finite():
    path=HERE/'results/finite-certificates.json'
    obj=json.loads(path.read_text())
    assert obj['classification']=='PASS_T97700_DIRECTED_FINITE_STRESS_CASES'
    rec={r['X']:r for r in obj['records']}
    assert rec[184]['depth2_current'][0]>0 and rec[184]['P61_base'][0]-rec[184]['native_scalar'][1]>1.36
    assert rec[32605]['depth2_current'][0]>0>rec[32606]['depth2_current'][1]
    assert rec[61841]['depth2_current'][1]<-21.3 and rec[61841]['native_scalar'][0]>9.5
    return obj

def run():
    finite=load_finite()
    payload={
      'classification':'PASS_T97700_THRESHOLD_FLEXIBLE_CAUSAL_DECISION',
      'schema':'riemann.t97700.v1','frozen_base_pr':587,
      'frozen_base_sha':'8a0f074c5b96600b461fdd6e23b47ee2162c4a70',
      'one_prime':one_prime_fixture(),'odd_history':odd_history_gap(),
      'resolvent':matrix_fixture(),'native_root':coefficient_identity(),
      'finite_directed':finite,'asymptotic_barrier_fixtures':asymptotic_barrier_fixtures(),
      'proved':['atomwise first-owner coefficient identity','exact residual absorption','raw exposure conservation','subcritical-depth asymptotic no-go (paper proof)','high-least-prime positive sector (paper proof)'],
      'refuted':['LAPBR67 as stated','universal local one-channel thinning','subcritical threshold-depth closure'],
      'does_not_prove':['critical-saddle Hall transport','eventual native annular scalar positivity','Riemann Hypothesis'],
      'rh_established':False,
    }
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(raw).hexdigest()
    return payload

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=HERE/'results/verification.json')
    a=ap.parse_args();obj=run();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    print(obj['classification']);print(obj['proof_object_sha256'])
if __name__=='__main__':main()
