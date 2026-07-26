#!/usr/bin/env python3
"""Discovery-only ranker for slab-complement cross-height Pick packets.

Floating linear algebra may nominate an exact Gaussian-dyadic zero-sum vector.
It never decides a proof sign; verify_slab_complement.py must replay it.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import numpy as np


def q(value):
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, list) and len(value) == 2:
        return Fraction(int(value[0]), int(value[1]))
    raise ValueError("rational required")


def midpoint(raw):
    return (float(q(raw["lower"])) + float(q(raw["upper"]))) / 2.0


def load_points(payload):
    zs, fs = [], []
    for point in payload["points"]:
        zs.append(float(q(point["x"])) + 1j * float(q(point["t"])))
        f = point["f"]
        fs.append(midpoint(f["real"]) + 1j * midpoint(f["imag"]))
    return np.asarray(zs, dtype=np.complex128), np.asarray(fs, dtype=np.complex128)


def build_matrix(payload):
    a = float(q(payload["slab"]["lower"]))
    b = float(q(payload["slab"]["upper"]))
    center = (a + b) / 2.0
    half = (b - a) / 2.0
    zs, fs = load_points(payload)
    w = zs - 1j * center
    n = len(zs)
    matrix = np.empty((n, n), dtype=np.complex128)
    for i in range(n):
        for j in range(n):
            alpha_ij = (-half * half - w[i] * w[i]) / (w[i] + np.conj(w[j]))
            alpha_ji = (-half * half - w[j] * w[j]) / (w[j] + np.conj(w[i]))
            matrix[i, j] = alpha_ij * fs[i] + np.conj(alpha_ji * fs[j])

    for row in payload["zero_bins"]:
        gamma = (float(q(row["lower"])) + float(q(row["upper"]))) / 2.0
        count = int(q(row["count"]))
        weight = (gamma - a) * (gamma - b)
        h = 1.0 / (np.conj(zs) + 1j * gamma)
        matrix -= count * weight * np.outer(h, np.conj(h))
    return (matrix + matrix.conj().T) / 2.0


def nullspace_basis(size):
    basis = np.zeros((size, size - 1), dtype=np.complex128)
    for j in range(size - 1):
        basis[j, j] = 1.0
        basis[-1, j] = -1.0
    qmat, _ = np.linalg.qr(basis)
    return qmat[:, : size - 1]


def freeze(vector, bits):
    vector = vector / np.linalg.norm(vector)
    scale = 1 << bits
    real = [int(np.rint(value.real * scale)) for value in vector]
    imag = [int(np.rint(value.imag * scale)) for value in vector]
    pivot = int(np.argmax(np.abs(vector)))
    real[pivot] = -sum(value for index, value in enumerate(real) if index != pivot)
    imag[pivot] = -sum(value for index, value in enumerate(imag) if index != pivot)
    if not any(real) and not any(imag):
        raise ValueError("dyadic freezing produced the zero vector")
    return [
        {"re": f"{r}/{scale}", "im": f"{s}/{scale}"}
        for r, s in zip(real, imag)
    ], pivot


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("--bits", type=int, default=52)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    payload = json.loads(args.packet.read_text(encoding="utf-8"))
    matrix = build_matrix(payload)
    basis = nullspace_basis(len(matrix))
    reduced = basis.conj().T @ matrix @ basis
    values, vectors = np.linalg.eigh(reduced)
    index = int(np.argmin(values))
    vector = basis @ vectors[:, index]
    frozen, pivot = freeze(vector, args.bits)

    result = {
        "schema": "riemann.slab-complement-pick.nomination.v1",
        "classification": "DISCOVERY_ONLY_EXACT_VECTOR; exact checker must decide sign",
        "midpoint_minimum_eigenvalue": repr(float(values[index])),
        "point_ids": [point["id"] for point in payload["points"]],
        "dyadic_bits": args.bits,
        "zero_sum_repair_pivot": pivot,
        "vector": frozen,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
