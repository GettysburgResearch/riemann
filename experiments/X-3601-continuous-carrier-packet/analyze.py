#!/usr/bin/env python3
"""Analyze one empirical L-3602 leading matrix emitted by the C++ producer."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def analyze(data: dict) -> dict:
    if data.get("schema") != "riemann.legendre-carrier-leading-matrix.v1":
        raise ValueError("unexpected input schema")
    matrix = np.asarray(data["matrix"], dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("matrix must be square")
    if not np.allclose(matrix, matrix.T, rtol=0, atol=1e-12):
        raise ValueError("matrix is not symmetric")
    values, vectors = np.linalg.eigh((matrix + matrix.T) / 2)
    vector = vectors[:, 0]
    residual = matrix @ vector - values[0] * vector
    return {
        "schema": "riemann.legendre-carrier-analysis.v1",
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "cutoff": int(data["cutoff"]),
        "carrier": data["T"],
        "order": int(data["order"]),
        "dimension": int(data["dimension"]),
        "prime_power_terms": int(data["prime_power_terms"]),
        "minimum_leading_eigenvalue": float(values[0]),
        "minimum_diagonal": float(np.min(np.diag(matrix))),
        "residual_inf_norm": float(np.linalg.norm(residual, ord=np.inf)),
        "vector": [float(x) for x in vector],
        "counterexample_candidate": None,
        "warning": data["warning"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.matrix.read_text(encoding="utf-8"))
    result = analyze(data)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
