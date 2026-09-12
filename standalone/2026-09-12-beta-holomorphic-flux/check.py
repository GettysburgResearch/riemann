#!/usr/bin/env python3
"""Exact finite algebra for BHF26. NOT a checker of RH or of the flux sign.

Python standard library only. No floating-point quantity enters acceptance.
Run: python -I check.py --emit results.json
     python -I check.py --check results.json --self-test
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import json
from math import comb, factorial
from pathlib import Path
import sys


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def fs(x: Q | int) -> str:
    return str(Q(x))


# The exact field Q(sqrt(2),sqrt(3)); entries are 1,sqrt(2),sqrt(3),sqrt(6).
K = tuple[Q, Q, Q, Q]
ZERO: K = (Q(0), Q(0), Q(0), Q(0))
ONE: K = (Q(1), Q(0), Q(0), Q(0))
S2: K = (Q(0), Q(1), Q(0), Q(0))
S3: K = (Q(0), Q(0), Q(1), Q(0))


def add(a: K, b: K) -> K:
    return tuple(x+y for x, y in zip(a, b))  # type: ignore[return-value]


def scale(a: K, b: Q | int) -> K:
    return tuple(x*b for x in a)  # type: ignore[return-value]


def mul(a: K, b: K) -> K:
    out = [Q(0)]*4
    for i in range(4):
        for j in range(4):
            common = i & j
            factor = (2 if common & 1 else 1)*(3 if common & 2 else 1)
            out[i ^ j] += a[i]*b[j]*factor
    return tuple(out)  # type: ignore[return-value]


def kp(a: K, n: int) -> K:
    require(n >= 0, 'negative field power')
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out


def anti(y: K, iy: K) -> K:
    out = scale(kp(iy, 3), -Q(1, 3))
    for term in (scale(iy, -4), scale(y, 6),
                 scale(kp(y, 3), Q(4, 3)), scale(kp(y, 5), Q(1, 5))):
        out = add(out, term)
    return out


def rf(a: Q, n: int) -> Q:
    out = Q(1)
    for j in range(n):
        out *= a+j
    return out


def gamma_half_coefficient(k: int) -> tuple[Q, int]:
    """Gamma(k/2)=rational * sqrt(pi)^parity, for positive integer k."""
    require(k > 0, 'gamma argument')
    if k % 2 == 0:
        return Q(factorial(k//2-1)), 0
    n = (k-1)//2
    return Q(factorial(2*n), 4**n*factorial(n)), 1


def beta_coefficient(k: int, l: int) -> tuple[Q, int]:
    a, pa = gamma_half_coefficient(k)
    b, pb = gamma_half_coefficient(l)
    c, pc = gamma_half_coefficient(k+l)
    return a*b/c, pa+pb-pc


def scale_moment(theta: Q, j: int) -> Q:
    if j == 0:
        return Q(1)
    beta = rf(Q(5, 2), j)/rf(Q(5), j)
    uniform = (1-Q(1, 2**(2*j-1)))/(2*j-1)
    return (1-theta)*beta+theta*uniform


def moments(theta: Q, order: int) -> list[Q]:
    out = [Q(1), Q(1)]
    for j in range(2, order+1):
        a = scale_moment(theta, j)
        require(1-2*a > 0, 'nonpositive moment denominator')
        out.append(a/(1-2*a)*sum(
            (Q(comb(j, i))*out[i]*out[j-i] for i in range(1, j)), Q(0)))
    return out


def brownian_moments(order: int) -> list[Q]:
    # Independent reciprocal of sinh(sqrt(6t))/sqrt(6t).
    den = [Q(6**j, factorial(2*j+1)) for j in range(order+1)]
    inv = [Q(1)]
    for j in range(1, order+1):
        inv.append(-sum((den[i]*inv[j-i] for i in range(1, j+1)), Q(0)))
    return [Q((-1)**j*factorial(j))*inv[j] for j in range(order+1)]


# Rational polynomials, coefficient order ascending.
def pmul(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def ppow(a: list[Q], n: int) -> list[Q]:
    out = [Q(1)]
    for _ in range(n):
        out = pmul(out, a)
    return out


def pd(a: list[Q], n: int = 1) -> list[Q]:
    for _ in range(n):
        a = [Q(j)*a[j] for j in range(1, len(a))] or [Q(0)]
    return a


def peval(a: list[Q], x: Q) -> Q:
    out = Q(0)
    for v in reversed(a):
        out = out*x+v
    return out


def build() -> dict:
    # Check the antiderivative as an exact Laurent polynomial.
    P = {-3: -Q(1, 3), -1: Q(-4), 1: Q(6), 3: Q(4, 3), 5: Q(1, 5)}
    derivative = {j-1: j*v for j, v in P.items()}
    require(derivative == {-4: Q(1), -2: Q(4), 0: Q(6), 2: Q(4), 4: Q(1)},
            'incorrect continuum antiderivative')
    integral = scale(add(anti(S3, scale(S3, Q(1, 3))),
                         scale(anti(scale(S2, Q(1, 2)), S2), -1)), 2)
    require(integral == (Q(0), Q(157, 60), Q(2816, 135), Q(0)),
            'incorrect exact radical integral')
    q_w = mul(scale(S3, Q(32, 6561)), integral)
    tail = scale(add(ONE, scale(mul(S2, S3), -Q(4, 27))), Q(2, 5))
    q_w = add(q_w, tail)
    require(q_w == (Q(41642, 59049), Q(0), Q(0), -Q(4576, 98415)),
            'uniform-scale norm expression mismatch')
    require(Q(12, 5)**2 < 6, 'sqrt(6) lower bound')
    q_upper = q_w[0]+q_w[3]*Q(12, 5)
    require(q_upper == Q(876314, 1476225) and q_upper < Q(3, 5),
            'uniform contraction inequality')

    beta_high, p1 = beta_coefficient(17, 3)
    beta_base, p2 = beta_coefficient(5, 5)
    require(p1 == p2, 'uncancelled pi in beta ratio')
    beta_ratio = beta_high/beta_base
    a6 = rf(Q(5, 2), 6)/rf(Q(5), 6)
    require(beta_ratio == Q(715, 1536), 'beta quadratic ratio')
    require(32*a6 == Q(143, 64) < 15, 'small-x beta quadratic bound')
    require(32*beta_ratio == Q(715, 48) < 15, 'large-x beta quadratic bound')
    w_max = Q(3, 2)**3/(1+Q(3, 2))**5
    require(w_max == Q(108, 3125) and 16*w_max < 1, 'W quadratic bound')
    require(Q(50, 7) < 8 and 32 < 36, 'forcing bounds')

    delta, radius = Q(1, 4096), Q(1, 128)
    linear = Q(3, 5)+Q(39, 40)*delta
    quadratic = 15+16*delta
    image = 8*delta+linear*radius+quadratic*radius**2
    lip = linear+2*quadratic*radius
    require(image < radius and lip < Q(7, 8), 'complex contraction ball')
    require(20*delta < radius, 'real source lies in complex ball')
    require((2*radius+radius**2)/6 < radius/2, 'normalizer cannot vanish')

    moment_samples = {}
    for theta in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
        m = moments(theta, 12)
        require(m[2] == Q(7, 5), 'second moment')
        require(m[3] == 21*(30+theta)/(5*(50-theta)), 'third moment')
        require(2*m[3]+6*m[2] <= Q(96, 7), 'pair third moment sample')
        moment_samples[fs(theta)] = [fs(v) for v in m]
    require(moments(Q(0), 12) == [rf(Q(5, 2), j)*Q(2, 5)**j for j in range(13)],
            'gamma endpoint independent moment check')
    require(moments(Q(1), 12) == brownian_moments(12),
            'Brownian endpoint independent sinh-series check')

    # h(d)=d^2(1/4-d^2)^2; no boundary delta term in its weak second derivative.
    h = [Q(0), Q(0), Q(1, 16), Q(0), -Q(1, 2), Q(0), Q(1)]
    for edge in (Q(-1, 2), Q(1, 2)):
        require(peval(h, edge) == 0 and peval(pd(h), edge) == 0, 'edge regularity')
    h_of_u = [Q(0), Q(1, 16), -Q(1, 2), Q(1)]
    require(peval(h_of_u, Q(1, 12)) == Q(1, 432), 'weight maximum value')
    h_second_u = [Q(1, 8), Q(-6), Q(30)]
    require(peval(h_second_u, Q(1, 8)) == -Q(5, 32), 'negative Green-kernel point')
    require(peval(h_of_u, Q(1, 8)) == Q(1, 512), 'Green-kernel weight point')
    green_negative = -Q(5, 32)+10*Q(1, 512)
    require(green_negative == -Q(35, 256) < 0, 'signed Green-kernel obstruction')
    require(Q(40, 432) == Q(5, 54), 'whole-height tail coefficient')

    # Persistent repeated root velocity tested by actual polynomial derivatives.
    velocity_cases = 0
    for theta in (Q(0), Q(1, 3), Q(1)):
        root = 2+theta+theta**2
        velocity = 1+2*theta
        base = [-root**2, Q(0), Q(1)]
        for multiplicity in range(1, 9):
            f = ppow(base, multiplicity)
            ftheta = [v*(-2*multiplicity*root*velocity)
                      for v in ppow(base, multiplicity-1)]
            numerator = peval(pd(ftheta, multiplicity-1), root)
            denominator = peval(pd(f, multiplicity), root)
            require(denominator != 0 and -numerator/denominator == velocity,
                    'persistent-multiplicity velocity identity')
            velocity_cases += 1
    # At z=2+v*w, u=v^3, the leading polynomial is 64*w^3-1.
    shifted_cube = ppow([Q(0), Q(4), Q(1)], 3)
    require(shifted_cube[:3] == [0, 0, 0] and shifted_cube[3] == 64,
            'triple-collision Puiseux leading term')

    return {
        'packet': 'BHF26',
        'scope': 'EXACT_FINITE_ALGEBRA_ONLY_NOT_RH_NOT_NATIVE_FLUX_SIGN',
        'uniform_scale_bound': {
            'rational_part': fs(q_w[0]), 'sqrt6_coefficient': fs(q_w[3]),
            'rational_upper': fs(q_upper), 'contractivity_margin': fs(Q(3, 5)-q_upper)},
        'quadratic_bounds': {'beta_small': fs(32*a6), 'beta_large': fs(32*beta_ratio),
                             'uniform': fs(16*w_max)},
        'analytic_ball': {'delta': fs(delta), 'radius': fs(radius),
                          'image_bound': fs(image), 'image_margin': fs(radius-image),
                          'lipschitz_bound': fs(lip), 'lipschitz_margin': fs(Q(7, 8)-lip)},
        'normalizer_difference_bound': fs((2*radius+radius**2)/6),
        'moment_order_checked': 12, 'moment_samples': moment_samples,
        'whole_height_tail_coefficient': '5/54',
        'green_kernel_negative_upper': fs(green_negative),
        'persistent_velocity_cases': velocity_cases,
        'triple_collision_leading_polynomial': '64*w^3-1',
        'native_flux_evaluated': False, 'native_zeros_evaluated': False,
        'analytic_proofs_machine_verified': False,
    }


def validate_record(record: object) -> None:
    expected = build()
    # Canonical typed JSON avoids True==1 and similar permissive comparisons.
    require(json.dumps(record, sort_keys=True, separators=(',', ':')) ==
            json.dumps(expected, sort_keys=True, separators=(',', ':')),
            'record differs from fresh exact reconstruction')


def self_test() -> None:
    expected = build()
    validate_record(expected)
    for label in ('scope', 'analytic_ball', 'native_flux_evaluated', 'moment_samples'):
        changed = copy.deepcopy(expected)
        if label == 'analytic_ball':
            changed[label]['delta'] = '1/2'
        elif label == 'moment_samples':
            changed[label]['1'][3] = '1'
        elif label == 'native_flux_evaluated':
            changed[label] = True
        else:
            changed[label] = 'RH_PROVED'
        try:
            validate_record(changed)
        except ValueError:
            pass
        else:
            raise ValueError('altered record accepted: '+label)
    print('self-test: 4 altered records rejected; finite algebra controls passed')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--emit', type=Path)
    parser.add_argument('--check', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    try:
        result = build()
        if args.emit:
            args.emit.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n', encoding='utf-8')
        if args.check:
            validate_record(json.loads(args.check.read_text(encoding='utf-8')))
        if args.self_test:
            self_test()
        print('PASS: exact finite algebra only; native flux sign remains OPEN')
        return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print('FAIL: '+str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
