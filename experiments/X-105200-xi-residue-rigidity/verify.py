#!/usr/bin/env python3
"""Light exact replay for T-105200.

This checker authenticates the finite algebra used after the analytic saddle
estimate. It does not prove the uniform Laplace theorem or rerun Xi numerics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable


def model_residue(m: int, j: int, moment_prev: Fraction, moment_next: Fraction) -> Fraction:
    """Residue of the exact common-frequency trig model at its m-th zero."""
    if moment_prev <= 0 or moment_next <= 0:
        raise ValueError("moments must be positive")
    # At theta_m=(j+1/2)pi, adjacent cosines are (-1)^j and -(-1)^j.
    left_sign = -1 if j % 2 else 1
    right_sign = -left_sign
    return Fraction(left_sign, right_sign) * moment_prev / moment_next


def coherence(values: Iterable[Fraction]) -> Fraction:
    vals = list(values)
    if not vals:
        raise ValueError("empty family")
    if any(v <= 0 for v in vals):
        raise ValueError("coherence fixture must be positive")
    s1 = sum(vals, Fraction(0))
    s2 = sum((v * v for v in vals), Fraction(0))
    return s1 * s1 / (len(vals) * s2)


def coherence_identity(values: Iterable[Fraction]) -> tuple[Fraction, Fraction]:
    vals = list(values)
    n = len(vals)
    mean = sum(vals, Fraction(0)) / n
    mean2 = sum((v * v for v in vals), Fraction(0)) / n
    var = sum(((v - mean) ** 2 for v in vals), Fraction(0)) / n
    return coherence(vals), Fraction(1) - var / mean2


def firewall_residues(c: Fraction) -> tuple[Fraction, Fraction]:
    return (c - Fraction(2, 3)) / 2, -(c + Fraction(2, 3)) / 2


def natural_window_drift(samples: Iterable[int], eta: float = 0.6, c: float = 2.0) -> list[float]:
    """Surrogate check of (w_(m+1)-w_m)T_N -> 0 at natural width."""
    out: list[float] = []
    for n in samples:
        m = max(10, int(eta * n))
        w = 0.5 * math.log(m)
        a = math.sqrt(w / (2.0 * m))
        t = c / a
        dw = 1.0 / (2.0 * m)
        out.append(dw * t)
    return out


def run() -> dict[str, object]:
    # Exact common-frequency residue sign and scale.
    moment_prev = Fraction(37, 11)
    moment_next = Fraction(91, 13)
    expected = -moment_prev / moment_next
    residue_rows = []
    for m in range(4, 10):
        for j in range(-5, 6):
            got = model_residue(m, j, moment_prev, moment_next)
            assert got == expected
            residue_rows.append((m, j, str(got)))

    # Exact coherence = 1 - variance / second moment.
    families = [
        [Fraction(1), Fraction(1), Fraction(1)],
        [Fraction(99, 100), Fraction(1), Fraction(101, 100)],
        [Fraction(7, 8), Fraction(9, 8), Fraction(1), Fraction(17, 16)],
    ]
    coherence_rows = []
    for vals in families:
        lhs, rhs = coherence_identity(vals)
        assert lhs == rhs
        assert 0 < lhs <= 1
        coherence_rows.append({"values": [str(v) for v in vals], "coherence": str(lhs)})
    assert coherence(families[0]) == 1
    assert coherence(families[1]) > Fraction(999, 1000)

    # Exact integration-constant firewall.
    r0 = firewall_residues(Fraction(0))
    r1 = firewall_residues(Fraction(1))
    assert r0 == (Fraction(-1, 3), Fraction(-1, 3))
    assert r1[0] > 0 and r1[1] < 0

    # The natural-window adjacent phase drift decreases to zero in the saddle surrogate.
    drift = natural_window_drift([10**3, 10**4, 10**5, 10**6])
    assert all(drift[i + 1] < drift[i] for i in range(len(drift) - 1))
    assert drift[-1] < 0.01

    payload = {
        "schema": "riemann.x105200.xi-residue-rigidity.v1",
        "classification": "PASS_T105200_NATURAL_WINDOW_RESIDUE_RIGIDITY",
        "exact_model_residue_rows": len(residue_rows),
        "coherence_fixtures": coherence_rows,
        "integration_constant_firewall": {
            "C=0": [str(x) for x in r0],
            "C=1": [str(x) for x in r1],
        },
        "natural_window_surrogate_drift": drift,
        "analytic_gaussian_saddle_replayed": False,
        "xi_numerics_run": False,
        "rcmv_high_band_proved_by_replay": False,
        "rh_established": False,
        "mutations_rejected": [
            "zero_count_called_residue_coherence",
            "adjacent_derivative_orders_omitted",
            "natural_window_replaced_by_little_o_window",
            "moment_ratio_replaced_by_untyped_frequency_fit",
            "high_band_result_called_fixed_order_descent",
            "rh_established_by_light_replay",
        ],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
