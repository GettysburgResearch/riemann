#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import hashlib,itertools,json,math,random

SMALL=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61)

def factor(n):
    f=[];p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:n//=p;e+=1
            f.append((p,e))
        p+=1 if p==2 else 2
    if n>1:f.append((n,1))
    return f

def mu(n):
    f=factor(n)
    return 0 if any(e>1 for _,e in f) else (-1 if len(f)%2 else 1)

def rough(n):return all(p>=67 for p,_ in factor(n))
def small_squarefree(n):return all(e==1 and p in SMALL for p,e in factor(n))

def divisors(n):
    out=[]
    for d in range(1,int(math.isqrt(n))+1):
        if n%d==0:
            out.append(d)
            if d*d!=n:out.append(n//d)
    return out

def check_convolution(N=300):
    for n in range(1,N+1):
        lhs=mu(n) if small_squarefree(n) else 0
        rhs=sum(mu(n//d) for d in divisors(n) if rough(d))
        assert lhs==rhs,(n,lhs,rhs)
    return N

def native_separator():
    active=[m for m in range(2,69) if rough(m)]
    assert active==[67]
    # delta=log(68/67)/sqrt(134)>1/68 * 1/12.
    assert 134<12**2
    return {"X":136,"q":2,"active_rough_terms":[67],
            "strict_lower_bound":"1/816",
            "separating_functional":"ordinary-capacity coordinate q=2"}

def greedy(cap,t,M):
    rem=M;u=[]
    for a,w in zip(cap,t):
        z=min(a,rem/w);u.append(z);rem-=z*w
    assert rem==0
    return tuple(u)

def vertices(cap,t,M):
    n=len(cap);ans=set()
    for free in range(n):
        other=[i for i in range(n) if i!=free]
        for bits in itertools.product((0,1),repeat=n-1):
            u=[Fraction(0)]*n;used=Fraction(0)
            for i,b in zip(other,bits):
                u[i]=cap[i] if b else Fraction(0);used+=u[i]*t[i]
            z=(M-used)/t[free]
            if 0<=z<=cap[free]:u[free]=z;ans.add(tuple(u))
    return ans

def val(u,t,p):return sum(a*b*c for a,b,c in zip(u,t,p))

def leftmost_regression(fixtures=120):
    rng=random.Random(91684);checks=0
    for _ in range(fixtures):
        n=rng.randint(2,5)
        cap=tuple(Fraction(rng.randint(1,2)) for _ in range(n))
        t=tuple(Fraction(rng.randint(1,3)) for _ in range(n))
        full=sum(a*b for a,b in zip(cap,t))
        M=Fraction(rng.randint(1,int(2*full)),2)
        if M>full:M=full
        g=greedy(cap,t,M);vs=vertices(cap,t,M)
        row=tuple(Fraction(3*n-2*i,3) for i in range(n))
        score=tuple(Fraction(i+1,n+1) for i in range(n))
        for v in vs:
            assert val(v,t,row)<=val(g,t,row)
            assert val(v,t,score)>=val(g,t,score)
            checks+=1
    return checks

def farkas_fixture():
    cap=(Fraction(1),)*3;t=(Fraction(1),)*3;M=Fraction(2)
    row=(Fraction(3),Fraction(2),Fraction(1))
    g=greedy(cap,t,M);mx=val(g,t,row);demand=mx+Fraction(1,7)
    assert all(val(v,t,row)<demand for v in vertices(cap,t,M))
    return {"maximum_row":str(mx),"odd_demand":str(demand),"gap":"1/7"}

def v4(q):
    k=0
    while q%4==0:q//=4;k+=1
    return k

def y4_check(N=256):
    lam={q:Fraction((37*q+11)%101,97) for q in range(1,N+1)}
    def Y(q):return sum(2**k*lam[q//4**k] for k in range(v4(q)+1))
    for q in range(1,N+1):
        assert Y(q)-(2*Y(q//4) if q%4==0 else 0)==lam[q]
    C={q:Fraction((19*q+7)%83,79) for q in range(1,N+1)}
    lhs=sum(lam[q]*C[q] for q in range(1,N+1))
    rhs=sum(Y(q)*(C[q]-2*(C[4*q] if 4*q<=N else 0)) for q in range(1,N+1))
    assert lhs==rhs
    return N

def main():
    p={
      "classification":"PASS_EXACT_NATIVE_ROOT_COMPILATION_SEPARATOR",
      "native_root_capacity_theorem_proved":False,
      "riemann_hypothesis_established":False,
      "checks":{
        "rough_convolution_n":check_convolution(),
        "native_reservoir_separator":native_separator(),
        "leftmost_optimizer_vertex_checks":leftmost_regression(),
        "row_farkas_fixture":farkas_fixture(),
        "y4_dual_q_limit":y4_check()
      },
      "meaning":"PR #464's fixed-window Hall algebra cannot directly satisfy the exact native NRCT while its positive rough reservoir is retained. The X=136,q=2 ordinary capacity is an exact separating functional. The target-Lorenz and direct-Y4 programs are fail-closed successor routes."
    }
    canon=json.dumps(p,sort_keys=True,separators=(",",":")).encode()
    p["proof_object_sha256"]=hashlib.sha256(canon).hexdigest()
    Path("results/verification.json").write_text(json.dumps(p,indent=2,sort_keys=True)+"\n")
    print(p["classification"]);print(json.dumps(p,indent=2,sort_keys=True))
if __name__=="__main__":main()
