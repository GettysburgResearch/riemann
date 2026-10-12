#!/usr/bin/env python3
"""Replay a refined low prefix and native complete tail-moment guards.

The original full simple census is an explicitly imported prior native packet.
This checker replays only the refined prefix, its native degree-six jet and
whole-parameter guards; it certifies no companion slab or RH assertion.
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
    parser.add_argument('--output', type=Path, default=HERE / 'refined_prefix_moments.json')
    args = parser.parse_args()
    ctx.prec, ctx.cap = 224, 7
    need(flint.__version__ == '0.9.0' and flint.__FLINT_VERSION__ == '3.6.0', 'frozen directed backend')
    original_path = HERE / 'native_candidates.json'
    original = json.loads(original_path.read_text())
    inherited = json.loads((HERE / 'native_slab_certificate.json').read_text())
    refined = json.loads((HERE / 'refined_prefix_candidates.json').read_text())
    need(original['status'] == 'CANDIDATES_ONLY_NOT_A_ZERO_CENSUS', 'original candidates qualified')
    need(inherited['status'] == 'PASS_DIRECTED_NATIVE_COMPANION_SLAB', 'prior native receipt imported')
    need(inherited['historical_Gram_Rosser_verification_replayed'] is False, 'historical count remains imported')
    for path, expected in inherited['source_sha256'].items():
        need(digest(WAVE / path) == expected, 'inherited direct-source hash: ' + path)
    need(refined['status'] == 'REFINED_PREFIX_CANDIDATES_ONLY_NOT_A_CENSUS', 'refined candidates qualified')
    need(refined['original_candidates_sha256'] == digest(original_path), 'original candidate binding')
    need(refined['producer_sha256'] == digest(HERE / 'produce_refined_prefix.py'), 'refinement producer binding')
    need(original['normalization'] == refined['normalization'] == 'Xi(z)=xi(1/2+i*z)', 'actual normalization')
    height, cutoff, old_den, new_den = 8192, 256, 2**24, 2**80
    need(original['height'] == height and original['denominator'] == old_den,
         'original exact dyadic source parameters')
    need(refined['prefix_cutoff'] == cutoff and refined['denominator'] == new_den,
         'refined exact dyadic source parameters')
    old = original['interval_numerators']
    new = refined['interval_numerators']
    need(len(old) == original['candidate_count'] == inherited['imported_complete_count'] == 8049,
         'inherited complete count and original root geometry')
    count = arb(height).zeta_nzeros()
    need(count.is_exact() and count.unique_fmpz() is not None and int(count.unique_fmpz()) == 8049,
         'native complete-count contract replay, including imported historical finite rules')
    prefix_count = sum(hi < cutoff * old_den for lo, hi in old)
    need(prefix_count == len(new) == refined['refined_count'] == 111, 'complete retained low prefix')
    half, pi_log = arb(fmpq(1, 2)), arb.pi().log()

    def hardy(t: arb) -> arb:
        theta = acb(arb(fmpq(1, 4)), t/2).lgamma().imag - t*pi_log/2
        value = acb(0, theta).exp() * acb(half, t).zeta()
        need(value.imag.contains(0), 'actual Hardy-Z reality')
        return value.real

    gamma_squared = []
    previous = 0
    for index, bracket in enumerate(old):
        need(isinstance(bracket, list) and len(bracket) == 2, 'original bracket shape')
        lo, hi = bracket
        need(type(lo) is int and type(hi) is int and previous < lo < hi < height*old_den and hi == lo+1,
             'original ordered positive geometry')
        previous = hi
        den = old_den
        if index < prefix_count:
            new_lo, new_hi = new[index]
            need(type(new_lo) is int and type(new_hi) is int and new_hi == new_lo+1,
                 'exact refined endpoint integers')
            need(fmpq(lo, old_den) < fmpq(new_lo, new_den) < fmpq(new_hi, new_den) < fmpq(hi, old_den),
                 'strict nesting inside inherited unique-root interval')
            lv, hv = hardy(arb(fmpq(new_lo, new_den))), hardy(arb(fmpq(new_hi, new_den)))
            need((lv > 0 and hv < 0) or (lv < 0 and hv > 0), 'refined actual strict sign crossing')
            lo, hi, den = new_lo, new_hi, new_den
        gamma = arb(fmpq(lo+hi, 2*den), fmpq(hi-lo, 2*den))
        gamma_squared.append(gamma*gamma)

    z = acb_series([0, 1], 7)
    s = acb(half) + acb(0, 1)*z
    xi = s*(s-1)/2*(-s*pi_log/2).exp()*(s/2).gamma()*s.zeta()
    need(xi[0].real > arb(fmpq(1, 4)) and not xi[0].contains(0), 'native Xi constant seed and division')
    for index in range(7):
        need(xi[index].contains(0) if index % 2 else xi[index].imag.contains(0),
             'native Taylor parity/reality')
    logarithm = (xi/xi[0]).log()
    moment_balls, moment_intervals = [], []
    for k in [1, 2, 3]:
        need(logarithm[2*k].imag.contains(0), 'native logarithmic coefficient reality')
        finite = sum((1/gamma2**k for gamma2 in gamma_squared), arb(0))
        tail = -k*logarithm[2*k].real - finite
        need(tail > 0, 'strict complete native tail moment positivity')
        lo, hi = tail.lower().fmpq(), tail.upper().fmpq()
        moment_balls.append(tail)
        moment_intervals.append([lo, hi])
    a1, t2, t3 = moment_intervals
    K, R, A = 6905, fmpq(8192), fmpq(1, 2)
    need(K*t3[1]**2 < t2[0]**3 and t2[1]**3 < 2*K*t3[0]**2,
         'whole native rectangle lies strictly inside two-pair moment cone')
    need(a1[0]**2 > 2*K*t2[1], 'whole native family has positive Gaussian parameter')
    need(t2[1] / K < 1/R**4, 'every artificial root lies beyond complete census')
    phase_constants = [
        (R**2-A**2)/(R**2+A**2),
        (R**4-6*R**2*A**2+A**4)/(R**2+A**2)**2,
        (R**6-15*R**4*A**2+15*R**2*A**4-A**6)/(R**2+A**2)**3,
    ]
    need(all(c > 0 for c in phase_constants), 'positive exact tail phase projections')
    sources = [Path(__file__).resolve(), HERE / 'produce_refined_prefix.py',
               HERE / 'refined_prefix_candidates.json', original_path,
               HERE / 'native_slab_certificate.json', HERE / 'NATIVE_SLAB_CERTIFICATE.md',
               HERE / 'THEOREM.md', HERE / 'MOMENT_NORM_TRANSPORT.md', HERE / 'SEXTIC_ABSORPTION.md',
               HERE / 'REFINED_PREFIX_MOMENTS.md']
    package = Path(flint.__file__).resolve().parent
    binaries = [package/'types'/name for name in ['arb.abi3.so', 'acb.abi3.so', 'acb_series.abi3.so']]
    binaries.extend(sorted((package.parent/'python_flint.libs').glob('lib*.so*')))
    result = {
        'status': 'PASS_DIRECTED_REFINED_PREFIX_MOMENT_GUARDS',
        'normalization': 'Xi(z)=xi(1/2+i*z)', 'native_series_degree': 6,
        'arithmetic': 'Arb/acb/acb_series directed ball arithmetic at224bits; exact dyadic endpoints and rational final guards.',
        'refined_prefix_count': prefix_count, 'refined_endpoint_signs_replayed': 2*prefix_count,
        'refined_bracket_width': '1/1208925819614629174706176', 'strict_nesting_in_prior_simple_census_verified': True,
        'remaining_original_endpoint_signs_replayed_by_this_checker': False,
        'original_full_native_census_explicitly_imported_from_named_prior_packet': True,
        'complete_count_contract_replayed': 8049, 'complete_census_height': 8192,
        'native_complete_count_dependencies': 'FLINT3.6.0 complete count with historical finite Gram/Rosser rules at this index; prior8049 native primitive sign replay imported.',
        'historical_Gram_Rosser_verification_replayed': False,
        'actual_tail_moment_intervals': {str(k): [str(lo), str(hi)] for k, (lo, hi) in enumerate(moment_intervals, 1)},
        'actual_tail_moment_widths': {str(k): str(hi-lo) for k, (lo, hi) in enumerate(moment_intervals, 1)},
        'two_artificial_pairs_multiplicity_each': K, 'whole_parameter_cone_Gaussian_and_root_guards_passed': True,
        'complete_absolute_norm_upper': {str(2*k): str(moment_intervals[k-1][1]/phase_constants[k-1]) for k in [1, 2, 3]},
        'complete_absolute_inverse_eighth_norm_upper': str(t3[1]/(phase_constants[2]*R**2)),
        'different_arithmetic_implementation_used': False,
        'analytic_complete_product_or_norm_lemma_authenticated_by_checker': False,
        'companion_sector_or_slab_certified_by_this_checker': False, 'rh_proved': False,
        'source_sha256': {str(p.relative_to(WAVE)): digest(p) for p in sources},
        'backend_binary_sha256': {p.name: digest(p) for p in binaries},
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(result['status'], 'PREFIX', prefix_count, 'K', K, flush=True)


if __name__ == '__main__':
    main()
