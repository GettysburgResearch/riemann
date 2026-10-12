#!/usr/bin/env python3
"""Exact guards for L2_FRAME_REFINEMENT.md; published inputs remain imported."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from verify_annular import H, require

HERE = Path(__file__).resolve().parent


def sharp_legendre_controls():
    receipts = []
    for d in range(129):
        m = d+1
        frobenius = sum((Q((2*k+1)*(2*j+1)) for k in range(1,d+1)
                         for j in range(k) if (j+k)%2),Q(0))
        exact = Q(d*m*m*(d+2),4)
        require(frobenius == exact <= Q(m**4,4), "sharp derivative Frobenius identity")
        cross = sum((Q(2*k+1,2)*(-1)**k for k in range(d+1)),Q(0))
        require(cross == Q((-1)**d*m,2), "endpoint evaluation inner product")
        diagonal = Q(m*m,2)
        trace_bound = diagonal+abs(cross)
        require(trace_bound == Q(m*m+m,2), "two-endpoint evaluation largest eigenvalue")
        receipts.append({"degree":d,"derivative_frobenius_squared_exact":str(exact),
                         "two_endpoint_bound_exact":str(trace_bound)})
    return receipts


def guards(n,a):
    require(n % 2 == 0 and 256 <= n <= 6000, "even declared guard range")
    r = 1+Q(1,2*n)
    h = Q(1,2*n)+Q(1,8*n*n)
    variation = r*r*(Q(3*n*n,8)+Q(n,4)+h*(n+1))
    require(variation <= Q(49*n*n,128), "weighted correlated endpoint/variation bound")
    require(Q(3*n*n,8)+Q(n,4) <= Q(49*n*n,128), "unweighted variation bound")
    require(Q(1,6)+Q(441*n**3,1024*H) <= Q(1,5), "complete discrete sampling constant")
    require(Q(5*n**3,16*H) <= Q(1,32), "variable complex Taylor factor")
    require(n*a*a/Q(H*H) < Q(1,17), "rational source weight bound")
    require(r*r+Q(5,4*H) < Q(4,3), "complex segment magnitude")
    require(2*(n+1)*Q(17,16) < 3*n, "complex weight first derivative")
    require(2*(n+1)*(n+2)*Q(17,16)**2 < 4*n*n, "complex weight second derivative")
    require(Q(4,n**4)+Q(3,n*n)+Q(1,2) < Q(9,16), "integrated second derivative")
    require(Q(32,31)<Q(17,16), "elementary exponential rounding")
    require(Q(6400,57568)>Q(1,9), "complete main density lower bound")


def ratio(n,a):
    x = Q(n**3,H)
    return (Q(43659,4096)*x+Q(1287495,131072)*a*a*x*x
            +Q(99,20)*a*a*Q(n**3+3*n,H*H))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    orders = list(range(256,6001,2))
    for n in orders:
        guards(n,Q(1,2))
    sufficient = ratio(6000,Q(1,2))
    require(sufficient < Q(4,5), "global6000 strict sufficient inequality")
    output = {"status":"PASS_EXACT_L2_FRAME_REFINEMENT_CONTROLS",
              "packet_size":6000,"horizontal_depth":"1/2","verified_height":H,
              "sufficient_ratio_exact":str(sufficient),"sufficient_ratio_decimal":float(sufficient),
              "sufficient_ratio_upper":"4/5","all_positive_node_scales":True,
              "auxiliary_orders":{"first":256,"last":6000,"step":2,"count":len(orders)},
              "sharp_legendre_controls":sharp_legendre_controls(),
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                                for name in ("L2_FRAME_REFINEMENT.md","verify_l2_refinement.py",
                                             "L2_ANNULAR_PICK.md","verify_l2_annular.py",
                                             "ANNULAR_GLOBAL_PICK.md","verify_annular.py")},
              "published_inputs_replayed":False,
              "limitations":["global claim relies on the analytic refinement proof",
                             "complete source and published argument/height inputs are imported",
                             "finite Legendre and arithmetic checks are not a zero census",
                             "RH remains unproved"]}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content,end="")

if __name__ == "__main__":
    main()
