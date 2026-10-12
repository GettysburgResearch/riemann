#!/usr/bin/env python3
"""Exact source and rational guards for a whole-source infinite mixed cone."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPLORATORY = HERE.parent.parent
OLD = EXPLORATORY / '2026-10-10-four-hour-wave'
PRIOR = OLD / 'xi/outer-ray'
XI = HERE.parent / 'xi'


def need(ok: bool, message: str) -> None:
    if not ok:
        raise SystemExit('FAIL: ' + message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE/'finite_census_mixed_cone.json')
    args = parser.parse_args()
    inherited = XI/'heat_derivative_cone.json'
    need(sha(inherited) == '1708abc0dd320a35d8f753aa20b1330d5fda60c364a6ad678acf3122226a3bcd',
         'frozen actual-source head/count adapter')
    adapter = json.loads(inherited.read_text())
    need(adapter['status'] == 'PASS_EXACT_COMPLETE_HEAT_DERIVATIVE_CONE_GUARDS',
         'accepted source adapter status')
    need(adapter['imported_complete_count_free_real_head'] == 5419
         and adapter['historical_zero_count_used'] is False,
         'complete actual real-head contract')
    for path, expected in adapter['source_sha256'].items():
        need(sha(EXPLORATORY/path) == expected, 'frozen inherited source ' + path)
    census_path = PRIOR/'sixteenth_moment_census.json'
    need(sha(census_path) == '964f49cc79a61b354cd77fe1f077637e54bb46f39a5643e1455e87f60fabc4d6',
         'direct complete native census')
    census = json.loads(census_path.read_text())
    need(any(x['height'] == 5419 and x['recovered_complete_simple_positive_zero_count'] == 4968
             for x in census['recovered_domains']), 'complete real-head scope')
    for path, expected in census['source_sha256'].items():
        need(sha(OLD/path) == expected, 'direct native census source ' + path)
    candidate_path = PRIOR/'native_candidates.json'
    candidates = json.loads(candidate_path.read_text())
    need(candidates['normalization'] == 'Xi(z)=xi(1/2+i*z)', 'actual source normalization')
    lo, hi = candidates['interval_numerators'][0]
    den = candidates['denominator']
    need(14 < Q(lo, den) < Q(hi, den) < 15, 'known actual real occurrence')
    R, A, t = Q(5419), Q(1,2), Q(512)
    c, a, B = t*t-A*A, Q(14)**2+A*A, Q(15)**2+t*t
    total = R*R+c
    need(R >= 1024 and t*t >= 3*A*A, 'complete tail count and norm domains')
    need(a == Q(785,4) and B == 262369 and total == Q(118510819,4),
         'exact physical source constants')
    r, s = B/total, B/a
    need(0 < r < 1 and s > 1, 'ratio domains')
    need(2*B*r**3 < 1 and r**61*s**40 < 1, 'strict infinite cone base and block')
    remainders = []
    for h in range(40):
        power = (61*h+39)//40
        value = r**power*s**h
        need(value <= 1, 'exact remainder ' + str(h))
        remainders.append({'j_remainder':h, 'minimum_n_increment':power,
                           'exact_ratio':str(value)})
    # Controls for the exact closed Stieltjes integral, including the subtracted
    # cQ^(-n-1) term. These do not sample the infinite theorem's n,j domain.
    for n in range(1,41):
        tail_price = Q(n+1,n)*total**(-n)-c*total**(-n-1)
        need(0 < tail_price < 2*total**(-n), 'closed integral price ' + str(n))
    sources = [Path(__file__).resolve(), HERE/'FINITE_CENSUS_MIXED_MOMENT_CONE.md',
               inherited, XI/'FINITE_CENSUS_HEAT_DERIVATIVE_CONE.md',
               XI/'cofinal-audit/LAGUERRE_MIXED_HEAT_IDENTITY.md',
               XI/'cofinal-audit/HAUSDORFF_LOG_MOMENT_CRITERION.md',
               census_path, candidate_path, OLD/'heights/COARSE_ZERO_COUNT.md']
    result = {
        'status':'PASS_EXACT_COMPLETE_INFINITE_MIXED_MOMENT_CONE_GUARDS',
        'normalization':'D_nj=sum_h(-1)^h binom(j,h)c^(n+h) C_(n+h+1)(512)',
        'physical_shift':'512', 'strip_half_width':'1/2', 'complete_real_head':5419,
        'known_actual_real_root_interval':[str(Q(lo,den)),str(Q(hi,den))],
        'complete_tail_upper_count':'N(x)<x log(x)<=x^2 for all realx>=1024',
        'coverage':'EVERY integern,j>=0 with40*n>=61*j+120; full actual source',
        'exact_constants':{'a':str(a),'B':str(B),'Q':str(total),'r':str(r),'s':str(s)},
        'exact_base_ratio':str(2*B*r**3),
        'exact_block_ratio':str(r**61*s**40),
        'exact_remainder_guards':remainders,
        'native_moment_or_root_replay_performed':False,
        'historical_zero_count_used':False,
        'whole_unknown_complex_tail_retained':True,
        'all_mixed_pairs_covered':False, 'RH_proved':False,
        'infinite_analytic_proof_imported':True,
        'source_sha256':{str(p.relative_to(EXPLORATORY)):sha(p) for p in sources},
    }
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'], flush=True)


if __name__ == '__main__':
    main()
