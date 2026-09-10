#!/usr/bin/env python3
"""Hostile diagnostic for arXiv:2609.04176v1, Proposition 9.5.

Status: NON_PROOF_DIAGNOSTIC.

The script evaluates the one-term lower bound on the *max-summand majorant*
which the first paragraph of Proposition 9.5 says is used after (3.5), (4.1)
and (5.24). It uses the consecutive-row ideal model of Lemma 5.5 and the
specific Cauchy--Binet subset I0={0,...,S-1}. For this subset and consecutive
rows the Pascal minor is exactly one.

The proof-level obstruction is in HEIGHT_BOUND_COUNTERCHECK.md. This script
only provides finite numerical corroboration and must not be cited as the
proof of the asymptotic mismatch.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from collections import defaultdict
from pathlib import Path
from typing import Iterator


def phi_q(n: int, q: int) -> int:
    """Phi_q(n)=sum_{0<=r<n} floor(r/q), exactly."""
    a, r = divmod(n, q)
    return q * a * (a - 1) // 2 + r * a


def count_n(i: int, k: int, q: int) -> int:
    """Count 1<=h<=k with q | 2i+2h+1, for odd q."""
    if q <= 0 or q % 2 == 0:
        raise ValueError("q must be a positive odd integer")
    inv2 = (q + 1) // 2
    residue = (-(2 * i + 1) * inv2) % q
    first = q if residue == 0 else residue
    if first > k:
        return 0
    return 1 + (k - first) // q


def ideal_m(B: int, S: int, q: int) -> int:
    """Exact ideal local minimum m^(0)_{q,B} from Sections 5.1 and 7."""
    U0 = 2 * B + S - 1
    row_factor = sum((2 * B + a) // q for a in range(S))
    by_residue: dict[int, list[int]] = defaultdict(list)

    for i in range(U0 + 1):
        base = (
            2 * count_n(i, B, q)
            - count_n(i, S, q)
            - 2 * int(q <= 2 * i + 1)
            - (i // q + (U0 - i) // q)
        )
        by_residue[i % q].append(base)

    # If k points are selected in one residue class, the collision cost is
    # 2*binom(k,2); hence the kth marginal is sorted_base[k-1]+2(k-1).
    marginals: list[int] = []
    for costs in by_residue.values():
        costs.sort()
        marginals.extend(cost + 2 * k for k, cost in enumerate(costs))
    marginals.sort()
    return row_factor + sum(marginals[:S])


def odd_prime_powers(limit: int) -> Iterator[tuple[int, int]]:
    """Yield (p,p^nu) for every odd prime power <=limit."""
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    for p in range(3, limit + 1, 2):
        if not sieve[p]:
            continue
        q = p
        while q <= limit:
            yield p, q
            if q > limit // p:
                break
            q *= p


def v2_factorial_product(B: int) -> int:
    """v_2(prod_{r=0}^{2B-1} r!), exactly."""
    total = 0
    q = 2
    while q <= 2 * B:
        total += phi_q(2 * B, q)
        q *= 2
    return total


def selected_pi_log(B: int, S: int) -> float:
    """log prod_{0<=i<S} Pi_i, with Pi_i from Theorem 2.1."""
    return 2.0 * sum(
        math.log(2 * (i + h) + 1)
        for i in range(S)
        for h in range(1, B + 1)
    )


def cauchy_log(S: int) -> float:
    """Exact logarithm of the consecutive Cauchy determinant in Lemma 4.2."""
    log_vandermonde = sum((S - d) * math.log(d) for d in range(1, S))
    log_denominator = sum(
        math.log(2 * (i + j) + 1)
        for i in range(S)
        for j in range(1, S + 1)
    )
    return (
        S * (S - 1) * math.log(2.0)
        + 2.0 * log_vandermonde
        - log_denominator
    )


def tail_two_term_lower_log(S: int) -> float:
    """Log of a rigorous lower bound for prod_{i<S} T_{i+1}."""
    total = 0.0
    for i in range(S):
        m = i + 1
        lower = 1.0 / (2 * m + 1) ** 2 - 1.0 / (2 * m + 3) ** 2
        if not lower > 0:
            raise AssertionError("alternating two-term lower bound failed")
        total += math.log(lower)
    return total


def evaluate(B: int) -> dict[str, int | float]:
    if B < 20:
        raise ValueError("B must be at least 20")
    S = B // 20
    rho = S / B

    # For the ideal range U0=2B+S-1, every defining divisibility/floor/
    # collision contribution vanishes above 6B+2S-1. 7B+10 is a safe
    # finite enumeration cutoff in the rho<=1/20 regime.
    support_cutoff = 7 * B + 10
    m_log_sum = 0.0
    nonzero_layers = 0
    for p, q in odd_prime_powers(support_cutoff):
        m = ideal_m(B, S, q)
        if m:
            nonzero_layers += 1
            m_log_sum += m * math.log(p)

    v2_log = v2_factorial_product(B) * math.log(2.0)
    pi_log = selected_pi_log(B, S)
    cauchy = cauchy_log(S)
    tails = tail_two_term_lower_log(S)

    # After exact cancellation of the odd a_{p^nu,B} terms against
    # log(F_B/prod Pi_i), this is a lower bound supplied by the single
    # subset I0 on the max-summand majorant. The Pascal minor is 1.
    lower = v2_log - m_log_sum + pi_log + cauchy + tails

    return {
        "B": B,
        "S": S,
        "rho": rho,
        "support_cutoff": support_cutoff,
        "nonzero_odd_prime_power_layers": nonzero_layers,
        "v2_F_B_times_log_2": v2_log,
        "minus_sum_m_q_log_p": -m_log_sum,
        "selected_Pi_log": pi_log,
        "consecutive_Cauchy_log_abs_det": cauchy,
        "two_term_tail_lower_log": tails,
        "Pascal_minor_log_abs": 0.0,
        "one_term_lower_bound": lower,
        "normalized_by_B_squared": lower / (B * B),
        "normalized_by_B_squared_log_B": lower / (B * B * math.log(B)),
        "analytic_uncancelled_coefficient_rho_squared_over_2": rho * rho / 2.0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("height_hostile_replay.json"),
    )
    parser.add_argument(
        "--B",
        type=int,
        nargs="*",
        default=[100, 200, 300, 500, 1000, 1500],
    )
    args = parser.parse_args()

    rows = [evaluate(B) for B in args.B]
    payload = {
        "status": "NON_PROOF_DIAGNOSTIC",
        "paper": "arXiv:2609.04176v1",
        "target": "Proposition 9.5 max-summand majorant",
        "model": "consecutive-row ideal model of Lemma 5.5",
        "subset": "I0={0,...,S-1}",
        "printed_tail_index_used": "T_{i+1}",
        "proof_level_result_location": "../HEIGHT_BOUND_COUNTERCHECK.md",
        "interpretation": (
            "The finite values corroborate that the majorant is not near the "
            "negative O(B^2) quantity asserted in (9.3). The decisive result "
            "is analytic: its uncancelled leading term is "
            "(rho^2/2) B^2 log B."
        ),
        "limitations": [
            "This is finite floating-log evaluation, not interval arithmetic.",
            "It uses the ideal model; Lemma 5.5 is needed to transfer leading order.",
            "It does not evaluate the signed determinant or prove Catalan's constant rational or irrational.",
            "It is corroboration, not the proof of the asymptotic obstruction.",
        ],
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
        },
        "rows": rows,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded, encoding="utf-8")
    digest = hashlib.sha256(encoded.encode("utf-8")).hexdigest()
    print(f"wrote {args.output}")
    print(f"sha256 {digest}")
    for row in rows:
        print(
            f"B={row['B']:4d} S={row['S']:3d} "
            f"lower/B^2={row['normalized_by_B_squared']:.15f}"
        )


if __name__ == "__main__":
    main()
