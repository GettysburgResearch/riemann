#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, math
from fractions import Fraction
from pathlib import Path

PRIMES=(2,3,5,7,11,13,17)

def q(j,m):
    if m<j: return Fraction(0)
    if m==j: return Fraction(j+1,j-1)
    if m==j+1: return -Fraction((j+1)*(j-2),j*(j-1))
    return Fraction(2,j*(j-1))

def h(j,m):
    C=Fraction(2,j*(j-1))
    if m<j: return -C
    if m==j: return Fraction(j+2,j)
    if m==j+1: return Fraction(-1)
    return Fraction(0)

def mu_squarefree_divisor(d,ps):
    count=0
    for p in ps:
        if d%p==0:
            d//=p; count+=1
    return Fraction(-1 if count%2 else 1) if d==1 else Fraction(0)

def divisors(ps):
    out=[1]
    for p in ps: out += [d*p for d in list(out)]
    return sorted(out)

def fixed_product_counterexample():
    j=3; ps=(2,3); n=24
    rows=[]; total=Fraction(0)
    for d in divisors(ps):
        if n%d: continue
        m=n//d
        s=mu_squarefree_divisor(d,ps)*q(j,m)
        rows.append((d,m,str(s)))
        total+=s
    assert total==Fraction(-1)
    assert rows==[(1,24,'1/3'),(2,12,'-1/3'),(3,8,'-1/3'),(6,4,'-2/3')]
    return rows,str(total)

def rough_identity_checks():
    checks=0
    for j in range(2,33):
        C=Fraction(2,j*(j-1))
        for r in range(0,6):
            ps=PRIMES[:r]; P=math.prod(ps) if ps else 1
            ds=divisors(ps)
            for n in range(1,401):
                direct=sum((mu_squarefree_divisor(d,ps)*q(j,n//d)
                            for d in ds if n%d==0),Fraction(0))
                rhs=C if math.gcd(n,P)==1 else Fraction(0)
                for m in range(1,j+2):
                    if n%m==0 and n//m in ds:
                        rhs += mu_squarefree_divisor(n//m,ps)*h(j,m)
                assert direct==rhs,(j,r,n,direct,rhs)
                checks+=1
    return checks

def finite_knot_scan():
    # Diagnostic only. Each row is affine in log Y between integer knots.
    global_min=1e100; arg=None; checks=0
    for j in range(2,25):
        N=1600
        base=[0.0]*(N+1)
        A=(j+1)/(j-1); B=(j+1)*(j-2)/(j*(j-1)); C=2/(j*(j-1))
        base[j]=A; base[j+1]=-B
        for n in range(j+2,N+1): base[n]=C
        for r in range(0,7):
            omega=base[:]
            for p in PRIMES[:r]:
                old=omega[:]
                for n in range(p,N+1,p): omega[n]-=old[n//p]
            mass=0.0; moment=0.0
            for n in range(1,N+1):
                a=omega[n]/math.sqrt(n)
                mass+=a; moment+=a*math.log(n)
                if n>j:
                    val=mass*math.log(n)-moment
                    if val<global_min: global_min=val; arg=(j,r,n)
                    assert val>-2e-11,(j,r,n,val)
                    checks+=1
    return checks,global_min,arg

def capacity_checks():
    checks=0
    for j in range(2,2000):
        A=Fraction(j+1,j-1); B=Fraction((j+1)*(j-2),j*(j-1)); C=Fraction(2,j*(j-1))
        assert A-B==(j+1)*C
        # square positive inequality A/sqrt(j)>B/sqrt(j+1)
        assert A*A*(j+1)>B*B*j
        checks+=2
    return checks

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path); args=ap.parse_args()
    rows,total=fixed_product_counterexample()
    knot_checks,minv,arg=finite_knot_scan()
    payload={
      'schema':'riemann.t96100.global-frontier-shadow.v1',
      'base_sha':'ca5fb69c15cda29b3b589660f9be44ea2f440677',
      'fixed_product_counterexample':{'j':3,'primes':[2,3],'n':24,'rows':rows,'total':total},
      'rough_reservoir_identity_checks':rough_identity_checks(),
      'frontier_capacity_exact_checks':capacity_checks(),
      'finite_knot_positivity_diagnostics':knot_checks,
      'finite_knot_minimum':minv,
      'finite_knot_minimum_location':arg,
      'global_transport_proved_by_replay':False,
      'rh_established_by_replay':False,
      'verdict':'PASS_GLOBAL_FRONTIER_SHADOW_HARDENING_DIAGNOSTICS',
    }
    canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(canonical).hexdigest()
    text=json.dumps(payload,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text)
    else: print(text,end='')
    print(payload['verdict']); print(payload['proof_object_sha256'])
if __name__=='__main__': main()
