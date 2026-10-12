#!/usr/bin/env python3
"""Exact controls for the separately scoped optimized count/strip corollary."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

HERE=Path(__file__).resolve().parent
WAVE=HERE.parents[1]
HEIGHTS=HERE.parent
H=3000000000000
N0=850000
D=Q(3191,5000)
C1=Q(6383,10000)
C2=Q(2037,5000)


def need(condition:bool,message:str)->None:
    if not condition:
        raise SystemExit('FAIL: '+message)


def digest(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exponential_upper(x:Q,degree:int=8)->Q:
    need(0<=x<degree+2,'full positive exponential tail domain')
    partial=sum((x**k/math.factorial(k) for k in range(degree+1)),Q(0))
    first=x**(degree+1)/math.factorial(degree+1)
    return partial+first/(1-x/(degree+2))


def maximum_even(t:int,q:Q)->int:
    n=math.isqrt((q.numerator*t)//q.denominator)
    n-=n%2
    need(n*n<=q*t<(n+2)**2,'literal maximal even paid order')
    return n


def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    need(digest(HEIGHTS/'DOUBLE_COUNT_PICK.md')=='23e67ff10510aa7b27b497cd58e7e8a6f1a874c1fe3a9099ba5b7651df7a74b0','frozen source proof binding')
    a,b,theta=Q(2067,1000),Q(59,1000),Q(1,141)
    L=Q(28729,1000)
    c0=a/L
    ca=b+c0
    need(c0==Q(2067,28729)>theta,'constant allowance pays accumulated theta log')
    need(ca==Q(3762011,28729000),'strict optimized count primitive coefficient')
    # For x=logT>=L and v=log(t/T)>=0, the reserve is
    # c0*(x+v)-(a+theta*v)=c0*(x-L)+(c0-theta)*v.
    need(c0>0 and c0-theta>0 and c0*L==a,'all-variable logarithmic reserve identity')
    C=C2+C1*C1
    J=4*ca*C
    need(J==Q(306538772327579,718225000000000),'twice-integrated exact quadrature coefficient')
    need(D+Q(3,N0)<C1,'uniform first derivative guard')
    need(D*D+(Q(6,N0)+Q(1,N0*N0))*D+Q(9,N0*N0)+Q(7,N0**3)<C2,'uniform second derivative guard')
    low=Q(113,355)*(1-Q(1838,28729))
    high=Q(106,333)
    need(0<low<high,'strict complete density order')
    specs=[(Q(1,2),Q(667,1000),Q(1531,1000),Q(4257,10000),1414000,
            Q(762345376598329967484512648703103327298527,6792397470000000000000000000000000000000000000)),
           (Q(3,8),Q(731,1000),Q(71,50),Q(7,20),1480000,
            Q(73091897928132099409751855017013608382087,30188433200000000000000000000000000000000000))]
    cases=[]
    for A,q,kappa,expbound,globalorder,expectedgap in specs:
        need(0<A<=Q(1,2),'uniform displacement domain')
        expactual=2*A*(D+Q(2,N0))*q
        need(expactual<expbound,'uniform arbitrary-variable amplification exponent')
        expupper=exponential_upper(expbound)
        need(expupper<kappa,'complete rational exponential upper enclosure')
        gap=low-J*q*q-A*A*C*kappa*kappa*q*q*(high+J*q*q)
        need(gap==expectedgap>0,'literal strict complete-source endpoint gap')
        need(globalorder**2<q*H,'global headline order paid at every common cutoff')
        maximum=maximum_even(H,q)
        need(maximum=={Q(1,2):1414566,Q(3,8):1480878}[A],'literal maximal even order at H0')
        cases.append({'complete_displacement_bound':str(A),'q0_exact':str(q),
                      'amplification_exact':str(kappa),'exponent_at_N0_exact':str(expactual),
                      'exponent_upper_exact':str(expbound),'full_exponential_upper_exact':str(expupper),
                      'endpoint_gap_exact':str(gap),'endpoint_gap_decimal':float(gap),
                      'global_order':globalorder,'maximal_even_order_at_H0':maximum,
                      'additional_uniform_strip_hypothesis':A<Q(1,2),
                      'selectable_tail_examples':[{'height':t,'even_order':maximum_even(t,q)}
                                                  for t in [H,10**14,10**18,10**24,10**36]]})
    need(3000175332800>H+20,'complete common-cutoff interval within imported census')
    paths=[Path(__file__).resolve(),HERE/'OPTIMIZED_DOUBLE_COUNT.md']
    paths.extend(HEIGHTS/name for name in ['DOUBLE_COUNT_PICK.md','verify_double_count.py',
        'GOOD_CUTOFF_PICK.md','DENSITY_RATIONAL_REFINEMENT.md','VOLTERRA_RATIONAL_REFINEMENT.md',
        'WEIGHTED_RATIONAL_DILATION.md','ANNULAR_GLOBAL_PICK.md'])
    paths.extend(WAVE/'literature'/name for name in ['TRUDGIAN_TURING_SOURCE_RECORD.md','PRIMARY_SOURCES.md'])
    report={'status':'PASS_EXACT_OPTIMIZED_DOUBLE_COUNT_CONTROLS','minimum_height':H,'minimum_order':N0,
            'optimized_primitive_coefficient_exact':str(ca),'constant_allowance_per_log_exact':str(c0),
            'theta_primitive_coefficient_exact':str(theta),'quadrature_coefficient_exact':str(J),
            'all_variable_logarithmic_reserve_coefficients_nonnegative':True,
            'arbitrary_individual_displacements_retained':True,'cases':cases,
            'published_Turing_integral_or_critical_census_replayed':False,
            'optional_quasi_RH_strip_proof_or_formal_solution_replayed':False,
            'global_critical_census_used':True,'tail_critical_census_used':False,
            'cutoff_computed':False,'rh_proved':False,
            'source_sha256':{str(path.relative_to(WAVE)):digest(path) for path in paths}}
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(report['status'],flush=True)


if __name__=='__main__':
    main()
