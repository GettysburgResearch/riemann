#!/usr/bin/env python3
"""Exact bounded replay for the duplicate-67 critical scale-filter firewall."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "070be728e8d434bfb72645e23f9894acf920d3c0"
SOURCE_BLOBS = {
    "research/l-families/atlas/BETA_BANDPASS_WAVELET_FIVE_MINUTE_HANDOFF.md": (
        "130ef8d478929ce37a8ec4266d1e8b2277073078"
    ),
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
    "research/l-families/atlas/function_field/FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md": (
        "21ef8f5215ca349f0efffd52dca1543ef6d988d6"
    ),
    "research/l-families/atlas/function_field/ffps_assembled_beta_perron_fourier_bridge.py": (
        "2dbe93508eadcc9ba9ed15a5f64d02f13c728ef3"
    ),
    "research/l-families/atlas/function_field/ffps_assembled_beta_perron_fourier_bridge.json": (
        "1223ab8049492f58cf5e64a25f80d5799aa165f7"
    ),
    "tests/test_ffps_assembled_beta_perron_fourier_bridge.py": (
        "c59efdea340a2f47c8f1a0b55c9052e2468f7c6a"
    ),
    "research/l-families/atlas/function_field/FFPS_BANDPASS_ASSEMBLED_PERRON_LEAKAGE.md": (
        "e7959b8788b8a374920aa53bcafd1fb28cda3b72"
    ),
    "research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.py": (
        "52023bb4527a32a2c9983fdd25707da3361242e8"
    ),
    "research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.json": (
        "0031e9ae114d7bf6c60d69789d5d52fe4cf04f6e"
    ),
    "tests/test_ffps_bandpass_assembled_perron_leakage.py": (
        "efc9cde7eef3e833aaa5ac40b5d37b1e34f76770"
    ),
}

EXCEPTIONAL_PRIME = 67
TOY_PRIME = 5
COEFFICIENT_CAP = 625
SCALE_DEPTH_CAP = 12
TOY_CONTRACTION = Fraction(1, 5)


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


def validate_positive_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{label} must be a positive integer")


def mobius(value: int) -> int:
    validate_positive_integer(value, "value")
    remaining = value
    parity = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            parity += 1
            if remaining % prime == 0:
                return 0
        prime += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def beta(value: int, prime: int) -> int:
    validate_positive_integer(value, "value")
    validate_positive_integer(prime, "prime")
    return mobius(value) - (mobius(value // prime) if value % prime == 0 else 0)


def q_free_mobius(value: int, prime: int) -> int:
    validate_positive_integer(value, "value")
    validate_positive_integer(prime, "prime")
    return mobius(value) if value % prime else 0


def shifted_coefficient(
    coefficients: tuple[int, ...], value: int, prime_power: int
) -> int:
    if value % prime_power:
        return 0
    index = value // prime_power
    return coefficients[index] if index < len(coefficients) else 0


def coefficient_identity_panel(prime: int, cap: int) -> dict[str, object]:
    validate_positive_integer(prime, "prime")
    validate_positive_integer(cap, "cap")
    ordinary = tuple(0 if value == 0 else mobius(value) for value in range(cap + 1))
    q_free = tuple(
        0 if value == 0 else q_free_mobius(value, prime) for value in range(cap + 1)
    )
    digest_rows: list[tuple[int, int]] = []
    layer_counts = {"0": 0, "1": 0, "2": 0, "zero": 0}
    for value in range(1, cap + 1):
        direct = beta(value, prime)
        first_difference = ordinary[value] - shifted_coefficient(ordinary, value, prime)
        square_filter = (
            q_free[value]
            - 2 * shifted_coefficient(q_free, value, prime)
            + shifted_coefficient(q_free, value, prime * prime)
        )
        if direct != first_difference or direct != square_filter:
            raise ArithmeticError("duplicate-prime coefficient identity changed")
        if direct:
            exponent = 0
            remaining = value
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            layer_counts[str(exponent)] += 1
        else:
            layer_counts["zero"] += 1
        digest_rows.append((value, direct))
    payload = json.dumps(digest_rows, separators=(",", ":"))
    return {
        "prime": prime,
        "cap": cap,
        "identity": "beta=M-q^(-s)M_(X/q)=(1-q^(-s)S)^2 A_qfree",
        "layer_counts": layer_counts,
        "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
    }


def first_filter(values: tuple[Fraction, ...], omega: Fraction) -> tuple[Fraction, ...]:
    if not values:
        raise ValueError("values must be nonempty")
    return tuple(
        value - omega * (values[index + 1] if index + 1 < len(values) else 0)
        for index, value in enumerate(values)
    )


def second_filter(
    values: tuple[Fraction, ...], omega: Fraction
) -> tuple[Fraction, ...]:
    return first_filter(first_filter(values, omega), omega)


def inverse_first_filter(
    values: tuple[Fraction, ...], omega: Fraction
) -> tuple[Fraction, ...]:
    if not values:
        raise ValueError("values must be nonempty")
    return tuple(
        sum(
            (
                omega**offset * values[index + offset]
                for offset in range(len(values) - index)
            ),
            Fraction(0),
        )
        for index in range(len(values))
    )


def inverse_second_filter(
    values: tuple[Fraction, ...], omega: Fraction
) -> tuple[Fraction, ...]:
    if not values:
        raise ValueError("values must be nonempty")
    return tuple(
        sum(
            (
                (offset + 1) * omega**offset * values[index + offset]
                for offset in range(len(values) - index)
            ),
            Fraction(0),
        )
        for index in range(len(values))
    )


def scale_replay_panel() -> dict[str, object]:
    ordinary = tuple(
        Fraction(((-1) ** index) * (index + 2), index + 1)
        for index in range(SCALE_DEPTH_CAP)
    )
    beta_values = first_filter(ordinary, TOY_CONTRACTION)
    reconstructed = inverse_first_filter(beta_values, TOY_CONTRACTION)
    if reconstructed != ordinary:
        raise ArithmeticError("first scale-filter inverse changed")
    q_free = tuple(
        Fraction((index + 1) * (index + 3), 2 * index + 1)
        for index in range(SCALE_DEPTH_CAP)
    )
    square_filtered = second_filter(q_free, TOY_CONTRACTION)
    square_reconstructed = inverse_second_filter(square_filtered, TOY_CONTRACTION)
    if square_reconstructed != q_free:
        raise ArithmeticError("squared scale-filter inverse changed")
    return {
        "depth": SCALE_DEPTH_CAP,
        "toy_modulus": str(TOY_CONTRACTION),
        "first_inverse": "M_X=sum_(k>=0) omega^k D_(X/q^k)",
        "second_inverse": "A_X=sum_(k>=0)(k+1)omega^k D_(X/q^k)",
        "first_reconstruction": True,
        "second_reconstruction": True,
    }


def squared_norm(values: tuple[Fraction, ...]) -> Fraction:
    return sum((value * value for value in values), Fraction(0))


def block_filter_panel() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    lower_squared = (1 - TOY_CONTRACTION) ** 2
    upper_squared = (1 + TOY_CONTRACTION) ** 2
    for depth in range(2, SCALE_DEPTH_CAP + 1):
        for mode, blocks in (
            ("aligned", (Fraction(1),) * depth),
            ("alternating", tuple(Fraction((-1) ** index) for index in range(depth))),
        ):
            filtered = first_filter(blocks, TOY_CONTRACTION)
            ratio = squared_norm(filtered) / squared_norm(blocks)
            if not lower_squared <= ratio <= upper_squared:
                raise ArithmeticError("block-filter Hilbert bound changed")
            rows.append(
                {
                    "depth": depth,
                    "mode": mode,
                    "energy_ratio": str(ratio),
                }
            )
    return {
        "rows": rows,
        "lower_energy_constant": str(lower_squared),
        "upper_energy_constant": str(upper_squared),
        "asymptotic_sharpness": (
            "aligned and alternating scale modes approach the two constants"
        ),
    }


def perron_panel() -> dict[str, object]:
    lower = 1 - TOY_CONTRACTION
    upper = 1 + TOY_CONTRACTION
    if not 0 < lower < upper:
        raise ArithmeticError("Perron unit interval changed")
    return {
        "half_plane": "Re(w)>=1/2",
        "single_factor": ("1-1/sqrt(67)<=|1-67^(-w)|<=1+1/sqrt(67)"),
        "pair_factor": (
            "(1-1/sqrt(67))^2<=|(1-67^(-w1))(1-67^(-w2))|<=(1+1/sqrt(67))^2"
        ),
        "inverse": "1/(1-67^(-w))=sum_(k>=0)67^(-kw)",
        "toy_lower": str(lower),
        "toy_upper": str(upper),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "scope": (
                "critical-window smoother, assembled Perron bridge, linear "
                "leakage theorem, and successor handoff"
            ),
        },
        "exact_scale_ladder": {
            "ordinary_to_beta": (
                "D_X(t)=M_X(t)-omega_q(t)M_(X/q)(t), omega_q(t)=q^(-1/2-it)"
            ),
            "qfree_to_ordinary": "M_X=A_X-omega_q A_(X/q)",
            "qfree_to_beta": ("D_X=A_X-2omega_q A_(X/q)+omega_q^2 A_(X/q^2)"),
            "ordinary_inverse": ("M_X=sum_(k>=0)omega_q^k D_(X/q^k)"),
            "qfree_inverse": ("A_X=sum_(k>=0)(k+1)omega_q^k D_(X/q^k)"),
            "q67_coefficients": coefficient_identity_panel(
                EXCEPTIONAL_PRIME, COEFFICIENT_CAP
            ),
            "q67_explicit_layers_on_residue_2": [
                beta(2 * EXCEPTIONAL_PRIME**exponent, EXCEPTIONAL_PRIME)
                for exponent in range(4)
            ],
            "toy_coefficients": coefficient_identity_panel(TOY_PRIME, COEFFICIENT_CAP),
            "finite_scale_replay": scale_replay_panel(),
        },
        "weighted_maximal_isomorphism": {
            "measure_scope": "every positive Fourier measure nu",
            "beta_vs_mobius_norm": (
                "(1-q^(-1/2))*M_nu(X)<=D_nu(X)<=(1+q^(-1/2))*M_nu(X)"
            ),
            "beta_vs_qfree_norm": (
                "(1-q^(-1/2))^2*A_nu(X)<=D_nu(X)<=(1+q^(-1/2))^2*A_nu(X)"
            ),
            "maximal_definition": ("F_nu(X)=sup_(1<=Y<=X)||F_Y||_(L2(nu))"),
            "critical_measure": (
                "dnu_X=(1/(2pi))*|Bhat_(r,infinity)(t)|^2"
                "*1_(|t|<=exp(sqrt(log(2)*log(X))))dt"
            ),
            "critical_consequence": (
                "the maximal beta, ordinary-Mobius, and 67-free-Mobius "
                "critical-window X^o targets are equivalent"
            ),
            "asymptotic_gain_from_duplicate_factor": "none beyond q-dependent constants",
        },
        "short_multiplicative_blocks": {
            "ordinary_block": ("U_k=M_(X/q^k)-M_(X/q^(k+1))"),
            "beta_block": ("V_k=D_(X/q^k)-D_(X/q^(k+1))=U_k-omega_q U_(k+1)"),
            "hilbert_bound": (
                "(1-q^(-1/2))^2*sum_k||U_k||^2"
                "<=sum_k||V_k||^2"
                "<=(1+q^(-1/2))^2*sum_k||U_k||^2"
            ),
            "bounded_replay": block_filter_panel(),
        },
        "perron_unit_firewall": perron_panel(),
        "smallest_live_estimate": {
            "name": "MOBIUS-CRIT-BLOCK",
            "statement": (
                "sum_(k<=log_q X) integral_(critical window) "
                "|Bhat(t)|^2|M_(X/q^k)(t)-M_(X/q^(k+1))(t)|^2 dt"
                "=X^o(1)"
            ),
            "status": "OPEN SUFFICIENT TARGET; STRONGER THAN THE ASSEMBLED ENDPOINT",
            "why_live": (
                "Cauchy costs only O(log X)=X^o(1), but the duplicate-67 "
                "filter gives no saving for this block square"
            ),
        },
        "scope": {
            "exact_scale_identities_proved": True,
            "weighted_maximal_isomorphism_proved": True,
            "block_hilbert_isomorphism_proved": True,
            "perron_numerator_zero_or_contraction": False,
            "critical_window_estimate_proved": False,
            "mobius_block_estimate_proved": False,
            "asymptotic_cancellation_proved": False,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "coefficient_cap": COEFFICIENT_CAP,
            "scale_depth": SCALE_DEPTH_CAP,
            "toy_primes": [TOY_PRIME],
            "zeta_zeros": 0,
            "floating_point_operations": 0,
            "large_matrices": 0,
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
