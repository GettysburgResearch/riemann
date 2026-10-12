#!/usr/bin/env python3
"""Exact compression/operator/payment controls for the Volterra square proof."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from verify_optimized_double_count import exponential_upper, maximum_even

HERE=Path(__file__).resolve().parent
WAVE=HERE.parents[1]
N=850000
H=3000000000000


def need(condition:bool,message:str)->None:
    if not condition:
        raise SystemExit('FAIL: '+message)


def digest(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compression_controls()->list[dict]:
    rows=[]
    for n in range(1,13):
        for kind in ['uniform','unequal_with_zero']:
            e=[Q(1)]*n if kind=='uniform' else [Q(0) if i%4==3 else Q(1,i+1) for i in range(n)]
            masses=[x*x for x in e]
            edges=[Q(0)]
            for m in masses:edges.append(edges[-1]+m)
            u=[[e[i]*e[j] if i<j else Q(0) for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    square=sum((u[i][k]*u[k][j] for k in range(n)),Q(0))
                    if e[i]==0 or e[j]==0: integral=Q(0)
                    elif i<j:
                        # Independently integrate s-t over two disjoint cells.
                        il,ih,jl,jh=edges[i],edges[i+1],edges[j],edges[j+1]
                        integral=((ih-il)*(jh*jh-jl*jl)-(jh-jl)*(ih*ih-il*il))/(2*e[i]*e[j])
                    elif i==j:integral=masses[i]**2/6
                    else:integral=Q(0)
                    formula=(e[i]*e[j]*(sum(masses[i+1:j],Q(0))+(masses[i]+masses[j])/2) if i<j
                             else masses[i]**2/6 if i==j else Q(0))
                    need(integral==formula and Q(0)<=square<=integral,'literal compressed V square and entrywise domination')
            rows.append({'dimension':n,'kind':kind,'trace':str(sum(masses,Q(0)))})
    return rows


def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    need(digest(HERE/'OPTIMIZED_DOUBLE_COUNT.md')=='4a760969f52d03199ce38fcd29ad787382d9c61e4009f6f3cd79dd7e19d9c5c9','frozen optimized predecessor')
    b=(2+Q(1,28*N))/1300+Q(1,N)
    u=Q(200000,314159)
    hs=Q(288676,1000000)
    need(12*hs*hs>1 and 1300**2<2*N,'complete Hilbert-Schmidt and dimension square-root guards')
    bound=hs+2*u*b+b*b
    e0=Q(2907,10000)
    need(bound<e0,'complete dilation square uniform guard')
    d=Q(3191,5000)
    c1=Q(6383,10000)
    c2=Q(291,1000)
    need(d+Q(3,N)<c1,'unchanged first derivative guard')
    need(e0+(Q(6,N)+Q(1,N*N))*d+Q(9,N*N)+Q(7,N**3)<c2,'new complete second derivative guard')
    C=c2+c1*c1
    ca=Q(3762011,28729000)
    J=4*ca*C
    low=Q(113,355)*(1-Q(1838,28729));high=Q(106,333)
    cases=[]
    for A,q,kappa,expbound,order,expectedgap in [
        (Q(1,2),Q(713,1000),Q(1577,1000),Q(4551,10000),1462000,
         Q(4375993412166867933228645792648959018712823,6792397470000000000000000000000000000000000000)),
        (Q(3,8),Q(787,1000),Q(729,500),Q(3767,10000),1536000,
         Q(2707828754395387643273072991404578154931367,3018843320000000000000000000000000000000000000))]:
        exponent=2*A*(d+Q(2,N))*q
        need(exponent<expbound,'complete arbitrary-path amplification exponent')
        expupper=exponential_upper(expbound)
        need(expupper<kappa,'complete exponential positive tail')
        gap=low-J*q*q-A*A*C*kappa*kappa*q*q*(high+J*q*q)
        need(gap==expectedgap>0,'literal strict complete-source gap')
        need(order**2<q*H,'global headline source payment')
        maximum=maximum_even(H,q)
        need(maximum=={Q(1,2):1462532,Q(3,8):1536554}[A],'maximal even order at H0')
        cases.append({'complete_displacement_bound':str(A),'q0_exact':str(q),'amplification_exact':str(kappa),
                      'exponent_upper_exact':str(expbound),'full_exponential_upper_exact':str(expupper),
                      'gap_exact':str(gap),'global_order':order,'maximal_even_order_at_H0':maximum,
                      'additional_uniform_strip_hypothesis':A<Q(1,2),
                      'selectable_tail_examples':[{'height':t,'even_order':maximum_even(t,q)}
                                                  for t in [H,10**14,10**18,10**24,10**36]]})
    paths=[Path(__file__).resolve(),HERE/'VOLTERRA_SQUARE_DOUBLE_COUNT.md',HERE/'verify_optimized_double_count.py',
           HERE/'OPTIMIZED_DOUBLE_COUNT.md',HERE.parent/'VOLTERRA_RATIONAL_REFINEMENT.md',
           HERE.parent/'WEIGHTED_RATIONAL_DILATION.md',HERE.parent/'DOUBLE_COUNT_PICK.md']
    report={'status':'PASS_EXACT_VOLTERRA_SQUARE_COMPLETE_SOURCE_CONTROLS','minimum_order':N,'minimum_height':H,
            'normalized_small_matrix_bound_exact':str(b),'dilation_square_endpoint_upper_exact':str(bound),
            'dilation_square_uniform_constant':str(e0),'new_second_derivative_constant':str(c2),
            'quadrature_coefficient_exact':str(J),'compression_controls':compression_controls(),'cases':cases,
            'full_operator_analytic_proof_authenticated_by_finite_controls':False,
            'Turing_census_or_optional_narrower_strip_proof_replayed':False,
            'global_critical_census_used':True,'tail_critical_census_used':False,'cutoff_computed':False,'rh_proved':False,
            'source_sha256':{str(path.relative_to(WAVE)):digest(path) for path in paths}}
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(report['status'],flush=True)


if __name__=='__main__':main()
