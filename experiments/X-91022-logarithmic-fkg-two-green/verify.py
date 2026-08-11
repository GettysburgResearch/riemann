#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path


def prime_factors(n:int)->list[int]:
    out=[]; m=n; p=2
    while p*p<=m:
        if m%p==0:
            out.append(p)
            while m%p==0: m//=p
        p += 1 if p==2 else 2
    if m>1: out.append(m)
    return out


def is_prime(n:int)->bool:
    return n>=2 and prime_factors(n)==[n]


def F(n:int,s:int)->Fraction:
    z=Fraction(1)
    for p in prime_factors(n):
        z*=Fraction(p**s-1,p**s)
    return z


def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--json',type=Path); args=ap.parse_args()
    checks=0
    minimum_gap=None; minimum_nontrivial=None
    selected={}
    for s in [1,2,3,4]:
        H=Fraction(0); A=Fraction(0); P=Fraction(1)
        for N in range(1,501):
            H+=Fraction(1,N)
            A+=F(N,s)/N
            if is_prime(N):
                P*=Fraction(N**(s+1)-1,N**(s+1))
            gap=A-H*P
            assert gap>=0
            if minimum_gap is None or gap<minimum_gap: minimum_gap=gap
            if N>1 and (minimum_nontrivial is None or gap<minimum_nontrivial): minimum_nontrivial=gap
            checks+=1
            if N in [2,10,100,500]:
                selected[f's={s},N={N}']={
                    'conditional_expectation':str(A/H),
                    'unconditioned_product':str(P),
                    'gap':str(gap),
                }
    # Exact divisor-expansion identity F_s(n)=sum_(d|n) mu(d)d^-s.
    def mobius(n:int)->int:
        fs=prime_factors(n)
        m=n
        for p in fs:
            if m%(p*p)==0:return 0
        return -1 if len(fs)%2 else 1
    for s in [1,2,3]:
        for n in range(1,301):
            rhs=sum(Fraction(mobius(d),d**s) for d in range(1,n+1) if n%d==0)
            assert rhs==F(n,s)
            checks+=1
    result={
        'classification':'PASS_LOGARITHMIC_INTEGER_FKG_TWO_GREEN',
        'checks':checks,
        'minimum_exact_gap_including_N1':str(minimum_gap),
        'minimum_exact_nontrivial_gap':str(minimum_nontrivial),
        'selected_exact_controls':selected,
        'scope':'finite exact arithmetic controls only; Harris-FKG and Bernstein transfer remain written proofs, and RH is not claimed',
    }
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True); args.json.write_text(text)
    else: print(text,end='')
    print('PASS_LOGARITHMIC_INTEGER_FKG_TWO_GREEN')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
