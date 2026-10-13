#!/usr/bin/env python3
"""Exact degree-four control for K=Q(zeta_12), independent of the quadratic check.

Build reciprocal ideal coefficients from splitting degrees, then apply the
three companion Dirichlet series. Retain repeated prime-ideal norms in S.
This is a finite coefficient check, not an estimate of a growing sum.
"""
import hashlib
import json


def primes(n):
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for p in range(2, n + 1):
        if sieve[p]:
            yield p
            for q in range(p * p, n + 1, p):
                sieve[q] = False


def c3(n):
    return (0, 1, -1)[n % 3]


def c4(n):
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)


def conv(a, b, n):
    out = [0] * (n + 1)
    for j in range(1, n + 1):
        if a[j]:
            for k in range(1, n // j + 1):
                out[j * k] += a[j] * b[k]
    return out


def times_factor(a, q, n):
    # Multiply a Dirichlet series by 1-q^{-s}, from an unchanged source.
    out = a[:]
    for j in range(1, n // q + 1):
        out[q * j] -= a[j]
    return out


def divide_factor(a, q, n):
    # Ascending recurrence solves (1-q^{-s}) out = a.
    out = a[:]
    for j in range(1, n // q + 1):
        out[q * j] += out[j]
    return out


def main():
    n = 1200
    ps = list(primes(n))
    raw = [0] * (n + 1)
    raw[1] = 1
    split_counts = {"ramified_degree_two": 0, "fully_split": 0, "two_degree_two": 0}
    for p in ps:
        # Splitting in Q(zeta_12): at 2 and 3, e=2,f=2,g=1;
        # otherwise f is the order of p modulo 12 and g=4/f.
        if p in (2, 3):
            norms = [p * p]
            split_counts["ramified_degree_two"] += 1
        elif p % 12 == 1:
            norms = [p] * 4
            split_counts["fully_split"] += 1
        else:
            norms = [p * p] * 2
            split_counts["two_degree_two"] += 1
        for q in norms:
            raw = times_factor(raw, q, n)
    # An independent ordinary Eratosthenes Möbius calculation.
    mu = [1] * (n + 1)
    mu[0] = 0
    for p in ps:
        for j in range(p, n + 1, p):
            mu[j] *= -1
        for j in range(p * p, n + 1, p * p):
            mu[j] = 0
    companions = [[0] + [f(j) for j in range(1, n + 1)]
                  for f in (c3, c4, lambda j: c3(j) * c4(j))]
    masks = [[], [13], [13, 13], [13, 13, 13, 13],
             [25, 25], [4, 9, 13, 13, 25]]
    retained = []
    failed_dedup = 0
    for norms in masks:
        source = raw[:]
        for q in norms:
            source = divide_factor(source, q, n)
        transformed = source
        for c in companions:
            transformed = conv(transformed, c, n)
        restored = transformed[:]
        for q in norms:
            restored = times_factor(restored, q, n)
        if restored[1:] != mu[1:]:
            raise RuntimeError(f"Abelian coefficient restoration failed: {norms}")
        if len(set(norms)) < len(norms):
            wrong = transformed[:]
            for q in sorted(set(norms)):
                wrong = times_factor(wrong, q, n)
            if wrong[1:] == mu[1:]:
                raise RuntimeError("deduplication negative control failed to detect error")
            failed_dedup += 1
        retained.append([norms, restored[1:]])
    # Exact bounded-prefix controls for all three nonprincipal companions.
    prefix_bounds = []
    for c in companions:
        s = mx = 0
        for j in range(1, n + 1):
            s += c[j]
            mx = max(mx, abs(s))
        if s != 0:  # n is a multiple of the common period 12.
            raise RuntimeError("companion mean is nonzero")
        prefix_bounds.append(mx)
    encoded = json.dumps(retained, separators=(",", ":")).encode()
    print(json.dumps({
        "status": "PASS",
        "field": "Q(zeta_12), degree 4",
        "arithmetic": "exact Python integers; no floating-point tolerance",
        "companion_characters": ["chi_-3", "chi_-4", "chi_12"],
        "splitting_prime_cases": split_counts,
        "maximum_integer_norm": n,
        "restoration_mask_cases": len(masks),
        "coefficient_comparisons": n * len(masks),
        "deduplicated_norm_negative_controls": failed_dedup,
        "observed_prefix_bounds": prefix_bounds,
        "case_sha256": hashlib.sha256(encoded).hexdigest(),
        "scope": "finite coefficient identities; no native moment, growing-field uniformity, or RH inference",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
