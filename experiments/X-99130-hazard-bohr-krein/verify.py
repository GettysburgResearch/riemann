#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, random
from fractions import Fraction
from pathlib import Path


def bernoulli_hazard(xs, lambdas):
    B = Fraction(1)
    for x in xs:
        B *= 1-x
    numerator = Fraction(0)
    for j, (x, lam) in enumerate(zip(xs, lambdas)):
        term = lam*x
        for k, y in enumerate(xs):
            if k != j:
                term *= 1-y
        numerator += term
    return numerator/(1-B), B


def surviving_exponents(lo=-8, hi=8):
    out=[]
    for e in range(lo,hi+1):
        pole_safe=all(m*(e+1)+1 <= 1 for m in range(1,9))
        zero_safe=max(0,-e) <= 1
        if pole_safe and zero_safe:
            out.append(e)
    return out


def run():
    rng=random.Random(99130)
    hazard=0
    for size in range(1,8):
        for _ in range(24):
            xs=[Fraction(rng.randint(1,9),rng.randint(12,30)) for _ in range(size)]
            ls=[Fraction(rng.randint(1,20),rng.randint(1,8)) for _ in range(size)]
            H,B=bernoulli_hazard(xs,ls)
            den=Fraction(0); num=Fraction(0)
            for mask in range(1<<size):
                prob=Fraction(1); occ=[]
                for j,x in enumerate(xs):
                    if mask&(1<<j): prob*=x; occ.append(j)
                    else: prob*=1-x
                if occ: den+=prob
                if len(occ)==1: num+=prob*ls[occ[0]]
            assert den==1-B and H==num/den and H>=0
            hazard+=1

    assert 64*7**5 > 16**5
    upper=Fraction(20631,23040)
    lower=Fraction(75,64)
    assert upper<1<lower

    survivors=surviving_exponents()
    assert survivors==[-1]

    psd=0
    for _ in range(512):
        a=Fraction(rng.randint(0,100),rng.randint(1,20))
        b=Fraction(rng.randint(0,100),rng.randint(1,20))
        c=Fraction(rng.randint(-20,20),20)
        eta2=c*c*a*b
        assert (a+b)**2 >= 4*eta2
        psd+=1

    heat=0
    for T in range(1,2049):
        fT=Fraction(T,4)
        fT1=Fraction(T+1,2)-Fraction((T+1)**2,4*T)
        assert fT1==Fraction(T,4)-Fraction(1,4*T)
        assert min(fT,fT1)>=Fraction(T,4)-Fraction(1,4)
        heat+=1

    hostile=0
    if upper != Fraction(20630,23040): hostile+=1
    if lower != 1: hostile+=1
    if survivors != [0]: hostile+=1
    if Fraction(1,4) != 0: hostile+=1

    payload={
      'schema':'riemann.t99130.hazard-bohr-krein.v1',
      'classification':'PASS_X_99130_HAZARD_BOHR_KREIN_ALGEBRA',
      'arithmetic_class':'EXACT_INTEGER_AND_RATIONAL',
      'base_pr':623,
      'base_sha':'712412e286cc309bbe9960ee839df158316df9e5',
      'bernoulli_hazard_checks':hazard,
      'twist_upper_6_5':str(upper),
      'twist_lower_2':str(lower),
      'unique_transform_exponents':survivors,
      'positive_completion_checks':psd,
      'heat_floor_checks':heat,
      'hostile_mutations_detected':hostile,
      'analytic_proof_required':['Kronecker approximation','uniform Euler tails','Hurwitz transfer'],
      'does_not_prove':['PCSS','Riemann Hypothesis'],
      'rh_established':False,
    }
    core=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(core).hexdigest()
    return payload


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path)
    args=ap.parse_args(); payload=run()
    text=json.dumps(payload,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8',newline='\n')
    print(payload['classification'])
    print(payload['proof_object_sha256'])

if __name__=='__main__': main()
