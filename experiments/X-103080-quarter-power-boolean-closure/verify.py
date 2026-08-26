#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def powerset(n: int):
    for mask in range(1 << n):
        yield frozenset(i for i in range(n) if (mask >> i) & 1)


def star(f, g, subsets):
    out = {}
    for s in subsets:
        elems = list(s)
        total = Fraction(0)
        for mask in range(1 << len(elems)):
            a = frozenset(
                elems[j] for j in range(len(elems)) if (mask >> j) & 1
            )
            b = s - a
            total += f[a] * g[b]
        out[s] = total
    return out


def digest(payload):
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    prime_sets = [
        [2, 3, 5, 7],
        [2, 3, 5, 7, 11],
        [2, 3, 5, 7, 11, 13],
        [2, 3, 5, 7, 11, 13, 17],
    ]

    boolean_checks = 0
    cutoff_transfer_checks = 0
    half_source_checks = 0

    for primes in prime_sets:
        n = len(primes)
        subsets = list(powerset(n))

        def product(s):
            out = 1
            for i in s:
                out *= primes[i]
            return out

        eps = {s: Fraction(1 if not s else 0) for s in subsets}
        one = {s: Fraction(1) for s in subsets}
        mu = {s: Fraction((-1) ** len(s)) for s in subsets}
        h = {
            s: Fraction((-1) ** len(s), 2 ** len(s))
            for s in subsets
        }

        def rows(u):
            mu_u = {
                s: mu[s] if product(s) <= u else Fraction(0)
                for s in subsets
            }
            type_i_conv = star(star(mu_u, mu_u, subsets), one, subsets)
            type_i = {
                s: 2 * mu_u[s] - type_i_conv[s] for s in subsets
            }
            mu_u_zeta = star(mu_u, one, subsets)
            a_u = {s: eps[s] - mu_u_zeta[s] for s in subsets}
            balanced = star(star(a_u, a_u, subsets), mu, subsets)
            half = star(a_u, h, subsets)

            assert all(type_i[s] + balanced[s] == mu[s] for s in subsets)
            assert star(half, half, subsets) == balanced
            assert all(
                half[s] == 0 for s in subsets if product(s) <= u
            )
            return type_i, balanced

        cutoffs = [1, 2, 3, 5, 8, 13, 21]
        cached = {u: rows(u) for u in cutoffs}
        boolean_checks += len(cutoffs) * len(subsets)
        half_source_checks += len(cutoffs) * len(subsets)

        for u, v in combinations(cutoffs, 2):
            t_u, b_u = cached[u]
            t_v, b_v = cached[v]
            assert all(
                b_u[s] - b_v[s] == t_v[s] - t_u[s]
                for s in subsets
            )
            cutoff_transfer_checks += len(subsets)

    support_checks = 0
    ratio_checks = 0
    for y in range(64, 50000, 7):
        a = 1
        while a <= 2 * y:
            v = math.floor((2 * y / a) ** 0.25)
            if v >= 1:
                assert (v + 1) ** 4 > 2 * y / a
                ratio = v * (y / (2 * a)) ** (-0.25)
                assert ratio <= math.sqrt(2) + 1e-12
                support_checks += 1
                ratio_checks += 1
            a *= 2

    payload = {
        "schema": "riemann.t103080.quarter-power-boolean.v1",
        "base_pr": 719,
        "base_sha": "4146f81e7237d41e2e4a0cb1737511266683e980",
        "boolean_identity_checks": boolean_checks,
        "cutoff_transfer_checks": cutoff_transfer_checks,
        "half_source_support_checks": half_source_checks,
        "physical_support_checks": support_checks,
        "type_i_ratio_checks": ratio_checks,
        "quarter_power_ratio_bound": "sqrt(2)",
        "bci102990_proved_by_replay": False,
        "rh_established_by_replay": False,
        "verdict": "PASS_T103080_QUARTER_POWER_BOOLEAN_CLOSURE_ALGEBRA",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")

    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
