#!/usr/bin/env python3
"""Finite directed guards for complete actual-Xi heat/scalar positivity."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import flint
from flint import arb, ctx, fmpq

HERE=Path(__file__).resolve().parent
EXPLORATORY=HERE.parent.parent
OLD=EXPLORATORY/'2026-10-10-four-hour-wave'
PRIOR=OLD/'xi/outer-ray'


def need(ok: bool, why: str) -> None:
    if not ok:
        raise SystemExit('FAIL: '+why)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def interval(value: arb) -> list[str]:
    need(value.is_finite(),'finite directed interval')
    return [str(value.lower().fmpq()),str(value.upper().fmpq())]


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'global_scalar_positivity.json')
    args=parser.parse_args()
    need(flint.__version__=='0.9.0' and flint.__FLINT_VERSION__=='3.6.0','native backend versions')
    ctx.prec=320
    receipt_path=PRIOR/'sixteenth_moment_census.json'
    need(sha(receipt_path)=='964f49cc79a61b354cd77fe1f077637e54bb46f39a5643e1455e87f60fabc4d6',
         'explicit frozen count-free source census')
    prior=json.loads(receipt_path.read_text())
    need(prior['status']=='PASS_DIRECTED_COUNT_FREE_SIXTEENTH_MOMENT_CENSUS'
         and prior['historical_Gram_Rosser_contract_used_by_this_theorem'] is False
         and any(x['height']==5419 and x['recovered_complete_simple_positive_zero_count']==4968
                 for x in prior['recovered_domains']),'complete count-free real head5419')
    for path,expected in prior['source_sha256'].items():
        need(sha(OLD/path)==expected,'inherited census direct source '+path)
    candidates_path=PRIOR/'native_candidates.json'
    candidates=json.loads(candidates_path.read_text())
    lo,hi=candidates['interval_numerators'][0]
    denominator=candidates['denominator']
    need(candidates['normalization']=='Xi(z)=xi(1/2+i*z)'
         and 14<fmpq(lo,denominator)<fmpq(hi,denominator)<15,'inherited actual first root interval')

    U=arb(fmpq(1,100000))
    delta=arb(fmpq(1,20))
    log2,log8=arb(2).log(),arb(8).log()
    need(12*U<delta<1 and (9*U).exp()<2,'complete negative Gamma region')
    need(2<log8<3 and log8>4*U,'complete prime integral monotonicity/tail guard')
    J=((1-arb(-1).exp())/(1-(-delta).exp())).log()
    C=J-arb.const_euler()-arb.pi().log()-20*arb(fmpq(-125,8)).exp()-18*U
    D=21*(-log2*log2/(4*U)).exp()+4*U*(-log8*log8/(8*U)).exp()
    small=C-2*D
    need(small>0,'uniform entire small-time full Gamma-minus-prime positivity')
    R=arb(5419)
    rate=R*R-arb(fmpq(1,4))-225
    need(rate>0,'strict large-time tail/head decay')
    B=(R*R+1/U)*(-U*rate).exp()
    need(B<1,'uniform complete large-time tail/head ratio')

    sources=[Path(__file__).resolve(),HERE/'GLOBAL_SCALAR_MOMENT_POSITIVITY.md',
             HERE/'COMPLETE_PRIME_HEAT_TRACE.md',HERE/'FINITE_CENSUS_HEAT_DERIVATIVE_CONE.md',
             receipt_path,candidates_path,PRIOR/'SIXTEENTH_MOMENT_CENSUS_RECOVERY.md',
             OLD/'heights/COARSE_ZERO_COUNT.md',PRIOR/'THEOREM.md']
    package=Path(flint.__file__).resolve().parent
    bins=[package/'types/arb.abi3.so']
    bins.extend(sorted((package.parent/'python_flint.libs').glob('lib*.so*')))
    result={'status':'PASS_DIRECTED_GLOBAL_ACTUAL_HEAT_AND_SCALAR_MOMENT_POSITIVITY_GUARDS',
            'normalization':'Xi(z)=xi(1/2+i*z), K(u)=sum_(Re rho>0)m_rho exp(-rho^2*u)',
            'precision_bits':320,'small_time_upper':'1/100000','Gamma_positive_segment':['1/20','1'],
            'literal_prime_upper_bound_split':8,'complete_small_time_Gamma_lower_constant':interval(C),
            'complete_small_time_prime_upper_constant':interval(D),
            'strict_complete_small_time_margin_C_minus_2D':interval(small),
            'complete_large_time_tail_head_ratio_at_split':interval(B),
            'imported_complete_count_free_real_head':5419,
            'known_actual_first_real_root_interval':[str(fmpq(lo,denominator)),str(fmpq(hi,denominator))],
            'all_positive_heat_times_covered_by_analytic_proof':True,
            'all_scalar_orders_and_all_nonnegative_shifts_covered_by_analytic_proof':True,
            'native_checker_enumerates_infinite_times_or_orders':False,
            'infinite_analytic_source_and_transport_proof_explicitly_imported':True,
            'complete_zero_count_routine_called':False,'historical_zero_count_used':False,
            'new_endpoint_sign_or_high_jet_replay':False,
            'all_heat_derivative_or_Hankel_Hausdorff_signs_proved':False,'RH_proved_or_refuted':False,
            'source_sha256':{str(p.relative_to(EXPLORATORY)):sha(p) for p in sources},
            'backend_binary_sha256':{p.name:sha(p) for p in bins}}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],flush=True)


if __name__=='__main__':
    main()
