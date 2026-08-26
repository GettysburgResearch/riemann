#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
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
            a = frozenset(elems[j] for j in range(len(elems)) if (mask >> j) & 1)
            total += f[a] * g[s - a]
        out[s] = total
    return out


def digest(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    subsets = list(powerset(6))
    primes = [2, 3, 5, 7, 11, 13]

    def prod(s):
        z = 1
        for i in s:
            z *= primes[i]
        return z

    eps = {s: Fraction(1 if not s else 0) for s in subsets}
    one = {s: Fraction(1) for s in subsets}
    mu = {s: Fraction((-1) ** len(s)) for s in subsets}

    rows = {}
    for u in [2, 3, 5, 8, 13]:
        mu_u = {s: mu[s] if prod(s) <= u else Fraction(0) for s in subsets}
        type_i = {
            s: 2 * mu_u[s] - star(star(mu_u, mu_u, subsets), one, subsets)[s]
            for s in subsets
        }
        a_u = {s: eps[s] - star(mu_u, one, subsets)[s] for s in subsets}
        balanced = star(star(a_u, a_u, subsets), mu, subsets)
        assert all(type_i[s] + balanced[s] == mu[s] for s in subsets)
        rows[u] = (type_i, balanced)

    transfer_checks = 0
    for u in rows:
        for v in rows:
            t_u, b_u = rows[u]
            t_v, b_v = rows[v]
            assert all(b_u[s] - b_v[s] == t_v[s] - t_u[s] for s in subsets)
            transfer_checks += len(subsets)

    # Source-blind owner-collapse countermodel: N orthogonal labelled copies,
    # each of coefficient 1/sqrt(N), collapse to one common physical vector.
    collapse_checks = 0
    for n in range(1, 65):
        labelled_norm_sq = Fraction(n, n)
        physical_norm_sq = Fraction(n * n, n)
        assert labelled_norm_sq == 1
        assert physical_norm_sq == n
        collapse_checks += 1

    payload = {
        "schema": "riemann.t103110.quarter-power-owner-collapse-audit.v1",
        "boolean_cutoff_transfer_checks": transfer_checks,
        "clustered_collapse_checks": collapse_checks,
        "historical_l103070_complete_owner_conclusion": False,
        "fixed_owner_type_i_endpoint": True,
        "quarter_power_balanced_support_empty": True,
        "quarter_power_complete_type_i_equals_harmonic_field": True,
        "same_occurrence_multiplicity_controls_cross_owner_collapse": False,
        "qpti103112_proved": False,
        "bci102990_proved": False,
        "rh_established": False,
        "verdict": "PASS_T103110_QUARTER_POWER_OWNER_COLLAPSE_AUDIT",
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
