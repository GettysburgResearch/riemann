#!/usr/bin/env python3
"""Directed exact replay for the X=14 critical Pascal occupation firewall."""
from __future__ import annotations
from fractions import Fraction
import hashlib, json, math
from pathlib import Path

STATUS = "PASS_X_90703_CRITICAL_OCCUPATION_FIREWALL"


def mobius(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    lp = [0] * (n + 1)
    primes: list[int] = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if p > lp[i] or i * p > n:
                break
            lp[i * p] = p
            mu[i * p] = 0 if p == lp[i] else -mu[i]
    return mu


def occupation_functionals(X: int) -> list[list[Fraction]]:
    mu = mobius(X)
    U = [[Fraction(0) for _ in range(X + 1)] for _ in range(X + 2)]
    for n in range(1, X + 1):
        for k in range(1, X // n + 1):
            U[n][n * k] += mu[k]
    s = [[Fraction(0) for _ in range(X + 1)] for _ in range(X + 1)]
    for n in range(1, X + 1):
        for q in range(1, X + 1):
            s[n][q] = n * (U[n][q] - U[n + 1][q])
    tail = [[Fraction(0) for _ in range(X + 1)] for _ in range(X + 2)]
    for n in range(X, 0, -1):
        for q in range(1, X + 1):
            tail[n][q] = tail[n + 1][q] + s[n][q]
    M = [[Fraction(0) for _ in range(X + 1)] for _ in range(X + 1)]
    for n in range(1, X + 1):
        for q in range(1, X + 1):
            M[n][q] = s[n][q] + Fraction(2, n + 1) * tail[n + 1][q]
    return M


def invsqrt_bounds(n: int, digits: int = 70) -> tuple[Fraction, Fraction]:
    scale = 10**digits
    a = math.isqrt(scale * scale // n)
    assert a * a * n <= scale * scale < (a + 1) * (a + 1) * n
    lo = Fraction(a, scale)
    hi = lo if a * a * n == scale * scale else Fraction(a + 1, scale)
    return lo, hi


def log_bounds(a: int, b: int, terms: int = 120) -> tuple[Fraction, Fraction]:
    if a == b:
        return Fraction(0), Fraction(0)
    if a < b:
        lo, hi = log_bounds(b, a, terms)
        return -hi, -lo
    y = Fraction(a - b, a + b)
    power = y
    total = Fraction(0)
    for k in range(terms):
        total += power / (2 * k + 1)
        power *= y * y
    lo = 2 * total
    tail = 2 * power / ((2 * terms + 1) * (1 - y * y))
    return lo, lo + tail


def w_bounds(X: int, q: int) -> tuple[Fraction, Fraction]:
    il, ih = invsqrt_bounds(q)
    ll, lh = log_bounds(X, q)
    assert ll >= 0
    return il * ll, ih * lh


def evaluate(coeffs: list[Fraction], X: int) -> tuple[Fraction, Fraction]:
    lo = Fraction(0)
    hi = Fraction(0)
    for q, c in enumerate(coeffs):
        if not c:
            continue
        wl, wh = w_bounds(X, q)
        if c >= 0:
            lo += c * wl
            hi += c * wh
        else:
            lo += c * wh
            hi += c * wl
    return lo, hi


def decimal(x: Fraction, digits: int = 40) -> str:
    sign = "-" if x < 0 else ""
    x = abs(x)
    integer, rem = divmod(x.numerator, x.denominator)
    out = [sign + str(integer), "."]
    for _ in range(digits):
        rem *= 10
        digit, rem = divmod(rem, x.denominator)
        out.append(str(digit))
    return "".join(out)


def serialize(coeffs: list[Fraction]) -> str:
    return ";".join(
        f"{q}:{c.numerator}/{c.denominator}"
        for q, c in enumerate(coeffs) if c
    )


def main() -> dict[str, object]:
    X = 14
    M = occupation_functionals(X)
    intervals = {}
    positive_indices = []
    for n in range(2, X):
        coeffs = [M[n + 1][q] - M[n][q] for q in range(X + 1)]
        lo, hi = evaluate(coeffs, X)
        intervals[n] = (lo, hi, coeffs)
        if lo > 0:
            positive_indices.append(n)
        elif hi >= 0:
            raise AssertionError(("unresolved sign", n, lo, hi))

    if positive_indices != [6]:
        raise AssertionError(("upward locations", positive_indices))

    up_lo, up_hi, up_coeffs = intervals[6]
    m2_lo, m2_hi = evaluate(M[2], X)
    gates = {
        "critical_occupation_not_monotone": up_lo > Fraction(13, 1000),
        "only_one_upward_step": positive_indices == [6],
        "upward_variation_small": up_hi < Fraction(14, 1000),
        "M2_positive_large": m2_lo > Fraction(19, 10),
        "factor64_variation_gate_has_slack": 4 * up_hi < 3 * m2_lo,
    }
    if not all(gates.values()):
        raise AssertionError([k for k, v in gates.items() if not v])

    result = {
        "status": STATUS,
        "gates": gates,
        "X": X,
        "upward_step": {
            "index": 6,
            "quantity": "M(7)-M(6)",
            "lower": decimal(up_lo),
            "upper": decimal(up_hi),
            "functional": serialize(up_coeffs),
            "functional_sha256": hashlib.sha256(serialize(up_coeffs).encode()).hexdigest(),
        },
        "M2": {"lower": decimal(m2_lo), "upper": decimal(m2_hi)},
        "upward_variation_over_M2_upper": decimal(up_hi / m2_lo, 40),
        "adjacent_signs": {
            str(n): ("positive" if intervals[n][0] > 0 else "negative")
            for n in range(2, X)
        },
        "scope": "exact X=14 firewall only; no cofinal variation theorem or RH",
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


if __name__ == "__main__":
    result = main()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(STATUS)
