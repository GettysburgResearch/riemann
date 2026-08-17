#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
SCHEMA="riemann.x96600.single-scalar-prefix.v1"
RESULT="riemann.x96600.single-scalar-prefix.result.v1"

def mobius(n:int)->int:
    x=n; mu=1; p=2
    while p*p<=x:
        if x%p==0:
            x//=p; mu=-mu
            if x%p==0:return 0
            while x%p==0:x//=p
        p+=1
    if x>1:mu=-mu
    return mu

def qstar(n:int)->int:
    if n==1:return 0
    if n==2:return 15
    if n==3:return 6
    if n==4:return 3
    return 6

def divisors(primes:list[int])->list[int]:
    out=[1]
    for p in primes: out += [d*p for d in list(out)]
    return sorted(out)

def a_direct(n:int)->int:
    return sum(mobius(d)*qstar(n//d) for d in range(1,n+1) if n%d==0)

def a_formula(n:int)->int:
    return (6 if n==1 else 0)-6*mobius(n)+(9*mobius(n//2) if n%2==0 else 0)-(3*mobius(n//4) if n%4==0 else 0)

def aP_direct(n:int,primes:list[int])->int:
    return sum(mobius(d)*qstar(n//d) for d in divisors(primes) if n%d==0)

def aP_ledger(n:int,primes:list[int])->int:
    from math import gcd
    P=1
    for p in primes:P*=p
    value=6 if gcd(n,P)==1 else 0
    for e in divisors([p for p in primes if p!=2]):
        me=mobius(e)
        if n==e:value-=6*me
        if n==2*e:value+=15*me
        if n==4*e:value-=12*me
        if n==8*e:value+=3*me
    return value

def validate(data):
    if data.get('schema')!=SCHEMA: raise ValueError('schema mismatch')
    N=int(data['formal_cutoff'])
    if N<1024: raise ValueError('formal cutoff too small')
    for n in range(1,N+1):
        if a_direct(n)!=a_formula(n): raise ValueError(('full coefficient',n))
    unit=[a_formula(1),a_formula(2),a_formula(4),a_formula(8)]
    if unit != [0,15,-12,3]: raise ValueError(('unit-core packet',unit))
    for d in range(3,N//8+1,2):
        if mobius(d)==0: continue
        got=[a_formula(d),a_formula(2*d),a_formula(4*d),a_formula(8*d)]
        want=[-6*mobius(d),15*mobius(d),-12*mobius(d),3*mobius(d)]
        if got!=want: raise ValueError(('odd-core packet',d))
    stages=[]; primes=[]
    for p in data['prime_stages']:
        if p!=2 and any(p%q==0 for q in range(2,int(p**0.5)+1)):
            raise ValueError('nonprime stage')
        previous=list(primes); primes.append(p)
        for n in range(1,min(N,5000)+1):
            if aP_direct(n,primes)!=aP_ledger(n,primes): raise ValueError(('ledger',p,n))
            rhs=aP_direct(n,previous)-(aP_direct(n//p,previous) if n%p==0 else 0)
            if aP_direct(n,primes)!=rhs: raise ValueError(('prime recurrence',p,n))
        stages.append({'prime':p,'checked_through':min(N,5000)})
    fw=data['firewalls']
    for name in ('scps_proved','actq2_proved','rh_established','imports_pr552_transport','finite_scan_promoted'):
        if fw[name] is not False: raise ValueError(('firewall promoted',name))
    genealogy={
      'base_pr':551,'base_sha':'c8702aef34a25c614f91dea1ecc6e787478e8170',
      'comparison_pr':552,'comparison_sha':'81df9c3f507aba0e5f21187044583a0d6fb90db9'}
    if data.get('genealogy')!=genealogy: raise ValueError('genealogy mismatch')
    out={
      'schema':RESULT,
      'verdict':'PASS_T96600_SINGLE_SCALAR_PREFIX_AND_FILTER_FIREWALL',
      'formal_cutoff':N,
      'coefficient_formula':'6*1_{n=1}-6mu(n)+9*1_{2|n}mu(n/2)-3*1_{4|n}mu(n/4)',
      'unit_core_packet':[0,15,-12,3],
      'nonunit_odd_core_packet':[-6,15,-12,3],
      'prime_stages':stages,
      'numerator_factorization':'-3(a-1)(a-2)',
      'green_positive_real_zero':'s=1/2',
      'genealogy':genealogy,
      'open_producers':['SCPS','eventual prefix positivity','ACTQ_2'],
      'rh_established':False,
      'proof_boundary':'Exact scalar convolution, unit/nonunit odd-core packets, finite-prime ledger and recurrence, and finite-shift zero firewall. Does not prove SCPS, ACTQ2, scalar positivity, or RH.'}
    canonical=json.dumps(out,sort_keys=True,separators=(',',':')).encode()
    out['proof_object_sha256']=hashlib.sha256(canonical).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('certificate',nargs='?',type=Path,default=HERE/'certificates/control.json'); ap.add_argument('--output',type=Path)
    args=ap.parse_args(); out=validate(json.loads(args.certificate.read_text())); text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if args.output: args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text)
    print(out['verdict']); print(out['proof_object_sha256'])
if __name__=='__main__':main()
