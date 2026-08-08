#!/usr/bin/env python3
"""Exact interval replay for the Q=4 balanced reserve and true physical interval field."""
from fractions import Fraction
import hashlib, json, math
N=4734; SCALE=10**24; TERMS=55
def fl(x): return x.numerator//x.denominator
def ce(x): return -((-x.numerator)//x.denominator)
def logi(y):
    x=(y-1)/(y+1); x2=x*x; t=x; s=Fraction(0)
    for r in range(TERMS): s+=t/(2*r+1); t*=x2
    lo=2*s; hi=lo+2*t/((2*TERMS+1)*(1-x2)); return lo,hi
L2L,L2H=logi(Fraction(2))
def ln(n):
    if n==1:return 0,0
    k=n.bit_length()-1; lo,hi=logi(Fraction(n,1<<k)); lo+=k*L2L;hi+=k*L2H
    return fl(lo*SCALE),ce(hi*SCALE)
def sieve(N):
    s=list(range(N+1));s[1]=1
    for p in range(2,math.isqrt(N)+1):
        if s[p]==p:
            for m in range(p*p,N+1,p):
                if s[m]==m:s[m]=p
    return s
spf=sieve(N); primes=[p for p in range(2,N+1) if spf[p]==p]; logs={p:ln(p) for p in primes}
def pp(n):
    p=spf[n];m=n;e=0
    while m%p==0:m//=p;e+=1
    return p,e
mullo=lambda a,b:a*b//SCALE
mulhi=lambda a,b:(a*b+SCALE-1)//SCALE
lamlo=[0]*(N+1);lamhi=[0]*(N+1)
for p in primes:
    lo,hi=logs[p];q=p
    while q<=N:
        lamlo[q]+=lo;lamhi[q]+=hi
        if q>N//p:break
        q*=p
l2lo,l2hi=logs[2];q=4
while q<=N:
    c=2*(q-1);lamlo[q]+=c*l2lo;lamhi[q]+=c*l2hi
    if q>N//4:break
    q*=4
supp=[n for n in range(2,N+1) if lamhi[n]]
Clo=[0]*(N+1);Chi=[0]*(N+1)
for n in supp:
    p,e=pp(n);lo,hi=logs[p];Clo[n]+=mullo(lamlo[n],e*lo);Chi[n]+=mulhi(lamhi[n],e*hi)
for a in supp:
    for b in supp:
        if a*b>N:break
        Clo[a*b]+=mullo(lamlo[a],lamlo[b]);Chi[a*b]+=mulhi(lamhi[a],lamhi[b])
# c4=e4*Lambda4 is the coefficient of E4 L4; it multiplies the centered-interval kernel.
clo=[0]*(N+1);chi=[0]*(N+1)
for n in range(2,N+1):
    lo,hi=lamlo[n],lamhi[n];q=4
    while q<=n:
        if n%q==0: lo-=3*lamhi[n//q];hi-=3*lamlo[n//q]
        if q>n//4:break
        q*=4
    clo[n]=lo;chi[n]=hi
Glo=[0]*(N+1);Ghi=[0]*(N+1)
for n in range(1,N+1):Glo[n]=Glo[n-1]+clo[n];Ghi[n]=Ghi[n-1]+chi[n]
def floorpref(lo,hi):
    dl=[0]*(N+1);dh=[0]*(N+1)
    for d in range(2,N+1):
        if lo[d]==0 and hi[d]==0:continue
        for m in range(d,N+1,d):dl[m]+=lo[d];dh[m]+=hi[d]
    pl=[0]*(N+1);ph=[0]*(N+1)
    for m in range(1,N+1):pl[m]=pl[m-1]+dl[m];ph[m]=ph[m-1]+dh[m]
    return pl,ph
P1L,P1H=floorpref(lamlo,lamhi);P2L,P2H=floorpref(Clo,Chi)
rows=0;minm=None;minrow=None;maxr=Fraction(0);maxrow=None
for n in range(4,N+1):
  for j in range((n+3)//4,n//2+1):
    k=n-j;P=P1L[n]-P1H[j]-P1H[k];S=P2H[n]-P2L[j]-P2L[k];m=P*P-S*SCALE
    assert P>0 and m>0
    if minm is None or m<minm:minm=m;minrow=(n,j)
    qlo=Glo[n]-Ghi[j]-Ghi[k];qhi=Ghi[n]-Glo[j]-Glo[k];qa=max(abs(qlo),abs(qhi));r=Fraction(qa*qa,m)
    assert r<Fraction(11)
    if r>maxr:maxr=r;maxrow=(n,j)
    rows+=1
assert Fraction(69,100)<L2L
_,l4735h=ln(4735);assert l4735h<Fraction(847,100)*SCALE
ratio=Fraction(1355200,1502889);assert ratio<Fraction(19,20)
result={"classification":"PASS_EXACT_Q4_BALANCED_RESERVE_AND_TRUE_PHYSICAL_TRANSFERENCE","finite_endpoint":N,"balanced_rows":rows,"minimum_row":list(minrow),"minimum_margin_scaled_square":minm,"physical_transference_finite_constant":11,"maximum_physical_ratio_row":list(maxrow),"maximum_physical_ratio_interval_upper":[maxr.numerator,maxr.denominator],"tail_ratio_upper":[ratio.numerator,ratio.denominator],"scale":SCALE,"atanh_terms":TERMS}
payload=json.dumps(result,sort_keys=True,separators=(",",":")).encode();result["result_sha256"]=hashlib.sha256(payload).hexdigest();print(json.dumps(result,indent=2,sort_keys=True))
