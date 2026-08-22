#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import random
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"


@dataclass(frozen=True)
class Q2:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other):
        other = as_q2(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-as_q2(other))

    def __rsub__(self, other):
        return as_q2(other) - self

    def __mul__(self, other):
        other = as_q2(other)
        return Q2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_q2(other)
        den = other.a * other.a - 2 * other.b * other.b
        if den == 0:
            raise ZeroDivisionError
        return Q2(
            (self.a * other.a - 2 * self.b * other.b) / den,
            (self.b * other.a - self.a * other.b) / den,
        )

    def __pow__(self, n: int):
        if n < 0:
            return (Q2(1) / self) ** (-n)
        out = Q2(1)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out

    def sign(self) -> int:
        a, b = self.a, self.b
        if a == 0 and b == 0:
            return 0
        if a >= 0 and b >= 0:
            return 1
        if a <= 0 and b <= 0:
            return -1
        if a >= 0 and b < 0:
            cmp = a * a - 2 * b * b
            return 1 if cmp > 0 else (-1 if cmp < 0 else 0)
        cmp = 2 * b * b - a * a
        return 1 if cmp > 0 else (-1 if cmp < 0 else 0)

    def text(self) -> str:
        return f"({self.a})+({self.b})*sqrt(2)"


def as_q2(x) -> Q2:
    if isinstance(x, Q2):
        return x
    return Q2(Fraction(x), Fraction(0))


def convolve(p: list[Q2], q: list[Q2]) -> list[Q2]:
    out = [Q2() for _ in range(len(p) + len(q) - 1)]
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] = out[i + j] + x * y
    return out


def prefixes(q: list[Q2]) -> tuple[list[Q2], list[Q2]]:
    S: list[Q2] = []
    cur = Q2()
    for x in q:
        cur = cur + x
        S.append(cur)
    A = [Q2() for _ in range(len(q) + 1)]
    for j in range(1, len(A)):
        A[j] = sum(
            (Q2(2 ** (ell + 1)) * S[ell] for ell in range(j)),
            Q2(),
        )
    return S, A


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            composite[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
    return mu


def source_coeff(mu: list[int], mode: str) -> list[float]:
    n = len(mu) - 1
    out = [0.0] * (n + 1)
    if mode == "canonical":
        for k in range(1, n + 1):
            out[k] += 2.0 * mu[k]
            if 2 * k <= n:
                out[2 * k] -= 3.0 * mu[k]
            if 4 * k <= n:
                out[4 * k] += mu[k]
    elif mode == "star":
        for k in range(1, n + 1):
            out[k] += mu[k]
            if 2 * k <= n:
                out[2 * k] -= (1.0 + math.sqrt(2.0)) * mu[k]
            if 4 * k <= n:
                out[4 * k] += math.sqrt(2.0) * mu[k]
    else:
        raise ValueError(mode)
    return out


def scalar_at(x: float, coeff: list[float], scale: float) -> float:
    top = min(int(math.floor(x)), len(coeff) - 1)
    total = 0.0
    invx = 1.0 / math.sqrt(x)
    for q in range(2, top + 1):
        total += coeff[q] * (1.0 / math.sqrt(q) - invx)
    return scale * total


def J(x: float) -> float:
    top = int(math.floor(x))
    return sum(1.0 / math.sqrt(d) for d in range(1, top + 1)) - top / math.sqrt(x)


def canonical_forcing(x: float) -> float:
    if x < 2.0:
        return 0.0
    if x < 4.0:
        return 6.0 * J(x) - 6.0 + 9.0 / math.sqrt(2.0) - 3.0 / math.sqrt(x)
    return 6.0 * J(x) - 7.5 + 9.0 / math.sqrt(2.0)


def star_forcing(x: float) -> float:
    if x < 2.0:
        return 0.0
    if x < 4.0:
        return J(x) + 1.0 / math.sqrt(2.0) - math.sqrt(2.0 / x)
    return J(x)


def direct_renewal_check(mode: str, xmax: int = 100) -> tuple[float, float]:
    mu = mobius_sieve(xmax)
    coeff = source_coeff(mu, mode)

    def h(x: float) -> float:
        if mode == "canonical":
            return scalar_at(x, coeff, -3.0)
        return scalar_at(x, coeff, -1.0)

    forcing = canonical_forcing if mode == "canonical" else star_forcing
    max_err = 0.0
    min_force = float("inf")
    grid = [1.0 + i / 8.0 for i in range(0, 8 * (xmax - 1) + 1)]
    for x in grid:
        lhs = sum(h(x / d) / math.sqrt(d) for d in range(1, int(x) + 1))
        rhs = forcing(x)
        max_err = max(max_err, abs(lhs - rhs))
        min_force = min(min_force, rhs)
    return max_err, min_force


def critical_defect_checks(limit: int = 10000) -> dict:
    s = 0.0
    min_b = float("inf")
    min_j = None
    min_integral_lower = float("inf")
    for n in range(1, limit + 2):
        s += 1.0 / math.sqrt(n)
        if n >= 3:
            j = n - 1
            b = 2.0 * s / n - math.sqrt(j) + (j - 2.0) / math.sqrt(n)
            if b < min_b:
                min_b, min_j = b, j
            if n >= 4:
                lower = (
                    4.0 * math.sqrt(n + 1.0) / n
                    - 4.0 / n
                    - math.sqrt(n - 1.0)
                    + (n - 3.0) / math.sqrt(n)
                )
                min_integral_lower = min(min_integral_lower, lower)
                if lower <= 0.0:
                    raise AssertionError(("integral lower", j, lower))
            if b <= 0.0:
                raise AssertionError(("critical defect", j, b))
    return {
        "j_max": limit,
        "minimum_B_j_half": min_b,
        "minimum_at_j": min_j,
        "minimum_integral_lower_N_ge_4": min_integral_lower,
        "N_3_direct_value": (
            2.0 / 3.0 * (1.0 + 1.0 / math.sqrt(2.0) + 1.0 / math.sqrt(3.0))
            - math.sqrt(2.0)
        ),
    }


def minimax_checks(cases: int = 100) -> dict:
    rng = random.Random(90221)
    qstar = [Q2(1), Q2(-1, -1), Q2(0, 1)]
    lam = Q2(0, Fraction(1, 4))
    target = Q2(2, -4)
    exact_identities = 0
    bound_checks = 0

    for _ in range(cases):
        degree = rng.randint(0, 7)
        R = [Q2(1)]
        for _j in range(degree):
            R.append(Q2(Fraction(rng.randint(-4, 4), rng.randint(1, 5))))
        q = convolve(qstar, R)
        _S, A = prefixes(q)
        degree_q = len(q) - 1
        lhs = Q2()
        for k in range(2, degree_q):
            lhs += (Q2(1) - lam) * (lam ** (k - 1)) * A[k]
        lhs += (lam ** (degree_q - 1)) * A[degree_q]
        rhs = Q2(-2) * (Q2(1) - lam)
        if lhs != rhs:
            raise AssertionError((q, lhs, rhs))
        exact_identities += 1

        if not any((A[k] - target).sign() <= 0 for k in range(2, degree_q + 1)):
            raise AssertionError(("minimax bound", q, A))
        bound_checks += 1

    _S, A = prefixes(qstar)
    if A[2] != target:
        raise AssertionError(("qstar equality", A[2]))

    return {
        "random_critical_neutral_filters": cases,
        "exact_weighted_identities": exact_identities,
        "minimax_bound_checks": bound_checks,
        "minimax_numerator": target.text(),
    }


def qstar_reward_checks(nmax: int = 256) -> dict:
    q = [Q2(1), Q2(-1, -1), Q2(0, 1)]
    F = Q2()
    potential = [Q2() for _ in range(nmax + 1)]
    for n in range(1, nmax + 1):
        a = Q2(1)
        if n & (n - 1) == 0:
            j = n.bit_length() - 1
            if j < len(q):
                a = Q2(1) - q[j]
        F += a
        potential[n] = F / n

    reward = [Q2() for _ in range(nmax + 1)]
    for m in range(2, nmax + 1):
        pf = Q2()
        for k in range(1, m):
            pf += Q2(Fraction(2 * k, m * (m - 1))) * potential[k]
        reward[m] = potential[m] - pf

    if reward[2] != Q2(1, Fraction(1, 2)):
        raise AssertionError(reward[2])
    if reward[3] != Q2(Fraction(1, 3)):
        raise AssertionError(reward[3])
    tail = Q2(2, -4)
    for m in range(4, nmax + 1):
        if reward[m] != tail / (m * (m - 1)):
            raise AssertionError((m, reward[m]))

    rng = random.Random(9022101)
    sweep_checks = 0
    for N in (8, 16, 32):
        for _ in range(10):
            s = [Q2() for _ in range(N + 1)]
            for n in range(2, N + 1):
                s[n] = Q2(Fraction(rng.randint(-9, 9), rng.randint(1, 7)))
            s[1] = -sum(s[2:], Q2())

            M = [Q2() for _ in range(N + 1)]
            for n in range(N, 1, -1):
                incoming = Q2()
                for m in range(n + 1, N + 1):
                    incoming += Q2(Fraction(2 * n, m * (m - 1))) * M[m]
                M[n] = s[n] + incoming

            lhs = sum((M[m] * reward[m] for m in range(2, N + 1)), Q2())
            canonical = Q2(15) * M[2] + Q2(4) * M[3]
            rhs = Q2(0, Fraction(1, 6)) * canonical + Q2(-1, 2) * s[1]
            if lhs != rhs:
                raise AssertionError(("tail sweep", N, lhs, rhs))
            sweep_checks += 1

    return {
        "reward_rows_checked": nmax - 1,
        "tail_sweep_exact_sources": sweep_checks,
        "tail_numerator": tail.text(),
    }


def main() -> None:
    can_err, can_min = direct_renewal_check("canonical")
    star_err, star_min = direct_renewal_check("star")
    if can_err > 2e-11 or star_err > 2e-11:
        raise AssertionError((can_err, star_err))
    if can_min < -2e-12 or star_min < -2e-12:
        raise AssertionError((can_min, star_min))

    result = {
        "verdict": "PASS_X_90208_CRITICAL_BOUNDARY_ATTACK",
        "all_scale_renewals": {
            "canonical_max_error": can_err,
            "canonical_min_forcing": can_min,
            "critical_star_max_error": star_err,
            "critical_star_min_forcing": star_min,
        },
        "positive_reward_critical_defect": critical_defect_checks(),
        "critical_filter_minimax": minimax_checks(),
        "critical_star_reward": qstar_reward_checks(),
        "scope": (
            "Finite algebra and numerical mutation checks only; the proofs of "
            "L-90215/L-90220/L-90221 are analytic. No RH or final sign claim."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
