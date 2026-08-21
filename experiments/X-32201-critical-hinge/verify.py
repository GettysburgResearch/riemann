#!/usr/bin/env python3
"""Exact finite regression for L-32201/L-32202.

Uses only integer/Fraction arithmetic.  It verifies the top-half inversion
formula and the Mertens formula for finite step targets.  It deliberately does
NOT certify square-root-hinge positivity or RH.
"""

from fractions import Fraction
import json
import hashlib
from pathlib import Path


def mobius_table(n: int):
    mu = [0] * (n + 1)
    mu[1] = 1
    for m in range(2, n + 1):
        # elementary factorization; tiny verification ranges only
        x = m
        p = 2
        sign = 1
        square = False
        while p * p <= x:
            if x % p == 0:
                x //= p
                sign = -sign
                if x % p == 0:
                    square = True
                    break
                while x % p == 0:
                    x //= p
            p += 1
        if square:
            mu[m] = 0
        else:
            if x > 1:
                sign = -sign
            mu[m] = sign
    return mu


def beta(n: int, q: int) -> Fraction:
    if q > n:
        return Fraction(0)
    a, r = divmod(n, q)
    return Fraction(a * (q - 1 - r), n + 1)


def triangular_inverse(target):
    T = len(target) - 1
    c = [Fraction(0) for _ in range(T + 1)]
    for q in range(T, 1, -1):
        rhs = target[q]
        for n in range(q + 1, T + 1):
            rhs -= c[n] * beta(n, q)
        c[q] = rhs / beta(q, q)
    return c


def check_top_half():
    rows = 0
    for T in range(3, 80):
        N = T // 2
        # deterministic rational decreasing targets, with h(T+1)=0
        for mode in range(4):
            h = [Fraction(0) for _ in range(T + 2)]
            for q in range(N + 1, T + 1):
                k = T - q
                if mode == 0:
                    h[q] = Fraction(k, T)
                elif mode == 1:
                    h[q] = Fraction(k * (k + 1), T * T)
                elif mode == 2:
                    h[q] = Fraction(k + 1, q) - Fraction(1, T)
                else:
                    h[q] = sum(Fraction(1, m * m) for m in range(q, T))
            # solve only the top triangular subsystem
            c = [Fraction(0) for _ in range(T + 1)]
            for q in range(T, N, -1):
                rhs = h[q]
                for n in range(q + 1, T + 1):
                    rhs -= c[n] * beta(n, q)
                c[q] = rhs / beta(q, q)
                assert c[q] >= 0

            # independent V/S formula from L-32201
            V = [Fraction(0) for _ in range(T + 2)]
            for q in range(T, N, -1):
                V[q] = q * (h[q] - h[q + 1]) + V[q + 1]
            S = [Fraction(0) for _ in range(T + 2)]
            for q in range(N + 1, T + 1):
                S[q] = V[q] / (q * (q - 1))
            for q in range(N + 1, T + 1):
                d = S[q] - S[q + 1]
                assert (q + 1) * d == c[q]
                assert d >= 0
                rows += 1
    return rows


def check_step_mertens():
    rows = 0
    for N in range(2, 90):
        mu = mobius_table(N)
        M = [0] * (N + 1)
        for k in range(1, N + 1):
            M[k] = M[k - 1] + mu[k]

        target = [Fraction(0) for _ in range(N + 1)]
        for q in range(2, N + 1):
            target[q] = Fraction(1)
        c = triangular_inverse(target)

        for j in range(2, N + 1):
            uj = M[N // j]
            uj1 = M[N // (j + 1)] if j + 1 <= N else 0
            tail = sum(M[N // m] for m in range(j + 2, N + 1))
            formula = Fraction(
                (j + 1) * (j * uj - (j - 2) * uj1) + 2 * tail,
                j * (j - 1),
            )
            assert formula == c[j]
            rows += 1
    return rows


def main():
    top_rows = check_top_half()
    step_rows = check_step_mertens()
    result = {
        "classification": "EXACT_CRITICAL_HINGE_ALGEBRA_REPLAYED",
        "top_half_formula_rows": top_rows,
        "step_mertens_rows": step_rows,
        "proof_boundary": (
            "Exact rational algebra only. Does not certify CHS, any large-T "
            "square-root positivity scan, Carry Saturation, or RH."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
