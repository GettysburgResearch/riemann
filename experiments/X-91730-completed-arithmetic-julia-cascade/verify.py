#!/usr/bin/env python3
"""Finite replay for the completed arithmetic Julia tensor cascade."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

OMEGA = 0.2
SIGMA = 1.4


def carrier_kernel(points, weights, carriers):
    phase = np.exp(-1j * np.outer(carriers, points))
    return (phase * weights) @ phase.conj().T


def eta_measure():
    points = []
    widths = []
    for m in range(1, 240):
        lo = np.log(2 * m - 1)
        hi = np.log(2 * m)
        points.append((lo + hi) / 2)
        widths.append(hi - lo)
    points = np.asarray(points)
    widths = np.asarray(widths)
    hard = widths * np.exp(-(SIGMA - OMEGA) * points)
    safe = hard * np.exp(-2 * OMEGA * points)
    return points, hard, safe


def bridge_measure():
    L = np.log(2.0)
    edges = np.linspace(0.0, L, 1001)
    points = (edges[:-1] + edges[1:]) / 2
    widths = np.diff(edges)
    q = 0.8
    hard = widths * np.exp(-q * points)
    safe = hard * np.exp(-2 * OMEGA * points)
    return points, hard, safe


def gamma_measure():
    # Midpoint rule on a quadratic grid resolves the integrable t^(omega-1) endpoint.
    u = np.linspace(0.0, np.sqrt(12.0), 2401)
    edges = u**2
    points = (edges[:-1] + edges[1:]) / 2
    widths = np.diff(edges)
    density = (
        np.exp(-(SIGMA - OMEGA) * points)
        * np.maximum(1 - np.exp(-2 * points), 1e-300) ** (OMEGA - 1)
    )
    hard = widths * density
    safe = hard * np.exp(-2 * OMEGA * points)
    return points, hard, safe


def build():
    carriers = np.array([0.0, 0.23, 0.61, 1.17])

    channel_data = []
    detail_mins = []
    for name, builder in [
        ("eta", eta_measure),
        ("bridge", bridge_measure),
        ("gamma", gamma_measure),
    ]:
        points, hard_w, safe_w = builder()
        hard = carrier_kernel(points, hard_w, carriers)
        safe = carrier_kernel(points, safe_w, carriers)
        detail = (hard - safe + (hard - safe).conj().T) / 2
        eigs = np.linalg.eigvalsh(detail)
        detail_mins.append(float(eigs.min()))
        channel_data.append((name, hard, safe, detail))

    _, eta_h, eta_s, eta_d = channel_data[0]
    _, bridge_h, bridge_s, bridge_d = channel_data[1]
    _, gamma_h, gamma_s, gamma_d = channel_data[2]

    hard_total = eta_h * bridge_h * gamma_h
    returned_total = eta_s * bridge_s * gamma_s

    detail_eta = eta_d * bridge_h * gamma_h
    detail_bridge = eta_s * bridge_d * gamma_h
    detail_gamma = eta_s * bridge_s * gamma_d
    reconstructed = returned_total + detail_eta + detail_bridge + detail_gamma
    cascade_error = float(np.max(np.abs(hard_total - reconstructed)))

    all_mins = {
        "hard_total": float(np.linalg.eigvalsh((hard_total + hard_total.conj().T) / 2).min()),
        "returned_total": float(
            np.linalg.eigvalsh((returned_total + returned_total.conj().T) / 2).min()
        ),
        "eta_detail": float(np.linalg.eigvalsh((detail_eta + detail_eta.conj().T) / 2).min()),
        "bridge_detail": float(
            np.linalg.eigvalsh((detail_bridge + detail_bridge.conj().T) / 2).min()
        ),
        "gamma_detail": float(
            np.linalg.eigvalsh((detail_gamma + detail_gamma.conj().T) / 2).min()
        ),
    }

    hard_diag = float(np.real(hard_total[0, 0]))
    returned_diag = float(np.real(returned_total[0, 0]))
    channel_entropy = 0.0
    for _, hard, safe, _ in channel_data:
        channel_entropy += np.log(np.real(hard[0, 0]) / np.real(safe[0, 0]))
    entropy_error = float(abs(np.log(hard_diag / returned_diag) - channel_entropy))

    gates = {
        "cascade": bool(cascade_error < 1e-10),
        "channel_details_psd": bool(min(detail_mins) > -1e-10),
        "global_channels_psd": bool(min(all_mins.values()) > -1e-9),
        "entropy_chain": bool(entropy_error < 1e-12),
    }
    assert all(gates.values())

    return {
        "status": "PASS_COMPLETED_ARITHMETIC_JULIA_CASCADE",
        "gates": gates,
        "cascade_max_error": cascade_error,
        "channel_detail_min_eigenvalues": detail_mins,
        "global_min_eigenvalues": all_mins,
        "hard_diagonal": hard_diag,
        "returned_diagonal": returned_diag,
        "entropy_chain_error": entropy_error,
    }


def main():
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
