#!/usr/bin/env python3
"""Directed finite residue obstruction; nonresonance remains an assumption."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
from flint import acb, acb_series, arb, ctx


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def aq(q):
    return arb(q.numerator)/q.denominator


def hardy_z(t):
    theta=acb(arb(1)/4,t/2).lgamma().imag-t*arb.pi().log()/2
    return acb(0,theta).exp()*acb(arb(1)/2,t).zeta()


def run(count, bits, degree):
    require(count>=1 and bits>=80 and degree>=1, 'domains')
    ctx.prec=bits;ctx.cap=2
    denominator=2**20
    records=[];total=arb(0);previous=Q(0)
    for j in range(1,count+1):
        # This library output proposes locations only; signs below certify zeros.
        proposal=acb.zeta_zero(j)
        q=math.floor(float(proposal.imag)*denominator)
        low,high=Q(q,denominator),Q(q+1,denominator)
        require(previous<low<high, 'disjoint positive exact brackets')
        previous=high
        signs=[]
        for endpoint in (low,high):
            z=hardy_z(aq(endpoint))
            require(z.imag.contains(0), 'Hardy-Z reality consistency')
            require(bool(z.real>0) or bool(z.real<0), 'strict endpoint sign')
            signs.append(1 if bool(z.real>0) else -1)
        require(signs[0]!=signs[1], 'critical zero existence by IVT')
        t=arb(aq((low+high)/2),aq((high-low)/2))
        rho=acb(arb(1)/2,t)
        zeta=rho.zeta()
        derivative=acb_series([rho,1],2).zeta()[1]
        require(not derivative.contains(0), 'simple critical zeros throughout bracket')
        theta=acb(arb(1)/4,t/2).lgamma().imag-t*arb.pi().log()/2
        theta_prime=(acb(arb(1)/4,t/2).digamma().real-arb.pi().log())/2
        zprime=acb(0,1)*acb(0,theta).exp()*(theta_prime*zeta+derivative)
        require(zprime.imag.contains(0), 'Hardy-Z derivative reality consistency')
        require(bool(zprime.real>0) or bool(zprime.real<0), 'unique line crossing')
        residue=(1-acb(67)**(-rho))*(rho+1)/((rho-acb(arb(1)/2))*(rho-1)*derivative)
        magnitude=abs(residue)
        require(bool(magnitude>0), 'strict residue magnitude')
        total+=magnitude
        records.append({'proposal_index':j,'interval':[str(low),str(high)],
            'endpoint_signs':signs,'derivative_ball':str(derivative),
            'hardy_z_derivative_real_ball':str(zprime.real),
            'residue_ball':str(residue),'absolute_residue_ball':str(magnitude)})
    a0=-3*(1-arb(67)**(-arb(1)/2))/ (arb(1)/2).zeta()
    margin=2*arb(degree)/(degree+1)*total-a0
    require(bool(a0>0), 'constant residue positive')
    require(bool(margin>arb(1)/50), 'finite Fejer obstruction exceeds 1/50')
    return {'status':'PASS_CONDITIONAL_CRITICAL_SIGN_RESIDUE_TARGET',
        'arithmetic':'DIRECTED_ARB_BALLS_AND_EXACT_DYADIC_ENDPOINTS',
        'precision_bits':bits,'python_flint_version':importlib.metadata.version('python-flint'),
        'certified_distinct_simple_critical_zeros':count,'fejer_degree':degree,
        'sum_absolute_residues_ball':str(total),'constant_residue_ball':str(a0),
        'strict_margin_ball':str(margin),'certified_margin_lower_bound':'1/50',
        'nonresonance_certified':False,
        'unconditional_negative_value_certified':False,'rh_proved':False,
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'zero_intervals_and_residues':records}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--count',type=int,default=1000)
    parser.add_argument('--bits',type=int,default=128)
    parser.add_argument('--degree',type=int,default=9)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run(args.count,args.bits,args.degree)
    rendered=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(rendered)
    print(json.dumps({k:v for k,v in result.items() if k!='zero_intervals_and_residues'},indent=2))
