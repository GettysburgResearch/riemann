#!/usr/bin/env python3
"""Finite regression for the prime Clark/Redheffer continuation."""
from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

import numpy as np


FACTORS = (
    (0.07, 0.21),
    (0.11, 0.37),
    (0.03, 0.28),
    (0.17, 0.43),
)


def params(alpha: float, beta: float) -> tuple[float, float]:
    c = (1.0 - beta) / (1.0 - alpha)
    delta2 = (beta - alpha) * (1.0 - alpha * beta) / (1.0 - alpha) ** 2
    return c, math.sqrt(delta2)


def local(alpha: float, beta: float, z: complex) -> tuple[complex, complex, complex]:
    c, delta = params(alpha, beta)
    m = c * (1.0 - alpha * z) / (1.0 - beta * z)
    d = delta * (1.0 - z) / (1.0 - beta * z)
    h = (1.0 - m) / (1.0 + m)
    return m, d, h


def product_m(z: complex) -> complex:
    out = 1.0 + 0.0j
    for alpha, beta in FACTORS:
        out *= local(alpha, beta, z)[0]
    return out


def product_h(z: complex) -> complex:
    m = product_m(z)
    return (1.0 - m) / (1.0 + m)


def build() -> dict[str, object]:
    max_julia = 0.0
    max_dissipation = 0.0
    max_redheffer = 0.0
    max_telescope = 0.0
    min_real_h = float("inf")

    for k in range(4096):
        theta = 2.0 * math.pi * k / 4096.0
        z = cmath.exp(1j * theta)
        ms: list[complex] = []
        ds: list[complex] = []
        hs: list[complex] = []
        for alpha, beta in FACTORS:
            m, d, h = local(alpha, beta, z)
            even = (1.0 + m) / math.sqrt(2.0)
            max_julia = max(max_julia, abs(abs(m) ** 2 + abs(d) ** 2 - 1.0))
            max_dissipation = max(
                max_dissipation,
                abs(2.0 * h.real * abs(even) ** 2 - abs(d) ** 2),
            )
            min_real_h = min(min_real_h, h.real)
            ms.append(m)
            ds.append(d)
            hs.append(h)

        m_product = 1.0 + 0.0j
        h_redheffer = 0.0 + 0.0j
        defect_sum = 0.0
        transmitted_weight = 1.0
        for j, (m, d, h) in enumerate(zip(ms, ds, hs)):
            h_redheffer = h if j == 0 else (h_redheffer + h) / (1.0 + h_redheffer * h)
            defect_sum += transmitted_weight * abs(d) ** 2
            transmitted_weight *= abs(m) ** 2
            m_product *= m

        max_redheffer = max(
            max_redheffer,
            abs((1.0 - m_product) / (1.0 + m_product) - h_redheffer),
        )
        max_telescope = max(
            max_telescope,
            abs(1.0 - abs(m_product) ** 2 - defect_sum),
        )

    nodes = np.array(
        [0.05 + 0.10j, -0.20 + 0.15j, 0.30 - 0.10j, -0.40 - 0.20j],
        dtype=complex,
    )
    kernel = np.empty((len(nodes), len(nodes)), dtype=complex)
    for i, z in enumerate(nodes):
        for j, w in enumerate(nodes):
            kernel[i, j] = (
                product_h(z) + np.conj(product_h(w))
            ) / (1.0 - z * np.conj(w))
    kernel = (kernel + kernel.conj().T) / 2.0
    eigenvalues = np.linalg.eigvalsh(kernel)

    resonance_details = []
    resonance_product = 1.0 + 0.0j
    for alpha, beta in FACTORS:
        m, d, _h = local(alpha, beta, 1.0 + 0.0j)
        resonance_product *= m
        resonance_details.append(abs(d))

    gates = {
        "local_julia": max_julia < 2e-13,
        "cayley_dissipation": max_dissipation < 2e-13,
        "redheffer_addition": max_redheffer < 2e-13,
        "cascade_telescope": max_telescope < 2e-13,
        "herglotz_kernel": float(eigenvalues[0]) > 0.0,
        "resonance_return": abs(resonance_product - 1.0) < 2e-13
        and max(resonance_details) < 2e-13,
    }
    assert all(gates.values())

    return {
        "status": "PASS_PRIME_CLARK_REDHEFFER",
        "gates": gates,
        "factors": [list(x) for x in FACTORS],
        "max_local_julia_error": max_julia,
        "max_cayley_dissipation_error": max_dissipation,
        "max_redheffer_error": max_redheffer,
        "max_cascade_telescope_error": max_telescope,
        "minimum_boundary_real_impedance": min_real_h,
        "herglotz_kernel_eigenvalues": [float(x) for x in eigenvalues],
        "resonance_detail_magnitudes": resonance_details,
        "resonance_returned_product": [
            resonance_product.real,
            resonance_product.imag,
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = json.dumps(build(), sort_keys=True, separators=(",", ":")) + "\n"
    if args.json:
        args.json.write_text(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
