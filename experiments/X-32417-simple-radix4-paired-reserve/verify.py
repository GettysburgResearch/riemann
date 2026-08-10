#!/usr/bin/env python3
"""Directed exact replay for L-32417 through parent 4734."""
from fractions import Fraction
import hashlib, json, math

N=4734
SCALE=10**24
TERMS=55

def fl(x): return x.numerator//x.denominator
def ce(x): return -((-x.numerator)//x.denominator)

def logi(y):
    x=(y-1)/(y+1); x2=x*x; t=x; s=Fraction(0)
    for r in range(TERMS):
        s += t/(2*r+1)
        t *= x2
    lo=2*s
    hi=lo+2*t/((2*TERMS+1)*(1-x2))
    return lo,hi

L2L,L2H=logi(Fraction(2))

def ln(n):
    if n==1:return 0,0
    k=n.bit_length()-1
    lo,hi=logi(Fraction(n,1<<k))
    lo+=k*L2L; hi+=k*L2H
    return fl(lo*SCALE),ce(hi*SCALE)

def sieve(N):
    s=list(range(N+1)); s[1]=1
    for p in range(2,math.isqrt(N)+1):
        if s[p]==p:
            for m in range(p*p,N+1,p):
                if s[m]==m:s[m]=p
    return s

spf=sieve(N)
primes=[p for p in range(2,N+1) if spf[p]==p]
logs={p:ln(p) for p in primes}

def pp(n):
    p=spf[n]; m=n; e=0
    while m%p==0:
        m//=p; e+=1
    return p,e

mullo=lambda a,b:a*b//SCALE
mulhi=lambda a,b:(a*b+SCALE-1)//SCALE

# Orthogonalized generalized-prime channels.
l0lo=[0]*(N+1); l0hi=[0]*(N+1)
l1lo=[0]*(N+1); l1hi=[0]*(N+1)

# Ordinary von Mangoldt sequence belongs to channel zero.
for p in primes:
    lo,hi=logs[p]; q=p
    while q<=N:
        l0lo[q]+=lo; l0hi[q]+=hi
        if q>N//p:break
        q*=p

# Radix-four tower: even r -> channel zero, odd r -> channel one.
l2lo,l2hi=logs[2]
q=4; r=1
while q<=N:
    c=2*q  # 4^r log 4 = 2*4^r log 2.
    if r%2==0:
        l0lo[q]+=c*l2lo; l0hi[q]+=c*l2hi
    else:
        l1lo[q]+=c*l2lo; l1hi[q]+=c*l2hi
    if q>N//4:break
    q*=4; r+=1

# C_pair = Lambda0 log + Lambda0*Lambda0 + Lambda1*Lambda1.
Clo=[0]*(N+1); Chi=[0]*(N+1)
supp0=[n for n in range(2,N+1) if l0hi[n]]
supp1=[n for n in range(2,N+1) if l1hi[n]]
for n in supp0:
    p,e=pp(n); lo,hi=logs[p]
    Clo[n]+=mullo(l0lo[n],e*lo)
    Chi[n]+=mulhi(l0hi[n],e*hi)
for a in supp0:
    for b in supp0:
        if a*b>N:break
        Clo[a*b]+=mullo(l0lo[a],l0lo[b])
        Chi[a*b]+=mulhi(l0hi[a],l0hi[b])
for a in supp1:
    for b in supp1:
        if a*b>N:break
        Clo[a*b]+=mullo(l1lo[a],l1lo[b])
        Chi[a*b]+=mulhi(l1hi[a],l1hi[b])

def floorpref(lo,hi):
    dl=[0]*(N+1); dh=[0]*(N+1)
    for d in range(2,N+1):
        if lo[d]==0 and hi[d]==0:continue
        for m in range(d,N+1,d):
            dl[m]+=lo[d]; dh[m]+=hi[d]
    pl=[0]*(N+1); ph=[0]*(N+1)
    for m in range(1,N+1):
        pl[m]=pl[m-1]+dl[m]
        ph[m]=ph[m-1]+dh[m]
    return pl,ph

P0L,P0H=floorpref(l0lo,l0hi)
P1L,P1H=floorpref(l1lo,l1hi)
SL,SH=floorpref(Clo,Chi)

rows=0; minm=None; minrow=None
for n in range(4,N+1):
    for j in range((n+3)//4,n//2+1):
        k=n-j
        # True P0,P1 are nonnegative because Lambda0,Lambda1 and each carry are nonnegative.
        # A tiny negative directed lower endpoint may arise only from outward rounding of
        # prefix subtraction, so clamping that certified lower endpoint to zero is valid.
        p0=max(0,P0L[n]-P0H[j]-P0H[k])
        p1=max(0,P1L[n]-P1H[j]-P1H[k])
        s=SH[n]-SL[j]-SL[k]
        margin=p0*p0+p1*p1-s*SCALE
        assert margin>0,(n,j,margin)
        if minm is None or margin<minm:
            minm=margin; minrow=(n,j)
        rows+=1

assert Fraction(69,100)<L2L
_,l4735h=ln(4735)
assert l4735h<Fraction(847,100)*SCALE
ratio=Fraction(1355200,1502889)
assert ratio<Fraction(19,20)

result={
    "classification":"PASS_EXACT_SIMPLE_Q4_PLUS_MINUS_PAIRED_RESERVE",
    "finite_endpoint":N,
    "balanced_rows":rows,
    "minimum_row":list(minrow),
    "minimum_margin_scaled_square":minm,
    "tail_ratio_upper":[ratio.numerator,ratio.denominator],
    "scale":SCALE,
    "atanh_terms":TERMS,
}
payload=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
result["result_sha256"]=hashlib.sha256(payload).hexdigest()
print(json.dumps(result,indent=2,sort_keys=True))
