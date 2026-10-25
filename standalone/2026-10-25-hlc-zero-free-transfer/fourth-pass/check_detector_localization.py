#!/usr/bin/env python3
"""Exact finite algebra and endpoint coverage for DETECTOR_LOCALIZATION.md.

This is not an analytic proof of the imported estimates or the open
residual spike-count hypothesis. Every predicate survives python -O.
The divisor examples use the free prime monoid of positive integers;
they test algebra valid for ideal factorization, not Hecke mean values.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd
from pathlib import Path
import hashlib
import json


def require(test, message):
    if not test:
        raise RuntimeError(message)


@lru_cache(None)
def divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


@lru_cache(None)
def mobius(n):
    out = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            out = -out
            if n % d == 0:
                return 0
            while n % d == 0:
                n //= d
        d += 1
    return -out if n > 1 else out


def cut(x):
    """Rational surrogate with the exact support and partition properties."""
    return F(1) if x <= 1 else F(0) if x >= 2 else 2 - x


def coefficient(n, y1, y2):
    return sum(F(mobius(d) * mobius(n // d))
               * cut(F(d) / y1) * cut(F(n // d) / y2)
               for d in divisors(n))


def psi(n, puncture, signs):
    if gcd(n, puncture) != 1:
        return 0
    out = 1
    d = 2
    while d * d <= n:
        while n % d == 0:
            out *= signs.get(d, 1)
            n //= d
        d += 1
    if n > 1:
        out *= signs.get(n, 1)
    return out


counts = {'coefficient_returns': 0, 'coherent_primal_returns': 0,
          'selector_partitions': 0, 'support_implications': 0,
          'far_envelopes': 0, 'marked_corners': 0,
          'thin_band_partitions': 0, 'thin_band_returns': 0,
          'thin_label_supports': 0, 'thin_box_corners': 0}

# No smoothness conclusion is drawn from the piecewise-linear surrogate.
# The finite support keeps the full A through 4*y1*y2, including terms
# beyond the primal annulus that can survive a selected reflection.
for y1, y2 in [(F(2), F(3)), (F(3), F(5)), (F(5, 2), F(7, 2))]:
    limit = int(4 * y1 * y2)
    aa = {n: coefficient(n, y1, y2) for n in range(1, limit + 1)}
    for puncture in [1, 2, 3, 6, 10]:
        cc = {m: sum(aa[m*d] / d for d in range(1, limit//m + 1)
                     if gcd(d, puncture) == 1)
              for m in range(1, limit + 1)}
        for bscale, kscale in [(F(5), F(5, 8)), (F(12), F(3, 2)),
                               (F(20), F(5, 2))]:
            components = []
            for m in range(1, limit + 1):
                terms = [F(0), F(0), F(0)]
                for k in range(1, limit//m + 1):
                    if gcd(k, puncture) != 1:
                        continue
                    hh = cut(F(k*m) / bscale)
                    ss = (1-hh) * cut(F(k) / kscale)
                    rr = (1-hh) * (1-cut(F(k) / kscale))
                    require(hh + ss + rr == 1, 'Selector partition lost')
                    counts['selector_partitions'] += 1
                    weight = F(mobius(k), k) * cc[k*m]
                    for j, selector in enumerate([hh, ss, rr]):
                        terms[j] += weight * selector
                    if ss:
                        # Here kscale=bscale/(4*row_threshold).
                        row_threshold = bscale / (4*kscale)
                        require(m > 2*row_threshold,
                                'Small-divisor support did not force long return')
                        counts['support_implications'] += 1
                    if rr:
                        require(k > kscale and k*m > bscale,
                                'Large-divisor support lost')
                require(sum(terms) == aa[m], 'Full signed divisor return failed')
                components.append(terms)
                counts['coefficient_returns'] += 1
                for low_scale, high_scale in [(F(2),F(4)), (F(5,2),F(9,2))]:
                    low = cut(F(m)/low_scale)
                    high = 1-cut(F(m)/high_scale)
                    middle = cut(F(m)/high_scale)-low
                    require(low+high+middle == 1,
                            'Original-product band partition failed')
                    require(aa[m]*(low+high+middle) == aa[m],
                            'Primal signed band identity failed')
                    counts['thin_band_partitions'] += 1
                    if middle:
                        require(low_scale < m < 2*high_scale,
                                'Thin original-product support failed')
                    require(aa[m]*middle == terms[0]*middle
                            +(terms[1]+terms[2])*middle,
                            'Ratio head and high ratio do not return primal band')
                    counts['thin_band_returns'] += 1
            for signs in [{2: -1, 3: 1, 5: -1}, {2: 1, 3: -1, 7: -1}]:
                # The common product weight is exact rational and finite;
                # sqrt(D) is omitted on both sides of the equality.
                dscale = int(2*y1*y2)
                direct = F(0)
                separated = [F(0), F(0), F(0)]
                for m in range(1, limit + 1):
                    for c in range(1, 2*dscale//m + 1):
                        x = F(m*c, dscale)
                        vv = (x-1)*(2-x) if 1 < x < 2 else F(0)
                        vv *= psi(m*c, puncture, signs)
                        direct += aa[m] * vv
                        for j in range(3):
                            separated[j] += components[m-1][j] * vv
                require(sum(separated) == direct, 'Coherent primal return failed')
                counts['coherent_primal_returns'] += 1

alpha, eta, kappa = F(2,125), F(1,1000), F(1,100)
r0, r1 = F(29,25), F(117,100)
require(r0-1-kappa == F(3,20) and r1-1-kappa == F(4,25),
        'Wrong large-divisor localization exponents')
require(kappa/8 == F(1,800), 'Wrong pointwise head saving')
require(F(1,750)-eta == F(1,3000), 'Wrong unmarked reserve')

# Exact continuous far-envelope proof: on each affine branch the maximum
# over its b interval occurs at an endpoint. A dense rational replay is an
# additional regression check, not a substitute for those affine facts.
for j in range(101):
    r = r0 + (r1-r0)*j/100
    bpoints = [1-alpha, F(1), r-alpha]
    for b in bpoints:
        e = max(F(1), (1+5*b)/6)
        require((1+5*r)/6 - (e+F(3,4)*(r-b)) >= F(1,750),
                'Far envelope lost its guaranteed saving')
        counts['far_envelopes'] += 1

# Authenticate the existing source certificate before reusing its exact
# polynomial routines. Exclude its report-writing block to preserve all
# third-pass bytes. This replays its acceptance checks, not derived JSON.
source = Path(__file__).parents[1] / 'third-pass/check_conditional_consumer.py'
expected_sha = 'c611bedacf374e4ee58f19d2f52e09e07e8933d092f20947be1a01cc10d2349f'
raw = source.read_bytes()
require(hashlib.sha256(raw).hexdigest() == expected_sha,
        'Pinned conditional-consumer source changed')
text_source = raw.decode('utf-8')
require(text_source.count('\nreport = {') == 1,
        'Unexpected certificate report boundary')
namespace = {'__file__': str(source), '__name__': 'pinned_conditional_certificate'}
exec(compile(text_source[:text_source.index('\nreport = {')], str(source), 'exec'),
     namespace)

bernstein = namespace['bernstein_coefficients']
old_poly = namespace['old_polynomial']
old_cells = []
lo, hi = F(1,4), F(5,6)
for j in range(128):
    left, right = lo + (hi-lo)*j/128, lo + (hi-lo)*(j+1)/128
    coeffs = bernstein(old_poly, left, right, F(49,100), F(49,100))
    require(min(coeffs) > 0, 'Old consumer fails below the retained amplitude box')
    old_cells.append({'delta': [str(left), str(right)],
                      'bernstein': [str(x) for x in coeffs]})
old_margin = min(F(x) for cell in old_cells for x in cell['bernstein'])
require(old_margin == F(799945092153101,1119744000000000000),
        'Old-amplitude box certificate changed')

# The marked component proof uses the source's finite-slot selection,
# not just these scalar inequalities. Here certify the stated box margins.
sigma = F(79,100)
delta0, delta1, x0, x1 = F(473,1024), F(487,1024), F(49,100), F(1,2)
marked = []
for delta, x, r in product([delta0,delta1], [x0,x1], [r0,r1]):
    g = delta*x
    short_gap = (-F(5,6)+(F(5,6)-delta)*r + g
                 +(delta-g)*(sigma-alpha))
    long_gap = alpha*(F(5,6)-delta)
    require(short_gap > eta and long_gap > eta, 'Marked box gap failed')
    marked.append((short_gap,long_gap))
    counts['marked_corners'] += 1
require(min(x[0] for x in marked) == F(372257,153600000),
        'Incorrect marked short-end minimum')
require(min(x[1] for x in marked) == F(1099,192000),
        'Incorrect marked long-end minimum')
require((1-sigma+alpha)/2 == F(113,1000), 'Wrong maximal prime capacity')
require(sigma-alpha > F(1,2), 'Second marked constraint loses its strict margin')
require(r0-kappa-sigma == F(9,25) and r1-kappa-sigma == F(37,100),
        'Wrong stronger localized divisor exponents')

# The box-gap expression is multilinear in r,delta,x; corner testing is
# therefore an exact continuous certificate. These derivative signs also
# identify the unique worst corner without relying on a numerical grid.
require(F(5,6)-delta1 > 0, 'Wrong r monotonicity')
require(delta0*(1-sigma+alpha) > 0, 'Wrong x monotonicity')
require(-r0+x1+(1-x1)*(sigma-alpha) < 0, 'Wrong delta monotonicity')

# A separate, smaller asymmetric cutoff leaves all earlier certificates
# unchanged. These are continuous multilinear box certificates, not just
# approximate evaluations of the old critical point.
alpha_star, low, high = F(1,250), F(147,200), F(773,1000)
thin_gaps = []
for delta, x, r in product([delta0,delta1], [x0,x1], [r0,r1]):
    g = delta*x
    old_count = (1+5*r)/6-delta*r
    high_short = 1-g-(delta-g)*(high-alpha_star)
    high_long = F(1,6)+(F(5,6)-delta)*(r-alpha_star)
    c = r-low
    low_count = 1-2*delta*c-F(4,9)*g*(1-2*c)
    gaps = (old_count-low_count, old_count-high_short, old_count-high_long)
    require(min(gaps) > eta, 'Thin-band complement fails target saving')
    thin_gaps.append(gaps)
    counts['thin_box_corners'] += 1
thin_minima = tuple(min(v[j] for v in thin_gaps) for j in range(3))
require(thin_minima == (F(23,16000),F(371959,307200000),F(1099,768000)),
        'Thin-band exact reserves changed')
require(high-alpha_star == F(769,1000), 'Wrong thin high inverse length')
require((1-high+alpha_star)/2 == F(231,2000),
        'Wrong high prime capacity')
require(2*(1-2*(r0-low))/9 == F(1,30),
        'Wrong low prime capacity')
require(r0-high == F(387,1000) and r1-low == F(87,200),
        'Wrong ordinary-factor length interval')
require(r0-kappa-high == F(377,1000) and r1-low == F(87,200),
        'Wrong linked large-divisor range')
require(-r0+x1+(1-x1)*(high-alpha_star) < 0,
        'Wrong high-gap delta derivative')
require(r1-2*low+F(4,9)*x1*(1-2*r1+2*low) < 0,
        'Wrong low-gap delta derivative')
require(1-2*r1+2*low > 0 and 1-F(8,9)*x1 > 0,
        'Wrong low-gap x/r derivatives')

# Exact support implications use abstract rational scales, retaining the
# factors two and eight. No discretization of nonintegral powers is used.
for dscale, bscale, low_scale, high_scale in [
        (F(20),F(12),F(3),F(5)),
        (F(30),F(20),F(5),F(8)),
        (F(40),F(32),F(5,2),F(9,2))]:
    for m in range(1,int(2*high_scale)+1):
        mid = cut(F(m)/high_scale)-cut(F(m)/low_scale)
        if not mid:
            continue
        for k in range(1,int(8*dscale/m)+1):
            high_ratio = 1-cut(F(k*m)/bscale)
            if not high_ratio:
                continue
            for d in range(1,int(8*dscale/(k*m))+1):
                if k*m*d >= 8*dscale:
                    continue
                require(low_scale < m < 2*high_scale,
                        'Returned interval lost in expanded coefficient')
                require(bscale < k*m < 8*dscale,
                        'Near-full coefficient support failed')
                require(bscale/(2*high_scale) < k < 8*dscale/low_scale,
                        'Linked large-divisor support failed')
                require(d < 8*dscale/bscale,
                        'Short auxiliary divisor support failed')
                counts['thin_label_supports'] += 1

# Adversarial controls: a high ratio does not force a high returned m;
# omitting the signed divisor inversion does not reconstruct A.
require(3 < 10 and 7*3 > 10 and 7 > 2,
        'False-support control malformed')
fake_A = {1:F(1), 2:F(-1)}
fake_C = {1:F(1,2), 2:F(-1)}
require(fake_C[1] + fake_C[2]/2 != fake_A[1],
        'Unsigned-inversion mutation was not rejected')
require(not (min(x[0] for x in marked) > F(1,200)),
        'Oversized-saving mutation was not rejected')

report = {
    'status': 'PASS',
    'scope': 'Finite algebra and conditional endpoint coverage; residual estimates OPEN',
    'counts': counts,
    'pinned_consumer_sha256': expected_sha,
    'old_x_at_most_49_over_100_certificate': old_cells,
    'old_box_minimum_Bernstein_coefficient': str(old_margin),
    'marked_short_gap': '372257/153600000',
    'marked_long_gap': '1099/192000',
    'stronger_residual_k_log_exponents': ['9/25','37/100'],
    'thin_asymmetric_alpha': str(alpha_star),
    'thin_returned_band_log_exponents': [str(low),str(high)],
    'thin_low_high_short_high_long_gaps': [str(x) for x in thin_minima],
    'thin_large_divisor_log_range': ['377/1000','87/200'],
    'thin_auxiliary_divisor_upper_log_exponent': '1/100',
    'open_hypotheses_tested': False,
}
destination = Path(__file__).with_name('DETECTOR_LOCALIZATION_CHECKS.json')
destination.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: report[k] for k in
                 ['status','scope','counts','old_box_minimum_Bernstein_coefficient',
                  'marked_short_gap','marked_long_gap',
                  'thin_low_high_short_high_long_gaps','open_hypotheses_tested']},
                 indent=2))
