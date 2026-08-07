#!/usr/bin/env python3
"""Exact verifier for the Euler-aligned dyadic shell (X-23402).

Standard-library only. Prime logarithms are formal symbols; no floating
transcendentals are evaluated. The checker proves finite coefficient identities
only, not a cofinal energy estimate or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Mapping, Tuple


class VerificationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise VerificationError(message)


def factor(n: int) -> Dict[int, int]:
    if n < 1:
        fail("positive integers only")
    out: Dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n: int):
    out = [1]
    for p, exponent in factor(n).items():
        out = [a * p**j for a in out for j in range(exponent + 1)]
    return out


def mobius(n: int) -> int:
    f = factor(n)
    return 0 if any(exponent > 1 for exponent in f.values()) else (-1 if len(f) % 2 else 1)


def v2(n: int) -> int:
    exponent = 0
    while n % 2 == 0:
        exponent += 1
        n //= 2
    return exponent


def b2(n: int) -> int:
    return mobius(n) - (mobius(n // 2) if n % 2 == 0 else 0)


def a2(n: int) -> int:
    return v2(n) + 1


def log_vector(n: int) -> Dict[int, int]:
    return factor(n)


def prime_power(n: int):
    f = factor(n)
    if len(f) != 1:
        return None
    return next(iter(f.items()))


def generalized_lambda(n: int, extra_two: int) -> Dict[int, int]:
    item = prime_power(n)
    if item is None:
        return {}
    p, _ = item
    return {p: 1 + (extra_two if p == 2 else 0)}


def linear_add(a: Mapping[int, int], b: Mapping[int, int], scale: int = 1):
    out = dict(a)
    for p, value in b.items():
        out[p] = out.get(p, 0) + scale * value
        if out[p] == 0:
            del out[p]
    return out


def linear_scale(a: Mapping[int, int], scale: int):
    return {p: scale * value for p, value in a.items() if scale * value}


Quad = Dict[Tuple[int, int], int]


def outer(a: Mapping[int, int], b: Mapping[int, int], scale: int = 1) -> Quad:
    out: Quad = {}
    for p, x in a.items():
        for q, y in b.items():
            key = (p, q) if p <= q else (q, p)
            out[key] = out.get(key, 0) + scale * x * y
    return {key: value for key, value in out.items() if value}


def quad_add(a: Mapping[Tuple[int, int], int], b: Mapping[Tuple[int, int], int], scale: int = 1) -> Quad:
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, 0) + scale * value
        if out[key] == 0:
            del out[key]
    return out


def verify(certificate: Mapping[str, Any]) -> Dict[str, Any]:
    if certificate.get("schema") != "riemann.x23402.euler-aligned-shell.v1":
        fail("schema mismatch")

    limit = int(certificate["limit"])
    if limit < 4:
        fail("limit too small")
    extra_two = int(certificate["extra_two_von_mangoldt_copy"])
    if extra_two not in (0, 1, 2):
        fail("invalid extra two weight")
    expected_pattern = list(map(int, certificate["expected_two_adic_pattern"]))
    if len(expected_pattern) != 4:
        fail("wrong local pattern length")

    pattern = [b2(2**exponent) for exponent in range(4)]
    if pattern != expected_pattern:
        fail("2-adic local pattern mismatch")

    inverse_rows = 0
    first_rows = 0
    second_rows = 0
    selberg_rows = 0

    for n in range(1, limit + 1):
        inverse = sum(a2(d) * b2(n // d) for d in divisors(n))
        if inverse != (1 if n == 1 else 0):
            fail(f"inverse identity failed at {n}")
        inverse_rows += 1

        first_left = linear_scale(log_vector(n), b2(n))
        first_right: Dict[int, int] = {}
        for d in divisors(n):
            first_right = linear_add(first_right, generalized_lambda(d, extra_two), -b2(n // d))
        if first_left != first_right:
            fail(f"first logarithmic identity failed at {n}")
        first_rows += 1

        second_left = outer(log_vector(n), log_vector(n), b2(n))
        second_right: Quad = {}
        for d in divisors(n):
            for e in divisors(n // d):
                second_right = quad_add(
                    second_right,
                    outer(generalized_lambda(d, extra_two), generalized_lambda(e, extra_two), b2(n // d // e)),
                )
        for d in divisors(n):
            second_right = quad_add(
                second_right,
                outer(generalized_lambda(d, extra_two), log_vector(d), -b2(n // d)),
            )
        if second_left != second_right:
            fail(f"second logarithmic identity failed at {n}")
        second_rows += 1

        selberg_left: Quad = {}
        for d in divisors(n):
            m = n // d
            selberg_left = quad_add(
                selberg_left,
                outer(log_vector(m), log_vector(m), b2(d) * a2(m)),
            )
        selberg_right = outer(generalized_lambda(n, extra_two), log_vector(n))
        for d in divisors(n):
            selberg_right = quad_add(
                selberg_right,
                outer(generalized_lambda(d, extra_two), generalized_lambda(n // d, extra_two)),
            )
        if selberg_left != selberg_right:
            fail(f"Selberg identity failed at {n}")
        selberg_rows += 1

    result: Dict[str, Any] = {
        "schema": "riemann.x23402.euler-aligned-shell.result.v1",
        "verified": True,
        "limit": limit,
        "two_adic_pattern": pattern,
        "inverse_rows": inverse_rows,
        "first_logarithmic_rows": first_rows,
        "second_logarithmic_rows": second_rows,
        "selberg_rows": selberg_rows,
        "verdict": "EXACT_EULER_ALIGNED_DYADIC_SHELL_SELBERG_ALGEBRA_VERIFIED",
        "proof_boundary": "Finite formal-prime-log coefficient algebra only; no reflected forcing estimate, shell-energy bound, Mertens estimate, or RH claim is certified.",
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode("utf-8")
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()

    expected = certificate.get("expected_proof_object_sha256")
    if expected is not None and expected != result["proof_object_sha256"]:
        fail("proof digest mismatch")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(json.loads(args.certificate.read_text()))
    except (OSError, ValueError, KeyError, TypeError, VerificationError) as exc:
        print(f"VERIFICATION_FAILED: {exc}")
        return 1
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
