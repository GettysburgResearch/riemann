#!/usr/bin/env python3
"""Finite diagnostics for the first-Hermite large-value theorem.

This script checks finite identities and scale laws only.  It does not prove
the analytic large-value theorem, the first-Hermite sign, or RH.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path
from typing import Dict, List


def von_mangoldt_sieve(limit: int) -> List[float]:
    """Return Lambda(n), 0 <= n <= limit, using prime powers."""
    lam = [0.0] * (limit + 1)
    is_prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        is_prime[0] = 0
    if limit >= 1:
        is_prime[1] = 0
    for p in range(2, limit + 1):
        if not is_prime[p]:
            continue
        lp = math.log(p)
        power = p
        while power <= limit:
            lam[power] = lp
            if power > limit // p:
                break
            power *= p
        if p * p <= limit:
            start = p * p
            step = p
            is_prime[start : limit + 1 : step] = b"\x00" * (((limit - start) // step) + 1)
    return lam


def hermite_weight(u: float, q: float) -> float:
    return (1.0 - u * u / (2.0 * q)) * math.exp(-u * u / (4.0 * q))


def coefficients(lam: List[float], q: float) -> List[float]:
    out = [0.0] * len(lam)
    for n in range(2, len(lam)):
        if lam[n] == 0.0:
            continue
        u = math.log(n)
        out[n] = lam[n] * hermite_weight(u, q) / math.sqrt(n)
    return out


def coefficient_energy_rows(lam: List[float]) -> List[Dict[str, float]]:
    rows = []
    for q in (2.0, 4.0, 8.0):
        coeff = coefficients(lam, q)
        energy = sum(x * x for x in coeff)
        rows.append(
            {
                "q": q,
                "energy": energy,
                "energy_over_q": energy / q,
                "absolute_error_from_q": abs(energy - q),
                "error_over_sqrt_q": abs(energy - q) / math.sqrt(q),
            }
        )
    return rows


def prime_block_rows(lam: List[float]) -> List[Dict[str, float]]:
    rows: List[Dict[str, float]] = []
    primes = (2, 3, 5, 11, 29)
    for q in (1.0, 4.0, 16.0):
        coeff = coefficients(lam, q)
        for p in primes:
            block_l1 = 0.0
            power = p
            while power < len(coeff):
                block_l1 += abs(coeff[power])
                if power > (len(coeff) - 1) // p:
                    break
                power *= p
            elementary = 3.0 * math.log(p) / (math.sqrt(p) - 1.0)
            rows.append(
                {
                    "q": q,
                    "prime": p,
                    "block_l1": block_l1,
                    "elementary_bound": elementary,
                    "bound_holds": block_l1 <= elementary + 1e-12,
                }
            )
    return rows


def torus_moment_control(lam: List[float]) -> Dict[str, object]:
    """Exact finite root-of-unity average for four prime blocks."""
    q = 3.0
    coeff = coefficients(lam, q)
    primes = (2, 3, 5, 7)
    order = 12
    blocks: Dict[int, List[float]] = {}
    for p in primes:
        arr = []
        power = p
        while power < len(coeff):
            arr.append(coeff[power])
            if power > (len(coeff) - 1) // p:
                break
            power *= p
        blocks[p] = arr

    moments = {1: 0.0, 2: 0.0, 3: 0.0}
    count = order ** len(primes)
    for idx in range(count):
        digits = []
        r = idx
        for _ in primes:
            digits.append(r % order)
            r //= order
        total = 0j
        for p, d in zip(primes, digits):
            z = cmath.exp(2j * math.pi * d / order)
            zp = z
            for a in blocks[p]:
                total += a * zp
                zp *= z
        abs2 = total.real * total.real + total.imag * total.imag
        moments[1] += abs2
        moments[2] += abs2 * abs2
        moments[3] += abs2 * abs2 * abs2

    for k in moments:
        moments[k] /= count

    variance = sum(a * a for p in primes for a in blocks[p])
    rows = []
    constant = 100.0
    for k in (1, 2, 3):
        bound = (constant * k * (variance + k)) ** k
        rows.append(
            {
                "k": k,
                "moment_2k": moments[k],
                "bernstein_moment_bound": bound,
                "bound_holds": moments[k] <= bound,
            }
        )
    return {
        "q": q,
        "root_order": order,
        "prime_blocks": list(primes),
        "variance": variance,
        "rows": rows,
    }


def time_mean_square_control(lam: List[float]) -> Dict[str, float]:
    q = 3.0
    cutoff = 500
    coeff = coefficients(lam[: cutoff + 1], q)
    variance = sum(a * a for a in coeff)
    x0 = 10000.0
    length = 2400.0
    samples = 12000
    total = 0.0
    for j in range(samples):
        x = x0 + length * (j + 0.5) / samples
        value = 0j
        for n in range(2, len(coeff)):
            a = coeff[n]
            if a:
                value += a * cmath.exp(1j * x * math.log(n))
        total += abs(value) ** 2
    average = total / samples
    return {
        "q": q,
        "cutoff": cutoff,
        "interval_start": x0,
        "interval_length": length,
        "samples": samples,
        "coefficient_energy": variance,
        "sampled_mean_square": average,
        "ratio": average / variance,
    }


def gaussian_tail_rows() -> List[Dict[str, float]]:
    rows = []
    b = 8.0
    for q in (1.0, 2.0, 4.0, 8.0, 16.0):
        u = b * q
        exponent = u / 2.0 - u * u / (4.0 * q)
        completed = q / 4.0 - (u - q) ** 2 / (4.0 * q)
        rows.append(
            {
                "q": q,
                "B": b,
                "boundary_exponent": exponent,
                "completed_square": completed,
                "identity_error": abs(exponent - completed),
                "decay_at_least_exp_minus_12q": exponent <= -12.0 * q + 1e-12,
            }
        )
    return rows


def exceptional_optimization_rows() -> Dict[str, object]:
    """Check the deterministic parameter optimization in the union bound."""
    eps = 0.25
    kappa = 1.0 / 50.0
    B = 8.0
    model_C = 8.0
    rows = []
    for L in (1e8, 1e12, 1e16, 1e20, 1e24):
        Q = L ** (1.0 - eps)
        k = max(1, int(kappa * L / (Q + 1.0)))
        length_exponent = B * k * Q / L
        base = model_C * k * (Q + k) / (L * L)
        log_union_fraction = math.log(Q) + k * math.log(max(base, 1e-300))
        rows.append(
            {
                "log_height_L": L,
                "Q": Q,
                "k_at_worst_q": k,
                "Bkq_over_L": length_exponent,
                "markov_base_model": base,
                "log_union_fraction_model": log_union_fraction,
            }
        )
    return {
        "epsilon": eps,
        "kappa": kappa,
        "truncation_B": B,
        "model_constant": model_C,
        "rows": rows,
        "eventual_length_budget": all(row["Bkq_over_L"] < 0.25 for row in rows),
        "union_fraction_strictly_decreases": all(
            rows[i + 1]["log_union_fraction_model"] < rows[i]["log_union_fraction_model"]
            for i in range(len(rows) - 1)
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    parser.add_argument("--limit", type=int, default=250000)
    args = parser.parse_args()

    lam = von_mangoldt_sieve(args.limit)
    energy = coefficient_energy_rows(lam)
    prime_blocks = prime_block_rows(lam)
    torus = torus_moment_control(lam)
    mean_square = time_mean_square_control(lam)
    tails = gaussian_tail_rows()
    optimization = exceptional_optimization_rows()

    gates = {
        "coefficient_energy_scale": all(
            0.65 <= row["energy_over_q"] <= 1.35 for row in energy
        ),
        "prime_block_uniform_bound": all(row["bound_holds"] for row in prime_blocks),
        "finite_torus_moment_bound": all(row["bound_holds"] for row in torus["rows"]),
        "time_mean_square_matches_energy": 0.65 <= mean_square["ratio"] <= 1.35,
        "gaussian_truncation_tail": all(
            row["decay_at_least_exp_minus_12q"] and row["identity_error"] < 1e-12
            for row in tails
        ),
        "exceptional_optimization": optimization["eventual_length_budget"]
        and optimization["union_fraction_strictly_decreases"],
    }
    if not all(gates.values()):
        raise SystemExit(f"verification gate failed: {gates}")

    result = {
        "status": "PASS_FIRST_HERMITE_LARGE_VALUES",
        "parameters": {"von_mangoldt_limit": args.limit},
        "gates": gates,
        "coefficient_energy": energy,
        "prime_blocks": prime_blocks,
        "torus_moments": torus,
        "time_mean_square": mean_square,
        "gaussian_tail": tails,
        "exceptional_optimization": optimization,
    }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json is None:
        print(text, end="")
    else:
        args.json.write_text(text, encoding="utf-8")
        print(result["status"])


if __name__ == "__main__":
    main()
