#!/usr/bin/env python3
"""Replay refined source signs and a count-free complete eighth-moment guard."""
from __future__ import annotations
import argparse
import hashlib
import json
from math import comb
from pathlib import Path
import flint
from flint import acb, acb_series, arb, ctx, fmpq

HERE = Path(__file__).resolve().parent
WAVE = HERE.parents[1]


def need(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit('FAIL: '+message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE/'eighth_moment_census.json')
    args = parser.parse_args()
    ctx.prec, ctx.cap = 224, 9
    need(flint.__version__ == '0.9.0' and flint.__FLINT_VERSION__ == '3.6.0', 'frozen directed backend')
    original_path = HERE/'native_candidates.json'
    candidate_path = HERE/'eighth_prefix_candidates.json'
    original = json.loads(original_path.read_text())
    candidate = json.loads(candidate_path.read_text())
    prior = json.loads((HERE/'native_slab_certificate.json').read_text())
    need(prior['status'] == 'PASS_DIRECTED_NATIVE_COMPANION_SLAB'
         and prior['actual_primitive_endpoints_replayed'] is True
         and prior['replayed_disjoint_sign_crossing_brackets'] == 8049,
         'imported original primitive sign facts only')
    for path, expected in prior['source_sha256'].items():
        need(digest(WAVE/path) == expected, 'prior primitive direct-source hash: '+path)
    need(candidate['status'] == 'EIGHTH_MOMENT_PREFIX_CANDIDATES_NOT_A_CENSUS', 'candidate status qualified')
    need(candidate['original_candidates_sha256'] == digest(original_path), 'original candidate source binding')
    need(candidate['producer_sha256'] == digest(HERE/'produce_eighth_prefix.py'), 'producer binding')
    need(original['normalization'] == candidate['normalization'] == 'Xi(z)=xi(1/2+i*z)', 'actual normalization')
    old_den, new_den = 2**24, 2**80
    need(original['height'] == 8192 and original['denominator'] == old_den
         and candidate['denominator'] == new_den and candidate['prefix_cutoff'] == 512,
         'exact source parameters')
    old, new = original['interval_numerators'], candidate['interval_numerators']
    count = sum(hi < 512*old_den for lo,hi in old)
    need(len(old) == 8049 and count == len(new) == candidate['refined_count'] == 278,
         'selected sign-interval geometry, not a complete zero count')
    half, pl = arb(fmpq(1,2)), arb.pi().log()

    def hardy(t: arb) -> arb:
        theta = acb(arb(fmpq(1,4)),t/2).lgamma().imag-t*pl/2
        value = acb(0,theta).exp()*acb(half,t).zeta()
        need(value.imag.contains(0), 'exact Hardy source reality enclosure')
        return value.real

    selected, gamma_balls = [], []
    previous = 0
    for index, bracket in enumerate(old):
        need(isinstance(bracket,list) and len(bracket) == 2, 'original bracket shape')
        lo, hi = bracket
        need(type(lo) is int and type(hi) is int and previous < lo < hi < 8192*old_den
             and hi == lo+1, 'ordered disjoint original sign intervals')
        previous = hi
        den = old_den
        if index < count:
            need(isinstance(new[index],list) and len(new[index]) == 2, 'refined bracket shape')
            nlo, nhi = new[index]
            need(type(nlo) is int and type(nhi) is int and nhi == nlo+1, 'exact refined geometry')
            need(fmpq(lo,old_den) < fmpq(nlo,new_den) < fmpq(nhi,new_den) < fmpq(hi,old_den),
                 'strict nesting without assumed root uniqueness')
            lv, hv = hardy(arb(fmpq(nlo,new_den))), hardy(arb(fmpq(nhi,new_den)))
            need((lv > 0 and hv < 0) or (lv < 0 and hv > 0), 'refined actual strict opposite signs')
            lo, hi, den = nlo, nhi, new_den
        qlo, qhi = fmpq(lo,den), fmpq(hi,den)
        selected.append((qlo,qhi))
        gamma_balls.append(arb((qlo+qhi)/2,(qhi-qlo)/2))

    z = acb_series([0,1],9)
    s = acb(half)+acb(0,1)*z
    xi = s*(s-1)/2*(-s*pl/2).exp()*(s/2).gamma()*s.zeta()
    need(xi[0].real > arb(fmpq(99,200)) and not xi[0].contains(0), 'strict actual native Xi seed')
    for index in range(9):
        need(xi[index].contains(0) if index%2 else xi[index].imag.contains(0), 'exact source parity/reality enclosure')
    logarithm = (xi/xi[0]).log()
    need(logarithm[8].imag.contains(0), 'native logarithmic coefficient reality')
    finite = sum((1/gamma**8 for gamma in gamma_balls),arb(0))
    residual = -4*logarithm[8].real-finite
    need(residual > 0, 'strict native full remaining moment enclosure')
    lower, upper = residual.lower().fmpq(), residual.upper().fmpq()
    need(fmpq(22,7)**3/63 < fmpq(99,200) and arb.pi() < arb(fmpq(22,7)),
         'strict source zero-free disk seed comparison')
    R, A, B = fmpq(27,5), fmpq(1,2), fmpq(11,2)
    need(R**2+A**2 < B**2 and 8*A/R < fmpq(3,2) and arb.pi() > 3,
         'strict exact source disk and acute angular guards')
    c = sum((-1)**j*comb(8,2*j)*R**(8-2*j)*A**(2*j) for j in range(5))/(R**2+A**2)**4
    need(c > 0, 'positive exact inverse-eighth projection')
    domains = []
    for height, expected_count in [(3072,2539),(3168,2634)]:
        need(all(hi < height or lo > height for lo,hi in selected), 'no selected interval meets height boundary')
        ratio = upper*(height**2+A**2)**4/c
        need(ratio < 1, 'strict full remaining-source exclusion at height '+str(height))
        below = sum(hi < height for lo,hi in selected)
        need(below == expected_count, 'derived selected real-root list size')
        domains.append({
            'height':height, 'recovered_complete_simple_positive_zero_count':below,
            'maximum_derivative_order':2*height-3,
            'strict_horizontal_range':'abs(T)<'+str(height)+'-(r+2)/2',
            'all_lambda_positive':True, 'all_y_nonnegative':True,
            'exclusion_ratio_upper':str(ratio), 'strict_exclusion_margin':str(1-ratio),
        })
    sources = [Path(__file__).resolve(), HERE/'produce_eighth_prefix.py', candidate_path,
               HERE/'EIGHTH_MOMENT_CENSUS_RECOVERY.md', HERE/'HIGHER_MOMENT_CENSUS_RECOVERY.md',
               HERE/'COUNT_FREE_CENSUS_RECOVERY.md', HERE/'THEOREM.md',
               HERE/'CENSUS_FULL_COLUMN_SECTOR.md', HERE/'CENSUS_LOCALIZATION.md',
               original_path, HERE/'native_slab_certificate.json', HERE/'NATIVE_SLAB_CERTIFICATE.md']
    package = Path(flint.__file__).resolve().parent
    binaries = [package/'types'/name for name in ['arb.abi3.so','acb.abi3.so','acb_series.abi3.so']]
    binaries.extend(sorted((package.parent/'python_flint.libs').glob('lib*.so*')))
    result = {
        'status':'PASS_DIRECTED_COUNT_FREE_EIGHTH_MOMENT_CENSUS',
        'normalization':'Xi(z)=xi(1/2+i*z)',
        'arithmetic':'Arb/acb/acb_series directed ball arithmetic at224bits; exact dyadic endpoints and rational exclusion guards.',
        'refined_prefix_cutoff':512, 'refined_prefix_count':count,
        'refined_endpoint_signs_replayed':2*count, 'refined_bracket_width':'1/1208925819614629174706176',
        'remaining_original_sign_intervals_imported':len(old)-count,
        'remaining_original_endpoint_signs_replayed_by_this_checker':False,
        'native_logarithmic_jet_degree_replayed':8,
        'selected_interval_inverse_eighth_terms_replayed':len(old),
        'strict_native_xi_zero_seed_lower':str(xi[0].real.lower().fmpq()),
        'global_zero_free_disk_radius':'11/2', 'complete_strip_half_width':'1/2',
        'complete_root_real_part_lower':'sqrt(30)>27/5',
        'residual_inverse_eighth_moment_interval':[str(lower),str(upper)],
        'residual_inverse_eighth_moment_width':str(upper-lower),
        'exact_global_angular_projection':str(c),
        'initial_root_uniqueness_or_completeness_assumed':False,
        'complete_zero_count_routine_called_by_this_checker':False,
        'historical_Gram_Rosser_contract_used_by_this_theorem':False,
        'published_large_zero_verification_used_by_this_theorem':False,
        'imported_original_sign_receipt_also_contains_unused_count_claims':True,
        'analytic_source_product_theta_or_column_theorem_authenticated_by_checker':False,
        'different_arithmetic_implementation_used':False,
        'recovered_domains':domains, 'rh_proved':False,
        'source_sha256':{str(p.relative_to(WAVE)):digest(p) for p in sources},
        'backend_binary_sha256':{p.name:digest(p) for p in binaries},
    }
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],'PREFIX',count,'HEIGHTS',','.join(str(d['height']) for d in domains),flush=True)


if __name__ == '__main__':
    main()
