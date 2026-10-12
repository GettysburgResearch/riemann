#!/usr/bin/env python3
"""Exact finite source/phase guards for an infinite actual-Xi heat cone."""
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
PRIOR=OLD/'xi/outer-ray'


def need(ok: bool, message: str) -> None:
    if not ok:
        raise SystemExit('FAIL: '+message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'heat_derivative_cone.json')
    args=parser.parse_args()
    receipt_path=PRIOR/'sixteenth_moment_census.json'
    need(sha(receipt_path)=='964f49cc79a61b354cd77fe1f077637e54bb46f39a5643e1455e87f60fabc4d6',
         'frozen count-free census identity')
    prior=json.loads(receipt_path.read_text())
    need(prior['status']=='PASS_DIRECTED_COUNT_FREE_SIXTEENTH_MOMENT_CENSUS'
         and prior['historical_Gram_Rosser_contract_used_by_this_theorem'] is False
         and any(x['height']==5419 and x['recovered_complete_simple_positive_zero_count']==4968
                 for x in prior['recovered_domains']),'explicit complete real-head scope')
    for path,expected in prior['source_sha256'].items():
        need(sha(OLD/path)==expected,'prior direct source '+path)
    candidates_path=PRIOR/'native_candidates.json'
    candidates=json.loads(candidates_path.read_text())
    need(candidates['normalization']=='Xi(z)=xi(1/2+i*z)','source normalization')
    lo,hi=candidates['interval_numerators'][0]
    denominator=candidates['denominator']
    need(14<Q(lo,denominator)<Q(hi,denominator)<15,'selected actual root interval in14..15')
    R,A,l,b=Q(5419),Q(1,2),Q(14),Q(15)
    e_lower=sum((Q(1,factorial(j)) for j in range(5)),Q(0))
    need(e_lower==Q(65,24)>Q(27,10),'exact exponential series lower bound')
    W=(R*R+A*A)/(l*l)
    need(W<Q(27,10)**12 and R*R+2<Q(27,10)**18,'full tail/head logarithmic upper bounds')
    margin=Q(5,8)*R*R-(18+b*b+A*A)
    need(margin==Q(146825859,8)>0,'strict entire-cone tail margin')
    order_at_one=int(R*R/Q(32))
    need(order_at_one==917673,'exact u1 derivative range')
    sources=[Path(__file__).resolve(),HERE/'FINITE_CENSUS_HEAT_DERIVATIVE_CONE.md',
             HERE/'COMPLETE_PRIME_HEAT_TRACE.md',receipt_path,candidates_path,
             PRIOR/'SIXTEENTH_MOMENT_CENSUS_RECOVERY.md',OLD/'heights/COARSE_ZERO_COUNT.md',
             PRIOR/'THEOREM.md']
    result={'status':'PASS_EXACT_COMPLETE_HEAT_DERIVATIVE_CONE_GUARDS',
            'normalization':'K(u)=sum_(Re rho>0)m_rho exp(-rho^2*u), Xi(z)=xi(1/2+i*z)',
            'imported_complete_count_free_real_head':5419,'complete_strip_half_width':'1/2',
            'complete_actual_source_upper_count_imported':'N(T)<T logT<=T^2 for everyT>=1024',
            'known_actual_real_root_interval':[str(Q(lo,denominator)),str(Q(hi,denominator))],
            'coverage':'All real u>=1 and all integer0<=r<=u*5419^2/32 by complete analytic proof.',
            'maximum_integer_order_at_u_one':order_at_one,'exact_exponential_lower_bound':str(e_lower),
            'exact_final_tail_head_log_margin_coefficient':str(margin),
            'new_native_root_or_heat_replay':False,'historical_zero_count_used':False,
            'all_positive_times_and_all_derivative_orders_covered':False,'RH_proved':False,
            'infinite_analytic_source_and_coverage_proof_imported':True,
            'source_sha256':{str(p.relative_to(EXPLORATORY)):sha(p) for p in sources}}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],flush=True)


if __name__=='__main__':
    main()
