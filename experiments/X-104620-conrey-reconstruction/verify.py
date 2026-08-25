#!/usr/bin/env python3
"""Exact rational replay for T-104620.

The replay evaluates Conrey's finite variational functional at four explicit
admissible test functions. It uses Fraction arithmetic throughout. The only
transcendental bounds are proved by Taylor series with an explicit geometric
tail.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path

Q = Fraction


def add(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out


def scale(a: list[Q], c: Q) -> list[Q]:
    return [c*x for x in a]


def mul(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out


def power(a: list[Q], n: int) -> list[Q]:
    out = [Q(1)]
    for _ in range(n): out = mul(out, a)
    return out


def derivative(a: list[Q]) -> list[Q]:
    return [Q(i)*a[i] for i in range(1, len(a))] if len(a)>1 else [Q(0)]


def exp_bounds(x: Q, terms: int = 96) -> tuple[Q,Q]:
    assert x >= 0
    term = total = Q(1)
    for k in range(1, terms+1):
        term *= x/k
        total += term
    first = term*x/(terms+1)
    ratio = x/(terms+2)
    assert ratio < 1
    return total, total + first/(1-ratio)


def integral_monomial_affine(n: int) -> tuple[Q,Q]:
    """Return (a,b) with int_0^1 x^n exp(2x) dx = a exp(2)+b."""
    a,b = Q(1,2),Q(-1,2)
    for k in range(1,n+1):
        a,b = Q(1,2)-Q(k,2)*a, -Q(k,2)*b
    return a,b


def affine_integral(poly: list[Q]) -> tuple[Q,Q]:
    a=b=Q(0)
    for n,c in enumerate(poly):
        an,bn=integral_monomial_affine(n)
        a += c*an; b += c*bn
    return a,b


def eval_affine_interval(a: Q,b: Q,elo: Q,ehi: Q) -> tuple[Q,Q]:
    return (a*elo+b,a*ehi+b) if a>=0 else (a*ehi+b,a*elo+b)


def square_integral_interval(poly: list[Q],elo: Q,ehi: Q) -> tuple[Q,Q]:
    a,b=affine_integral(mul(poly,poly))
    return eval_affine_interval(a,b,elo,ehi)


def sqrt_upper(x: Q, scale_den: int = 10**12) -> Q:
    assert x>=0
    target=(x.numerator*scale_den*scale_den+x.denominator-1)//x.denominator
    n=isqrt(target)
    if n*n<target: n+=1
    out=Q(n,scale_den)
    assert out*out>=x
    return out


def certificate(m: int, perturb: Q, defect: Q) -> None:
    # phi=1-x+perturb*x(1-x)(1-2x)
    phi=[Q(1),Q(-1)]
    if perturb:
        h=mul([Q(0),Q(1)],mul([Q(1),Q(-1)],[Q(1),Q(-2)]))
        phi=add(phi,scale(h,perturb))

    # Verify phi(x)+phi(1-x)=1, equivalent to the derivative symmetry.
    reflected=[Q(0)]*len(phi)
    for k,c in enumerate(phi):
        for j in range(k+1):
            reflected[j]+=c*Q(comb(k,j))*((-1)**j)
    assert add(phi,reflected)==[Q(1)]
    assert sum(phi)==0

    q=mul(phi,power([Q(1),Q(-2)],m))
    qp=derivative(q)
    elo,ehi=exp_bounds(Q(2))
    plo,phi_hi=square_integral_interval(q,elo,ehi)
    slo,shi=square_integral_interval(qp,elo,ehi)
    assert plo>0

    nlo=slo-1-phi_hi
    nhi=shi-1-plo
    assert nlo>0
    a2lo=nlo/(4*phi_hi)
    a2hi=nhi/(4*plo)
    assert a2lo>0

    ahi=sqrt_upper(a2hi)
    e2a_lo,_=exp_bounds(2*ahi)
    coth_hi=(e2a_lo+1)/(e2a_lo-1)
    f_hi=Q(1,2)+2*phi_hi*ahi*coth_hi
    edef_lo,_=exp_bounds(defect)
    assert f_hi<edef_lo


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("output",nargs="?",type=Path)
    args=parser.parse_args()

    certificate(0,Q(0),Q(7,10))
    certificate(1,Q(3,5),Q(1,5))
    certificate(2,Q(0),Q(3,40))
    certificate(3,Q(0),Q(1,25))

    payload={
      "schema":"riemann.t104620.conrey_variational_reconstruction.v1",
      "verdict":"PASS_T104620_CONREY_VARIATIONAL_RECONSTRUCTION",
      "certified_bounds":{
        "alpha_0":"3/10","alpha_1":"4/5",
        "alpha_2":"37/40","alpha_3":"24/25"
      },
      "scope":{
        "conrey_variational_functional_reconstructed":True,
        "low_order_bounds_certified":True,
        "published_table_reproduced":False,
        "new_numerical_record_claimed":False,
        "adjacent_derivative_9218_claim_reconstructed":False,
        "rh_established":False
      }
    }
    text=json.dumps(payload,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else:
        print(text,end="")


if __name__=="__main__": main()
