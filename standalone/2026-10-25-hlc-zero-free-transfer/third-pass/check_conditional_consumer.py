#!/usr/bin/env python3
"""Exact certificate for CONDITIONAL_CONSUMER.md.

All acceptance uses fractions and Bernstein coefficients. No sampled
optimization, floating-point tolerance, network, or third-party package is
used. The new coherent-tail moment is an OPEN HYPOTHESIS, not tested here.
"""

from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# Sparse two-variable polynomials over Q, variables (delta,x).
def clean(p):
    return {ij: F(v) for ij, v in p.items() if v}


def add(*ps):
    out = {}
    for p in ps:
        for ij, v in p.items():
            out[ij] = out.get(ij, F(0)) + v
    return clean(out)


def scale(p, c):
    return clean({ij: v * c for ij, v in p.items()})


def mul(p, q):
    out = {}
    for (i, j), v in p.items():
        for (k, l), w in q.items():
            out[i+k, j+l] = out.get((i+k, j+l), F(0)) + v*w
    return clean(out)


def derivative(p, variable):
    out = {}
    for ij, v in p.items():
        if ij[variable]:
            new = list(ij)
            new[variable] -= 1
            out[tuple(new)] = ij[variable] * v
    return clean(out)


def evaluate(p, d, x):
    return sum(v*d**i*x**j for (i, j), v in p.items())


def local_power_coefficients(p, a, b, c, d):
    """Substitute delta=a+(b-a)t, x=c+(d-c)u exactly."""
    out = {}
    for (i, j), v in p.items():
        for k in range(i+1):
            for l in range(j+1):
                term = (v * comb(i, k) * a**(i-k) * (b-a)**k
                        * comb(j, l) * c**(j-l) * (d-c)**l)
                out[k, l] = out.get((k, l), F(0)) + term
    return clean(out)


def bernstein_coefficients(p, a, b, c, d):
    """Return the full tensor Bernstein array on the specified box."""
    require(a <= b and c <= d, 'Reversed polynomial box')
    pp = local_power_coefficients(p, a, b, c, d)
    n = max((i for i, j in pp), default=0)
    m = max((j for i, j in pp), default=0)
    out = []
    for i in range(n+1):
        for j in range(m+1):
            value = sum(
                v * F(comb(i, k), comb(n, k))
                * F(comb(j, l), comb(m, l))
                for (k, l), v in pp.items() if k <= i and l <= j
            )
            out.append(value)
    return out


one = {(0, 0): F(1)}
delta = {(1, 0): F(1)}
xpoly = {(0, 1): F(1)}
alpha = F(5, 6)
boundary = F(8748856, 10**7)
ell = 4 * (F(11, 12) - boundary)
b = F(43267, 500000)
h = (1+b+3*ell)/2
ly = (1+b-ell)/2
lx = (1-b-ell)/2
K = ell + (-1-b+5*ell)/18  # worst endpoint kappa=3/4
C0 = -F(1, 4)+b/6+5*ell/4
eta = F(1, 1000)
r_left = F(29, 25)
r_right = F(117, 100)
margin = F(1, 10**6)
zeta = F(1, 10**9)
cutoffs = [F(581, 500), F(291, 250), F(583, 500), F(146, 125)]

require(ell == F(156679, 937500), 'Wrong boundary/length relation')
require(h == F(3969767, 5000000), 'Wrong h')
require(ly == F(6895573, 15000000), 'Wrong l_y')
require(K == F(20679931, 135000000), 'Wrong amplitude coefficient')
require(C0 == -F(80017, 3000000), 'Wrong constant coefficient')
require(all(r_left < t < r_right for t in cutoffs), 'Cutoff outside hypothesis')

Apoly = add(scale(one, alpha), scale(delta, -1))
Dpoly = add(scale(one, 3), scale(xpoly, -F(17, 9)))
Ppoly = mul(add(scale(one, 2), scale(xpoly, -F(8, 9))),
            add(one, scale(xpoly, -1)))
Jpoly = add(mul(Apoly, Dpoly), mul(delta, Ppoly))

denominator_min = min(bernstein_coefficients(
    Jpoly, F(1, 8), F(5, 6), F(0), F(1, 2)))
require(denominator_min > 0, 'Count denominator not positive')

# Verify the elementary f=P/D inequalities used in monotonicity.
fp_numerator = add(mul(derivative(Ppoly, 1), Dpoly),
                   scale(mul(Ppoly, derivative(Dpoly, 1)), -1))
f_tests = {
    'P>=7/9': add(Ppoly, scale(one, -F(7, 9))),
    'f>=14/37': add(Ppoly, scale(Dpoly, -F(14, 37))),
    'f_prime<=0': scale(fp_numerator, -1),
    '-f_prime<=2/3': add(scale(mul(Dpoly, Dpoly), F(2, 3)), fp_numerator),
}
f_margins = {}
for name, p in f_tests.items():
    value = min(bernstein_coefficients(p, F(0), F(0), F(0), F(1, 2)))
    require(value >= 0, 'Failed f inequality: '+name)
    f_margins[name] = value

old_monotonic = K - h/4*F(37, 43)**2
new_monotonic = K - F(17, 100)*h
require(old_monotonic > 0 and new_monotonic > 0 and K > 0,
        'Endpoint monotonicity margin failed')

# base=E(1-delta)+margin; use the actual algebraic denominators.
base = add(scale(one, C0+margin),
           scale(delta, F(1, 2)-F(3, 4)*h),
           scale(mul(delta, xpoly), K))
old_polynomial = add(scale(mul(Jpoly, base), -2),
                     scale(mul(mul(Apoly, delta), Ppoly), -F(3, 4)*h))


def long_polynomial(t, saving):
    row_count = add(scale(one, F(1, 6)-saving), scale(Apoly, t))
    endpoint = add(scale(one, C0+margin-F(3, 4)*h),
                   scale(delta, F(1, 2)),
                   scale(mul(delta, xpoly), K),
                   scale(row_count, F(3, 4)*h))
    return scale(endpoint, -1)


floor_polynomial = long_polynomial(r_left, F(0))
candidate_polynomials = {}
for t in cutoffs:
    short = add(scale(mul(Dpoly, base), -1),
                scale(mul(delta, Ppoly), -F(3, 4)*h*(F(3, 2)-t)))
    candidate_polynomials[t] = [short, long_polynomial(t, eta), floor_polynomial]

small_coefficients = bernstein_coefficients(
    old_polynomial, F(1, 8), F(1, 4), F(0), F(1, 2))
require(min(small_coefficients) > 0, 'Small rectangle is not certified')

# Six fixed intervals form an exact cover; these are not sample points.
intervals = [
    (F(1, 4), F(473, 1024), 'old'),
    (F(473, 1024), F(953, 2048), cutoffs[0]),
    (F(953, 2048), F(15, 32), cutoffs[1]),
    (F(15, 32), F(967, 2048), cutoffs[2]),
    (F(967, 2048), F(487, 1024), cutoffs[3]),
    (F(487, 1024), F(5, 6), 'old'),
]
require(intervals[0][0] == F(1, 4) and intervals[-1][1] == F(5, 6),
        'Wrong cover endpoints')
for previous, current in zip(intervals, intervals[1:]):
    require(previous[1] == current[0], 'Gap or overlap in interval certificate')

interval_report = []
displayed_lower_bounds = [F(7,10**6), F(2,10**6), F(6,10**5),
                          F(7,10**5), F(4,10**5), F(5,10**7)]
for (lo, hi, method), displayed in zip(intervals, displayed_lower_bounds):
    require(lo < hi, 'Empty certificate interval')
    polys = [old_polynomial] if method == 'old' else candidate_polynomials[method]
    arrays = [bernstein_coefficients(p, lo, hi, F(1, 2), F(1, 2)) for p in polys]
    require(all(min(a) > 0 for a in arrays), 'Failed interval: '+str((lo, hi, method)))
    require(all(min(a) > displayed for a in arrays), 'Displayed coefficient floor failed')
    interval_report.append({
        'delta_interval': [str(lo), str(hi)],
        'method': str(method),
        'polynomial_order': ['old'] if method == 'old' else ['short', 'improved_long', 'old_floor'],
        'bernstein_coefficients': [[str(v) for v in a] for a in arrays],
    })

# Actual finite prime supply and all extra scalar gates in Remark 14.1.
kmin, kmax = F(7497, 10000), F(3, 4)
Asm = F(1, 2)+ell/2*(F(1, 2)+2*ell/h)-h/2
side_margins = {
    'b>0': b,
    'ell>1/6': ell-F(1, 6),
    'ell<1/5': F(1, 5)-ell,
    'B>437/500': boundary-F(437, 500),
    'lx>ell': lx-ell,
    'ly-ell>11b/6': ly-ell-F(11, 6)*b,
    '6kappa ell>3/4': 6*kmin*ell-F(3, 4),
    'ell/h<1/(6kappa)': 1/(6*kmax)-ell/h,
    'ell/(h+zeta)>21/100': ell/(h+zeta)-F(21, 100),
    'h/2<ly': ly-h/2,
    'ly<1/2': F(1, 2)-ly,
    'small-delta endpoint margin over 1/250': -F(1, 250)-max(C0, C0+Asm/8),
    'floor endpoint margin over 1/100': -F(1, 100)-(C0+(F(1, 2)+F(3, 2)*ell)/50),
    'small-row margin over 1/20': -F(1, 20)-(F(13, 75)*h-ly/2+F(1, 50)),
    '2zeta<margin/2': margin/2-2*zeta,
    'maximal numerator capacity': F(21, 100)*(6*kmin-F(1, 8))-(1-F(2, 3)*F(1, 8)),
}
for name, value in side_margins.items():
    require(value > 0, 'Source side condition failed: '+name)
require(side_margins['maximal numerator capacity'] == F(1279, 750000),
        'Wrong explicit capacity margin')

# Smooth-HB head exponent gamma0=83/24-sqrt(195)/6.
# e0(r_left)=17/15. Compare to eta without a floating-point square root.
radical_threshold = 6*(F(83,24)-F(17,15)+eta)
require(radical_threshold == F(3489,250) and radical_threshold > 0,
        'Wrong radical threshold for the smooth head')
radical_margin = F(195)-radical_threshold**2
require(radical_margin == F(14379,62500) and radical_margin > 0,
        'Smooth-HB head does not beat the required full-inverse exponent')

# Isolate the source's fixed input algebraic root and certify the improvement.
quartic = {(i, 0): F(v) for i, v in enumerate([-275, 1290, 9936, -27405, 16686])}
klo, khi = F(749773294079928, 10**15), F(749773294079929, 10**15)
require(evaluate(quartic, klo, F(0)) > 0 > evaluate(quartic, khi, F(0)),
        'Quartic sign bracket failed')
require(max(bernstein_coefficients(derivative(quartic, 0), klo, khi, F(0), F(0))) < 0,
        'Quartic root isolation failed')
require(kmin < klo < khi < kmax, 'Moment interval does not include kappa_flat')
improvement_lower = (1+klo)/2-boundary
require(improvement_lower > F(1, 10**6), 'Conditional improvement is not greater than 10^-6')

# Negative control: with eta=0, every trial cutoff count is at least the old
# crossing count. The old endpoint is strictly positive at this exact class.
d0, x0 = F(469345, 10**6), F(1, 2)
dd, pp = evaluate(Dpoly, d0, x0), evaluate(Ppoly, d0, x0)
aa, cc = alpha-d0, d0*pp/dd
rr = 1-d0+aa*cc/(2*(aa+cc))
old_endpoint = C0+d0/2+d0*x0*K-F(3, 4)*h*(1-rr)
require(old_endpoint > 0, 'Negative control lost its adverse old class')
for t in cutoffs:
    without_gain = max(1-d0+cc*(F(3, 2)-t), F(1, 6)+aa*t, F(1, 6)+aa*r_left)
    require(without_gain >= rr, 'Zero-gain negative control unexpectedly improved count')

report = {
    'status': 'PASS',
    'scope': 'Conditional consumer only; the coherent-tail moment is OPEN',
    'boundary': str(boundary),
    'boundary_decimal': float(boundary),
    'input_tail_saving': str(eta),
    'input_tail_outer_product_cutoff': 'U^(13/20)',
    'input_tail_decomposition': 'smooth two-factor Heath-Brown, same fixed cutoff w_0',
    'proved_short_component_exponent': '83/24-sqrt(195)/6',
    'short_component_radical_comparison_margin': str(radical_margin),
    'input_inverse_length_interval': [str(r_left), str(r_right)],
    'proved_endpoint_margin': str(margin),
    'geometry': {name: str(value) for name, value in
                 [('b', b), ('ell', ell), ('lx', lx), ('ly', ly), ('h', h), ('K', K), ('C0', C0), ('zeta', zeta)]},
    'denominator_Bernstein_lower_bound': str(denominator_min),
    'f_inequality_Bernstein_margins': {k: str(v) for k, v in f_margins.items()},
    'old_x_monotonicity_margin': str(old_monotonic),
    'new_x_monotonicity_margin': str(new_monotonic),
    'small_rectangle_Bernstein_coefficients': [str(v) for v in small_coefficients],
    'six_interval_certificate': interval_report,
    'source_side_margins': {k: str(v) for k, v in side_margins.items()},
    'kappa_flat_interval': [str(klo), str(khi)],
    'improvement_over_B_flat_lower_bound': str(improvement_lower),
    'zero_gain_negative_control_endpoint': str(old_endpoint),
    'warning': 'No new tail estimate, imported analytic theorem, or unconditional zero-free region is verified.'
}
Path(__file__).with_name('CONDITIONAL_CONSUMER_CHECKS.json').write_text(
    json.dumps(report, indent=2)+'\n')
print(json.dumps({k: report[k] for k in
                  ['status', 'scope', 'boundary', 'proved_endpoint_margin',
                   'improvement_over_B_flat_lower_bound']}, indent=2))
