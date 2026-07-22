#!/usr/bin/env python3
"""Assemble and analyze a high-carrier D-0001 principal packet.

STATUS: discovery arithmetic only. Prime source files may be direct or
moment-corrected; neither path is an interval proof. The script uses mpmath for
the pole/archimedean closed forms and NumPy for the symmetric eigensolve.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

import mpmath as mp
import numpy as np


def geometric_corrections(n: int, L: mp.mpf, target: mp.mpf) -> tuple[mp.mpf, ...]:
    w = 2 * mp.pi * n / L
    w2 = w * w
    g_s = g_cc = g_x1 = g_x2 = mp.mpf("0")
    ratio = mp.exp(-2 * L)
    for k in range(100_000):
        c_k = mp.mpf(2 * k) + mp.mpf("0.5")
        e_k = mp.exp(-c_k * L)
        den = c_k * c_k + w2
        g_s += e_k / den
        g_cc += e_k * w2 / (c_k * den)
        g_x1 += e_k * c_k / den
        g_x2 += e_k * (c_k * c_k - w2) / (den * den)
        c_next = c_k + 2
        envelope = mp.exp(-c_next * L) / (1 - ratio)
        if max(envelope / (c_next * c_next), envelope / c_next) <= target:
            return g_s, g_cc, g_x1, g_x2
    raise RuntimeError("geometric correction series did not reach the target")


def sequences(n: int, L: mp.mpf, target: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    z = mp.mpc(mp.mpf("0.25"), mp.pi * n / L)
    psi = mp.digamma(z)
    psi1 = mp.polygamma(1, z)
    g_s, g_cc, g_x1, g_x2 = geometric_corrections(n, L, target)
    w = 2 * mp.pi * n / L
    S = mp.im(psi) / 2 - w * g_s
    CC = -(mp.re(psi) - mp.digamma(mp.mpf("0.25"))) / 2 + g_cc
    XC = mp.re(psi1) / 4 - L * g_x1 - g_x2
    return S, CC, XC


def constants(L: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    U = mp.exp(L / 2)
    J = -2 * mp.log(U + 1) + mp.log(U * U + 1) + 2 * mp.atan(U) + mp.log(2) - mp.pi / 2
    eL = mp.exp(L)
    kappa = mp.log(4 * mp.pi * (eL - 1) / (eL + 1)) + mp.euler
    prefactor = 32 * L * mp.sinh(L / 4) ** 2
    return prefactor, kappa, J


def load_source(path: Path) -> tuple[dict, list[mp.mpf], list[mp.mpf], int, int]:
    data = json.loads(path.read_text(encoding="utf-8"))
    ps = [mp.mpf(x) for x in data["PS"]]
    pd = [mp.mpf(x) for x in data["PD"]]
    if "n0" in data:
        first = int(data["n0"])
        source_center_offset = 0
    else:
        K = int(data["K"])
        first = int(data["n_center"]) - K
        source_center_offset = K
    if len(ps) != len(pd):
        raise ValueError("PS and PD lengths differ")
    return data, ps, pd, first, source_center_offset


def packet_matrix(
    source_path: Path,
    *,
    dimension: int,
    center_offset: int,
    dps: int,
) -> tuple[mp.matrix, dict]:
    mp.mp.dps = dps
    data, ps, pd, first_n, source_center = load_source(source_path)
    c = int(data["c"])
    L = mp.log(c)
    start_index = source_center + center_offset - (dimension - 1) // 2
    if start_index < 0 or start_index + dimension > len(ps):
        raise ValueError("requested packet lies outside the source array")
    ns = [first_n + start_index + j for j in range(dimension)]
    ids = [start_index + j for j in range(dimension)]
    target = mp.power(10, -(dps - 12))
    seq = [sequences(n, L, target) for n in ns]
    prefactor, kappa, J = constants(L)
    pi = mp.pi
    L2 = L * L
    matrix = mp.matrix(dimension, dimension)
    for i, n in enumerate(ns):
        S_n, CC_n, XC_n = seq[i]
        for j, m in enumerate(ns):
            S_m, _, _ = seq[j]
            w02 = prefactor * (L2 - 16 * pi * pi * m * n) / (
                (L2 + 16 * pi * pi * m * m) * (L2 + 16 * pi * pi * n * n)
            )
            if i == j:
                wr = kappa + 2 * CC_n + J - (2 / L) * XC_n
                wp = pd[ids[i]]
            else:
                wr = (S_m - S_n) / (pi * (n - m))
                wp = (ps[ids[j]] - ps[ids[i]]) / (pi * (n - m))
            matrix[i, j] = (w02 - wr - wp) / (2 * pi)
    metadata = {
        "c": c,
        "dimension": dimension,
        "center_offset": center_offset,
        "first_index": ns[0],
        "last_index": ns[-1],
        "center_height": mp.nstr(2 * pi * (first_n + source_center + center_offset) / L, 35),
        "dps": dps,
    }
    return matrix, metadata


def analyze(source_path: Path, dimension: int, center_offset: int, dps: int) -> dict:
    matrix, meta = packet_matrix(
        source_path, dimension=dimension, center_offset=center_offset, dps=dps
    )
    array = np.array(
        [[float((matrix[i, j] + matrix[j, i]) / 2) for j in range(dimension)] for i in range(dimension)]
    )
    eigenvalues, eigenvectors = np.linalg.eigh(array)
    vector = mp.matrix([mp.mpf(str(x)) for x in eigenvectors[:, 0]])
    rayleigh = (vector.T * matrix * vector)[0] / (vector.T * vector)[0]
    residual = max(abs((matrix * vector)[i] - rayleigh * vector[i]) for i in range(dimension))
    return {
        **meta,
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "minimum_diagonal": format(float(np.diag(array).min()), ".17g"),
        "minimum_eigenvalue_binary64": format(float(eigenvalues[0]), ".17g"),
        "rayleigh_recomputed_mpmath": mp.nstr(rayleigh, 45),
        "residual_inf_norm": mp.nstr(residual, 15),
        "vector": [format(float(x), ".17g") for x in eigenvectors[:, 0]],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--dimension", type=int, default=64)
    parser.add_argument("--center-offset", type=int, default=0)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--output", type=Path, default=None)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.dimension < 1 or args.dps < 40:
        raise SystemExit("dimension must be positive and dps at least 40")
    result = analyze(args.source, args.dimension, args.center_offset, args.dps)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
