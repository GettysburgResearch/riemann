#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import isqrt, prod, gcd
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
import argparse, bisect, heapq, json, time
from pathlib import Path

PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
P61=prod(PRIMES)
D=10**55
YMAX=67

@dataclass(frozen=True)
class FI:
    lo:int
    hi:int
    def __add__(self,o):
        o=asfi(o); return FI(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return FI(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asfi(o))
    def __rsub__(self,o): return asfi(o)-self
    def __mul__(self,o):
        o=asfi(o); vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return FI(min(vals)//D, -((-max(vals))//D))
    __rmul__=__mul__
    def scale(self,q:Fraction):
        q=Fraction(q)
        vals=(self.lo*q.numerator,self.hi*q.numerator)
        if q.numerator>=0:
            return FI(vals[0]//q.denominator,-((-vals[1])//q.denominator))
        return FI(vals[1]//q.denominator,-((-vals[0])//q.denominator))

def asfi(x):
    if isinstance(x,FI):return x
    q=Fraction(x)
    lo=(q.numerator*D)//q.denominator
    hi=-((-q.numerator*D)//q.denominator)
    return FI(lo,hi)

def absup(x:FI):return max(abs(x.lo),abs(x.hi))
def rec_pos(x:FI):
    assert x.lo>0
    return FI((D*D)//x.hi,-((-(D*D))//x.lo))
def div_pos(x:FI,y:FI):return x*rec_pos(y)

@lru_cache(maxsize=None)
def sqrt_i(x:Fraction)->FI:
    x=Fraction(x); assert x>=0
    z=(D*D*x.numerator)//x.denominator; m=isqrt(z)
    while (m+1)*(m+1)*x.denominator<=D*D*x.numerator:m+=1
    while m*m*x.denominator>D*D*x.numerator:m-=1
    hi=m if m*m*x.denominator==D*D*x.numerator else m+1
    return FI(m,hi)

@lru_cache(maxsize=None)
def log_int(n:int)->FI:
    assert n>=1
    if n==1:return FI(0,0)
    with localcontext() as ctx:
        ctx.prec=90
        value=Decimal(n).ln()
        scaled=value*Decimal(D)
        lo=scaled.to_integral_value(rounding=ROUND_FLOOR)-2
        hi=scaled.to_integral_value(rounding=ROUND_CEILING)+2
    return FI(int(lo),int(hi))

@lru_cache(maxsize=None)
def log_i(x:Fraction)->FI:
    x=Fraction(x); assert x>0
    return log_int(x.numerator)-log_int(x.denominator)

@lru_cache(maxsize=None)
def invsqrt_int(n:int)->FI:return rec_pos(sqrt_i(Fraction(n)))

# ---------- global 2^18 prefix scan ----------
def half_products(primes):
    vals=[(1,1,invsqrt_int(1),log_int(1))]
    for p in primes:
        old=list(vals); lp=log_int(p)
        for v,s,iv,lv in old:
            vals.append((v*p,-s,invsqrt_int(v*p),lv+lp))
    vals.sort(key=lambda x:x[0]);return vals
LEFT=half_products(PRIMES[:9]);RIGHT=half_products(PRIMES[9:])

def scan_global():
    beta_lo=beta_hi=D
    for p in PRIMES:
        iv=invsqrt_int(p)
        flo,fhi=D-iv.hi,D-iv.lo
        beta_lo=(beta_lo*flo)//D
        beta_hi=(beta_hi*fhi + D-1)//D
    assert beta_lo>0 and 400*beta_hi<D
    heap=[]
    for i,a in enumerate(LEFT):heapq.heappush(heap,(a[0]*RIGHT[0][0],i,0))
    Mlo=Mhi=Clo=Chi=0;maxm=(0,1);maxe=(0,1);cnt=0
    while heap:
        v,i,j=heapq.heappop(heap);a=LEFT[i];b=RIGHT[j]
        sign=a[1]*b[1]
        il=(a[2].lo*b[2].lo)//D
        ih=(a[2].hi*b[2].hi + D-1)//D
        ll,lh=a[3].lo+b[3].lo,a[3].hi+b[3].hi
        if sign>0:
            Mlo+=il;Mhi+=ih;Clo+=il*ll;Chi+=ih*lh
        else:
            Mlo-=ih;Mhi-=il;Clo-=ih*lh;Chi-=il*ll
        am=max(abs(Mlo),abs(Mhi));assert 20*am<27*D
        if am>maxm[0]:maxm=(am,v)
        dlo,dhi=Mlo-beta_hi,Mhi-beta_lo
        vals=(dlo*ll,dlo*lh,dhi*ll,dhi*lh)
        elo,ehi=min(vals)-Chi,max(vals)-Clo
        ae=max(abs(elo),abs(ehi));assert 6*ae<7*D*D
        if ae>maxe[0]:maxe=(ae,v)
        cnt+=1;j+=1
        if j<len(RIGHT):heapq.heappush(heap,(a[0]*RIGHT[j][0],i,j))
    assert cnt==2**18
    return {'states':cnt,'beta':[beta_lo/D,beta_hi/D],
            'max_abs_M':maxm[0]/D,'M_at':maxm[1],
            'max_abs_E':maxe[0]/(D*D),'E_at':maxe[1]}

# ---------- compact splines for p=67 and p=71 ----------
def small_divisors(limit):
    vals=[(1,1)]
    for p in PRIMES:vals += [(v*p,-s) for v,s in list(vals) if v*p<=limit]
    return sorted(set(vals))
SMALL=small_divisors(71*YMAX);SD=[v for v,s in SMALL]
PM=[];PC=[];M=FI(0,0);C=FI(0,0)
for v,s in SMALL:
    iv=invsqrt_int(v);lv=log_int(v);M=M+s*iv;C=C+s*(iv*lv);PM.append(M);PC.append(C)
def MP(x):
    x=Fraction(x)
    if x<1:return FI(0,0)
    return PM[bisect.bisect_right(SD,x)-1]
def G(x):
    x=Fraction(x)
    if x<1:return FI(0,0)
    i=bisect.bisect_right(SD,x)-1
    return PM[i]*log_i(x)-PC[i]

ROUGH=[k for k in range(1,71*YMAX+1) if gcd(k,P61)==1]
RS=[];RT=[];S=FI(0,0);T=FI(0,0)
for k in ROUGH:
    iv=invsqrt_int(k);lv=log_int(k);S+=iv;T+=iv*lv;RS.append(S);RT.append(T)
def RG(x):
    x=Fraction(x)
    if x<1:return FI(0,0)
    i=bisect.bisect_right(ROUGH,x)-1
    return RS[i]*log_i(x)-RT[i]

def compact(p,fb,lb,bb):
    r=invsqrt_int(p)
    events={Fraction(2,3),Fraction(YMAX)}
    for d in SD:
        z=Fraction(d,p)
        if Fraction(2,3)<=z<=YMAX:events.add(z)
        if d<=YMAX:events.add(Fraction(d))
    maxf=(0,None);maxl=(0,None)
    for z in sorted(events):
        f=G(p*z)-r*G(z);sl=MP(p*z)-r*MP(z)
        assert absup(f)*fb.denominator<fb.numerator*D,(p,z,f)
        assert absup(sl)*lb.denominator<lb.numerator*D,(p,z,sl)
        if absup(f)>maxf[0]:maxf=(absup(f),z)
        if absup(sl)>maxl[0]:maxl=(absup(sl),z)
    events={Fraction(1),Fraction(YMAX)}
    for k in ROUGH:
        y=Fraction(k,p)
        if 1<=y<=YMAX:events.add(y)
        if k<=YMAX:events.add(Fraction(k))
    minr=None
    for y in sorted(events):
        d=RG(p*y)-r*RG(y);sy=sqrt_i(y)
        assert d.lo*bb.denominator>bb.numerator*sy.hi,(p,y,d,sy)
        ratio=div_pos(d,sy)
        rec=(ratio.lo,y)
        if minr is None or rec[0]<minr[0]:minr=rec
    return {'p':p,'max_F':maxf[0]/D,'F_at':str(maxf[1]),
            'max_lip':maxl[0]/D,'lip_at':str(maxl[1]),
            'min_bulk_ratio':minr[0]/D,'bulk_at':str(minr[1])}

def geometry():
    maxs=(0,None);maxkr=(0,None)
    for j in range(2,YMAX):
        sj=sqrt_i(Fraction(j));w=[]
        for m in range(1,j):w.append((sj*invsqrt_int(m)).scale(Fraction(-2,j-1)))
        w.append(asfi(j+2));w.append(-(sj*invsqrt_int(j+1)).scale(j))
        total=FI(0,0)
        for x in w:total+=x
        assert 5*absup(total)<6*D
        if absup(total)>maxs[0]:maxs=(absup(total),j)
        anchor=1 if j<=18 else 2 if j<=39 else 3 if j<=62 else 4
        kr=0
        pref=[];s=FI(0,0)
        for x in w:s+=x;pref.append(s)
        suff=[None]*len(w);s=FI(0,0)
        for k in range(len(w)-1,-1,-1):s+=w[k];suff[k]=s
        for m in range(1,j+1):
            cum=pref[m-1] if m<anchor else -suff[m]
            width=log_i(Fraction(m+1,m))
            kr += (absup(cum)*width.hi + D-1)//D
        assert 5*kr<19*D,(j,kr/D)
        if kr>maxkr[0]:maxkr=(kr,j)
    return {'max_mass':maxs[0]/D,'mass_j':maxs[1],
            'max_KR':maxkr[0]/D,'KR_j':maxkr[1]}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--json', default='results/verification.json')
    args=ap.parse_args()
    g=scan_global();geo=geometry()
    c67=compact(67,Fraction(119,100),Fraction(7,5),Fraction(37,10))
    c71=compact(71,Fraction(100),Fraction(100),Fraction(19,5))
    m67=Fraction(2)*Fraction(37,10)*Fraction(66,65)-Fraction(6,5)*Fraction(119,100)-Fraction(19,5)*Fraction(7,5)
    assert m67==Fraction(2489,3250)>0
    fixed=Fraction(38,5)*Fraction(66,65)
    boundary0=Fraction(6,5)*Fraction(4,3)+Fraction(19,5)*Fraction(31,20)
    slope=Fraction(6,5)*Fraction(1,400)
    cross=fixed/Fraction(2,9)
    mlarge=fixed-boundary0-slope*cross
    assert mlarge==Fraction(9973,81250)>0
    assert Fraction(2,9)>slope
    out={'classification':'PASS_P61_ONE_PRIME_ROW_SPLICE','global':g,'geometry':geo,
         'p67':c67,'p71':c71,'p67_margin':str(m67),'large_margin':str(mlarge),
         'crossover':str(cross),
         'scope':'Directed fixed-denominator Decimal-log, exact integer square-root, and exact Fraction comparisons certify the P61 finite gates. The analytic comparison proves every p>=67 inherited row. This does not by itself certify the complete ordinary/radix-four splice or RH.'}
    path=Path(args.json)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['classification']);print(path)
if __name__=='__main__':main()
