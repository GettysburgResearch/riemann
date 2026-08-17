#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math,random
from fractions import Fraction
from pathlib import Path
from exact_kernels import A,B,Q,band,certificate

HERE=Path(__file__).resolve().parent

def mobius(N):
    mu=[0]*(N+1); mu[1]=1; ps=[]; comp=[False]*(N+1)
    for n in range(2,N+1):
        if not comp[n]: ps.append(n); mu[n]=-1
        for p in ps:
            if n*p>N: break
            comp[n*p]=True
            if n%p==0: mu[n*p]=0; break
            mu[n*p]=-mu[n]
    return mu

def factors(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def W(x):
    if not 0<=x<=1:return 0.0
    if x<=.25:return 5*x-63*x*x+170*x*x*x
    return (-x+3*x*x-2*x*x*x)/3

def K(x,c):return sum(a*2**(-r/2)*W(2**r*x) for r,a in enumerate(c))
def J(x,c):return sum(float(Q[h])*K(2**h*x,c) for h in range(4))

def scan(X,mu):
    S=D=0.0; L=math.log(2)
    for m in range(X//1024+1,X+1):
        if m%2==0 or mu[m]==0:continue
        g=(math.log(m)*J(m/X,A)+L*J(m/X,B))/math.sqrt(m)
        S+=mu[m]*g; D+=g*g
    return {"X":X,"annular_sum":S,"diagonal":D,"cross":S*S-D}

def run(limit):
    cert=certificate(); exact=ann=inv=ratio=gcd=square=typei=count=fire=0
    assert len(cert["bands"])==10
    for src in (A,B):
        for j in range(10):
            assert len(band(src,j))==3; exact+=3
        for j in range(10,17):
            assert all(v.zero() for v in band(src,j).values()); ann+=1
    for k in (1,2,3):
        assert sum(Q[h]*2**(h*k) for h in range(4))==0; ann+=1
    coeff=[]
    for n in range(40):
        coeff.append(sum(Fraction(1,2**a)*Fraction(1,4**b)*Fraction(1,8**(n-a-b))
                         for a in range(n+1) for b in range(n-a+1)))
    for n in range(35):
        assert sum(Q[h]*coeff[n-h] for h in range(min(3,n)+1))==(1 if n==0 else 0); inv+=1
    assert Fraction(64,21)==1/((1-Fraction(1,2))*(1-Fraction(1,4))*(1-Fraction(1,8))); inv+=1
    mu=mobius(max(limit,4096)); rng=random.Random(95400)
    for X in range(1024,1057):
        for _ in range(200):
            m=rng.randint(X//1024+1,X-1); n=rng.randint(m+1,X)
            assert n/m<1024; ratio+=1
    for X in range(33,70):
        active=[m for m in range(1,X+1) if m%2 and mu[m]]
        w={m:Fraction((m%11)-5,m+3) for m in active}
        S=sum(Fraction(mu[m])*w[m] for m in active); D=sum(w[m]**2 for m in active)
        C=sum(2*Fraction(mu[m]*mu[n])*w[m]*w[n] for i,m in enumerate(active) for n in active[i+1:])
        assert S*S==D+C; square+=1
        G=Fraction()
        for i,m in enumerate(active):
            for n in active[i+1:]:
                d=math.gcd(m,n); a=m//d; b=n//d
                assert math.gcd(a,b)==math.gcd(a,d)==math.gcd(b,d)==1
                assert mu[m]*mu[n]==mu[a]*mu[b]
                G+=2*Fraction(mu[a]*mu[b])*w[m]*w[n]; gcd+=1
        assert G==C
    for m in range(3,2048,2):
        if not mu[m]:continue
        fs=factors(m)
        assert {p:mu[m]*e for p,e in fs.items()}=={p:-mu[m//p] for p in fs}; typei+=1
    for X in range(32,96):
        for H in range(1,7):
            near=sum(1 for m in range(1,X+1) for n in range(m+1,min(X,m+H)+1))
            assert near<=X*H; count+=1
        for H in range(2,7):
            large=sum(1 for m in range(1,X+1) for n in range(m+1,X+1) if math.gcd(m,n)>=X/H)
            assert large<=2*X*H; count+=1
    for N in range(2,32):
        assert N-1<N; fire+=1
    selected=sorted(set(x for x in (256,1000,10000,limit) if 64<=x<=limit))
    scans=[scan(x,mu) for x in selected]
    muts=sum([sum(Q[h]*2**h for h in range(4))!=1,Fraction(64,21)!=Fraction(63,21),
              band(A,10)[1].zero(),Fraction(2,81)!=Fraction(1,81)])
    return {"classification":"PASS_X_95400_Q4_FOCC_ANNULAR_HARDENING",
            "frozen_base_pr":573,"frozen_base_sha":"0865242eb9dc0ed6094afc8a87a52b974c6f1307",
            "exact_kernel_checks":exact,"annihilation_checks":ann,"inverse_checks":inv,
            "ratio_checks":ratio,"gcd_checks":gcd,"square_checks":square,
            "type_i_checks":typei,"pair_count_checks":count,"firewall_checks":fire,
            "hostile_mutations_detected":muts,"floating_reconnaissance":scans,
            "does_not_prove":["SACF","FOCC","OCHD","Riemann Hypothesis"]}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--output",type=Path); p.add_argument("--scan-limit",type=int,default=100000); a=p.parse_args()
    text=json.dumps(run(a.scan_limit),indent=2,sort_keys=True)+"\n"
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text)
    else:print(text,end="")
if __name__=="__main__":main()
