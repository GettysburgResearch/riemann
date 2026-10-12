#!/usr/bin/env python3
"""Exact constants and finite complex controls for NARROW_ANNULAR_PICK.md."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from verify_annular import CQ, H, require, cprod

HERE = Path(__file__).resolve().parent


def norm_squared(value):
    return value.re*value.re+value.im*value.im


def auxiliary_conditions(n, a):
    require(n % 2 == 0 and 8 <= n <= 350, "admissible even order")
    require(Q(1024,1023)**n < 2, "uniform rational-weight upper bound")
    require(Q(3*n**3,8*H) < Q(1,2), "complex polynomial exponential factor")
    require(a*a/Q(H*H) < Q(1,n**3), "peak projection shrink")
    require(H*(Q(25,896)-Q(1,100)) > n**3, "uniform polynomial peak zero count")
    require(H > Q(6*n,5), "narrow annular upper count")
    require(Q(96,n**4)+Q(48,n*n)+6 < 7, "quadratic second derivative constant")
    require(6*(n+1)*Q(1024,1023) < 12*n, "rational weight first derivative")
    require(6*(n+1)*(n+2)*Q(1024,1023)**2 < 24*n*n,
            "rational weight second derivative")


def scalar_conditions(n, a):
    auxiliary_conditions(n, a)
    ratio = Q(204800)*a*a*n**8/Q(H*H)
    require(ratio < 1, "strict global annular domination")
    return {"packet_size": n, "horizontal_depth": str(a),
            "relative_error_upper_exact": str(ratio),
            "relative_error_upper_decimal": float(ratio),
            "certifies_all_positive_node_scales": True}


def chebyshev_coefficients(degree):
    older, current = [Q(1)], [Q(0),Q(1)]
    if degree == 0:
        return older
    for _ in range(1,degree):
        following = [Q(0)]*(len(current)+1)
        for j,value in enumerate(current):
            following[j+1] += 2*value
        for j,value in enumerate(older):
            following[j] -= value
        older,current = current,following
    return current


def derivative(coefficients):
    return [j*coefficients[j] for j in range(1,len(coefficients))]


def evaluate(coefficients,z):
    result = CQ()
    for value in reversed(coefficients):
        result = result*z+value
    return result


def polynomial_controls():
    receipts = []
    for n, a, l in ((8,Q(1,2),1024),(16,Q(1,2),2048),
                    (16,Q(3,8),1024),(16,Q(1,2),H)):
        degree = n//2-1
        polynomial = chebyshev_coefficients(degree)
        first,second = derivative(polynomial),derivative(derivative(polynomial))
        r = 1+Q(1,n)
        lower,upper = 1-a*a/Q(l*l),r*r
        center,half_width = (lower+upper)/2,(upper-lower)/2
        # Widely separated rho values stress the denominator normalization.
        rhos = [Q(1,10**12)*(10**(2*j)) for j in range(n)]
        d = Q(1)
        for rho in rhos:
            d *= 1+rho
        for position in (Q(1,16),Q(1,4),Q(1,2),Q(3,4),Q(15,16)):
            b_over_l = 1+position/n
            v = b_over_l*b_over_l-a*a/Q(l*l)
            delta = 2*a*b_over_l/l
            z = CQ(v,delta)
            phi = CQ(d)/cprod(rho+z for rho in rhos)
            t = (z-center)/half_width
            p = evaluate(polynomial,t)
            dp = evaluate(first,t)/half_width
            ddp = evaluate(second,t)/(half_width*half_width)
            require(norm_squared(p) <= 4, "finite complex polynomial bound")
            require(norm_squared(dp) <= Q(n**6,4), "finite complex first derivative")
            require(norm_squared(ddp) <= Q(n**12,64), "finite complex second derivative")
            projected_phi = d
            for rho in rhos:
                projected_phi /= rho+v
            projected_p = evaluate(polynomial,CQ((v-center)/half_width)).real()
            for k in (0,1):
                psi = phi*z**k
                log_first = CQ(k)/z-sum((CQ(1)/(rho+z) for rho in rhos),CQ())
                log_second = -(CQ(k)/(z*z))+sum((CQ(1)/((rho+z)*(rho+z))
                                                   for rho in rhos),CQ())
                dpsi = psi*log_first
                ddpsi = psi*(log_first*log_first+log_second)
                fsecond = (ddpsi*p*p+4*dpsi*p*dp
                           +2*psi*dp*dp+2*psi*p*ddp)
                require(norm_squared(psi) <= 36, "finite complex rational-weight bound")
                require(norm_squared(dpsi) <= 144*n*n, "finite rational first derivative")
                require(norm_squared(ddpsi) <= 576*n**4, "finite rational second derivative")
                require(norm_squared(fsecond) < 49*n**12,
                        "finite second derivative quadratic bound")
                actual = (psi*p*p).re
                projected = projected_phi*v**k*projected_p*projected_p
                error = abs(actual-projected)
                error_bound = 32*a*a*n**6/Q(l*l)
                require(error < error_bound, "finite conjugate projection error")
                receipts.append({"packet_size":n,"polynomial_degree":degree,
                                 "height":l,"depth":str(a),
                                 "annular_position":str(position),"shift":k,
                                 "error_to_bound_ratio_exact":str(error/error_bound)})
    return receipts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    for n in range(8,351,2):
        auxiliary_conditions(n,Q(1,2))
    classical = scalar_conditions(320,Q(1,2))
    quasi = scalar_conditions(350,Q(3,8))
    require(Q(classical["relative_error_upper_exact"]) < Q(2,3), "classical stated margin")
    require(Q(quasi["relative_error_upper_exact"]) < Q(3,4), "quasi-RH stated margin")
    require(Q(63,2) < 32, "general depth Taylor coefficient")
    require(Q(121,16) < 8, "e^2 bound for positive rational weight")
    output = {"status":"PASS_EXACT_NARROW_ANNULAR_PICK_CONTROLS",
              "classical":classical,"quasi_RH":quasi,
              "auxiliary_orders_checked":list(range(8,351,2)),
              "finite_complex_polynomial_controls":polynomial_controls(),
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                                for name in ("NARROW_ANNULAR_PICK.md","verify_narrow_annular.py",
                                             "ANNULAR_GLOBAL_PICK.md","verify_annular.py")},
              "external_theorems_replayed":False,
              "limitations":["finite controls do not prove uniform analytic inequalities",
                             "Markov inequality and complete xi source are classical inputs",
                             "S(T) estimate and verified height are published inputs",
                             "order350 additionally imports quasi-RH depth<=3/8",
                             "RH remains unproved"]}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content,end="")

if __name__ == "__main__":
    main()
