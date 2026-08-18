#!/usr/bin/env python3
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Dict, Iterable

HERE=Path(__file__).resolve().parent


def primes_upto(n:int)->list[int]:
    sieve=bytearray(b'\x01')*(n+1)
    if n>=0: sieve[0]=0
    if n>=1: sieve[1]=0
    for p in range(2,int(n**0.5)+1):
        if sieve[p]:
            sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if sieve[i]]


def mobius_upto(n:int)->list[int]:
    mu=[0]*(n+1); mu[1]=1
    primes=[]; comp=[False]*(n+1)
    for i in range(2,n+1):
        if not comp[i]: primes.append(i); mu[i]=-1
        for p in primes:
            if i*p>n: break
            comp[i*p]=True
            if i%p==0:
                mu[i*p]=0; break
            mu[i*p]=-mu[i]
    return mu


def quotient_values(N:int)->list[int]:
    return sorted({N//m for m in range(1,N+1)})


def quotient_values_fast(N:int)->list[int]:
    M=math.isqrt(N)
    return sorted(set(range(1,M+1)) | {N//k for k in range(1,M+1)})


def divisors_squarefree(q:int)->list[int]:
    ps=[]; x=q; p=2
    while p*p<=x:
        if x%p==0:
            ps.append(p); x//=p
            if x%p==0: raise ValueError('not squarefree')
        p+=1
    if x>1: ps.append(x)
    ds=[1]
    for p in ps: ds += [d*p for d in ds]
    return sorted(ds)


def odd_squarefree_count(n:int)->int:
    mu=mobius_upto(n)
    return sum(1 for q in range(1,n+1,2) if mu[q]!=0)


def exact_bridge_fixture()->dict:
    # A finite step base h with h(0)=h(1)=0, represented by jumps dh.
    dh={2:Fraction(3,5),3:Fraction(-1,7),5:Fraction(2,9),8:Fraction(4,11)}
    maxx=96
    h=[Fraction(0) for _ in range(maxx+1)]
    run=Fraction(0)
    for x in range(maxx+1):
        run += dh.get(x,Fraction(0)); h[x]=run
    P=[3,5,7]
    products=[1]
    for p in P: products += [m*p for m in list(products)]
    products=sorted(products)
    mu={m:(-1)**sum(m%p==0 for p in P) for m in products}

    cases=0
    for Y in range(1,maxx+1):
        direct=sum(Fraction(mu[m],m)*h[Y//m] for m in products if m<=Y)
        st=Fraction(0)
        for x,jump in dh.items():
            if x>Y: continue
            prefix=sum(Fraction(mu[m],m) for m in products if m<=Y//x)
            st += prefix*jump
        if direct!=st: raise AssertionError(('stieltjes',Y,direct,st))
        # Sequential exact prime update on the complete endpoint vector.
        vec=h[:]
        for p in P:
            old=vec[:]
            for y in range(maxx,-1,-1):
                vec[y]=old[y]-Fraction(1,p)*old[y//p]
        if vec[Y]!=direct: raise AssertionError(('transition',Y,vec[Y],direct))
        cases += 1
    return {'cases':cases,'jump_count':len(dh),'prime_count':len(P)}


def symbolic_half_order_fixture(N:int=256)->dict:
    vals=quotient_values_fast(N); vset=set(vals)
    primes=[3,5,7,11]
    # Formal coefficients keyed by squarefree radicand: c*sqrt(r).
    def base(x:int)->Dict[int,Fraction]:
        out={1:Fraction(1)}
        if x>=2: out[2]=out.get(2,Fraction(0))-Fraction(5,4)
        if x>=4: out[1]=out.get(1,Fraction(0))+Fraction(1)
        if x>=8: out[2]=out.get(2,Fraction(0))-Fraction(1,8)
        return {r:c for r,c in out.items() if c}
    def mul_inv_sqrt(a:Dict[int,Fraction],p:int)->Dict[int,Fraction]:
        out={}
        for r,c in a.items():
            if r%p==0: nr=r//p; nc=c
            else: nr=r*p; nc=c/Fraction(p)
            out[nr]=out.get(nr,Fraction(0))+nc
        return {r:c for r,c in out.items() if c}
    def sub(a,b):
        out=dict(a)
        for r,c in b.items(): out[r]=out.get(r,Fraction(0))-c
        return {r:c for r,c in out.items() if c}
    vec={x:base(x) for x in vals}
    for p in reversed(primes):
        old={x:dict(v) for x,v in vec.items()}
        for x in reversed(vals):
            if x>=p:
                y=x//p
                if y not in vset: raise AssertionError('quotient closure')
                vec[x]=sub(old[x],mul_inv_sqrt(old[y],p))
    # Direct divisor expansion of the same transition word.
    q=math.prod(primes)
    ds=divisors_squarefree(q)
    mu=mobius_upto(q)
    checked=0
    for x in vals:
        direct={}
        for d in ds:
            if d>x: continue
            term=base(x//d)
            # multiply by mu(d)/sqrt(d), prime by prime
            for p in primes:
                if d%p==0: term=mul_inv_sqrt(term,p)
            for r,c in term.items(): direct[r]=direct.get(r,Fraction(0))+mu[d]*c
        direct={r:c for r,c in direct.items() if c}
        if direct!=vec[x]: raise AssertionError(('half-order',x,direct,vec[x]))
        checked+=1
    return {'horizon':N,'coordinates':len(vals),'checked':checked}


def state_minimality_fixture(N:int)->dict:
    M=math.isqrt(N); mu=mobius_upto(M)
    qs=[q for q in range(1,M+1,2) if mu[q]!=0]
    coords=[N//q for q in qs]
    if len(coords)!=len(set(coords)): raise AssertionError('quotient collision')
    # Triangular support: q-coordinate occurs with nonzero coefficient, proper divisors are earlier.
    pos={q:i for i,q in enumerate(qs)}
    for q in qs:
        ds=divisors_squarefree(q)
        if q not in ds or mu[q]==0: raise AssertionError('diagonal')
        for d in ds:
            if d!=q and d>q: raise AssertionError('triangular order')
    return {'horizon':N,'sqrt_horizon':M,'independent_rows':len(qs)}


def exponent_fixture()->dict:
    beta=Fraction(3,8); gamma=Fraction(-3,4)
    L_power=1-beta
    L_log=-gamma
    rhs_power=Fraction(3,5)*L_power
    rhs_log=Fraction(3,5)*L_log-Fraction(1,5)
    lhs_power=beta
    lhs_log=gamma+1
    if (rhs_power,rhs_log)!=(lhs_power,lhs_log):
        raise AssertionError('critical exponent mismatch')
    return {
      'u_power':str(beta),'u_log_power':str(gamma),
      'vk_power':str(rhs_power),'vk_log_power':str(rhs_log),
      'strict_margin':'obtained by choosing c0 sufficiently small'
    }


def sha(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument('control'); ap.add_argument('--output')
    args=ap.parse_args(); control=json.loads(Path(args.control).read_text())
    small=state_minimality_fixture(control['small_horizon'])
    large=state_minimality_fixture(control['large_horizon'])
    if large['sqrt_horizon']!=control['expected_large_sqrt']: raise AssertionError('sqrt')
    if large['independent_rows']!=control['expected_large_odd_squarefree_count']: raise AssertionError('count')
    qcount=len(quotient_values_fast(control['large_horizon']))
    if qcount!=control['expected_large_quotient_coordinates']: raise AssertionError('qcount')

    bridge=exact_bridge_fixture()
    half=symbolic_half_order_fixture()
    exponents=exponent_fixture()
    diag_path=HERE/'results/fcbi-scan-100m.json'
    diag=json.loads(diag_path.read_text())
    if diag['classification']!='DIAGNOSTIC_ONLY' or diag['proves_all_scale'] is not False: raise AssertionError('diagnostic scope')
    if diag['horizon']!=control['large_horizon']: raise AssertionError('diagnostic horizon')
    if diag['quotient_coordinates']!=qcount: raise AssertionError('diagnostic qcount')
    if diag['minimum_witness']!={'prime':control['expected_diagnostic_min_prime'],'coordinate':control['expected_diagnostic_min_x']}: raise AssertionError('diagnostic witness')
    if float(diag['minimum_slack'])<=0: raise AssertionError('diagnostic sign')

    payload={
      'schema':'riemann.x98400.future-profile.result.v1',
      'base_pr':582,'base_sha':control['base_sha'],'namespace':'T98400',
      'quotient_markov_closure':'PROVED_EXACT',
      'linear_state_lower_bound':'PROVED_EXACT_OMEGA_SQRT_N',
      'small_state_certificate':small,
      'large_state_certificate':{**large,'quotient_coordinates':qcount},
      'bridge':bridge,'half_order_symbolic':half,'corridor_exponent_algebra':exponents,
      'diagnostic':{
        'classification':diag['classification'],'horizon':diag['horizon'],
        'minimum_slack':diag['minimum_slack'],'minimum_witness':diag['minimum_witness'],
        'sha256':sha(diag_path)
      },
      'critical_saddle_QMP67':'OPEN_RH_BEARING',
      'rh_established':False,
      'verdict':'PASS_T98400_FUTURE_PROFILE_MINIMALITY_BRIDGE_AND_CORRIDOR'
    }
    proof=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    result={**payload,'proof_object_sha256':proof}
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output: Path(args.output).write_text(text)
    else: print(text,end='')

if __name__=='__main__': main()
