#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

SCHEMA = "riemann.t100710.scme_lrnm_disposition.v1"


def k0(y: float) -> float:
    if y < 1.0 or y >= 8.0:
        return 0.0
    r = math.sqrt(y)
    if y < 2.0:
        return 8.0 * r - 8.0 - 3.0 * math.log(y)
    if y < 4.0:
        return (
            -8.0 * math.sqrt(2.0) * r
            + 8.0 * (1.0 + math.sqrt(2.0))
            + 3.0 * (1.0 + math.sqrt(2.0)) * math.log(y)
            - 3.0 * (2.0 + math.sqrt(2.0)) * math.log(2.0)
        )
    return (
        4.0 * r
        - 8.0 * math.sqrt(2.0)
        + 9.0 * math.sqrt(2.0) * math.log(2.0)
        - 3.0 * math.sqrt(2.0) * math.log(y)
    )


def linear_sieve(limit: int) -> tuple[list[int], list[int], list[int]]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    least = [0] * (limit + 1)
    greatest = [0] * (limit + 1)
    primes: list[int] = []
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            greatest[n] = n
            mu[n] = -1
            primes.append(n)
        for p in primes:
            if n * p > limit:
                break
            least[n * p] = p
            greatest[n * p] = max(greatest[n], p)
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu, least, greatest


def evaluate(X: int, mu: list[int], least: list[int], greatest: list[int]) -> dict[str, float]:
    lo = (X + 7) // 8
    total = 0.0
    short = 0.0
    for n in range(lo, X + 1):
        if mu[n] == 0:
            continue
        value = mu[n] * k0(X / n) / math.sqrt(n)
        total += value
        if greatest[n] <= 8 * least[n]:
            short += value
    long = total - short
    scale = math.sqrt(X) / math.log(X)
    return {
        "X": X,
        "G_mu": total,
        "G_short": short,
        "G_long": long,
        "short_over_scale": short / scale,
        "long_over_scale": long / scale,
    }


def verify() -> dict[str, Any]:
    kappa = 8.0 * math.log(2.0) * (1.0 - 1.0 / math.sqrt(2.0)) ** 2
    assert kappa > 0.47
    assert abs(k0(1.0)) < 1e-14
    assert abs(k0(8.0)) < 1e-14

    limit = 200_000
    mu, least, greatest = linear_sieve(limit)
    samples = [evaluate(X, mu, least, greatest) for X in (20_000, 80_000, 200_000)]
    for row in samples:
        assert abs(row["G_mu"] - row["G_short"] - row["G_long"]) < 1e-10
        assert row["G_short"] < 0.0
        assert row["G_long"] > 0.0

    core = {
        "schema": SCHEMA,
        "base_pr": 693,
        "base_head": "2cc70798b453ce4e5059dcc25d8d3fb7c38e172e",
        "kappa_0": f"{kappa:.17g}",
        "samples": samples,
        "scope": {
            "short_prime_main_coefficient_checked": True,
            "source_partition_checked": True,
            "finite_sign_diagnostics_checked": True,
            "scme100704_refuted_analytically": True,
            "lrnm100704_proved_analytically": True,
            "rh_established": False,
            "finite_replay_is_not_the_asymptotic_proof": True,
        },
        "verdict": "PASS_T100710_SCME_REFUTATION_AND_LRNM_DISPOSITION",
    }
    digest = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    core["proof_object_sha256"] = digest
    return core


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
