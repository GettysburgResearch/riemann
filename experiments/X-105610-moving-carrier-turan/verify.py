#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction as Q
from math import factorial
import hashlib
import json
from pathlib import Path
import sys

N = 96


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def conv(f: list[Q], g: list[Q]) -> list[Q]:
    out = [Q(0) for _ in range(N + 1)]
    for n in range(1, N + 1):
        out[n] = sum((f[d] * g[n // d] for d in divisors(n)), Q(0))
    return out


def p_add(*ps: dict[int, Q]) -> dict[int, Q]:
    out: dict[int, Q] = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, Q(0)) + v
    return {k: v for k, v in out.items() if v}


def p_scale(p: dict[int, Q], a: Q) -> dict[int, Q]:
    return {k: a * v for k, v in p.items() if a * v}


def p_u(p: dict[int, Q]) -> dict[int, Q]:
    return {k + 1: v for k, v in p.items()}


def cadd(z, w): return (z[0] + w[0], z[1] + w[1])
def csub(z, w): return (z[0] - w[0], z[1] - w[1])
def cmul(z, w): return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])
def cconj(z): return (z[0], -z[1])
def cscale(a, z): return (a * z[0], a * z[1])
def cnorm2(z): return z[0] * z[0] + z[1] * z[1]


def cdiv(z, w):
    d = cnorm2(w)
    return ((z[0] * w[0] + z[1] * w[1]) / d,
            (z[1] * w[0] - z[0] * w[1]) / d)


def poly_eval(coeff: list[Q], z):
    out = (Q(0), Q(0))
    for a in reversed(coeff):
        out = cadd(cmul(out, z), (a, Q(0)))
    return out


def derivative(coeff: list[Q]) -> list[Q]:
    return [Q(i) * coeff[i] for i in range(1, len(coeff))]


def main(output: str) -> None:
    checks: list[str] = []

    delta = [Q(0)] * (N + 1)
    delta[1] = Q(1)
    a = [Q(0)] * (N + 1)
    for n, value in {
        2: 2, 3: 3, 4: 5, 5: 7, 6: 11,
        7: 13, 8: 17, 9: 19, 10: 23,
    }.items():
        a[n] = Q(value)

    prime_weight = {2: 1, 3: 2, 5: 3, 7: 5, 11: 7, 13: 11}

    def ell(n: int) -> int:
        x, total = n, 0
        while x > 1:
            p = x
            for q in range(2, int(x ** 0.5) + 2):
                if x % q == 0:
                    p = q
                    break
            while x % p == 0:
                total += prime_weight.get(p, p)
                x //= p
        return total

    for m in range(1, 13):
        for n in range(1, 13):
            if m * n <= N:
                assert ell(m * n) == ell(m) + ell(n)
                checks.append(f"additive_log_{m}_{n}")

    powers = [delta]
    for _ in range(1, 8):
        powers.append(conv(powers[-1], a))

    c: list[dict[int, Q]] = [{} for _ in range(N + 1)]
    for k, power in enumerate(powers):
        for n in range(1, N + 1):
            if power[n]:
                c[n][k] = power[n] / Q(factorial(k))

    alog = [Q(0)] * (N + 1)
    for n in range(1, N + 1):
        alog[n] = Q(ell(n)) * a[n]
    for n in range(1, N + 1):
        lhs: dict[int, Q] = {}
        for d in divisors(n):
            if alog[d]:
                lhs = p_add(lhs, p_scale(p_u(c[n // d]), alog[d]))
        rhs = p_scale(c[n], Q(ell(n)))
        assert lhs == rhs
        checks.append(f"dirichlet_exponential_derivative_{n}")

    L = Q(7)
    Lp = Q(2, 5)
    h = Q(3, 4)

    q = [Q(0)] * (N + 1)
    for k, power in enumerate(powers):
        for n in range(1, N + 1):
            q[n] += power[n] / (L ** (k + 1))

    bprime = [Q(0)] * (N + 1)
    bprime[1] = Lp
    for n in range(2, N + 1):
        bprime[n] = alog[n]

    qprime = [-x for x in conv(conv(q, bprime), q)]
    direct = [q[n] - h * qprime[n] for n in range(N + 1)]

    def laplace_polynomial(p: dict[int, Q]) -> Q:
        return sum((v * Q(factorial(k)) / (L ** (k + 1))
                    for k, v in p.items()), Q(0))

    for n in range(1, N + 1):
        integrand = p_add(
            p_scale(c[n], Q(1) + h * Q(ell(n))),
            p_scale(p_u(c[n]), h * Lp),
        )
        assert direct[n] == laplace_polynomial(integrand)
        checks.append(f"moving_carrier_laplace_{n}")

    assert q[2] == a[2] / (L * L)
    checks.append("prime_two_resolvent_coefficient")

    fixtures = [
        ([1, 2, -3, 1], (Q(2, 3), Q(1, 2))),
        ([4, 0, -5, 0, 1], (Q(1, 3), Q(2, 5))),
        ([1, -1, 2, -2, 1], (Q(3, 4), Q(1, 3))),
    ]
    for j, (raw, z) in enumerate(fixtures):
        coeff = [Q(x) for x in raw]
        F = poly_eval(coeff, z)
        D = poly_eval(derivative(coeff), z)
        D2 = poly_eval(derivative(derivative(coeff)), z)
        T = csub(cmul(D, D), cmul(F, D2))
        J = cmul(F, cconj(D))[1]
        m = cdiv(F, D)
        assert m[1] != 0 and J != 0 and cnorm2(D) != 0
        mp = cdiv(T, cmul(D, D))
        hyper = cscale(z[1] / m[1], mp)
        factored = cscale(z[1] / J, cmul(T, cdiv(cconj(D), D)))
        assert hyper == factored
        assert cnorm2(hyper) == z[1] * z[1] * cnorm2(T) / (J * J)
        checks.extend([
            f"turan_hyperbolic_factorization_{j}",
            f"turan_hyperbolic_modulus_{j}",
        ])

    freqs = list(range(-4, 5))
    phi = {u: Q(5 - abs(u), 7) for u in freqs}
    positive = 0
    for xi in range(-8, 9):
        direct_coeff = Q(0)
        square_coeff = Q(0)
        for u in freqs:
            v = xi - u
            if v in phi:
                direct_coeff += Q(v * v - u * v) * phi[u] * phi[v]
                square_coeff += Q((u - v) * (u - v), 2) * phi[u] * phi[v]
        assert direct_coeff == square_coeff
        assert square_coeff >= 0
        positive += int(square_coeff > 0)
        checks.append(f"exterior_square_density_{xi}")
    assert positive == 15
    checks.append("exterior_square_strict_support_count")

    payload = {
        "arithmetic_class": "EXACT_RATIONAL_FINITE_DIRICHLET_AND_TURAN_ALGEBRA",
        "checks": len(checks),
        "moving_carrier_laplace_identity_replayed": True,
        "dirichlet_exponential_positivity_replayed": True,
        "turan_hyperbolic_factorization_replayed": True,
        "exterior_square_density_replayed": True,
        "one_sided_physical_transfer_proved": False,
        "xi_pointwise_microscope_sign_proved": False,
        "rh_established": False,
        "verdict": "PASS_X_105610_MOVING_CARRIER_TURAN_BRIDGE",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object"] = hashlib.sha256(canonical).hexdigest()

    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["verdict"])
    print(f"checks={payload['checks']}")
    print(payload["proof_object"])
    print("RH_UNPROVEN")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py OUTPUT_JSON")
    main(sys.argv[1])
