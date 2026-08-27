#!/usr/bin/env python3
"""Exact replay for the critical beta single-spectral-witness principle."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "8192514ed68f50b8e2a9cff9e1bedab2478bb5c1"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_CRITICAL_BETA_FOURIER_LATTICE_COMPRESSION.md": (
        "2334c471d37456acd974765d15c21122f65d01b1"
    ),
    "research/l-families/atlas/function_field/ffps_critical_beta_fourier_lattice_compression.py": (
        "ad0fe111e1cd4be4a56f0da8171fe5cc6cec4d14"
    ),
    "research/l-families/atlas/function_field/ffps_critical_beta_fourier_lattice_compression.json": (
        "9cc5d8cf91a00fb18a5a416c0c1a4c8963ff4986"
    ),
    "tests/test_ffps_critical_beta_fourier_lattice_compression.py": (
        "3c71d664649a9cfd3f5840f5ccfa0b6487bb7b67"
    ),
    "research/l-families/atlas/function_field/FFPS_DUPLICATE67_CRITICAL_SCALE_FILTER_FIREWALL.md": (
        "3a66ff2c438945ba3c25193fa6c36734e59bc09f"
    ),
    "research/l-families/atlas/function_field/ffps_duplicate67_critical_scale_filter_firewall.py": (
        "4a67f44518dad3116aed2b23716cbfbeccea131d"
    ),
    "research/l-families/atlas/function_field/ffps_duplicate67_critical_scale_filter_firewall.json": (
        "60d20a60b378fc22632195a4c9f1c6d6eff916dc"
    ),
    "tests/test_ffps_duplicate67_critical_scale_filter_firewall.py": (
        "b63c96d25d5c4829ed6854785464c528959d885b"
    ),
}

TOY_SCALE_MODULUS = Fraction(1, 5)
SCALE_DEPTH = 9
FREQUENCY_COUNT = 3

Gaussian = tuple[Fraction, Fraction]


def check_source_contract() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {path}")


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gneg(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def gsub(left: Gaussian, right: Gaussian) -> Gaussian:
    return gadd(left, gneg(right))


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gscale(value: Gaussian, scalar: Fraction) -> Gaussian:
    return value[0] * scalar, value[1] * scalar


def gnorm2(value: Gaussian) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def ell2_linfty_panel() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for size in range(1, 13):
        values = tuple(Fraction((index + 1) ** 2, size + 1) for index in range(size))
        maximum = max(value * value for value in values)
        energy = sum((value * value for value in values), Fraction(0))
        if not maximum <= energy <= size * maximum:
            raise ArithmeticError("finite ell2/ell-infinity comparison changed")
        rows.append(
            {
                "coordinate_count": size,
                "maximum_square": str(maximum),
                "energy": str(energy),
                "energy_over_maximum": str(energy / maximum),
            }
        )
    return {
        "rows": rows,
        "theorem": "max_j|z_j|^2<=sum_j|z_j|^2<=N*max_j|z_j|^2",
        "subpower_consequence": (
            "when N(X)=X^o(1), the squared ell2 and squared ell-infinity "
            "targets are exponent-equivalent"
        ),
    }


def dft4(values: tuple[Gaussian, Gaussian, Gaussian, Gaussian]) -> tuple[Gaussian, ...]:
    roots = (
        ((Fraction(1), Fraction(0)),) * 4,
        (
            (Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(-1)),
            (Fraction(-1), Fraction(0)),
            (Fraction(0), Fraction(1)),
        ),
        (
            (Fraction(1), Fraction(0)),
            (Fraction(-1), Fraction(0)),
            (Fraction(1), Fraction(0)),
            (Fraction(-1), Fraction(0)),
        ),
        (
            (Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(1)),
            (Fraction(-1), Fraction(0)),
            (Fraction(0), Fraction(-1)),
        ),
    )
    return tuple(
        sum_gaussians(
            gmul(value, root) for value, root in zip(values, row, strict=True)
        )
        for row in roots
    )


def sum_gaussians(values: object) -> Gaussian:
    total = (Fraction(0), Fraction(0))
    for value in values:
        total = gadd(total, value)
    return total


def weight_mass_panel() -> dict[str, object]:
    field = (
        (Fraction(1), Fraction(0)),
        (Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    spectrum = dft4(field)
    spatial_energy = sum((gnorm2(value) for value in field), Fraction(0))
    spectral_energy = sum((gnorm2(value) for value in spectrum), Fraction(0))
    if spectral_energy != 4 * spatial_energy:
        raise ArithmeticError("weight-only Parseval normalization changed")
    if spectrum[0] != (Fraction(0), Fraction(0)):
        raise ArithmeticError("mean-zero central coordinate no longer vanishes")
    weights = tuple(gnorm2(value) / 4 for value in spectrum)
    return {
        "period_cells": 4,
        "field": [[str(real), str(imag)] for real, imag in field],
        "weight_mass": [str(value) for value in weights],
        "total_weight": str(sum(weights, Fraction(0))),
        "spatial_energy": str(spatial_energy),
        "central_weight": str(weights[0]),
        "identity": "(1/L)*sum_k|Bhat(t_k)|^2=||B||_2^2",
    }


def scale_filter(values: tuple[Gaussian, ...], omega: Gaussian) -> tuple[Gaussian, ...]:
    if not values:
        raise ValueError("scale sequence must be nonempty")
    zero = (Fraction(0), Fraction(0))
    return tuple(
        gsub(value, gmul(omega, values[index + 1] if index + 1 < len(values) else zero))
        for index, value in enumerate(values)
    )


def inverse_scale_filter(
    values: tuple[Gaussian, ...], omega: Gaussian
) -> tuple[Gaussian, ...]:
    if not values:
        raise ValueError("scale sequence must be nonempty")
    reconstructed: list[Gaussian] = []
    for index in range(len(values)):
        total = (Fraction(0), Fraction(0))
        omega_power = (Fraction(1), Fraction(0))
        for offset in range(len(values) - index):
            total = gadd(total, gmul(omega_power, values[index + offset]))
            omega_power = gmul(omega_power, omega)
        reconstructed.append(total)
    return tuple(reconstructed)


def weighted_max_square(
    panels: tuple[tuple[Gaussian, ...], ...], weights: tuple[Fraction, ...]
) -> Fraction:
    if not panels or any(len(row) != len(weights) for row in panels):
        raise ValueError("panel and weight shapes must agree")
    return max(
        weight * gnorm2(value)
        for row in panels
        for value, weight in zip(row, weights, strict=True)
    )


def common_lattice_scale_panel() -> dict[str, object]:
    weights = (Fraction(1, 7), Fraction(3, 11), Fraction(5, 13))
    unit_phases = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(-3, 5), Fraction(4, 5)),
    )
    omegas = tuple(gscale(phase, TOY_SCALE_MODULUS) for phase in unit_phases)
    ordinary_by_frequency: list[tuple[Gaussian, ...]] = []
    beta_by_frequency: list[tuple[Gaussian, ...]] = []
    qfree_by_frequency: list[tuple[Gaussian, ...]] = []
    beta_from_qfree_by_frequency: list[tuple[Gaussian, ...]] = []
    for frequency, omega in enumerate(omegas):
        qfree = tuple(
            (
                Fraction((scale + 2) * (frequency + 1), scale + 1),
                Fraction(((-1) ** scale) * (frequency + 2), scale + 2),
            )
            for scale in range(SCALE_DEPTH)
        )
        ordinary = scale_filter(qfree, omega)
        beta = scale_filter(ordinary, omega)
        if inverse_scale_filter(beta, omega) != ordinary:
            raise ArithmeticError("ordinary prefix ladder did not reconstruct")
        if inverse_scale_filter(ordinary, omega) != qfree:
            raise ArithmeticError("q-free prefix ladder did not reconstruct")
        ordinary_by_frequency.append(ordinary)
        beta_by_frequency.append(beta)
        qfree_by_frequency.append(qfree)
        beta_from_qfree_by_frequency.append(
            scale_filter(scale_filter(qfree, omega), omega)
        )

    ordinary_panel = tuple(
        tuple(ordinary_by_frequency[k][j] for k in range(FREQUENCY_COUNT))
        for j in range(SCALE_DEPTH)
    )
    beta_panel = tuple(
        tuple(beta_by_frequency[k][j] for k in range(FREQUENCY_COUNT))
        for j in range(SCALE_DEPTH)
    )
    qfree_panel = tuple(
        tuple(qfree_by_frequency[k][j] for k in range(FREQUENCY_COUNT))
        for j in range(SCALE_DEPTH)
    )
    beta_qfree_panel = tuple(
        tuple(beta_from_qfree_by_frequency[k][j] for k in range(FREQUENCY_COUNT))
        for j in range(SCALE_DEPTH)
    )
    if beta_panel != beta_qfree_panel:
        raise ArithmeticError("squared scale filter changed")

    ordinary_max = weighted_max_square(ordinary_panel, weights)
    beta_max = weighted_max_square(beta_panel, weights)
    qfree_max = weighted_max_square(qfree_panel, weights)
    a = TOY_SCALE_MODULUS
    if not (1 - a) ** 2 * ordinary_max <= beta_max <= (1 + a) ** 2 * ordinary_max:
        raise ArithmeticError("single-filter weighted witness bound changed")
    if not (1 - a) ** 4 * qfree_max <= beta_max <= (1 + a) ** 4 * qfree_max:
        raise ArithmeticError("squared-filter weighted witness bound changed")
    return {
        "scale_depth": SCALE_DEPTH,
        "frequency_count": FREQUENCY_COUNT,
        "toy_modulus": str(a),
        "ordinary_weighted_max_square": str(ordinary_max),
        "beta_weighted_max_square": str(beta_max),
        "qfree_weighted_max_square": str(qfree_max),
        "single_filter_bounds": [
            str((1 - a) ** 2 * ordinary_max),
            str((1 + a) ** 2 * ordinary_max),
        ],
        "squared_filter_bounds": [
            str((1 - a) ** 4 * qfree_max),
            str((1 + a) ** 4 * qfree_max),
        ],
        "common_lattice": (
            "all prefixes use one guarded period and the same weighted "
            "frequency coordinates before the scale supremum"
        ),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imports": (
                "critical Fourier-lattice compression and duplicate-67 "
                "maximal scale-filter firewall"
            ),
        },
        "single_witness": {
            "coordinate": ("Z_X(k)=L_X^(-1/2)*Bhat(t_(k,X))*D_X(t_(k,X))"),
            "finite_comparison": (
                "max_(0<|k|<=K_*)|Z_X(k)|^2 <= Q_*(X) <= "
                "2*K_*(X)*max_(0<|k|<=K_*)|Z_X(k)|^2"
            ),
            "rh_equivalence": ("RH iff max_(0<|k|<=K_*)|Z_X(k)|^2=X^o(1)"),
            "off_rh_witness": (
                "if RH fails, some epsilon>0, unbounded X_j, and retained "
                "k_j have |Z_(X_j)(k_j)|^2>=X_j^epsilon"
            ),
            "unweighted_warning": (
                "the equivalent maximum is the weighted coordinate Z_X(k), "
                "not the raw D_X(t_k); Bhat can be very small"
            ),
        },
        "weight_probability": {
            "full_mass": ("(1/L_X)*sum_(k in Z)|Bhat(t_k)|^2=||B||_2^2 exactly"),
            "critical_retained_mass": "||B||_2^2+O(X^(-1+o(1)))",
            "probability_view": (
                "after normalizing retained weights, Q_*(X) is total retained "
                "weight times E_pi |D_X(t_k)|^2"
            ),
        },
        "maximal_common_lattice": {
            "definition": (
                "W_F(X)=sup_(1<=Y<=X) max_(0<|k|<=K_*(X)) |Bhat(t_k)|^2|F_Y(t_k)|^2/L_X"
            ),
            "rh_equivalence": "RH iff W_beta(X)=X^o(1)",
            "beta_vs_mobius": ("(1-67^-1/2)^2 W_M <= W_beta <= (1+67^-1/2)^2 W_M"),
            "beta_vs_67free": ("(1-67^-1/2)^4 W_A <= W_beta <= (1+67^-1/2)^4 W_A"),
            "verdict": (
                "the exceptional source filter creates no hidden small "
                "single-frequency witness direction"
            ),
        },
        "bounded_replay": {
            "ell2_linfty": ell2_linfty_panel(),
            "weight_mass": weight_mass_panel(),
            "common_lattice_scale": common_lattice_scale_panel(),
        },
        "scope": {
            "continuum_replaced_by_exact_lattice": True,
            "subpower_lattice_replaced_by_weighted_maximum": True,
            "raw_unweighted_pointwise_bound_equivalent": False,
            "retained_witness_estimate_proved": False,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "toy_fourier_cells": 4,
            "toy_scale_depth": SCALE_DEPTH,
            "toy_frequency_count": FREQUENCY_COUNT,
            "primes_enumerated": 0,
            "zeta_zeros": 0,
            "floating_point_operations": 0,
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
