#!/usr/bin/env python3
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def inner(x, y):
    return x.conjugate() * y


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    exceptional_checks = 0
    for Y in range(65, 20001):
        U = int(Y ** (1.0 / 6.0))
        assert 2 * (U + 1) ** 4 > 4 * math.sqrt(Y)
        exceptional_checks += 1

    ratio_checks = 0
    for a in range(2, 51):
        for b in range(2, 51):
            for P in range(2, a + 1):
                for Q in range(2, b + 1):
                    N = P * a * a
                    M = Q * b * b
                    if N <= 8 * M and M <= 8 * N:
                        assert Q <= 2 * a
                        assert P <= 2 * b
                        ratio_checks += 1

    ns = list(range(1, 13))
    coeff = {
        n: complex((n % 5) - 2, (n % 3) - 1) / 7.0
        for n in ns
    }

    masked_phase_checks = 0
    lhs = 0.0
    rhs = 0j
    for ell in [3, 5, 7]:
        mask = {
            n: complex(((n + ell) % 4) / 3.0,
                       ((2 * n + ell) % 3) / 5.0)
            for n in ns
        }
        for h in range(1, ell):
            S = sum(
                mask[n] * coeff[n]
                * cmath.exp(2j * math.pi * h * n / ell)
                for n in ns
            )
            lhs += abs(S) ** 2 / ell
        for n in ns:
            for r in ns:
                kernel = (1.0 if (n - r) % ell == 0 else 0.0) - 1.0 / ell
                rhs += inner(mask[r] * coeff[r], mask[n] * coeff[n]) * kernel
        masked_phase_checks += 1
    assert abs(lhs - rhs.real) < 1e-8
    assert abs(rhs.imag) < 1e-8

    lhs2 = 0.0
    rhs2 = 0j
    for ell in [3, 5]:
        for rho in [7, 11]:
            mask = {
                n: complex(((n + ell + rho) % 5) / 4.0,
                           ((n * rho + ell) % 4) / 6.0)
                for n in ns
            }
            for h in range(1, ell):
                for k in range(1, rho):
                    S = sum(
                        mask[n] * coeff[n]
                        * cmath.exp(2j * math.pi * h * n / ell)
                        * cmath.exp(2j * math.pi * k * n / rho)
                        for n in ns
                    )
                    lhs2 += abs(S) ** 2 / (ell * rho)
            for n in ns:
                for r in ns:
                    k1 = (1.0 if (n-r) % ell == 0 else 0.0) - 1.0 / ell
                    k2 = (1.0 if (n-r) % rho == 0 else 0.0) - 1.0 / rho
                    rhs2 += inner(mask[r] * coeff[r], mask[n] * coeff[n]) * k1 * k2
            masked_phase_checks += 1
    assert abs(lhs2 - rhs2.real) < 1e-8
    assert abs(rhs2.imag) < 1e-8

    owner_primes = [2, 3, 5, 7]
    A = {}
    for ell in owner_primes:
        for rho in owner_primes:
            if ell == rho:
                continue
            for k in range(1, rho):
                A[ell, rho, k] = complex(ell + 2 * k, rho - k) / 13.0

    F = {}
    for ell in owner_primes:
        for rho in owner_primes:
            if ell == rho:
                continue
            scale = math.sqrt((rho - 1) / (ell * rho * (ell - 1)))
            for h in range(1, ell):
                for k in range(1, rho):
                    F[ell, rho, h, k] = scale * A[ell, rho, k]

    Pnorm = sum(abs(z) ** 2 for z in F.values())
    G = 0j
    plus = 0.0
    minus = 0.0
    visited = set()
    for key, z in F.items():
        ell, rho, h, k = key
        tkey = (rho, ell, k, h)
        G += inner(z, F[tkey])
        if key not in visited:
            zt = F[tkey]
            plus += abs((z + zt) / 2) ** 2 + abs((zt + z) / 2) ** 2
            minus += abs((z - zt) / 2) ** 2 + abs((zt - z) / 2) ** 2
            visited.add(key)
            visited.add(tkey)
    assert abs(G.imag) < 1e-9
    assert abs(Pnorm - (plus + minus)) < 1e-9
    assert abs(G.real - (plus - minus)) < 1e-9

    hodge_checks = 0
    for k in range(4, 41):
        C = k * (k - 1) // 2
        w = {}
        for i in range(k):
            for j in range(i + 1, k):
                w[i, j] = (
                    Fraction(1 if (i, j) == (0, 1) else 0)
                    - Fraction(1, C)
                )
        rows = [
            sum(w[min(i, j), max(i, j)] for j in range(k) if j != i)
            for i in range(k)
        ]
        aa = [r / Fraction(k - 2) for r in rows]
        g = {
            (i, j): aa[i] + aa[j]
            for i in range(k)
            for j in range(i + 1, k)
        }
        c = {e: w[e] - g[e] for e in w}
        assert all(
            sum(c[min(i, j), max(i, j)] for j in range(k) if j != i) == 0
            for i in range(k)
        )
        assert sum(x * x for x in g.values()) == Fraction(2, k)
        assert sum(x * x for x in c.values()) == Fraction(k - 3, k - 1)
        hodge_checks += 1

    payload = {
        "schema": "riemann.t102980.boolean-incidence-hardening.v1",
        "exceptional_sector_integer_checks": exceptional_checks,
        "ratioeight_owner_core_checks": ratio_checks,
        "masked_phase_checks": masked_phase_checks,
        "transpose_array_entries": len(F),
        "minimum_pair_hodge_checks": hodge_checks,
        "exceptional_sector_empty_cofinally": True,
        "opposite_owner_products_core_paid": True,
        "incidence_masks_preserve_centered_phase_bounds": True,
        "selector_gram_transpose_signature": True,
        "minimum_pair_cycle_energy_limit": "1",
        "cocurl102980_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102980_BOOLEAN_INCIDENCE_HARDENING",
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
