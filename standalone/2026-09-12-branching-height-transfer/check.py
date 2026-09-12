#!/usr/bin/env python3
"""BHT26 bounded exact controls, NOT a xi zero census or a formal proof."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

N0 = 1 << 18
RADIUS_DIVISOR = 500
PAYLOAD = ('PROOF.md', 'README.md', 'REVIEW.md', 'SOURCES.json',
           'VALIDATION.md', 'check.py', 'test_check.py', 'result.json')


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def fq(x: Q | int) -> str:
    return str(Q(x))


def ceil_log2(n: int) -> int:
    if type(n) is not int or n < 1:
        raise ValueError('ceil_log2 requires a positive integer')
    return (n - 1).bit_length()


def prescription(n: int) -> dict:
    if type(n) is not int or n < N0:
        raise ValueError('height must be an integer at least 2^18')
    ell = ceil_log2(n + 12)
    k = n // (RADIUS_DIVISOR * ell)
    require(k >= ell + 8, 'radius exponent induction bound')
    require(96 * ell * 4 < 2 ** (ell + 8), 'cluster size induction bound')
    reserve = Q(3*n, 50) - 111*ell - 11
    require(reserve > 0, 'coarse logarithmic Rouche reserve')
    return {'height_and_onset': n, 'ell': ell, 'radius_exponent': k,
            'radius': f'2^-{k}', 'log_ratio_upper_lt': fq(-reserve),
            'cluster_diameter_upper': f'{96*ell} * 2^-{k}',
            'actual_zero_locations_computed': False}


def log_bounds(x: Q, terms: int = 64) -> tuple[Q, Q]:
    if not isinstance(x, Q) or x < 1:
        raise ValueError('log routine requires rational x >= 1')
    u = (x-1)/(x+1)
    low = 2 * sum((u**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
    tail = 2*u**(2*terms+1)/((2*terms+1)*(1-u*u))
    return low, low+tail


def atan_bounds(x: Q, terms: int = 64) -> tuple[Q, Q]:
    require(Q(0) <= x <= 1, 'atan range')
    partial = sum(((-1)**j*x**(2*j+1)/Q(2*j+1)
                   for j in range(terms)), Q(0))
    other = partial + (-1)**terms*x**(2*terms+1)/Q(2*terms+1)
    return min(partial, other), max(partial, other)


def decimal_bracket(low: Q, high: Q, digits: int = 18) -> list[str]:
    base = 10**digits
    a = (low.numerator*base)//low.denominator
    b = -((-high.numerator*base)//high.denominator)
    def render(n: int) -> str:
        return f'{n//base}.{n%base:0{digits}d}'
    return [render(a), render(b)]


def inverse_moment(b: int) -> Q:
    require(1 <= b < 5, 'inverse exponent for Gamma(5)')
    u = Q(2**(2*b+1)-1, 2*b+1)
    denominator = 1
    for j in range(1, b+1):
        denominator *= 5-j
    return u * Q(5, 2)**b / denominator


def coeffs(q: Q, a: int = 40) -> list[Q]:
    # product ((z-a)^2+q)((z+a)^2+q), increasing powers
    return [(a*a+q)**2, Q(0), 2*(q-a*a), Q(0), Q(1)]


def reconstruct() -> dict:
    r = Q(31,80)
    a2 = Q(7,24)
    a3 = Q(31,160)
    require(2*a2 == Q(7,12), 'shared-uniform coupling')
    m30 = Q(63,25)
    m3star = (a3*6*Q(7,5))/(1-2*a3)
    d0 = (m3star-m30)/6
    require(m3star == Q(93,35) and d0 == Q(4,175), 'native moment normalization')
    moments = []
    m3, m4 = m30, Q(693,125)
    for depth in range(13):
        require(m3 == m3star-6*d0*r**depth, 'third moment independent recurrence')
        require(m4 < 8, 'fourth moment bounded panel')
        moments.append({'depth': depth, 'third': fq(m3), 'fourth': fq(m4)})
        m4 = Q(127,896)*(2*m4+8*m3+6*Q(7,5)**2)
        m3 = a3*(2*m3+6*Q(7,5))
    inv = {str(b): fq(inverse_moment(b)) for b in range(1,5)}
    require(inverse_moment(1) == Q(35,24), 'inverse first normalization')
    require(inverse_moment(4) == Q(319375,3456) < 100, 'inverse fourth normalization')
    require(2*200*d0/8 == Q(8,7), 'complex-power third-derivative coefficient')
    # At T+5 >= 5 the reflected normalization fits 2(T+5)^3.
    require(2*5**3-Q(4,7)*(2*5**3+6) > 0, 'extended-strip coarse envelope')
    # The local analytic inequalities reduce to these exact endpoint guards.
    b = Q(10)
    em = 1+b/2+b*b/12+b**4/720+b**5/720
    require(em < b**5 and 2*b**5 <= b**6, 'Euler--Maclaurin disk bound')
    harnack = (Q(3)+Q(5,2))/(Q(3)-Q(5,2))
    require(harnack == 11 and 6*(harnack-1) == 60, 'Harnack power')
    require(16+3*Q(5,2) < 24, 'Blaschke denominator')
    binet_constant = -Q(5,12)-Q(7,4)-Q(1,9)
    require(binet_constant > -3 and 2*27*4 < 256, 'gamma lower prefactor')
    log_lo = Q(6,7)+Q(18,343)
    require(log_lo == Q(312,343) > Q(9,10), 'log contraction lower bound')
    gap = Q(9,10)-Q(11,14)-Q(24,RADIUS_DIVISOR)
    require(gap > Q(3,50), 'height-exponent reserve')
    require(Q(3*N0,50)-111*19-11 > 0, 'all-N reserve base')
    require(Q(3,50)-Q(111,N0+12) > 0, 'all-N reserve monotonicity')
    induction = []
    for ell in range(19,49):
        a = 2**(ell-1)-12
        c = RADIUS_DIVISOR*ell*(ell+8)
        require(a >= c, 'dyadic-block base inequality')
        poly = 2*ell*(ell+8)-(ell+1)*(ell+9)
        require(poly == ell*ell+6*ell-9 > 0, 'dyadic induction polynomial')
        induction.append({'ell': ell, 'base_margin': a-c,
                          'induction_polynomial': poly})
    heights = sorted(set([N0,N0+1,2**19-13,2**19-12,2**19-11,
                          10**6,2**20,2**24]))
    samples = [prescription(n) for n in heights]
    # A second ceil-log implementation, intentionally only a bounded control.
    for n in heights:
        e, t = 0, 1
        while t < n+12:
            t *= 2
            e += 1
        require(e == ceil_log2(n+12), 'power-of-two endpoint convention')
    lamlo, lamhi = log_bounds(Q(80,31))
    al, ah = atan_bounds(Q(1,5)); bl, bh = atan_bounds(Q(1,239))
    plo, phi = 16*al-4*bh, 16*ah-4*bl
    require(Q(3)<plo<phi<Q(22,7), 'Machin pi brackets')
    speed = decimal_bracket(4*lamlo/phi, 4*lamhi/plo)
    synthetic = []
    q0 = Q(1,16)
    p0 = coeffs(q0)
    for m in (0,1,2,5,10,20):
        e = r**m/100
        q = q0+e
        require(0<q<Q(1,4), 'synthetic quartet stays in band')
        p = coeffs(q)
        difference = [p[j]-p0[j] for j in range(5)]
        wanted = [2*(1600+q0)*e+e*e,0,2*e,0,0]
        require(difference == wanted, 'whole polynomial error identity')
        # Positivity on the imaginary axis has three positive coefficients.
        require(p[0]>0 and -p[2]>0 and p[4]>0, 'imaginary-axis positivity')
        synthetic.append({'depth':m,'q':fq(q),'difference':[fq(v) for v in difference],
                          'noncentral_real_frequency':40,
                          'three_protected_real_zeros':[5,15,25]})
    return {'schema':'BHT26-v1',
            'status':{'rh_proved':False, 'unbounded_line_confinement_proved':False,
                      'new_actual_zero_census':False, 'formal_proof':False,
                      'analytic_theorems':'proposed; independent review required'},
            'source_constants':{'r':fq(r),'d0':fq(d0),'inverse_moments':inv,
                                'extended_strip_coefficient':fq(Q(8,7))},
            'moment_panels':moments,
            'local_guards':{'EM_bound_at_10':fq(em), 'Harnack':fq(harnack),
                            'Binet_constant':fq(binet_constant),'exponent_gap':fq(gap)},
            'induction_panels':induction,'height_prescriptions':samples,
            'comparison_speed_interval':speed,
            'synthetic_control':synthetic,
            'scope':'exact finite controls of constants and algebra; no analytic zero evaluation'}


def load_strict(path: Path) -> dict:
    def pairs(items):
        out = {}
        for key,value in items:
            if key in out:
                raise ValueError(f'duplicate key: {key}')
            out[key] = value
        return out
    def reject(value):
        raise ValueError(f'noninteger JSON number: {value}')
    return json.loads(path.read_text('utf-8'), object_pairs_hook=pairs,
                      parse_float=reject, parse_constant=reject)


def canonical(obj: object) -> str:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def authenticate(root: Path) -> None:
    expected = set(PAYLOAD) | {'SHA256SUMS'}
    entries = list(root.iterdir())
    require({p.name for p in entries} == expected, 'packet inventory mismatch')
    require(all(p.is_file() and not p.is_symlink() for p in entries),
            'only regular non-symlink files accepted')
    rows = (root/'SHA256SUMS').read_text('ascii').splitlines()
    seen = set()
    for row in rows:
        digest, name = row.split('  ')
        require(name in PAYLOAD and name not in seen, 'bad/duplicate manifest path')
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),
                'invalid digest')
        seen.add(name)
        require(hashlib.sha256((root/name).read_bytes()).hexdigest() == digest,
                f'content mismatch: {name}')
    require(seen == set(PAYLOAD), 'incomplete manifest')


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', type=Path)
    ap.add_argument('--emit', type=Path)
    args = ap.parse_args()
    try:
        expected = reconstruct()
        if args.emit:
            require(not args.check, 'choose one mode')
            args.emit.write_text(json.dumps(expected, indent=2, sort_keys=True)+'\n', 'utf-8')
            print('PRODUCER_OUTPUT_ONLY; no package acceptance claimed')
            return 0
        require(args.check is not None, '--check or --emit required')
        authenticate(Path(__file__).resolve().parent)
        observed = load_strict(args.check)
        require(canonical(observed) == canonical(expected), 'typed primitive reconstruction mismatch')
        digest = hashlib.sha256(canonical(expected).encode('ascii')).hexdigest()
        print('PASS_BHT26_BOUNDED_CONTROLS', digest)
        print('No new xi zero count; no unbounded critical-line confinement; RH not proved.')
        return 0
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print('REJECT:', str(exc), file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
