#!/usr/bin/env python3
from __future__ import annotations
import argparse, cmath, json, math, random
from fractions import Fraction
from pathlib import Path

def fac(n):
    d={}; p=2
    while p*p<=n:
        while n%p==0: d[p]=d.get(p,0)+1; n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def mu(n):
    f=fac(n)
    return 0 if any(e>1 for e in f.values()) else (-1)**len(f)
def lv(n): return {p:Fraction(e) for p,e in fac(n).items()}
def add(a,b,s=Fraction(1)):
    o=dict(a)
    for p,x in b.items():
        o[p]=o.get(p,Fraction(0))+s*x
        if not o[p]:del o[p]
    return o
def scl(a,s): return {p:s*x for p,x in a.items() if s*x}
def Lam(n):
    f=fac(n)
    return {next(iter(f)):Fraction(1)} if len(f)==1 else {}
def chi(N,j,d): return N//d-j//d-(N-j)//d

def sources(M):
    muv={n:mu(n) for n in range(1,M+1) if mu(n)}
    bc=dict(muv)
    for n in range(4,M+1,4):
        if n//4 in muv: bc[n]=bc.get(n,0)-4*muv[n//4]
    b4=dict(muv); q=4
    while q<=M:
        for s,v in muv.items():
            if q*s<=M:b4[q*s]=b4.get(q*s,0)-3*v
        q*=4
    i={n:scl(lv(n),Fraction(-v)) for n,v in bc.items() if v}
    L={2:Fraction(2)}
    for n in range(4,M+1,4):
        if n//4 in b4:i[n]=add(i.get(n,{}),L,Fraction(-b4[n//4]))
    return i

def source_checks(M=512):
    i=sources(M); L={2:Fraction(2)}
    for n in range(1,M+1):
        a=0;s=n
        while s%4==0:s//=4;a+=1
        u=mu(s); e={}
        if u:
            e=scl(lv(s),Fraction(-u)) if a==0 else (
              add(scl(lv(s),Fraction(4*u)),L,Fraction(3*u))
              if a==1 else scl(L,Fraction(3*u)))
        assert i.get(n,{})==e
    for n in range(1,M+1):
        a={}
        for d in range(1,n+1):
            if n%d==0:a=add(a,i.get(d,{}))
        e=Lam(n)
        if n%4==0:e=add(e,Lam(n//4),Fraction(-4))
        x=n
        while x>=4 and x%4==0:x//=4
        if n>=4 and x==1:e=add(e,L,Fraction(3))
        assert a==e
    return M,M

def prefix_checks():
    r=random.Random(90410); rows=0
    for N in range(2,65):
        f={d:r.randint(-5,5) for d in range(1,N+1)}
        c={m:sum(f[d] for d in range(1,m+1) if m%d==0) for m in range(1,N+1)}
        C=[0]
        for m in range(1,N+1):C.append(C[-1]+c[m])
        for j in range(N+1):
            assert sum(f[d]*chi(N,j,d) for d in f)==C[N]-C[j]-C[N-j]
            rows+=1
    return rows

def vals(c,N):
    C=[0.]
    for m in range(1,N+1):C.append(C[-1]+c.get(m,0.))
    return [C[N]-C[j]-C[N-1-j] for j in range(N)]
def hat(v,k):
    N=len(v)
    if k==0:return sum(v)/N
    return sum(v[j]*(cmath.exp(-2j*math.pi*k*(j+1)/N)-
      cmath.exp(-2j*math.pi*k*j/N))/(-2j*math.pi*k) for j in range(N))
def fourier_checks():
    r=random.Random(90411); nr=er=0
    for N in (5,8,11,16,23,31):
        c={m:r.uniform(-2,2) for m in range(1,N+1)}; v=vals(c,N)
        for k in (-2*N-1,-7,-1,1,2,N+3):
            z=sum(c[m]*math.sin(2*math.pi*k*m/N) for m in range(1,N))/(math.pi*k)
            assert abs(hat(v,k)-z)<2e-11*(1+abs(z)); nr+=1
        z0=-sum(c.values())+2/N*sum(m*x for m,x in c.items())
        lhs=sum(x*x for x in v)/N; rhs=z0*z0
        for a in range(1,N):
            S=sum(c[m]*math.sin(2*math.pi*a*m/N) for m in range(1,N))
            rhs+=S*S/(N*N*math.sin(math.pi*a/N)**2)
        assert abs(lhs-rhs)<3e-10*(1+lhs); er+=1
    return nr,er

def primes(N): return [x for x in range(2,N+1) if all(x%p for p in range(2,int(x**.5)+1))]
def eps(s,sgn):
    z=1
    for p in fac(s):z*=sgn[p]
    return z
def amp(s,N,j):
    L=math.log(4); z=-math.log(s)*chi(N,j,s)
    if 4*s<=N:z+=(4*math.log(s)+3*L)*chi(N,j,4*s)
    q=16*s
    while q<=N:z+=3*L*chi(N,j,q);q*=4
    return z
def random_checks(N=24):
    ps=primes(N); cores=[s for s in range(1,N+1) if s%4 and mu(s)]
    R=1<<len(ps)
    for j in range(N+1):
        A={s:amp(s,N,j) for s in cores}; D=sum(x*x for x in A.values()); E=0.
        for mask in range(R):
            sg={p:(-1 if mask>>k&1 else 1) for k,p in enumerate(ps)}
            E+=sum(eps(s,sg)*A[s] for s in cores)**2
        assert abs(E/R-D)<2e-10*(1+D)
    return R,N+1

def cv(n):
    L=math.log(4); o={}
    for m in range(1,n+1):
        z=sum(float(x)*math.log(p) for p,x in Lam(m).items())
        if m%4==0:z-=4*sum(float(x)*math.log(p) for p,x in Lam(m//4).items())
        x=m
        while x>=4 and x%4==0:x//=4
        if m>=4 and x==1:z+=3*L
        o[m]=z
    return o
def bulk_checks():
    rows=0
    for N in (64,97,128,191,256,383):
        c=cv(N); K=math.ceil(math.sqrt(N)); bulk=total=0.
        for a in range(1,N):
            S=sum(c[m]*math.sin(2*math.pi*a*m/N) for m in range(1,N))
            total+=S*S
            if min(a,N-a)>=K:bulk+=S*S/(N*N*math.sin(math.pi*a/N)**2)
        E=sum(c[m]**2 for m in range(1,N))
        assert total<=N*E*(1+2e-11)
        assert bulk<=N*E/(4*K*K)*(1+2e-10);rows+=1
    return rows

def main():
    p=argparse.ArgumentParser();p.add_argument("--json",default=str(Path(__file__).with_name("results")/"verification.json"));a=p.parse_args()
    f,c=source_checks(); fr,ir=fourier_checks(); rc,rr=random_checks()
    out={"classification":"PASS_X_90410_PIG_FOURIER_RADEMACHER",
      "scope":"finite source algebra, finite Fourier identities, random-model orthogonality, and finite bulk inequalities only",
      "fiber_rows":f,"prefix_rows":c,"prefix_carry_rows":prefix_checks(),
      "fourier_coefficient_rows":fr,"inverse_laplacian_rows":ir,
      "rademacher_configurations":rc,"rademacher_carry_rows":rr,
      "bulk_inequality_rows":bulk_checks(),"deterministic_pig_proved":False,"rh_proved":False}
    Path(a.json).parent.mkdir(parents=True,exist_ok=True);Path(a.json).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=="__main__":main()
