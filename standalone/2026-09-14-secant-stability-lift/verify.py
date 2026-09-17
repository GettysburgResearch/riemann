#!/usr/bin/env python3
"""Exact bounded checks for the secant-stability lift.

No floating arithmetic, zeta data, eigenvalue oracle, or seven-gap search.
The all-matrix statement is proved in PROOF.md, not by the finite spectra.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path

BITS = 200
K = F(19, 5000)
SIGMA = F(1, 500)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sqrt_bounds(x: F, bits: int = BITS) -> tuple[F, F]:
    require(x >= 0, "negative radicand")
    scale = 1 << bits
    r = isqrt((x.numerator * scale * scale) // x.denominator)
    lo, hi = F(r, scale), F(r + 1, scale)
    require(lo * lo <= x <= hi * hi, "invalid square-root bracket")
    return (lo, lo) if lo * lo == x else (lo, hi)


def mt_bounds(terms: int = 48) -> tuple[F, F]:
    # x=1/sqrt(2): x*cot(x)=cos(x)/sinc(x). Both power series are rational.
    cs = [sum((F((-1)**j, 2**j * factorial(2*j)) for j in range(n)), F(0))
          for n in (terms, terms + 1)]
    ss = [sum((F((-1)**j, 2**j * factorial(2*j+1)) for j in range(n)), F(0))
          for n in (terms, terms + 1)]
    cl, cu, sl, su = min(cs), max(cs), min(ss), max(ss)
    require(cl > 0 and sl > 0, "series denominator")
    return F(3,2)-cu/sl, F(3,2)-cl/su


def q_of(m: int) -> F:
    return K*(m-6)


def spike_cost(m: int, q: F) -> tuple[F, F]:
    """Exact equicorrelation cost; only a proved LOWER envelope when q<2."""
    require(m >= 2 and 0 < q <= m*(m-1), "infeasible spike")
    if q <= F(m, m-1):
        return q, q
    lo, hi = sqrt_bounds(F(m-1, m)*q)
    return 2*lo-1+q/m, 2*hi-1+q/m


def lift_bounds(m: int, h: tuple[F, F]) -> tuple[F, F]:
    q = q_of(m)
    cl, cu = spike_cost(m, q)
    vals = []
    for hv in h:
        for c in (cl, cu):
            require(1-c/m > 0, "lift denominator")
            vals.append((hv-(c/q)*SIGMA*F(m-1,m))/(1-c/m))
    return min(vals), max(vals)


def legacy280(h: tuple[F, F]) -> tuple[F,F]:
    m=280
    cl,cu=spike_cost(m,q_of(m))
    vals=[(hv-SIGMA*F(m-1,m))/(1-c/m) for hv in h for c in (cl,cu)]
    return min(vals),max(vals)


def decimal_enclosure(bounds: tuple[F,F], places: int=30) -> dict:
    s=10**places
    low=(bounds[0].numerator*s)//bounds[0].denominator
    high=-((-bounds[1].numerator*s)//bounds[1].denominator)
    def text(v):
        sign='-' if v<0 else ''
        v=abs(v)
        return f'{sign}{v//s}.{v%s:0{places}d}'
    return {'lower':text(low),'upper':text(high),'denominator':s,
            'lower_numerator':low,'upper_numerator':high}


def psi(x: F) -> F:
    require(x >= 0, "non-PSD spectrum")
    return (x-1)**2 if x <= 2 else 2*x-3


def secant_test(m:int, q:F, energy:F, delta:F) -> bool:
    # Test delta >= phi_m(q)*min(E,q)/q WITHOUT an approximate square root.
    e=min(energy,q)
    if q <= F(m,m-1):
        return delta >= e
    w=e/q
    left=delta-w*(-1+q/m)
    return left >= 0 and left*left >= 4*w*w*F(m-1,m)*q


def partitions(total:int, slots:int, minimum:int=0):
    if slots==1:
        if total>=minimum:
            yield (total,)
        return
    for j in range(minimum,total//slots+1):
        for rest in partitions(total-j,slots-1,j):
            yield (j,)+rest


def reconstruct() -> dict:
    h=mt_bounds()
    h_alt=mt_bounds(56)
    require(h[0]<=h_alt[0]<=h_alt[1]<=h[1], 'alternative longer-series bracket')
    require(h[0]>F(6725,10000) and h[1]<F(672501,10**6), 'MT scale')
    winner=322
    best=lift_bounds(winner,h)
    require(q_of(winner)<2, 'winning lower-envelope domain')
    old=legacy280(h)
    require(best[0]>old[1], 'no strict improvement')
    require(best[0]>F(6730129,10**7), 'headline ceiling not reached')
    candidates=[]
    runner=(-1,F(0))
    for m in range(7,2000):
        b=lift_bounds(m,h)
        # For q>=2 this is an UPPER bound on a trace-only affine deduction,
        # obtained by testing one feasible equicorrelation matrix, not a
        # claimed lower spectral envelope or new feasible zeta bound.
        upper=max(h[1],b[1])
        candidates.append([m,decimal_enclosure(b,24)])
        if m!=winner:
            require(upper<best[0], f'undominated block size {m}')
            if upper>runner[1]:runner=(m,upper)
    # Every m>=2000: c_m/q_m <=2/sqrt(q_m)+1/m <=3/4.
    qtail=q_of(2000)
    require(F(4)/qtail < (F(3,4)-F(1,2000))**2, 'tail slope')
    require(6*K*h[0]>SIGMA, 'negative finite-size correction')
    tail_upper=h[1]+F(3,4)*(K*h[1]-SIGMA)/(1-F(3,4)*K)
    require(tail_upper<best[0], 'infinite tail not dominated')

    spectra=0; predicates=0; large_energy=0
    for m in range(2,8):
        for parts in partitions(4*m,m):
            lam=[F(j,4) for j in parts]
            e=sum(((x-1)**2 for x in lam),F(0))
            d=sum((psi(x) for x in lam),F(0))
            spectra+=1
            if e>=2:large_energy+=1
            for q in (F(1,5),F(3,4),F(11,10),F(17,10)):
                require(secant_test(m,q,e,d),'finite spectrum violates secant')
                predicates+=1

    equality=0; robust=0
    for m in (3,4,7,20,280,322,533,2000):
        for a in (F(1,2),F(1),F(11,10),F(6,5)):
            q=F(m,m-1)*a*a
            if not(q<2):continue
            lam=[1+a]+[1-a/(m-1)]*(m-1)
            require(min(lam)>=0, 'equality PSD')
            d=sum((psi(x) for x in lam),F(0))
            c=q if a<=1 else q-(a-1)**2
            require(d==c,'spike equality')
            require(secant_test(m,q,q,d), 'spike secant equality')
            equality+=1
            for t in (F(1,4),F(1,2),F(3,4),F(1)):
                # G=t*G_spike: diag t, off-diagonal energy t^2*q.
                dg=sum((psi(t*x) for x in lam),F(0))
                z=max(F(0),q-t*t*q)
                require(dg>=c*(1-z/q)-2*m*(1-t),'robust trace-defect case')
                robust+=1

    # Algebraic pinching/offset accounting: every length-m window belongs to
    # exactly one offset, and each interior gap occurs at most m-1 times.
    window_cases=0
    for m in range(2,15):
        for r in range(m,4*m+1):
            windows=[(j,j+m-1) for j in range(r-m+1)]
            groups=[[(j,j+m-1) for j in range(off,r-m+1,m)] for off in range(m)]
            require(sorted(w for g in groups for w in g)==windows,'offset exhaustion')
            counts=[sum(a<=g<b for a,b in windows) for g in range(r-1)]
            require(max(counts)<=m-1,'gap overcount')
            window_cases+=1
    return {
        'schema':1,
        'status':'PROPOSED_FINITE_THEOREM_INPUT_QUALIFIED_ZETA_COROLLARY',
        'rh_proved':False,
        'new_seven_point_search_performed':False,
        'external_analytic_replay_performed':False,
        'baseline_main':'f99d9e3908dde4865377c75d9ca051c1f545bf4f',
        'H_MT':decimal_enclosure(h),
        'legacy_280':decimal_enclosure(old),
        'winning_m':winner,
        'winning_q':[q_of(winner).numerator,q_of(winner).denominator],
        'winning_c':decimal_enclosure(spike_cost(winner,q_of(winner))),
        'new_input_qualified_bound':decimal_enclosure(best),
        'improvement_fraction':decimal_enclosure((best[0]-old[1],best[1]-old[0])),
        'improvement_percentage_points':decimal_enclosure((100*(best[0]-old[1]),100*(best[1]-old[0]))),
        'finite_m_range':[7,1999],
        'finite_m_count':len(candidates),
        'finite_m_brackets_sha256':hashlib.sha256(canonical(candidates)).hexdigest(),
        'runner_up_m':runner[0],
        'runner_gap_lower':decimal_enclosure((best[0]-runner[1],best[0]-runner[1])),
        'all_m_ge_2000_upper':decimal_enclosure((tail_upper,tail_upper)),
        'finite_spectra':spectra,
        'spectral_predicates':predicates,
        'spectra_with_energy_ge_two':large_energy,
        'sharp_spike_spectra':equality,
        'robust_trace_defect_cases':robust,
        'offset_cases':window_cases,
        'arithmetic':'integers/Fraction; 200-bit integer-root enclosures; alternating rational series',
        'global_optimization_scope':'trace-and-pressure-only affine block deductions, and fixed finite convex mixtures thereof; not all kernel arguments'
    }


def canonical(x) -> bytes:
    return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False).encode()


def seal(body):
    return {'body':body,'sha256':hashlib.sha256(canonical(body)).hexdigest()}


def reject_number(x):
    raise ValueError('noninteger JSON number is not permitted')


def no_duplicates(pairs):
    obj={}
    for k,v in pairs:
        require(k not in obj,'duplicate JSON key')
        obj[k]=v
    return obj


def read_json(path):
    require(path.is_file() and not path.is_symlink(),'report must be a regular file')
    return json.loads(path.read_text(),object_pairs_hook=no_duplicates,
                      parse_float=reject_number,parse_constant=reject_number)


def accept(receipt,expected):
    require(isinstance(receipt,dict) and set(receipt)=={'body','sha256'},'receipt shape')
    require(receipt['sha256']==seal(receipt['body'])['sha256'],'digest mismatch')
    require(canonical(receipt['body'])==canonical(expected),'fresh reconstruction mismatch')


def self_test(expected):
    mutations=[lambda b:b.update(rh_proved=True),
               lambda b:b.update(winning_m=321),
               lambda b:b.update(finite_m_count=1),
               lambda b:b.update(new_seven_point_search_performed=True),
               lambda b:b.update(external_analytic_replay_performed=True),
               lambda b:b.update(schema=True),
               lambda b:b.update(winning_m=322.0),
               lambda b:b['new_input_qualified_bound'].update(lower_numerator=0),
               lambda b:b.update(global_optimization_scope='all methods and all primes'),
               lambda b:b.update(offset_cases=0)]
    for i,change in enumerate(mutations):
        bad=copy.deepcopy(expected);change(bad)
        try:accept(seal(bad),expected)
        except ValueError:pass
        else:raise ValueError(f'mutation {i} accepted')
    try:json.loads('{"x":1,"x":2}',object_pairs_hook=no_duplicates)
    except ValueError:pass
    else:raise ValueError('duplicate accepted')
    return len(mutations)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',type=Path,help='producer mode, write a new receipt')
    g.add_argument('--check',type=Path,help='reconstruct and compare without overwriting')
    p.add_argument('--self-test',action='store_true')
    args=p.parse_args()
    body=reconstruct()
    if args.write:
        require(not args.write.exists(),'refusing to overwrite an existing receipt')
        args.write.write_bytes(canonical(seal(body))+b'\n')
        print('PRODUCED',seal(body)['sha256'])
    else:
        accept(read_json(args.check),body)
        print('PASS',seal(body)['sha256'])
    if args.self_test:print('RESEALED_MUTATIONS_REJECTED',self_test(body),'DUPLICATE_REJECTED',1)
    print('SCOPE: finite/theoretical lift; inherited seven-point and analytic inputs NOT replayed')

if __name__=='__main__':
    main()
