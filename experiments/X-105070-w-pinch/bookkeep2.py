import math
# (C) DIRECT u-block <-> X-octave check: independent quadratures of
#  I1 = int_{u1}^{u2} u W_u^2 du/u  vs  I2 = (1/3) int_{u1^3}^{u2^3} V^2 dX/X
NMAX=200000
# eta = coeffs of zeta^{1/2}: multiplicative, eta(p^k)=C(2k,k)/4^k
spf=list(range(NMAX+1))
for p in range(2,int(NMAX**.5)+1):
    if spf[p]==p:
        for q in range(p*p,NMAX+1,p):
            if spf[q]==q: spf[q]=p
from math import comb
def etaval(n):
    v=1.0
    while n>1:
        p=spf[n]; k=0
        while n%p==0: n//=p; k+=1
        v*=comb(2*k,k)/4**k
    return v
eta=[0.0]*(NMAX+1); eta[1]=1.0
for n in range(2,NMAX+1): eta[n]=etaval(n)
mu=[0]*(NMAX+1); mu[1]=1
for n in range(2,NMAX+1):
    m=n; v=1; ok=True
    while m>1:
        p=spf[m]; m//=p
        if m%p==0: ok=False; break
        v=-v
    mu[n]=v if ok else 0
import functools
@functools.lru_cache(maxsize=200000)
def Lam(X):
    U=int(round(X**(1/3.)))
    while U**3>X: U-=1
    while (U+1)**3<=X: U+=1
    N=int(X//U)
    s=0.0
    for n in range(N//2+1,N+1):
        # h_U(n)=sum_{d|n, d>U} mu(d) eta(n/d)
        h=0.0
        d=1
        for d in divisors(n):
            if d>U and mu[d]!=0: h+=mu[d]*eta[n//d]
        if h: s+=h*n**-0.5*math.log(2*n/N)/math.log(2)
    return s,N
divcache={}
def divisors(n):
    if n in divcache: return divcache[n]
    ds=[1]; m=n
    while m>1:
        p=spf[m]; k=0
        while m%p==0: m//=p; k+=1
        ds=[d*p**j for d in ds for j in range(k+1)]
    if len(divcache)<400000: divcache[n]=ds
    return ds
def Wsq_u(u):   # u W_u^2 (integrand against du/u)
    X=u**3
    L,N=Lam(math.floor(X))
    return u*(L*math.sqrt(math.log(N))/u)**2
def Vsq_X(X):
    L,N=Lam(math.floor(X))
    return (L*math.sqrt(math.log(N))*X**(-1/6.))**2
u1,u2=20.0,40.0   # one u-octave; X in [8000, 64000], N<=~4000
M1=6000
I1=0.0
for i in range(M1):
    lu=math.log(u1)+(i+0.5)*(math.log(u2)-math.log(u1))/M1
    I1+=Wsq_u(math.exp(lu))
I1*=(math.log(u2)-math.log(u1))/M1
M2=18000
I2=0.0
X1,X2=u1**3,u2**3
for i in range(M2):
    lx=math.log(X1)+(i+0.5)*(math.log(X2)-math.log(X1))/M2
    I2+=Vsq_X(math.exp(lx))
I2*=(math.log(X2)-math.log(X1))/M2/3.0
print("I1 (u-side)  =",I1)
print("I2 (X-side/3)=",I2)
print("rel diff     =",abs(I1-I2)/max(abs(I1),1e-12))
# octave split: the 3 X-octaves of [X1,X2)
for L0 in range(3):
    a=X1*2**L0; b=X1*2**(L0+1)
    Mo=6000; s=0.0
    for i in range(Mo):
        lx=math.log(a)+(i+0.5)*(math.log(b)-math.log(a))/Mo
        s+=Vsq_X(math.exp(lx))
    s*=math.log(2)/Mo
    print("X-octave",L0,"int V^2 dX/X =",s)
