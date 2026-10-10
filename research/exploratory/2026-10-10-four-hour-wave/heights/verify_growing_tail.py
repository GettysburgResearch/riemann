#!/usr/bin/env python3
"""Exact uniform guards for GROWING_TAIL_ORDER.md; no zero census."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from verify_annular import H, require

HERE = Path(__file__).resolve().parent


def multiply(a,b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def largest_order(t):
    """Largest even n with 14*n**3 <= t, using integer arithmetic."""
    lo,hi = 0,2
    while 14*hi**3 <= t:
        hi *= 2
    while hi-lo>1:
        mid = (lo+hi)//2
        if 14*mid**3 <= t:
            lo = mid
        else:
            hi = mid
    n = lo-lo%2
    require(14*n**3 <= t < 14*(n+2)**3, "maximal even tail order")
    return n


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    u = Q(1,256)
    coefficients = multiply([Q(1),Q(1),Q(1,4)],
                           [Q(3,8),Q(1,4),Q(1,2),Q(5,8),Q(1,8)])
    require(all(c>0 for c in coefficients), "variation polynomial monotonicity")
    variation = sum((c*u**j for j,c in enumerate(coefficients)),Q(0))
    require(variation < Q(49,128), "uniform weighted variation")
    require(Q(3,8)+u/4 <= Q(49,128), "uniform unweighted variation")
    sampling = Q(1,6)+Q(441,1024*14)
    require(sampling < Q(1,5), "uniform complete-source sampling")
    require(Q(5,16*14) < Q(1,32), "uniform complex Taylor exponent")
    require(Q(1,56*256**2*H)<Q(1,17), "uniform rational source weight")
    require((1+u/2)**2+Q(5,4*H)<Q(4,3), "uniform segment magnitude")
    require(2*(1+u)*Q(17,16)<3, "uniform weight first derivative")
    require(2*(1+u)*(1+2*u)*Q(17,16)**2<4, "uniform weight second derivative")
    require(4*u**4+3*u*u+Q(1,2)<Q(9,16), "uniform integrated second derivative")
    require(Q(32,31)<Q(17,16), "exponential rounding")
    require(Q(6400,57568)>Q(1,9), "count main density")
    ratio = (Q(43659,4096*14)+Q(1287495,131072*4*14**2)
             +Q(99,1120*H)*(1+3*u*u))
    require(ratio < Q(4,5), "uniform strict domination")
    samples = []
    for t in (H,10**14,10**18,10**24,10**36):
        n = largest_order(t)
        require(n>=256, "sample belongs to theorem range")
        samples.append({"height":t,"tail_order":n,"14_n_cubed":14*n**3})
    output = {"status":"PASS_EXACT_UNIFORM_GROWING_TAIL_GUARDS",
              "threshold":H,"minimum_even_order":256,"condition":"14*n^3 <= T",
              "monotone_variation_coefficients":[str(c) for c in coefficients],
              "variation_worst_exact":str(variation),
              "sampling_worst_exact":str(sampling),
              "relative_loss_uniform_upper_exact":str(ratio),
              "relative_loss_uniform_upper_decimal":float(ratio),
              "relative_loss_strict_upper":"4/5","examples":samples,
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ("GROWING_TAIL_ORDER.md","verify_growing_tail.py",
                                            "L2_FRAME_REFINEMENT.md","L2_ANNULAR_PICK.md",
                                            "ANNULAR_GLOBAL_PICK.md")},
              "published_inputs_replayed":False,"critical_line_census_used":False,
              "limitations":["tail kernels change as T increases",
                             "the complete kernel below T is not certified by this theorem",
                             "analytic source/count/frame inputs are not replaced by arithmetic",
                             "RH remains unproved"]}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content,end="")


if __name__ == "__main__":
    main()
