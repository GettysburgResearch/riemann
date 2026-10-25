#!/usr/bin/env python3
"""Finite full-Weil variance-selector experiment, not interval certification.

Uses the exact archived PR1017 matrix-assembly source (source/experiment.py).
Every prime power through exp(2a), the archimedean tail, and both pole terms
are retained. Xi supplies only the explicitly declared target variance.
No zero ordinates enter the assembly or selection.

mpmath is required. A local .deps installation is accepted for this scratch
run; a normal mpmath installation is sufficient for reproduction elsewhere.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
try:
    import mpmath as mp
except ModuleNotFoundError:
    sys.path.insert(0, str(HERE / '.deps'))
    import mpmath as mp


def source_module(path):
    spec = importlib.util.spec_from_file_location('pinned_weil_source', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fmt(x, digits=45):
    return mp.nstr(mp.re(x), digits)


def physical_grid(c, a, points):
    values = []
    for j in range(points + 1):
        x = a * j / points
        value = (1 + mp.sqrt(2) * mp.fsum(
            c[n] * mp.cos(mp.pi * n * x / a)
            for n in range(1, len(c)))) / (2*a)
        values.append(value)
    step = a / points
    neg = 2*step*mp.fsum(
        (mp.mpf('.5') if j in (0,points) else 1)
        * max(mp.mpf(0), -v) * mp.exp(a*j/points)
        for j,v in enumerate(values))
    # These are sampled values and an ordinary trapezoidal diagnostic only.
    return {'points_on_half_interval':points+1,
            'minimum_sampled_density':fmt(min(values)),
            'maximum_sampled_density':fmt(max(values)),
            'minimum_sample_location':fmt(a*values.index(min(values))/points),
            'endpoint_density':fmt(values[-1]),
            'negative_part_exp_weight_trapezoid':fmt(neg),
            'global_nonnegativity_certified':False}


def run_one(src, a_text, modes, dps, order, points):
    with mp.workdps(dps):
        a = mp.mpf(a_text)
        full,E,O,prime_data,safe = src.assemble(a,modes,order,True)
        ev,Q = mp.eigsy(E)
        ov = mp.eigsy(O,eigvals_only=True)
        low = min(ev[0],ov[0])
        if abs(low) < mp.power(10,-dps+25):
            raise RuntimeError('Finite spectral bottom below declared resolution')
        vx = mp.re(-mp.diff(lambda z:src.xi(z)/src.xi(0),0,2))

        def vector(shift):
            c = mp.matrix([mp.fsum(Q[i,j]*Q[0,j]/(ev[j]-shift)
                                  for j in range(modes+1))
                           for i in range(modes+1)])
            return c/c[0]

        def variance(c):
            return -2*src.log_coefficients(c,a,count=1)[0]

        gap = abs(low)*mp.mpf('1e-15')
        near = low-gap
        left,right = safe,near
        fleft = variance(vector(left))-vx
        fright = variance(vector(right))-vx
        record = {'halfwidth':a_text,'modes_each_side':modes,
                  'decimal_precision':dps,'quadrature_order':order,
                  'prime_powers':[n for n,_,_,_ in prime_data],
                  'even_min':fmt(ev[0]),'odd_min':fmt(ov[0]),
                  'second_even':fmt(ev[1]),'target_xi_variance':fmt(vx),
                  'safe_shift':fmt(safe),'safe_variance':fmt(fleft+vx),
                  'near_finite_bottom_shift':fmt(near),
                  'near_finite_bottom_variance':fmt(fright+vx),
                  'opposite_sign_endpoint_bracket':bool(fleft*fright<0),
                  'continuum_shift_legality_certified':False,
                  'analytic_selector_exists_proved':False}
        if fleft*fright >= 0:
            return record
        middle=None
        for iteration in range(4*dps):
            middle=(left+right)/2
            cm=vector(middle)
            fm=variance(cm)-vx
            if abs(fm)<mp.mpf('1e-36'):
                break
            if fm*fleft>0:
                left,fleft=middle,fm
            else:
                right,fright=middle,fm
        else:
            raise RuntimeError('Variance bisection did not reach requested residual')
        c=vector(middle)
        r=(E-middle*mp.eye(modes+1))*c
        max_resid=max([abs(r[j]) for j in range(1,modes+1)]+[mp.mpf(0)])
        record['selected']={'shift':fmt(middle),
                            'finite_spectral_margin':fmt(low-middle),
                            'variance':fmt(variance(c)),
                            'variance_residual':fmt(variance(c)-vx),
                            'linear_system_off_forcing_residual':fmt(max_resid),
                            'iterations':iteration+1,
                            'normalized_even_coefficients':[fmt(x,70) for x in c],
                            'physical_grid':physical_grid(c,a,points)}
        return record


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,default=HERE/'source/experiment.py')
    parser.add_argument('--a',nargs='+',default=['0.4','0.6','0.8','1.0','1.3'])
    parser.add_argument('--modes',type=int,default=16)
    parser.add_argument('--dps',type=int,default=110)
    parser.add_argument('--order',type=int,default=160)
    parser.add_argument('--points',type=int,default=512)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    src=source_module(args.source)
    report={'scope':'FINITE_FULL_SOURCE_GALERKIN_EXPLORATION_NOT_CERTIFIED',
            'source_commit':'450dd8abecf58dfe60b3bc39bda0f792ea82ce95',
            'source_archive_member':'standalone/2026-10-22-weil-resolvent-selection/experiment.py',
            'source_sha256':'79563f448d916f400ecc22f3461d6d3583c5604100cba6c7c61c705ebf500463',
            'mpmath_version':mp.__version__,'cases':[]}
    for a in args.a:
        result=run_one(src,a,args.modes,args.dps,args.order,args.points)
        report['cases'].append(result)
        print(json.dumps({'a':a,'even_min':result['even_min'],
                          'bracket':result['opposite_sign_endpoint_bracket'],
                          'near_variance':result['near_finite_bottom_variance'],
                          'selected_shift':result.get('selected',{}).get('shift'),
                          'sampled_min':result.get('selected',{}).get('physical_grid',{}).get('minimum_sampled_density')}),flush=True)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
