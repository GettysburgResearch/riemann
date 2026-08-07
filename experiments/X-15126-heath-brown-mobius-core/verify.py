#!/usr/bin/env python3
"""Exact finite decoder for the Möbius core inside the truncated Heath--Brown packet."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Dict, List, Tuple


def mobius_table(nmax: int) -> List[int]:
    mu = [1] * (nmax + 1)
    mu[0] = 0
    primes: List[int] = []
    lp = [0] * (nmax + 1)
    mu[1] = 1
    for n in range(2, nmax + 1):
        if lp[n] == 0:
            lp[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p > lp[n] or n * p > nmax:
                break
            lp[n * p] = p
            if p == lp[n]:
                mu[n * p] = 0
            else:
                mu[n * p] = -mu[n]
    return mu


def primes_up_to(nmax: int) -> List[int]:
    sieve = [True] * (nmax + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(nmax**0.5) + 1):
        if sieve[p]:
            sieve[p * p : nmax + 1 : p] = [False] * (
                ((nmax - p * p) // p) + 1
            )
    return [n for n, ok in enumerate(sieve) if ok]


def scalar_convolution(a: List[int], b: List[int], nmax: int) -> List[int]:
    out = [0] * (nmax + 1)
    for d in range(1, nmax + 1):
        if a[d] == 0:
            continue
        for e in range(1, nmax // d + 1):
            if b[e]:
                out[d * e] += a[d] * b[e]
    return out


def packet_inverse(K: int, V: int, X: int, *, mutate_sign: bool = False) -> List[int]:
    """Compute A_(K,V)=sum_j (-1)^(j-1) C(K,j) mu_V^j*1^(j-1)."""
    mu = mobius_table(X)
    mu_v = [0] * (X + 1)
    one = [0] + [1] * X
    for n in range(1, min(V, X) + 1):
        mu_v[n] = mu[n]

    out = [0] * (X + 1)
    mu_pow = [0] * (X + 1)
    mu_pow[1] = 1
    one_pow = [0] * (X + 1)
    one_pow[1] = 1

    for j in range(1, K + 1):
        mu_pow = scalar_convolution(mu_pow, mu_v, X)
        if j > 1:
            one_pow = scalar_convolution(one_pow, one, X)
        sign = -1 if j % 2 == 0 else 1
        if mutate_sign and j == K:
            sign *= -1
        coeff = sign * math.comb(K, j)
        row = scalar_convolution(mu_pow, one_pow, X)
        for n in range(1, X + 1):
            out[n] += coeff * row[n]
    return out


def vector_add(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(x + y for x, y in zip(a, b))


def vector_scale(c: int, a: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(c * x for x in a)


def vector_convolution(
    a: List[int], b: List[Tuple[int, ...]], X: int, dimension: int
) -> List[Tuple[int, ...]]:
    zero = (0,) * dimension
    out = [zero for _ in range(X + 1)]
    for d in range(1, X + 1):
        if a[d] == 0:
            continue
        for e in range(1, X // d + 1):
            if b[e] != zero:
                out[d * e] = vector_add(out[d * e], vector_scale(a[d], b[e]))
    return out


def log_vectors(X: int) -> Tuple[List[int], List[Tuple[int, ...]]]:
    primes = primes_up_to(X)
    index = {p: i for i, p in enumerate(primes)}
    zero = (0,) * len(primes)
    logs = [zero for _ in range(X + 1)]
    for n in range(2, X + 1):
        m = n
        vec = [0] * len(primes)
        for p in primes:
            if p * p > m:
                break
            while m % p == 0:
                vec[index[p]] += 1
                m //= p
        if m > 1:
            vec[index[m]] += 1
        logs[n] = tuple(vec)
    return primes, logs


def lambda_vectors(X: int, primes: List[int]) -> List[Tuple[int, ...]]:
    index = {p: i for i, p in enumerate(primes)}
    zero = (0,) * len(primes)
    out = [zero for _ in range(X + 1)]
    for n in range(2, X + 1):
        m = n
        p0 = None
        for p in primes:
            if m % p == 0:
                p0 = p
                while m % p == 0:
                    m //= p
                break
        if p0 is not None and m == 1:
            vec = [0] * len(primes)
            vec[index[p0]] = 1
            out[n] = tuple(vec)
    return out


def digest_rows(rows: List[object]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def verify_case(K: int, V: int) -> Dict[str, object]:
    X = V**K
    mu = mobius_table(X)
    A = packet_inverse(K, V, X)
    inverse_mismatches = [n for n in range(1, X + 1) if A[n] != mu[n]]

    primes, logs = log_vectors(X)
    recovered_lambda = vector_convolution(A, logs, X, len(primes))
    expected_lambda = lambda_vectors(X, primes)
    lambda_mismatches = [
        n for n in range(1, X + 1) if recovered_lambda[n] != expected_lambda[n]
    ]

    q0 = 2
    q2_mismatches = []
    if q0 <= X:
        basis_q2 = expected_lambda[q0]
        for m in range(1, X // q0 + 1):
            actual = vector_scale(A[m], basis_q2)
            expected = vector_scale(mu[m], basis_q2)
            if actual != expected:
                q2_mismatches.append(m)

    sample_points = sorted({1, 2, V, min(X, 2 * V), X})
    rows = [{"n": n, "A": A[n], "mu": mu[n]} for n in range(1, X + 1)]
    return {
        "K": K,
        "V": V,
        "X": X,
        "prime_basis_size": len(primes),
        "inverse_mismatches": inverse_mismatches,
        "lambda_mismatches": lambda_mismatches,
        "q2_slice_mismatches": q2_mismatches,
        "sample_A": {str(n): A[n] for n in sample_points},
        "row_digest": digest_rows(rows),
    }


def build_result() -> Dict[str, object]:
    cases = [verify_case(2, 5), verify_case(3, 4), verify_case(4, 3)]
    payload: Dict[str, object] = {
        "schema": "X-15126-v1",
        "classification": "EXACT_MOBIUS_CORE_DECODER",
        "cases": cases,
        "proof_boundary": (
            "This verifies the finite convolution identities A_{K,V}=mu and "
            "A_{K,V}*log=Lambda through V^K, plus the q=2 Möbius slice. "
            "It does not prove any asymptotic Möbius-energy bound or RH."
        ),
        "verdict": "PASS"
        if all(
            not c["inverse_mismatches"]
            and not c["lambda_mismatches"]
            and not c["q2_slice_mismatches"]
            for c in cases
        )
        else "FAIL",
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_sha256"] = hashlib.sha256(encoded).hexdigest()
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("expected", nargs="?", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()
    result = build_result()
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if args.expected:
        expected = json.loads(args.expected.read_text())
        if expected != result:
            print("certificate mismatch")
            return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
