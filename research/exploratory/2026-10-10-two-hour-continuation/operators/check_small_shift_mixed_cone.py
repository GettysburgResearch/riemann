#!/usr/bin/env python3
"""Exact source/rational guards for the complete t1 mixed-moment cone."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPLORATORY = HERE.parent.parent


def need(ok: bool, message: str) -> None:
    if not ok:
        raise SystemExit('FAIL: ' + message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'small_shift_mixed_cone.json')
    args = parser.parse_args()
    baseline = HERE/'finite_census_mixed_cone.normal.json'
    need(sha(baseline) == 'bffb559967304c3ccb46c6a185d03bed376be5a46dd84394852c68bea39b427f',
         'reviewed source adapter identity')
    inherited = json.loads(baseline.read_text())
    need(inherited['status'] == 'PASS_EXACT_COMPLETE_INFINITE_MIXED_MOMENT_CONE_GUARDS'
         and inherited['complete_real_head'] == 5419
         and inherited['historical_zero_count_used'] is False,
         'complete actual real-head source scope')
    for path,expected in inherited['source_sha256'].items():
        need(sha(EXPLORATORY/path) == expected, 'direct inherited source ' + path)
    census_path=EXPLORATORY/'2026-10-10-four-hour-wave/xi/outer-ray/sixteenth_moment_census.json'
    census=json.loads(census_path.read_text())
    for path,expected in census['source_sha256'].items():
        need(sha(EXPLORATORY/'2026-10-10-four-hour-wave'/path) == expected,
             'native head transitive source ' + path)
    candidate_path=EXPLORATORY/'2026-10-10-four-hour-wave/xi/outer-ray/native_candidates.json'
    candidate=json.loads(candidate_path.read_text())
    first_lo,first_hi=candidate['interval_numerators'][0]
    denominator=candidate['denominator']
    lower,upper=Q(141347,10000),Q(141348,10000)
    need(lower<Q(first_lo,denominator)<Q(first_hi,denominator)<upper,
         'same native real occurrence inside tight physical interval')
    R,A,t=Q(5419),Q(1,2),Q(1)
    c,a,B=t*t-A*A,lower**2+A*A,upper**2+t*t
    total=R*R+c
    r,s=B/total,B/a
    need(t>A and t*t>=3*A*A and R>=1024, 'source norm/count domains')
    need((c,a,B,total)==(Q(3,4),Q(20003974409,100000000),Q(1254953569,6250000),Q(117462247,4)),
         'exact physical t1 constants')
    need(r==Q(1254953569,183534760937500) and s==Q(692388176,689792221),
         'exact spectral ratios')
    need(0<r<1 and s>1 and 2*B*r*s**1500<Q(4,5) and r*s**3100<Q(4,5),
         'strict infinite-cone guards')
    sources=[Path(__file__).resolve(),HERE/'SMALL_SHIFT_MIXED_CONE.md',baseline,
             HERE/'FINITE_CENSUS_MIXED_MOMENT_CONE.md',
             HERE/'check_finite_census_mixed_cone.py',candidate_path]
    result={
        'status':'PASS_EXACT_COMPLETE_SMALL_SHIFT_INFINITE_MIXED_CONE_GUARDS',
        'normalization':'D_nj(1)=sum_h(-1)^h binom(j,h)(3/4)^(n+h) C_(n+h+1)(1)',
        'physical_shift':'1','complete_real_head':5419,'strip_half_width':'1/2',
        'coverage':'EVERY integern,j>=0 satisfying j<=3100*(n-1)+1500; complete actual source',
        'constants':{'c':str(c),'a':str(a),'B':str(B),'Q':str(total),'r':str(r),'s':str(s)},
        'actual_first_root_outer_interval':[str(lower),str(upper)],
        'exact_base_ratio_upper_bound':'4/5',
        'exact_base_exponent':1500,'exact_block_exponent':3100,
        'exact_block_ratio_upper_bound':'4/5',
        'uniform_tail_to_selected_head_ratio_bound':'(4/5)^n',
        'whole_unknown_complex_tail_retained':True,
        'new_native_moment_root_or_quadrature_replay':False,
        'historical_zero_count_used':False,'all_mixed_pairs_covered':False,'RH_proved':False,
        'infinite_analytic_proof_imported':True,
        'source_sha256':{str(p.relative_to(EXPLORATORY)):sha(p) for p in sources},
        'inherited_source_sha256':inherited['source_sha256'],
    }
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],flush=True)


if __name__=='__main__':
    main()
