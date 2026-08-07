#!/usr/bin/env python3
"""Exact verifier for L-23006/L-23007 synthetic algebra.

Uses only Python integers and fractions.Fraction. This proves no Möbius
asymptotic estimate and no statement about RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Mapping

SCHEMA = "riemann.x23001-finite-inverse-boundary.v1"
RESULT_SCHEMA = "riemann.x23001-finite-inverse-boundary.result.v1"


def frac(x: object) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("booleans are not rational inputs")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, str):
        return Fraction(x)
    raise TypeError(f"unsupported rational value: {x!r}")


def mobius_table(n: int) -> List[int]:
    if n < 1:
        raise ValueError("n must be positive")
    mu = [1] * (n + 1)
    prime = [True] * (n + 1)
    mu[0] = 0
    for p in range(2, n + 1):
        if prime[p]:
            for k in range(p, n + 1, p):
                prime[k] = False if k != p else prime[k]
                mu[k] *= -1
            p2 = p * p
            if p2 <= n:
                for k in range(p2, n + 1, p2):
                    mu[k] = 0
    return mu


def conv(a: List[int], b: List[int], n: int) -> List[int]:
    out = [0] * (n + 1)
    for d in range(1, n + 1):
        ad = a[d] if d < len(a) else 0
        if ad == 0:
            continue
        for q in range(1, n // d + 1):
            bq = b[q] if q < len(b) else 0
            if bq:
                out[d * q] += ad * bq
    return out


def add_scaled(out: List[int], a: List[int], scale: int) -> None:
    if len(out) != len(a):
        raise ValueError("length mismatch")
    for i in range(1, len(out)):
        out[i] += scale * a[i]


def conv_pow(a: List[int], k: int, n: int) -> List[int]:
    if k < 0:
        raise ValueError("negative convolution power")
    eps = [0] * (n + 1)
    eps[1] = 1
    out = eps
    for _ in range(k):
        out = conv(out, a, n)
    return out


def finite_inverse(mu_v: List[int], k: int, n: int) -> List[int]:
    one = [0] + [1] * n
    out = [0] * (n + 1)
    for j in range(1, k + 1):
        term = conv(conv_pow(mu_v, j, n), conv_pow(one, j - 1, n), n)
        add_scaled(out, term, (-1) ** (j - 1) * math.comb(k, j))
    return out


def check_arithmetic_case(case: Mapping[str, object]) -> Dict[str, object]:
    keys = set(case)
    if keys != {"V", "K", "N"}:
        raise ValueError(f"unexpected arithmetic-case keys: {keys}")
    V, K, N = (case[k] for k in ("V", "K", "N"))
    if any(isinstance(x, bool) or not isinstance(x, int) for x in (V, K, N)):
        raise TypeError("V, K, N must be integers")
    if not (V >= 1 and K >= 1 and N >= max(2 * V, V**K)):
        raise ValueError("invalid arithmetic case range")

    mu = mobius_table(N)
    mu_v = [0] * (N + 1)
    for n in range(1, min(V, N) + 1):
        mu_v[n] = mu[n]
    one = [0] + [1] * N
    eps = [0] * (N + 1)
    eps[1] = 1

    B = conv(mu_v, one, N)
    r = [eps[n] - B[n] for n in range(N + 1)]
    A = finite_inverse(mu_v, K, N)
    rK = conv_pow(r, K, N)
    mu_rK = conv(mu, rK, N)

    for n in range(1, N + 1):
        if A[n] != mu[n] - mu_rK[n]:
            raise AssertionError(("global_identity", V, K, n, A[n], mu[n] - mu_rK[n]))

    exact_end = min(N, V**K)
    for n in range(1, exact_end + 1):
        if A[n] != mu[n]:
            raise AssertionError(("finite_exactness", V, K, n, A[n], mu[n]))

    for n in range(V + 1, min(2 * V, N) + 1):
        if r[n] != mu[n]:
            raise AssertionError(("first_shell", V, n, r[n], mu[n]))

    shell = [0] * (N + 1)
    for n in range(V + 1, min(2 * V, N) + 1):
        shell[n] = mu[n]
    shellK = conv_pow(shell, K, N)

    lo = (V + 1) ** K
    hi = min(N, (2 * V + 1) * (V + 1) ** (K - 1) - 1)
    if lo <= hi:
        for n in range(lo, hi + 1):
            if rK[n] != shellK[n]:
                raise AssertionError(("boundary_tensor", V, K, n, rK[n], shellK[n]))

    overlap_hi = min(hi, 2 * (V + 1) ** K - 1)
    if lo <= overlap_hi:
        for n in range(lo, overlap_hi + 1):
            if mu[n] - A[n] != shellK[n]:
                raise AssertionError(("boundary_overlap", V, K, n, mu[n] - A[n], shellK[n]))

    A_next = finite_inverse(mu_v, K + 1, N)
    increment = conv(mu_v, rK, N)
    for n in range(1, N + 1):
        if A_next[n] - A[n] != increment[n]:
            raise AssertionError(("adjacent_order", V, K, n, A_next[n] - A[n], increment[n]))

    return {
        "V": V,
        "K": K,
        "N": N,
        "finite_exact_through": exact_end,
        "boundary_range": [lo, hi],
        "overlap_range": [lo, overlap_hi],
        "nonzero_boundary_coefficients": sum(
            1 for n in range(max(1, lo), max(lo, hi) + 1) if n <= N and rK[n]
        ),
    }


Series = Dict[int, Fraction]


def series_mul(a: Series, b: Series, lo: int, hi: int) -> Series:
    out: Series = {}
    for i, ai in a.items():
        for j, bj in b.items():
            e = i + j
            if lo <= e <= hi:
                out[e] = out.get(e, Fraction(0)) + ai * bj
    return {e: c for e, c in out.items() if c}


def series_pow(a: Series, k: int, lo: int, hi: int) -> Series:
    out: Series = {0: Fraction(1)}
    for _ in range(k):
        out = series_mul(out, a, lo, hi)
    return out


def analytic_inverse(g: List[Fraction], degree: int) -> List[Fraction]:
    if not g or g[0] == 0:
        raise ValueError("nonzero constant term required")
    h = [Fraction(0)] * (degree + 1)
    h[0] = 1 / g[0]
    for n in range(1, degree + 1):
        total = sum(g[j] * h[n - j] for j in range(1, min(n, len(g) - 1) + 1))
        h[n] = -total / g[0]
    return h


def check_germ_case(case: Mapping[str, object]) -> Dict[str, object]:
    if set(case) != {"multiplicity", "K_values", "g", "M"}:
        raise ValueError("unexpected germ-case keys")
    m = case["multiplicity"]
    ks = case["K_values"]
    if isinstance(m, bool) or not isinstance(m, int) or m < 1:
        raise ValueError("invalid multiplicity")
    if not isinstance(ks, list) or not ks or any(
        isinstance(k, bool) or not isinstance(k, int) or k < 1 for k in ks
    ):
        raise ValueError("invalid K_values")
    g = [frac(x) for x in case["g"]]  # type: ignore[index]
    M = [frac(x) for x in case["M"]]  # type: ignore[index]
    max_k = max(ks)
    hi = 3 * m + max(len(g), len(M)) + 2
    lo = -m

    h = analytic_inverse(g, hi + m)
    inv_zeta: Series = {
        j - m: h[j] for j in range(len(h)) if lo <= j - m <= hi and h[j]
    }
    gser: Series = {i: c for i, c in enumerate(g) if c}
    mser: Series = {i: c for i, c in enumerate(M) if c}
    gm = series_mul(gser, mser, 0, hi)
    R: Series = {0: Fraction(1)}
    for e, c in gm.items():
        ee = e + m
        if ee <= hi:
            R[ee] = R.get(ee, Fraction(0)) - c

    negative_reference = {e: inv_zeta.get(e, Fraction(0)) for e in range(-m, 0)}
    for k in ks:
        rk = series_pow(R, k, 0, hi + m)
        residual = series_mul(rk, inv_zeta, lo, hi)
        negative = {e: residual.get(e, Fraction(0)) for e in range(-m, 0)}
        if negative != negative_reference:
            raise AssertionError(("principal_part", m, k, negative, negative_reference))

    for k, ell in zip(ks, ks[1:]):
        rk = series_pow(R, k, 0, hi + m)
        rl = series_pow(R, ell, 0, hi + m)
        diff_r = {
            e: rk.get(e, Fraction(0)) - rl.get(e, Fraction(0)) for e in set(rk) | set(rl)
        }
        diff = series_mul(diff_r, inv_zeta, lo, hi)
        if any(diff.get(e, Fraction(0)) for e in range(-m, 0)):
            raise AssertionError(("order_difference_pole", m, k, ell))

    return {
        "multiplicity": m,
        "K_values": ks,
        "principal_part": {str(e): str(c) for e, c in negative_reference.items()},
    }


def canonical_digest(payload: Mapping[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def verify(cert: Mapping[str, object]) -> Dict[str, object]:
    if set(cert) != {"schema", "arithmetic_cases", "germ_cases"}:
        raise ValueError("certificate keys must match schema exactly")
    if cert["schema"] != SCHEMA:
        raise ValueError("wrong schema")
    arithmetic_cases = cert["arithmetic_cases"]
    germ_cases = cert["germ_cases"]
    if not isinstance(arithmetic_cases, list) or not arithmetic_cases:
        raise ValueError("arithmetic_cases must be a nonempty list")
    if not isinstance(germ_cases, list) or not germ_cases:
        raise ValueError("germ_cases must be a nonempty list")

    result: Dict[str, object] = {
        "schema": RESULT_SCHEMA,
        "verified": True,
        "arithmetic": [check_arithmetic_case(c) for c in arithmetic_cases],
        "germs": [check_germ_case(c) for c in germ_cases],
        "verdict": "EXACT_FINITE_INVERSE_BOUNDARY_AND_PRINCIPAL_PART_ALGEBRA_VERIFIED",
        "proof_boundary": (
            "Synthetic exact convolution and local Laurent algebra only; no asymptotic "
            "Möbius estimate, safe-window transfer, BTP(K), or RH claim is certified."
        ),
    }
    result["proof_object_sha256"] = canonical_digest(result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cert = json.loads(args.certificate.read_text())
    result = verify(cert)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
