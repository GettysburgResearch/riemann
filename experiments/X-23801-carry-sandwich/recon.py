#!/usr/bin/env python3
"""Discovery-only double-precision carry reconnaissance.

This script is not a directed certificate.  It evaluates the canonical descending
greedy packing and the exact binomial-row entropy at selected finite endpoints.
"""

import argparse
import json
import math
from pathlib import Path


def beta(n: int, q: int) -> float:
    if q > n:
        return 0.0
    k, r = divmod(n, q)
    return k * (q - 1 - r) / (n + 1)


def g_values(x: int):
    log_fact = [0.0] * (x + 1)
    prefix = [0.0] * (x + 1)
    g = [0.0] * (x + 1)
    for n in range(1, x + 1):
        log_fact[n] = log_fact[n - 1] + math.log(n)
        prefix[n] = prefix[n - 1] + log_fact[n]
        g[n] = log_fact[n] - 2.0 * prefix[n] / (n + 1)
    return g


def run_endpoint(x: int):
    residual = [0.0] * (x + 1)
    for q in range(2, x + 1):
        residual[q] = math.log(x / q) / math.sqrt(q)

    d = [0.0] * (x + 1)
    off_diagonal = 0
    for n in range(x, 1, -1):
        best = None
        q_best = None
        for q in range(2, n + 1):
            b = beta(n, q)
            if b == 0.0:
                continue
            ratio = residual[q] / b
            if best is None or ratio < best:
                best = ratio
                q_best = q
        if best is None:
            best = 0.0
        if best < -1e-11:
            raise ArithmeticError((x, n, best))
        best = max(0.0, best)
        d[n] = best
        if q_best is not None and q_best != n and best > 1e-14:
            off_diagonal += 1
        for q in range(2, n + 1):
            b = beta(n, q)
            if b:
                residual[q] -= best * b
                if abs(residual[q]) < 1e-12:
                    residual[q] = 0.0

    g = g_values(x)
    entropy = sum(d[n] * g[n] for n in range(2, x + 1))
    mass = 0.5 * sum(n * d[n] for n in range(2, x + 1))
    barrier = 4.0 * math.sqrt(x)
    positive = [d[n] for n in range(2, x) if d[n] > 0.0]
    return {
        "X": x,
        "entropy": entropy,
        "entropy_over_sqrt_X": entropy / math.sqrt(x),
        "entropy_deficit_from_4sqrtX": barrier - entropy,
        "deficit_over_log_X": (barrier - entropy) / math.log(x),
        "signed_half_n_mass": mass,
        "mass_minus_4sqrtX": mass - barrier,
        "off_diagonal_saturations": off_diagonal,
        "minimum_positive_coefficient": min(positive) if positive else None,
        "minimum_final_residual": min(residual[2:]),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--endpoints",
        nargs="+",
        type=int,
        default=[50, 100, 200, 400, 800, 1200, 2000, 5000],
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = {
        "schema": "X-23801-recon-v1",
        "classification": "DOUBLE_PRECISION_DISCOVERY_ONLY",
        "rows": [run_endpoint(x) for x in args.endpoints],
        "proof_boundary": (
            "The run nominates diagonal greedy saturation and a logarithmic "
            "entropy deficit. It is not interval arithmetic and proves neither "
            "the Carry Obstacle theorem nor RH."
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
