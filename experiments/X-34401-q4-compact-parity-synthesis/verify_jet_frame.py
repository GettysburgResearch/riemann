#!/usr/bin/env python3
"""Exact Q(sqrt(2)) replay for L-34402. Standard library only."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


class Q2:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def _c(self, x):
        return x if isinstance(x, Q2) else Q2(x)

    def __add__(self, x):
        x = self._c(x)
        return Q2(self.a + x.a, self.b + x.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, x):
        return self + (-self._c(x))

    def __rsub__(self, x):
        return self._c(x) - self

    def __mul__(self, x):
        x = self._c(x)
        return Q2(self.a * x.a + 2 * self.b * x.b,
                  self.a * x.b + self.b * x.a)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = Fraction(x)
        return Q2(self.a / x, self.b / x)

    def __eq__(self, x):
        x = self._c(x)
        return self.a == x.a and self.b == x.b

    def positive(self):
        if self.a >= 0 and self.b >= 0:
            return self.a > 0 or self.b > 0
        if self.a <= 0 and self.b <= 0:
            return False
        if self.a > 0 and self.b < 0:
            return self.a * self.a > 2 * self.b * self.b
        if self.a < 0 and self.b > 0:
            return 2 * self.b * self.b > self.a * self.a
        return False

    def text(self):
        return f"({self.a})+({self.b})sqrt2"


ZERO = Q2()
ONE = Q2(1)
RT2 = Q2(0, 1)


def ptrim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == ZERO:
        p.pop()
    return p


def padd(p, q):
    out = [ZERO for _ in range(max(len(p), len(q)))]
    for i in range(len(out)):
        out[i] = (p[i] if i < len(p) else ZERO) + (q[i] if i < len(q) else ZERO)
    return ptrim(out)


def pscale(p, c):
    return ptrim([a * c for a in p])


def pmul(p, q):
    out = [ZERO for _ in range(len(p) + len(q) - 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = out[i + j] + a * b
    return ptrim(out)


def pder(p):
    return [p[k] * k for k in range(1, len(p))] or [ZERO]


def pnegz(p):
    return [a if i % 2 == 0 else -a for i, a in enumerate(p)]


def ladd(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, ZERO) + v
        if out[k] == ZERO:
            del out[k]
    return out


def lscale(p, c):
    return {k: v * c for k, v in p.items() if v * c != ZERO}


def lmul(p, q):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            out[i + j] = out.get(i + j, ZERO) + a * b
    return {k: v for k, v in out.items() if v != ZERO}


def to_laurent(p):
    return {i: a for i, a in enumerate(p) if a != ZERO}


def circle_conj(p):
    # On |z|^2=1/2, conjugate(z^k)=2^(-k) z^(-k).
    out = {}
    for k, a in p.items():
        if k >= 0:
            scale = Fraction(1, 2 ** k)
        else:
            scale = Fraction(2 ** (-k), 1)
        out[-k] = a * scale
    return out


def outer_entry(row_i, row_j):
    return lmul(circle_conj(row_i), row_j)


def xpoly_add(p, q):
    return padd(p, q)


def xpoly_mul(p, q):
    return pmul(p, q)


def symmetric_laurent_to_x(f):
    # First write f=c0+sum_{k>0} c_k S_k(y),
    # S_k=z^k+2^(-k)z^(-k), y=z+bar(z).
    maxk = max(abs(k) for k in f) if f else 0
    S = {0: [Q2(2)], 1: [ZERO, ONE]}
    for k in range(2, maxk + 1):
        y_times = [ZERO] + S[k - 1]
        S[k] = padd(y_times, pscale(S[k - 2], Fraction(-1, 2)))

    py = [f.get(0, ZERO)]
    for k in range(1, maxk + 1):
        cp = f.get(k, ZERO)
        cn = f.get(-k, ZERO)
        assert cn == cp * Fraction(1, 2 ** k)
        py = padd(py, pscale(S[k], cp))

    # y=sqrt(2) x.
    out = []
    rt_power = ONE
    for c in py:
        out.append(c * rt_power)
        rt_power = rt_power * RT2
    return ptrim(out)


def compose_affine(poly, a: Fraction, b: Fraction):
    # x=a+(b-a)t, return power coefficients in t.
    d = b - a
    out = [ZERO for _ in range(len(poly))]
    for k, ck in enumerate(poly):
        for i in range(k + 1):
            out[i] = out[i] + ck * Fraction(comb(k, i)) * (a ** (k - i)) * (d ** i)
    return ptrim(out)


def bernstein_coeffs(poly, a: Fraction, b: Fraction, degree: int):
    power = compose_affine(poly, a, b)
    power += [ZERO] * (degree + 1 - len(power))
    coeffs = []
    for i in range(degree + 1):
        value = ZERO
        for k in range(i + 1):
            value = value + power[k] * Fraction(comb(i, k), comb(degree, k))
        coeffs.append(value)
    return coeffs


def main():
    p = pmul(pmul([ONE, Q2(-1)], [ONE, Q2(-2)]),
             pmul([ONE, -RT2], [ONE, -RT2]))
    pm = pnegz(p)
    T = pmul([ONE, Q2(-1)], [ONE, ZERO, Q2(-4)])

    qplus = [to_laurent(p), to_laurent(pscale([ZERO] + pder(p), -1))]
    # d/ds p(-z)=+L z p'(-z), hence the v-coefficient is -z d/dz p(-z).
    qminus = [to_laurent(pm), to_laurent(pscale([ZERO] + pder(pm), -1))]
    target = [to_laurent(T), to_laurent(pscale([ZERO] + pder(T), -1))]

    M = [[{} for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            value = ladd(outer_entry(qplus[i], qplus[j]),
                         outer_entry(qminus[i], qminus[j]))
            if i == 1 and j == 1:
                bare = ladd(outer_entry(to_laurent(p), to_laurent(p)),
                            outer_entry(to_laurent(pm), to_laurent(pm)))
                value = ladd(value, lscale(bare, 2))
            value = ladd(value, lscale(outer_entry(target[i], target[j]), -2))
            M[i][j] = value

    q1 = symmetric_laurent_to_x(M[0][0])
    det = ladd(lmul(M[0][0], M[1][1]), lscale(lmul(M[0][1], M[1][0]), -1))
    q2_times8 = symmetric_laurent_to_x(det)
    q2 = pscale(q2_times8, Fraction(1, 8))

    expected_q1 = [
        Q2(9), Q2(0, 18), Q2(92, 96), Q2(0, -16), Q2(32)
    ]
    expected_q2 = [
        Q2(117, 54), Q2(-216, 72), Q2(-420, 78), Q2(1560, 552),
        Q2(7912, 4776), Q2(-960, -224), Q2(976, 1344), Q2(0, -128), Q2(256)
    ]
    assert q1 == expected_q1
    assert q2 == expected_q2

    q1_intervals = [(Fraction(-1), Fraction(0)), (Fraction(0), Fraction(1))]
    q2_intervals = [
        (Fraction(-1), Fraction(-1, 2)),
        (Fraction(-1, 2), Fraction(0)),
        (Fraction(0), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(1)),
    ]

    b1 = [bernstein_coeffs(q1, a, b, 4) for a, b in q1_intervals]
    b2 = [bernstein_coeffs(q2, a, b, 8) for a, b in q2_intervals]
    assert all(c.positive() for row in b1 for c in row)
    assert all(c.positive() for row in b2 for c in row)

    result = {
        "schema": "X-34402-q4-parity-jet-frame-v1",
        "classification": "EXACT_Q_SQRT2_BERNSTEIN",
        "principal_minor_polynomial_verified": True,
        "determinant_polynomial_verified": True,
        "principal_minor_bernstein_coefficients": 10,
        "determinant_bernstein_coefficients": 36,
        "all_bernstein_coefficients_strictly_positive": True,
        "critical_jet_frame": "2|q_circ|^2 <= |q_+|^2+|q_-|^2+|B_+|^2+|B_-|^2",
        "does_not_prove": [
            "final reflected no-double-spend recurrence",
            "Riemann Hypothesis",
        ],
    }
    canonical = json.dumps(result, indent=2, sort_keys=True) + "\n"
    result["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    destination = Path(__file__).with_name("results") / "jet-frame-verification.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
