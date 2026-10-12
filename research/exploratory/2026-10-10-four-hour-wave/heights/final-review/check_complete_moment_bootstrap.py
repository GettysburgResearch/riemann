#!/usr/bin/env python3
"""Directed full logarithmic moments bootstrap zero exclusion; no root input."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import flint
from flint import acb, acb_series, arb, ctx, fmpq

HERE=Path(__file__).resolve().parent
WAVE=HERE.parents[1]
SOURCE=WAVE/'xi'/'outer-ray'


def need(condition:bool,message:str)->None:
    if not condition:
        raise SystemExit('FAIL: '+message)


def digest(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def projection(k:int,R:fmpq,A:fmpq)->fmpq:
    return sum(((-1)**j*math.comb(2*k,2*j)*R**(2*k-2*j)*A**(2*j)
                for j in range(k+1)),fmpq(0))/(R*R+A*A)**k


def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    ctx.prec,ctx.cap=224,13
    need(flint.__version__=='0.9.0' and flint.__FLINT_VERSION__=='3.6.0','frozen directed native backend')
    z=acb_series([0,1],13)
    s=acb(arb(fmpq(1,2)))+acb(0,1)*z
    pi=arb.pi()
    xi=s*(s-1)/2*(-s*pi.log()/2).exp()*(s/2).gamma()*s.zeta()
    need(xi[0].real>arb(fmpq(99,200)) and not xi[0].contains(0),'strict actual Xi seed and divisor')
    for j in range(13):
        need(xi[j].contains(0) if j%2 else xi[j].imag.contains(0),'analytic source parity/reality enclosure')
    native=(xi/xi[0]).log()
    need(pi<arb(fmpq(22,7)) and pi>arb(fmpq(314159,100000)),'fresh directed strict pi constants')
    need(fmpq(22,7)**3/63<fmpq(99,200),'source-theta zero-free disk seed margin')
    A=fmpq(1,2)
    steps=[(2,fmpq(12)),(3,fmpq(13)),(4,fmpq(27,2)),(5,fmpq(139,10)),(6,fmpq(14))]
    R=fmpq(5)
    domains=[]
    for k,H in steps:
        need(fmpq(k)/R<1,'strict complete-source acute-angle sufficient guard')
        c=projection(k,R,A)
        need(c>0,'positive exact angular projection')
        need(native[2*k].imag.contains(0),'complete logarithmic coefficient reality')
        coefficient=-k*native[2*k].real
        need(coefficient>0,'strict native complete moment enclosure')
        low,high=coefficient.lower().fmpq(),coefficient.upper().fmpq()
        ratio=high*(H*H+A*A)**k/c
        need(ratio<1,'strict complete-source unselected zero exclusion')
        domains.append({'prior_real_part_exclusion':str(R),'moment_order':k,
                        'new_real_part_exclusion':str(H),'projection_exact':str(c),
                        'native_complete_coefficient_interval':[str(low),str(high)],
                        'exclusion_ratio_upper_exact':str(ratio),'strict_margin_exact':str(1-ratio)})
        R=H
    need(R==14,'final global real-part exclusion')
    x=fmpq(1,28)
    atan_upper=x-x**3/3+x**5/5
    need(44*atan_upper<fmpq(314159,200000),'exact endpoint acute-angle comparison')
    projections={str(k):str(projection(k,R,A)) for k in range(1,23)}
    need(all(fmpq(value)>0 for value in projections.values()),'all22exactglobalpositiveprojections')
    # A complete quartet at +/-1+/-i has negative fourth inverse moment;
    # this exact control preserves the necessity of the acute hypothesis.
    need(2*(fmpq(1)-6*fmpq(1)+fmpq(1))/(fmpq(1)+fmpq(1))**4==fmpq(-1,2),'nonacute quartet countercontrol')
    paths=[Path(__file__).resolve(),HERE/'COMPLETE_MOMENT_ZERO_FREE_BOOTSTRAP.md',
           SOURCE/'THEOREM.md',SOURCE/'COUNT_FREE_CENSUS_RECOVERY.md',
           SOURCE/'HIGHER_MOMENT_CENSUS_RECOVERY.md']
    package=Path(flint.__file__).resolve().parent
    binaries=[package/'types'/name for name in ['arb.abi3.so','acb.abi3.so','acb_series.abi3.so']]
    binaries.extend(sorted((package.parent/'python_flint.libs').glob('lib*.so*')))
    report={'status':'PASS_DIRECTED_COMPLETE_MOMENT_ZERO_FREE_BOOTSTRAP',
            'normalization':'Xi(z)=xi(1/2+i*z)','arithmetic':'Arb/acb/acb_series outward ball arithmetic at224bits; exact rational acceptance predicates.',
            'native_jet_degree_replayed':12,'native_complete_moment_orders_replayed':[2,3,4,5,6],
            'strict_xi_zero_seed_lower':str(xi[0].real.lower().fmpq()),
            'initial_theta_zero_free_disk_radius':'11/2','complete_strip_half_width':'1/2',
            'final_all_source_root_real_part_exclusion':'abs(Re rho)>14',
            'all_steps':domains,'higher_acute_projection_orders':list(range(1,23)),
            'higher_positive_projections_exact':projections,
            'k22_arctangent_upper_exact':str(44*atan_upper),
            'directed_pi_lower_rational':'314159/100000',
            'finite_root_input_or_strict_sign_receipt_used':False,
            'complete_zero_count_or_root_enumeration_routine_called':False,
            'historical_Gram_Rosser_or_published_verification_used':False,
            'higher_native_jet_above_degree12_replayed':False,
            'new_residual_census_height_certified':False,
            'analytic_complete_theta_strip_product_authenticated_by_checker':False,
            'different_arithmetic_backend_used':False,'rh_proved':False,
            'source_sha256':{str(path.relative_to(WAVE)):digest(path) for path in paths},
            'backend_binary_sha256':{path.name:digest(path) for path in binaries}}
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(report['status'],flush=True)


if __name__=='__main__':
    main()
