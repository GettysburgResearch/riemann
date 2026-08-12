#!/usr/bin/env python3
"""Finite replay for the logarithmic Clark–Redheffer entropy identities."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 70


def node(alpha: float, beta: float):
    c = (1.0 - beta) / (1.0 - alpha)
    delta = np.sqrt((beta - alpha) * (1.0 - alpha * beta)) / (1.0 - alpha)

    def m(z: complex) -> complex:
        return c * (1.0 - alpha * z) / (1.0 - beta * z)

    def d(z: complex) -> complex:
        return delta * (1.0 - z) / (1.0 - beta * z)

    return m, d


def local_checks():
    m, d = node(0.2, 0.45)
    julia_err = 0.0
    entropy_err = 0.0
    resonance = None
    for theta in np.linspace(0.0, 2.0 * np.pi, 33, endpoint=False):
        z = np.exp(1j * theta)
        mz, dz = m(z), d(z)
        julia_err = max(julia_err, abs(abs(mz) ** 2 + abs(dz) ** 2 - 1.0))
        x = mp.mpf(abs(mz) ** 2)
        q = mp.mpf(abs(dz) ** 2)
        integral = mp.quad(lambda t: q / (x + t * q), [0, 1])
        entropy_err = max(entropy_err, float(abs(-mp.log(x) - integral)))
        if abs(theta) < 1e-15:
            resonance = {
                "m": float(abs(mz)),
                "d": float(abs(dz)),
                "entropy": float(-mp.log(x)),
            }

    cayley_err = 0.0
    min_re_log = 1e100
    zs = [0.11 + 0.07j, -0.19 + 0.12j, 0.31 - 0.18j, 0.57 + 0.09j]
    ell = []
    for z in zs:
        mz = m(z)
        h = (1.0 - mz) / (1.0 + mz)
        lz = -np.log(mz)
        ell.append(lz)
        cayley_err = max(cayley_err, abs(lz - 2.0 * np.arctanh(h)))
        min_re_log = min(min_re_log, float(np.real(lz)))

    K = np.array(
        [[(ell[i] + np.conj(ell[j])) / (1.0 - zs[i] * np.conj(zs[j])) for j in range(len(zs))]
         for i in range(len(zs))],
        dtype=np.complex128,
    )
    K = (K + K.conj().T) / 2.0
    eig = np.linalg.eigvalsh(K)
    return {
        "julia_error": float(julia_err),
        "entropy_integral_error": entropy_err,
        "log_cayley_error": float(cayley_err),
        "minimum_real_log_impedance": min_re_log,
        "herglotz_kernel_eigenvalues": [float(v) for v in eig],
        "resonance": resonance,
    }


def cascade_checks():
    params = [(0.07, 0.18), (0.12, 0.31), (0.19, 0.43), (0.24, 0.52)]
    nodes = [node(a, b)[0] for a, b in params]
    zs = [0.13 + 0.09j, 0.41 - 0.16j, 0.72 + 0.04j]
    log_add_err = 0.0
    redheffer_err = 0.0
    for z in zs:
        ms = [m(z) for m in nodes]
        M = np.prod(ms)
        log_add_err = max(log_add_err, abs(-np.log(M) - sum(-np.log(v) for v in ms)))
        h = [(1.0 - v) / (1.0 + v) for v in ms]
        h_acc = h[0]
        m_acc = ms[0]
        for hj, mj in zip(h[1:], ms[1:]):
            h_acc = (h_acc + hj) / (1.0 + h_acc * hj)
            m_acc *= mj
        redheffer_err = max(redheffer_err, abs(h_acc - (1.0 - m_acc) / (1.0 + m_acc)))
    return {"log_additivity_error": float(log_add_err), "redheffer_error": float(redheffer_err)}


def matrix_entropy_check():
    rng = np.random.default_rng(20260812)
    X = rng.normal(size=(5, 5))
    Q, _ = np.linalg.qr(X)
    eig = np.array([0.08, 0.21, 0.43, 0.68, 0.91])
    A = Q @ np.diag(eig) @ Q.T
    integral = mp.mpf("0")
    for lam in eig:
        lam_mp = mp.mpf(str(lam))
        integral += mp.quad(lambda t: (1 - lam_mp) / (lam_mp + t * (1 - lam_mp)), [0, 1])
    target = -sum(mp.log(mp.mpf(str(lam))) for lam in eig)
    return {
        "logdet_resolvent_error": float(abs(integral - target)),
        "matrix_min_eigenvalue": float(np.min(np.linalg.eigvalsh(A))),
        "matrix_max_eigenvalue": float(np.max(np.linalg.eigvalsh(A))),
    }


def build():
    local = local_checks()
    cascade = cascade_checks()
    matrix = matrix_entropy_check()
    gates = {
        "local_julia": local["julia_error"] < 2e-14,
        "entropy_integral": local["entropy_integral_error"] < 2e-14,
        "log_cayley": local["log_cayley_error"] < 2e-14,
        "herglotz_psd": min(local["herglotz_kernel_eigenvalues"]) > 0,
        "cascade_log": cascade["log_additivity_error"] < 2e-14,
        "redheffer": cascade["redheffer_error"] < 2e-14,
        "matrix_entropy": matrix["logdet_resolvent_error"] < 1e-55,
        "resonance_returned": abs(local["resonance"]["m"] - 1.0) < 2e-14
        and local["resonance"]["d"] < 2e-14,
    }
    gates = {k: bool(v) for k, v in gates.items()}
    assert all(gates.values())
    return {
        "status": "PASS_LOG_CLARK_ENTROPY",
        "gates": gates,
        "local": local,
        "cascade": cascade,
        "matrix": matrix,
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
