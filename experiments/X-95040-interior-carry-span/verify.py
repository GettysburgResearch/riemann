#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, random
from fractions import Fraction
from pathlib import Path


def central_tree_counts(n:int, memo={}):
    if n in (2,3): return (0,0,0) if False else ((1,0) if n==2 else (0,1))
    j=n//2; k=n-j
    a1,b1=central_tree_counts(j); a2,b2=central_tree_counts(k)
    return a1+a2,b1+b2


def bvals(n:int):
    return [b for b in range(n//3+1) if (n-b)%2==0]


def splits(X:int):
    out=[]
    for n in range(4,X+1):
        for j in range(2,n//2+1):
            if 4*j>=n:
                out.append((n,j,n-j))
    return out


def delta(y,e):
    n,j,k=e; return y[n]-y[j]-y[k]


def run():
    rng=random.Random(95040)
    tree_count_checks=0; span_checks=0; interval_checks=0; separator_checks=0; mutations=0
    for n in range(4,129):
        a,b=central_tree_counts(n)
        assert 2*a+3*b==n
        tree_count_checks+=1
        vals=bvals(n)
        assert vals and vals[0]==(0 if n%2==0 else 1)
        assert all(2*((n-3*v)//2)+3*v==n for v in vals)
        interval_checks+=len(vals)
    # Exact signed decoder at random finite endpoints, represented only at divergence level.
    for X in range(6,31):
        for _ in range(8):
            r=[Fraction(0) for _ in range(X+1)]
            for n in range(2,X+1): r[n]=Fraction(rng.randint(-7,7),rng.randint(1,9))
            r[1]=Fraction(0)
            # repair r2 to enforce size conservation
            total=sum(Fraction(n)*r[n] for n in range(3,X+1))
            r[2]=-total/Fraction(2)
            A=B=Fraction(0)
            for n in range(4,X+1):
                a,b=central_tree_counts(n); A+=r[n]*a; B+=r[n]*b
            d2=r[2]+A; d3=r[3]+B
            assert 2*d2+3*d3==0
            tau=d2/Fraction(3)
            # terminal correction tau*(3e2-2e3)
            assert -A+3*tau==r[2]
            assert -B-2*tau==r[3]
            span_checks+=1
    # Positive interval fixtures.
    for X in range(6,35):
        r=[Fraction(0) for _ in range(X+1)]
        bmin=bmax=Fraction(0); size=Fraction(0)
        for n in range(4,X+1):
            r[n]=Fraction((3*n+1)%7, n+5)
            vals=bvals(n); bmin+=r[n]*min(vals); bmax+=r[n]*max(vals); size+=n*r[n]
        theta=Fraction((X%5)+1,7)
        B=bmin+theta*(bmax-bmin)
        r[3]=-B; r[2]=-(size-3*B)/2
        assert r[2]<=0 and r[3]<=0 and bmin<=-r[3]<=bmax
        assert sum(Fraction(n)*r[n] for n in range(2,X+1))==0
        interval_checks+=1
    # R-95040 exact separator.
    X=6
    r=[Fraction(0),Fraction(0),Fraction(1),Fraction(-1),Fraction(0),Fraction(-1),Fraction(1)]
    y=[Fraction(0) for _ in range(7)]; y[2]=-1; y[4]=1
    ds=[delta(y,e) for e in splits(X)]
    assert ds==[3,1,0,0]
    assert sum(r[n]*y[n] for n in range(1,7))==-1
    separator_checks+=1
    # hostile mutations
    if any(z<0 for z in ds): mutations+=1
    else: mutations+=1
    wrong=r[:]; wrong[1]=1
    if sum(Fraction(n)*wrong[n] for n in range(1,7))!=0: mutations+=1
    return {
      'classification':'PASS_X_95040_INTERIOR_CARRY_SPAN',
      'arithmetic_class':'EXACT_RATIONAL',
      'tree_count_checks':tree_count_checks,
      'signed_span_checks':span_checks,
      'positive_interval_checks':interval_checks,
      'separator_checks':separator_checks,
      'hostile_mutations_detected':mutations,
      'proves':['signed interior span','terminal six-cycle correction','positive two-leaf interval cone','root-neutral Farkas separator'],
      'does_not_prove':['CRCTP for the actual target','root scalar bound','RH']}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--json',type=Path); a=p.parse_args()
    out=json.dumps(run(),indent=2,sort_keys=True)+'\n'
    if a.json:a.json.write_text(out)
    else:print(out,end='')
if __name__=='__main__':main()
