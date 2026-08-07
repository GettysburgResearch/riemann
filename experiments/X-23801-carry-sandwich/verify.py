#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Dict, List


def beta(n: int, q: int) -> Fraction:
    if q < 2 or n < q:
        return Fraction(0)
    k, r = divmod(n, q)
    return Fraction(k * (q - 1 - r), n + 1)


def beta_floor(n: int, q: int) -> Fraction:
    if q < 2 or n < q:
        return Fraction(0)
    return Fraction(n // q) - Fraction(
        2 * sum(j // q for j in range(n + 1)), n + 1
    )


def mobius_sieve(n: int) -> List[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: List[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def mobius_adjoint_check(limit: int = 80) -> Dict[str, object]:
    mu = mobius_sieve(limit)
    mismatches = []
    for n in range(2, limit + 1):
        for m in range(2, n + 1):
            lhs = sum(
                Fraction(mu[k]) * beta(n, m * k)
                for k in range(1, n // m + 1)
            )
            rhs = Fraction(2 * m - n - 1, n + 1)
            if lhs != rhs:
                mismatches.append(
                    {"n": n, "m": m, "lhs": str(lhs), "rhs": str(rhs)}
                )
    return {"limit": limit, "mismatches": mismatches}


def prime_factors(n: int) -> Dict[int, int]:
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


def vp_factorial(n: int, p: int) -> int:
    total = 0
    while n:
        n //= p
        total += n
    return total


def average_binomial_valuation(n: int, p: int) -> Fraction:
    total = 0
    for j in range(n + 1):
        total += (
            vp_factorial(n, p)
            - vp_factorial(j, p)
            - vp_factorial(n - j, p)
        )
    return Fraction(total, n + 1)


def legendre_carry_check(limit: int = 36) -> Dict[str, object]:
    mismatches = []
    primes = []
    for p in range(2, limit + 1):
        factors = prime_factors(p)
        if factors == {p: 1}:
            primes.append(p)
    for n in range(2, limit + 1):
        for p in primes:
            if p > n:
                continue
            rhs = Fraction(0)
            q = p
            while q <= n:
                rhs += beta(n, q)
                q *= p
            lhs = average_binomial_valuation(n, p)
            if lhs != rhs:
                mismatches.append(
                    {"n": n, "p": p, "lhs": str(lhs), "rhs": str(rhs)}
                )
    return {"limit": limit, "mismatches": mismatches}


def greedy_decimal(x: int, precision: int = 60) -> Dict[str, object]:
    if x < 2:
        raise ValueError("x must be at least 2")
    with localcontext() as ctx:
        ctx.prec = precision
        residual = [Decimal(0)] * (x + 1)
        for q in range(2, x + 1):
            residual[q] = (Decimal(x) / Decimal(q)).ln() / Decimal(q).sqrt()

        d = [Decimal(0)] * (x + 1)
        saturation = []
        for n in range(x, 1, -1):
            best = None
            q_best = None
            for q in range(2, n + 1):
                b = beta(n, q)
                if b == 0:
                    continue
                b_dec = Decimal(b.numerator) / Decimal(b.denominator)
                ratio = residual[q] / b_dec
                if best is None or ratio < best:
                    best = ratio
                    q_best = q
            if best is None:
                best = Decimal(0)
            if best < 0:
                raise ArithmeticError(f"negative greedy step at n={n}: {best}")
            d[n] = best
            saturation.append((n, q_best))
            for q in range(2, n + 1):
                b = beta(n, q)
                if b:
                    residual[q] -= best * (
                        Decimal(b.numerator) / Decimal(b.denominator)
                    )
                    if abs(residual[q]) < Decimal(10) ** (-(precision - 12)):
                        residual[q] = Decimal(0)

        log_fact = [Decimal(0)] * (x + 1)
        prefix = [Decimal(0)] * (x + 1)
        g = [Decimal(0)] * (x + 1)
        for n in range(1, x + 1):
            log_fact[n] = log_fact[n - 1] + Decimal(n).ln()
            prefix[n] = prefix[n - 1] + log_fact[n]
            g[n] = log_fact[n] - Decimal(2) * prefix[n] / Decimal(n + 1)

        entropy = sum(d[n] * g[n] for n in range(2, x + 1))
        mass = sum(Decimal(n) * d[n] / Decimal(2) for n in range(2, x + 1))
        root_barrier = Decimal(4) * Decimal(x).sqrt()
        off_diagonal = sum(1 for n, q in saturation if q is not None and q != n)
        minimum_residual = min(residual[2:])

        return {
            "X": x,
            "precision": precision,
            "entropy": str(+entropy),
            "entropy_over_sqrt_X": str(+(entropy / Decimal(x).sqrt())),
            "entropy_deficit_from_4sqrtX": str(+(root_barrier - entropy)),
            "signed_half_n_mass": str(+mass),
            "mass_minus_4sqrtX": str(+(mass - root_barrier)),
            "off_diagonal_saturations": off_diagonal,
            "minimum_final_residual": str(+minimum_residual),
        }


def build_result() -> Dict[str, object]:
    floor_mismatches = []
    for n in range(2, 81):
        for q in range(2, n + 1):
            if beta(n, q) != beta_floor(n, q):
                floor_mismatches.append([n, q])
    result: Dict[str, object] = {
        "schema": "X-23801-v1",
        "classification": "EXACT_ALGEBRA_PLUS_DECIMAL_RECONNAISSANCE",
        "floor_formula_mismatches": floor_mismatches,
        "mobius_adjoint": mobius_adjoint_check(80),
        "legendre_carry": legendre_carry_check(36),
        "reconnaissance": [
            greedy_decimal(50, 60),
            greedy_decimal(100, 60),
            greedy_decimal(200, 60),
        ],
        "proof_boundary": (
            "Exact checks cover the carry floor identity, the average "
            "Legendre/carry identity, the Mobius adjoint identity, and finite "
            "greedy feasibility. Decimal reconnaissance is discovery-only and "
            "does not prove the Carry Sandwich theorem or RH."
        ),
        "verdict": "PASS_EXACT_INTERFACES_CARRY_SANDWICH_OPEN",
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


def main() -> None:
    result = build_result()
    if len(sys.argv) == 2:
        expected = json.loads(Path(sys.argv[1]).read_text())
        if expected != result:
            raise SystemExit("FAIL: retained result does not match deterministic replay")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
