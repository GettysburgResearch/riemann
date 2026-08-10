#!/usr/bin/env python3
"""Directed fixed-point replay for L-32419 through parent 4734."""
from fractions import Fraction
import hashlib, json, math

N=4734
SCALE=10**20
TERMS=50

def fl(x): return x.numerator//x.denominator
def ce(x): return -((-x.numerator)//x.denominator)

def logi_frac(y):
    x=(y-1)/(y+1); x2=x*x; t=x; s=Fraction(0)
    for r in range(TERMS):
        s+=t/(2*r+1); t*=x2
    lo=2*s; hi=lo+2*t/((2*TERMS+1)*(1-x2))
    return lo,hi

L2F=logi_frac(Fraction(2))
L2=(fl(L2F[0]*SCALE),ce(L2F[1]*SCALE))

def ln(n):
    if n==1:return (0,0)
    k=n.bit_length()-1
    lo,hi=logi_frac(Fraction(n,1<<k))
    return fl(lo*SCALE)+k*L2[0],ce(hi*SCALE)+k*L2[1]

def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def mul(a,b):
    z=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return min(z)//SCALE,(max(z)+SCALE-1)//SCALE

def square_lower(a):
    lo,hi=a
    if lo<=0<=hi:return 0
    return min(lo*lo,hi*hi)

# SPF and Mobius.
spf=list(range(N+1)); spf[1]=1
for p in range(2,math.isqrt(N)+1):
    if spf[p]==p:
        for m in range(p*p,N+1,p):
            if spf[m]==m:spf[m]=p
primes=[p for p in range(2,N+1) if spf[p]==p]
mu=[1]*(N+1); mu[0]=0
for n in range(2,N+1):
    x=n; omega=0; square=False
    while x>1:
        p=spf[x]; e=0
        while x%p==0:x//=p;e+=1
        if e>1:square=True;break
        omega+=1
    mu[n]=0 if square else (-1 if omega&1 else 1)

LOG=[(0,0)]*(N+1)
for n in range(1,N+1):LOG[n]=ln(n)

# Separate-system generalized primes and positive orthogonal channels.
lm=[(0,0)]*(N+1); lp=[(0,0)]*(N+1)
l0=[(0,0)]*(N+1); l1=[(0,0)]*(N+1)
for p in primes:
    q=p
    while q<=N:
        for seq in (lm,lp,l0):seq[q]=add(seq[q],LOG[p])
        if q>N//p:break
        q*=p
q=4; r=1
while q<=N:
    corr=scale(2*q,L2) # 4^r log 4.
    lm[q]=add(lm[q],corr)
    lp[q]=add(lp[q],scale((-1)**r*2*q,L2))
    if r%2==0:l0[q]=add(l0[q],corr)
    else:l1[q]=add(l1[q],corr)
    if q>N//4:break
    q*=4; r+=1

def selberg(lam):
    out=[(0,0)]*(N+1)
    supp=[i for i in range(2,N+1) if lam[i]!=(0,0)]
    for n in supp:out[n]=add(out[n],mul(lam[n],LOG[n]))
    for a in supp:
        for b in supp:
            if a*b>N:break
            out[a*b]=add(out[a*b],mul(lam[a],lam[b]))
    return out

Cm=selberg(lm); Cp=selberg(lp)

# C_pair = Lambda0 log + Lambda0^2 + Lambda1^2.
Cpair=[(0,0)]*(N+1)
s0=[i for i in range(2,N+1) if l0[i]!=(0,0)]
s1=[i for i in range(2,N+1) if l1[i]!=(0,0)]
for n in s0:Cpair[n]=add(Cpair[n],mul(l0[n],LOG[n]))
for a in s0:
    for b in s0:
        if a*b>N:break
        Cpair[a*b]=add(Cpair[a*b],mul(l0[a],l0[b]))
for a in s1:
    for b in s1:
        if a*b>N:break
        Cpair[a*b]=add(Cpair[a*b],mul(l1[a],l1[b]))

# Inverse sources, first and second currents.
bm=[0]*(N+1); bp=[0]*(N+1)
qm=[(0,0)]*(N+1); qp=[(0,0)]*(N+1)
for n in range(1,N+1):
    bm[n]=mu[n]-(4*mu[n//4] if n%4==0 else 0)
    bp[n]=mu[n]+(4*mu[n//4] if n%4==0 else 0)
    if n>1:
        qm[n]=scale(-bm[n],LOG[n])
        qp[n]=scale(-bp[n],LOG[n])

def conv_exact_interval(b,C):
    out=[(0,0)]*(N+1)
    sb=[i for i in range(1,N+1) if b[i]]
    sc=[i for i in range(1,N+1) if C[i]!=(0,0)]
    for d in sb:
        for m in sc:
            if d*m>N:break
            out[d*m]=add(out[d*m],scale(b[d],C[m]))
    return out

tm=conv_exact_interval(bm,Cm)
tp=conv_exact_interval(bp,Cp)

def floor_prefix_interval(seq):
    dlo=[0]*(N+1); dhi=[0]*(N+1)
    for d in range(1,N+1):
        lo,hi=seq[d]
        if lo or hi:
            for m in range(d,N+1,d):dlo[m]+=lo;dhi[m]+=hi
    plo=[0]*(N+1); phi=[0]*(N+1)
    for m in range(1,N+1):
        plo[m]=plo[m-1]+dlo[m]; phi[m]=phi[m-1]+dhi[m]
    return plo,phi

def floor_prefix_exact(seq):
    d=[0]*(N+1)
    for q in range(1,N+1):
        if seq[q]:
            for m in range(q,N+1,q):d[m]+=seq[q]
    p=[0]*(N+1)
    for m in range(1,N+1):p[m]=p[m-1]+d[m]
    return p

F0=floor_prefix_interval(l0); F1=floor_prefix_interval(l1); FS=floor_prefix_interval(Cpair)
FQm=floor_prefix_interval(qm); FQp=floor_prefix_interval(qp)
FTm=floor_prefix_interval(tm); FTp=floor_prefix_interval(tp)
FYm=floor_prefix_exact(bm); FYp=floor_prefix_exact(bp)

def row_interval(F,n,j):
    k=n-j
    return F[0][n]-F[1][j]-F[1][k],F[1][n]-F[0][j]-F[0][k]

def row_exact(F,n,j): return F[n]-F[j]-F[n-j]

def negative_product_lower(y,t):
    # Lower endpoint of -y*t, converted from SCALE to SCALE^2.
    p=scale(y,t)
    return -p[1]*SCALE

rows=0; minimum=None; minimum_row=None
for n in range(4,N+1):
    for j in range((n+3)//4,n//2+1):
        p0=row_interval(F0,n,j); p1=row_interval(F1,n,j); ss=row_interval(FS,n,j)
        # True P0/P1 are nonnegative. Clamp only the outward-rounded lower endpoint.
        p0=(max(0,p0[0]),p0[1]); p1=(max(0,p1[0]),p1[1])
        reserve_lower=square_lower(p0)+square_lower(p1)-ss[1]*SCALE
        twice_augmented=(
            2*reserve_lower
            +square_lower(row_interval(FQm,n,j))
            +square_lower(row_interval(FQp,n,j))
            +negative_product_lower(row_exact(FYm,n,j),row_interval(FTm,n,j))
            +negative_product_lower(row_exact(FYp,n,j),row_interval(FTp,n,j))
        )
        assert twice_augmented>0,(n,j,twice_augmented)
        if minimum is None or twice_augmented<minimum:
            minimum=twice_augmented; minimum_row=(n,j)
        rows+=1

result={
    "classification":"PASS_EXACT_SIMPLE_Q4_PAIRED_AUGMENTED_HERMITIAN_RESERVE",
    "finite_endpoint":N,
    "balanced_rows":rows,
    "minimum_row":list(minimum_row),
    "minimum_twice_augmented_margin_scaled_square":minimum,
    "scale":SCALE,
    "atanh_terms":TERMS,
}
payload=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
result["result_sha256"]=hashlib.sha256(payload).hexdigest()
print(json.dumps(result,indent=2,sort_keys=True))
