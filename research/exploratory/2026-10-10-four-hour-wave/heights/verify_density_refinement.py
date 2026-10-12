#!/usr/bin/env python3
"""Exact all-height scalar guards for DENSITY_RATIONAL_REFINEMENT.md."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path
from verify_annular import H, require
from verify_weighted_rational import arctan_bounds
from verify_volterra_refinement import D,C1,C2,N0,exponential_upper,largest_even

HERE = Path(__file__).resolve().parent


def logarithm_lower(x,terms):
    require(x>1,"positive log-series domain")
    r = (x-1)/(x+1)
    return 2*sum((r**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))


def exponential_lower(x,degree):
    require(x>=0,"positive exponential series")
    return sum((x**k/Q(math.factorial(k)) for k in range(degree+1)),Q(0))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    a5lo,a5hi = arctan_bounds(Q(1,5))
    a239lo,a239hi = arctan_bounds(Q(1,239))
    pi_lo,pi_hi = 16*a5lo-4*a239hi,16*a5hi-4*a239lo
    require(Q(333,106)<pi_lo<pi_hi<Q(355,113),"precise two-sided main-density pi")
    l0 = Q(28729,1000)
    log_h_lower = logarithm_lower(Q(3),24)+12*logarithm_lower(Q(10),80)
    require(log_h_lower>l0,"actual H logarithm positive-series lower bound")
    require(exponential_lower(Q(3358,1000),20)>l0,"logL0 strict Taylor upper bound")
    require(exponential_lower(Q(1838,1000),12)>2*pi_hi,"log2pi strict Taylor upper")
    require(exponential_upper(Q(1))<3<l0,"uniform logL/L decreasing domain")
    ce = Q(232,1000)
    count_base = Q(112,1000)+Q(278,1000)*Q(3358,28729)+Q(2510,28729)
    require(count_base+Q(1,84*H)<ce,"complete discrepancy count margin")
    lower = Q(113,355)*(1-Q(1838,28729))
    upper = Q(106,333)
    ell = 2*ce*(1+2*D)
    require(ell==Q(165039,156250),"exact density-refined quadrature coefficient")
    q,kappa = Q(27,100),Q(119,100)
    require((D+Q(2,N0))*q<Q(173,1000),"uniform density-refined displacement exponent")
    exp_upper = exponential_upper(Q(173,1000))
    require(exp_upper<kappa,"whole displacement exponential rational enclosure")
    gap = lower-ell*q-(C2+C1*C1)*kappa*kappa*q*q*(upper+ell*q)/4
    require(gap>0,"strict complete density-refined source gap")
    require(100*900000**2==27*H,"exact global900000 height guard")
    require(largest_even(H,27,100)==900000,"maximal global even order")
    output = {"status":"PASS_EXACT_DENSITY_RATIONAL_REFINEMENT",
              "minimum_order":N0,"condition":"100*n^2 <= 27*T","minimum_height":H,
              "global_order":900000,"count_constant_exact":str(ce),
              "count_base_exact":str(count_base),"count_margin_exact":str(ce-count_base),
              "main_density_lower_exact":str(lower),"main_density_upper_exact":str(upper),
              "quadrature_coefficient_exact":str(ell),"amplification_exact":str(kappa),
              "exponential_upper_exact":str(exp_upper),"strict_gap_exact":str(gap),
              "strict_gap_decimal":float(gap),
              "elementary_guards":{"logH_lower":"28729/1000","logL0_upper":"3358/1000",
                                  "pi_lower":"333/106","pi_upper":"355/113",
                                  "log2pi_upper":"1838/1000"},
              "examples":[{"height":t,"tail_order":largest_even(t,27,100)}
                          for t in (H,10**14,10**18,10**24,10**36)],
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                              for name in ("DENSITY_RATIONAL_REFINEMENT.md",
                                           "verify_density_refinement.py",
                                           "VOLTERRA_RATIONAL_REFINEMENT.md",
                                           "verify_volterra_refinement.py")},
              "published_inputs_replayed":False,"tail_critical_census_used":False,
              "global_critical_census_used":True,"RH_proved":False}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output: args.output.write_text(content)
    else: print(content,end="")


if __name__ == "__main__":
    main()
