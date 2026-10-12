#!/usr/bin/env python3
"""Exact uniform guards for WEIGHTED_RATIONAL_DILATION.md."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from verify_annular import H, require

HERE = Path(__file__).resolve().parent


def arctan_bounds(x,terms=12):
    s = sum(((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
    next_s = s+(-1)**terms*x**(2*terms+1)/Q(2*terms+1)
    return min(s,next_s),max(s,next_s)


def largest_order(t):
    lo,hi = 0,2
    while 6*hi*hi<=t: hi*=2
    while hi-lo>1:
        mid = (lo+hi)//2
        if 6*mid*mid<=t: lo=mid
        else: hi=mid
    n = lo-lo%2
    require(6*n*n<=t<6*(n+2)**2,"maximal even square-root tail order")
    return n


def triangular_control():
    receipts = []
    for n in range(1,17):
        d = [[Q(0) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            d[i][i] = i
            for j in range(i+1,n):
                d[i][j] = Q((-1)**(i+j)*(i+2)*(j+1),i+j+1)
        df = sum((x*x for row in d for x in row),Q(0))
        sf = sum(((d[i][j]+d[j][i])**2 for i in range(n) for j in range(n)),Q(0))
        require(df==(sf-2*sum(k*k for k in range(n)))/2,"triangular Frobenius identity")
        receipts.append({"dimension":n,"d_frobenius_squared":str(df)})
    return receipts


def endpoint_controls():
    receipts = []
    for n in range(1,65):
        exact = sum(2*k+1 for k in range(n))
        require(exact==n*n,"unweighted shifted-Legendre endpoint trace")
        receipts.append({"dimension":n,"endpoint_trace":exact})
    return receipts


def lower_gap(q):
    return Q(13,44)-Q(3,2)*q-Q(75,32)*q*q*(Q(1,3)+Q(3,2)*q)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    a5lo,a5hi = arctan_bounds(Q(1,5))
    a239lo,a239hi = arctan_bounds(Q(1,239))
    pi_lo,pi_hi = 16*a5lo-4*a239hi,16*a5hi-4*a239lo
    require(3<pi_lo<pi_hi<Q(22,7),"Machin rational pi enclosure")
    exp2_lower = sum((Q(2)**k/Q(__import__('math').factorial(k)) for k in range(5)),Q(0))
    require(exp2_lower>2*pi_hi,"log(2pi)<2")
    n0 = 256
    poly_coefficient = Q(5,7)*(1+Q(2,16)+Q(1,28*n0*16))
    require(Q(5,7)**2>Q(1,2),"inverse square-root-two upper bound")
    require(poly_coefficient<Q(13,16),"uniform polynomial dilation norm")
    require(Q(n0+1,n0*n0)<Q(3,16),"rational dilation multiplier allowance")
    require(Q(1,2*H)<Q(1,2),"complex prefactor geometric guard")
    exponent = Q(1,6)*(1+Q(2,n0))
    require(exponent<Q(1,5),"uniform complex amplification exponent")
    require(1/(1-exponent)<Q(5,4),"uniform complex amplification")
    require(1+Q(3,n0)<2,"complex first derivative guard")
    require(1+Q(7,n0)+Q(13,n0*n0)<2,"complex second derivative guard")
    q = Q(1,6)
    require(Q(75,32)*q*q*(Q(1,3)+Q(3,2)*q)==Q(175,4608),"endpoint strip cost")
    gap = lower_gap(q)
    require(gap==Q(379,50688)>0,"uniform strict reference-minus-loss gap")
    require(6*700000**2<H,"global700000 exact height guard")
    examples = [{"height":t,"tail_order":largest_order(t)}
                for t in (H,10**14,10**18,10**24,10**36)]
    global_q = Q(700000**2,H)
    output = {"status":"PASS_EXACT_WEIGHTED_RATIONAL_DILATION_GUARDS",
              "threshold":H,"minimum_order":n0,"condition":"6*n^2 <= T",
              "global_rounded_order":700000,"global_rounded_q_exact":str(global_q),
              "global_rounded_gap_exact":str(lower_gap(global_q)),
              "global_rounded_gap_decimal":float(lower_gap(global_q)),
              "uniform_gap_exact":str(gap),"uniform_gap_decimal":float(gap),
              "complex_amplification_upper":"5/4","examples":examples,
              "pi_interval_exact":[str(pi_lo),str(pi_hi)],
              "triangular_controls":triangular_control(),
              "endpoint_controls":endpoint_controls(),
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ("WEIGHTED_RATIONAL_DILATION.md",
                                            "verify_weighted_rational.py",
                                            "ANNULAR_GLOBAL_PICK.md",
                                            "GROWING_TAIL_ORDER.md",
                                            "RATIONAL_DILATION.md")},
              "published_inputs_replayed":False,
              "tail_critical_census_used":False,"global_critical_census_used":True,
              "limitations":["analytic weighted and complex sampling proofs remain essential",
                             "the full kernel needs the imported finite critical-line census",
                             "increasing tail orders belong to changing kernels",
                             "RH remains unproved"]}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output: args.output.write_text(content)
    else: print(content,end="")


if __name__ == "__main__":
    main()
