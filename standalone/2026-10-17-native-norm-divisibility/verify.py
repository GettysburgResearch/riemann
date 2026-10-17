#!/usr/bin/env python3
"""Reproduce finite algebra checks and a rigorous bound for an infinite constant.

Run from any working directory. --quick skips the long certificate, not the
coefficient/ratio/kernel checks. There are no assertions disabled by python -O.
"""
import argparse
import json
from collections import defaultdict
from fractions import Fraction as F
from math import gcd
from pathlib import Path

from arithmetic import coefficient_arrays, enumerate_squarefree_ideals, factor, shared_divisors, q_at_one
from intervals import I, SCALE, BITS, gaussian_ratio_weight, certified_tails, log_int, exp_minus


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def mobius_array(cap):
    # Independent rational-integer definition by divisibility, not local_a.
    mu=[1]*(cap+1)
    mu[0]=0
    prime=[True]*(cap+1)
    prime[0]=prime[1]=False
    for p in range(2,cap+1):
        if prime[p]:
            for n in range(p,cap+1,p):
                mu[n]*=-1
                if n>p:
                    prime[n]=False
            for n in range(p*p,cap+1,p*p):
                mu[n]=0
    return mu


def independent_norm_coefficients(cap):
    mu=mobius_array(cap)
    chi=lambda n: (0 if n%3==0 else (1 if n%3==1 else -1))
    out=[0]*(cap+1)
    for d in range(1,cap+1):
        if mu[d]:
            for m in range(1,cap//d+1):
                out[d*m]+=mu[d]*mu[m]*chi(m)
    for n in range(1,cap+1):
        if gcd(n,6)!=1:
            out[n]=0
    return out


def polymul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):
            out[j+k]+=x*y
    return out


def finite_checks():
    cap=4096
    spf,a,b=coefficient_arrays(cap)
    ai=independent_norm_coefficients(cap)
    require(a==ai,'native norm coefficients differ from mu*(chi*mu)')
    ideals=enumerate_squarefree_ideals(1024)
    agg=[0]*1025
    counts=[0]*1025
    for norm,sgn,labels in ideals:
        agg[norm]+=sgn
        counts[norm]+=1
        require(len(labels)==len(set(labels)),'squarefree ideal repeated a prime')
    require(agg==a[:1025],'distinct-ideal aggregation mismatch')
    require(all(abs(x)==y for x,y in zip(agg,counts)), 'native norm-fiber sign failure')

    prefix=0
    ratio_checks=0
    for r in range(1,cap+1):
        prefix+=abs(a[r])
        require(prefix<=3*r,'coefficient prefix bound fails in finite census')
        require(abs(b[r])<=abs(a[r]),'positive arithmetic majorant fails')
        Q=F(1)
        for p,_ in factor(r,spf):
            Q*=q_at_one(p)
        expected=F(a[r])*sum((F(1,d) for d in shared_divisors(r,spf)),F(0))/Q
        require(expected==b[r],f'normalized ratio coefficient mismatch at {r}')
        ratio_checks+=1

    # Raw two-ideal assembly compared with exact norm-ratio/shared-factor reconstruction.
    lim=512
    small=[x for x in ideals if x[0]<=lim]
    direct=defaultdict(int)
    incomparable_ideal_witness=False
    selected_ordered_ideal_pairs=0
    for n,sn,ln in small:
        for m,sm,lm in small:
            if n>m and n%m==0:
                direct[(n,m)]+=sn*sm
                selected_ordered_ideal_pairs+=1
                if n==91 and m==7 and not(set(lm)<=set(ln)):
                    incomparable_ideal_witness=True
    direct={key:value for key,value in direct.items() if value}
    replay=defaultdict(int)
    reconstruction_terms=0
    for r in range(2,lim+1):
        if not a[r]:
            continue
        for d in shared_divisors(r,spf):
            for h in range(1,lim//(r*d)+1):
                if gcd(h,r)==1 and a[h]:
                    replay[(r*d*h,d*h)]+=a[r]*a[h]*a[h]
                    reconstruction_terms+=1
    replay={key:value for key,value in replay.items() if value}
    require(direct==replay,'ratio reconstruction lost a shared factor or ideal multiplicity')
    require(incomparable_ideal_witness,'new sector lacks explicit incomparable ideal witness')
    require(replay[(49,7)]==-2,'split common-prime overlap was erased')
    require(replay[(49,1)]==1 and replay[(7,1)]==-2,'both covariance signs not retained')
    # Two rational kernels: check the entire finite sector, not a sampled pair set.
    for kernel in [lambda n,m:F(1,n+m+1),lambda n,m:F(n+m+3,n*m+1)]:
        v1=sum((v*kernel(*key) for key,v in direct.items()),F(0))
        v2=sum((v*kernel(*key) for key,v in replay.items()),F(0))
        require(v1==v2,'complete finite kernel comparison failed')

    require(polymul([1,4,1],[1,-4,6,-4,1])==[1,0,-9,16,-9,0,1],
            'split square-mass Euler cancellation failed')
    require(polymul([1,0,1],[1,0,-2,0,1])==[1,0,-1,0,-1,0,1],
            'inert square-mass Euler cancellation failed')
    kernel_checks=0
    for c in [F(0),F(1,2),F(5,6),F(2)]:
        beta=2*c-1
        for av in map(F,[-2,-1,0,1,2]):
            for bv in map(F,[-2,-1,0,1,2]):
                for xx in map(F,[-2,0,2]):
                    left=-c*(av-xx)-c*(bv-xx)-(av-xx)**2/4-(bv-xx)**2/4-xx
                    right=-(xx-(av+bv)/2-beta)**2/2-(av+bv)/2+beta**2/2-(av-bv)**2/8
                    require(left==right,'Gaussian kernel square-completion mismatch')
                    kernel_checks+=1

    intervals_checked=0
    for n in [1,2,3,7,13,25,49,64,100,1024,65536]:
        if n==1:
            continue
        test=exp_minus(log_int(n))
        require(test.contains(F(1,n)),f'log-exp reciprocal interval failed at {n}')
        intervals_checked+=1
    return {'norm_coefficients_checked':cap,
            'complete_good_squarefree_ideals_through_1024':len(ideals),
            'complete_good_squarefree_ideals_through_512':len(small),
            'normalized_ratio_coefficients_checked':ratio_checks,
            'selected_one_orientation_ideal_pairs':selected_ordered_ideal_pairs,
            'distinct_norm_pair_keys':len(direct),
            'shared_factor_reconstruction_terms':reconstruction_terms,
            'rational_kernel_checks':2,'gaussian_square_completions':kernel_checks,
            'interval_log_exp_identity_checks':intervals_checked,
            'incomparable_ideal_witness':{'larger_norm':91,'smaller_norm':7}}


def certificate(cap=65536):
    spf,a,b=coefficient_arrays(cap)
    signed=I.exact_fraction(0)
    abs_second=I.exact_fraction(0)
    nonzero=0
    prefix=0
    for n in range(1,cap+1):
        prefix+=abs(a[n])
        require(prefix<=3*n,'complete finite ideal-count majorant failed')
        require(abs(b[n])<=abs(a[n]),'b majorant failed')
        if not b[n]:
            continue
        weight,L=gaussian_ratio_weight(n)
        signed += I.exact_fraction(b[n])*weight
        abs_second += I.exact_fraction(abs(b[n]))*weight*L*L
        nonzero+=1
    tail0,tail2=certified_tails(cap)
    # Only tail upper endpoints are needed. Both tail expressions are positive.
    S_inf=I(signed.lo-tail0.hi,signed.hi+tail0.hi)
    Lambda=2*(1-S_inf)
    C2=I(abs_second.lo,abs_second.hi+tail2.hi)
    require(Lambda.lower_gt(F(2153,1000)),'infinite leading coefficient lower certificate failed')
    require(Lambda.upper_lt(F(2155,1000)),'infinite leading coefficient upper certificate failed')
    require(C2.upper_lt(16),'uniform-center second derivative bound failed')
    uniform=Lambda-C2*F(1,400)
    require(uniform.lower_gt(F(21,10)),'bounded-center cancellation certificate failed')
    return {'cap':cap,'nonzero_rational_ratio_coefficients':nonzero,
            'interval_arithmetic':'integer dyadic intervals, 112 fractional bits',
            'log_series_terms':40,'exp_taylor_degree':40,'exp_squarings':5,
            'finite_S':signed.record(),'absolute_S_tail_bound':tail0.record(),
            'Lambda_zero':Lambda.record(),'finite_absolute_log_second_moment':abs_second.record(),
            'absolute_log_second_moment_tail_bound':tail2.record(),'C2_bound':C2.record(),
            'lower_bound_expression_Lambda0_minus_C2_over_400':uniform.record(),
            'proved_rational_conclusions':['2153/1000 < Lambda(0) < 2155/1000',
                'C2 < 16','Lambda(t) > 21/10 for every |t| <= 1/20'],
            'scope':'infinite-constant enclosure uses the written global ideal-count tail theorem; '
                    'finite coefficient enumeration does not independently certify that theorem'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--quick',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result={'status':'PASS','finite_checks':finite_checks()}
    if not args.quick:
        result['infinite_constant_certificate']=certificate()
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text,end='')

if __name__=='__main__':
    main()
