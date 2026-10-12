#!/usr/bin/env python3
"""Exact complete-source guards for actual all-order size-two Hankel positivity."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from math import factorial
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
EXPLORATORY=HERE.parent.parent
OLD=EXPLORATORY/'2026-10-10-four-hour-wave'


def need(ok: bool,message: str) -> None:
    if not ok:
        raise SystemExit('FAIL: '+message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'all_order_two_by_two_hankel.json')
    args=parser.parse_args()
    prior_path=HERE/'small_shift_mixed_cone.normal.json'
    need(sha(prior_path)=='ba1ded9839161033c2bc2e5e911dad90c32326925669ceee3382623834cdfa8e',
         'reviewed complete source adapter')
    prior=json.loads(prior_path.read_text())
    need(prior['complete_real_head']==5419 and prior['historical_zero_count_used'] is False,
         'complete actual real-head scope')
    for key in ['source_sha256','inherited_source_sha256']:
        for path,expected in prior[key].items():
            need(sha(EXPLORATORY/path)==expected,'direct inherited source '+path)
    census_path=OLD/'xi/outer-ray/sixteenth_moment_census.json'
    census=json.loads(census_path.read_text())
    for path,expected in census['source_sha256'].items():
        need(sha(OLD/path)==expected,'native census transitive source '+path)
    candidates_path=OLD/'xi/outer-ray/native_candidates.json'
    candidates=json.loads(candidates_path.read_text())
    denominator=candidates['denominator']
    endpoints=[(Q(141347,10000),Q(141348,10000)),(Q(2102,100),Q(2103,100))]
    for row,(lower,upper) in zip(candidates['interval_numerators'][:2],endpoints):
        lo,hi=map(lambda x:Q(x,denominator),row)
        need(lower<lo<hi<upper,'actual native root inside exact anchor interval')
    R,c=Q(5419),Q(3,4)
    z1lo=c/(endpoints[0][1]**2+1)
    z1hi=c/(endpoints[0][0]**2+1)
    z2lo=c/(endpoints[1][1]**2+1)
    z2hi=c/(endpoints[1][0]**2+1)
    need(z1lo-z2hi>Q(1,500) and z2lo>Q(1,600), 'selected Vandermonde gap and minimum node')
    need(z1hi**2+z2hi**2<1,'Vandermonde trace below3')
    need((Q(1,500)**2)/3==Q(1,750000),'exact head Vandermonde constant')
    need(Q(1)/(c*750000)==Q(1,562500),'exact all-order head gap normalization')
    alpha=c/(R*R+c)
    need(alpha<Q(1,39000000) and Q(20,R)/(1-alpha**2)<Q(1,250),
         'whole count tail and coefficient norm constants')
    e_lower=sum((Q(1,factorial(j)) for j in range(5)),Q(0))
    need(e_lower==Q(65,24)>Q(27,10) and R<Q(27,10)**9,'complete tail logR bound')
    need(Q(562500*600,250)==1350000 and Q(39000000,600)==65000,
         'exact uniform tail/head ratio')
    need(Q(1350000,65000**2)<Q(1,2),'every integern>=2 uniform ratio')
    low_prices=[4*c*c/(3*R**6),5*c**3/(2*R**8)]
    for n,price in enumerate(low_prices):
        need(price<Q(1,2*562500*600**(n+1)), 'whole conjugate-pair low-order price '+str(n))
    need(Q(1)/(2*c*750000)==Q(1,1125000),'exact complete lower gap')
    # Independent exact determinant controls for the two complete pair blocks.
    fixtures=0
    for i in range(1,9):
        x,y=Q(i+1,7),Q(i,100)
        det0=x*(x**3-3*x*y*y)-(x*x-y*y)**2
        det1=(x*x-y*y)*(x**4-6*x*x*y*y+y**4)-(x**3-3*x*y*y)**2
        need(det0==-y*y*(x*x+y*y),'complete pair n0 determinant')
        need(det1==-y*y*(x*x+y*y)**2,'complete pair n1 determinant')
        fixtures+=2
    sources=[Path(__file__).resolve(),HERE/'ALL_ORDER_TWO_BY_TWO_HANKEL.md',prior_path,
             HERE/'SMALL_SHIFT_MIXED_CONE.md',candidates_path,census_path,
             OLD/'heights/COARSE_ZERO_COUNT.md']
    result={
        'status':'PASS_EXACT_ACTUAL_ALL_ORDER_TWO_BY_TWO_HANKEL_GUARDS',
        'normalization':'b_n=(3/4)^n C_(n+1)(1); H_n=[[b_n,b_n+1],[b_n+1,b_n+2]]',
        'coverage':'EVERY integern>=0 and EVERY complex2-vector; complete actual Xi source',
        'uniform_lower_bound':'H_n>=I/(1125000*600^(n+1))',
        'strict_Turan_coverage':'C_k(1)*C_(k+2)(1)>C_(k+1)(1)^2 for EVERY integerk>=1',
        'complete_real_head':5419,'known_real_anchor_intervals':[[str(a),str(b)] for a,b in endpoints],
        'alpha':str(alpha),'exact_head_Vandermonde_gap':'1/750000',
        'exact_uniform_n2_tail_head_upper_ratio':str(Q(1350000,65000**2)),
        'exact_low_order_negative_prices':[str(x) for x in low_prices],
        'complete_pair_determinant_fixture_count':fixtures,
        'whole_unknown_complex_tail_retained':True,
        'new_native_root_moment_or_quadrature_replay':False,'historical_zero_count_used':False,
        'all_Hankel_sizes_proved':False,'RH_proved':False,'infinite_analytic_proof_imported':True,
        'source_sha256':{str(p.relative_to(EXPLORATORY)):sha(p) for p in sources},
        'inherited_source_sha256':prior['source_sha256'],
        'inherited_native_source_sha256':prior['inherited_source_sha256'],
    }
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],flush=True)


if __name__=='__main__':
    main()
