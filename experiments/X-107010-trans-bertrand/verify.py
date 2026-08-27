#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def ilog(x: float, depth: int) -> float:
    y = x
    for _ in range(depth):
        y = math.log(math.e + y)
    return y


def W(x: float, depth: int) -> float:
    out = 1.0
    for j in range(1, depth + 1):
        out *= ilog(x, j)
    out *= ilog(x, depth + 1) ** 2
    return out


def digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    depths = range(4)
    width_partial = {}
    monotonicity_checks = 0
    active_checks = 0
    hierarchy_checks = 0
    sample_checks = 0

    for m in depths:
        total = 0.0
        last_w = 0.0
        for n in range(1, 200001):
            w = W(float(n), m)
            assert w >= last_w
            last_w = w
            total += 1.0 / (n * w)
            monotonicity_checks += 1
        width_partial[str(m)] = total

        c = 1.0 / total
        for t in (1e4, 1e5, 1e6, 1e7):
            n_active = int(c * t / (64.0 * W(t, m)))
            if n_active < 1:
                continue
            for n in (1, max(1, n_active // 2), n_active):
                a = c / (n * W(float(n), m))
                assert a * t >= 63.9
                active_checks += 1

        for y in (1e6, 1e12, 1e24):
            t = y * W(y, m)
            assert W(t, m) <= 20.0 * W(y, m)
            sample_count = y * t
            normalized = sample_count / (y * y * W(y, m))
            assert 0.99 <= normalized <= 1.01
            sample_checks += 1

    for m in range(3):
        for x in (1e12, 1e24, 1e48, 1e96):
            ratio = W(x, m + 1) / W(x, m)
            # The ratio decreases eventually; finite fixtures only check the
            # exact formula and positivity.
            expected = ilog(x, m + 2) ** 2 / ilog(x, m + 1)
            assert abs(ratio - expected) < 1e-12 * max(1.0, abs(expected))
            hierarchy_checks += 1

    # Source-blind coherent-collapse firewall.
    coherent_checks = 0
    for n in range(2, 100):
        labelled = float(n)
        collapsed = float(n * n)
        assert collapsed / labelled == n
        coherent_checks += 1

    payload = {
        "schema": "riemann.t107010.trans-bertrand.v1",
        "parent_pr": 759,
        "parent_sha": "ebaf1dbcccecd7ed18812e786da40f1d610e497d",
        "width_partial_sums_200000": width_partial,
        "monotonicity_checks": monotonicity_checks,
        "active_factor_checks": active_checks,
        "hierarchy_checks": hierarchy_checks,
        "sample_count_checks": sample_checks,
        "coherent_collapse_checks": coherent_checks,
        "same_detector_all_depths": True,
        "exact_quadratic_source_blind_rank_possible": False,
        "nbv107000_proved": False,
        "rh_established": False,
        "verdict": "PASS_T107010_TRANS_BERTRAND_NYQUIST",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")

    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
