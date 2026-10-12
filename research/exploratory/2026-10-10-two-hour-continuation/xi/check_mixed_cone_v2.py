#!/usr/bin/env python3
"""Exact finite phase rectangle from an explicitly imported count-free head."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPLORATORY = HERE.parent.parent
OLD = EXPLORATORY/'2026-10-10-four-hour-wave'


def need(ok: bool, why: str) -> None:
    if not ok:
        raise SystemExit('FAIL: '+why)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'mixed_cone_v2.json')
    args=parser.parse_args()
    source=OLD/'xi/outer-ray/sixteenth_moment_census.json'
    need(sha(source)=='964f49cc79a61b354cd77fe1f077637e54bb46f39a5643e1455e87f60fabc4d6','frozen count-free source')
    prior=json.loads(source.read_text())
    need(prior['status']=='PASS_DIRECTED_COUNT_FREE_SIXTEENTH_MOMENT_CENSUS'
         and prior['historical_Gram_Rosser_contract_used_by_this_theorem'] is False
         and any(x['height']==5419 and x['recovered_complete_simple_positive_zero_count']==4968
                 for x in prior['recovered_domains']), 'explicit imported real-head scope')
    for path,expected in prior['source_sha256'].items():
        need(sha(OLD/path)==expected,'prior direct source '+path)
    R,A,t,nmax,jmax=Q(5419),Q(1,2),Q(512),8000,900000
    need(R>0 and t>A>=0,'positive phase domain')
    first=(nmax+1)*2*A/R
    second=jmax*2*A*(t*t-A*A)/R**3
    need(first==Q(8001,5419) and second==Q(235929375000,159131975059),'exact extreme phase values')
    need(first<Q(3,2) and second<Q(3,2),'complete rectangle strict phase guards')
    paths=[Path(__file__).resolve(),HERE/'MIXED_MOMENT_CONE_V2.md',HERE/'SHIFTED_COMPLETE_MOMENTS_V2.md',source,
           OLD/'xi/outer-ray/SIXTEENTH_MOMENT_CENSUS_RECOVERY.md',OLD/'xi/outer-ray/THEOREM.md']
    result={'status':'PASS_EXACT_FINITE_MIXED_MOMENT_PHASE_RECTANGLE',
            'normalization':'Xi(z)=xi(1/2+i*z)','shift':'512','complete_strip_half_width':'1/2',
            'imported_count_free_real_head':5419,'n_range':[0,nmax],'difference_degree_range':[0,jmax],
            'coverage':'Entire integer rectangle by two monotone extreme phase inequalities and complete analytic source proof.',
            'first_phase_extreme':str(first),'second_phase_extreme':str(second),
            'pi_lower_bound':'pi>3, elementary analytic input','new_native_primitive_replay':False,
            'individual_mixed_coefficient_enumeration':False,'historical_complete_zero_count_used':False,
            'all_unbounded_mixed_moment_signs_proved':False,'rh_proved':False,
            'source_sha256':{str(p.relative_to(EXPLORATORY)):sha(p) for p in paths}}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],flush=True)


if __name__=='__main__':
    main()
