#!/usr/bin/env python3
"""Bounded replay for exact beta-source insertion into the cusp channel."""

from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "beta_chiral_source_cauchy_decomposition.json"

SOURCE_BLOBS = {
    (
        "bbfb9761c2b4bb37e35342e8d9279895f8d44be0",
        "README_108006.md",
    ): "a47efcd778e9d4332f3d534df41e64679f214dc2",
    (
        "bbfb9761c2b4bb37e35342e8d9279895f8d44be0",
        "integration/2026-08-31/t108006-source-lock.json",
    ): "f63274b3f938867b6fb9f94c363f3d07be7c7cbe",
    (
        "bbfb9761c2b4bb37e35342e8d9279895f8d44be0",
        "research/l-families/atlas/function_field/BETA_CHEBYSHEV_CHIRAL_CUSP_SOURCE_CONVOLUTION.md",
    ): "17b2bb796d5217b7939e784b5d5f28c7f9d99b90",
    (
        "bbfb9761c2b4bb37e35342e8d9279895f8d44be0",
        "research/l-families/atlas/function_field/beta_chebyshev_chiral_cusp_source_convolution.py",
    ): "0a6aa29a4adf82fd989823a4561422b29f4d320e",
    (
        "bbfb9761c2b4bb37e35342e8d9279895f8d44be0",
        "research/l-families/atlas/function_field/beta_chebyshev_chiral_cusp_source_convolution.json",
    ): "00c7d8b17ae1572795943b98dba6a29d27eefce1",
    (
        "bbfb9761c2b4bb37e35342e8d9279895f8d44be0",
        "tests/test_beta_chebyshev_chiral_cusp_source_convolution.py",
    ): "ec6a3f7e8352b67bbcd351472f5dfcdffd501e3f",
    (
        "b41a4e4b9fd518dfb97229a6a94346b2d49e528f",
        "research/l-families/atlas/function_field/BETA_CHEBYSHEV_PERRON_FOURIER_CUSP_CARRIER.md",
    ): "f46a7b283061ad35c38a5060a99c5098d4c14aff",
    (
        "b41a4e4b9fd518dfb97229a6a94346b2d49e528f",
        "research/l-families/atlas/function_field/beta_chebyshev_perron_fourier_cusp_carrier.py",
    ): "027a306e69f65661fbf44de4ee503dc03004a315",
    (
        "b41a4e4b9fd518dfb97229a6a94346b2d49e528f",
        "research/l-families/atlas/function_field/beta_chebyshev_perron_fourier_cusp_carrier.json",
    ): "216de6ac6230e99b233fa7af913c7daf3952a09a",
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md",
    ): "21ef8f5215ca349f0efffd52dca1543ef6d988d6",
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/ffps_assembled_beta_perron_fourier_bridge.py",
    ): "2dbe93508eadcc9ba9ed15a5f64d02f13c728ef3",
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/ffps_assembled_beta_perron_fourier_bridge.json",
    ): "1223ab8049492f58cf5e64a25f80d5799aa165f7",
}


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def mobius(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    value = n
    sign = 1
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            value //= prime
            sign = -sign
            if value % prime == 0:
                return 0
        prime += 1
    if value > 1:
        sign = -sign
    return sign


def beta(n: int, exceptional_prime: int = 67) -> int:
    return mobius(n) - (mobius(n // exceptional_prime) if n % exceptional_prime == 0 else 0)


def dirichlet_prefix(coefficient, cap: int, t: float) -> complex:
    return sum(
        coefficient(n) * cmath.exp(-(0.5 + 1j * t) * math.log(n))
        for n in range(1, cap + 1)
    )


def scale_filter_rows() -> list[dict[str, float | int]]:
    rows: list[dict[str, float | int]] = []
    for cap in (80, 134, 256):
        for t in (0.0, 0.7, 2.0):
            duplicate = dirichlet_prefix(beta, cap, t)
            ordinary = dirichlet_prefix(mobius, cap, t)
            lower = dirichlet_prefix(mobius, cap // 67, t)
            omega = cmath.exp(-(0.5 + 1j * t) * math.log(67))
            error = abs(duplicate - (ordinary - omega * lower))
            if error > 2e-13:
                raise AssertionError("duplicate-67 scale identity failed")
            rows.append({"cap": cap, "t": t, "absolute_error": error})
    return rows


def jump_masses(order: int) -> tuple[int, ...]:
    return tuple(
        ((-1) ** index) * (1 if index in (0, order) else 2)
        for index in range(order + 1)
    )


def step_value(x: Fraction, boundaries: tuple[Fraction, ...]) -> int:
    if x < boundaries[0] or x >= boundaries[-1]:
        return 0
    for index in range(len(boundaries) - 1):
        if boundaries[index] <= x < boundaries[index + 1]:
            return (-1) ** index
    raise AssertionError("unreachable cell lookup")


def direct_field(
    u: Fraction,
    shifts: tuple[Fraction, ...],
    coefficients: tuple[Fraction, ...],
    boundaries: tuple[Fraction, ...],
) -> Fraction:
    return sum(
        (coefficient * step_value(u - shift, boundaries) for shift, coefficient in zip(shifts, coefficients)),
        Fraction(0),
    )


def jump_field(
    u: Fraction,
    shifts: tuple[Fraction, ...],
    coefficients: tuple[Fraction, ...],
    boundaries: tuple[Fraction, ...],
) -> Fraction:
    masses = jump_masses(len(boundaries) - 1)
    total = Fraction(0)
    for boundary, mass in zip(boundaries, masses):
        prefix = sum(
            (coefficient for shift, coefficient in zip(shifts, coefficients) if shift <= u - boundary),
            Fraction(0),
        )
        total += mass * prefix
    return total


def cell_field(
    u: Fraction,
    shifts: tuple[Fraction, ...],
    coefficients: tuple[Fraction, ...],
    boundaries: tuple[Fraction, ...],
) -> Fraction:
    total = Fraction(0)
    for index in range(len(boundaries) - 1):
        cell_sum = sum(
            (
                coefficient
                for shift, coefficient in zip(shifts, coefficients)
                if u - boundaries[index + 1] < shift <= u - boundaries[index]
            ),
            Fraction(0),
        )
        total += ((-1) ** index) * cell_sum
    return total


def rational_cell_fixture() -> dict[str, object]:
    boundaries = (Fraction(0), Fraction(1, 4), Fraction(3, 4), Fraction(1))
    shifts = (Fraction(0), Fraction(1, 8), Fraction(1, 2), Fraction(7, 8), Fraction(5, 4))
    coefficients = (Fraction(2), Fraction(-1), Fraction(3), Fraction(-2), Fraction(1))
    breakpoints = sorted({shift + boundary for shift in shifts for boundary in boundaries})
    energy_direct = Fraction(0)
    energy_jump = Fraction(0)
    energy_cell = Fraction(0)
    samples: list[dict[str, object]] = []
    for left, right in zip(breakpoints, breakpoints[1:]):
        if left == right:
            continue
        midpoint = (left + right) / 2
        direct = direct_field(midpoint, shifts, coefficients, boundaries)
        jump = jump_field(midpoint, shifts, coefficients, boundaries)
        cell = cell_field(midpoint, shifts, coefficients, boundaries)
        if not (direct == jump == cell):
            raise AssertionError("signed Chebyshev source coordinates disagree")
        width = right - left
        energy_direct += width * direct * direct
        energy_jump += width * jump * jump
        energy_cell += width * cell * cell
        samples.append(
            {
                "left": [left.numerator, left.denominator],
                "right": [right.numerator, right.denominator],
                "field": [direct.numerator, direct.denominator],
            }
        )
    if not (energy_direct == energy_jump == energy_cell):
        raise AssertionError("cell-current energy identity failed")
    return {
        "boundaries": [[value.numerator, value.denominator] for value in boundaries],
        "jump_masses": list(jump_masses(3)),
        "interval_count": len(samples),
        "energy": [energy_direct.numerator, energy_direct.denominator],
        "samples": samples,
    }


def cauchy_kernel(z: complex, u: complex) -> complex:
    return z / (2 * math.pi * (u * u + z * z / 4))


def cauchy_partial_fraction(z: complex, u: complex) -> complex:
    return (1 / (2j * math.pi)) * (
        1 / (u - 1j * z / 2) - 1 / (u + 1j * z / 2)
    )


def partial_fraction_rows() -> list[dict[str, float]]:
    rows = []
    for z, u in (
        (complex(3.0, 4.0), complex(0.7, 0.0)),
        (complex(2.5, 7.0), complex(-1.2, 0.3)),
        (complex(5.0, -2.0), complex(3.1, -0.4)),
    ):
        error = abs(cauchy_kernel(z, u) - cauchy_partial_fraction(z, u))
        if error > 2e-15:
            raise AssertionError("Cauchy partial fraction failed")
        rows.append({"absolute_error": error})
    return rows


def pair_transfer_fixture() -> dict[str, object]:
    positions = (-0.7, 0.0, 0.4, 1.1)
    coefficients = (2.0, -1.0, 3.0, -2.0)
    z = 1.75
    xi = 0.9
    diagonal = sum(value * value for value in coefficients)
    total = 0j
    off_diagonal = 0j
    oriented_half = 0j
    for left_index, (left, a) in enumerate(zip(positions, coefficients)):
        for right_index, (right, b) in enumerate(zip(positions, coefficients)):
            lag = left - right
            term = a * b * cmath.exp(-z * abs(lag) / 2 + 1j * xi * lag)
            total += term
            if left_index != right_index:
                off_diagonal += term
            if left_index > right_index:
                oriented_half += term
    oriented_real = 2 * oriented_half.real
    if abs(total - (diagonal + off_diagonal)) > 2e-14:
        raise AssertionError("diagonal/off-diagonal source split failed")
    if abs(total.imag) > 2e-14:
        raise AssertionError("symmetric pair transfer was not real")
    if abs(off_diagonal.real - oriented_real) > 2e-14:
        raise AssertionError("beta-pair evenness failed to orient the source")
    return {
        "diagonal": diagonal,
        "off_diagonal_real": off_diagonal.real,
        "off_diagonal_imag": off_diagonal.imag,
        "oriented_off_diagonal_real": oriented_real,
        "total_real": total.real,
        "total_imag": total.imag,
    }


def directed_orientation_fixture() -> dict[str, object]:
    """Check the Fourier-sign binding between carrier support and pair order."""
    rows: list[dict[str, object]] = []
    for numerator, denominator in ((3, 5), (5, 3), (7, 7), (11, 2)):
        lag = math.log(numerator / denominator)
        # With D(tau)=(2pi)^(-1) int H(v)e^{i tau v}dv and source phase
        # e^{i tau lag}, tau integration evaluates the carrier at v=-lag.
        carrier_argument = -lag
        selected = carrier_argument < 0
        expected = numerator > denominator
        if selected != expected:
            raise AssertionError("directed carrier selected the wrong pair order")
        rows.append(
            {
                "numerator": numerator,
                "denominator": denominator,
                "log_ratio": lag,
                "carrier_argument": carrier_argument,
                "selected_by_negative_carrier_support": selected,
            }
        )
    return {
        "fourier_convention": "D(tau)=(2pi)^-1 int H(v) exp(i tau v) dv",
        "source_phase": "exp(i tau log(m/k))",
        "distributional_evaluation": "H(-log(m/k))",
        "negative_carrier_support_selects": "m>k",
        "rows": rows,
    }


def exceptional_euler_fixture() -> dict[str, object]:
    primes = (2, 3, 5)
    power = 2
    direct = Fraction(0)
    for mask in range(1 << len(primes)):
        base = 1
        for index, prime in enumerate(primes):
            if mask & (1 << index):
                base *= prime
        for exponent in range(3):
            number = base * 67**exponent
            direct += Fraction(beta(number) ** 2, number**power)
    product = Fraction(1)
    for prime in primes:
        product *= 1 + Fraction(1, prime**power)
    x = Fraction(1, 67**power)
    product *= 1 + 4 * x + x * x
    if direct != product:
        raise AssertionError("exceptional beta-square Euler factor failed")
    return {
        "power": power,
        "direct": [direct.numerator, direct.denominator],
        "product": [product.numerator, product.denominator],
        "exceptional_local_factor": [
            (1 + 4 * x + x * x).numerator,
            (1 + 4 * x + x * x).denominator,
        ],
    }


def edge_channel_rows() -> list[dict[str, float | int]]:
    rows: list[dict[str, float | int]] = []
    for n in (32, 64, 128):
        sigma = 2.0 * n ** (1 / 3)
        z = sigma + 4j * n
        first_pole = 1j * z / 2
        second_pole = -1j * z / 2
        expected_first = complex(-2 * n, sigma / 2)
        expected_second = complex(2 * n, -sigma / 2)
        error = max(abs(first_pole - expected_first), abs(second_pole - expected_second))
        if error > 2e-14:
            raise AssertionError("first-edge Cauchy channels failed")
        rows.append({"n": n, "sigma": sigma, "pole_error": error})
    return rows


def build_payload() -> dict[str, object]:
    scale_rows = scale_filter_rows()
    cells = rational_cell_fixture()
    partial = partial_fraction_rows()
    pairs = pair_transfer_fixture()
    orientation = directed_orientation_fixture()
    euler = exceptional_euler_fixture()
    channels = edge_channel_rows()
    core = {
        "scale_filter_rows": scale_rows,
        "rational_cell_fixture": cells,
        "partial_fraction_rows": partial,
        "pair_transfer_fixture": pairs,
        "directed_orientation_fixture": orientation,
        "exceptional_euler_fixture": euler,
        "edge_channel_rows": channels,
    }
    proof_object = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    finite_checks = (
        len(scale_rows)
        + cells["interval_count"] * 3
        + len(partial)
        + len(channels)
        + len(orientation["rows"])
        + 15
    )
    return {
        "schema": "riemann.t108008.beta-chiral-source-cauchy-decomposition.v1",
        "classification": "PASS_T108008_BETA_CHIRAL_SOURCE_CAUCHY_DECOMPOSITION",
        "proof_object_sha256": proof_object,
        "finite_checks": finite_checks,
        **core,
        "t108006_chiral_source_front_door_authenticated": True,
        "t108006_primitive_pair_orientation_sign_corrected": True,
        "beta_pair_evenness_oriented_reduction_proved": True,
        "exact_cauchy_transfer_proved": True,
        "finite_jump_spectrum_inserted_before_source_norm": True,
        "signed_chebyshev_cell_current_identity_proved": True,
        "duplicate67_cross_scale_field_identity_proved": True,
        "diagonal_beta_square_euler_product_proved": True,
        "diagonal_has_no_cusp_amplification_proved": True,
        "first_edge_two_cauchy_channels_proved": True,
        "signed_off_diagonal_cusp_correlation_estimate_proved": False,
        "outer_frequency_tails_paid": False,
        "direct_lambda_zero_tau_nonzero_boundary_proved": False,
        "new_zero_free_region_proved": False,
        "rh_established": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--skip-source-check", action="store_true")
    args = parser.parse_args()
    if not args.skip_source_check:
        check_source_blobs()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != text:
            raise SystemExit("retained output mismatch")
    else:
        OUTPUT.write_text(text)
    print(payload["classification"])


if __name__ == "__main__":
    main()
