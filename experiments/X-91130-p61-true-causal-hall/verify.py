#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from bisect import bisect_right
from functools import lru_cache
from math import isqrt
import json
from pathlib import Path
import hashlib

SCALE=10**42
PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
MAXT=4096; SHIFT=8; PMIN=67; YMAX=67

@dataclass(frozen=True)
class I:
    lo:int; hi:int
    def __add__(self,o): o=ii(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-ii(o))
    def __rsub__(self,o): return ii(o)-self
    def __mul__(self,o):
        o=ii(o); vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(vals)//SCALE,-((-max(vals))//SCALE))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=ii(o)
        if o.lo<=0<=o.hi: raise ZeroDivisionError
        rec=I((SCALE*SCALE)//o.hi,-((-(SCALE*SCALE))//o.lo))
        return self*rec
    def __rtruediv__(self,o): return ii(o)/self

def floor_scaled(q:Fraction)->int: return (q.numerator*SCALE)//q.denominator
def ceil_scaled(q:Fraction)->int: return -((-q.numerator*SCALE)//q.denominator)
def ii(x):
    if isinstance(x,I): return x
    if isinstance(x,int): return I(x*SCALE,x*SCALE)
    if isinstance(x,Fraction): return I(floor_scaled(x),ceil_scaled(x))
    raise TypeError(type(x))

@lru_cache(None)
def sqrt_i(q:Fraction)->I:
    q=Fraction(q)
    n=q.numerator*SCALE*SCALE
    d=q.denominator
    m=isqrt(n//d)
    while (m+1)*(m+1)*d<=n: m+=1
    while m*m*d>n: m-=1
    if m*m*d==n: return I(m,m)
    return I(m,m+1)

def invsqrt_i(n:int)->I: return 1/sqrt_i(Fraction(n))

vals=[(1,1)]
for p in PRIMES:
    vals += [(d*p,-mu) for d,mu in list(vals) if d*p<=MAXT+SHIFT]
vals=sorted(vals)
assert len(vals)==len(set(d for d,_ in vals))
E=[d for d,mu in vals if mu==1]
O=[d for d,mu in vals if mu==-1]
ODDS=[d for d in O if d<MAXT]
INV={d:invsqrt_i(d) for d,_ in vals}

def make_pref(arr):
    pa=[Fraction(0)]; pb=[I(0,0)]
    for d in arr:
        pa.append(pa[-1]+Fraction(1,d)); pb.append(pb[-1]+INV[d])
    return pa,pb
EA,EB=make_pref(E); OA,OB=make_pref(O)

def pref(arr,pa,pb,cut):
    i=bisect_right(arr,cut); return pa[i],pb[i]

def hp(t,parent_cut,child_cut):
    ep=min(Fraction(t+SHIFT),parent_cut); op=min(Fraction(t),parent_cut)
    ec=min(Fraction(t+SHIFT),child_cut); oc=min(Fraction(t),child_cut)
    ae,be=pref(E,EA,EB,ep); ao,bo=pref(O,OA,OB,op)
    ace,bce=pref(E,EA,EB,ec); aco,bco=pref(O,OA,OB,oc)
    return ae-ao,be-bo,ace-aco,bce-bco

def eval_h(a,ap,bp,ac,bc,x,y):
    sx=sqrt_i(x); sy=sqrt_i(y)
    return a*sx*ap-3*bp-(a*sy*ac-3*bc)/sx

def fixed_lower(a,ap,bp,ac,bc,x,yl,yr):
    low=min(eval_h(a,ap,bp,ac,bc,x,yl).lo,eval_h(a,ap,bp,ac,bc,x,yr).lo)
    if ac<0:
        sx=sqrt_i(x); q=(-a*ac)/sx; ell=(3*bc)/sx
        vertex=(-ell)/(2*q)
        ulo=sqrt_i(yl).lo; uhi=sqrt_i(yr).hi
        if not (vertex.hi<ulo or vertex.lo>uhi):
            C=a*sx*ap-3*bp; ell2=ell*ell
            penalty_hi=-((-(ell2.hi*SCALE))//(4*q.lo))
            low=min(low,C.lo-penalty_hi)
    return low

def diagonal_lower(a,ap,bp,ac,bc,yl,yr):
    sp=sqrt_i(Fraction(PMIN)); coef=a*sp*ap-a*ac/sp; const=-3*bp+3*bc/sp
    return min((coef*sqrt_i(yl)+const).lo,(coef*sqrt_i(yr)+const).lo)

base_y={Fraction(1),Fraction(YMAX)}
for d,_ in vals:
    if d<=YMAX: base_y.add(Fraction(d))
base_y=sorted(base_y)
mins={4:(None,None),5:(None,None)}; checks=0; child_checks=0

for t in ODDS:
    future=[e for e in E if t<e<=t+SHIFT]
    pb=sorted(set([Fraction(t),Fraction(t+SHIFT)]+[Fraction(e) for e in future]))
    yb=set(base_y)
    for x in pb:
        v=x/PMIN
        if 1<v<YMAX: yb.add(v)
    yb=sorted(yb)
    pints=[(pb[k],pb[k+1],(pb[k]+pb[k+1])/2) for k in range(len(pb)-1)]
    for yl,yr in zip(yb,yb[1:]):
        ym=(yl+yr)/2
        _,_,ac0,bc0=hp(t,Fraction(t+SHIFT),ym)
        for a in (4,5):
            c1=(a*sqrt_i(yl)*ac0-3*bc0).lo
            c2=(a*sqrt_i(yr)*ac0-3*bc0).lo
            child_checks+=2
            assert min(c1,c2)>0,("child",a,t,yl,yr,c1,c2)
        for left,right,xm in pints:
            ap,bp,ac,bc=hp(t,xm,ym)
            if yl>=right/PMIN: continue
            ya=yl; yy=min(yr,right/PMIN)
            if ya>=yy: continue
            for a in (4,5):
                candidates=[(fixed_lower(a,ap,bp,ac,bc,right,ya,yy),"upper")]
                yc=min(yy,left/PMIN)
                if ya<yc: candidates.append((fixed_lower(a,ap,bp,ac,bc,left,ya,yc),"lower"))
                yd=max(ya,left/PMIN)
                if yd<yy: candidates.append((diagonal_lower(a,ap,bp,ac,bc,yd,yy),"diag"))
                for value,kind in candidates:
                    checks+=1
                    assert value>0,(kind,a,t,left,right,ya,yy,value/SCALE)
                    if mins[a][0] is None or value<mins[a][0]: mins[a]=(value,(kind,t,str(left),str(right),str(ya),str(yy)))
        ap,bp,ac,bc=hp(t,Fraction(t+SHIFT),ym); left=Fraction(t+SHIFT)
        for a in (4,5):
            candidates=[]; yc=min(yr,left/PMIN)
            if yl<yc: candidates.append((fixed_lower(a,ap,bp,ac,bc,left,yl,yc),"fullfixed"))
            yd=max(yl,left/PMIN)
            if yd<yr: candidates.append((diagonal_lower(a,ap,bp,ac,bc,yd,yr),"fulldiag"))
            for value,kind in candidates:
                checks+=1
                assert value>0,(kind,a,t,yl,yr,value/SCALE)
                if mins[a][0] is None or value<mins[a][0]: mins[a]=(value,(kind,t,str(yl),str(yr)))

target_large=Fraction(6,25)*64-Fraction(4*67,64)
score_large=Fraction(51,200)*64-Fraction(5*67,64)
assert target_large>0 and score_large>0

result={
  "classification":"PASS_P61_TRUE_CAUSAL_SHIFT8_HALL",
  "small_prime_block":PRIMES,
  "shift":SHIFT,
  "finite_threshold_bound":MAXT,
  "odd_thresholds_checked":len(ODDS),
  "directed_cell_gates":checks,
  "child_hall_gates":child_checks,
  "minimum_target_lower":mins[4][0]/SCALE,
  "minimum_target_location":mins[4][1],
  "minimum_score_lower":mins[5][0]/SCALE,
  "minimum_score_location":mins[5][1],
  "large_prefix_target_lower_at_4096":str(target_large),
  "large_prefix_score_lower_at_4096":str(score_large),
  "scope":("Fixed-point directed intervals include every parent activation boundary d/p and every child activation boundary. "
           "The finite certificate covers all odd P61 thresholds below 4096; the displayed exact corridor inequalities cover all larger thresholds. "
           "This certifies target/score Hall feasibility only, not row typing or RH."),
}
canonical=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
result["proof_object_sha256"]=hashlib.sha256(canonical).hexdigest()
root=Path(__file__).resolve().parent
out=root/"results"/"verification.json"; out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(result["classification"])
print("checks",checks,"child",child_checks)
print("target",result["minimum_target_lower"],result["minimum_target_location"])
print("score",result["minimum_score_lower"],result["minimum_score_location"])
print("sha",result["proof_object_sha256"])
