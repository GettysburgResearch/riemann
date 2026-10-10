#!/usr/bin/env python3
"""Exact finite verification of the new algebra, not of an infinite moment bound.

Two actual split Eisenstein primes of norms 7 and 13 supply all local sextic
states through the 91 integer residue classes. Integer-scaled finite test
weights avoid floating arithmetic. The hypergraph expansion is assembled
independently of direct polynomial multiplication. All checks use explicit
exceptions and remain active under python -O.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import product
import json
from math import comb, factorial
from pathlib import Path


COUNTS: dict[str, int] = defaultdict(int)
ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
PRIMES = (7, 13)
OMEGA_RESIDUES = (4, 9)


def check(category, condition, message):
    COUNTS[category] += 1
    if not condition:
        raise ArithmeticError(f"{category}: {message}")


def zadd(z, w):
    return z[0] + w[0], z[1] + w[1]


def zmul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c + b * d


def zscale(z, n):
    return z[0] * n, z[1] * n


def znorm(z):
    a, b = z
    return a * a + a * b + b * b


def zpow(z, n):
    out = (1, 0)
    for _ in range(n):
        out = zmul(out, z)
    return out


def character(u, p, omega):
    """(u/pi)_6, with O/pi=F_p and omega mapped to the specified root."""
    if u % p == 0:
        return (0, 0)
    value = pow(u % p, (p - 1) // 6, p)
    zeta = (1 + omega) % p
    for j in range(6):
        if pow(zeta, j, p) == value:
            return ROOTS[j]
    raise ArithmeticError("sextic symbol was not a sixth root")


def charge(n):
    # Zero means the prime is absent. Six means a positive multiple of six;
    # it retains the coprimality mask and must not be replaced by zero.
    return 0 if n == 0 else (n % 6 or 6)


def keymul(a, b):
    return tuple(charge(x + y) for x, y in zip(a, b))


def keyconj(a):
    return tuple(0 if x == 0 else (-x) % 6 or 6 for x in a)


def clean(d):
    return {key: value for key, value in d.items() if value}


def polymul(a, b):
    out = defaultdict(int)
    for ka, va in a.items():
        for kb, vb in b.items():
            out[keymul(ka, kb)] += va * vb
    return clean(out)


def scaled_weight(n, D, i, mixed):
    # D * W_i(n/D), with W_i(y)=(y+i%3) 1_[1/4,3](y).
    # These finite algebra fixtures need not be smooth. No analytic estimate
    # is inferred for them. The same support/dilation identity is exact.
    if not (D <= 4 * n and n <= 3 * D):
        return 0
    return n + ((i % 3) * D if mixed else 0)


def one_polynomial(D, i, nus, mixed):
    out = {}
    for mask in range(4):
        n = 1
        coef = 1
        key = []
        for j, p in enumerate(PRIMES):
            active = bool(mask & (1 << j))
            key.append(int(active))
            if active:
                n *= p
                coef *= -nus[j]
        coef *= scaled_weight(n, D, i, mixed)
        if coef:
            out[tuple(key)] = coef
    return out


def hypergraph_polynomial(k, D, nus, mixed):
    """Separate repeated incidence ideals, then enumerate singleton columns."""
    repeated = [0] + [m for m in range(1 << k) if m.bit_count() >= 2]
    out = defaultdict(int)
    for incidence in product(repeated, repeat=2):
        scales = [1] * k  # c_i in X_i=D/N(c_i)
        external = 1
        powers = [0, 0]
        available = []
        for j, bits in enumerate(incidence):
            if bits == 0:
                available.append(j)
                continue
            m = bits.bit_count()
            powers[j] = m
            external *= (-nus[j]) ** m
            for i in range(k):
                if bits & (1 << i):
                    scales[i] *= PRIMES[j]
        # For each prime absent from the repeated ideals: absent altogether,
        # or placed in exactly one singleton factor. No duplicate allocation.
        for allocation in product(range(-1, k), repeat=len(available)):
            singleton_norms = [1] * k
            e = powers.copy()
            coef = external
            for j, i in zip(available, allocation):
                if i >= 0:
                    singleton_norms[i] *= PRIMES[j]
                    e[j] = 1
                    coef *= -nus[j]
            for i in range(k):
                coef *= scaled_weight(scales[i] * singleton_norms[i], D, i, mixed)
                if coef == 0:
                    break
            if coef:
                out[tuple(charge(x) for x in e)] += coef
    return clean(out)


def evaluate(poly, chars):
    value = (0, 0)
    for key, coef in poly.items():
        term = (1, 0)
        for e, ch in zip(key, chars):
            if e:
                term = zmul(term, zpow(ch, e))
        value = zadd(value, zscale(term, coef))
    return value


def verify_hypergraphs():
    states = set()
    characters = []
    for u in range(91):
        chars = tuple(character(u, p, w) for p, w in zip(PRIMES, OMEGA_RESIDUES))
        characters.append(chars)
        states.add(chars)
    check("native_characters", len(states) == 49, "CRT must realize every zero/sixth-root pair")
    for p, omega in zip(PRIMES, OMEGA_RESIDUES):
        check("native_characters", (omega * omega + omega + 1) % p == 0, "Eisenstein embedding")
        check("native_characters", len({pow(1 + omega, j, p) for j in range(6)}) == 6, "primitive sixth root")
    panels = []
    for k in range(1, 9):
        for D in (2, 3, 5, 10, 40):
            for nus, mixed in (((1, 1), False), ((-1, -1), True)):
                factors = [one_polynomial(D, i, nus, mixed) for i in range(k)]
                direct = {(0, 0): 1}
                for factor in factors:
                    direct = polymul(direct, factor)
                regrouped = hypergraph_polynomial(k, D, nus, mixed)
                check("hypergraph_polynomials", direct == regrouped, (k, D, nus, mixed))
                complete_moment = 0
                for chars in characters:
                    actual = (1, 0)
                    for factor in factors:
                        actual = zmul(actual, evaluate(factor, chars))
                    recovered = evaluate(regrouped, chars)
                    check("native_row_identities", actual == recovered, (k, D, chars))
                    complete_moment += znorm(actual)
                # Complete residue orthogonality, independently from field
                # evaluations. Nonprincipal local powers sum to zero; a used
                # sixth-power coordinate sums to p-1, and an absent one to p.
                conjugated = {keyconj(key): coef for key, coef in direct.items()}
                squared = polymul(direct, conjugated)
                diagonal = 0
                for key, coef in squared.items():
                    local = 1
                    for e, p in zip(key, PRIMES):
                        local *= p if e == 0 else (p - 1 if e == 6 else 0)
                    diagonal += coef * local
                check("complete_residue_moments", complete_moment == diagonal, (k, D))
                panels.append({"k": k, "D": D, "mixed": mixed, "nu_at_primes": list(nus),
                               "polynomial_terms": len(regrouped), "complete_moment": str(complete_moment)})
    # Explicitly reject the tempting wrong convention chi_p^6 = 1 at p|u.
    ch = character(7, 7, 4)
    check("adversarial_zero_mask", zpow(ch, 6) == (0, 0), "sixfold local zero survives")
    check("adversarial_zero_mask", evaluate({(6, 0): 1}, characters[7]) != (1, 0), "constant-one mutation rejected")
    return panels


def indices(r, degree):
    if r == 0:
        yield ()
        return
    for e in range(degree + 1):
        for tail in indices(r - 1, degree - e):
            yield (e,) + tail


def multinomial(e):
    out = factorial(sum(e))
    for value in e:
        out //= factorial(value)
    return out


def coefficient_convolution(a, b, e):
    total = 0
    for d in product(*(range(x + 1) for x in e)):
        f = tuple(x - y for x, y in zip(e, d))
        total += a.get(d, 0) * b.get(f, 0)
    return total


def verify_local_series():
    panels = []
    for r in range(1, 7):
        degree = 8
        exps = list(indices(r, degree))
        zero = (0,) * r
        F, P, K, C, H = {}, {}, {}, {}, {}
        for e in exps:
            E = sum(e)
            active = [i for i, x in enumerate(e) if x]
            F[e] = 1 if E == 0 else (-1 if E == 1 else 0)
            P[e] = (-1) ** E if max(e, default=0) <= 1 else 0
            K[e] = multinomial(e)
            C[e] = 1 if E == 0 else 1 - len(active)
            h = 0
            for mask in range(1 << len(active)):
                v = list(e)
                m = 0
                for j, i in enumerate(active):
                    if mask & (1 << j):
                        v[i] -= 1
                        m += 1
                h += (-1) ** m * multinomial(tuple(v))
            H[e] = h
        for e in exps:
            delta = int(e == zero)
            check("multinomial_inverse", coefficient_convolution(K, F, e) == delta, (r, e))
            check("euler_correction", coefficient_convolution(C, P, e) == F[e], (r, e))
            check("inverse_correction", coefficient_convolution(H, F, e) == P[e], (r, e))
            check("two_way_correction", coefficient_convolution(C, H, e) == delta, (r, e))
            check("inverse_positivity", H[e] >= 0, (r, e))
        c2 = sum(abs(v) for e, v in C.items() if sum(e) == 2)
        h2 = sum(v for e, v in H.items() if sum(e) == 2)
        check("logarithmic_leading_cost", c2 == h2 == comb(r, 2), r)
        panels.append({"factors": r, "total_degree": degree, "coefficients": len(exps),
                       "pair_coefficient": c2})
    return panels


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    hypergraphs = verify_hypergraphs()
    local_series = verify_local_series()
    result = {
        "status": "PASS", "arithmetic": "EXACT_INTEGER_IN_Z[zeta_6]",
        "scope": "finite algebra and actual two-prime character fixtures; no infinite analytic estimate",
        "actual_character_fixture": {"prime_ideal_norms": list(PRIMES),
                                     "omega_images": list(OMEGA_RESIDUES),
                                     "integer_residues": 91, "local_state_pairs": 49},
        "predicate_counts": dict(sorted(COUNTS.items())),
        "total_predicates": sum(COUNTS.values()),
        "hypergraph_panels": hypergraphs,
        "local_series_panels": local_series,
        "unproved": ["short-row fourth moment", "short-row generalized moment", "17/24", "RH"]
    }
    rendered = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(json.dumps({key: result[key] for key in ("status", "arithmetic", "total_predicates", "predicate_counts")}))


if __name__ == "__main__":
    main()
