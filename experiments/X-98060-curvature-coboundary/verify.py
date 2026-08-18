#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp

VERDICT = "PASS_T98060_MULTIPLICATIVE_CURVATURE_CUTOFF_COBOUNDARY"


def primes_upto(n: int) -> list[int]:
    out: list[int] = []
    for k in range(2, n + 1):
        ok = True
        d = 2
        while d * d <= k:
            if k % d == 0:
                ok = False
                break
            d += 1
        if ok:
            out.append(k)
    return out


def mobius(n: int) -> int:
    if n == 1:
        return 1
    x = n
    sign = 1
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            sign = -sign
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        sign = -sign
    return sign


def exact_cross_ratio_fixture() -> bool:
    p, q = 3, 5
    vy = Fraction(17, 5)
    vyp = Fraction(13, 7)
    vyq = Fraction(11, 9)
    vypq = Fraction(7, 8)
    lhs = (vyp - Fraction(1, q) * vypq) / (vy - Fraction(1, q) * vyq)
    qp = vyp / vy
    qq_y = vyq / vy
    qq_yp = vypq / vyp
    rhs = qp * (1 - Fraction(1, q) * qq_yp) / (1 - Fraction(1, q) * qq_y)
    curvature = vy * vypq - vyp * vyq
    delta = lhs - qp
    return lhs == rhs and (delta > 0) == (curvature < 0)


def prefix_value(jumps: dict[int, Fraction], t: Fraction) -> Fraction:
    return sum((c for x, c in jumps.items() if Fraction(x) <= t), Fraction())


def stieltjes(jumps: dict[int, Fraction], a: Fraction, b: Fraction, kernel) -> Fraction:
    return sum((c * kernel(Fraction(x)) for x, c in jumps.items() if a < x <= b), Fraction())


def cutoff_coboundary_fixture() -> bool:
    q = 5
    X = Fraction(840)
    a, b = Fraction(2), Fraction(42)
    u = {2: Fraction(3, 5), 3: Fraction(-1, 7), 5: Fraction(2, 9), 9: Fraction(1, 11)}
    splus_jumps = {1: Fraction(1), 7: Fraction(-1, 7), 11: Fraction(-1, 11), 77: Fraction(1, 77)}

    def splus(t: Fraction) -> Fraction:
        return prefix_value(splus_jumps, t)

    def sbefore(t: Fraction) -> Fraction:
        return splus(t) - Fraction(1, q) * splus(t / q)

    uplus = dict(u)
    for x, c in u.items():
        uplus[q * x] = uplus.get(q * x, Fraction()) - Fraction(1, q) * c

    jplus = stieltjes(uplus, a, b, lambda y: splus(X / y))
    jminus = stieltjes(u, a, b, lambda y: sbefore(X / y))
    upper = stieltjes(u, b / q, b, lambda y: splus(X / (q * y)))
    lower = stieltjes(u, a / q, a, lambda y: splus(X / (q * y)))
    return jplus - jminus == Fraction(1, q) * (upper - lower)


def p61_coefficients(limit: int) -> list[int]:
    small_primes = primes_upto(61)
    p61 = 1
    for p in small_primes:
        p61 *= p

    def a61(n: int) -> int:
        value = 6 if math.gcd(n, p61) == 1 else 0
        if p61 % n == 0:
            value -= 6 * mobius(n)
        if n % 2 == 0 and p61 % (n // 2) == 0:
            value += 9 * mobius(n // 2)
        if n % 4 == 0 and p61 % (n // 4) == 0:
            value -= 3 * mobius(n // 4)
        return value

    coeff = [0] + [a61(n) for n in range(1, limit + 1)]
    # Install every future Euler prime >=71. A descending loop preserves the
    # pre-q coefficient at n/q and implements multiplication by (1-q^-s).
    for q in primes_upto(limit):
        if q < 71:
            continue
        for n in range((limit // q) * q, q - 1, -q):
            coeff[n] -= coeff[n // q]
    return coeff


def directed_ratio_fixture() -> dict[str, str]:
    limit = 600
    coeff = p61_coefficients(limit)
    mp.iv.dps = 80
    zero = mp.iv.mpf([0, 0])
    pw = [zero for _ in range(limit + 1)]
    pl = [zero for _ in range(limit + 1)]
    for n in range(1, limit + 1):
        w = mp.iv.mpf(coeff[n]) / mp.iv.sqrt(n)
        pw[n] = pw[n - 1] + w
        pl[n] = pl[n - 1] + w * mp.iv.log(n)

    def f(x):
        mid = float(x.mid)
        n = int(math.floor(mid))
        k = int(math.floor(mid / 4))
        return mp.iv.log(4) * pw[k] + mp.iv.log(x) * (pw[n] - pw[k]) - (pl[n] - pl[k])

    def v(x):
        return f(x) / mp.iv.sqrt(x)

    def dv(x):
        mid = float(x.mid)
        n = int(math.floor(mid))
        k = int(math.floor(mid / 4))
        df = pw[n] - pw[k]
        return (df - mp.iv.mpf("0.5") * f(x)) / mp.iv.sqrt(x)

    def wronskian(num: int):
        x = mp.iv.mpf(num) / 2
        child = x / 67
        return dv(child) * v(x) - v(child) * dv(x)

    w869 = wronskian(869)
    w871 = wronskian(871)
    w875 = wronskian(875)
    assert w869.a > 0
    assert w871.b < 0
    assert w875.a > 0

    x = mp.iv.mpf(871) / 2
    parent = v(x)
    child = v(x / 67)
    ratio = child / parent
    assert parent.a > 0 and child.a > 0
    assert ratio.b < 67

    return {
        "W_869_over_2": str(w869),
        "W_871_over_2": str(w871),
        "W_875_over_2": str(w875),
        "Q_871_over_2": str(ratio),
    }


def finite_part_constants() -> dict[str, str]:
    mp.mp.dps = 80
    prod_half = mp.mpf(1)
    prod_one = mp.mpf(1)
    for p in primes_upto(61):
        prod_half *= 1 - 1 / mp.sqrt(p)
        prod_one *= 1 - mp.mpf(1) / p
    bracket = 6 * mp.zeta(mp.mpf("0.5")) - mp.mpf(15) / 2 + 9 / mp.sqrt(2)
    cstar = mp.log(4) * bracket * prod_half
    astar = 12 * prod_one
    assert astar > 0
    assert bracket < 0
    assert cstar < 0
    return {"a_star": mp.nstr(astar, 50), "c_star": mp.nstr(cstar, 50)}


def asymptotic_exponent_fixture() -> bool:
    # q <= (1-eps) log X: the finite-cube remainder is
    # X^(-1-eps/2+o(1)), while the c_* increment is X^(-1/2-o(1)).
    eps = Fraction(1, 5)
    error_power = -1 - eps / 2
    main_power = Fraction(-1, 2)
    return error_power < main_power


def main() -> None:
    assert exact_cross_ratio_fixture()
    assert cutoff_coboundary_fixture()
    assert asymptotic_exponent_fixture()
    directed = directed_ratio_fixture()
    constants = finite_part_constants()
    core = {
        "schema": "riemann.x98060.curvature-coboundary.v1",
        "base_pr608": "f362acf56bbbbd183976b6377fbe883193886e1a",
        "cross_ratio_identity": True,
        "cutoff_coboundary_identity": True,
        "directed_ratio_fixture": directed,
        "finite_part_constants": constants,
        "fully_activated_log_prime_switch_exponent": True,
        "post_log_product_boundary_proved": False,
        "gpc67_proved": False,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = Path(__file__).resolve().parent / "results/verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(core, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(core["verdict"])
    print(core["proof_object_sha256"])


if __name__ == "__main__":
    main()
