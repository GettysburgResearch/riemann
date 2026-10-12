#!/usr/bin/env python3
"""Exact actual-source guards for all-order size-four Hankel positivity."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
EXPLORATORY=HERE.parent.parent
OLD=EXPLORATORY/'2026-10-10-four-hour-wave'


def need(ok: bool,message: str) -> None:
    if not ok: raise SystemExit('FAIL: '+message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'all_order_four_by_four_hankel.json')
    args=parser.parse_args()
    baseline=HERE/'all_order_two_by_two_hankel.normal.json'
    need(sha(baseline)=='4c0d4237e0ef7158c9eec5d532b2d65042fe26474f9bdf097e2e220211b084bc',
         'reviewed complete actual source adapter')
    prior=json.loads(baseline.read_text())
    need(prior['complete_real_head']==5419 and prior['historical_zero_count_used'] is False,
         'complete actual source head contract')
    for key in ['source_sha256','inherited_source_sha256','inherited_native_source_sha256']:
        for path,expected in prior[key].items():
            need(sha(EXPLORATORY/path)==expected,'direct actual source '+path)
    census_path=OLD/'xi/outer-ray/sixteenth_moment_census.json'
    census=json.loads(census_path.read_text())
    for path,expected in census['source_sha256'].items():
        need(sha(OLD/path)==expected,'transitive native census source '+path)
    candidates_path=OLD/'xi/outer-ray/native_candidates.json'
    candidates=json.loads(candidates_path.read_text())
    den=candidates['denominator']
    anchors=[(Q(141347,10000),Q(141348,10000)),(Q(2102,100),Q(2103,100)),
             (Q(2501,100),Q(2502,100)),(Q(3042,100),Q(3043,100))]
    need(len(candidates['interval_numerators'])>=4,'four actual root occurrences')
    for row,(lower,upper) in zip(candidates['interval_numerators'][:4],anchors):
        lo,hi=map(lambda x:Q(x,den),row)
        need(lower<lo<hi<upper,'authenticated actual anchor interval')
    R,c=Q(5419),Q(3,4)
    lows=[c/(upper*upper+1) for lower,upper in anchors]
    highs=[c/(lower*lower+1) for lower,upper in anchors]
    gaps={(0,1):500,(0,2):400,(0,3):350,(1,2):2100,(1,3):1200,(2,3):2700}
    for (i,j),reciprocal in gaps.items():
        need(lows[i]-highs[j]>Q(1,reciprocal),'actual Vandermonde gap '+str((i,j)))
    need(lows[3]>Q(1,1250) and max(highs)<Q(1,250),'selected node minimum and numerator norm')
    numerator_norm=1+Q(3,250)**2+Q(3,250**2)**2+Q(1,250**3)**2
    need(numerator_norm<2,'all Lagrange numerator coefficient norms')
    reciprocal_products=[500*400*350,500*2100*1200,400*2100*2700,350*1200*2700]
    inverse_norm_bound=2*sum(v*v for v in reciprocal_products)
    need(inverse_norm_bound==16044560000000000000<20000000000000000000,
         'full inverse Vandermonde Frobenius bound')
    head_denom=15000000000000000000
    need(c*20000000000000000000==head_denom,'complete head normalization')
    alpha=c/(R*R+c)
    need(alpha<Q(1,39000000) and Q(20,R)/(1-alpha*alpha)<Q(1,250),
         'whole tail norm source constants')
    high_ratio=Q(head_denom*1250,250)*Q(1250,39000000)**5
    need(high_ratio<Q(1,2) and Q(1250,39000000)<1,'every integern>=5 high-order price')
    need(1+4*alpha*alpha+9*alpha**4<2,'complete cubic imaginary-polynomial bound')
    need(5/R<1 and 1-Q(1,2)*(5/R)**2>Q(1,2),'all five low-order phase signs')
    need(Q(8,7)*(9+Q(1,7))==Q(512,49),'sharp whole negative-tail count coefficient')
    low_prefactor=Q(2048,49)*c*c/R**7*head_denom*1250
    need(low_prefactor<Q(1,2) and 1250*c/(R*R)<1,'every low-order signed pair price')
    sources=[Path(__file__).resolve(),HERE/'ALL_ORDER_FOUR_BY_FOUR_HANKEL.md',baseline,
             HERE/'ALL_ORDER_TWO_BY_TWO_HANKEL.md',candidates_path,census_path,
             OLD/'heights/COARSE_ZERO_COUNT.md']
    result={
        'status':'PASS_EXACT_ACTUAL_ALL_ORDER_FOUR_BY_FOUR_HANKEL_GUARDS',
        'normalization':'b_n=(3/4)^n C_(n+1)(1); H_n=[b_(n+i+j)] i,j0..3',
        'coverage':'EVERY integern>=0 and EVERY complex4-vector; complete actual Xi source',
        'uniform_lower_bound':'H_n>=I/(30000000000000000000*1250^(n+1))',
        'complete_real_head':5419,
        'actual_root_anchor_intervals':[[str(a),str(b)]for a,b in anchors],
        'exact_inverse_Vandermonde_squared_Frobenius_upper_bound':inverse_norm_bound,
        'exact_low_order_tail_head_upper_prefactor':str(low_prefactor),
        'exact_high_order_n5_tail_head_upper_ratio':str(high_ratio),
        'whole_unknown_complex_tail_retained':True,
        'new_native_root_moment_jet_or_quadrature_replay':False,
        'historical_zero_count_used':False,'all_Hankel_sizes_proved':False,'RH_proved':False,
        'infinite_analytic_proof_imported':True,
        'source_sha256':{str(p.relative_to(EXPLORATORY)):sha(p)for p in sources},
        'inherited_source_sha256':prior['source_sha256'],
        'inherited_native_source_sha256':prior['inherited_native_source_sha256'],
    }
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],flush=True)


if __name__=='__main__': main()
