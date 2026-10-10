#!/usr/bin/env python3
"""Directed scalar boundaries for the fixed exclusion-pair architecture."""
from fractions import Fraction as Q
import argparse,hashlib,json
from pathlib import Path
from flint import arb,ctx
from check_threshold_arb import mobius_sieve
from verify_four_label import prime_power_sum
from verify_horizon_stitch import as_arb,require


def elementary(a,degree,mu):
    W=[arb(0)]+[prime_power_sum(a,j,mu) for j in range(1,degree+1)]
    e=[arb(1)]
    for k in range(1,degree+1):
        e.append(sum(((-1)**(j-1)*W[j]*e[k-j] for j in range(1,k+1)),arb(0))/k)
    return W,e


def bracket(function,lo=Q('1.001'),hi=Q('1.5'),iterations=42):
    require(bool(function(lo)<0) and bool(function(hi)>0),'strict bracket endpoints')
    for step in range(iterations):
        midpoint=(lo+hi)/2;value=function(midpoint)
        if bool(value<0):lo=midpoint
        elif bool(value>0):hi=midpoint
        else:raise ValueError('scalar root sign unresolved')
    require(bool(function(lo)<0) and bool(function(hi)>0),'retained strict boundary bracket')
    return {'a_interval':[str(lo),str(hi)],'m_interval':[str(2*lo-1),str(2*hi-1)],
            'm_lower_ball':str(as_arb(2*lo-1)),'m_upper_ball':str(as_arb(2*hi-1)),
            'function_lower_ball':str(function(lo)),'function_upper_ball':str(function(hi)),
            'both_strict_endpoint_signs_certified':True}


def run():
    ctx.prec=192;mu=mobius_sieve(80)
    records={'V_less_than_three_guard':bracket(lambda a:3-prime_power_sum(a,1,mu))}
    for pairs in [1,2,3]:
        degree=2*pairs+1
        def function(a):
            W,e=elementary(a,degree,mu)
            return sum(((-1)**j*e[j] for j in range(degree+1)),arb(0))
        records[f'ideal_complete_{pairs}_even_pairs']=bracket(function)
    return {'status':'PASS_FIXED_PAIR_BARRIERS','arithmetic':'ARB_DIRECTED_BALLS_EXACT_RATIONAL_BISECTION',
            'precision_bits':ctx.prec,'records':records,
            'boundaries_are_method_barriers_not_native_counterexamples':True,
            'critical_power_one_proved':False,'rh_proved':False,
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path)
    args=p.parse_args();result=run();text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')

if __name__=='__main__':main()
