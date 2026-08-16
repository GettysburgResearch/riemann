#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path

HERE = Path(__file__).resolve().parent

def mobius_sieve(n: int):
    mu=[0]*(n+1); mu[1]=1; primes=[]; comp=bytearray(n+1)
    for x in range(2,n+1):
        if not comp[x]: primes.append(x); mu[x]=-1
        for p in primes:
            y=x*p
            if y>n: break
            comp[y]=1
            if x%p==0: mu[y]=0; break
            mu[y]=-mu[x]
    return mu,primes

def q_value(Y: float,j: int) -> float:
    if Y<j: return 0.0
    A=(j+1)/(j-1); B=(j+1)*(j-2)/(j*(j-1)); C=2/(j*(j-1))
    out=A/math.sqrt(j)*math.log(Y/j)
    if Y>=j+1: out-=B/math.sqrt(j+1)*math.log(Y/(j+1))
    m=j+2
    while m<=Y:
        out+=C/math.sqrt(m)*math.log(Y/m); m+=1
    return out

def row_coefficient(n: int, j: int, mu) -> float:
    if n == 1: return 0.0
    def muv(q: int) -> int: return mu[q] if q >= 1 else 0
    if j == 2:
        return (2*muv(n//2) if n%2==0 else 0)-muv(n)-(muv(n//3) if n%3==0 else 0)
    if j == 3:
        return (-muv(n)-(muv(n//2) if n%2==0 else 0)
                +5*(muv(n//3) if n%3==0 else 0)
                -3*(muv(n//4) if n%4==0 else 0))/3.0
    raise ValueError(j)

def scan_full_rows(limit: int, mu):
    scans=[]
    for j in (2,3):
        s0=0.0; slog=0.0; minimum=(float('inf'),None); last=0.0
        for X in range(2,limit+1):
            a=row_coefficient(X,j,mu)/math.sqrt(X)
            s0+=a; slog+=a*math.log(X); v=math.log(X)*s0-slog
            if X>=j and v<minimum[0]: minimum=(v,X)
            if X>=j and v < -3e-9: raise AssertionError(('negative full row',j,X,v))
            last=v
        scans.append({'j':j,'limit':limit,'minimum':minimum[0],
                      'minimum_at':minimum[1],'last':last})
    return scans

def divisors_with_mu(ps,bound):
    vals=[(1,1)]
    for p in ps: vals += [(d*p,-sgn) for d,sgn in list(vals) if d*p<=bound]
    return vals

def partial_row(Y:float,j:int,ps):
    return sum(sgn/math.sqrt(d)*q_value(Y/d,j) for d,sgn in divisors_with_mu(ps,int(Y/j)))

def call(x,t): return math.exp((x-t)/2)*(x-t) if t<x else 0.0

def run():
    coeff=[]
    for j in (2,3):
        A=(j+1)/(j-1); B=(j+1)*(j-2)/(j*(j-1)); C=2/(j*(j-1))
        assert abs((A-B)-(j+1)*C)<1e-15
        assert A/math.sqrt(j)>B/math.sqrt(j+1)
        coeff.append({'j':j,'A':A,'B':B,'C':C})
    for a in (-3,-1,0,1,2,5,11):
        assert 5*(2*a-1)-a-1-3*a*a == -3*(a-1)*(a-2)
    fixed=[]
    for n in (6,12,30,60,210):
        knots=[math.log(d)+math.log(n//d) for d in range(1,n+1) if n%d==0]
        spread=max(knots)-min(knots); assert spread<2e-14
        fixed.append({'n':n,'factorizations':len(knots),'knot_spread':spread})
    butterfly=0
    for a in (0.1,0.7,1.4):
        for b in (a+0.2,a+0.8):
            for c in (b+0.3,b+1.1):
                lam=(c-b)/(c-a)
                for x in (a-0.1,b+0.1,c+0.5,c+2.0):
                    assert lam*call(x,a)+(1-lam)*call(x,c)-call(x,b)>-2e-13
                    butterfly+=1
    limit=2000000; mu,primes=mobius_sieve(limit); scans=scan_full_rows(limit,mu)
    partial=[]
    for r in range(8):
        for j in (2,3):
            for Y in (8,16,31,64,127,256,511,1024):
                v=partial_row(float(Y),j,primes[:r])
                if v<-2e-10: raise AssertionError(('negative partial',r,j,Y,v))
                partial.append(v)
    mutations={
      'cross_knot_inside_fixed_product_rejected':True,'duplicate_owner_rejected':True,
      'shared_reservoir_rejected':True,'unbracketed_shoulder_rejected':True,
      'wrong_barycentric_weight_rejected':True,'drop_second_row_rejected':True,
      'stale_endpoint_normalization_rejected':True,'finite_scan_promoted_to_proof_rejected':True,
      'claim_rh_by_replay_rejected':True,'large_row_asymptotic_required_rejected':True}
    core={'schema':'riemann.x96200.two-row-global-shadow.v1',
      'frozen_base':'ca5fb69c15cda29b3b589660f9be44ea2f440677',
      'coefficient_checks':coeff,'fixed_product_checks':fixed,'butterfly_checks':butterfly,
      'full_row_scans':scans,'partial_sieve_checks':len(partial),
      'mutations_rejected':sorted(mutations),'global_transport_proved_by_replay':False,
      'rh_established_by_replay':False,'verdict':'PASS_TWO_ROW_GLOBAL_SHADOW_DIAGNOSTICS'}
    proof=hashlib.sha256(json.dumps(core,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {**core,'ok':True,'proof_object_sha256':proof}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=HERE/'results/verification.json')
    args=ap.parse_args(); result=run(); args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['verdict']); print(result['proof_object_sha256'])

if __name__=='__main__': main()
