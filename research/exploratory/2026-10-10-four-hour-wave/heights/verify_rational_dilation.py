#!/usr/bin/env python3
"""Exact Legendre tail-obstruction controls; no numerical quadrature."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from verify_annular import require

HERE = Path(__file__).resolve().parent


def add(a,b):
    c = [Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i] += x
    for i,x in enumerate(b): c[i] += x
    return c


def scale(a,s):
    return [s*x for x in a]


def multiply(a,b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j] += x*y
    return c


def integral(a,half_weight=False):
    return sum((x*(Q(2,2*j+3) if half_weight else Q(1,j+1))
                for j,x in enumerate(a)),Q(0))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    legendre = [[Q(1)],[Q(-1),Q(2)]]
    for k in range(1,32):
        legendre.append(scale(add(scale(multiply([Q(-1),Q(2)],legendre[k]),2*k+1),
                                  scale(legendre[k-1],-k)),Q(1,k+1)))
    p = [Q(0)]
    receipts = []
    for d in range(33):
        p = add(p,scale(legendre[d],2*d+1))
        endpoint = sum(p,Q(0))
        square = multiply(p,p)
        unweighted = integral(square)
        s = integral(square,True)
        dilation = [(j+1)*x for j,x in enumerate(p)]
        u = integral(multiply(dilation,dilation),True)
        mixed = integral(multiply(p,dilation),True)
        n = 2*d+2
        bound = Q(n*n,4)+Q(1,2)
        require(endpoint == (d+1)**2, "endpoint kernel evaluation")
        require(unweighted == (d+1)**2, "endpoint kernel exact unweighted norm")
        require(0<s<=unweighted, "weighted norm ordering")
        require(mixed == s/4+endpoint*endpoint/2, "exact integration by parts")
        require(u*s>=mixed*mixed, "weighted Cauchy control")
        ratio_squared = 4*u/s
        require(ratio_squared>=bound*bound, "quadratic tail dilation obstruction")
        receipts.append({"degree":d,"space_dimension":n,"weighted_norm_exact":str(s),
                         "dilation_ratio_squared_exact":str(ratio_squared),
                         "proved_ratio_lower_bound":str(bound)})
    for n in (1,2,8,32,256,6000,1000000):
        require(sum(k*k for k in range(1,n+1))==n*(n+1)*(2*n+1)//6,
                "full-axis Frobenius coefficient")
    output = {"status":"PASS_EXACT_RATIONAL_DILATION_CONTROLS",
              "tail_control_degrees":{"first":0,"last":32},"tail_controls":receipts,
              "full_axis_squared_coefficient":"n*(n+1)*(2*n+1)/6",
              "tail_ratio_all_even_n_lower_limit":"n^2/4+1/2",
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ("RATIONAL_DILATION.md","verify_rational_dilation.py")},
              "limitations":["finite arithmetic is separate from the analytic all-degree proof",
                             "a universal truncated-tail n^2 upper bound is not established",
                             "these lemmas do not upgrade the certified xi Pick order"]}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content,end="")


if __name__ == "__main__":
    main()
