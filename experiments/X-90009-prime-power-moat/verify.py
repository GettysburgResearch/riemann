#!/usr/bin/env python3
"""Finite audit for L-90009 / T-90009.

The mathematical theorems are the exact transform identities and contour
arguments in the claims files.  This script authenticates only:

* radical-switching and prefix formulas for A, the full prime-power deficit,
  the zero-insensitive moat M=A-Delta_Lambda, and their logarithmic derivatives;
* the exact integer increment formula for A_{N+1}-A_N;
* finite reconnaissance for endpoint monotonicity and negative derivative.

The scan is discovery evidence.  It is not extrapolated to all endpoints.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

ZETA_HALF = -1.4603545088095868128894991525152980124672293310126
MOAT_QUADRATIC = (1.0 + ZETA_HALF) / 4.0
MOAT_DERIVATIVE = (1.0 + ZETA_HALF) / 2.0


def prime_sieve(n: int) -> np.ndarray:
    is_prime = np.ones(n + 1, dtype=np.bool_)
    is_prime[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = False
    return np.flatnonzero(is_prime)


def build_prefixes(n: int):
    primes = prime_sieve(n)

    lograd = np.zeros(n + 1, dtype=np.float64)
    for p0 in primes:
        p = int(p0)
        lograd[p::p] += math.log(p)

    # d[m-1] = log rad(m)-log rad(m-1).
    d = lograd[1:] - lograd[:-1]
    m = np.arange(1, n + 1, dtype=np.longdouble)
    d80 = d.astype(np.longdouble)

    s_half = np.cumsum(np.sqrt(m) * d80, dtype=np.longdouble)
    s_half_log = np.cumsum(np.sqrt(m) * np.log(m) * d80, dtype=np.longdouble)
    s_one = np.cumsum(m * d80, dtype=np.longdouble)

    theta_atom = np.zeros(n + 1, dtype=np.longdouble)
    theta_log_atom = np.zeros(n + 1, dtype=np.longdouble)
    psi_atom = np.zeros(n + 1, dtype=np.longdouble)
    psi_log_atom = np.zeros(n + 1, dtype=np.longdouble)

    for p0 in primes:
        p = int(p0)
        lp = np.longdouble(math.log(p))
        prime_weight = lp / np.sqrt(np.longdouble(p))
        theta_atom[p] = prime_weight
        theta_log_atom[p] = prime_weight * np.log(np.longdouble(p))

        q = p
        while q <= n:
            weight = lp / np.sqrt(np.longdouble(q))
            psi_atom[q] += weight
            psi_log_atom[q] += weight * np.log(np.longdouble(q))
            if q > n // p:
                break
            q *= p

    theta = np.cumsum(theta_atom, dtype=np.longdouble)
    theta_log = np.cumsum(theta_log_atom, dtype=np.longdouble)
    psi = np.cumsum(psi_atom, dtype=np.longdouble)
    psi_log = np.cumsum(psi_log_atom, dtype=np.longdouble)

    return {
        "primes": primes,
        "lograd": lograd,
        "s_half": s_half,
        "s_half_log": s_half_log,
        "s_one": s_one,
        "theta": theta,
        "theta_log": theta_log,
        "psi": psi,
        "psi_log": psi_log,
    }


def endpoint_values(x: int, pfx) -> dict:
    i = x - 1
    lx = np.longdouble(math.log(x))
    sx = np.sqrt(np.longdouble(x))

    j_prime = (
        2 * lx * pfx["s_half"][i]
        - 2 * pfx["s_half_log"][i]
        - 4 * pfx["s_half"][i]
        + 4 * pfx["s_one"][i] / sx
    )
    prime_ramp = lx * pfx["theta"][x] - pfx["theta_log"][x]
    a_value = j_prime - prime_ramp

    full_ramp = lx * pfx["psi"][x] - pfx["psi_log"][x]
    delta_lambda = 4 * sx - full_ramp
    moat = a_value - delta_lambda

    d_j_prime = 2 * pfx["s_half"][i] - 2 * pfx["s_one"][i] / sx
    d_a = d_j_prime - pfx["theta"][x]
    e_half = pfx["psi"][x] - 2 * sx
    d_moat = d_a + e_half

    return {
        "X": x,
        "A": float(a_value),
        "Delta_lambda": float(delta_lambda),
        "moat": float(moat),
        "D_A": float(d_a),
        "E_half": float(e_half),
        "D_moat": float(d_moat),
        "moat_over_log2": float(moat / (lx * lx)),
        "D_moat_over_log": float(d_moat / lx),
    }


def direct_a(x: int, pfx) -> float:
    """Direct radical-switching check, deliberately not using prefix moments."""
    m = np.arange(2, x + 1, dtype=np.float64)
    b = 2 * np.sqrt(m) * (
        np.log(x / m) - 2 * (1 - np.sqrt(m / x))
    )
    d = pfx["lograd"][2 : x + 1] - pfx["lograd"][1:x]
    j_prime = math.fsum((b * d).tolist())

    ramp = 0.0
    for p0 in pfx["primes"]:
        p = int(p0)
        if p > x:
            break
        ramp += math.log(p) / math.sqrt(p) * math.log(x / p)
    return j_prime - ramp


def audit(max_n: int) -> dict:
    pfx = build_prefixes(max_n)

    # Exact formula audit at modest endpoints.
    direct_rows = []
    for x in (10, 31, 100, 257, 1000):
        if x > max_n:
            continue
        via_prefix = endpoint_values(x, pfx)["A"]
        via_direct = direct_a(x, pfx)
        err = abs(via_prefix - via_direct)
        if err > 2e-10:
            raise AssertionError(f"radical-switching mismatch at X={x}: {err}")
        direct_rows.append({"X": x, "absolute_error": err})

    # Integer increments: M=N-1 in the notation of T-90009.
    m = np.arange(2, max_n, dtype=np.longdouble)
    log_step = np.log1p(1 / m)
    increments = (
        log_step
        * (
            2 * pfx["s_half"][1 : max_n - 1]
            - pfx["theta"][2:max_n]
        )
        + 4
        * (1 / np.sqrt(m + 1) - 1 / np.sqrt(m))
        * pfx["s_one"][1 : max_n - 1]
    )
    i_inc = int(np.argmax(increments))
    max_increment = float(increments[i_inc])
    max_increment_at = int(m[i_inc])

    # On each interval (N,N+1), D A is affine in X^{-1/2};
    # its maximum is therefore at one of the two interval endpoints.
    n = np.arange(2, max_n, dtype=np.longdouble)
    s_half = pfx["s_half"][1 : max_n - 1]
    s_one = pfx["s_one"][1 : max_n - 1]
    theta = pfx["theta"][2:max_n]
    d_start = 2 * s_half - 2 * s_one / np.sqrt(n) - theta
    d_end = 2 * s_half - 2 * s_one / np.sqrt(n + 1) - theta
    d_interval_max = np.maximum(d_start, d_end)
    i_der = int(np.argmax(d_interval_max))

    sample_candidates = [
        10_000,
        100_000,
        200_000,
        500_000,
        1_000_000,
        2_000_000,
        5_000_000,
        max_n,
    ]
    rows = [
        endpoint_values(x, pfx)
        for x in sorted({x for x in sample_candidates if 2 <= x <= max_n})
    ]

    if np.any(increments >= 0):
        raise AssertionError("finite endpoint monotonicity mutation")
    if np.any(d_interval_max >= 0):
        raise AssertionError("finite real-interval derivative mutation")

    return {
        "classification": "PASS_PRIME_POWER_MOAT_AND_MONOTONICITY_RECONNAISSANCE",
        "scope": (
            "Finite identity authentication and reconnaissance only. "
            "The all-X moat asymptotic and the conditional implications are "
            "mathematical arguments in L-90009/T-90009."
        ),
        "constants": {
            "zeta_half": ZETA_HALF,
            "moat_quadratic_coefficient": MOAT_QUADRATIC,
            "moat_derivative_coefficient": MOAT_DERIVATIVE,
        },
        "max_X": max_n,
        "direct_formula_checks": direct_rows,
        "integer_increment_scan": {
            "positive_count": int(np.sum(increments >= 0)),
            "largest_increment": max_increment,
            "at_M": max_increment_at,
        },
        "real_interval_derivative_scan": {
            "nonnegative_count": int(np.sum(d_interval_max >= 0)),
            "largest_interval_maximum": float(d_interval_max[i_der]),
            "interval_left_endpoint": int(n[i_der]),
            "attained_at": (
                "right_limit"
                if d_end[i_der] >= d_start[i_der]
                else "left_limit"
            ),
        },
        "sample_rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=1_000_000)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("results") / "verification.json",
    )
    args = parser.parse_args()
    if args.max_x < 1000:
        raise SystemExit("--max-x must be at least 1000")

    result = audit(args.max_x)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(args.output)


if __name__ == "__main__":
    main()
