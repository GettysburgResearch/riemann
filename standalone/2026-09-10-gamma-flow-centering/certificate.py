"""Complete defining-integral root certificates, not a xi-zero computation.
The analytic Cauchy, branch, full-tail and Rouche contracts are proved in PROOF.md.
"""
from fractions import Fraction as Q
from math import factorial, floor
from pathlib import Path
import json, time
from interval import I, C, PI, S, BITS, exp_series, sqrt_series, mul, cm_sincos

def rows(rates):
    out = []
    for a in rates:
        B = Q(1)
        s = Q(0)
        for b in rates:
            if b == a:
                continue
            B *= (b / (b - a)) ** 2
            s += 1 / (b - a)
        out.append((a, a * a * B, -2 * s))
    return out

def verify_analytic(rates):
    if not 2 <= len(rates) <= 4 or len(set(rates)) != len(rates):
        raise ValueError('rate count or collision')
    tilt = Q(1)
    for a in rates[1:]:
        tilt *= (a / (a - 1)) ** 2
    if tilt > 4:
        raise ValueError('complete exponential tilt')
    r = rows(rates)
    a0, b0, c0 = r[0]
    if a0 != 1:
        raise ValueError('first rate')
    ratio = sum((b / b0 * (2 + abs(c) / Q(29, 10)) / (1 - abs(c0) / Q(29, 10)) * Q(1, 2 ** floor((a - 1) * Q(29, 10))) for a, b, c in r[1:]), Q(0))
    if not ratio < Q(1, 2):
        raise ValueError('dominance')
    if not max(rates) <= 16 or not min(rates[1:]) >= 4:
        raise ValueError('rate sector')
    if not Q(31, 10) * Q(15, 16) * Q(511, 512) > Q(29, 10):
        raise ValueError('Re x')
    normal = Q(1)
    for a in rates:
        normal *= a * a
    normal /= factorial(2 * len(rates) - 1)
    if not normal * 4 ** (2 * len(rates) - 1) < 2 ** 21:
        raise ValueError('Cauchy envelope')
    return {'dominance_ratio': [ratio.numerator, ratio.denominator], 'simplex_constant': [normal.numerator, normal.denominator]}

def h_series(t, rs, d):
    xp = PI * (2 * t).exp()
    yp = PI * (-2 * t).exp()

    def fs(v, sgn):
        x = [v]
        for k in range(1, d + 1):
            x.append(x[-1] * (2 * sgn) / k)
        out = [I(0) for _ in range(d + 1)]
        for a, b, c in rs:
            exponent = [-a * u for u in x]
            e = exp_series(exponent, d)
            p = x.copy()
            p[0] = p[0] + c
            val = mul(p, e, d)
            out = [out[k] + b * val[k] for k in range(d + 1)]
        return out
    f = fs(xp, 1)
    g = fs(yp, -1)
    return sqrt_series(mul(f, g, d), d)

def trig_series(z, t, d):
    sn, cs = cm_sincos(z * C(t))
    ss = [sn, -z * cs]
    cc = [cs, -z * sn]
    ss[1] = z * cs
    z2 = z * z
    for k in range(d - 1):
        ss.append(-z2 * ss[k] / ((k + 1) * (k + 2)))
        cc.append(-z2 * cc[k] / ((k + 1) * (k + 2)))
    return (ss, cc)

def integrate(rates, z, degree=40, cells=256):
    rs = rows(rates)
    acc = [C(0), C(0), C(0)]
    delta = Q(1, cells)
    for j in range(cells):
        t = I(Q(2 * j + 1, cells))
        h = h_series(t, rs, degree)
        ss, cc = trig_series(z, t, degree)
        hc = [sum((C(h[k]) * cc[n - k] for k in range(n + 1)), C(0)) for n in range(degree + 1)]
        hs = [sum((C(h[k]) * ss[n - k] for k in range(n + 1)), C(0)) for n in range(degree + 1)]
        for n in range(0, degree + 1, 2):
            w = Q(2) * delta ** (n + 1) / (n + 1)
            acc[0] = acc[0] + hc[n] * w
            acc[1] = acc[1] - (hs[n] * C(t) + (hs[n - 1] if n >= 1 else C(0))) * w
            acc[2] = acc[2] - (hc[n] * C(t * t) + (2 * C(t) * hc[n - 1] if n >= 1 else C(0)) + (hc[n - 2] if n >= 2 else C(0))) * w
    q = Q(32, cells)
    err = 2 * 2 ** 36 * q ** (degree + 1) / (1 - q)
    tail = tail_bound()
    return ([x.widen(err + tail) for x in acc], err, tail)

def tail_bound():
    v = I(4).exp()
    a = PI / 2
    b = 2 * PI * (v * v / a + 2 * v / (a * a) + 2 / (a * a * a)) * (-a * v).exp()
    return Q(b.hi, S)

def run_one(name, rates, re, im):
    source = verify_analytic(rates)
    if not abs(Q(re)) < 29 or not abs(Q(im)) < 3:
        raise ValueError('Cauchy frequency bounds')
    z = C(Q(re), Q(im))
    vals, err, tail = integrate(rates, z)
    I0, I1, I2 = vals
    R = Q(1, 10 ** 6)
    res = Q(I0.r.absmax() + I0.i.absmax(), S)
    slope = max(Q(max(0, -I1.r.hi, I1.r.lo), S), Q(max(0, -I1.i.hi, I1.i.lo), S))
    curve = Q(I2.r.absmax() + I2.i.absmax(), S)
    lhs = res + curve * R * R / 2 + R ** 3 / 6
    rhs = slope * R
    if not abs(Q(im)) + R < 3:
        raise ValueError('strip for third derivative')
    if not lhs < rhs:
        raise ValueError('Rouche inequality fails')

    def frac(q):
        return [str(q.numerator), str(q.denominator)]
    return {'name': name, 'rates': [frac(r) for r in rates], 'center': [re, im], 'radius': frac(R), 'analytic': source, 'bits': BITS, 'degree': 40, 'cells': 256, 'integral_jets': [v.pair() for v in vals], 'quadrature_error': frac(err), 'tail_error': frac(tail), 'rouche_lhs': frac(lhs), 'rouche_rhs': frac(rhs), 'exactly_one_zero': True, 'rh_proved': False}

def build_result():
    targets = [('N4', [Q(1), Q(4), Q(9), Q(16)], '28.0555855384091825810295021076097455522309', '2.6219979332686197954925378014004831147962'), ('FLOW_u_7_over_10', [Q(1), Q(4), Q(90, 7)], '26.8135855368140614010181412691765400069731', '0.4209949404628029929584207065487732398251')]
    out = [run_one(*args) for args in targets]
    radius = Q(1, 10 ** 6)
    if not Q(out[1]['center'][1]) - radius > 0 or not Q(out[1]['center'][1]) + radius < Q(1, 2):
        raise ValueError('critical strip not proved')
    return {'schema': 'GFC26-v1', 'status': 'PROPOSED_COMPONENTS_WITH_TWO_ROOT_CERTIFICATES', 'rh_proved': False, 'actual_zeta_zero_certified': False, 'all_order_confinement_proved': False, 'arithmetic': 'outward_integer_dyadics_512_bits', 'zero_certificates': out}
