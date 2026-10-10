#!/usr/bin/env python3
"""Exact quartet-factor and count-margin controls for a modified source."""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)


def cmul(a,b):
    return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]


def quartet(z,R,d):
    first=cmul((z[0]-R,z[1]),(z[0]-R,z[1]))
    second=cmul((z[0]+R,z[1]),(z[0]+R,z[1]))
    return cmul((first[0]+d*d,first[1]),(second[0]+d*d,second[1]))


def run():
    R,d,H=10**50,Q(1,4),3*10**12
    need(R>H and 0<d<Q(3,8)<Q(1,2), 'preserved census and strip')
    roots=[(Q(sign*R),isign*d) for sign in [-1,1] for isign in [-1,1]]
    need(len(set(roots))==4, 'four distinct off-real locations')
    need(all(quartet(z,R,d)==(0,0) for z in roots), 'exact quartet factorization')
    denominator=quartet((Q(0),Q(1,2)),R,d)
    need(denominator[1]==0 and denominator[0]>0, 'positive endpoint normalization')
    original_constant=Q(251,100)+Q(7,8)
    need(original_constant==Q(677,200), 'count constant')
    slope=Q(14,125)+Q(139,500)/8
    need(slope==Q(587,4000), 'logarithmic slope')
    final_constant=original_constant+1+2
    need(final_constant==Q(1277,200), 'upper-half-plane multiplicity added')
    gap=(Q(1,4)-slope)*100-final_constant
    need(gap==Q(197,50) and gap>0, 'uniform high-count gap')
    # e<3 gives log(10)>2, hence log(R)>100. For u>=100,
    # log u<u/8 follows at100 from e^5>100, then monotonicity.
    exp5_lower=sum((Q(5)**j / factorial(j) for j in range(11)),Q(0))
    need(exp5_lower>100 and 5<Q(100,8), 'elementary logarithmic guard')
    return {'status':'PASS_EXACT_MODIFIED_SOURCE_FINITE_ORDER_FIREWALL',
            'R':str(R),'d':str(d),'added_upper_zeros':2,
            'count_gap_at_log_T_100':str(gap),
            'actual_xi_modified':False,'actual_high_zero_located':False,
            'rh_proved':False,
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def factorial(n):
    value=1
    for j in range(2,n+1):
        value*=j
    return value


if __name__=='__main__':
    print(json.dumps(run(),indent=2)+'\n',end='')
