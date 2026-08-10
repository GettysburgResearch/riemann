#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results" / "verification.json"
mp.mp.dps = 60


def kernel_closed(a: mp.mpf, t: mp.mpf, s: mp.mpf) -> mp.mpf:
    return a / mp.pi * (
        1 / (a * a + (t - s) ** 2)
        - 1 / (a * a + (t + s) ** 2)
    )


def kernel_integral(a: mp.mpf, t: mp.mpf, s: mp.mpf) -> mp.mpf:
    return 2 / mp.pi * mp.quad(
        lambda x: mp.e ** (-a * x) * mp.sin(t * x) * mp.sin(s * x),
        [0, mp.inf],
    )


def h(x: mp.mpf) -> mp.mpf:
    return x * mp.e ** (-mp.mpf("0.4") * x * x)


def sine_h(t: mp.mpf) -> mp.mpf:
    alpha = mp.mpf("0.4")
    return mp.sqrt(2) * t / (4 * alpha ** mp.mpf("1.5")) * mp.e ** (-t * t / (4 * alpha))


def main() -> None:
    a = mp.mpf("0.8")
    pts = [mp.mpf(x) for x in ("0.2", "0.7", "1.5", "3.0", "5.0")]
    errors = []
    gram = np.zeros((len(pts), len(pts)), dtype=float)
    for i, t in enumerate(pts):
        for j, s in enumerate(pts):
            c = kernel_closed(a, t, s)
            q = kernel_integral(a, t, s)
            errors.append(abs(c - q))
            gram[i, j] = float(c)
    mineig = float(np.linalg.eigvalsh(gram).min())
    if max(errors) > mp.mpf("1e-10") or mineig <= 0:
        raise AssertionError((max(errors), mineig))

    shift_checks = []
    norm = mp.quad(lambda x: h(x) ** 2, [0, mp.inf])
    for y in (mp.mpf("0.3"), mp.mpf("0.9"), mp.mpf("2.0")):
        # Odd extension normalised by 1/sqrt(2).
        corr_physical = (
            mp.quad(lambda x: h(x + y) * h(x), [0, mp.inf])
            - mp.mpf("0.5") * mp.quad(lambda x: h(x) * h(y - x), [0, y])
        )
        corr_spectral = mp.quad(
            lambda t: mp.cos(y * t) * sine_h(t) ** 2,
            [0, 1, 3, 7, mp.inf],
        )
        energy_physical = 2 * norm - 2 * corr_physical
        energy_spectral = 2 * mp.quad(
            lambda t: (1 - mp.cos(y * t)) * sine_h(t) ** 2,
            [0, 1, 3, 7, mp.inf],
        )
        ce = abs(corr_physical - corr_spectral)
        ee = abs(energy_physical - energy_spectral)
        if ce > mp.mpf("1e-35") or ee > mp.mpf("1e-35"):
            raise AssertionError((y, ce, ee))
        shift_checks.append({
            "y": str(y),
            "correlation_error": mp.nstr(ce, 8),
            "energy_error": mp.nstr(ee, 8),
        })

    # Finite matrix version of K M_r M_symbol M_r K.
    grid = np.linspace(0.15, 5.0, 40)
    weights = np.full(40, (grid[-1] - grid[0]) / 39)
    K = np.array([[float(kernel_closed(a, mp.mpf(t), mp.mpf(s))) for s in grid] for t in grid])
    r = 1 / (1.7 ** 2 + grid ** 2)
    symbol = 0.7 + grid ** 2 / (1 + grid ** 2)
    W = np.diag(weights)
    A = K @ W @ np.diag(r * symbol * r) @ W @ K
    A = (A + A.T) / 2
    sandwich_min = float(np.linalg.eigvalsh(A).min())
    if sandwich_min < -1e-12:
        raise AssertionError(sandwich_min)

    result = {
        "verdict": "PASS_X_90506_SINE_CAUCHY_SANDWICH",
        "kernel_pairs": len(errors),
        "kernel_max_error": mp.nstr(max(errors), 8),
        "kernel_gram_minimum_eigenvalue": mineig,
        "shift_checks": shift_checks,
        "positive_symbol_sandwich_minimum_eigenvalue": sandwich_min,
        "scope": "High-precision sine/Cauchy identities and a finite positive-symbol sandwich only; no zeta symbol sign theorem or RH claim.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
