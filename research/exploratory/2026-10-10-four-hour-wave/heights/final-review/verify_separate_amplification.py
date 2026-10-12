#!/usr/bin/env python3
"""Exact complete series/derivative/source payment with separate amplitudes."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from fractions import Fraction as Q
from verify_optimized_double_count import exponential_upper,maximum_even

HERE=Path(__file__).resolve().parent
WAVE=HERE.parents[1]


def need(condition:bool,message:str)->None:
    if not condition:raise SystemExit('FAIL: '+message)


def digest(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()


def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    need(digest(HERE/'VOLTERRA_SQUARE_DOUBLE_COUNT.md')=='f749951aa06421b4856d26ff795127f22649980371d16b619e4003df0dba6629','frozen square predecessor')
    N,H=850000,3000000000000
    d,e=Q(3191,5000),Q(2907,10000)
    r=e/(d*d)
    need(0<r<1,'strict complete square improvement')
    C1,C2=Q(6383,10000),Q(291,1000)
    need(d+Q(24,5*N)<C1,'all-variable first derivative finite prefactor reserve')
    C=C2+C1*C1
    J=4*Q(3762011,28729000)*C
    low=Q(113,355)*(1-Q(1838,28729));high=Q(106,333)
    p=Q(500001,500000)
    cases=[]
    for A,q,order,expectedmaximum in [(Q(1,2),Q(727,1000),1476000,1476820),
                                      (Q(3,8),Q(199,250),1545000,1545314)]:
        need(exponential_upper(4*A*q/N)<p,'whole signed-pole prefactor exponential')
        xi=2*A*d*q
        E=exponential_upper(xi)
        need(E>1+xi,'positive complete exponential tail')
        S0=p*(1+xi+r*(E-1-xi));S1=p*(1+r*(E-1));S2=p*E
        need(1<=S1<=S0<=S2<Q(8,5),'all uniform amplitude and ratio guards')
        payment=C2*S2*S0+C1*C1*S1*S1
        gap=low-J*q*q-A*A*payment*q*q*(high+J*q*q)
        need(gap>0,'strict complete-source separate-amplitude gap')
        need(order**2<q*H,'global complete-source headline payment')
        maximum=maximum_even(H,q)
        need(maximum==expectedmaximum,'literal maximal even order at H0')
        cases.append({'complete_displacement_bound':str(A),'q0_exact':str(q),'global_order':order,
                      'maximal_even_order_at_H0':maximum,'polynomial_exponent_exact':str(xi),
                      'complete_exponential_upper_exact':str(E),'prefactor_upper_exact':str(p),
                      'R_amplitude_exact':str(S0),'Rprime_amplitude_exact':str(S1),'Rsecond_amplitude_exact':str(S2),
                      'full_product_rule_coefficient_exact':str(payment),'strict_gap_exact':str(gap),
                      'strict_gap_decimal':float(gap),'additional_uniform_strip_hypothesis':A<Q(1,2),
                      'selectable_tail_examples':[{'height':t,'even_order':maximum_even(t,q)}
                                                  for t in [H,10**14,10**18,10**24,10**36]]})
    paths=[Path(__file__).resolve(),HERE/'SEPARATE_DERIVATIVE_AMPLIFICATION.md',
           HERE/'VOLTERRA_SQUARE_DOUBLE_COUNT.md',HERE/'verify_volterra_square.py',
           HERE/'OPTIMIZED_DOUBLE_COUNT.md',HERE/'verify_optimized_double_count.py',
           HERE.parent/'WEIGHTED_RATIONAL_DILATION.md']
    report={'status':'PASS_EXACT_SEPARATE_DERIVATIVE_AMPLIFICATION','minimum_order':N,'minimum_height':H,
            'complete_square_to_norm_ratio_exact':str(r),'quadrature_coefficient_exact':str(J),'cases':cases,
            'all_full_series_and_variable_displacement_paths_retained':True,
            'finite_controls_authenticate_complete_operator_proof':False,
            'Turing_published_census_or_optional_narrower_strip_replayed':False,
            'global_critical_census_used':True,'tail_critical_census_used':False,'cutoff_computed':False,'rh_proved':False,
            'source_sha256':{str(path.relative_to(WAVE)):digest(path) for path in paths}}
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(report['status'],flush=True)


if __name__=='__main__':main()
