#!/usr/bin/env python3
"""Exact finite verifier for the Green--dipole Skorokhod carry interfaces.

This consumer uses only Python's standard library, integers, and Fraction.
It verifies finite algebra only. It does not prove the asymptotic contact
theorem or the Riemann Hypothesis.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "X-26201-v1"


class VerificationError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise VerificationError(f"{name} must be a non-Boolean integer")
    return value


def parse_fraction(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise VerificationError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise VerificationError(f"invalid fraction for {name}") from exc
    if isinstance(value, dict) and set(value) == {"numerator", "denominator"}:
        num = parse_int(value["numerator"], f"{name}.numerator")
        den = parse_int(value["denominator"], f"{name}.denominator")
        if den == 0:
            raise VerificationError(f"{name}.denominator must be nonzero")
        return Fraction(num, den)
    raise VerificationError(f"{name} must be an int, fraction string, or fraction object")


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_sha(obj: Any) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for k in range(p * p, limit + 1, p):
                sieve[k] = False
        p += 1
    return [n for n in range(2, limit + 1) if sieve[n]]


def prime_powers_upto(limit: int) -> tuple[list[int], dict[int, int]]:
    powers: dict[int, int] = {}
    for p in primes_upto(limit):
        q = p
        while q <= limit:
            if q in powers and powers[q] != p:
                raise AssertionError("unique factorization failure")
            powers[q] = p
            q *= p
    return sorted(powers), powers


def mobius_table(limit: int) -> list[int]:
    mu = [1] * (limit + 1)
    prime_count = [0] * (limit + 1)
    squareful = [False] * (limit + 1)
    for p in primes_upto(limit):
        for n in range(p, limit + 1, p):
            prime_count[n] += 1
        p2 = p * p
        for n in range(p2, limit + 1, p2):
            squareful[n] = True
    mu[0] = 0
    for n in range(1, limit + 1):
        mu[n] = 0 if squareful[n] else (-1 if prime_count[n] % 2 else 1)
    return mu


def factor_exponents(n: int) -> dict[int, int]:
    if n < 1:
        raise VerificationError("factor_exponents requires n>=1")
    result: dict[int, int] = {}
    value = n
    for p in primes_upto(int(value**0.5) + 1):
        while value % p == 0:
            result[p] = result.get(p, 0) + 1
            value //= p
        if value == 1:
            break
    if value > 1:
        result[value] = result.get(value, 0) + 1
    return result


def add_log_vector(a: dict[int, Fraction], b: dict[int, Fraction], scale: Fraction = Fraction(1)) -> None:
    for p, value in b.items():
        a[p] = a.get(p, Fraction(0)) + scale * value
        if a[p] == 0:
            del a[p]


def log_integer_vector(n: int, scale: Fraction = Fraction(1)) -> dict[int, Fraction]:
    return {p: scale * exponent for p, exponent in factor_exponents(n).items()}


def log_ratio_vector(num: int, den: int, scale: Fraction = Fraction(1)) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    add_log_vector(out, log_integer_vector(num), scale)
    add_log_vector(out, log_integer_vector(den), -scale)
    return out


def vector_to_json(v: dict[int, Fraction]) -> dict[str, str]:
    return {str(p): fstr(v[p]) for p in sorted(v) if v[p]}


def vector_equal(a: dict[int, Fraction], b: dict[int, Fraction]) -> bool:
    return {p: v for p, v in a.items() if v} == {p: v for p, v in b.items() if v}


def solve_linear(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix) or len(rhs) != n:
        raise VerificationError("invalid square linear system")
    aug = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise VerificationError("singular Green Gram")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor:
                aug[r] = [aug[r][j] - factor * aug[col][j] for j in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def divisor_coordinate(b: list[Fraction], q: int, X: int) -> Fraction:
    total = Fraction(0)
    k = 1
    while k * q <= X:
        n = k * q
        total += b[n] - b[n + 1]
        k += 1
    return total


def formal_objective(b: list[Fraction], prime_powers: list[int], roots: dict[int, int], X: int) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for q in prime_powers:
        value = divisor_coordinate(b, q, X)
        if value:
            p = roots[q]
            out[p] = out.get(p, Fraction(0)) + value
    return {p: value for p, value in out.items() if value}


def build_profiles(X: int, prime_powers: list[int]) -> dict[int, list[Fraction]]:
    profiles: dict[int, list[Fraction]] = {}
    for q in prime_powers:
        ux = 1 if X % q == 0 else 0
        row = [Fraction(0) for _ in range(X + 1)]
        for j in range(1, X + 1):
            row[j] = Fraction(1 if j % q == 0 else 0) - Fraction(j, X) * ux
        if row[0] != 0 or row[X] != 0:
            raise AssertionError("endpoint projection failed")
        profiles[q] = row
    return profiles


def build_gram(X: int, prime_powers: list[int], profiles: dict[int, list[Fraction]]) -> list[list[Fraction]]:
    gram: list[list[Fraction]] = []
    for q in prime_powers:
        row: list[Fraction] = []
        for d in prime_powers:
            value = sum(
                (profiles[q][j + 1] - profiles[q][j])
                * (profiles[d][j + 1] - profiles[d][j])
                for j in range(X)
            )
            row.append(value)
        gram.append(row)
    return gram


def layer_cake(values: list[Fraction], X: int) -> list[dict[str, Any]]:
    positive_levels = sorted({values[m] for m in range(2, X + 1) if values[m] > 0})
    previous = Fraction(0)
    blocks: list[dict[str, Any]] = []
    for level in positive_levels:
        height = level - previous
        active = [values[m] >= level for m in range(X + 1)]
        m = 2
        while m <= X:
            if not active[m]:
                m += 1
                continue
            start = m
            while m + 1 <= X and active[m + 1]:
                m += 1
            end = m
            blocks.append({"start": start, "end": end, "height": height})
            m += 1
        previous = level
    return blocks


def verify_certificate(cert: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(cert, dict):
        raise VerificationError("certificate must be an object")
    if cert.get("schema") != SCHEMA:
        raise VerificationError("schema mismatch")
    X = parse_int(cert.get("X"), "X")
    if X < 3:
        raise VerificationError("X must be at least 3")

    prime_powers, roots = prime_powers_upto(X)
    if cert.get("prime_powers") != prime_powers:
        raise VerificationError("prime-power manifest mismatch")

    seed_data = cert.get("seed_b")
    target_data = cert.get("target_w")
    if not isinstance(seed_data, dict) or not isinstance(target_data, dict):
        raise VerificationError("seed_b and target_w must be objects")

    b0 = [Fraction(0) for _ in range(X + 2)]
    for m in range(2, X + 1):
        key = str(m)
        if key not in seed_data:
            raise VerificationError(f"missing seed_b[{m}]")
        b0[m] = parse_fraction(seed_data[key], f"seed_b[{m}]")
        if b0[m] < 0:
            raise VerificationError("seed must be nonnegative")

    w: dict[int, Fraction] = {}
    for q in prime_powers:
        key = str(q)
        if key not in target_data:
            raise VerificationError(f"missing target_w[{q}]")
        w[q] = parse_fraction(target_data[key], f"target_w[{q}]")

    profiles = build_profiles(X, prime_powers)
    gram = build_gram(X, prime_powers, profiles)
    v0 = [divisor_coordinate(b0, q, X) for q in prime_powers]
    residual = [v0[i] - w[q] for i, q in enumerate(prime_powers)]
    T = solve_linear(gram, residual)

    for i in range(len(prime_powers)):
        lhs = sum(gram[i][j] * T[j] for j in range(len(prime_powers)))
        if lhs != residual[i]:
            raise AssertionError("Green solve replay failed")

    potential = [
        sum(T[i] * profiles[q][j] for i, q in enumerate(prime_powers))
        for j in range(X + 1)
    ]
    if potential[0] != 0 or potential[X] != 0:
        raise AssertionError("Green potential endpoint failure")

    b_star = list(b0)
    for m in range(2, X + 1):
        b_star[m] += potential[m - 1] - potential[m]
    for q in prime_powers:
        if divisor_coordinate(b_star, q, X) != w[q]:
            raise AssertionError("exact Green equality failed")

    correction = [b_star[m] - b0[m] for m in range(X + 2)]
    gamma = [Fraction(0) for _ in range(X + 1)]
    for m in range(2, X + 1):
        gamma[m] = correction[m] - correction[m + 1]
    induced_h = {q: divisor_coordinate(correction, q, X) for q in range(2, X + 1)}
    mu = mobius_table(X)
    for m in range(2, X + 1):
        decoded = sum(mu[k] * induced_h[m * k] for k in range(1, X // m + 1))
        if decoded != gamma[m]:
            raise AssertionError("Möbius--Poisson decoder failed")
        if sum(gamma[n] for n in range(m, X + 1)) != correction[m]:
            raise AssertionError("Poisson recovery failed")

    obstacle = [Fraction(0) for _ in range(X + 2)]
    b_clip = list(b_star)
    for m in range(2, X + 1):
        obstacle[m] = max(Fraction(0), -b_star[m])
        b_clip[m] += obstacle[m]
        if b_clip[m] < 0:
            raise AssertionError("clipping failed")

    epsilon = {q: divisor_coordinate(b_clip, q, X) - w[q] for q in prime_powers}
    blocks = layer_cake(obstacle, X)
    reconstructed = [Fraction(0) for _ in range(X + 2)]
    dipole = {q: Fraction(0) for q in prime_powers}
    for block in blocks:
        start = int(block["start"])
        end = int(block["end"])
        height = Fraction(block["height"])
        for m in range(start, end + 1):
            reconstructed[m] += height
        A = start - 1
        B = end
        for q in prime_powers:
            dipole[q] += height * ((1 if B % q == 0 else 0) - (1 if A % q == 0 else 0))
    if reconstructed != obstacle:
        raise AssertionError("layer-cake reconstruction failed")
    if dipole != epsilon:
        raise AssertionError("signed dipole recombination failed")

    P_formal: dict[int, Fraction] = {}
    for q in prime_powers:
        P_formal[roots[q]] = P_formal.get(roots[q], Fraction(0)) + w[q]
    J_clip = formal_objective(b_clip, prime_powers, roots, X)
    D_plus: dict[int, Fraction] = {}
    D_minus: dict[int, Fraction] = {}
    for q in prime_powers:
        value = epsilon[q]
        if value > 0:
            D_plus[roots[q]] = D_plus.get(roots[q], Fraction(0)) + value
        elif value < 0:
            D_minus[roots[q]] = D_minus.get(roots[q], Fraction(0)) - value

    lower = dict(J_clip)
    add_log_vector(lower, D_plus, Fraction(-1))
    upper = dict(J_clip)
    add_log_vector(upper, D_minus, Fraction(1))
    expected_lower = dict(P_formal)
    add_log_vector(expected_lower, D_minus, Fraction(-1))
    expected_upper = dict(P_formal)
    add_log_vector(expected_upper, D_plus, Fraction(1))
    if not vector_equal(lower, expected_lower):
        raise AssertionError("lower dipole certificate identity failed")
    if not vector_equal(upper, expected_upper):
        raise AssertionError("upper dipole certificate identity failed")

    sigma = [Fraction(0) for _ in range(X + 2)]
    for m in range(2, X + 1):
        sigma[m] = max(sigma[m - 1], obstacle[m])
    tau = [Fraction(0) for _ in range(X + 2)]
    for m in range(X, 1, -1):
        tau[m] = max(tau[m + 1], obstacle[m])
    lam = [Fraction(0) for _ in range(X + 2)]
    nu = [Fraction(0) for _ in range(X + 2)]
    for j in range(2, X + 1):
        lam[j] = sigma[j] - sigma[j - 1]
        nu[j] = tau[j] - tau[j + 1]
        if lam[j] < 0 or nu[j] < 0:
            raise AssertionError("Skorokhod contact increments must be nonnegative")

    b_lower = [b_star[m] + sigma[m] for m in range(X + 2)]
    b_upper = [b_star[m] + tau[m] for m in range(X + 2)]
    if min(b_lower[2 : X + 1]) < 0 or min(b_upper[2 : X + 1]) < 0:
        raise AssertionError("Skorokhod reflected vector is negative")

    lower_res = {q: divisor_coordinate(b_lower, q, X) - w[q] for q in prime_powers}
    upper_res = {q: divisor_coordinate(b_upper, q, X) - w[q] for q in prime_powers}
    for q in prime_powers:
        predicted_lower = sum(
            lam[j] * ((1 if X % q == 0 else 0) - (1 if (j - 1) % q == 0 else 0))
            for j in range(2, X + 1)
        )
        predicted_upper = sum(nu[j] * (1 if j % q == 0 else 0) for j in range(2, X + 1))
        if lower_res[q] != predicted_lower or upper_res[q] != predicted_upper:
            raise AssertionError("Skorokhod incidence formula failed")
        if X % q != 0 and lower_res[q] > 0:
            raise AssertionError("prefix reflection has a non-endpoint positive residual")
        if upper_res[q] < 0:
            raise AssertionError("suffix reflection is not a cover")

    endpoint_charge: dict[int, Fraction] = {}
    for q in prime_powers:
        if X % q == 0:
            p = roots[q]
            endpoint_charge[p] = endpoint_charge.get(p, Fraction(0)) + lower_res[q]

    J_lower = formal_objective(b_lower, prime_powers, roots, X)
    scalar_lower = dict(J_lower)
    add_log_vector(scalar_lower, endpoint_charge, Fraction(-1))
    prefix_gap = dict(P_formal)
    add_log_vector(prefix_gap, scalar_lower, Fraction(-1))

    contact_gap: dict[int, Fraction] = {}
    import math
    for j in range(2, X + 1):
        if lam[j]:
            g = math.gcd(X, j - 1)
            add_log_vector(contact_gap, log_ratio_vector(j - 1, g), lam[j])
    if not vector_equal(prefix_gap, contact_gap):
        raise AssertionError("prefix contact-debt identity failed")

    J_upper = formal_objective(b_upper, prime_powers, roots, X)
    suffix_gap = dict(J_upper)
    add_log_vector(suffix_gap, P_formal, Fraction(-1))
    suffix_contact: dict[int, Fraction] = {}
    for j in range(2, X + 1):
        if nu[j]:
            add_log_vector(suffix_contact, log_integer_vector(j), nu[j])
    if not vector_equal(suffix_gap, suffix_contact):
        raise AssertionError("suffix contact-debt identity failed")

    result = {
        "schema": SCHEMA,
        "classification": "EXACT_FINITE_GREEN_DIPOLE_SKOROKHOD_ALGEBRA",
        "X": X,
        "prime_powers": prime_powers,
        "green_rank": len(prime_powers),
        "green_solution": [fstr(x) for x in T],
        "minimum_green_coordinate": fstr(min(b_star[2 : X + 1])),
        "negative_green_coordinates": [m for m in range(2, X + 1) if b_star[m] < 0],
        "dipole_blocks": [
            {"start": int(b["start"]), "end": int(b["end"]), "height": fstr(Fraction(b["height"]))}
            for b in blocks
        ],
        "formal_prime_ramp": vector_to_json(P_formal),
        "clipped_positive_residual": vector_to_json(D_plus),
        "clipped_negative_residual": vector_to_json(D_minus),
        "clipped_lower": vector_to_json(lower),
        "clipped_upper": vector_to_json(upper),
        "prefix_contact_gap": vector_to_json(contact_gap),
        "suffix_contact_gap": vector_to_json(suffix_contact),
        "mobius_poisson_rows": X - 1,
        "verdict": "PASS_EXACT_GREEN_DIPOLE_SKOROKHOD_INTERFACES",
        "proof_boundary": (
            "Exact finite algebra only. The checker does not prove the cofinal "
            "Green contact-debt theorem, the prime-ramp asymptotic, or RH."
        ),
    }

    expected = cert.get("expected")
    if expected is not None:
        if not isinstance(expected, dict):
            raise VerificationError("expected must be an object")
        for key, value in expected.items():
            if result.get(key) != value:
                raise VerificationError(f"expected field mismatch: {key}")

    digest_payload = dict(result)
    result["proof_sha256"] = canonical_sha(digest_payload)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cert = json.loads(args.certificate.read_text(encoding="utf-8"))
    result = verify_certificate(cert)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
