#!/usr/bin/env python3
"""Exact uniform controls for VOLTERRA_RATIONAL_REFINEMENT.md."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path
from verify_annular import H, require
from verify_weighted_rational import arctan_bounds

HERE = Path(__file__).resolve().parent
N0 = 850000
D = Q(3191,5000)
C1 = Q(6383,10000)
C2 = Q(2037,5000)
CE = Q(236393,1000000)
KAPPA = Q(237,200)
Q0 = Q(2631,10000)
ELL = 2*CE*(1+2*D)


def exponential_upper(x,degree=6):
    partial = sum((x**k/Q(math.factorial(k)) for k in range(degree+1)),Q(0))
    next_term = x**(degree+1)/Q(math.factorial(degree+1))
    require(0<=x<degree+2,"exponential geometric-tail domain")
    return partial+next_term/(1-x/Q(degree+2))


def gap(q,ell=ELL,kappa=KAPPA):
    return Q(13,44)-ell*q-(C2+C1*C1)*kappa*kappa*q*q*(Q(1,3)+ell*q)/4


def largest_even(t,num=2631,den=10000):
    lo,hi = 0,2
    while den*hi*hi<=num*t: hi*=2
    while hi-lo>1:
        mid = (lo+hi)//2
        if den*mid*mid<=num*t: lo=mid
        else: hi=mid
    n = lo-lo%2
    require(den*n*n<=num*t<den*(n+2)**2,"maximal exact even tail order")
    return n


def positive_ldl(a):
    n = len(a)
    l = [[Q(int(i==j)) for j in range(n)] for i in range(n)]
    pivots = []
    for j in range(n):
        pivot = a[j][j]-sum((l[j][k]*l[j][k]*pivots[k] for k in range(j)),Q(0))
        require(pivot>0,"independent Volterra norm Gram strictly positive")
        pivots.append(pivot)
        for i in range(j+1,n):
            l[i][j] = (a[i][j]-sum((l[i][k]*l[j][k]*pivots[k]
                                    for k in range(j)),Q(0)))/pivot
    return pivots


def volterra_controls():
    receipts = []
    for n in range(1,13):
        for kind in ("uniform","zero_and_unequal"):
            e = ([Q(1)]*n if kind=="uniform" else
                 [Q(0) if i%4==0 and i else Q(1,i+1) for i in range(n)])
            masses = [x*x for x in e]
            total = sum(masses,Q(0))
            u = [[e[i]*e[j] if i<j else Q(0) for j in range(n)] for i in range(n)]
            b = [[u[i][j]+(masses[i]/2 if i==j else Q(0))
                  for j in range(n)] for i in range(n)]
            # Independently integrate the compressed Volterra kernel on each cell.
            endpoints = [Q(0)]
            for mass in masses: endpoints.append(endpoints[-1]+mass)
            for i in range(n):
                for j in range(n):
                    if not e[i] or not e[j]: integral = Q(0)
                    elif i<j: integral = masses[i]*masses[j]/(e[i]*e[j])
                    elif i==j: integral = masses[i]*masses[i]/(2*e[i]*e[i])
                    else: integral = Q(0)
                    require(integral==b[i][j],"exact compressed Volterra integral")
            bound = Q(200000,314159)*total
            gram = [[(bound*bound if i==j else Q(0))-
                     sum((u[k][i]*u[k][j] for k in range(n)),Q(0))
                     for j in range(n)] for i in range(n)]
            pivots = positive_ldl(gram)
            receipts.append({"dimension":n,"kind":kind,"endpoint_trace_exact":str(total),
                             "norm_upper_exact":str(bound),
                             "smallest_ldl_pivot_exact":str(min(pivots))})
    return receipts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    a5lo,a5hi = arctan_bounds(Q(1,5))
    a239lo,a239hi = arctan_bounds(Q(1,239))
    pi_lo,pi_hi = 16*a5lo-4*a239hi,16*a5hi-4*a239lo
    require(Q(314159,100000)<pi_lo<pi_hi<Q(22,7),"Machin precise rational pi bounds")
    count_base = Q(112,1000)+Q(278,8000)+Q(2510,28000)
    require(count_base==Q(6619,28000),"literal published argument-bound constants")
    require(CE-count_base==Q(1,7000000)>Q(1,84*H),"complete-count sharpening margin")
    require(1300**2<2*N0,"uniform inverse square-root guard")
    dilation_upper = Q(200000,314159)+(2+Q(1,28*N0))/1300+Q(2,N0)
    require(dilation_upper<D,"uniform Volterra rational dilation")
    require(D+Q(3,N0)<C1,"uniform complex first derivative")
    second_upper = D*D+(6*N0+1)*D/Q(N0*N0)+Q(9,N0*N0)+Q(7,N0**3)
    require(second_upper<C2,"uniform complex second derivative")
    exponent = (D+Q(2,N0))*Q0
    require(exponent<Q(21,125),"uniform variable complex amplification exponent")
    exp_upper = exponential_upper(Q(21,125))
    require(exp_upper<KAPPA,"full exponential rational upper bound")
    require(ELL==Q(1345312563,1250000000),"exact improved quadrature coefficient")
    exact_gap = gap(Q0)
    require(exact_gap==Q(18928758577227631999353142201217,
                         220000000000000000000000000000000000)>0,
            "strict complete-source primary endpoint gap")
    require(10000*888000**2<2631*H,"global888000 height guard")
    require(largest_even(H)==888424,"maximal primary global order")
    fallback_q,fallback_kappa = Q(1,4),Q(47,40)
    fallback_ell = Q(1,2)+D
    require((D+Q(2,N0))*fallback_q<Q(4,25),"fallback amplification exponent")
    require(exponential_upper(Q(4,25))<fallback_kappa,"fallback exponential upper")
    fallback_gap = gap(fallback_q,fallback_ell,fallback_kappa)
    require(fallback_gap==Q(294672985812197,6758400000000000000)>0,
            "strict unchanged-count fallback gap")
    require(4*866000**2<H,"global866000 fallback height guard")
    require(largest_even(H,1,4)==866024,"maximal fallback global order")
    output = {"status":"PASS_EXACT_VOLTERRA_REFINEMENT_CONTROLS",
              "minimum_order":N0,"minimum_height":H,"condition":"10000*n^2 <= 2631*T",
              "global_order":888000,"maximal_even_global_order":888424,
              "uniform_gap_exact":str(exact_gap),"uniform_gap_decimal":float(exact_gap),
              "count_constant_exact":str(CE),"count_constant_margin_exact":str(CE-count_base),
              "rational_dilation_exact":str(D),"dilation_upper_exact":str(dilation_upper),
              "complex_amplification_exact":str(KAPPA),"exponential_upper_exact":str(exp_upper),
              "first_derivative_exact":str(C1),"second_derivative_exact":str(C2),
              "quadrature_coefficient_exact":str(ELL),"fallback_order":866000,
              "fallback_gap_exact":str(fallback_gap),
              "examples":[{"height":t,"tail_order":largest_even(t)}
                          for t in (H,10**14,10**18,10**24,10**36)],
              "volterra_controls":volterra_controls(),
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                              for name in ("VOLTERRA_RATIONAL_REFINEMENT.md",
                                           "verify_volterra_refinement.py",
                                           "WEIGHTED_RATIONAL_DILATION.md",
                                           "ANNULAR_GLOBAL_PICK.md")},
              "published_inputs_replayed":False,"tail_critical_census_used":False,
              "global_critical_census_used":True,
              "limitations":["native analytic operator/source proof remains essential",
                             "published argument bound and finite critical census are imported",
                             "tail order increases for changing kernels","RH remains open"]}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output: args.output.write_text(content)
    else: print(content,end="")


if __name__ == "__main__":
    main()
