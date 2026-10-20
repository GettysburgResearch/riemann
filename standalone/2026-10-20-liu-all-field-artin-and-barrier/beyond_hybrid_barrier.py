#!/usr/bin/env python3
"""Exact rational certificate for the balanced hybrid-numerator barrier.

Proves finite algebra/sign predicates supporting beyond_hybrid_barrier.md
and beyond_free_length_barrier.md.
No floating-point value participates in acceptance. The analytic comparison
formula is imported from Liu, arXiv:2610.26835v1, (14.3), (14.8), and (2.3).
This does not check Liu's analytic proof or exclude actual zeros.
"""
from fractions import Fraction as F
import json


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def of(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        other = I.of(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-I.of(other))

    def __rsub__(self, other):
        return I.of(other) - self

    def __mul__(self, other):
        other = I.of(other)
        a = [self.lo * other.lo, self.lo * other.hi,
             self.hi * other.lo, self.hi * other.hi]
        return I(min(a), max(a))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I.of(other)
        if other.lo <= 0 <= other.hi:
            raise ValueError("division interval contains zero")
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return I.of(other) / self

    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("nonnegative integer power required")
        out = I(1)
        for _ in range(n):
            out *= self
        return out

    def receipt(self):
        return {"lo": str(self.lo), "hi": str(self.hi),
                "display_lo": float(self.lo), "display_hi": float(self.hi)}


def require(condition, name):
    if not condition:
        raise ValueError("certificate failed: " + name)


def poly(coeff, x):
    out = I(0) if isinstance(x, I) else F(0)
    for c in reversed(coeff):
        out = out * x + c
    return out


def ptrim(a):
    a = [F(x) for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    return ptrim([(a[i] if i < len(a) else F(0)) +
                  (b[i] if i < len(b) else F(0))
                  for i in range(max(len(a), len(b)))])


def psub(a, b):
    return padd(a, [-x for x in b])


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return ptrim(out)


def prem(a, b):
    a, b = ptrim(a), ptrim(b)
    while len(a) >= len(b) and a != [0]:
        degree, factor = len(a) - len(b), a[-1] / b[-1]
        for i, x in enumerate(b):
            a[degree + i] -= factor * x
        a = ptrim(a)
    return a


Q = [-275, 1290, 9936, -27405, 16686]
Qprime = [1290, 19872, -82215, 66744]
U = [2200, -26220, -49500, 1086480, -1263600]
V = [2220, -25272, -30672, 917568, -1026432]
# Coefficients in delta, each a polynomial in kappa, in ascending order.
CR = [[0, 40, -300], [-5, -54, 756], [3, 0, -324]]
N = [[0, -60, 450], [-5, 126, -684], [3, -72, 324]]
D = [[0, -300, 2250], [-25, 450, -2340], [15, -144, 324]]


def rational_delta_numerator(coefficients):
    return padd(padd(pmul(coefficients[2], pmul(U, U)),
                     pmul(coefficients[1], pmul(U, V))),
                pmul(coefficients[0], pmul(V, V)))


def pcoprime(a, b):
    a, b = ptrim(a), ptrim(b)
    while b != [0]:
        a, b = b, prem(a, b)
    return len(a) == 1 and a[0] != 0


class RQ:
    """Exact rational functions evaluated in Q[kappa]/(Q(kappa))."""
    def __init__(self, numerator, denominator=None):
        numerator = numerator if isinstance(numerator, list) else [F(numerator)]
        denominator = [F(1)] if denominator is None else denominator
        self.n, self.d = prem(numerator, Q), prem(denominator, Q)
        require(pcoprime(self.d, Q), "algebraic denominator coprime to Q")

    @staticmethod
    def of(x):
        return x if isinstance(x, RQ) else RQ(x)

    def __add__(self, other):
        other = RQ.of(other)
        return RQ(padd(pmul(self.n, other.d), pmul(other.n, self.d)),
                  pmul(self.d, other.d))

    __radd__ = __add__

    def __neg__(self):
        return RQ([-x for x in self.n], self.d)

    def __sub__(self, other):
        return self + (-RQ.of(other))

    def __rsub__(self, other):
        return RQ.of(other) - self

    def __mul__(self, other):
        other = RQ.of(other)
        return RQ(pmul(self.n, other.n), pmul(self.d, other.d))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = RQ.of(other)
        require(pcoprime(other.n, Q), "algebraic divisor coprime to Q")
        return RQ(pmul(self.n, other.d), pmul(self.d, other.n))

    def __rtruediv__(self, other):
        return RQ.of(other) / self


def verify_direct_critical_zero():
    """Substitute into the original E_av, without assuming Lemma 14.9's algebra."""
    k, delta = RQ([0, 1]), RQ(U, V)
    ell, c = F(5, 3) - 2 * k, 1 / (3 * k)
    dd, pp = F(5, 2) - c, 1 - c / 2
    jj = (F(5, 6) - delta) * dd + delta * pp
    rr = 1 - delta + (F(5, 6) - delta) * delta * pp / (2 * jj)
    # The displayed endpoint is affine in b. Its values at b=0 and b=1
    # therefore bind the identity for every b, including b<0.
    for b in (0, 1):
        h, ly = (1 + b + 3 * ell) / 2, (1 + b - ell) / 2
        c0 = -F(1, 4) + F(b, 6) + 5 * ell / 4
        eav = c0 + delta / 2 + delta * (ell + c * (h / 4 - ly / 2)) / 2 - 3 * h * (1 - rr) / 4
        require(eav.n == [0], "direct critical averaged zero at b=" + str(b))


def exponents(b, ell, kappa, delta, x=F(1, 2)):
    b, ell, kappa, delta, x = map(I.of, (b, ell, kappa, delta, x))
    c = 1 / (3 * kappa)
    d = 3 - (1 + 2 * c) * x
    p = (2 - 2 * c * x) * (1 - x)
    j = (F(5, 6) - delta) * d + delta * p
    r = 1 - delta + (F(5, 6) - delta) * delta * p / (2 * j)
    h, ly = (1 + b + 3 * ell) / 2, (1 + b - ell) / 2
    c0 = -F(1, 4) + b / 6 + 5 * ell / 4
    eav = c0 + delta / 2 + delta * x * (ell + c * (h / 4 - ly / 2)) - 3 * h * (1 - r) / 4
    ept = c0 + (F(1, 2) + ell) * delta + ell * delta * x - h * (1 - r)
    sav = F(1, 6) - c * delta * x / 8 - 3 * (1 - r) / 8
    spt = F(1, 6) - (1 - r) / 2
    return eav, ept, sav, spt


class S:
    """Tiny sparse exact polynomial ring, for checking affine reductions."""
    def __init__(self, value):
        if isinstance(value, dict):
            self.c = {m: F(v) for m, v in value.items() if v}
        elif isinstance(value, str):
            self.c = {(value,): F(1)}
        else:
            self.c = {} if not value else {(): F(value)}

    @staticmethod
    def of(x):
        return x if isinstance(x, S) else S(x)

    def __add__(self, other):
        out = self.c.copy()
        for m, v in S.of(other).c.items():
            out[m] = out.get(m, F(0)) + v
        return S(out)

    __radd__ = __add__

    def __neg__(self):
        return S({m: -v for m, v in self.c.items()})

    def __sub__(self, other):
        return self + (-S.of(other))

    def __rsub__(self, other):
        return S.of(other) - self

    def __mul__(self, other):
        out = {}
        for m, v in self.c.items():
            for n, w in S.of(other).c.items():
                mn = tuple(sorted(m + n))
                out[mn] = out.get(mn, F(0)) + v * w
        return S(out)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (1 / F(other))

    def sub(self, mapping):
        out = S(0)
        for monomial, coefficient in self.c.items():
            term = S(coefficient)
            for variable in monomial:
                term *= mapping.get(variable, S(variable))
            out += term
        return out


def verify_free_length_algebra():
    b, ell, ell0, t, B0, gap, delta, r, theta = map(
        S, ("b", "ell", "ell0", "t", "B0", "gap", "delta", "R", "theta"))
    a, g, kr = (1 + delta) / 2, delta / 2, (3 * r + 1) / 4

    def full(M, b_, ell_, B):
        lx, ly = (M - b_) / 2, (M + b_) / 2
        h = 1 - lx + ell_
        left = a - B - a * ly - ell_ / 2 + ell_ * g + h * (r + delta / 2 - F(1, 6))
        right = a - B + (a - 1) * ly - ell_ / 2 + ell_ * g + h * (r - F(1, 6))
        avg0 = a - B - ly / 2 - ell_ / 2 + ell_ * g + h * (kr - F(1, 6))
        avgmax = avg0 + theta * (h / 2 - ly)
        return [left, right, avg0, avgmax]

    general = full(1 - ell + t, b, ell, B0 - gap)
    balanced = full(1 - ell0, b, ell0, B0)
    balanced0 = full(1 - ell0, S(0), ell0, B0)
    A0 = -F(1, 8) + 9 * r / 8 + delta / 2
    C0 = -F(7, 24) - 3 * r / 8
    AA = [-F(1, 2) + 3 * r / 2 + 3 * delta / 2,
          -F(1, 2) + 3 * r / 2 + delta / 4, A0, A0 + 5 * theta / 4]
    CC = [-F(1, 6) - (delta + r) / 2,
          -F(1, 6) - r / 2 + delta / 4, C0, C0 - 3 * theta / 4]
    ss = [-F(1, 3) + r / 2,
          -F(1, 3) + r / 2 + delta / 4,
          -F(5, 24) + 3 * r / 8,
          -F(5, 24) + 3 * r / 8 - theta / 4]
    neg_b_slopes = [-F(1, 6) - delta / 2, -(1 - delta) / 6,
                    -(1 + delta) / 6, -(1 + delta) / 6 - 2 * theta / 3]
    left_slopes = [-S(1) / 3, -(1 - delta) / 3,
                   (-1 + delta / 2) / 3, (-1 + delta / 2 - theta) / 3]
    right_slopes = [-F(4, 3) + 3 * r + 3 * delta,
                    -F(4, 3) + 3 * r + 5 * delta / 6,
                    -F(7, 12) + 9 * r / 4 + 7 * delta / 6,
                    -F(7, 12) + 9 * r / 4 + 7 * delta / 6 + 13 * theta / 6]
    for j in range(4):
        require(not (general[j] - balanced[j] - AA[j] * (ell - ell0)
                     - CC[j] * t - gap).c, "free-length affine identity " + str(j))
        require(not (balanced[j] - balanced0[j] - ss[j] * b).c,
                "balanced b slope " + str(j))
        require(not (ss[j] - AA[j] / 3 - neg_b_slopes[j]).c,
                "paid negative-b slope " + str(j))
        require(not (CC[j] + AA[j] / 3 - left_slopes[j]).c,
                "negative-t coefficient " + str(j))
        require(not (CC[j] + 7 * AA[j] / 3 - right_slopes[j]).c,
                "positive-t coefficient " + str(j))

    require(not (balanced[1] - balanced[0] - delta * (1 + b - 5 * ell0) / 4).c,
            "balanced pointwise dual order")
    require(not (balanced[2] - balanced[3] - theta * (1 + b - 5 * ell0) / 4).c,
            "balanced averaged shift order")

    # R >= 1-delta and 0 <= delta <= 12/25. Substitution makes the
    # inequalities positive-coefficient polynomials in rho,u,theta >= 0.
    rho, u = S("rho"), S("u")
    substitution = {"delta": F(12, 25) - u,
                    "R": 1 - (F(12, 25) - u) + rho}
    a_floors = [F(1), F(2, 5), F(7, 10), F(7, 10)]
    left_floors = [F(1, 3), F(13, 75), F(19, 75), F(19, 75)]
    right_floors = [F(5, 3), F(47, 75), F(86, 75), F(86, 75)]
    for j in range(4):
        for label, polynomial, floor in [
            ("A", AA[j], a_floors[j]),
            ("negative left slope", -left_slopes[j], left_floors[j]),
            ("right slope", right_slopes[j], right_floors[j]),
        ]:
            rem = (polynomial - floor).sub(substitution)
            require(all(v >= 0 for v in rem.c.values()),
                    "positive-coefficient " + label + " " + str(j))
    # Bind the complete direct-price normalization and its unrestricted floor.
    MM, GG, KK = S("M"), S("G"), S("K")
    low = F(5, 6) + (MM - b) / 12 - ell / 6 + GG + KK / 2
    L0 = F(5, 6) + MM / 12 - ell / 6
    LK = F(1, 3) + 7 * MM / 12 + ell / 3
    LJ = F(23, 24) - MM / 6 + 5 * ell / 24
    require(not (low - L0 - (GG - b / 12 + KK / 2)).c, "direct L0 identity")
    require(not (low - LK - (GG - b / 12 + (KK - MM - ell + 1) / 2)).c,
            "direct LK identity")
    require(not (low - LJ - (GG - b / 12 + (KK - (1 + 3 * ell - 2 * MM) / 4) / 2)).c,
            "direct LJ identity")
    require(not (F(17, 30) * L0 + F(1, 30) * LK + F(2, 5) * LJ - F(13, 15)).c,
            "unrestricted direct 13/15 floor identity")
    balance_low = low.sub({"M": 1 - ell + t})
    require(not (balance_low - (F(11, 12) - ell / 4 + t / 12 - b / 12 + GG + KK / 2)).c,
            "exact direct balancing price")
    return {"affine_endpoint_identities": 4, "negative_b_identities": 4,
            "other_slope_and_order_identities": 14,
            "direct_price_identities": 5,
            "positive_coefficient_inequalities": 12,
            "scope": "four stated optimistic endpoints; free total length and either sign of b"}


def main():
    k = I(F(749773294079928, 10**15), F(749773294079929, 10**15))
    require(poly(Q, k.lo) > 0 > poly(Q, k.hi), "quartic endpoint signs")
    require(poly(Qprime, k).hi < 0, "quartic unique root in isolating interval")
    vk = poly(V, k)
    require(vk.lo > 0 or vk.hi < 0, "delta denominator")
    delta = poly(U, k) / vk
    require(F(4693, 10000) < delta.lo < delta.hi < F(4694, 10000), "critical delta bracket")
    ell = F(5, 3) - 2 * k
    require(F(1, 6) < ell.lo < ell.hi < F(1, 5), "critical length range")

    # These identities bind delta=U/V to the critical equation and
    # ell=5/3-2*kappa to Liu's exact ell_star=N/D, at the isolated root Q=0.
    require(prem(rational_delta_numerator(CR), Q) == [0], "critical polynomial identity")
    T = [psub(pmul([F(5, 3), -2], dd), nn) for dd, nn in zip(D, N)]
    require(prem(rational_delta_numerator(T), Q) == [0], "critical length polynomial identity")
    denom_d = sum(poly(D[i], k) * delta**i for i in range(3))
    require(denom_d.lo > 0 or denom_d.hi < 0, "ell_star denominator")
    verify_direct_critical_zero()

    b0, b1, b2 = F(969, 10000), F(273, 2500), F(13, 100)
    records = {}

    _, ept, _, spt = exponents(b0, ell, k, delta)
    require(ept.lo > F(19, 10**8), "critical pointwise margin")
    require(spt.hi < 0, "critical pointwise slope")
    records["0<b<=0.0969"] = {
        "delta": delta.receipt(), "averaged": "exactly zero by critical identities",
        "pointwise_at_upper_b": ept.receipt(), "pointwise_b_slope": spt.receipt()}

    for label, left, right, delta0, floor_av, floor_pt in [
        ("0.0969<=b<=0.1092", b0, b1, F(9, 20), F(97, 10**7), F(96, 10**8)),
        ("0.1092<=b<=0.13", b1, b2, F(21, 50), F(16, 10**7), F(8, 10**5)),
    ]:
        eav_left, _, sav, spt = exponents(left, ell, k, delta0)
        _, ept_right, _, _ = exponents(right, ell, k, delta0)
        require(sav.lo > 0 and spt.hi < 0, label + " slopes")
        require(eav_left.lo > floor_av, label + " averaged margin")
        require(ept_right.lo > floor_pt, label + " pointwise margin")
        records[label] = {"delta": str(delta0),
                          "averaged_min": eav_left.receipt(),
                          "pointwise_min": ept_right.receipt(),
                          "averaged_b_slope": sav.receipt(),
                          "pointwise_b_slope": spt.receipt()}

    eav, ept, sav, spt = exponents(b2, ell, k, F(3, 8))
    require(sav.lo > 0 and spt.lo > 0, "b>=0.13 slopes")
    require(eav.lo > F(65, 10**6), "b>=0.13 averaged margin")
    require(ept.lo > F(38, 10**5), "b>=0.13 pointwise margin")
    records["b>=0.13"] = {"delta": "3/8", "averaged_min": eav.receipt(),
                            "pointwise_min": ept.receipt(),
                            "averaged_b_slope": sav.receipt(),
                            "pointwise_b_slope": spt.receipt()}

    free_length = verify_free_length_algebra()
    print(json.dumps({"status": "PASS", "arithmetic": "exact fractions and enclosing intervals",
                      "scope": "finite scalar identities and signs, not analytic L-function proof",
                      "kappa": k.receipt(), "ell": ell.receipt(), "witnesses": records,
                      "free_length_extension": free_length},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
