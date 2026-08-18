#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction
from pathlib import Path


def binom(a: Fraction, k: int) -> Fraction:
    out=Fraction(1)
    for j in range(k):
        out*=a-j
        out/=j+1
    return out


def one_minus_x(a: Fraction, k: int) -> Fraction:
    return (-1)**k*binom(a,k)


def odd_ghalf(k: int) -> Fraction:
    return Fraction(math.comb(2*k,k),4**k)


def two_ghalf(k: int) -> Fraction:
    return sum(odd_ghalf(j)*Fraction(1,2)**j for j in range(k+1))


def two_bhalf(k: int) -> Fraction:
    vals=[one_minus_x(Fraction(1,2),j)*Fraction(1,2)**j for j in range(k+1)]
    return vals[k]-(vals[k-1] if k else 0)


def factor(n: int):
    out=[]; p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0: n//=p; e+=1
            out.append((p,e))
        p+=1
    if n>1: out.append((n,1))
    return out


def ghalf(n: int) -> Fraction:
    out=Fraction(1)
    for p,e in factor(n): out*=two_ghalf(e) if p==2 else odd_ghalf(e)
    return out


def bhalf(n: int) -> Fraction:
    out=Fraction(1)
    for p,e in factor(n): out*=two_bhalf(e) if p==2 else one_minus_x(Fraction(1,2),e)
    return out


def conv(a,b,n):
    return sum(a[d]*b[n//d] for d in range(1,n+1) if n%d==0)


def mobius(n: int) -> int:
    mu=1
    for _,e in factor(n):
        if e>1: return 0
        mu=-mu
    return mu


def semigroup_numbers(P, x):
    vals=[1]
    for p in P:
        old=list(vals)
        for v in old:
            q=v*p
            while q<=x:
                vals.append(q); q*=p
    return sorted(set(vals))


def check_tao(P,x):
    S=semigroup_numbers(P,x)
    N=len(S); H=sum(Fraction(1,n) for n in S)
    Ncomp=sum(1 for n in range(1,x+1) if all(n%p for p in P))
    A=sum(Fraction(mobius(n),n) for n in S)
    C=Fraction(N+Ncomp, x)-H/Fraction(x)
    assert C+A>=0 and C-A>=0 and C<=1
    E=x*A-Ncomp
    E2=sum(Fraction(mobius(n)*(x%n),n) for n in S if mobius(n))
    assert E==E2
    for n in S:
        if mobius(n): assert abs(Fraction(x%n,n))<=1-Fraction(1,n)
    return A,C


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    N=512
    gh={n:ghalf(n) for n in range(1,N+1)}
    bh={n:bhalf(n) for n in range(1,N+1)}
    Q={n:(gh[n]+bh[n])/2 for n in range(1,N+1)}
    S={n:(gh[n]-bh[n])/2 for n in range(1,N+1)}
    assert all(Q[n]>=0 and S[n]>=0 for n in range(1,N+1))
    # B coefficients are the exact finite Euler tensor.
    b={}
    for n in range(1,N+1):
        e=0; m=n
        while m%2==0: m//=2; e+=1
        b2=[Fraction(1),Fraction(-5,2),Fraction(2),Fraction(-1,2)]
        b[n]=(b2[e] if e<len(b2) else 0)*mobius(m)
    # 1-B = 2 S * (Q-S) = 2 S * B^(1/2)
    for n in range(1,N+1):
        lhs=(Fraction(1) if n==1 else 0)-b[n]
        rhs=2*conv(S,bh,n)
        assert lhs==rhs
    tao=[]
    for P,x in [([3],26),([3,5],80),([3,5,7],160),([2,3,5],96),([3,5,7,11,13],26)]:
        A,C=check_tao(P,x); tao.append({'P':P,'x':x,'A':str(A),'C':str(C)})
    # Heat and rate algebra.
    assert Fraction(96,1)*Fraction(1,1000) < Fraction(1,10)
    delta=Fraction(1,5); theta=Fraction(1,10000)
    assert 96*theta < delta*delta/2
    # Main-canceling positive-filter negative control at the first dyadic factor.
    filtered4=S[4]-2*S[2]
    assert filtered4<0
    payload={
      'schema':'riemann.t98700.fractional-julia-hermite.v1',
      'base_sha':'edf28c9ad14ccbf5b18b9ced45f3c2fc4ce8221d',
      'fractional_coefficients_checked':N,
      'minimum_Q':str(min(Q.values())),
      'minimum_S':str(min(S.values())),
      'tao_fixtures':tao,
      'factorization_checks':N,
      'finite_positive_filter_firewall_n4':str(filtered4),
      'theta_delta_rate_fixture':{'delta':str(delta),'theta':str(theta)},
      'rh_established':False,
      'verdict':'PASS_T98700_FRACTIONAL_JULIA_TAO_HERMITE_ALGEBRA'
    }
    core=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(core).hexdigest()
    text=json.dumps(payload,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text)
    print(payload['verdict']); print(payload['proof_object_sha256'])

if __name__=='__main__': main()
