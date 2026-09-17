#!/usr/bin/env python3
"""Exact bounded controls and receipt checking for separated-core pressure.

The analytic proof is PROOF.md. Default mode reconstructs the rational controls
and checks the inherited seven-point receipt; --full-seven also reruns its
unchanged continuum exhaustion. Neither mode proves the imported prime-side
analytic theorem or independently referees the manuscript.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
import sys
from fractions import Fraction as Q

ROOT = Path(__file__).resolve().parent
A = Q(19, 5000)
B = Q(1, 500)
DELTA = Q(2, 3)
MAJORANT_SCALE = Q(6, 5)
EXPECTED_VENDOR = {
    'dyadic_interval.py': 'c0cb7d95a231099744dbd4278b3327c020812bb1b18a35147ea761e6390432e8',
    'seven_independent_cached.py': 'bc4a638373414581515edd950d7a811b81dfe0ef3fa77d119f35b49bea6fe361',
}
EXPECTED_SEVEN = {
    'verdict': 'PASS_INDEPENDENT_DYADIC_SEVEN_POINT',
    'target': '19/5000', 'grid': 4000, 'dyadic_bits': 128,
    'components': [[3809, 4778], [7221, 9364], [10571, 44827]],
    'counts': {'nodes': 713315, 'pressure': 3072, 'interval': 259807,
               'tangent': 94143, 'splits': 356293},
    'initial_boxes': 729,
    'kernel_table_sha256': '2a68fbb3ba1da02a5c3b66589ad07bc2c21de1317d42a5f3832cad2333906fa4',
    'second_table_sha256': 'e3be7c6d5250f26f6adc3ec6a998710a7f3aba95b3badd9378ecaf54418ee7a7',
    'traversal_sha256': '4c5c0d7ddd7f34f045f16474de38c8eb0f33abd1b3d4be24066e1f84ae297abf',
    'zeta_bound_proved_by_this_code': False,
}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(x: object) -> str:
    return json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False)


def strict_load(path: Path) -> object:
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError('duplicate JSON key: ' + key)
            out[key] = value
        return out
    def bad_constant(text):
        raise ValueError('nonfinite JSON constant: ' + text)
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs,
                      parse_constant=bad_constant)


def check_vendor() -> None:
    for name, digest in EXPECTED_VENDOR.items():
        path = ROOT / 'vendor' / name
        need(path.is_file() and not path.is_symlink(), 'missing or linked vendor source')
        need(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
             'changed vendor source: ' + name)


def check_seven(path: Path) -> dict:
    got = strict_load(path)
    need(type(got) is dict, 'seven receipt is not an object')
    need(set(got) == set(EXPECTED_SEVEN) | {'seconds'}, 'seven receipt inventory')
    reduced = {key: got[key] for key in EXPECTED_SEVEN}
    need(canonical(reduced) == canonical(EXPECTED_SEVEN), 'seven receipt mismatch')
    need(type(got['seconds']) in (int, float) and math.isfinite(got['seconds'])
         and got['seconds'] >= 0, 'invalid elapsed time')
    c = got['counts']
    need(c['nodes'] == got['initial_boxes'] + 2*c['splits'], 'tree node accounting')
    need(c['pressure'] + c['interval'] + c['tangent']
         == got['initial_boxes'] + c['splits'], 'tree leaf accounting')
    return reduced


def sqrt_bounds(x: Q, bits: int = 200) -> tuple[Q, Q]:
    need(x >= 0, 'negative square root')
    scale = 1 << bits
    a = math.isqrt((x.numerator * scale * scale) // x.denominator)
    lo = Q(a, scale)
    hi = lo if lo*lo == x else Q(a+1, scale)
    need(lo*lo <= x <= hi*hi, 'square-root enclosure')
    return lo, hi


def trig_series_bounds(kind: str, last: int = 40) -> tuple[Q, Q]:
    # x^2=1/2. These are cos(x) and sin(x)/x, so all terms are rational.
    need(last % 2 == 0, 'positive terminal alternating term required')
    shift = 0 if kind == 'cos' else 1
    hi = sum((Q((-1)**k, (2**k)*math.factorial(2*k+shift))
              for k in range(last+1)), Q(0))
    lo = hi - Q(1, 2**(last+1)*math.factorial(2*(last+1)+shift))
    need(0 < lo <= hi, 'alternating trig interval')
    return lo, hi


def decimal_bracket(x: tuple[Q, Q], places: int = 45) -> list[str]:
    scale = 10**places
    lo = x[0].numerator*scale // x[0].denominator
    hi = -((-x[1].numerator*scale) // x[1].denominator)
    def fmt(n: int) -> str:
        sign = '-' if n < 0 else ''
        n = abs(n)
        return sign + str(n//scale) + '.' + str(n%scale).zfill(places)
    return [fmt(lo), fmt(hi)]


def intervals_sub(x, y):
    return x[0]-y[1], x[1]-y[0]


def constants() -> dict:
    c = trig_series_bounds('cos')
    s = trig_series_bounds('sinc')
    h = (Q(3,2)-c[1]/s[0], Q(3,2)-c[0]/s[1])
    sep = tuple((x-B)/(1-A) for x in h)
    old269 = tuple((1345000*x-2680)/1340003 for x in h)
    root = sqrt_bounds(Q(726237,700000))
    cc = tuple(2*x-1+Q(2603,700000) for x in root)
    old280 = ((h[0]-Q(279,140000))/(1-cc[0]/280),
              (h[1]-Q(279,140000))/(1-cc[1]/280))
    gain = intervals_sub(sep, old280)
    distinct = tuple((1+x)/2 for x in sep)
    need(sep[0] > Q(67305,100000), 'new simple proportion target not reached')
    need(gain[0] > Q(48,10**6), 'not a strict improvement over pinned 280 bound')
    need(old280[0] > old269[1], 'old bound consistency')
    # Verify the closing affine relation exactly, using each shared endpoint.
    for hh, ss in zip(h, sep):
        need(A*ss-B == ss-hh, 'distinct-zero adapter')
    return {'H_MT': decimal_bracket(h), 'H_269': decimal_bracket(old269),
            'H_280': decimal_bracket(old280), 'H_separated': decimal_bracket(sep),
            'distinct': decimal_bracket(distinct),
            'proportion_gain_over_280': decimal_bracket(gain),
            'percentage_point_gain_over_280': decimal_bracket(tuple(100*x for x in gain))}


def majorant_controls() -> dict:
    # y=t^2. Only explicit rational consequences of 9<pi^2<10 are used here.
    sinc_lower = [Q(1), -Q(40,27), Q(4,9)]
    cos_upper = [Q(1), -Q(1), Q(1,6)]
    p = [MAJORANT_SCALE*s-c for s,c in zip(sinc_lower, cos_upper)]
    need(p == [Q(1,5), -Q(7,9), Q(11,30)], 'majorant polynomial coefficients')
    derivative_upper = p[1] + 2*p[2]*Q(1,4)
    minimum = p[0] + p[1]/4 + p[2]/16
    need(derivative_upper < 0, 'majorant monotonicity')
    need(minimum == Q(41,1440) and minimum > 0, 'majorant endpoint')
    mass = MAJORANT_SCALE/DELTA
    need(mass == Q(9,5), 'Fourier majorant mass')
    spectral_cap = mass/Q(11,12)
    need(spectral_cap == Q(108,55) and spectral_cap < 2, 'separated spectral cap')
    actual_cap = mass/Q(91,100)
    need(actual_cap == Q(180,91) and actual_cap < 2, 'actual separated spectral cap')
    need(Q(35,88) > Q(1,3), 'close-pair rational margin')
    need(Q(2,27) > A, 'bad-cluster pressure surplus')
    eta = Q(1,100)
    need(Q(2,3)*(Q(1,3)-eta)**2 > A, 'perturbed close-pair cost')
    need(Q(57,5)/3000 == A and 6*Q(1,3000) == B, 'pressure/span constants')
    need(sum((Q(2,7-s)*(7-s) for s in range(1,7)),Q(0)) == 12,
         'seven-window error coefficient')
    return {'polynomial': [str(x) for x in p], 'minimum': str(minimum),
            'derivative_upper': str(derivative_upper),
            'spectral_cap_exact_kernel': str(spectral_cap),
            'spectral_cap_actual_if_aL_ge_91_100': str(actual_cap),
            'cluster_surplus': str(Q(2,27)-A), 'local_overlap_error_multiplier': 24}


def combinatorial_controls() -> dict:
    cluster_cases = 0
    for n in range(1,14):
        for bits in itertools.product((False, True), repeat=n-1):
            # True = a short gap; false = a gap at least 2/3.
            clusters = []
            left = 0
            for i, close in enumerate(bits):
                if not close:
                    clusters.append(list(range(left,i+1))); left = i+1
            clusters.append(list(range(left,n)))
            good, pairs, leftovers = [], [], []
            for block in clusters:
                if len(block) == 1:
                    good.extend(block)
                else:
                    pairs.extend(zip(block[::2], block[1::2]))
                    if len(block)%2:
                        leftovers.append(block[-1])
            bad = n-len(good)
            flat = good+leftovers+[i for pair in pairs for i in pair]
            need(sorted(flat) == list(range(n)), 'cluster partition loses/duplicates points')
            need(3*len(pairs) >= bad, 'pair budget')
            for i,j in pairs:
                need(j == i+1 and bits[i], 'pair crosses a long gap')
            for i,j in zip(good,good[1:]):
                need(any(not close for close in bits[i:j]), 'good set not separated')
            cluster_cases += 1
    window_cases = 0
    for n in range(7,81):
        pair_cost, gap_cost = {}, [Q(0)]*(n-1)
        for start in range(n-6):
            for gap in range(start,start+6):
                gap_cost[gap] += Q(1,3000)
            for s in range(1,7):
                for i in range(start,start+7-s):
                    pair_cost[i,i+s] = pair_cost.get((i,i+s),Q(0))+Q(2,7-s)
        need(all(x <= 2 for x in pair_cost.values()), 'pair overcount')
        need(all(x <= B for x in gap_cost), 'gap overcount')
        window_cases += 1
    # All scalar inequalities used in the distinction between simple/other zeros.
    count_cases = 0
    for s1,s2,p in itertools.product(range(8), repeat=3):
        nmin = s1+2*s2+2*p
        ndmin = s1+s2+2*p
        need(3*s1+4*s2+4*p <= 2*nmin+s1, 'simple count adapter')
        need(3*s1+4*s2+4*p <= 2*ndmin+nmin, 'distinct count adapter')
        count_cases += 1
    return {'cluster_gap_patterns': cluster_cases, 'window_sizes': window_cases,
            'multiplicity_count_cases': count_cases}


def build() -> dict:
    return {'packet': 'SEP26', 'status': 'PROPOSED_ANALYTIC_IMPROVEMENT',
            'rh_proved': False, 'analytic_review_required': True,
            'prime_side_theorem_reproved_by_code': False,
            'bounded_controls': {'majorant': majorant_controls(),
                                 'combinatorics': combinatorial_controls()},
            'constant_enclosures': constants()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', type=Path, default=ROOT/'result.json')
    ap.add_argument('--emit', type=Path, help='write reconstructed bounded result')
    ap.add_argument('--seven-receipt', type=Path, default=ROOT/'seven_result.json')
    ap.add_argument('--full-seven', type=Path,
                    help='run unchanged exhaustive seven-point verifier into this output')
    args = ap.parse_args()
    check_vendor()
    result = build()
    if args.emit:
        args.emit.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    else:
        need(canonical(strict_load(args.check)) == canonical(result), 'bounded receipt mismatch')
    if args.full_seven:
        script = ROOT/'vendor'/'seven_independent_cached.py'
        flags = ['-S','-B'] + (['-O'] if sys.flags.optimize else [])
        subprocess.run([sys.executable,*flags,str(script),str(args.full_seven)],check=True)
        check_seven(args.full_seven)
        scope = 'FULL_SEVEN_EXHAUSTION_AND_BOUNDED_CONTROLS'
    else:
        check_seven(args.seven_receipt)
        scope = 'BOUNDED_CONTROLS_AND_SEVEN_RECEIPT_ONLY'
    print(json.dumps({'verdict':'PASS','scope':scope,
          'bounded_semantic_sha256':hashlib.sha256(canonical(result).encode()).hexdigest()},sort_keys=True))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, TypeError, KeyError, subprocess.CalledProcessError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        raise SystemExit(1)
