#!/usr/bin/env python3
"""Exact finite audit of the native Newton compression identities.

This is a finite replay, not a proof of asymptotic Mobius cancellation.
No third-party packages are required. All acceptance comparisons use
integers or fractions.Fraction. Decimal displays are explicitly diagnostic.
"""

from __future__ import annotations

if not __debug__:
    raise RuntimeError(
        "Exact replay requires assertions: run Python without -O or -OO."
    )

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


SOURCE_COMMIT = "0f82df3bf1d0bc669a1bbca09f8404b77c6fecde"
SOURCE_PATH = (
    "standalone/2026-09-21-native-covariance-compression/PROOF.md"
)


def mobius_trial(n: int) -> int:
    """Primitive trial factorization, used only for the input prefix."""
    if n == 1:
        return 1
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    if n > 1:
        sign = -sign
    return sign


def mobius_euler(limit: int) -> list[int]:
    """Separate full-length linear sieve, used only for comparison."""
    mu = [0] * (limit + 1)
    mu[1] = 1
    least = [0] * (limit + 1)
    primes: list[int] = []
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            product = n * p
            if product > limit:
                break
            least[product] = p
            if n % p == 0:
                mu[product] = 0
                break
            mu[product] = -mu[n]
    return mu


def floor_cuberoot(n: int) -> int:
    """Integer cube root without floating point."""
    assert n >= 0
    lower, upper = 0, 1
    while upper**3 <= n:
        upper *= 2
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if middle**3 <= n:
            lower = middle
        else:
            upper = middle
    assert lower**3 <= n < (lower + 1) ** 3
    return lower


def newton_from_prefix(prefix: list[int], end: int):
    """Only the declared prefix is producer input."""
    y = len(prefix) - 1
    z = [0] * (y * y + 1)
    for a in range(1, y + 1):
        for c in range(1, y + 1):
            z[a * c] += prefix[a] * prefix[c]
    v = [0] * (end + 1)
    for n in range(1, y + 1):
        v[n] = 2 * prefix[n]
    for d in range(1, len(z)):
        if z[d]:
            for n in range(d, end + 1, d):
                v[n] -= z[d]
    return z, v


def reciprocal_prefix(coefficients: list[int]) -> list[Fraction]:
    values = [Fraction(0)]
    running = Fraction(0)
    for n in range(1, len(coefficients)):
        running += Fraction(coefficients[n], n)
        values.append(running)
    return values


def mesh(b: int, q: int) -> list[tuple[int, int, int, int]]:
    """Blocks (left, length, annulus-left, untruncated-annulus-step)."""
    assert b >= 2 and q >= 1
    blocks: list[tuple[int, int, int, int]] = []
    x = b
    while x < b * b:
        endpoint = min(2 * x, b * b)
        # floor(cuberoot(A/b)) == floor(cuberoot(floor(A/b))).
        h = max(1, floor_cuberoot((q**3 * x * x) // b))
        a = x
        while a < endpoint:
            length = min(h, endpoint - a)
            blocks.append((a, length, x, h))
            a += length
        x *= 2
    assert blocks[0][0] == b
    cursor = b
    for a, length, x, h in blocks:
        assert a == cursor and 1 <= length <= h
        assert x <= a < a + length <= min(2 * x, b * b)
        cursor += length
    assert cursor == b * b
    assert sum(length for _, length, _, _ in blocks) == b * b - b
    return blocks


def block_stats(values: list[Fraction], blocks):
    coarse = Fraction(0)
    detail = Fraction(0)
    deterministic_bound = Fraction(0)
    means: list[Fraction] = []
    for a, h, _, _ in blocks:
        mean = sum(values[a : a + h], Fraction(0)) / h
        means.append(mean)
        coarse += h * mean * mean
        detail += sum(
            ((value - mean) ** 2 for value in values[a : a + h]),
            Fraction(0),
        )
        deterministic_bound += Fraction(h * (h * h - 1), 12 * a * a)
    return coarse, detail, deterministic_bound, means


def harmonic_primitive(t: int, d: int, harmonic) -> Fraction:
    quotient = (t - 1) // d
    return t * harmonic[quotient] - d * quotient


def exact_case(y: int, q: int) -> dict:
    b = y + 1
    endpoint = b * b
    n = endpoint - 1
    prefix = [0] + [mobius_trial(k) for k in range(1, y + 1)]
    z, produced = newton_from_prefix(prefix, endpoint)
    comparison = mobius_euler(endpoint)

    assert prefix == comparison[: y + 1], "Primitive-prefix disagreement"
    assert produced[1:endpoint] == comparison[1:endpoint], (
        "Strict square-step coefficient reconstruction failed"
    )
    # The first possibly nonzero Newton error is exactly mu(b)^2.
    endpoint_defect = comparison[endpoint] - produced[endpoint]
    assert endpoint_defect == comparison[b] ** 2
    if comparison[b] != 0:
        assert produced[endpoint] != comparison[endpoint], (
            "The excluded endpoint should detect an invalid extension"
        )

    values = reciprocal_prefix(produced[:endpoint])
    reference_values = reciprocal_prefix(comparison[:endpoint])
    assert values == reference_values
    harmonic = reciprocal_prefix([0] + [1] * n)
    blocks = mesh(b, q)
    coarse, detail, bound, means = block_stats(values, blocks)
    full = sum((value * value for value in values[b:]), Fraction(0))
    assert full == coarse + detail
    assert 0 <= detail <= bound
    assert len(values[b:]) == b * b - b

    nonzero_z = [(d, value) for d, value in enumerate(z) if value]
    for (a, h, _, _), mean in zip(blocks, means):
        source_mean = 2 * values[y] - sum(
            (
                Fraction(value, d)
                * (
                    harmonic_primitive(a + h, d, harmonic)
                    - harmonic_primitive(a, d, harmonic)
                )
                for d, value in nonzero_z
            ),
            Fraction(0),
        ) / h
        assert source_mean == mean, "Exact old-prefix quadratic mean failed"

    # The delta source has zero detail but quadratic coarse energy.
    delta_values = [Fraction(0)] + [Fraction(1)] * n
    delta_coarse, delta_detail, _, _ = block_stats(delta_values, blocks)
    assert delta_detail == 0
    assert delta_coarse == b * b - b
    assert sum((v * v for v in delta_values[1:b]), Fraction(0)) == y

    # A positive source retains the deterministic variation obstruction.
    _, positive_detail, positive_bound, _ = block_stats(harmonic, blocks)
    assert positive_detail <= positive_bound
    positive_lower_checked = False
    if b & (b - 1) == 0:
        x = b * b // 2
        h = max(1, floor_cuberoot((q**3 * x * x) // b))
        unfloored_cuberoot_ge_2 = q**3 * x * x >= 8 * b
        if h >= 2 and h <= b * b // 4 and unfloored_cuberoot_ge_2:
            assert positive_detail >= Fraction(q * q, 2048)
            positive_lower_checked = True

    return {
        "Y": y,
        "b": b,
        "q": q,
        "strict_last_native_cell": n,
        "complete_output_cell_count": b * b - b,
        "source_prefix_sha256": hashlib.sha256(
            json.dumps(prefix, separators=(",", ":")).encode()
        ).hexdigest(),
        "block_count": len(blocks),
        "strict_coefficient_replay": True,
        "excluded_endpoint_defect": endpoint_defect,
        "excluded_endpoint_defect_expected": comparison[b] ** 2,
        "exact_quadratic_means": True,
        "exact_complete_energy_identity": True,
        "exact_detail_le_deterministic_bound": True,
        "delta_source_control": True,
        "positive_source_lower_bound_checked": positive_lower_checked,
        "diagnostic_decimal_values_not_acceptance_bounds": {
            "annular_energy": float(full),
            "coarse_energy": float(coarse),
            "detail_energy": float(detail),
            "deterministic_detail_bound": float(bound),
            "positive_source_detail": float(positive_detail),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("audit.json"))
    args = parser.parse_args()
    cases = []
    for y in (1, 2, 3, 4, 7, 10, 15, 31):
        # q=1 is r=0; q=b.bit_length() is r=1. q=2 is an
        # extra fixed-multiplier exact-identity check.
        for q in sorted({1, 2, (y + 1).bit_length()}):
            cases.append(exact_case(y, q))
    assert any(c["excluded_endpoint_defect"] == 1 for c in cases)
    assert any(c["positive_source_lower_bound_checked"] for c in cases)
    assert any(
        c["diagnostic_decimal_values_not_acceptance_bounds"]["detail_energy"]
        > 0
        for c in cases
    )
    here = Path(__file__).resolve().parent
    output = {
        "status": "PASS: exact finite replay only",
        "arithmetic": "Python integers and fractions.Fraction",
        "acceptance": (
            "All assertions pass; exact coefficient comparisons and exact "
            "rational energy/coordinate identities on every declared cell."
        ),
        "primitive_source": "Trial factorization of every integer 1..Y",
        "comparison_source": "Separate full-length Euler linear Mobius sieve",
        "independent_review_claimed": False,
        "asymptotic_theorem_computationally_verified": False,
        "source_repository_commit": SOURCE_COMMIT,
        "source_repository_path": SOURCE_PATH,
        "producer_checker_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "proof_sha256": hashlib.sha256(
            (here / "PROOF.md").read_bytes()
        ).hexdigest(),
        "case_count": len(cases),
        "complete_case_grid_Y": [1, 2, 3, 4, 7, 10, 15, 31],
        "complete_case_grid_q": "distinct q in {1, 2, bit_length(Y+1)}",
        "cases": cases,
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({
        "status": output["status"],
        "case_count": len(cases),
        "largest_Y": max(c["Y"] for c in cases),
        "largest_strict_native_endpoint": max(
            c["strict_last_native_cell"] for c in cases
        ),
        "output": str(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
