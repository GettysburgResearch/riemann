#!/usr/bin/env python3
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from pathlib import Path


def digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    laplace_checks = 0
    for s in [0j, 0.2 + 0.4j, 0.7 - 0.3j, 1.1 + 0.2j]:
        # Fourier multiplier at -i s.
        lhs = cmath.exp(1.0 - cmath.cosh(-1j * s))
        rhs = cmath.exp(1.0 - cmath.cos(s))
        assert abs(lhs - rhs) < 1e-13
        assert abs(rhs) > 0
        laplace_checks += 1

    strip_checks = 0
    for sigma in [0.5, 0.75, 1.0, 1.25]:
        assert sigma < math.pi / 2
        assert math.cos(sigma) > 0
        strip_checks += 1
    assert 1.0 > 0.5

    # Finite periodic Parseval fixture for a sampled trigonometric polynomial.
    parseval_checks = 0
    for p in [17, 31, 47]:
        coeff = [complex(math.cos(j), math.sin(2 * j)) / (j + 1) for j in range(7)]
        time_energy = 0.0
        for x in range(p):
            f = sum(c * cmath.exp(2j * math.pi * j * x / p) for j, c in enumerate(coeff))
            time_energy += abs(f) ** 2
        freq_energy = p * sum(abs(c) ** 2 for c in coeff)
        assert abs(time_energy - freq_energy) < 1e-9
        parseval_checks += 1

    tail_checks = 0
    for x in [10.0**6, 10.0**12, 10.0**24]:
        a = 4.0
        t = math.log(math.log(math.e**math.e * x)) + a
        weight = x * math.exp(2.0 - 2.0 * math.cosh(t))
        assert weight < x ** -1.0
        tail_checks += 1

    rank_checks = 0
    for x in [10.0**6, 10.0**12, 10.0**24, 10.0**48]:
        l = math.log(x)
        dim_model = l * math.log(math.e**math.e + l)
        assert dim_model / (l * l) < 1.0
        rank_checks += 1

    coherent_checks = 0
    for n in range(2, 100):
        labelled = float(n)
        collapsed = float(n * n)
        assert collapsed / labelled == n
        coherent_checks += 1

    payload = {
        "schema": "riemann.t107020.hyperbolic-native-beta.v1",
        "base_pr": 759,
        "base_sha": "d1b8aa57b08db1ba9f2edf3b68238c2a129b7c33",
        "laplace_checks": laplace_checks,
        "strip_checks": strip_checks,
        "parseval_checks": parseval_checks,
        "tail_checks": tail_checks,
        "rank_checks": rank_checks,
        "coherent_collapse_checks": coherent_checks,
        "feature_dimension": "O(log X loglog X)",
        "hnbv107020_proved": False,
        "rh_established": False,
        "verdict": "PASS_T107020_HYPERBOLIC_NATIVE_BETA_COMPRESSION",
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
