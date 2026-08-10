#!/usr/bin/env python3
"""Regression for the finite off-line interpolation/capture theorem.

The experiment uses the rectangular aggregate-power profile, for which the
complete critical-lattice evaluation Gram has a closed form. It checks minimum-
norm interpolation, the target-pair Schur complement, monotonicity under added
zero constraints, and the exact local Weil value -2.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def interval_transform(
    z: np.ndarray | complex, length: float
) -> np.ndarray | complex:
    arr = np.asarray(z, dtype=np.complex128)
    out = np.empty_like(arr)
    small = np.abs(arr) < 1e-13
    out[small] = length
    out[~small] = (
        2.0 * np.sin(arr[~small] * length / 2.0) / arr[~small]
    )
    if np.ndim(z) == 0:
        return complex(out)
    return out


def evaluation_gram(points: np.ndarray, length: float) -> np.ndarray:
    diff = points[:, None] - np.conjugate(points[None, :])
    gram = length * interval_transform(diff, length)
    return (gram + gram.conj().T) / 2.0


def capture(
    points: np.ndarray, target: np.ndarray, length: float
) -> dict[str, object]:
    gram = evaluation_gram(points, length)
    alpha = np.linalg.solve(gram, target)
    recovered = gram @ alpha
    cost = float(np.vdot(target, alpha).real)
    return {
        "cost": cost,
        "min_gram_eigenvalue": float(np.min(np.linalg.eigvalsh(gram))),
        "interpolation_error": float(
            np.max(np.abs(recovered - target))
        ),
        "hermitian_error": float(
            np.linalg.norm(gram - gram.conj().T, ord="fro")
        ),
    }


def schur_cost(
    points: np.ndarray, target_pair: np.ndarray, length: float
) -> float:
    gram = evaluation_gram(points, length)
    if len(points) == 2:
        schur = gram
    else:
        target_block = gram[:2, :2]
        cross = gram[:2, 2:]
        nuisance = gram[2:, 2:]
        schur = target_block - cross @ np.linalg.solve(
            nuisance, cross.conj().T
        )
    return float(
        np.vdot(target_pair, np.linalg.solve(schur, target_pair)).real
    )


def run(
    length: float = 8.0, x: float = 0.37, y: float = 0.12
) -> dict[str, object]:
    pair = np.array([x + 1j * y, x - 1j * y], dtype=np.complex128)
    target_pair = np.array([1.0, -1.0], dtype=np.complex128)
    base = capture(pair, target_pair, length)

    ratio = np.sinh(y * length) / (y * length)
    expected_base_cost = 2.0 / (length**2 * (ratio - 1.0))

    nuisance_points = [x + 0.9, x - 0.7, x + 0.31, x - 0.18]
    costs = [base["cost"]]
    points = pair.copy()
    final: dict[str, object] = base
    for value in nuisance_points:
        points = np.concatenate(
            [points, np.array([value], dtype=np.complex128)]
        )
        target = np.zeros(len(points), dtype=np.complex128)
        target[:2] = target_pair
        final = capture(points, target, length)
        costs.append(final["cost"])
        schur = schur_cost(points, target_pair, length)
        if abs(schur - final["cost"]) > 5e-9 * max(
            1.0, final["cost"]
        ):
            raise AssertionError((schur, final["cost"]))

    final_target = np.zeros(len(points), dtype=np.complex128)
    final_target[:2] = target_pair
    local_weil_value = float(
        (
            final_target[0] * np.conjugate(final_target[1])
            + final_target[1] * np.conjugate(final_target[0])
        ).real
    )
    epsilon_threshold = 2.0 / final["cost"]

    gates = {
        "base_formula": abs(base["cost"] - expected_base_cost) < 2e-11,
        "positive_gram": final["min_gram_eigenvalue"] > 1e-8,
        "exact_interpolation": final["interpolation_error"] < 5e-10,
        "local_negative_value": abs(local_weil_value + 2.0) < 1e-13,
        "constraint_monotonicity": all(
            costs[index + 1] + 1e-10 >= costs[index]
            for index in range(len(costs) - 1)
        ),
    }
    return {
        "status": "PASS_ZETA23_FINITE_ISOLATION"
        if all(gates.values())
        else "FAIL",
        "gates": {key: bool(value) for key, value in gates.items()},
        "length": length,
        "pair": [[float(z.real), float(z.imag)] for z in pair],
        "ratio": float(ratio),
        "base_cost": base["cost"],
        "expected_base_cost": float(expected_base_cost),
        "nested_capture_costs": [float(value) for value in costs],
        "final_min_gram_eigenvalue": final["min_gram_eigenvalue"],
        "final_interpolation_error": final["interpolation_error"],
        "local_weil_value": local_weil_value,
        "far_tail_operator_threshold_for_m1": float(epsilon_threshold),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text + "\n", encoding="utf-8")
    if payload["status"] != "PASS_ZETA23_FINITE_ISOLATION":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
