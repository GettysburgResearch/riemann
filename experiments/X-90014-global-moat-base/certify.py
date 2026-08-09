#!/usr/bin/env python3
"""Directed finite base for L-90014."""
from __future__ import annotations

import json
import math
from pathlib import Path

from mpmath import iv

iv.dps = 70


def lower(x) -> float:
    return float(x.a)


def upper(x) -> float:
    return float(x.b)


def sieve(n: int) -> list[int]:
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = b"\x00" * (
                (n - p * p) // p + 1
            )
    return [p for p in range(2, n + 1) if is_prime[p]]


def main() -> None:
    top = 1999
    primes = sieve(top)

    lograd = [iv.mpf(0) for _ in range(top + 1)]
    theta_atom = [iv.mpf(0) for _ in range(top + 1)]
    psi_atom = [iv.mpf(0) for _ in range(top + 1)]

    for p in primes:
        lp = iv.log(p)
        for m in range(p, top + 1, p):
            lograd[m] += lp
        theta_atom[p] += lp / iv.sqrt(p)
        q = p
        while q <= top:
            psi_atom[q] += lp / iv.sqrt(q)
            q *= p

    s_half = iv.mpf(0)
    s_one = iv.mpf(0)
    theta_half = iv.mpf(0)
    psi_half = iv.mpf(0)

    branch_counts = {"left": 0, "right": 0, "critical": 0}
    worst_upper = -math.inf
    worst_n = None
    worst_branch = None

    for n in range(2, top + 1):
        d = lograd[n] - lograd[n - 1]
        s_half += iv.sqrt(n) * d
        s_one += n * d
        theta_half += theta_atom[n]
        psi_half += psi_atom[n]
        c_n = 2 * s_half - theta_half + psi_half

        if upper(s_one) <= n:
            y = iv.sqrt(n)
            value = c_n - 2 * s_one / y - 2 * y
            branch = "left"
        elif lower(s_one) >= n + 1:
            y = iv.sqrt(n + 1)
            value = c_n - 2 * s_one / y - 2 * y
            branch = "right"
        elif lower(s_one) > n and upper(s_one) < n + 1:
            value = c_n - 4 * iv.sqrt(s_one)
            branch = "critical"
        else:
            raise AssertionError(f"undecided maximizer branch at N={n}")

        branch_counts[branch] += 1
        this_upper = upper(value)
        if this_upper > worst_upper:
            worst_upper = this_upper
            worst_n = n
            worst_branch = branch
        if this_upper >= -2.82:
            raise AssertionError(
                f"finite moat derivative margin failed at N={n}: {this_upper}"
            )

    if worst_n != 2 or worst_branch != "left":
        raise AssertionError("least-negative interval was not the first one")

    result = {
        "classification": "PASS_GLOBAL_PRIME_POWER_MOAT_FINITE_BASE",
        "intervals": [2, 2000],
        "branch_counts": branch_counts,
        "least_negative_interval": {
            "N": worst_n,
            "branch": worst_branch,
            "upper_bound": worst_upper,
            "exact_reference": "-2sqrt(2)",
        },
        "initial_value": {
            "expression": "M(2)=-4sqrt(2)",
            "upper": upper(-4 * iv.sqrt(2)),
            "lower": lower(-4 * iv.sqrt(2)),
        },
        "scope": (
            "Directed finite base only. The analytic X>=2000 tail is L-90012."
        ),
    }
    out = Path(__file__).with_name("results") / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
