#!/usr/bin/env python3
"""Native rational certificate for complete source positivity on L=1/20.

This authenticates infinite prime/gamma tail bounds and the scalar inequalities
used by the continuum triangle-mixture proof.  No grid of the form is sampled.
"""

from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

from check_coercivity import log_rational_bounds, require
from check_codimension14 import atan_bounds, certify as certify_constants


def exp_bounds(x: Q, terms=80):
    require(0 <= x < terms+2, "nonnegative exp argument in geometric-tail regime")
    term = Q(1)
    partial = Q(1)
    for j in range(1, terms+1):
        term *= x/j
        partial += term
    following = term*x/(terms+1)
    upper = partial+following/(1-x/(terms+2))
    return partial, upper


def ceil_scaled(x, scale):
    return -((-x.numerator*scale)//x.denominator)


def compact_lower(x, scale=2**100):
    return Q((x.numerator*scale)//x.denominator,scale)


def compact_upper(x, scale=2**100):
    return Q(ceil_scaled(x,scale),scale)


def certify():
    certify_constants()  # authenticates C_b > -59/125 and all helper log bounds
    a_lo, _ = atan_bounds(Q(1,5),16)
    _, b_hi = atan_bounds(Q(1,239),8)
    pi_lo = 16*a_lo-4*b_hi
    log2_lo, log2_hi = log_rational_bounds(Q(2))

    # -zeta'(2)=sum log(n)/n².  For f(t)=log(t)/t², t>=128,
    # f''>=0 and integral f''=-f'(128).  The trapezoid error on each unit
    # interval is <=(1/8) integral f'', giving this complete tail upper bound.
    n_tail = 128
    scale = 2**100
    prefix_upper_scaled = 0
    for n in range(2,n_tail):
        power = n.bit_length()-1
        _, hi = log_rational_bounds(Q(n,2**power))
        hi += power*log2_hi
        prefix_upper_scaled += ceil_scaled(hi/(n*n),scale)
    log_n_hi = 7*log2_hi
    source_sum_hi = Q(prefix_upper_scaled,scale)+(log_n_hi+1)/n_tail
    source_sum_hi += log_n_hi/(2*n_tail**2)+(2*log_n_hi-1)/(8*n_tail**3)
    require(7*log2_lo>Q(5,6), "convex complete tail for f=log(t)/t²")
    p2_upper = 6*source_sum_hi/pi_lo**2
    require(p2_upper<Q(57,100), "complete P2<57/100")
    p2_lower = log2_lo/4  # the n=2 von Mangoldt term alone

    length = Q(1,20)
    b = Q(3,2)
    cb_lower = -Q(59,125)
    ep_lo,ep_hi=exp_bounds(length/2)
    eb_lo,eb_hi=exp_bounds(b*length)
    eb_negative_lo,eb_negative_hi=1/eb_hi,1/eb_lo
    cosh_hi=(eb_hi+eb_negative_hi)/2
    sinh_lo=(eb_lo-eb_negative_hi)/2
    gamma0_lo=Q()
    gamma1_lo=Q()
    gamma2_lo=Q()
    for j in range(1,65):
        lam=2*j+Q(1,2)
        _,e_hi=exp_bounds(lam*length)
        factor=(1/e_hi)/(lam*lam-b*b)
        gamma0_lo+=factor
        gamma1_lo+=lam*factor
        gamma2_lo+=lam*lam*factor
    w_endpoint_lo=ep_lo/2+cb_lower*eb_negative_hi+gamma0_lo-Q(57,100)*cosh_hi/b
    wprime_endpoint_hi=ep_hi/4-b*cb_lower*eb_negative_hi-gamma1_lo-p2_lower*sinh_lo
    wsecond_all_lo=Q(1,8)+b*b*cb_lower+gamma2_lo-b*Q(57,100)*cosh_hi
    require(w_endpoint_lo>Q(1,250), "W(1/20)>1/250")
    require(wprime_endpoint_hi<-Q(1,3), "W'(1/20)<-1/3")
    require(wsecond_all_lo>0, "W''(x)>0 for 0<x<=1/20")
    require(exp_bounds(length)[1]<2, "no interior prime-power cusp")
    return {
        "status":"EXACT_ARITHMETIC_ACCEPT",
        "scope":"entire continuum L=1/20 positivity for literal source kernel",
        "complete_prime_constant_upper":str(compact_upper(p2_upper)),
        "prime_constant_method":"zeta'(2) positive log series; convex trapezoid tail; zeta(2)=pi²/6",
        "gamma_lower_prefix_terms":64,
        "W_endpoint_lower":str(compact_lower(w_endpoint_lo)),
        "Wprime_endpoint_upper":str(compact_upper(wprime_endpoint_hi)),
        "Wsecond_complete_interval_lower":str(compact_lower(wsecond_all_lo)),
        "strict_acceptance":{"W_endpoint":"greater than1/250","Wprime":"less than-1/3","Wsecond":"greater than0"},
        "form_lower_coefficient":"b[-W'(L)]>1/2 multiplying the complete triangle form",
        "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "helper_hashes":{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                         for name in ['check_coercivity.py','check_codimension14.py']},
        "not_proved":["positivity at L=1","xi/Weil terminal adapter","any all-window theorem"],
    }


if __name__=='__main__':
    print(json.dumps(certify(),indent=2))
