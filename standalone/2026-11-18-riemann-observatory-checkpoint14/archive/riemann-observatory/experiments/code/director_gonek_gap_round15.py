#!/usr/bin/env python3
"""Rational enclosure of Gonek's gap integral at 19/10; no RH input."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json


def arctan_bounds(q, terms=80):
    total = sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(terms)), F(0))
    following = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(total,total+following), max(total,total+following)


def decimal_outward(x, places, up=False):
    scale=10**places
    v=x.numerator*scale//x.denominator
    if up and F(v,scale)<x: v+=1
    sign='-' if v<0 else ''
    v=abs(v)
    return f'{sign}{v//scale}.{v%scale:0{places}d}'


def main():
    a,b=arctan_bounds(5)
    c,d=arctan_bounds(239)
    pi_lo,pi_hi=16*a-4*d,16*b-4*c
    beta=F(19,10)
    lo=hi=F(0)
    for j in range(41):
        factor=F(2, factorial(2*j+2)*(2*j+1))
        x,y=factor*(pi_lo*beta)**(2*j),factor*(pi_hi*beta)**(2*j)
        if j%2: lo-=y;hi-=x
        else: lo+=x;hi+=y
    # All tail terms decrease: pi*beta<6 and ratio <36/(2j+3)^2.
    assert pi_hi*beta<6
    tail=F(2,factorial(84)*83)*(pi_hi*beta)**82
    # j=41 is negative; the alternating tail lies in [-tail,0].
    exact_lo=beta*(1-hi)
    exact_hi=beta*(1-lo+tail)
    assert F('0.99726619997764485')<exact_lo<exact_hi<F('0.99726619997764486')
    assert exact_hi<1
    source=Path(__file__).resolve()
    result=dict(status='PASS',beta='19/10',method='Exact fractions, Machin arctangent bounds, interval evaluation and alternating tail',
                arctan_terms=80,series_last_index=40,first_tail_index=41,
                pi_lower=decimal_outward(pi_lo,100),pi_upper=decimal_outward(pi_hi,100,True),
                gap_integral_lower=decimal_outward(exact_lo,50),
                gap_integral_upper=decimal_outward(exact_hi,50,True),
                conclusion='F(1.9)<1. The gap implication additionally uses the RH theorem and the repaired bulk covering argument.',
                code_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
    target=source.parents[1]/'results/director_gonek_gap_round15.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
