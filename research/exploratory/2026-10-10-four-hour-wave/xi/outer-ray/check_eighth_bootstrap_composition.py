#!/usr/bin/env python3
"""Exact imported-primitive composition; no native arithmetic is replayed."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
WAVE = HERE.parents[1]
BOOT = WAVE/'heights'/'final-review'


def need(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit('FAIL: '+message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE/'eighth_bootstrap_composition.json')
    args = parser.parse_args()
    ep = HERE/'eighth_moment_census.json'
    bp = BOOT/'complete_moment_bootstrap_normal.json'
    need(digest(ep) == 'e224616d2497c0477146ccd0c712e3888c55a279e55c5fa27115310b7710a47f',
         'exact imported eighth-moment native receipt')
    need(digest(bp) == 'b1074698a2529e98637ad8dc4554f4d89f55e063dbe44c1841e93ba5e620cec3',
         'exact imported complete-moment bootstrap receipt')
    e, b = json.loads(ep.read_text()), json.loads(bp.read_text())
    need(e['status'] == 'PASS_DIRECTED_COUNT_FREE_EIGHTH_MOMENT_CENSUS', 'imported source moment fact')
    need(b['status'] == 'PASS_DIRECTED_COMPLETE_MOMENT_ZERO_FREE_BOOTSTRAP'
         and b['final_all_source_root_real_part_exclusion'] == 'abs(Re rho)>14',
         'imported global source exclusion fact')
    need(e['normalization'] == b['normalization'] == 'Xi(z)=xi(1/2+i*z)', 'same exact actual source')
    need(e['historical_Gram_Rosser_contract_used_by_this_theorem'] is False
         and b['historical_Gram_Rosser_or_published_verification_used'] is False,
         'historical count and published census unused')
    for receipt in [e,b]:
        for path, expected in receipt['source_sha256'].items():
            need(digest(WAVE/path) == expected, 'imported direct-source identity: '+path)
    need(e['backend_binary_sha256'] == b['backend_binary_sha256'], 'same displayed native backend imports')
    lower, upper = map(Q,e['residual_inverse_eighth_moment_interval'])
    need(0 < lower < upper, 'imported directed complete moment interval')
    R, A = Q(14), Q(1,2)
    c = sum((-1)**j*comb(8,2*j)*R**(8-2*j)*A**(2*j) for j in range(5))/(R**2+A**2)**4
    need(c > 0 and 8*A/R < Q(3,2), 'exact positive acute projection')
    need(Q(b['higher_positive_projections_exact']['4']) == c, 'bootstrap projection identity')
    old = json.loads((HERE/'native_candidates.json').read_text())
    new = json.loads((HERE/'eighth_prefix_candidates.json').read_text())
    selected = []
    for index,(lo,hi) in enumerate(old['interval_numerators']):
        den = old['denominator']
        if index < new['refined_count']:
            lo, hi = new['interval_numerators'][index]
            den = new['denominator']
        selected.append((Q(lo,den),Q(hi,den)))
    need(len(selected) == 8049, 'same imported selected source list')
    domains = []
    for height, count in [(3264,2730),(3272,2737)]:
        need(all(hi < height or lo > height for lo,hi in selected), 'no selected interval meets boundary')
        need(sum(hi < height for lo,hi in selected) == count, 'derived selected list size')
        ratio = upper*(height**2+A**2)**4/c
        need(ratio < 1, 'strict remaining-source unit exclusion at height '+str(height))
        domains.append({'height':height,'recovered_complete_simple_positive_zero_count':count,
                        'maximum_derivative_order':2*height-3,
                        'strict_horizontal_range':'abs(T)<'+str(height)+'-(r+2)/2',
                        'all_lambda_positive':True,'all_y_nonnegative':True,
                        'exclusion_ratio_upper':str(ratio),'strict_exclusion_margin':str(1-ratio)})
    sources = [Path(__file__).resolve(),HERE/'EIGHTH_MOMENT_BOOTSTRAP_COMPOSITION.md',ep,bp,
               HERE/'eighth_prefix_candidates.json',HERE/'native_candidates.json',
               HERE/'EIGHTH_MOMENT_CENSUS_RECOVERY.md',HERE/'CENSUS_FULL_COLUMN_SECTOR.md',
               BOOT/'COMPLETE_MOMENT_ZERO_FREE_BOOTSTRAP.md']
    result = {'status':'PASS_EXACT_IMPORTED_EIGHTH_BOOTSTRAP_COMPOSITION',
              'normalization':'Xi(z)=xi(1/2+i*z)',
              'arithmetic':'Python Fraction exact rational arithmetic; primitive facts explicitly imported.',
              'imported_residual_inverse_eighth_upper':str(upper),
              'strengthened_global_inverse_eighth_projection':str(c),
              'native_jet_or_Hardy_endpoint_replayed_by_this_checker':False,
              'global_zero_free_bootstrap_native_receipt_explicitly_imported':True,
              'eighth_moment_native_receipt_explicitly_imported':True,
              'historical_count_or_published_large_verification_used':False,
              'analytic_source_or_column_theorem_authenticated_by_checker':False,
              'recovered_domains':domains,'rh_proved':False,
              'source_sha256':{str(p.relative_to(WAVE)):digest(p) for p in sources},
              'imported_native_backend_binary_sha256':e['backend_binary_sha256']}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],'HEIGHTS3264,3272',flush=True)


if __name__ == '__main__':
    main()
