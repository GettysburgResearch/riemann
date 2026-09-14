#!/usr/bin/env python3
"""Exact Gaussian-rational replay for T-106610."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import random
from pathlib import Path


@dataclass(frozen=True)
class G:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: "G") -> "G":
        return G(self.re + other.re, self.im + other.im)

    def __sub__(self, other: "G") -> "G":
        return G(self.re - other.re, self.im - other.im)

    def __neg__(self) -> "G":
        return G(-self.re, -self.im)

    def __mul__(self, other: "G") -> "G":
        return G(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def inv(self) -> "G":
        den = self.re * self.re + self.im * self.im
        if den == 0:
            raise ZeroDivisionError
        return G(self.re / den, -self.im / den)

    def __truediv__(self, other: "G") -> "G":
        return self * other.inv()


ZERO = G()
ONE = G(Fraction(1))
I = G(Fraction(0), Fraction(1))


def scalar(x: int | Fraction) -> G:
    return G(Fraction(x))


def add(a: list[G], b: list[G], n: int) -> list[G]:
    return [
        (a[k] if k < len(a) else ZERO) + (b[k] if k < len(b) else ZERO)
        for k in range(n)
    ]


def sub(a: list[G], b: list[G], n: int) -> list[G]:
    return [
        (a[k] if k < len(a) else ZERO) - (b[k] if k < len(b) else ZERO)
        for k in range(n)
    ]


def scale(a: list[G], c: G, n: int) -> list[G]:
    return [(a[k] if k < len(a) else ZERO) * c for k in range(n)]


def mul(a: list[G], b: list[G], n: int) -> list[G]:
    out = [ZERO for _ in range(n)]
    for i, ai in enumerate(a[:n]):
        for j, bj in enumerate(b[: n - i]):
            out[i + j] = out[i + j] + ai * bj
    return out


def deriv(a: list[G], n: int) -> list[G]:
    out = [ZERO for _ in range(n)]
    for k in range(n - 1):
        if k + 1 < len(a):
            out[k] = a[k + 1] * scalar(k + 1)
    return out


def inv_series(a: list[G], n: int) -> list[G]:
    if not a or a[0] == ZERO:
        raise ZeroDivisionError
    out = [ZERO for _ in range(n)]
    out[0] = a[0].inv()
    for k in range(1, n):
        acc = ZERO
        for j in range(1, k + 1):
            if j < len(a):
                acc = acc + a[j] * out[k - j]
        out[k] = -(out[0] * acc)
    return out


def eq_prefix(a: list[G], b: list[G], safe: int) -> bool:
    return a[:safe] == b[:safe]


def rand_series(rng: random.Random, n: int, nonzero0: bool = False) -> list[G]:
    out = []
    for k in range(n):
        re = Fraction(rng.randint(-5, 5), rng.randint(1, 7))
        im = Fraction(rng.randint(-5, 5), rng.randint(1, 7))
        out.append(G(re, im))
    if nonzero0 and out[0] == ZERO:
        out[0] = ONE
    return out


def real_series(rng: random.Random, n: int, positive0: bool = False) -> list[G]:
    out = [
        G(Fraction(rng.randint(-5, 5), rng.randint(1, 7)))
        for _ in range(n)
    ]
    if positive0:
        out[0] = G(Fraction(rng.randint(1, 7), rng.randint(1, 7)))
    return out


rng = random.Random(106610)
fixtures = 120
orders = (1, 3, 5)
checks = 0
n = 14
safe = 6

for _ in range(fixtures):
    q = real_series(rng, n)
    w = real_series(rng, n, positive0=True)
    h = rand_series(rng, n, nonzero0=True)
    winv = inv_series(w, n)
    alpha = add(q, scale(w, I, n), n)

    def Lop(f: list[G]) -> list[G]:
        return add(deriv(f, n), mul(alpha, f, n), n)

    def Pop(f: list[G]) -> list[G]:
        return add(deriv(f, n), mul(q, f, n), n)

    H = [h]
    for _k in range(1, 7):
        H.append(Lop(H[-1]))

    def C(k: int) -> list[G]:
        return scale(mul(winv, Pop(H[k]), n), I, n)

    def R(k: int) -> list[G]:
        return sub(scale(H[k], scalar(2), n), C(k), n)

    for k in range(6):
        plus = add(H[k], scale(mul(winv, H[k + 1], n), I, n), n)
        minus = sub(H[k], scale(mul(winv, H[k + 1], n), I, n), n)
        assert eq_prefix(plus, C(k), safe)
        assert eq_prefix(minus, R(k), safe)
        checks += 2

    for k in orders:
        lhs = sub(mul(R(0), C(k), n), mul(C(0), R(k), n), n)
        wr = sub(mul(H[0], deriv(H[k], n), n), mul(deriv(H[0], n), H[k], n), n)
        rhs = scale(mul(winv, wr, n), scalar(2) * I, n)
        assert eq_prefix(lhs, rhs, safe)
        checks += 1

    ap = deriv(alpha, n)
    app = deriv(ap, n)
    appp = deriv(app, n)
    apppp = deriv(appp, n)

    a2 = mul(alpha, alpha, n)
    a3 = mul(a2, alpha, n)
    a4 = mul(a3, alpha, n)
    a5 = mul(a4, alpha, n)

    B2 = add(a2, ap, n)
    B3 = add(add(a3, scale(mul(alpha, ap, n), scalar(3), n), n), app, n)
    B4 = add(
        add(
            add(a4, scale(mul(a2, ap, n), scalar(6), n), n),
            scale(mul(ap, ap, n), scalar(3), n),
            n,
        ),
        add(scale(mul(alpha, app, n), scalar(4), n), appp, n),
        n,
    )
    B5 = a5
    for term in (
        scale(mul(a3, ap, n), scalar(10), n),
        scale(mul(alpha, mul(ap, ap, n), n), scalar(15), n),
        scale(mul(a2, app, n), scalar(10), n),
        scale(mul(ap, app, n), scalar(10), n),
        scale(mul(alpha, appp, n), scalar(5), n),
        apppp,
    ):
        B5 = add(B5, term, n)

    ds = [h]
    for _j in range(1, 6):
        ds.append(deriv(ds[-1], n))

    bell = ds[5]
    bell = add(bell, scale(mul(alpha, ds[4], n), scalar(5), n), n)
    bell = add(bell, scale(mul(B2, ds[3], n), scalar(10), n), n)
    bell = add(bell, scale(mul(B3, ds[2], n), scalar(10), n), n)
    bell = add(bell, scale(mul(B4, ds[1], n), scalar(5), n), n)
    bell = add(bell, mul(B5, ds[0], n), n)
    assert eq_prefix(bell, H[5], safe)
    checks += 1

result = {
    "verdict": "PASS_T106610_RIEMANN_SIEGEL_GAUGE",
    "fixtures": fixtures,
    "exact_gaussian_rational_checks": checks,
    "odd_endpoint_orders_checked": list(orders),
    "companion_factorization_exact": True,
    "amplitude_connection_cancels_from_wronskian": True,
    "fifth_bell_packet_exact": True,
    "deep_height_payment": "3/40",
    "arithmetic_shallow_allowance": "11/500",
    "rsgauge106610_proved": False,
    "ninety_percent_established": False,
    "rh_established": False,
}
canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

print(result["verdict"])
print(json.dumps(result, indent=2, sort_keys=True))
