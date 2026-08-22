#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def mul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = tuple(x + y for x, y in zip(ka, kb))
            out[key] = out.get(key, Fraction(0)) + va * vb
    return {k: v for k, v in out.items() if v}


def scale(a, c):
    return {k: c * v for k, v in a.items() if c * v}


def factor(dim, i, c, power=1):
    z = (0,) * dim
    e = list(z)
    e[i] = power
    return {z: Fraction(1), tuple(e): c}


def product(fs, dim):
    out = {(0,) * dim: Fraction(1)}
    for f in fs:
        out = mul(out, f)
    return out


def prime_sieve(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n-p*p)//p)+1)
    return [i for i in range(2, n+1) if sieve[i]]


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    prefix_checks = 0
    duhamel_checks = 0

    rs = [Fraction(1, 2), Fraction(1, 3), Fraction(2, 5), Fraction(1, 7)]
    for dim in range(1, 5):
        r = rs[:dim]
        E = {(0,) * dim: Fraction(1)}
        A = {(0,) * dim: Fraction(1)}
        C = {(0,) * dim: Fraction(1)}

        for j in range(dim):
            Eprev, Aprev, Cprev = E, A, C
            minus = factor(dim, j, -r[j])
            plus = factor(dim, j, r[j])
            E = mul(Eprev, minus)
            A = mul(Aprev, plus)
            C = mul(Cprev, factor(dim, j, -(r[j] ** 2), power=2))

            owner = mul(Aprev, add(E, scale(Eprev, -1)))
            transfer = mul(add(A, scale(Aprev, -1)), Eprev)
            assert add(owner, transfer) == {}

            simultaneous = add(C, scale(Cprev, -1))
            expected = {}
            for mon, coeff in Cprev.items():
                e = list(mon)
                e[j] += 2
                expected[tuple(e)] = -r[j] ** 2 * coeff
            assert simultaneous == expected
            prefix_checks += 1

        assert C == mul(A, E)

        # Duhamel identity, integrating the t-polynomial exactly.
        # Represent t-degree separately.
        defect = add(E, scale(C, -1))
        integ = {}
        for j in range(dim):
            # A_{t, !=j} E = sum_T t^|T| r_T x_T * E.
            others = [i for i in range(dim) if i != j]
            for mask in range(1 << len(others)):
                tdeg = 0
                mon = [0] * dim
                coeff = r[j]
                mon[j] += 1
                for pos, i in enumerate(others):
                    if (mask >> pos) & 1:
                        tdeg += 1
                        mon[i] += 1
                        coeff *= r[i]
                shifted = {tuple(mon): coeff}
                term = mul(shifted, E)
                term = scale(term, -Fraction(1, tdeg + 1))
                integ = add(integ, term)
        assert integ == defect
        duhamel_checks += 1

    # Prime-power tail fixture.
    Y = 10**6
    ps = prime_sieve(int(math.sqrt(Y)))
    weighted = 0.0
    unweighted = 0.0
    for p in ps:
        k = 2
        while p**k <= Y:
            weighted += math.log(p) * p ** (-k / 2)
            unweighted += p ** (-k / 2)
            k += 1
    assert weighted < 3.0 * math.log(Y)
    assert unweighted < 10.0 * math.log(math.log(Y))

    # Finite multiplier identity for labelled ordinary primes plus duplicate 67.
    zs = [1.2 + 0.3j, 1.7 + 1.1j, 2.1 + 0.4j]
    multiplier_checks = 0
    finite_primes = [2, 3, 5, 7, 67]
    for z in zs:
        native = 1.0 + 0j
        comp = 1.0 + 0j
        for p in finite_primes:
            native *= 1 - p ** (-z)
            comp *= 1 - p ** (-2 * z)
        native *= 1 - 67 ** (-z)
        comp *= 1 - 67 ** (-2 * z)
        completion = 1.0 + 0j
        for p in finite_primes:
            completion *= 1 + p ** (-z)
        completion *= 1 + 67 ** (-z)
        assert abs(native * completion - comp) < 1e-12
        multiplier_checks += 1

    equal_owner_checks = 0
    for k in range(1, 9):
        total = sum(Fraction((-1) ** k, k) for _ in range(k))
        assert total == Fraction((-1) ** k, 1)
        equal_owner_checks += 1

    payload = {
        "schema": "riemann.t102600.completion-defect.v1",
        "prefix_cancellation_checks": prefix_checks,
        "duhamel_checks": duhamel_checks,
        "multiplier_checks": multiplier_checks,
        "equal_owner_checks": equal_owner_checks,
        "prime_power_weighted_fixture": weighted,
        "prime_power_unweighted_fixture": unweighted,
        "ar_defect102600_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102600_COMPLETION_DEFECT_REDUCTION",
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
