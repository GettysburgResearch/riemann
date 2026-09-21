#!/usr/bin/env python3
"""Exact local Sylvester fixtures and GL(2) cutoff algebra; not a proof checker for RH/BSD."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from math import isqrt


def need(ok, message):
    if not ok:
        raise ValueError(message)


def prime(p):
    return type(p) is int and p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def emul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def eadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def epow(x, n, p):
    r = (1, 0)
    while n:
        if n & 1:
            r = tuple(v % p for v in emul(r, x))
        x = tuple(v % p for v in emul(x, x))
        n //= 2
    return r


class Field:
    """Fp[w,t]/(w^2+w+1,t^3-varpi), validated to be a field."""
    def __init__(self, p, varpi):
        need(prime(p) and p % 3 == 2 and p > 3, 'inert prime required')
        self.p, self.varpi = p, tuple(v % p for v in varpi)
        need(epow(self.varpi, (p * p - 1) // 3, p) != (1, 0), 'cubic-residue condition fails')
        need(self.varpi != (0, 0), 'good reduction required')
        self.order = p ** 6

    def elt(self, value):
        if isinstance(value, Element):
            need(value.field is self, 'different fields')
            return value
        if isinstance(value, int):
            value = (value, 0, 0, 0, 0, 0)
        need(len(value) == 6, 'six coefficients required')
        return Element(self, tuple(v % self.p for v in value))


class Element:
    def __init__(self, field, coefficients):
        self.field, self.c = field, coefficients

    def __add__(self, other):
        other = self.field.elt(other)
        return self.field.elt(tuple(a + b for a, b in zip(self.c, other.c)))
    __radd__ = __add__

    def __neg__(self):
        return self.field.elt(tuple(-v for v in self.c))

    def __sub__(self, other):
        return self + (-self.field.elt(other))

    def __rsub__(self, other):
        return self.field.elt(other) - self

    def __mul__(self, other):
        other = self.field.elt(other)
        tmp = [(0, 0)] * 5
        for i in range(3):
            for j in range(3):
                tmp[i + j] = eadd(tmp[i + j], emul(self.c[2*i:2*i+2], other.c[2*j:2*j+2]))
        for i in (4, 3):
            tmp[i - 3] = eadd(tmp[i - 3], emul(tmp[i], self.field.varpi))
        return self.field.elt(tuple(v for pair in tmp[:3] for v in pair))
    __rmul__ = __mul__

    def __pow__(self, n):
        need(type(n) is int and n >= 0, 'nonnegative exponent')
        r, x = self.field.elt(1), self
        while n:
            if n & 1:
                r = r * x
            x = x * x
            n //= 2
        return r

    def __truediv__(self, other):
        other = self.field.elt(other)
        need(other != 0, 'division by zero')
        return self * (other ** (self.field.order - 2))

    def __eq__(self, other):
        if isinstance(other, int):
            other = self.field.elt(other)
        return isinstance(other, Element) and self.field is other.field and self.c == other.c

    def __repr__(self):
        return str(self.c)


def neg(P):
    return None if P is None else (P[0], -P[1])


def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u and y == -v:
        return None
    slope = (3*x*x)/(2*y) if P == Q else (v-y)/(u-x)
    X = slope*slope-x-u
    return X, slope*(x-X)-y


def mul(n, P):
    if n < 0:
        return mul(-n, neg(P))
    Q = None
    while n:
        if n & 1:
            Q = add(Q, P)
        P = add(P, P)
        n //= 2
    return Q


def cm(w, P):
    return None if P is None else (w * P[0], P[1])


def on_curve(P, a):
    return P is None or P[1] ** 2 == P[0] ** 3 + a * a / 4


def local_fixture(q, p):
    parameters = {13: (4, 3), 31: (1, 6)}
    A, B = parameters[q]
    f = Field(p, (A, B))
    w, t = f.elt((0, 1, 0, 0, 0, 0)), f.elt((0, 0, 1, 0, 0, 0))
    vp, a = A+B*w, (A-B)-B*w
    need(w*w+w+1 == 0 and t**3 == vp, 'defining equations')
    U, V = (w-1, t) if q == 13 else ((-2-10*w)/7, t*((-5+3*w)/7))
    need(V**3-U**3 == a, 'Fermat equation')
    R = (-w*a/(V-U), -a*(1+2*w)*(V+U)/(2*(V-U)))
    Q = (U*V, (U**3+V**3)/2)
    need(on_curve(R, a) and on_curve(Q, a), 'curve equations')
    need(add(R, neg(cm(w, R))) == Q, 'first lambda division')
    alpha = vp ** ((p*p-1)//3)
    j = 1 if alpha == w else 2
    need(alpha == w**j, 'nontrivial cubic residue')
    # Independent residue-symbol calculation modulo the rational auxiliary q.
    wq = (-A * pow(B, -1, q)) % q
    need(pow(p, (q-1)//3, q) == pow(wq, j, q), 'cubic reciprocity fixture')
    need(t**(p*p) == alpha*t, 'Frobenius on the cubic root')
    FrobR = tuple(v**(p*p) for v in R)
    need(FrobR == cm(alpha, mul(-p, R)), 'CM Frobenius on elliptic curve')
    TE = (f.elt(0), -a/2)
    eps = -1 if j == 1 else 1  # eta_13=eta_31=+1 in the supplied paper.
    actual = mul(p+1, R)
    need(actual == mul(eps, TE), '(p+1)R nonzero kernel identity')
    need(actual is not None and mul(3, TE) is None and cm(w, TE) == TE, 'kernel checks')
    need(actual != mul(-eps, TE), 'wrong boundary sign must fail')
    # Relative p-Frobenius followed by [-w^2] sends TE to (0,varpi/2).
    relative = tuple(v**p for v in TE)
    sharp = neg(cm(w*w, relative))
    need(sharp == (f.elt(0), vp/2), 'relative Frobenius normalization')
    return dict(q=q, p=p, alpha_power=j, epsilon=eps, field_order=p**6,
                reduced_division=[list(z.c) for z in R],
                reduced_kernel_multiple=[list(z.c) for z in actual],
                checks='Fermat, isogeny, two Frobenius calculations, kernel and wrong-sign rejection')


def projector_checks():
    units = [(1, 0), (0, 1), (-1, -1)]
    answer = []
    for n in (3, 6, 9, 27, 81):
        for j in (1, 2):
            pi = [units[(-j*k) % 3] for k in range(n)]
            D = [((0, 0), (1, 1), (1, 0))[(j*k) % 3] for k in range(n)]
            c = (1, 0) if j == 1 else (1, 1)
            for k in range(n):
                need(emul((1, -1), D[k]) == (1-pi[k][0], -pi[k][1]), 'integral divided projector')
                need((D[k-1][0]-D[k][0], D[k-1][1]-D[k][1]) == emul(c, pi[k]),
                     'norm-projector identity')
            answer.append([n, j])
    return answer


def trace(p, m):
    need(prime(p) and p > 3 and m % p != 0, 'good-prime point count')
    b = (m*m*pow(4, -1, p)) % p
    count = 1
    for x in range(p):
        v = (x*x*x+b) % p
        count += 1 if v == 0 else (2 if pow(v, (p-1)//2, p) == 1 else 0)
    return p+1-count


def factor(n):
    out = []
    p = 2
    while p*p <= n:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        if k:
            out.append((p, k))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def divisors(n):
    ds = [1]
    for p, a in factor(n):
        ds = [d*p**j for d in ds for j in range(a+1)]
    return sorted(ds)


def gl2_checks():
    counts = [[m, p, trace(p, m)] for m in (17, 17**2) for p in (5, 11, 23, 29, 41, 47, 59, 71)]
    need(all(a == 0 for _, _, a in counts), 'inert CM trace zero')
    local = {}
    for p in (5, 7, 11):
        A = [1, trace(p, 17)]
        for k in range(2, 14):
            A.append(A[1]*A[-1]-p*A[-2])
        v = [1, -A[1], p]
        need(all(sum(v[j]*A[k-j] for j in range(min(k, 2)+1)) == int(k == 0)
                 for k in range(14)), 'degree-two local inverse')
        local[p] = A, v
    # A three-good-prime Euler product ONLY, not the full elliptic L-function.
    N = 4096
    A, v = [0]*(N+1), [0]*(N+1)
    A[1] = v[1] = 1
    for n in range(2, N+1):
        a, z = 1, 1
        for p, k in factor(n):
            if p not in local:
                a = z = 0
                break
            a *= local[p][0][k]
            z *= local[p][1][k] if k <= 2 else 0
        A[n], v[n] = a, z
    checked = 0
    for Y in (3, 7, 15, 31, 63):
        B = (Y+1)**2-1
        residual = [0]*(B+1)
        residual[1] = 1
        for d in range(1, Y+1):
            for n in range(d, B+1, d):
                residual[n] -= v[d]*A[n//d]
        ng = [2*v[n] if n <= Y else 0 for n in range(B+1)]
        for r in range(1, Y+1):
            if v[r]:
                for s in range(1, Y+1):
                    if v[s]:
                        for n in range(r*s, B+1, r*s):
                            ng[n] -= v[r]*v[s]*A[n//(r*s)]
        need(ng[1:] == v[1:B+1], 'GL2 Newton prefix')
        for n in range(2, B+1):
            fac = factor(n)
            p, a = fac[0]
            if p not in local:
                continue
            m = n//p**a
            inner = 0
            for d in divisors(m):
                if not v[d] or not A[m//d]:
                    continue
                inner += v[d]*A[m//d]*sum(local[p][1][j]*local[p][0][a-j]
                                           for j in range(min(a, 2)+1) if p**j*d <= Y)
            need(-inner == residual[n], 'degree-two cutoff boundary')
            if local[p][0][1] == 0:
                value = 0 if a % 2 else -((-p)**(a//2))*sum(v[d]*A[m//d] for d in divisors(m)
                                                                         if Y < p*p*d and d <= Y)
                need(value == residual[n], 'inert p-squared cutoff boundary')
            checked += 1
    # Rank deflation controls, coefficients ascending in z about the center.
    simple = [0, 1, 0, 1]  # z(1+z^2): only critical-line zeros besides center.
    off_line = [0, Fraction(-1, 4), 0, 1]  # z(z^2-1/4).
    high_rank = [0, 0, 0, 1, 0, 1]  # z^3(1+z^2).
    need(simple[1:][0] != 0, 'simple center after deflation')
    def evaluate(poly, z):
        return sum(c*z**k for k, c in enumerate(poly))
    need(evaluate(off_line[1:], Fraction(1, 2)) == 0 and
         evaluate(off_line[1:], Fraction(-1, 2)) == 0, 'off-line zeros survive')
    need(high_rank[1:][0] == 0, 'rank-three control is not rank one')
    return dict(inert_point_counts=counts, local_traces={str(p): a[0][1] for p, a in local.items()},
                boundary_instances=checked, cutoff_tests=[3, 7, 15, 31, 63],
                scope='three-good-prime Euler-product fixture; bad Euler factors not modeled',
                deflation_controls='simple center removed; off-line pair retained; rank three rejected')


def report():
    examples = [local_fixture(13, 17), local_fixture(13, 107), local_fixture(31, 17)]
    refused = False
    try:
        Field(53, (4, 3))
    except ValueError:
        refused = True
    need(refused, 'trivial cubic-residue control was not rejected')
    return dict(status='exact finite arithmetic, not verification of global CM or Gross-Zagier inputs',
                local_examples=examples, projector_tests=projector_checks(),
                inadmissible_q13_p53_rejected=refused, gl2=gl2_checks())


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group()
    g.add_argument('--write', type=Path)
    g.add_argument('--check', type=Path)
    args = ap.parse_args()
    text = canonical(report())
    if args.write:
        args.write.write_text(text, encoding='utf-8')
    if args.check:
        # Exact bytes, not equality that identifies boolean and numeric values.
        need(args.check.read_text(encoding='utf-8') == text, 'L-family report mismatch')
    print('PASS', hashlib.sha256(text.encode()).hexdigest())


if __name__ == '__main__':
    main()
