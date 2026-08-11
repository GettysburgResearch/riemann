#!/usr/bin/env python3
"""Finite diagnostics for the linear-resolution first-Hermite continuation.

This script checks only elementary envelopes, scaling laws, and the finite
Cauchy--Schwarz resonance certificate.  It does not prove the analytic
large-value theorem or RH.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable


def simpson(f, a: float, b: float, n: int) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4.0 if j % 2 else 2.0) * f(a + j * h)
    return total * h / 3.0


def tail_integral(a: float, q: float) -> float:
    start = a * q
    end = start + max(80.0, 30.0 * math.sqrt(q))
    def f(u: float) -> float:
        return u * (1.0 + u * u / (2.0 * q)) * math.exp(
            u / 2.0 - u * u / (4.0 * q)
        )
    return simpson(f, start, end, 40000)


def prime_powers(limit: int) -> list[tuple[int, int, float]]:
    """Return (n, underlying prime, Lambda(n)) for prime powers n<=limit."""
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    primes: list[int] = []
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)
            if p * p <= limit:
                sieve[p * p : limit + 1 : p] = b"\x00" * (
                    (limit - p * p) // p + 1
                )
    out: list[tuple[int, int, float]] = []
    for p in primes:
        n = p
        lp = math.log(p)
        while n <= limit:
            out.append((n, p, lp))
            if n > limit // p:
                break
            n *= p
    out.sort()
    return out


def hq(u: float, q: float) -> float:
    return (1.0 - u * u / (2.0 * q)) * math.exp(-u * u / (4.0 * q))


def minimal_positive_subset(values: Iterable[float], target: float) -> list[float]:
    positive = sorted((v for v in values if v > 0.0), reverse=True)
    chosen: list[float] = []
    total = 0.0
    for value in positive:
        chosen.append(value)
        total += value
        if total >= target:
            return chosen
    raise RuntimeError("target exceeds positive mass")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    a = 3.0

    completion_rows = []
    max_completion_error = 0.0
    for q in (1.0, 2.0, 5.0, 10.0, 25.0):
        for u in (a * q, a * q + 0.7, a * q + 3.0 * math.sqrt(q)):
            lhs = u / 2.0 - u * u / (4.0 * q)
            rhs = q / 4.0 - (u - q) ** 2 / (4.0 * q)
            err = abs(lhs - rhs)
            max_completion_error = max(max_completion_error, err)
        completion_rows.append(
            {
                "q": q,
                "boundary_exponent": a * q / 2.0 - (a * q) ** 2 / (4.0 * q),
                "predicted": -a * (a - 2.0) * q / 4.0,
            }
        )

    tail_rows = []
    tail_gate = True
    for q in (1.0, 2.0, 4.0, 8.0, 16.0):
        actual = tail_integral(a, q)
        c_a = a * (a - 2.0) / 4.0
        envelope = 5000.0 * (q + 1.0) ** 3 * math.exp(-c_a * q)
        tail_gate = tail_gate and actual <= envelope
        tail_rows.append(
            {
                "q": q,
                "numeric_continuum_tail": actual,
                "coarse_q3_exponential_envelope": envelope,
                "ratio": actual / envelope,
            }
        )

    union_rows = []
    union_gate = True
    for K in (3, 4, 5):
        for L in (240.0, 480.0, 960.0, 1920.0):
            Q = max(1, int(L // (4.0 * a * K)))
            raw = sum(
                (K * (q + K) / (L * L)) ** K for q in range(1, Q + 1)
            )
            scaled = raw / (L ** (1 - K))
            union_gate = union_gate and math.isfinite(scaled) and scaled < 1.0
            union_rows.append(
                {
                    "K": K,
                    "log_height": L,
                    "max_integer_q": Q,
                    "raw_union_model": raw,
                    "ratio_to_L_power_1_minus_K": scaled,
                }
            )

    refined_rows = []
    refined_gate = True
    kappa = 0.03
    for L in (10_000.0, 40_000.0, 160_000.0):
        for q in (10.0, math.sqrt(L), 0.02 * L):
            k = max(1, int(kappa * L / (a * (q + 1.0))))
            ratio = 20.0 * k * (q + k) / (L * L)
            exponent_proxy = (
                L
                / (q + 1.0)
                * math.log(2.0 + min(q, math.sqrt(L)))
            )
            refined_gate = refined_gate and ratio < 1.0
            refined_rows.append(
                {
                    "log_height": L,
                    "q": q,
                    "moment_order": k,
                    "moment_ratio_proxy": ratio,
                    "refined_exponent_proxy": exponent_proxy,
                }
            )

    # A concrete prime-power coefficient packet.
    q_packet = 4.0
    limit = int(math.exp(a * q_packet))
    packet = prime_powers(limit)
    coeffs: list[tuple[int, int, float]] = []
    for n, p, lam in packet:
        u = math.log(n)
        coeff = lam / math.sqrt(n) * hq(u, q_packet)
        coeffs.append((n, p, coeff))

    projections = [max(c, 0.0) for _, _, c in coeffs]
    positive_mass = sum(projections)
    target = 0.55 * positive_mass
    chosen_values = minimal_positive_subset(projections, target / 2.0)
    variance = sum(c * c for _, _, c in coeffs)
    cs_lower_bound = (target / 2.0) ** 2 / variance
    rigidity_gate = len(chosen_values) + 1e-12 >= cs_lower_bound

    # Reconstruct one minimal subset and count its underlying primes.
    positive_terms = sorted(
        ((max(c, 0.0), p, n) for n, p, c in coeffs if c > 0.0),
        reverse=True,
    )
    selected = []
    selected_sum = 0.0
    for value, p, n in positive_terms:
        selected.append((value, p, n))
        selected_sum += value
        if selected_sum >= target / 2.0:
            break
    selected_primes = {p for _, p, _ in selected}
    max_powers_per_prime = int(a * q_packet / math.log(2.0)) + 1
    distinct_prime_lower_bound = len(selected) / max_powers_per_prime
    distinct_gate = len(selected_primes) + 1e-12 >= distinct_prime_lower_bound


    synthetic_rows = []
    synthetic_gate = True
    for L_syn, q_syn in ((100.0, 10.0), (200.0, 10.0), (400.0, 20.0)):
        count = int(math.ceil(4.0 * L_syn * L_syn / q_syn))
        magnitude = math.sqrt(q_syn / count)
        H_syn = L_syn
        selected_count = int(math.ceil((H_syn / 2.0) / magnitude))
        cs_bound = (H_syn / 2.0) ** 2 / q_syn
        synthetic_gate = synthetic_gate and selected_count + 1e-12 >= cs_bound
        synthetic_rows.append(
            {
                "log_height": L_syn,
                "q": q_syn,
                "packet_terms": count,
                "coefficient_magnitude": magnitude,
                "selected_terms_for_half_threshold": selected_count,
                "cauchy_schwarz_lower_bound": cs_bound,
                "L_squared_over_q": L_syn * L_syn / q_syn,
            }
        )

    output = {
        "status": "PASS_LINEAR_RESOLUTION_FIRST_HERMITE_RIGIDITY",
        "parameters": {
            "adaptive_cutoff_a": a,
            "packet_q": q_packet,
            "packet_limit": limit,
        },
        "completion_of_square": {
            "max_error": max_completion_error,
            "rows": completion_rows,
        },
        "adaptive_tail": tail_rows,
        "fixed_moment_union": union_rows,
        "refined_moment_exponent": refined_rows,
        "synthetic_resonance_scaling": synthetic_rows,
        "finite_resonance_packet": {
            "prime_power_terms": len(coeffs),
            "positive_mass": positive_mass,
            "target_H": target,
            "coefficient_variance": variance,
            "selected_terms": len(selected),
            "cauchy_schwarz_term_lower_bound": cs_lower_bound,
            "selected_distinct_primes": len(selected_primes),
            "max_powers_per_prime": max_powers_per_prime,
            "distinct_prime_lower_bound": distinct_prime_lower_bound,
        },
        "gates": {
            "completion_of_square": max_completion_error < 1e-12,
            "adaptive_tail_envelope": tail_gate,
            "fixed_K_linear_resolution_union": union_gate,
            "refined_exponent_ratio": refined_gate,
            "prime_power_resonance_cauchy_schwarz": rigidity_gate,
            "distinct_prime_conversion": distinct_gate,
            "synthetic_L2_over_q_scaling": synthetic_gate,
        },
    }

    if not all(output["gates"].values()):
        raise SystemExit(json.dumps(output, indent=2, sort_keys=True))

    rendered = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
