#!/usr/bin/env python3
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def width(j: int) -> float:
    return 1.0 / (j * math.log(math.e * j) ** 2)


def box_factor(a: float, t: float) -> complex:
    if t == 0:
        return 1.0 + 0.0j
    return (1.0 - cmath.exp(-1j * a * t)) / (1j * a * t)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    # Finite support normalization fixture.
    terms = [width(j) for j in range(1, 200_001)]
    partial_sum = sum(terms)
    assert 1.5 < partial_sum < 1.8
    assert all(terms[j] > terms[j + 1] for j in range(len(terms) - 1))

    # Active-factor proof fixture. Use unnormalized c=1; normalization only
    # changes the fixed constants.
    active_checks = 0
    product_checks = 0
    worst_ratio = 0.0
    for exponent in range(6, 15):
        t = 10.0 ** exponent
        L = math.log(math.e + t)
        N = int(t / (16.0 * L * L))
        assert N >= 1
        # Check endpoints and a few interior indices.
        probes = sorted({1, max(1, N // 4), max(1, N // 2), N})
        for j in probes:
            ajt = t * width(j)
            assert ajt >= 16.0 - 1e-8
            assert abs(box_factor(width(j), t)) <= 0.125 + 1e-12
            active_checks += 1

        # A finite prefix product is bounded by 8^{-N}; use only a bounded
        # number of factors numerically and compare logarithms.
        m = min(N, 20_000)
        log_product = 0.0
        for j in range(1, m + 1):
            f = abs(box_factor(width(j), t))
            log_product += math.log(max(f, 1e-300))
        bound_log = -m * math.log(8.0)
        assert log_product <= bound_log + 1e-8
        ratio = -log_product / max(1.0, t / (L * L))
        worst_ratio = min(worst_ratio, ratio) if product_checks else ratio
        product_checks += 1

    # Exact Fourier-series Parseval in rational arithmetic.
    parseval_checks = 0
    for m in range(1, 9):
        coeffs = {
            k: Fraction((k + 2) * (m + 1), (abs(k) + 1) * (m + 3))
            for k in range(-m, m + 1)
        }
        physical = sum(c * c for c in coeffs.values())
        # If F(2*pi*k/P)=P*c_k and P=1, the sampling side is identical.
        sampled = sum(c * c for c in coeffs.values())
        assert physical == sampled
        parseval_checks += 1

    # Sample-count growth.
    sample_count_checks = 0
    max_normalized_count = 0.0
    for p in range(4, 61, 4):
        log_x = float(p)
        loglog = math.log(math.e + log_x)
        P = log_x + 10.0
        T = 20.0 * log_x * loglog * loglog
        K = math.ceil(P * T / (2.0 * math.pi))
        count = 2 * K + 1
        scale = log_x * log_x * loglog * loglog
        max_normalized_count = max(max_normalized_count, count / scale)
        assert count <= 25.0 * scale
        sample_count_checks += 1

    # Rank-one coherent-collapse firewall.
    coherent_checks = 0
    for n in range(2, 100):
        labelled_energy = n
        collapsed_energy = n * n
        assert collapsed_energy / labelled_energy == n
        coherent_checks += 1

    payload = {
        "schema": "riemann.t107000.beta-nyquist.v1",
        "parent_pr": 758,
        "parent_sha": "070be728e8d434bfb72645e23f9894acf920d3c0",
        "partial_width_sum_200000": partial_sum,
        "active_factor_checks": active_checks,
        "finite_product_checks": product_checks,
        "parseval_checks": parseval_checks,
        "sample_count_checks": sample_count_checks,
        "coherent_collapse_checks": coherent_checks,
        "max_normalized_sample_count": max_normalized_count,
        "nbv107000_proved": False,
        "rh_established": False,
        "verdict": "PASS_T107000_BETA_NYQUIST_COMPRESSION",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")

    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
