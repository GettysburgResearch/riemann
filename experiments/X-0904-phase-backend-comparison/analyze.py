#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh, toeplitz


def matrix(data: dict, prefix: str) -> np.ndarray:
    cells = int(data["K"])
    values = np.asarray(data[prefix + "_real"]) + 1j * np.asarray(
        data[prefix + "_imag"]
    )
    first = np.empty(cells, dtype=np.complex128)
    first[0] = values[0].real
    first[1:] = 0.5 * values[1:]
    return toeplitz(np.conj(first), first)


def analyze(path: Path) -> dict:
    data = json.loads(path.read_text())
    cells = int(data["K"])
    alpha = math.log(float(data["T"]) / (2 * math.pi)) / (2 * math.pi)
    long_matrix = matrix(data, "long")
    quad_matrix = matrix(data, "quad")
    result = {}
    for name, current in (
        ("long_double", long_matrix),
        ("binary128_phase", quad_matrix),
    ):
        largest = float(
            eigh(
                current,
                eigvals_only=True,
                subset_by_index=[cells - 1, cells - 1],
                driver="evr",
            )[0]
        )
        result[name] = {
            "largest_prime_eigenvalue": largest,
            "leading_margin": alpha - largest,
        }
    difference = long_matrix - quad_matrix
    endpoints = eigh(
        difference,
        eigvals_only=True,
        subset_by_index=[0, cells - 1],
        driver="evr",
    )
    result.update(
        {
            "cutoff": data["cutoff"],
            "K": cells,
            "T": data["T"],
            "prime_count": data["prime_count"],
            "prime_power_count": data["prime_power_count"],
            "maximum_coefficient_difference": data[
                "maximum_coefficient_difference"
            ],
            "coefficient_l1_difference": data["coefficient_l1_difference"],
            "toeplitz_operator_difference": float(
                max(abs(endpoints[0]), abs(endpoints[-1]))
            ),
            "margin_shift": (
                result["binary128_phase"]["leading_margin"]
                - result["long_double"]["leading_margin"]
            ),
            "status": "EMPIRICAL_NOT_CERTIFIED",
            "counterexample_candidate": None,
        }
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(analyze(args.input), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
