#!/usr/bin/env python3
"""Bounded native shifted/unshifted complete-moment hierarchy experiment."""
from __future__ import annotations
import argparse
import hashlib
import json
from math import comb
from pathlib import Path
import flint
from flint import acb, acb_series, arb, ctx, fmpq

HERE = Path(__file__).resolve().parent
EXPLORATORY = HERE.parent.parent
OLD = EXPLORATORY/'2026-10-10-four-hour-wave'
PRIOR = OLD/'xi'/'outer-ray'


def need(ok: bool, why: str) -> None:
    if not ok:
        raise SystemExit('FAIL: '+why)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE/'shifted_hierarchy_v2.json')
    args = parser.parse_args()
    need(flint.__version__ == '0.9.0' and flint.__FLINT_VERSION__ == '3.6.0', 'native backend versions')
    original_path = PRIOR/'native_candidates.json'
    candidate_path = HERE/'continuation_prefix_candidates.json'
    prior_path = PRIOR/'sixteenth_moment_census.json'
    prior = json.loads(prior_path.read_text())
    need(sha(prior_path) == '964f49cc79a61b354cd77fe1f077637e54bb46f39a5643e1455e87f60fabc4d6',
         'explicit reviewed lower count-free simple census identity')
    need(prior['status'] == 'PASS_DIRECTED_COUNT_FREE_SIXTEENTH_MOMENT_CENSUS'
         and any(x['height'] == 5419 and x['recovered_complete_simple_positive_zero_count'] == 4968
                 for x in prior['recovered_domains']), 'lower census scope')
    for path, expected in prior['source_sha256'].items():
        need(sha(OLD/path) == expected, 'old frozen source binding '+path)
    primitive_path = PRIOR/'native_slab_certificate.json'
    primitive = json.loads(primitive_path.read_text())
    need(primitive['status'] == 'PASS_DIRECTED_NATIVE_COMPANION_SLAB'
         and primitive['actual_primitive_endpoints_replayed'] is True
         and primitive['replayed_disjoint_sign_crossing_brackets'] == 8049,
         'old strict sign facts, without old complete count')
    for path, expected in primitive['source_sha256'].items():
        need(sha(OLD/path) == expected, 'old primitive direct source '+path)
    original = json.loads(original_path.read_text())
    candidate = json.loads(candidate_path.read_text())
    need(original['normalization'] == candidate['normalization'] == 'Xi(z)=xi(1/2+i*z)', 'actual normalization')
    need(candidate['status'] == 'CONTINUATION_MOMENT_PREFIX_CANDIDATES_NOT_A_CENSUS', 'candidate scope')
    need(candidate['original_candidates_sha256'] == sha(original_path)
         and candidate['producer_sha256'] == sha(HERE/'produce_continuation_prefix.py'), 'candidate source hashes')
    old_den, new_den = 2**24, 2**512
    old, new = original['interval_numerators'], candidate['interval_numerators']
    need(original['height'] == 8192 and original['denominator'] == old_den
         and candidate['denominator'] == new_den and candidate['prefix_cutoff'] == 6144,
         'exact inventory parameters')
    count = sum(b < 6144*old_den for a,b in old)
    need(len(old) == 8049 and count == len(new) == candidate['refined_count'] == 5756, 'selected interval cardinality')
    ctx.prec, ctx.cap = 640, 49
    half, pl = arb(fmpq(1,2)), arb.pi().log()

    def hardy(q: fmpq) -> arb:
        v = arb(q)
        theta = acb(arb(fmpq(1,4)),v/2).lgamma().imag-v*pl/2
        value = acb(0,theta).exp()*acb(half,v).zeta()
        need(value.imag.contains(0), 'exact Hardy reality enclosure')
        return value.real

    selected, roots = [], []
    previous = 0
    for index, bracket in enumerate(old):
        need(isinstance(bracket,list) and len(bracket) == 2, 'original interval shape')
        a,b = bracket
        need(type(a) is int and type(b) is int and previous < a < b < 8192*old_den
             and b == a+1, 'ordered disjoint original intervals')
        previous = b
        den = old_den
        if index < count:
            need(isinstance(new[index],list) and len(new[index]) == 2, 'new interval shape')
            na,nb = new[index]
            need(type(na) is int and type(nb) is int and nb == na+1, 'exact new interval endpoints')
            need(fmpq(a,old_den) < fmpq(na,new_den) < fmpq(nb,new_den) < fmpq(b,old_den), 'strict source nesting')
            av,bv = hardy(fmpq(na,new_den)),hardy(fmpq(nb,new_den))
            need((av>0 and bv<0) or (av<0 and bv>0), 'actual new strict opposite Hardy signs')
            a,b,den = na,nb,new_den
            if (index+1)%512 == 0:
                print('STRICT_SIGNS',2*(index+1),flush=True)
        ql,qh = fmpq(a,den),fmpq(b,den)
        selected.append((ql,qh))
        roots.append(arb((ql+qh)/2,(qh-ql)/2))
    need(all(b<5419 or a>5419 for a,b in selected)
         and sum(b<5419 for a,b in selected) == 4968, 'selection removes every imported unique lower occurrence')
    print('ALL_NEW_SIGNS',2*count,flush=True)

    ctx.prec,ctx.cap = 896,49
    half,pl = arb(fmpq(1,2)),arb.pi().log()
    z = acb_series([0,1],49)
    s = acb(half)+acb(0,1)*z
    xi = s*(s-1)/2*(-s*pl/2).exp()*(s/2).gamma()*s.zeta()
    need(xi[0].real>arb(fmpq(99,200)) and not xi[0].contains(0), 'native critical-center seed')
    for j in range(49):
        need(xi[j].contains(0) if j%2 else xi[j].imag.contains(0), 'critical-center parity and reality')
    log_zero = (xi/xi[0]).log()
    print('COMPLETE_UNSHIFTED_JET_DEGREE48',flush=True)
    ctx.cap = 33
    w = acb_series([0,1],33)
    shifted_s = acb(half)+(acb_series([512**2],33)-w).sqrt()
    shifted_log = (shifted_s*(shifted_s-1)/2).log()-shifted_s*pl/2+(shifted_s/2).lgamma()+shifted_s.zeta().log()
    need(shifted_s[0].real>1 and shifted_log[0].imag.contains(0), 'positive-real shifted source branches')
    for j in range(33):
        need(shifted_log[j].imag.contains(0), 'shifted native coefficient reality')
    print('COMPLETE_SHIFTED_LOGJET_DEGREE32',flush=True)
    complete_shifted = [-k*shifted_log[k].real for k in range(1,33)]
    hausdorff_sequence = [value*fmpq(512**2*4-1,4)**n for n,value in enumerate(complete_shifted)]
    mixed = []
    for n in range(32):
        for degree in range(32-n):
            value = sum(((-1)**j*comb(degree,j)*hausdorff_sequence[n+j]
                         for j in range(degree+1)),arb(0))
            need(value.is_finite(), 'finite native mixed moment enclosure')
            mixed.append({'n':n,'difference_degree':degree,
                          'interval':[str(value.lower().fmpq()),str(value.upper().fmpq())],
                          'classification':'strict_positive' if value>0 else 'strict_negative' if value<0 else 'undetermined'})
    A,R = fmpq(1,2),fmpq(5419)
    results = []
    for kind,orders in [('unshifted',range(8,25)),('shifted',[8,16,24,32])]:
        for k in orders:
            t = 0 if kind == 'unshifted' else 512
            coefficient = -k*(log_zero[2*k].real if not t else shifted_log[k].real)
            finite = sum(((gamma**2+t**2)**(-k) for gamma in roots),arb(0))
            residual = coefficient-finite
            need(residual.is_finite(), 'finite full residual moment')
            lower,upper = residual.lower().fmpq(),residual.upper().fmpq()
            need(upper>0, 'positive upper endpoint consistent with complete source')
            if not t:
                need((2*k+1)*A/R<1 and arb.pi()>3, 'complete residual corner angle')
                def ratio(H: int) -> fmpq:
                    h = fmpq(H)
                    d = sum((-1)**j*comb(2*k,2*j)*h**(2*k-2*j)*A**(2*j) for j in range(k+1))/(h**2+A**2)**(2*k)
                    need(d>0,'positive exact unshifted corner')
                    return upper/d
                projection = 'complete residual joint corner after explicit prior census5419'
            else:
                q = fmpq(k,1000)
                c = 1-q*q/2
                need(0<q<1 and k*k*A*A <= q*q*(t*t-A*A) and c>0, 'global shifted positive kernel guard')
                def ratio(H: int) -> fmpq:
                    return upper*(H**2+A**2+t**2)**k/c
                projection = 'global shifted source positivity, q=k/1000 and c=1-q^2/2'
            admitted = None
            if ratio(5419)<1:
                lo,hi = 5419,8193
                while lo+1<hi:
                    mid=(lo+hi)//2
                    if ratio(mid)<1: lo=mid
                    else: hi=mid
                admitted=lo
                need(ratio(lo)<1 and (lo==8192 or ratio(lo+1)>=1), 'largest admitted inventory-range integer')
                need(all(b<lo or a>lo for a,b in selected), 'selected boundary disjointness')
            record = {'kind':kind,'order':k,'shift':t,'native_residual_interval':[str(lower),str(upper)],
                      'native_residual_interval_width':str(upper-lower),'projection':projection,
                      'largest_admitted_integer_height_in_inventory_range':admitted}
            if admitted is not None:
                record.update({'complete_simple_positive_zero_count':sum(b<admitted for a,b in selected),
                               'maximum_column_derivative_order':2*admitted-3,
                               'accepted_ratio_exact':str(ratio(admitted)),
                               'next_integer_ratio_exact':str(ratio(admitted+1)),
                               'next_integer_failure_only_this_predicate':admitted<8192,
                               'all_lambda_positive':True,'all_y_nonnegative':True,
                               'strict_horizontal_range':'abs(T)<'+str(admitted)+'-(r+2)/2'})
            results.append(record)
            print('MOMENT',kind,k,'HEIGHT',admitted,flush=True)
    sources = [Path(__file__).resolve(),HERE/'produce_continuation_prefix.py',candidate_path,
               HERE/'SHIFTED_COMPLETE_MOMENTS_V2.md',original_path,prior_path,primitive_path,
               PRIOR/'SIXTEENTH_MOMENT_CENSUS_RECOVERY.md',PRIOR/'CENSUS_FULL_COLUMN_SECTOR.md',
               PRIOR/'CENSUS_LOCALIZATION.md',PRIOR/'THEOREM.md']
    package = Path(flint.__file__).resolve().parent
    bins = [package/'types'/name for name in ['arb.abi3.so','acb.abi3.so','acb_series.abi3.so']]
    bins.extend(sorted((package.parent/'python_flint.libs').glob('lib*.so*')))
    result = {
        'status':'PASS_DIRECTED_PRIMITIVES_AND_COUNT_FREE_SHIFTED_HIERARCHY_GUARDS',
        'normalization':'Xi(z)=xi(1/2+i*z)','source_precision_bits':{'candidate_and_signs':640,'complete_jets':896},
        'refined_prefix_cutoff':6144,'refined_prefix_count':count,'new_actual_endpoint_signs_replayed':2*count,
        'refined_bracket_width':str(fmpq(1,new_den)),'remaining_old_strict_sign_intervals_imported':8049-count,
        'all_selected_full_interval_terms_retained':8049,'critical_center_native_jet_degree':48,
        'shifted_native_logjet_degree':32,'explicit_prior_count_free_complete_simple_census':5419,
        'prior_census_is_needed_only_for_unshifted_projection':True,
        'shifted_global_projection_needs_prior_census':False,
        'complete_zero_count_routine_called':False,'historical_zero_count_used':False,
        'source_infinite_theta_strip_product_or_column_theorem_authenticated_by_checker':False,
        'same_directed_native_backend':True,'cofinal_or_global_real_zero_statement':False,'rh_proved':False,
        'complete_shifted_moment_intervals':[
            [str(v.lower().fmpq()),str(v.upper().fmpq())] for v in complete_shifted],
        'finite_hausdorff_mixed_moments':mixed,
        'finite_mixed_moment_scope':'n+degree<=31 only; complete source coefficients, no selected-root subtraction; no infinite sign conclusion.',
        'finite_mixed_moment_identity':'b_n=M_(n+1)(512)*(512^2-1/4)^n; sum_j(-1)^j binomial(degree,j)b_(n+j)',
        'hausdorff_equivalence_theorem_authenticated_by_this_checker':False,
        'moments':results,'source_sha256':{str(p.relative_to(EXPLORATORY)):sha(p) for p in sources},
        'backend_binary_sha256':{p.name:sha(p) for p in bins},
    }
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],flush=True)


if __name__ == '__main__':
    main()
