#!/usr/bin/env python3
"""Exact complete-source certificate on L=3/20 with a negative endpoint W(L)."""

from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

from check_coercivity import log_rational_bounds, require
from check_codimension14 import atan_bounds, certify as certify_constants
from check_small_window import exp_bounds, ceil_scaled, compact_lower, compact_upper


def certify():
    certify_constants()
    al,ah=atan_bounds(Q(1,5),16)
    bl,bh=atan_bounds(Q(1,239),8)
    pi_lo,pi_hi=16*al-4*bh,16*ah-4*bl
    log2_lo,log2_hi=log_rational_bounds(Q(2))
    harmonic128=sum((Q(1,j) for j in range(1,129)),Q())
    require(harmonic128-7*log2_hi-Q(1,128)>Q(57,100), "gamma>57/100")
    logpi_lo,_=log_rational_bounds(pi_lo,64)
    require(log2_lo>Q(693,1000), "log2>.693")
    require(logpi_lo>Q(143,125), "logpi>1.144")
    scale=2**100
    prefix_lo=prefix_hi=0
    for n in range(2,128):
        power=n.bit_length()-1
        lo,hi=log_rational_bounds(Q(n,2**power))
        lo+=power*log2_lo
        hi+=power*log2_hi
        term_lo=lo/(n*n)
        prefix_lo+=(term_lo.numerator*scale)//term_lo.denominator
        prefix_hi+=ceil_scaled(hi/(n*n),scale)
    n=128
    logn_lo,logn_hi=7*log2_lo,7*log2_hi
    tail_lo=(logn_lo+1)/n+logn_lo/(2*n*n)
    tail_hi=(logn_hi+1)/n+logn_hi/(2*n*n)+(2*logn_hi-1)/(8*n**3)
    p2_lo=6*(Q(prefix_lo,scale)+tail_lo)/pi_hi**2
    p2_hi=6*(Q(prefix_hi,scale)+tail_hi)/pi_lo**2
    require(p2_hi<Q(57,100), "P2 complete upper")
    require(p2_lo>Q(5699,10000), "P2 complete lower")
    length=Q(3,20)
    b=Q(3,2)
    cb_lo=-Q(59,125)
    cb_hi=-Q(469,1000)
    ep_lo,ep_hi=exp_bounds(length/2)
    eb_lo,eb_hi=exp_bounds(b*length)
    en_lo,en_hi=1/eb_hi,1/eb_lo
    cosh_hi=(eb_hi+en_hi)/2
    cosh_lo=(eb_lo+en_lo)/2
    sinh_lo=(eb_lo-en_hi)/2
    sinh_hi=(eb_hi+0-en_lo)/2
    gamma1_lo=gamma2_lo=gamma_integral_lo=gamma0_hi=Q()
    for j in range(1,129):
        lam=2*j+Q(1,2)
        el,eh=exp_bounds(lam*length)
        coef=1/(lam*lam-b*b)
        gamma1_lo+=lam*coef/eh
        gamma2_lo+=lam*lam*coef/eh
        gamma_integral_lo+=coef*(1-1/el)/lam
        gamma0_hi+=coef/el
    next_lam=Q(517,2)  # j=129
    _,next_exp_hi=exp_bounds(next_lam*length)
    next_exp_lo,_=exp_bounds(next_lam*length)
    two_l_exp_lo,_=exp_bounds(2*length)
    gamma0_hi+=(1/next_exp_lo)/(next_lam**2-b*b)/(1-1/two_l_exp_lo)
    wp_hi=ep_hi/4-b*cb_lo*en_hi-gamma1_lo-p2_lo*sinh_lo
    wpp_lo=Q(1,8)+b*b*cb_lo+gamma2_lo-b*p2_hi*cosh_hi
    iw_lo=ep_lo-1+(cb_lo/b)*(1-en_lo)+gamma_integral_lo-(p2_hi/b**2)*sinh_hi
    w_endpoint_hi=ep_hi/2+cb_hi*en_lo+gamma0_hi-(p2_lo/b)*cosh_lo
    require(wp_hi<-Q(1,500), "W'(3/20)<-1/500")
    require(wpp_lo>0, "complete W'' positivity")
    require(iw_lo>Q(1,3000), "positive averaged source despite negative endpoint")
    require(exp_bounds(length)[1]<2, "no prime-power cusp")
    require(w_endpoint_hi<-Q(1,200), "negative kernel endpoint W(L)<-1/200")
    return {
        "status":"EXACT_ARITHMETIC_ACCEPT",
        "scope":"complete source positivity L=3/20, all complex L2 tests",
        "length":"3/20",
        "P2_lower":str(compact_lower(p2_lo)),
        "P2_upper":str(compact_upper(p2_hi)),
        "Wprime_endpoint_upper":str(compact_upper(wp_hi)),
        "Wsecond_whole_interval_lower":str(compact_lower(wpp_lo)),
        "source_integral_lower":str(compact_lower(iw_lo)),
        "W_endpoint_upper":str(compact_upper(w_endpoint_hi)),
        "result":"q>=3/500||H-mu/2||²+1/300|mu|²",
        "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "helper_hashes":{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                         for name in ['check_coercivity.py','check_codimension14.py','check_small_window.py']},
        "not_proved":["source positivity L=1","interval joining","all-window positivity","RH"],
    }


if __name__=='__main__':
    print(json.dumps(certify(),indent=2))
