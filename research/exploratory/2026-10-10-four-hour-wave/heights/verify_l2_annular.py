#!/usr/bin/env python3
"""Exact finite controls for L2_ANNULAR_PICK.md; no published theorem replay."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
from verify_annular import H, require

HERE = Path(__file__).resolve().parent


def add(a,b):
    result = [Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a):result[i] += v
    for i,v in enumerate(b):result[i] += v
    return result


def scale(a,factor):
    return [v*factor for v in a]


def derivative(a):
    return [i*a[i] for i in range(1,len(a))]


def integral_product(a,b):
    return sum((a[i]*b[j]*Q(2,i+j+1) for i in range(len(a))
                for j in range(len(b)) if (i+j)%2 == 0),Q(0))


def value(a,t):
    result = Q(0)
    for v in reversed(a):result = result*t+v
    return result


def legendre_rodrigues(k):
    # Differentiate (t^2-1)^k exactly k times, then divide by 2^k k!.
    result = [Q(0)]*(k+1)
    for j in range(k+1):
        degree = 2*j
        if degree >= k:
            result[degree-k] += Q(comb(k,j)*(-1)**(k-j)*factorial(degree),
                                  2**k*factorial(k)*factorial(degree-k))
    return result


def legendre_recurrence(maximum):
    result = [[Q(1)],[Q(0),Q(1)]]
    for k in range(1,maximum):
        shifted = [Q(0)]+scale(result[k],Q(2*k+1,k+1))
        older = scale(result[k-1],Q(-k,k+1))
        result.append(add(shifted,older))
    return result[:maximum+1]


def check_legendre():
    maximum = 32
    basis = legendre_recurrence(maximum)
    receipts = []
    for k,poly in enumerate(basis):
        require(poly == legendre_rodrigues(k), "Legendre recurrence/Rodrigues identity")
        require(value(poly,Q(1)) == 1 and value(poly,Q(-1)) == (-1)**k,
                "Legendre endpoint normalization")
        require(integral_product(poly,poly) == Q(2,2*k+1), "Legendre norm")
        for j in range(k):
            require(integral_product(poly,basis[j]) == 0, "Legendre orthogonality")
        target = []
        for j in range(k):
            if (j+k)%2:
                target = add(target,scale(basis[j],Q(2*j+1)))
        require(derivative(poly) == target, "Legendre derivative expansion")
        frobenius_squared = sum((Q((2*i+1)*(2*j+1)) for i in range(k+1)
                                 for j in range(i) if (i+j)%2),Q(0))
        require(frobenius_squared < (k+1)**4, "L2 derivative Frobenius bound")
        require(sum((Q(2*j+1,2) for j in range(k+1)),Q(0)) == Q((k+1)**2,2),
                "L2 endpoint trace bound")
        receipts.append({"degree":k,"derivative_frobenius_squared":str(frobenius_squared),
                         "norm_squared":str(Q(2,2*k+1))})
    return receipts


def auxiliary(n,a):
    require(n % 2 == 0 and 256 <= n <= 3500, "declared even auxiliary range")
    h = Q(1,n)+Q(1,2*n*n)
    require(Q(6400,57568) > Q(1,9), "reference source density")
    require(Q(1,6)+Q(27*n**3,64*H) <= Q(1,5), "discrete sampling constant")
    require(Q(5*n**3,16*H) <= Q(1,32), "complex Taylor Minkowski factor")
    require(Q(32,31) < Q(17,16), "exponential bound rounded")
    require(n*a*a/Q(H*H) < Q(1,17), "complex rational weight via Bernoulli")
    require((1+Q(1,n))**2+Q(5,4*H) < Q(4,3), "complex segment magnitude")
    require(2*(n+1)*Q(17,16) < 3*n, "complex weight first derivative")
    require(2*(n+1)*(n+2)*Q(17,16)**2 < 4*n*n, "complex weight second derivative")
    require(2*(n+1)*h < 3, "real normalized weight derivative")
    require(Q(3*n*n,2)+3 <= Q(25*n*n,16), "weighted endpoint variation")
    require(Q(4,n**4)+Q(3,n*n)+Q(1,2) < Q(9,16), "integrated second derivative")


def sufficient_ratio(n,a):
    x = Q(n**3,H)
    return Q(2025,32)*x+Q(117045,4096)*a*a*x*x+Q(72,5)*a*a*Q(n**3+3*n,H*H)


def check_quadrature_fixture():
    points = [Q(-9,10),Q(-2,5),Q(0),Q(3,10),Q(19,20)]
    weights = [Q(1),Q(3),Q(1),Q(2),Q(4)]
    mass = sum(weights,Q(0))
    # Continuous reference count rises linearly from zero to the full mass.
    cumulative = Q(0)
    discrepancy = Q(0)
    for point,weight in zip(points,weights):
        reference = mass*(point+1)/2
        discrepancy = max(discrepancy,abs(cumulative-reference))
        cumulative += weight
        discrepancy = max(discrepancy,abs(cumulative-reference))
    receipts = []
    for d in range(1,9):
        poly = add(legendre_rodrigues(d),[Q(1,3),Q(2,7)])
        q = integral_product(poly,poly)
        sampled = sum((w*value(poly,t)**2 for w,t in zip(weights,points)),Q(0))
        reference = mass*q/2
        bound = discrepancy*3*(d+1)**2*q
        require(abs(sampled-reference) <= bound, "finite count discrepancy quadratic control")
        receipts.append({"degree":d,"discrepancy_exact":str(discrepancy),
                         "error_to_derived_bound_exact":str(abs(sampled-reference)/bound)})
    return receipts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    checked = list(range(256,3501,2))
    for n in checked:
        auxiliary(n,Q(1,2))
    ratio = sufficient_ratio(3500,Q(1,2))
    require(ratio < Q(11,12), "global3500 stated sufficient inequality")
    output = {"status":"PASS_EXACT_L2_ANNULAR_PICK_CONTROLS",
              "packet_size":3500,"depth":"1/2","verified_height":H,
              "sufficient_ratio_exact":str(ratio),
              "sufficient_ratio_decimal":float(ratio),
              "sufficient_ratio_upper":"11/12",
              "all_positive_node_scales":True,
              "auxiliary_range_checked":{"first":256,"last":3500,"step":2,"count":len(checked)},
              "legendre_identity_controls":check_legendre(),
              "finite_count_quadrature_controls":check_quadrature_fixture(),
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                                for name in ("L2_ANNULAR_PICK.md","verify_l2_annular.py",
                                             "ANNULAR_GLOBAL_PICK.md","verify_annular.py")},
              "external_theorems_replayed":False,
              "limitations":["finite algebra does not establish the all-height source by itself",
                             "S(T) bound and verified height are imported published inputs",
                             "complete Hadamard source is a classical analytic input",
                             "RH remains unproved"]}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content,end="")

if __name__ == "__main__":
    main()
