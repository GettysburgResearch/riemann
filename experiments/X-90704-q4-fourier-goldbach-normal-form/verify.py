#!/usr/bin/env python3
"""Exact/floating replay for the Q4 Fourier--Goldbach normal form.

The checker verifies:
* the exact generic row-energy expansion over rational increment sequences;
* the cyclic Fourier diagonalisation and singular antiderivative formula;
* the exact sine-mode operator loss;
* the formal von-Mangoldt block-source identity in independent log(p) symbols.

It proves no arithmetic estimate, PIG, or RH.
"""
from __future__ import annotations

import cmath
from fractions import Fraction
import hashlib
import json
import math
import random
from pathlib import Path

STATUS = "PASS_X_90704_Q4_FOURIER_GOLDBACH_NORMAL_FORM"


def dft(values: list[float]) -> list[complex]:
    n = len(values)
    return [
        sum(values[j] * cmath.exp(-2j * math.pi * ell * j / n) for j in range(n))
        for ell in range(n)
    ]


def exact_generic_checks() -> int:
    rng = random.Random(90704)
    cases = 0
    for n in range(3, 81):
        for _ in range(18):
            b = [Fraction(0)] + [
                Fraction(rng.randint(-20, 20), rng.randint(1, 17))
                for _m in range(1, n + 1)
            ]
            B = [Fraction(0)]
            for m in range(1, n + 1):
                B.append(B[-1] + b[m])
            c = Fraction(rng.randint(-12, 12), rng.randint(1, 11))
            C = B[n] - c

            direct = sum(
                (C - B[j] - B[n - j]) ** 2 for j in range(1, n)
            )
            r1 = sum((n - m) * b[m] for m in range(1, n))
            rmax = sum(
                (n - max(a, d)) * b[a] * b[d]
                for a in range(1, n)
                for d in range(1, n)
            )
            rplus = sum(
                (n + 1 - a - d) * b[a] * b[d]
                for a in range(1, n + 1)
                for d in range(1, n + 1)
                if a + d <= n
            )
            physical = (n - 1) * C * C - 4 * C * r1 + 2 * rmax + 2 * rplus
            if direct != physical:
                raise AssertionError(("physical expansion", n, direct, physical))

            S = sum(B[:n], Fraction(0))
            zero_mode = n * C - 2 * S
            moment_mode = sum((2 * m - n) * b[m] for m in range(1, n + 1)) - n * c
            if zero_mode != moment_mode:
                raise AssertionError(("zero mode", n))

            # The artificial cyclic completion differs from the physical rows only at j=0.
            cyclic = [C - B[j] - B[(-j) % n] for j in range(n)]
            if cyclic[0] != C:
                raise AssertionError(("cyclic endpoint", n))
            if sum(x * x for x in cyclic) - C * C != direct:
                raise AssertionError(("cyclic parseval exact", n))
            cases += 1
    return cases


def floating_fourier_checks() -> tuple[int, float]:
    rng = random.Random(17090704)
    cases = 0
    max_error = 0.0
    for n in range(3, 100):
        b = [0.0] + [rng.uniform(-2.0, 2.0) for _ in range(n)]
        B = [0.0]
        for m in range(1, n + 1):
            B.append(B[-1] + b[m])
        c = rng.uniform(-2.0, 2.0)
        C = B[n] - c
        cyclic = [C - B[j] - B[(-j) % n] for j in range(n)]
        yhat = dft(cyclic)
        bhat = dft(B[:n])
        S = sum(B[:n])
        max_error = max(max_error, abs(yhat[0] - (n * C - 2 * S)))
        for ell in range(1, n):
            max_error = max(max_error, abs(yhat[ell] + 2.0 * bhat[ell].real))
            q = cmath.exp(-2j * math.pi * ell / n)
            increment_formula = sum(
                b[m] * (q**m - 1.0) for m in range(1, n + 1)
            ) / (1.0 - q)
            max_error = max(max_error, abs(bhat[ell] - increment_formula))
        direct = sum((C - B[j] - B[n - j]) ** 2 for j in range(1, n))
        spectral = (
            abs(n * C - 2 * S) ** 2
            + 4.0 * sum((bhat[ell].real) ** 2 for ell in range(1, n))
        ) / n - C * C
        max_error = max(max_error, abs(direct - spectral) / max(1.0, abs(direct)))
        cases += 1
    if max_error > 2e-10:
        raise AssertionError(("Fourier residual", max_error))
    return cases, max_error


def sine_mode_checks() -> tuple[int, float]:
    max_error = 0.0
    cases = 0
    for n in range(3, 401):
        theta = 2.0 * math.pi / n
        b = [0.0] + [math.sin(theta * m) for m in range(1, n + 1)]
        B = [0.0]
        for m in range(1, n + 1):
            B.append(B[-1] + b[m])
        direct = sum((-B[j] - B[n - j]) ** 2 for j in range(1, n))
        expected = 1.5 * n / (math.tan(math.pi / n) ** 2)
        input_energy = sum(value * value for value in b[1:])
        ratio = math.sqrt(direct / input_energy)
        expected_ratio = math.sqrt(3.0) / math.tan(math.pi / n)
        max_error = max(
            max_error,
            abs(direct - expected) / expected,
            abs(ratio - expected_ratio) / expected_ratio,
        )
        cases += 1
    if max_error > 2e-11:
        raise AssertionError(("sine mode", max_error))
    return cases, max_error


def sieve(limit: int) -> tuple[list[int], list[int]]:
    spf = list(range(limit + 1))
    primes = []
    for i in range(2, limit + 1):
        if spf[i] == i:
            primes.append(i)
            if i * i <= limit:
                for j in range(i * i, limit + 1, i):
                    if spf[j] == j:
                        spf[j] = i
    return spf, primes


def lambda_symbol(n: int, spf: list[int]) -> dict[int, int]:
    if n <= 1:
        return {}
    p = spf[n]
    m = n
    while m % p == 0:
        m //= p
    return {p: 1} if m == 1 else {}


def add_symbol(a: dict[int, int], b: dict[int, int], scale: int = 1) -> dict[int, int]:
    out = dict(a)
    for p, value in b.items():
        out[p] = out.get(p, 0) + scale * value
        if out[p] == 0:
            del out[p]
    return out


def formal_prime_checks(limit: int = 250) -> tuple[int, int]:
    spf, primes = sieve(4 * limit)
    psi: list[dict[int, int]] = [{}]
    running: dict[int, int] = {}
    for n in range(1, 4 * limit + 1):
        running = add_symbol(running, lambda_symbol(n, spf))
        psi.append(dict(running))

    B = [{}]
    increments = [{}]
    cases = 0
    nonzero_symbols = 0
    for m in range(1, limit + 1):
        block = {}
        for r in range(4):
            block = add_symbol(block, lambda_symbol(4 * m - r, spf))
        block = add_symbol(block, lambda_symbol(m, spf), scale=-4)
        increments.append(block)
        expected_B = add_symbol(psi[4 * m], psi[m], scale=-4)
        B.append(expected_B)
        prefix = add_symbol(B[m - 1], block)
        if prefix != expected_B:
            raise AssertionError(("formal block prefix", m, prefix, expected_B))
        if block:
            nonzero_symbols += 1
        cases += 1
    return cases, nonzero_symbols


def main() -> dict[str, object]:
    exact_cases = exact_generic_checks()
    fourier_cases, fourier_error = floating_fourier_checks()
    sine_cases, sine_error = sine_mode_checks()
    formal_cases, formal_nonzero = formal_prime_checks()

    gates = {
        "exact_physical_goldbach_expansion": exact_cases > 1000,
        "cyclic_cosine_diagonalisation": fourier_error < 2e-10,
        "singular_antiderivative_formula": fourier_error < 2e-10,
        "exact_linear_sine_mode_loss": sine_error < 2e-11,
        "formal_radix_four_prime_block_identity": formal_cases == 250,
    }
    if not all(gates.values()):
        raise AssertionError([name for name, ok in gates.items() if not ok])

    result = {
        "status": STATUS,
        "gates": gates,
        "exact_rational_cases": exact_cases,
        "floating_fourier_cases": fourier_cases,
        "max_relative_fourier_error": fourier_error,
        "sine_mode_cases": sine_cases,
        "max_relative_sine_error": sine_error,
        "formal_prime_block_cases": formal_cases,
        "formal_nonzero_block_symbols": formal_nonzero,
        "scope": (
            "exact finite algebra and operator-class firewall only; "
            "the arithmetic Fourier/Goldbach estimate, PIG and RH remain open"
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


if __name__ == "__main__":
    result = main()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(STATUS)
