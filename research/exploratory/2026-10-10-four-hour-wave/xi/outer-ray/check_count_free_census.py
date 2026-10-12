#!/usr/bin/env python3
"""Native moment guards recover a smaller census without a zero-count call.

Only the prior primitive Hardy-Z sign facts are imported. Their complete-count
and initial uniqueness claims are deliberately unused by this theorem.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import flint
from flint import acb, acb_series, arb, ctx, fmpq

HERE = Path(__file__).resolve().parent
WAVE = HERE.parents[1]


def need(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit('FAIL: ' + message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE / 'count_free_census.json')
    args = parser.parse_args()
    ctx.prec, ctx.cap = 224, 7
    need(flint.__version__ == '0.9.0' and flint.__FLINT_VERSION__ == '3.6.0', 'frozen directed backend')
    original = json.loads((HERE/'native_candidates.json').read_text())
    refined = json.loads((HERE/'refined_prefix_candidates.json').read_text())
    prior = json.loads((HERE/'native_slab_certificate.json').read_text())
    prefix = json.loads((HERE/'refined_prefix_moments.json').read_text())
    need(prior['status'] == 'PASS_DIRECTED_NATIVE_COMPANION_SLAB'
         and prior['actual_primitive_endpoints_replayed'] is True
         and prior['replayed_disjoint_sign_crossing_brackets'] == 8049,
         'imported original actual primitive sign facts')
    need(prefix['status'] == 'PASS_DIRECTED_REFINED_PREFIX_MOMENT_GUARDS'
         and prefix['refined_prefix_count'] == 111
         and prefix['refined_endpoint_signs_replayed'] == 222,
         'imported refined actual primitive sign facts')
    for receipt in [prior, prefix]:
        for path, expected in receipt['source_sha256'].items():
            need(digest(WAVE/path) == expected, 'imported primitive direct-source binding: '+path)
    need(original['normalization'] == refined['normalization'] == 'Xi(z)=xi(1/2+i*z)',
         'actual primitive normalization')
    old_den, new_den = 2**24, 2**80
    need(original['height'] == 8192 and original['denominator'] == old_den
         and refined['denominator'] == new_den and refined['prefix_cutoff'] == 256,
         'exact source parameters')
    old, new = original['interval_numerators'], refined['interval_numerators']
    need(len(old) == 8049 and len(new) == 111, 'selected sign interval count, not a zero count')
    selected = []
    previous = 0
    for index, bracket in enumerate(old):
        need(isinstance(bracket, list) and len(bracket) == 2, 'original bracket shape')
        lo, hi = bracket
        need(type(lo) is int and type(hi) is int and previous < lo < hi < 8192*old_den
             and hi == lo+1, 'ordered disjoint original sign intervals')
        previous = hi
        den = old_den
        if index < len(new):
            need(isinstance(new[index], list) and len(new[index]) == 2, 'refined bracket shape')
            nlo, nhi = new[index]
            need(type(nlo) is int and type(nhi) is int and nhi == nlo+1,
                 'exact refined interval geometry')
            need(fmpq(lo,old_den) < fmpq(nlo,new_den) < fmpq(nhi,new_den) < fmpq(hi,old_den),
                 'strict refined nesting; no imported uniqueness used')
            lo, hi, den = nlo, nhi, new_den
        selected.append((fmpq(lo,den),fmpq(hi,den)))

    half = arb(fmpq(1,2))
    z = acb_series([0,1],7)
    s = acb(half)+acb(0,1)*z
    xi = s*(s-1)/2*(-s*arb.pi().log()/2).exp()*(s/2).gamma()*s.zeta()
    need(xi[0].real > arb(fmpq(99,200)) and not xi[0].contains(0), 'strict actual native seed')
    for k in range(7):
        need(xi[k].contains(0) if k%2 else xi[k].imag.contains(0), 'exact source parity/reality enclosure')
    logarithm = (xi/xi[0]).log()
    need(logarithm[6].imag.contains(0), 'native logarithmic coefficient reality')
    finite = arb(0)
    for lo, hi in selected:
        gamma = arb((lo+hi)/2,(hi-lo)/2)
        finite += 1/gamma**6
    residual = -3*logarithm[6].real-finite
    need(residual > 0, 'strict residual moment enclosure')
    lower, upper = residual.lower().fmpq(), residual.upper().fmpq()

    seed = fmpq(99,200)
    pi_bound = fmpq(22,7)
    need(pi_bound**3/63 < seed, 'strict rational zero-free disk seed guard')
    need(arb.pi() < arb(pi_bound), 'directed pi bound, with elementary source proof')
    R, A = fmpq(5), fmpq(1,2)
    c = (R**6-15*R**4*A**2+15*R**2*A**4-A**6)/(R**2+A**2)**3
    need(c > 0, 'positive exact inverse-sixth projection')
    domains = []
    for height in [2048,2240]:
        need(all(hi < height or lo > height for lo,hi in selected), 'no selected interval meets boundary')
        ratio = upper*(height**2+A**2)**3/c
        need(ratio < 1, 'strict whole-source omitted-zero exclusion at height '+str(height))
        below = sum(hi < height for lo,hi in selected)
        domains.append({
            'height':height, 'recovered_complete_simple_positive_zero_count':below,
            'maximum_derivative_order':2*height-3,
            'strict_horizontal_range':'abs(T)<'+str(height)+'-(r+2)/2',
            'all_lambda_positive':True, 'all_y_nonnegative':True,
            'exclusion_ratio_upper':str(ratio), 'strict_exclusion_margin':str(1-ratio),
        })
    sources = [Path(__file__).resolve(), HERE/'COUNT_FREE_CENSUS_RECOVERY.md',
               HERE/'THEOREM.md', HERE/'CENSUS_FULL_COLUMN_SECTOR.md', HERE/'CENSUS_LOCALIZATION.md',
               HERE/'native_candidates.json', HERE/'native_slab_certificate.json',
               HERE/'refined_prefix_candidates.json', HERE/'refined_prefix_moments.json',
               HERE/'NATIVE_SLAB_CERTIFICATE.md', HERE/'REFINED_PREFIX_MOMENTS.md']
    package = Path(flint.__file__).resolve().parent
    binaries = [package/'types'/name for name in ['arb.abi3.so','acb.abi3.so','acb_series.abi3.so']]
    binaries.extend(sorted((package.parent/'python_flint.libs').glob('lib*.so*')))
    result = {
        'status':'PASS_DIRECTED_COUNT_FREE_CENSUS_GUARDS',
        'normalization':'Xi(z)=xi(1/2+i*z)',
        'arithmetic':'Arb/acb/acb_series directed ball arithmetic at224bits; exact rational final guards.',
        'native_logarithmic_jet_degree_replayed':6,
        'selected_interval_inverse_sixth_terms_replayed':8049,
        'strict_native_xi_zero_seed_lower':str(xi[0].real.lower().fmpq()),
        'global_zero_free_disk_radius':'11/2', 'complete_strip_half_width':'1/2',
        'complete_root_real_part_lower':'sqrt(30)>5',
        'residual_inverse_sixth_moment_interval':[str(lower),str(upper)],
        'exact_global_angular_projection':str(c),
        'original_8049_strict_sign_facts_imported':True,
        'refined_222_strict_endpoint_sign_facts_imported':True,
        'endpoint_signs_replayed_by_this_checker':False,
        'initial_root_uniqueness_or_completeness_assumed':False,
        'complete_zero_count_routine_called_by_this_checker':False,
        'historical_Gram_Rosser_contract_used_by_this_theorem':False,
        'published_large_zero_verification_used_by_this_theorem':False,
        'imported_sign_receipts_also_contain_unused_count_claims':True,
        'analytic_source_product_theta_or_column_theorem_authenticated_by_checker':False,
        'different_arithmetic_implementation_used':False,
        'recovered_domains':domains, 'rh_proved':False,
        'source_sha256':{str(p.relative_to(WAVE)):digest(p) for p in sources},
        'backend_binary_sha256':{p.name:digest(p) for p in binaries},
    }
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],'HEIGHTS',','.join(str(d['height']) for d in domains),flush=True)


if __name__ == '__main__':
    main()
