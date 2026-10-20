#!/usr/bin/env python3
"""Exact finite checks for the primitive-twist Type-I research packet.

No numerical integration, floating point, external packages, or analytic
zero-free theorem is certified. Mutations must fail, including under -O.
"""
from __future__ import annotations
import argparse
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from math import gcd, lcm
from typing import Iterable


class CheckFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def divide_exact(a: list[int], b: list[int]) -> list[int]:
    a = a[:]
    require(b[-1] == 1, "nonmonic polynomial divisor")
    out = [0] * (len(a) - len(b) + 1)
    for k in range(len(out) - 1, -1, -1):
        c = a[k + len(b) - 1]
        out[k] = c
        for j, v in enumerate(b):
            a[k+j] -= c * v
    require(not any(a), "inexact polynomial division")
    return trim(out)


@lru_cache(None)
def cyclotomic(n: int) -> tuple[int, ...]:
    a = [-1] + [0] * (n-1) + [1]
    for d in range(1, n):
        if n % d == 0:
            a = divide_exact(a, list(cyclotomic(d)))
    return tuple(a)


class Roots:
    """Integer arithmetic in Z[z]/Phi_order(z), using cyclic representatives."""
    def __init__(self, order: int):
        self.order = order
        self.mod = cyclotomic(order)
        self.degree = len(self.mod)-1
        self.terms = [(i, v) for i, v in enumerate(self.mod[:-1]) if v]

    def reduce(self, a: Iterable[int]) -> tuple[int, ...]:
        v = list(a)
        v += [0] * max(0, self.order-len(v))
        for k in range(len(v)-1, self.degree-1, -1):
            c = v[k]
            if c:
                for j, u in self.terms:
                    v[k-self.degree+j] -= c*u
                v[k] = 0
        return tuple(v[:self.degree])

    def mono_sum(self, exponents: Iterable[int]) -> list[int]:
        v = [0] * self.order
        for e in exponents:
            v[e % self.order] += 1
        return v

    def mul(self, a: list[int], b: list[int]) -> list[int]:
        out = [0] * self.order
        aa = [(i, v) for i, v in enumerate(a) if v]
        bb = [(i, v) for i, v in enumerate(b) if v]
        for i, x in aa:
            for j, y in bb:
                out[(i+j) % self.order] += x*y
        return out

    def shift(self, a: list[int], e: int) -> list[int]:
        out = [0] * self.order
        for i, v in enumerate(a):
            out[(i+e) % self.order] = v
        return out

    def conjugate(self, a: list[int]) -> list[int]:
        return [a[-i % self.order] for i in range(self.order)]


class Field:
    """F_p, or F_p[w]/(w^2+w+1) for inert p = 2 mod 3."""
    def __init__(self, p: int, quadratic: bool = False):
        self.p, self.quadratic = p, quadratic
        require(not quadratic or p % 3 == 2, "extension polynomial is reducible")
        self.q = p*p if quadratic else p
        self.products = [[self._mul(x, y) for y in range(self.q)] for x in range(self.q)]
        self.generator = next(g for g in range(1, self.q) if self._order(g) == self.q-1)
        self.log: dict[int, int] = {}
        x = 1
        for k in range(self.q-1):
            self.log[x] = k
            x = self.mul(x, self.generator)
        self.inv = {x: self.power(x, self.q-2) for x in range(1, self.q)}

    def _mul(self, x: int, y: int) -> int:
        p = self.p
        if not self.quadratic:
            return x*y % p
        a, b, c, d = x % p, x // p, y % p, y // p
        return (a*c-b*d) % p + p*((a*d+b*c-b*d) % p)

    def mul(self, x: int, y: int) -> int:
        return self.products[x][y]

    def add(self, x: int, y: int) -> int:
        if not self.quadratic:
            return (x+y) % self.p
        return (x % self.p+y % self.p) % self.p + self.p*((x//self.p+y//self.p) % self.p)

    def trace(self, x: int) -> int:
        return (2*(x % self.p)-x//self.p) % self.p if self.quadratic else x

    def power(self, x: int, n: int) -> int:
        y = 1
        while n:
            if n & 1:
                y = self.mul(y, x)
            x = self.mul(x, x)
            n //= 2
        return y

    def _order(self, x: int) -> int:
        y = 1
        for k in range(1, self.q):
            y = self.mul(y, x)
            if y == 1:
                return k
        raise CheckFailure("invalid finite field")


def local_checks(mutation: str | None) -> dict:
    digest = hashlib.sha256()
    cases, gauss_cases, pole_cases, unit_cases = 0, 0, 0, 0
    records = []
    for p, quadratic in [(7, False), (13, False), (19, False), (31, False), (2, True), (5, True)]:
        ff = Field(p, quadratic)
        q, m = ff.q, ff.q-1
        ring = Roots(lcm(p, m))
        char_scale, add_scale = ring.order//m, ring.order//p
        cubic = m//3
        gauss: dict[int, list[int]] = {}
        for j in range(m):
            gauss[j] = ring.mono_sum(char_scale*j*ff.log[x] + add_scale*ff.trace(x) for x in range(1, q))
        for j in range(1, m):
            norm = ring.reduce(ring.mul(gauss[j], ring.conjugate(gauss[j])))
            require(norm == (q,) + (0,)*(ring.degree-1), f"Gauss norm: q={q}, j={j}")
            gauss_cases += 1
            actual_theta = (j+cubic) % m
            theta = j if mutation == "forget-cubic" else actual_theta
            # h=1 is ad=1. One extra h verifies the unit factor in ad=h.
            hs = [1, ff.generator] if j in {1, m-cubic} else [1]
            for h in hs:
                phase = -char_scale*j*ff.log[h]
                for v in range(q):
                    direct = [0] * ring.order
                    for d in range(1, q):
                        a = ff.mul(h, ff.inv[d])
                        k_phase = char_scale*cubic*ff.log[a]
                        va = ff.mul(v, a)
                        for x in range(1, q):
                            e = char_scale*j*ff.log[x] + k_phase
                            e += add_scale*ff.trace(ff.add(ff.mul(d, x), va))
                            direct[e % ring.order] += 1
                    if theta:
                        expected = [0] * ring.order if v == 0 else ring.shift(ring.mul(gauss[j], gauss[theta]), phase-char_scale*theta*ff.log[v])
                    else:
                        c = q-1 if v == 0 else -1
                        expected = [c*x for x in ring.shift(gauss[j], phase)]
                    if mutation == "erase-zero" and theta and v == 0:
                        expected = ring.shift(ring.mul(gauss[j], gauss[theta]), phase)
                    a, b = ring.reduce(direct), ring.reduce(expected)
                    require(a == b, f"local transform: q={q}, psi={j}, v={v}, h={h}")
                    if h == 1:
                        cases += 1
                    else:
                        unit_cases += 1
                    if v == 0:
                        pole_cases += 1
                    if h == 1 and v == 1:
                        norm = ring.reduce(ring.mul(direct, ring.conjugate(direct)))
                        expected_norm = q*q if actual_theta else q
                        if mutation == "cheap-quadratic" and actual_theta:
                            expected_norm = q
                        require(norm == (expected_norm,) + (0,)*(ring.degree-1), f"conductor mass: q={q}, psi={j}")
                    digest.update(f"{q}:{j}:{h}:{v}:{a}\n".encode())
            records.append({"norm": q, "character_exponent": j, "resonant": actual_theta == 0})
    return {"field_norms": [7, 13, 19, 31, 4, 25], "characters": len(records), "transform_identities": cases,
            "additional_unit_identities": unit_cases, "gauss_norms": gauss_cases,
            "zero_frequency_checks": pole_cases, "exact_stream_sha256": digest.hexdigest()}


def root_checks() -> dict:
    def poly(x: F) -> F:
        return (((133488*x-376596)*x+384534)*x-167541)*x+26231
    lo, hi = F(874886647039964, 10**15), F(874886647039965, 10**15)
    require(poly(lo)*poly(hi) < 0, "quartic bracket")
    # A direct rational derivative bound on this very short interval.
    dl = 4*133488*lo**3-3*376596*hi**2+2*384534*lo-167541
    dh = 4*133488*hi**3-3*376596*lo**2+2*384534*hi-167541
    require(dl > 0 or dh < 0, "quartic local uniqueness")
    left, right = lo, hi
    for _ in range(180):
        mid = (left+right)/2
        if poly(mid)*poly(left) > 0:
            left = mid
        else:
            right = mid
    with localcontext() as ctx:
        ctx.prec = 70
        beta = Decimal(left.numerator)/Decimal(left.denominator)
        p, q = (2*beta+1)/6, (5-2*beta)/12
        exponent = p + Decimal(27)/20*q
        decimals = {"B_flat": str(beta), "p": str(p), "q": str(q), "unmatched_conductor_exponent": str(2*q),
                    "marked_example_exponent": str(exponent), "marked_example_saving_below_5_over_6": str(Decimal(5)/6-exponent)}
    return {"bracket": [str(lo), str(hi)], "derivative_interval": [str(dl), str(dh)], "decimal_evaluation_not_analytic_proof": decimals}


def scalar_checks() -> dict:
    count = 0
    for beta in [F(1,2), F(2,3), F(7,8), F(11,12), F(1)]:
        p, q = (2*beta+1)/6, (5-2*beta)/12
        for value in [p+2*q-1, 1+q-p-3*q, q-p-(1-2*beta)/4]:
            require(value == 0, "exponent identity")
            count += 1
        require(q <= p, "zero-mask divisor exponent")
        count += 1
    p, q = F(11,24), F(13,48)
    require(p+F(27,20)*q == F(791,960), "marked example")
    require(F(5,6)-F(791,960) == F(3,320), "marked margin")
    require(F(1,2)+F(27,80) == F(67,80) > F(5,6), "Euler baseline comparison")
    count += 3
    # Polynomial identity: 2-F_q(1)=t^2(t-1)/(t^5-1), t=sqrt(q)>1.
    # Multiply by t^2(t^5-1), all terms are integer polynomials.
    lhs = [0]*8
    lhs[5] += 1; lhs[0] -= 1  # t^5-1
    lhs[4] -= 1; lhs[0] += 1  # -(t^4-1)
    rhs = [0]*8
    rhs[5] += 1; rhs[4] -= 1  # t^4(t-1)
    require(lhs == rhs, "all-prime local factor identity")
    count += 1
    # Full cube-inversion identity at every tested local valuation.
    for n in range(25):
        a = Counter()
        if n % 3 in (0, 1):
            a[n//3] += 1
        if n >= 3 and (n-3) % 3 in (0, 1):
            a[1+(n-3)//3] -= 1
        a = {k:v for k,v in a.items() if v}
        require(a == ({0:1} if n in (0,1) else {}), f"cube inversion at valuation {n}")
        count += 1
    # Every nontrivial local sixth-order type; the matching type is exactly four.
    table = []
    for e in range(1, 6):
        theta, completion = (e+2)%6, 3*e%6
        require((theta == 0) == (e == 4), "sixth-order resonance")
        require(completion in (0, 3), "quadratic completion")
        table.append({"psi_exponent":e,"dual_exponent":theta,"completion_exponent":completion,"matching":theta==0})
        count += 2
    return {"exact_checks": count, "sixth_order_local_table": table,
            "rational_marked_example": {"beta":"7/8", "B_power_of_Y":"1/4", "unmatched_modulus_power_of_Y":"3/10",
            "exponent":"791/960", "saving_below_5_over_6":"3/320", "Euler_baseline":"67/80"}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mutation", choices=["forget-cubic", "cheap-quadratic", "erase-zero"])
    args = parser.parse_args()
    report = {"status":"PASS", "scope":"finite algebra and exponent identities only; not a global analytic theorem",
              "local": local_checks(args.mutation), "scalar": scalar_checks(), "root": root_checks(),
              "new_zero_free_boundary_proved":False, "independent_analytic_review":False}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
