#!/usr/bin/env python3
"""Exact composition of an accepted native census with a complete mixed tail."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTINUATION = HERE.parents[1]
EXPLORATORY = CONTINUATION.parent

def need(ok: bool, message: str) -> None:
    if not ok:
        raise SystemExit('FAIL: ' + message)

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE/'composed_mixed_cone_normal.json')
    args = parser.parse_args()
    prior_path = HERE/'infinite_mixed_cone_normal.json'
    need(sha(prior_path) == 'bffb559967304c3ccb46c6a185d03bed376be5a46dd84394852c68bea39b427f',
         'accepted complete mixed-tail guard adapter')
    prior = json.loads(prior_path.read_text())
    need(prior['status'] == 'PASS_EXACT_COMPLETE_INFINITE_MIXED_MOMENT_CONE_GUARDS'
         and prior['whole_unknown_complex_tail_retained'] is True
         and prior['historical_zero_count_used'] is False, 'complete prior source contract')
    for rel, expected in prior['source_sha256'].items():
        need(sha(EXPLORATORY/rel) == expected, 'frozen prior source ' + rel)
    native_path = CONTINUATION/'xi/shifted_hierarchy_v2.json'
    need(sha(native_path) == 'd6cf40e46dbe0292aff5a48dc5ebec357f378ffed4b2e3aefbfe4d848d517ba3',
         'accepted final full native V2 census')
    native = json.loads(native_path.read_text())
    need(native['status'] == 'PASS_DIRECTED_PRIMITIVES_AND_COUNT_FREE_SHIFTED_HIERARCHY_GUARDS'
         and native['normalization'] == 'Xi(z)=xi(1/2+i*z)'
         and native['historical_zero_count_used'] is False
         and native['complete_zero_count_routine_called'] is False, 'actual native source contract')
    for rel, expected in native['source_sha256'].items():
        need(sha(EXPLORATORY/rel) == expected, 'frozen final census source ' + rel)
    matches = [v for v in native['moments'] if v['kind']=='shifted' and v['order']==32 and v['shift']==512]
    need(len(matches)==1, 'unique complete shifted guard record')
    guard = matches[0]
    need(guard['largest_admitted_integer_height_in_inventory_range']==7570
         and guard['complete_simple_positive_zero_count']==7343
         and Q(guard['accepted_ratio_exact'])<1, 'stronger complete real head')
    lo, hi = map(Q, prior['known_actual_real_root_interval'])
    need(Q(14)<lo<hi<Q(15), 'authenticated positive real occurrence')
    R,A,t=Q(7570),Q(1,2),Q(512)
    c,a,B=t*t-A*A,Q(14)**2+A*A,Q(15)**2+t*t
    endpoint=R*R+c
    need(R>=1024 and t*t>=3*A*A, 'complete tail count and strip domains')
    need(endpoint==Q(230268175,4) and a==Q(785,4) and B==262369,
         'new exact endpoint and head constants')
    r,s=B/endpoint,B/a
    need(0<r<1 and s>1 and 2*B*r**3<1 and r**27*s**20<1, 'infinite cone base and block')
    remainders=[]
    for h in range(20):
        power=(27*h+19)//20
        value=r**power*s**h
        need(value<=1, 'exact residue '+str(h))
        need(value**20<= (r**27*s**20)**h, 'independent raised-power remainder proof')
        remainders.append({'j_remainder':h,'minimum_n_increment':power,'exact_ratio':str(value)})
    sources=[Path(__file__).resolve(),HERE/'COMPOSED_CENSUS_MIXED_CONE.md',
             prior_path,native_path,HERE/'SHIFTED_V2_DIRECT_NATIVE_REVIEW.md',
             HERE/'INFINITE_MIXED_CONE_REVIEW.md',
             EXPLORATORY/'2026-10-10-four-hour-wave/heights/COARSE_ZERO_COUNT.md']
    result={'status':'PASS_EXACT_COMPOSED_COMPLETE_MIXED_CONE_GUARDS',
            'normalization':prior['normalization'],'physical_shift':'512','strip_half_width':'1/2',
            'complete_real_head':7570,'imported_native_positive_zero_count':7343,
            'coverage':'EVERY integers n,j>=0 with20*n>=27*j+60; complete actual source',
            'exact_constants':{'a':str(a),'B':str(B),'Q':str(endpoint),'r':str(r),'s':str(s)},
            'exact_base_ratio':str(2*B*r**3),'exact_block_ratio':str(r**27*s**20),
            'exact_remainder_guards':remainders,'native_primitive_replayed_by_this_composer':False,
            'historical_zero_count_used':False,'whole_unknown_complex_tail_retained':True,
            'infinite_analytic_proof_imported':True,'all_mixed_pairs_covered':False,'RH_proved':False,
            'source_sha256':{str(p.relative_to(EXPLORATORY)):sha(p) for p in sources}}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],flush=True)

if __name__=='__main__':
    main()
