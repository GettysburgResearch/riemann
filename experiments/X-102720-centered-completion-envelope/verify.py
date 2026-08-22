#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

A = 7.1969474790828965544102785496665681514856235652677
B = 14.587000221630856811445504220868144497660448657826


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def mobius(n):
    mu = [0] * (n + 1)
    mu[1] = 1
    primes = []
    composite = bytearray(n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = 1
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--limit", type=int, default=200000)
    args = ap.parse_args()

    completion_checks = 0
    for dim in range(1, 9):
        r = [1.0 / math.sqrt(p) for p in [2, 3, 5, 7, 11, 13, 17, 19][:dim]]

        def poly_product(signs):
            poly = {(0,) * dim: 1.0}
            for j, coeff in enumerate(signs):
                nxt = dict(poly)
                for exps, value in poly.items():
                    ee = list(exps)
                    ee[j] += 1
                    ee = tuple(ee)
                    nxt[ee] = nxt.get(ee, 0.0) + coeff * value
                poly = nxt
            return poly

        Em = poly_product([-x for x in r])
        Am = poly_product(r)
        Cm = {}
        for ea, va in Am.items():
            for ee, ve in Em.items():
                ex = tuple(a+b for a, b in zip(ea, ee))
                Cm[ex] = Cm.get(ex, 0.0) + va*ve
        lhs = dict(Cm)
        for ex, value in Em.items():
            lhs[ex] = lhs.get(ex, 0.0) - value
        rhs = {}
        for ea, va in Am.items():
            if not any(ea):
                continue
            for ee, ve in Em.items():
                ex = tuple(a+b for a, b in zip(ea, ee))
                rhs[ex] = rhs.get(ex, 0.0) + va*ve
        keys = set(lhs) | set(rhs)
        assert max(abs(lhs.get(k, 0.0)-rhs.get(k, 0.0)) for k in keys) < 1e-12
        completion_checks += 1

    kernel_checks = 0
    for k in range(1, 10001):
        y = math.exp(-12 + 24 * k / 10001)
        R = 24 * math.sqrt(y) - 16 * y if y < 1 else 9.0
        assert R > 0
        kernel_checks += 1

    mellin_checks = 0
    for s in [0.1, 0.2, 0.3, 0.4]:
        direct = 24 / (0.5 - s) - 16 / (1 - s) + 9 / s
        closed = (2*s*s + 5*s + 9) / (s*(s-1)*(2*s-1))
        assert abs(direct - closed) < 1e-10
        mellin_checks += 1

    limit = args.limit
    mu = mobius(limit)
    beta = [0] * (limit + 1)
    for n in range(1, limit + 1):
        beta[n] = mu[n] - (mu[n // 67] if n % 67 == 0 else 0)

    mmax = int(math.isqrt(limit))
    s1_small = [0.0] * (mmax + 1)
    s2_small = [0.0] * (mmax + 1)
    s3_small = [0.0] * (mmax + 1)
    for n in range(1, mmax + 1):
        bn = beta[n]
        s1_small[n] = s1_small[n-1] + bn / n
        s2_small[n] = s2_small[n-1] + bn / (n*n)
        s3_small[n] = s3_small[n-1] + bn / (n*n*n)

    s05 = s1 = s15 = 0.0
    minimum = float("inf")
    argmin = 0
    qgamma_min = float("inf")
    for X in range(1, limit + 1):
        bn = beta[X]
        sx = math.sqrt(X)
        s05 += bn / sx
        s1 += bn / X
        s15 += bn / (X * sx)
        m = math.isqrt(X)
        q_native = 16*X*s15 - 24*sx*s1 + 9*s05
        q_square = 16*X*s3_small[m] - 24*sx*s2_small[m] + 9*s1_small[m]
        qgamma = q_square - q_native
        envelope = qgamma - A*X + B*sx
        qgamma_min = min(qgamma_min, qgamma)
        if envelope < minimum:
            minimum = envelope
            argmin = X

    assert qgamma_min > -1e-8
    assert minimum > 4.0

    payload = {
        "schema": "riemann.t102720.centered-completion-envelope.v1",
        "completion_dimension_checks": completion_checks,
        "kernel_positivity_checks": kernel_checks,
        "mellin_checks": mellin_checks,
        "diagnostic_limit": limit,
        "diagnostic_minimum": minimum,
        "diagnostic_argmin": argmin,
        "quadratic_completion_minimum": qgamma_min,
        "diagnostic_only": True,
        "cce102721_proved": False,
        "phdnc102710_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102720_CENTERED_COMPLETION_ENVELOPE",
    }
    payload["proof_object_sha256"] = digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
