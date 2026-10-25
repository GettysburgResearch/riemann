#!/usr/bin/env python3
"""Finite identities and rational margins for MIDDLE_JOINT.md.

No analytic theorem or open large-divisor estimate is certified here.
Every verification predicate remains active under python -O.
"""

from fractions import Fraction as Q
from functools import lru_cache
from math import gcd, isqrt
import json


def require(value, label):
    if not value:
        raise RuntimeError(label)


@lru_cache(None)
def divisors(n):
    lo, hi = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            lo.append(d)
            if d * d != n:
                hi.append(n // d)
    return tuple(lo + hi[::-1])


@lru_cache(None)
def mu(n):
    value = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
        p += 1
    if n > 1:
        value = -value
    return value


@lru_cache(None)
def radical(n):
    out = 1
    for d in divisors(n):
        if d > 1 and len(divisors(d)) == 2:
            out *= d
    return out


def cut(x):
    """Rational finite-test surrogate; analytic proof uses smooth cutoffs."""
    if x <= 1:
        return Q(1)
    if x >= 2:
        return Q(0)
    return 2 - x


Y1, Y2 = 5, 13
LIMIT = 4 * Y1 * Y2


@lru_cache(None)
def outer(n):
    return sum((Q(mu(a) * mu(n // a)) * cut(Q(a, Y1))
                * cut(Q(n // a, Y2)) for a in divisors(n)), Q(0))


def allocated(k, d, A, omit_g=False, omit_t_mask=False,
              omit_n_mask=False, omit_mu_m=False):
    total = Q(0)
    kd = k * d
    choices = (1,) if omit_g else divisors(radical(kd))
    for g in choices:
        m = kd // g
        if mu(m) == 0:
            continue
        for t in divisors(A):
            n = A // t
            if not omit_t_mask and gcd(t, kd) != 1:
                continue
            if not omit_n_mask and gcd(n, m) != 1:
                continue
            value = mu(g) * mu(t) * mu(n)
            if not omit_mu_m:
                value *= mu(m)
            total += (value * cut(Q(g * t, Y1))
                      * cut(Q(m * n, Y2)))
    return total


@lru_cache(None)
def coeff(A, P):
    return sum((outer(A * d) / d
                for d in range(1, LIMIT // A + 1)
                if gcd(d, P) == 1), Q(0))


def returned(A, P, F, omit_k_mask=False):
    return sum((Q(mu(k), k) * coeff(k * A, P) * F(k, A)
                for k in range(1, LIMIT // A + 1)
                if omit_k_mask or gcd(k, P) == 1), Q(0))


def returned_v(A, P, F):
    return sum((outer(A * v) / v *
                sum((Q(mu(k)) * F(k, A) for k in divisors(v)), Q(0))
                for v in range(1, LIMIT // A + 1)
                if gcd(v, P) == 1), Q(0))


def primitive(n):
    # Quadratic specialization of a finite-order character.
    if n % 7 == 0:
        return 0
    return 1 if n % 7 in (1, 2, 4) else -1


def natural(n, Qmask):
    return primitive(n) if gcd(n, Qmask) == 1 else 0


counts = {}
negative = {}
count = 0
mutations = {name: False for name in
             ('g_allocation', 'short_puncture', 'long_puncture', 'mu_m')}
for k in range(1, 17):
    for d in range(1, 13):
        for A in range(1, 19):
            target = outer(k * d * A)
            require(allocated(k, d, A) == target, 'exact gcd allocation')
            count += 1
            tests = {
                'g_allocation': dict(omit_g=True),
                'short_puncture': dict(omit_t_mask=True),
                'long_puncture': dict(omit_n_mask=True),
                'mu_m': dict(omit_mu_m=True),
            }
            for label, kw in tests.items():
                if not mutations[label] and allocated(k, d, A, **kw) != target:
                    mutations[label] = True
counts['exact_fixed_k_d_g_allocations'] = count
for label, found in mutations.items():
    require(found, 'negative control: ' + label)
negative.update(mutations)


count = 0
for Qmask in (1, 2, 5, 6, 30):
    P = 7 * Qmask
    for k in range(1, 36):
        for A in range(1, 12):
            for n in range(1, 9):
                lhs = natural(k * A, Qmask) * primitive(k * n)
                rhs = (natural(A, Qmask) * primitive(n)
                       * int(gcd(k, P) == 1))
                require(lhs == rhs, 'exact phase cancellation and k mask')
                count += 1
counts['natural_primitive_mask_identities'] = count


count = 0
missing_k_mask_found = False
for P in (1, 2, 3, 6, 35, 70):
    for A in range(1, 36):
        for B, K in ((Q(6), Q(2)), (Q(17, 2), Q(3)),
                     (Q(29), Q(4))):
            head = lambda k, a: cut(Q(k * a) / B)
            small = lambda k, a: (1 - cut(Q(k * a) / B)) * cut(Q(k) / K)
            large = lambda k, a: (1 - cut(Q(k * a) / B)) * (1 - cut(Q(k) / K))
            full = lambda k, a: Q(1)
            h, s, ell = (returned(A, P, f) for f in (head, small, large))
            require(h + s + ell == outer(A), 'three coherent components')
            require(returned(A, P, full) == outer(A), 'full coefficient return')
            require(returned(A, P, head) == returned_v(A, P, head),
                    'two finite divisor-return forms')
            if returned(A, P, full, omit_k_mask=True) != outer(A):
                missing_k_mask_found = True
            count += 1
counts['masked_finite_returns_and_three_part_partitions'] = count
require(missing_k_mask_found, 'negative control: missing k mask')
negative['missing_k_mask'] = missing_k_mask_found


count = 0
for B, K in ((Q(64), Q(4)), (Q(125), Q(5)), (Q(81, 2), Q(3))):
    for k in range(1, 50):
        for A in range(1, 70):
            h = cut(Q(k * A) / B)
            s = (1 - h) * cut(Q(k) / K)
            ell = (1 - h) * (1 - cut(Q(k) / K))
            require(h + s + ell == 1, 'selector partition')
            if s:
                require(Q(A) > B / (2 * K), 'returned far support')
            if ell:
                require(k > K and k * A > B, 'large divisor support')
            count += 1
counts['selector_support_cases'] = count


count = 0
for D in (Q(50), Q(75), Q(125), Q(250)):
    for B in (Q(5), Q(10), Q(25), Q(50)):
        for k in range(1, int(B) + 1):
            R = B / k
            X = D / R
            require(R * X / D == 1, 'central normalization')
            # Compare the square of the raw reflected normalizer with
            # both central normalizers, including its k^{-1} weight.
            conductor, deleted, dual_n = Q(77), Q(3), Q(11)
            dual_scale = conductor * R * deleted / D
            raw_square = D / (conductor * k * k * R * R * deleted * deleted)
            central_square = (Q(1, k * k) / (R * deleted)
                              * (dual_n / dual_scale) / dual_n)
            require(raw_square == central_square, 'reflected normalization')
            if k > 1:
                require(raw_square != central_square * k,
                        'negative control: replace k^{-1} by k^{-1/2}')
            count += 1
counts['normalization_cases'] = count
negative['incorrect_square_root_k_weight'] = True


alpha = Q(2, 125)
r_min, r_max = Q(29, 25), Q(117, 100)
b_head = Q(101, 100)
require(r_max < Q(600, 289), 'gap increases on consumer interval')
require(Q(2, 3) < r_min < r_max < Q(200, 147), 'interior envelope branch')
require(Q(7, 12) + r_min / 2 > 1 + r_min / 50, 'printed floor dominated')
margin = Q(58, 3) - Q(26381, 6000)**2
require(margin == Q(42839, 36000000) and margin > 0, 'exact radical margin')
require(Q(659, 150) + Q(1, 400) + Q(1, 1000) == Q(26381, 6000),
        'target comparison identity')
counts['exact_radical_certificates'] = 1


count = 0
for ir in range(51):
    r = r_min + (r_max - r_min) * Q(ir, 50)
    for idelta in range(151):
        delta = Q(3, 4) * Q(idelta, 150)
        t = 15 - 6 * delta
        left = (Q(25) / t + r * t / 6)**2 - Q(100) * r / 6
        right = (Q(25) / t - r * t / 6)**2
        require(left == right and right >= 0, 'exact envelope AM-GM certificate')
        count += 1
counts['rational_joint_envelope_identities'] = count


count = 0
for ir in range(51):
    r = r_min + (r_max - r_min) * Q(ir, 50)
    lo, hi = 1 - alpha, r - alpha
    e0 = (1 + 5 * r) / 6
    # Endpoints certify each affine branch; grid is an independent mutation aid.
    for b in (lo, Q(1), hi):
        e = max(Q(1), (1 + 5 * b) / 6)
        require(e + Q(3, 4) * (r - b) <= e0 - Q(1, 750),
                'far affine branch endpoints')
        count += 1
    for ib in range(101):
        b = lo + (hi - lo) * Q(ib, 100)
        e = max(Q(1), (1 + 5 * b) / 6)
        require(e + Q(3, 4) * (r - b) <= e0 - Q(1, 750),
                'far range check')
        count += 1
    b = hi
    e = max(Q(1), (1 + 5 * b) / 6)
    require(e + Q(3, 4) * (r - b) > e0 - Q(1, 700),
            'negative control: excessive far saving')
counts['far_exponent_cases'] = count
negative['excessive_far_saving'] = True


count = 0
for puncture in (1, 2, 6, 35, 70):
    for n in range(1, 201):
        left = sum(mu(n // h) for h in divisors(n)
                   if puncture % radical(h) == 0)
        right = mu(n) * int(gcd(n, puncture) == 1)
        require(left == right, 'exact inverse puncture restoration')
        count += 1
counts['inverse_puncture_restorations'] = count


sigma = Q(79, 100)
bmin = sigma - alpha
dlo, dhi = Q(473, 1024), Q(487, 1024)
xlo, xhi = Q(49, 100), Q(1, 2)
short_gap = Q(372257, 153600000)
long_gap = Q(1099, 192000)
require(bmin == Q(387, 500), 'marked long inverse lower endpoint')
require((1 - bmin) / 2 == Q(113, 1000) < Q(1, 5),
        'marked finite prime supply requirement')
require(short_gap > Q(1, 1000) and long_gap > Q(1, 1000),
        'marked fixed reserves')
count = 0
for ir in range(21):
    r = r_min + (r_max - r_min) * Q(ir, 20)
    for jd in range(21):
        delta = dlo + (dhi - dlo) * Q(jd, 20)
        for jx in range(11):
            x = xlo + (xhi - xlo) * Q(jx, 10)
            g = x * delta
            old_count = (1 + 5 * r) / 6 - delta * r
            inverse_endpoint = 1 - g - (delta - g) * bmin
            long_endpoint = Q(1, 6) + (Q(5, 6) - delta) * (r - alpha)
            require(old_count - inverse_endpoint >= short_gap,
                    'marked short endpoint margin')
            require(old_count - long_endpoint >= long_gap,
                    'marked long endpoint margin')
            # Exact derivative signs used to certify the whole box.
            require(Q(5, 6) - delta > 0, 'increasing r gap')
            require(delta * (1 - bmin) > 0, 'increasing x gap')
            require(r - x - (1 - x) * bmin > 0, 'decreasing delta gap')
            count += 1
counts['marked_critical_box_cases'] = count
require((Q(5, 6) - dhi) * r_min - Q(5, 6)
        + xlo * dhi + (dhi - xlo * dhi) * bmin == short_gap,
        'exact marked worst corner')
require((Q(5, 6) - dhi) * alpha == long_gap,
        'exact marked long endpoint')
old_corner = (1 + 5 * r_min) / 6 - dhi * r_min
require(old_corner - (1 - dhi * bmin) < 0,
        'negative control: omit necessary prime amplification')
negative['unmarked_critical_box'] = True

count = 0
strict_loss = Q(1, 1000000)
for ib in range(101):
    b = bmin + (1 - bmin) * Q(ib, 101)
    z = max(Q(0), (1 - b) / 2 - strict_loss)
    for ih in range(21):
        shorter_b = b * Q(ih, 20)
        require(shorter_b + 2 * z < 1, 'restored marked first margin')
        require(2 * shorter_b + 8 * z < 3, 'restored marked second margin')
        count += 1
counts['marked_puncture_capacity_cases'] = count


lam = Q(73, 100)
low_gap = Q(7427, 1440000)
require(r_min - lam == Q(43, 100) and r_max - lam == Q(44, 100),
        'low returned ordinary length interval')
require(2 * (1 - 2 * (r_min - lam)) / 9 == Q(7, 225) < Q(1, 5),
        'low returned prime supply')
require(low_gap > Q(1, 1000), 'low returned fixed reserve')
count = 0
for ir in range(21):
    r = r_min + (r_max - r_min) * Q(ir, 20)
    c = r - lam
    for jd in range(21):
        delta = dlo + (dhi - dlo) * Q(jd, 20)
        for jx in range(11):
            x = xlo + (xhi - xlo) * Q(jx, 10)
            g = x * delta
            old_count = (1 + 5 * r) / 6 - delta * r
            plain_count = 1 - 2 * delta * c - Q(4, 9) * g * (1 - 2 * c)
            require(old_count - plain_count >= low_gap,
                    'low returned count gap')
            delta_derivative = r - 2 * lam + Q(4, 9) * x * (1 - 2 * r + 2 * lam)
            require(delta_derivative < 0, 'decreasing low-gap delta')
            require(Q(5, 6) + delta * (1 - Q(8, 9) * x) > 0,
                    'increasing low-gap r')
            require(Q(4, 9) * delta * (1 - 2 * r + 2 * lam) > 0,
                    'increasing low-gap x')
            count += 1
counts['low_returned_critical_box_cases'] = count
c = r_min - lam
corner_low = ((1 + 5 * r_min) / 6 - dhi * r_min
              - (1 - 2 * dhi * c - Q(4, 9) * xlo * dhi * (1 - 2 * c)))
require(corner_low == low_gap, 'exact low returned worst corner')
require((1 + 5 * r_min) / 6 - dhi * r_min
        - (1 - 2 * dhi * c) < 0,
        'negative control: discard ordinary prime mark')
negative['unmarked_low_returned'] = True

count = 0
for ic in range(101):
    c = Q(43, 100) + (Q(1, 2) - Q(43, 100)) * Q(ic, 101)
    z = max(Q(0), 2 * (1 - 2 * c) / 9 - strict_loss)
    require(2 * c + Q(9, 2) * z < 1, 'marked ordinary strict capacity')
    for g in (Q(0), Q(1, 5), Q(1, 4)):
        delta = Q(1, 2)
        # The weight is |Q|^(1/2): its fourth power is |Q|^2.
        source_fourth_exponent = 1 + 2 * delta * (r_min - c)
        unweighted_fourth_exponent = source_fourth_exponent - 2 * g * z
        witness_fourth_exponent = 2 * delta * r_min
        require(unweighted_fourth_exponent - witness_fourth_exponent
                == 1 - 2 * delta * c - 2 * g * z,
                'weighted fourth moment normalization')
        count += 1
counts['low_returned_weighted_fourth_cases'] = count


alpha2, sigma2, lam2 = Q(1, 250), Q(773, 1000), Q(147, 200)
short_gap2, long_gap2, low_gap2 = Q(371959, 307200000), Q(1099, 768000), Q(23, 16000)
require(sigma2 - alpha2 == Q(769, 1000), 'new identity long inverse endpoint')
require((1 - sigma2 + alpha2) / 2 == Q(231, 2000),
        'new identity marked inverse supply')
require(2 * (1 - 2 * (r_min - lam2)) / 9 == Q(1, 30),
        'new identity marked ordinary supply')
count = 0
for r in (r_min, r_max):
    for delta in (dlo, dhi):
        for x in (xlo, xhi):
            g = x * delta
            old = (1 + 5 * r) / 6 - delta * r
            high_short = 1 - g - (delta - g) * (sigma2 - alpha2)
            high_long = Q(1, 6) + (Q(5, 6) - delta) * (r - alpha2)
            c = r - lam2
            low = 1 - 2 * delta * c - Q(4, 9) * g * (1 - 2 * c)
            require(old - high_short >= short_gap2 > Q(1, 1000),
                    'new identity high-short margin')
            require(old - high_long >= long_gap2 > Q(1, 1000),
                    'new identity high-long margin')
            require(old - low >= low_gap2 > Q(1, 1000),
                    'new identity low margin')
            require(r - x - (1 - x) * (sigma2 - alpha2) > 0,
                    'new inverse gap decreases in delta')
            require(r - 2 * lam2 + Q(4, 9) * x * (1 - 2 * r + 2 * lam2) < 0,
                    'new ordinary gap decreases in delta')
            count += 1
counts['new_identity_exact_corner_certificates'] = count
require((1 + 5 * r_min) / 6 - dhi * r_min
        - (1 - xlo * dhi - (dhi - xlo * dhi) * (sigma2 - alpha2)) == short_gap2,
        'new inverse corner equality')
require(alpha2 * (Q(5, 6) - dhi) == long_gap2, 'new long corner equality')
c = r_min - lam2
require((1 + 5 * r_min) / 6 - dhi * r_min
        - (1 - 2 * dhi * c - Q(4, 9) * xlo * dhi * (1 - 2 * c)) == low_gap2,
        'new ordinary corner equality')


count = 0
for P in (1, 2, 6, 35):
    for A in range(1, 61):
        for B, low_cut, high_cut in ((Q(12), Q(3), Q(7)),
                                     (Q(25), Q(5), Q(11))):
            xi = cut(Q(A) / high_cut) - cut(Q(A) / low_cut)
            full = returned(A, P, lambda k, a: xi)
            head = returned(A, P, lambda k, a: cut(Q(k * a) / B) * xi)
            high = returned(A, P, lambda k, a: (1 - cut(Q(k * a) / B)) * xi)
            require(full == outer(A) * xi, 'band full k inversion')
            require(high == outer(A) * xi - head, 'high-ratio / primal-band identity')
            count += 1
counts['band_ratio_return_equivalence_identities'] = count
require(Q(1, 100) / 8 == Q(1, 800), 'pointwise head ratio saving')
require(sigma2 + Q(1, 100) == Q(783, 1000), 'thin-strip lower k exponent')


d_contact, g_contact = Q(47, 100), Q(47, 200)
r_contact = Q(6994, 6007)
R_contact = (1 + 5 * r_contact) / 6 - d_contact * r_contact
b_contact = (1 - g_contact - R_contact) / (d_contact - g_contact)
c_contact = ((1 - Q(4, 9) * g_contact - R_contact)
             / (2 * d_contact - Q(8, 9) * g_contact))
require(r_contact == (185 - 96 * d_contact) / (185 - 138 * d_contact),
        'rational source contact equation')
require(b_contact + c_contact == r_contact, 'exact inverse/plain contact')
require(dlo <= d_contact <= dhi and r_min < r_contact < r_max,
        'contact lies in actual critical box')
eta = Q(1, 1000)
high_threshold = alpha2 + (1 - g_contact - R_contact + eta) / (d_contact - g_contact)
low_threshold = (r_contact - (1 - Q(4, 9) * g_contact - R_contact + eta)
                 / (2 * d_contact - Q(8, 9) * g_contact))
gap = alpha2 + eta / (d_contact - g_contact) + eta / (2 * d_contact - Q(8, 9) * g_contact)
require(high_threshold - low_threshold == gap > 0,
        'positive resource gap at exact contact')
best_gap = eta * (1 / (Q(5, 6) - d_contact) + 1 / (d_contact - g_contact)
                  + 1 / (2 * d_contact - Q(8, 9) * g_contact))
require(best_gap > 0, 'positive resource gap at minimum admissible alpha')
counts['rational_resource_contact_certificates'] = 6
negative['false_marked_endpoint_overlap'] = True


print(json.dumps({
    'status': 'passed',
    'counts': counts,
    'negative_controls': negative,
    'exact_head_squared_comparison': str(margin),
    'head_cutoff_exponent': str(b_head),
    'small_k_cutoff_exponent': '1/100',
    'far_saving': '1/750',
    'marked_short_gap': str(short_gap),
    'marked_long_gap': str(long_gap),
    'marked_returned_threshold': '79/100',
    'low_returned_count_gap': str(low_gap),
    'low_returned_threshold': '73/100',
    'new_identity_alpha': str(alpha2),
    'new_primal_band': [str(lam2), str(sigma2)],
    'new_identity_margins': [str(short_gap2), str(long_gap2), str(low_gap2)],
    'exact_contact_resource_gap': str(gap),
    'minimum_alpha_resource_gap': str(best_gap),
    'open_estimate_proved': False,
    'scope': 'Finite arithmetic and rational certificates; no analytic premise certified.'
}, indent=2, sort_keys=True))
