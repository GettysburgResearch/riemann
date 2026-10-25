#!/usr/bin/env python3
"""Exact rational certificate for the fixed-cap mixed numerator model.

No optimizer, floating-point acceptance, network, or third-party library is
used. The six duals were discovered numerically; this file verifies rounded
rational duals with full residual allowances on a proved parameter box.
This is a scalar certificate, not verification of the imported moment theorems.
"""
from fractions import Fraction as F
import json
from pathlib import Path

if not __debug__:
    raise SystemExit('This certificate requires assertions; run Python without -O.')


class I:
    def __init__(self, lo, hi=None):
        if isinstance(lo, I):
            self.lo, self.hi = lo.lo, lo.hi
        else:
            self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = I(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -I(other)

    def __rsub__(self, other):
        return I(other) + -self

    def __mul__(self, other):
        other = I(other)
        vals = [a * b for a in (self.lo, self.hi)
                for b in (other.lo, other.hi)]
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I(other)
        assert not other.lo <= 0 <= other.hi
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return I(other) / self

    def __pow__(self, n):
        assert n >= 0
        ans = I(1)
        for _ in range(n):
            ans = ans * self
        return ans

    def absmax(self):
        return max(abs(self.lo), abs(self.hi))


def trim(a):
    a = list(map(F, a))
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    return trim(c)


def scale(a, s):
    return trim([F(s) * x for x in a])


def divmodp(a, b):
    a, b = trim(a), trim(b)
    q = [F(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        j, v = len(a) - len(b), a[-1] / b[-1]
        q[j] = v
        a = add(a, [F(0)] * j + scale(b, -v))
    return trim(q), trim(a)


def poly(a, x):
    out = I(0)
    for v in reversed(a):
        out = out * x + v
    return out


PK = [-275, 1290, 9936, -27405, 16686]
K = I(F(749773294079927, 10**15), F(749773294079930, 10**15))
DPK = [i * PK[i] for i in range(1, len(PK))]
assert poly(PK, I(K.lo)).lo > 0 > poly(PK, I(K.hi)).hi
assert poly(DPK, K).hi < 0
B = (1 + K) / 2

# delta_c = N(kappa)/D(kappa), with an exact critical-count identity.
N, D = [0, -15, 27], [5, 18, -18]
DC = poly(N, K) / poly(D, K)
Qcritical = add(
    add(mul([3, 0, -324], mul(N, N)),
        mul([-5, -54, 756], mul(N, D))),
    mul([0, 40, -300], mul(D, D)))
assert divmodp(Qcritical, PK) == (list(map(F, [0, -5, -42])), [F(0)])

# Verify 9 R_k(delta_c,1/2)-5-delta_c/(2 kappa)=0 modulo PK.
jnum = add(mul([F(-5, 3), F(25, 2)], D), mul(N, [1, -9]))
rnum = add(scale(mul(add(D, scale(N, -1)), jnum), 2),
           mul(mul(add(scale(D, F(5, 6)), scale(N, -1)), N), [-1, 6]))
rden = scale(mul(D, jnum), 2)
critical_identity = add(
    mul(mul([0, 2], D), add(scale(rnum, 9), scale(rden, -5))),
    scale(mul(N, rden), -1))
assert divmodp(critical_identity, PK)[1] == [F(0)]

# The exact averaged dual value equals (1+kappa)/2 at delta=N/D.
fnum = add(add(mul([0, 42], D), mul([0, 42], N)), scale(N, 11))
fden = add(add(mul([0, 54], D), mul([0, 36], N)), scale(N, 12))
assert add(scale(fnum, 2), scale(mul([1, 1], fden), -1)) == [F(0)]

# Isolate the smaller pointwise critical root uniformly over K.
XI = I(F(388582767883349, 10**15), F(388582767883357, 10**15))


def qxi(x):
    return (216*K - 18)*x*x - (468*K - 57)*x + 150*K - 20


assert qxi(I(XI.lo)).lo > 0 > qxi(I(XI.hi)).hi
assert (2*(216*K - 18)*XI - (468*K - 57)).hi < 0


def count(d):
    p = 1 - 1/(6*K)
    dd = F(5, 2) - 1/(3*K)
    jj = (F(5, 6)-d)*dd + d*p
    assert jj.lo > 0
    return 1-d+(F(5, 6)-d)*d*p/(2*jj)


# Affine vectors are [constant, M, b, ell].
def vadd(*vs):
    return [sum((v[j] for v in vs), I(0)) for j in range(4)]


def vmul(t, v):
    return [I(t)*x for x in v]


h = list(map(I, [1, F(-1, 2), F(1, 2), 1]))
y = list(map(I, [0, F(1, 2), F(1, 2), 0]))
ell = list(map(I, [0, 0, 0, 1]))
L0 = list(map(I, [F(5, 6), F(1, 12), 0, F(-1, 6)]))
LK = list(map(I, [F(1, 3), F(7, 12), 0, F(1, 3)]))
L0b = vadd(L0, list(map(I, [0, 0, F(-1, 12), 0])))
LKb = vadd(LK, list(map(I, [0, 0, F(-1, 12), 0])))
right_side = vadd(vmul(2, y), vmul(-1, h))  # 2 ly-h <= 0


def high(d, kind, side):
    d = I(d)
    r, g = count(d), d/2
    u, qq = g/(6*K), (3*r+1)/4
    cc = vadd([(1+d)/2, I(0), I(0), I(0)],
              vmul(F(-1, 6), h), vmul(F(-1, 2), y), vmul(g-F(1, 2), ell))
    if kind == 'P':
        distance = vadd(h, vmul(-1, y)) if side == 'left' else y
        return vadd(cc, vmul(r, h), vmul(d/2, distance))
    assert kind == 'A'
    tilt = vadd(vmul(F(1, 2), h), vmul(-1, y))
    return vadd(cc, vmul(qq, h), vmul(u if side == 'left' else -u, tilt))


def check_dual(name, terms, integer_weights, side_weight=0):
    assert all(w > 0 for w in integer_weights)
    total = sum(integer_weights)
    ws = [F(w, total) for w in integer_weights]
    assert sum(ws) == 1
    ans = vadd(*(vmul(w, term) for w, term in zip(ws, terms)))
    if side_weight:
        assert side_weight > 0
        ans = vadd(ans, vmul(F(side_weight, 10**12), right_side))
    # B<7/8 and the low constraints give 0<=M<=1, |b|<=1, 0<=ell<=2.
    residual = ans[1].absmax() + ans[2].absmax() + 2*ans[3].absmax()
    floor = ans[0].lo - residual
    assert floor > B.hi, (name, float(floor), float(B.hi))
    return dict(name=name, rational_weights=[str(w) for w in ws],
                side_weight=str(F(side_weight, 10**12)),
                rigorous_lower_bound=str(floor),
                lower_bound_decimal=float(floor),
                residual_allowance=str(residual),
                margin_above_B_flat_lower_bound=float(floor-B.hi))


cases = [
    check_dual('right_point', [L0b, LKb, high(DC, 'P', 'right')],
               [461108703518, 113000555632, 425890740850], 28250138908),
    check_dual('right_average', [L0b, LKb, high(DC, 'A', 'right')],
               [439749746269, 117479332804, 442770920927], 69774280882),
    check_dual('left_xi_point', [L0, LK, high(XI, 'P', 'left')],
               [687392342258, 125043063097, 187564594645]),
    check_dual('left_xi_average_43_point',
               [L0, LK, high(XI, 'A', 'left'), high(F(43, 100), 'P', 'left')],
               [675628381548, 125108107905, 76778023559, 122485486988]),
    check_dual('left_43_average_45_point',
               [L0, LK, high(F(43, 100), 'A', 'left'), high(F(9, 20), 'P', 'left')],
               [664163876107, 125103809010, 138011532368, 72720782515]),
    check_dual('left_critical_point_45_average',
               [L0, LK, high(DC, 'P', 'left'), high(F(9, 20), 'A', 'left')],
               [655089546038, 125111562089, 36174178547, 183624713326]),
]

# All retained block envelopes have an interior crossing and slopes p>u.
for d in (XI, I(F(43, 100)), I(F(9, 20)), DC):
    r, p, u = count(d), d/2, d/(12*K)
    q = (3*r+1)/4
    assert (p-u).lo > 0
    assert (q-u/2-r).lo > 0
    assert (r+p/2-q).lo > 0

# The exact averaged-left dual is covered by polynomial identities above.
# Check its positive weights and parameter range using interval arithmetic.
gc, uc = DC/2, DC/(12*K)
den = 3+4*gc+8*uc
w0 = (4+14*gc+22*uc)/(3*den)
wk = 2*(1-gc+uc)/(3*den)
wh = 1/den
assert min(w0.lo, wk.lo, wh.lo) > 0
assert F(1, 8) < XI.lo < XI.hi < F(43, 100) < F(9, 20) < DC.lo < DC.hi < F(11, 15)

# Negative control: reversing the root bracket must not be accepted.
try:
    I(K.hi, K.lo)
except AssertionError:
    negative_control = True
else:
    raise AssertionError('interval implementation accepted reversed bounds')

report = dict(
    status='PASS', scope='fixed-kappa expanded scalar comparison only',
    kappa_interval=[str(K.lo), str(K.hi)],
    B_flat_interval=[str(B.lo), str(B.hi)],
    critical_delta_interval=[str(DC.lo), str(DC.hi)],
    xi_interval=[str(XI.lo), str(XI.hi)],
    exact_polynomial_identities=3,
    strict_duals=cases,
    exact_averaged_left_dual=True,
    smallest_strict_margin=min(x['margin_above_B_flat_lower_bound'] for x in cases),
    negative_control=negative_control,
    warning='No arithmetic input or RH claim is verified by this scalar certificate.'
)
Path(__file__).with_name('MIXED_NUMERATOR_CHECKS.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({k: report[k] for k in ('status', 'scope', 'exact_polynomial_identities',
                                      'smallest_strict_margin', 'negative_control')}, indent=2))
