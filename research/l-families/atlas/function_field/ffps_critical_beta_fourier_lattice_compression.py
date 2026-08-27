#!/usr/bin/env python3
"""Bounded replay for exact Fourier-lattice compression of beta energy."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREDECESSOR_COMMIT = "b631040b76d696dbc69cadde7af240077f605c94"
PREDECESSOR_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_INFINITE_DYADIC_BOX_BANDPASS_SMOOTHER.md": (
        "01d3ea427883fb761f6301f71d9dd05c552c5056"
    ),
    "research/l-families/atlas/function_field/ffps_infinite_dyadic_box_bandpass_smoother.py": (
        "2ba0f30c9bd67cdb01af639d320daf8133b5bb77"
    ),
    "research/l-families/atlas/function_field/ffps_infinite_dyadic_box_bandpass_smoother.json": (
        "7a38b5f943a8dc1c0afde8d1cc91f35118b767ca"
    ),
    "tests/test_ffps_infinite_dyadic_box_bandpass_smoother.py": (
        "d6a30d654d46edfa01add55cec55b0b3253a12b0"
    ),
}

BINARY_BLOCK_CAP = 18
TOY_FIELDS = (
    (3, -1, 4, 2),
    (1, 0, -1, 0),
    (5, 5, 5, 5),
)

Gaussian = tuple[int, int]


def check_source_contract() -> None:
    for path, expected in PREDECESSOR_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{PREDECESSOR_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"predecessor blob mismatch: {path}")


def gaussian_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gaussian_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[
        1
    ] * right[0]


def gaussian_abs_square(value: Gaussian) -> int:
    return value[0] ** 2 + value[1] ** 2


def fourth_root_power(exponent: int) -> Gaussian:
    return ((1, 0), (0, 1), (-1, 0), (0, -1))[exponent % 4]


def dft4(field: tuple[int, int, int, int]) -> tuple[Gaussian, ...]:
    if len(field) != 4:
        raise ValueError("the bounded exact replay uses four cells")
    return tuple(
        sum_gaussians(
            gaussian_mul((value, 0), fourth_root_power(-frequency * position))
            for position, value in enumerate(field)
        )
        for frequency in range(4)
    )


def sum_gaussians(values: object) -> Gaussian:
    result = (0, 0)
    for value in values:
        result = gaussian_add(result, value)
    return result


def parseval_panel() -> dict[str, object]:
    rows = []
    for field in TOY_FIELDS:
        transform = dft4(field)
        spatial_energy = sum(value * value for value in field)
        spectral_energy = sum(gaussian_abs_square(value) for value in transform)
        if spectral_energy != 4 * spatial_energy:
            raise ArithmeticError("four-cell Parseval normalization changed")
        rows.append(
            {
                "field": list(field),
                "spatial_energy": spatial_energy,
                "spectral_energy": spectral_energy,
                "normalization": "spectral=4*spatial",
            }
        )
    return {"rows": rows}


def stair_block_exponent(binary_scale: int) -> int:
    if (
        isinstance(binary_scale, bool)
        or not isinstance(binary_scale, int)
        or not 3 <= binary_scale <= BINARY_BLOCK_CAP
    ):
        raise ValueError("binary scale exceeds the bounded replay cap")
    # Squared smoother envelope contributes -(M-1)(M-2), while the
    # lattice point count in the block contributes +M.
    return -((binary_scale - 1) * (binary_scale - 2)) + binary_scale


def stair_panel() -> dict[str, object]:
    rows = []
    for binary_scale in range(3, BINARY_BLOCK_CAP + 1):
        exponent = stair_block_exponent(binary_scale)
        expected = -(binary_scale**2) + 4 * binary_scale - 2
        if exponent != expected:
            raise ArithmeticError("lattice stair exponent changed")
        rows.append(
            {
                "M": binary_scale,
                "lattice_block_upper_bound": f"constant*2^({exponent})",
            }
        )
    return {"rows": rows}


def rank_panel(max_log_height: int = 12) -> dict[str, object]:
    if (
        isinstance(max_log_height, bool)
        or not isinstance(max_log_height, int)
        or max_log_height < 1
    ):
        raise ValueError("max_log_height must be a positive integer")
    rows = []
    for log_height in range(1, max_log_height + 1):
        # Integer surrogate for L*T with L comparable to log X and
        # T=exp(sqrt(log(2)*log X)); this replay checks only rank counting.
        retained_radius = log_height * (2 ** ((log_height + 1) // 2))
        rows.append(
            {
                "integer_log_height": log_height,
                "retained_radius_surrogate": retained_radius,
                "nonzero_gram_rank_upper_bound": 2 * retained_radius,
            }
        )
    return {
        "rows": rows,
        "theorem_scale": (
            "rank <= 2*ceil(L_X*exp(sqrt(log(2)*log(X)))/(2*pi)) = X^o(1)"
        ),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commit": PREDECESSOR_COMMIT,
            "git_blobs": PREDECESSOR_BLOBS,
            "imported": (
                "fixed compact infinite-smoother beta field, exact energy, "
                "stair envelope, and critical tail exponent"
            ),
            "source_line_endings": "irrelevant because Git object IDs are pinned",
        },
        "exact_lattice_identity": {
            "guarded_period": "L_X=log(X)+S_(r,infinity)+delta, fixed delta>0",
            "frequencies": "t_k=2*pi*k/L_X",
            "identity": ("E(X)=(1/L_X)*sum_(k in Z) |Bhat(t_k)|^2*|D_X(t_k)|^2"),
            "reason": "compact support plus Fourier-series Parseval",
        },
        "critical_compression": {
            "critical_frequency": "T_*(X)=exp(sqrt(log(2)*log(X)))",
            "retained_radius": "K_*(X)=ceil(L_X*T_*(X)/(2*pi))",
            "discarded_lattice_energy": "X^o(1) unconditionally",
            "retained_mode_count": (
                "2*K_*(X)+1=X^o(1), with k=0 universally identically zero"
            ),
            "rh_criterion": "RH iff the retained lattice energy is X^o(1)",
        },
        "finite_rank_gram": {
            "entries": (
                "G_X(m,n)=(1/L_X)*sum_(|k|<=K_*) |Bhat(t_k)|^2*exp(-i*t_k*log(m/n))"
            ),
            "positive_semidefinite": True,
            "rank_upper_bound": "2*K_*(X)=X^o(1) because Bhat(0)=0",
            "higher_fixed_notch_reduces_rank_further": False,
            "other_filter_zeros": (
                "special nonzero lattice alignments may occur, but no additional "
                "coordinate is universally removed for every X"
            ),
            "additive_remainder": "E(X)=Q_*(X)+R_*(X), 0<=R_*(X)<=X^o(1)",
            "estimate_proved_for_retained_form": False,
        },
        "parseval_replay": parseval_panel(),
        "stair_replay": stair_panel(),
        "rank_replay": rank_panel(),
        "scope": {
            "arbitrary_vector_operator_norm_compression": False,
            "exact_continuous_to_discrete_identity": True,
            "critical_tail_uses_only_trivial_beta_bound": True,
            "finite_rank_is_not_an_energy_bound": True,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "toy_fourier_cells": 4,
            "binary_stair_block": BINARY_BLOCK_CAP,
            "rank_surrogate_rows": 12,
            "zeta_zeros": 0,
            "finite_fields": 0,
            "curves": 0,
            "l_functions": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    if not args.check and not args.write_json:
        print(rendered, end="")


if __name__ == "__main__":
    main()
