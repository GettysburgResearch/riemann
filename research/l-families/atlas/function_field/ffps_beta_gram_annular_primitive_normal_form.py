#!/usr/bin/env python3
"""Bounded replay for the first-rung annular primitive-pair normal form."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_beta_gram_annular_primitive_normal_form.json"

BASE_SOURCE_COMMIT = "3658d4c31cc866e15d48ab1fc9d8d119136da424"
BASE_SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/FFPS_ZERO_FREE_BETA_ENERGY_LADDER.md"
    ): "bd4cbb842e78c1dad5d380c8d20ff14c39bba15e",
    (
        "research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py"
    ): "df80000192292cc5fc1cd08013f152fb257054f9",
    (
        "research/l-families/atlas/function_field/"
        "ffps_zero_free_beta_energy_ladder.json"
    ): "7e8889aa0dd1b01674e20158a52502cff0d8dffa",
    "tests/test_ffps_zero_free_beta_energy_ladder.py": (
        "983a1320f89087028f6724fe36aaca5ca1309b15"
    ),
}
GEOMETRY_SOURCE_COMMIT = "731398930c02cdc871259656dac2e2a4e6569e37"
GEOMETRY_SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/FFPS_BETA_GRAM_SIGN_GEOMETRY.md"
    ): "bbdcb30dadb529cafad27abe6d6c9510d1c9b7d4",
    (
        "research/l-families/atlas/function_field/ffps_beta_gram_sign_geometry.py"
    ): "750b77d8864c8f1a69c3e7144dc926b9b0477dd9",
    (
        "research/l-families/atlas/function_field/ffps_beta_gram_sign_geometry.json"
    ): "00961f89cf3d74e364b89999a74b85e1f49018b8",
    "tests/test_ffps_beta_gram_sign_geometry.py": (
        "e486cca99bb4aaa4b61878e754c6b989d0f18d73"
    ),
}

EXCEPTIONAL_PRIME = 67
EXCEPTIONAL_COEFFICIENTS = (1, -2, 1)
EXCEPTIONAL_RADIAL_PROFILES = {
    0: (1, 4, 1),
    1: (1, 1),
    2: (1,),
}
REPLAY_SOURCE_CAP = 72
REPLAY_PRIMITIVE_CAP = 28
PHYSICAL_CHANNEL_CAP = 30
SIMPSON_PANELS_PER_PIECE = 256
MAX_SIMPSON_PANELS_PER_PIECE = 1024
WITNESS_PAIRS = (
    ((2, 3), "central", 1, 1),
    ((5, 6), "central", -1, -1),
    ((1, 3), "outer", -1, 1),
    ((2, 7), "outer", 1, -1),
)


def check_source_blobs() -> None:
    """Check the frozen base and sign-geometry quartets."""
    for path, expected in BASE_SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{BASE_SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen base blob mismatch: {path}")
    for path, expected in GEOMETRY_SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{GEOMETRY_SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen geometry blob mismatch: {path}")


def validate_positive_integer(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")


def mobius(value: int) -> int:
    validate_positive_integer(value)
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


def beta(value: int) -> int:
    validate_positive_integer(value)
    return mobius(value) - (
        mobius(value // EXCEPTIONAL_PRIME) if value % EXCEPTIONAL_PRIME == 0 else 0
    )


def exceptional_valuation(value: int) -> int:
    validate_positive_integer(value)
    exponent = 0
    residue = value
    while residue % EXCEPTIONAL_PRIME == 0:
        exponent += 1
        residue //= EXCEPTIONAL_PRIME
    return exponent


def squarefree_harmonic(bound: int, forbidden: int) -> Fraction:
    """Return sum mu(h)^2/h over h<=bound coprime to forbidden."""
    if isinstance(bound, bool) or not isinstance(bound, int) or bound < 0:
        raise ValueError("bound must be a nonnegative integer")
    validate_positive_integer(forbidden)
    return sum(
        (
            Fraction(1, value)
            for value in range(1, bound + 1)
            if mobius(value) != 0 and math.gcd(value, forbidden) == 1
        ),
        Fraction(0),
    )


def validate_primitive_pair(left: int, right: int) -> None:
    validate_positive_integer(left)
    validate_positive_integer(right)
    if math.gcd(left, right) != 1:
        raise ValueError("primitive coordinates must be coprime")


def direct_radial_coefficient(left: int, right: int, bound: int) -> Fraction:
    """Return sum_(g<=bound) beta(gr)beta(gs)/g directly."""
    validate_primitive_pair(left, right)
    if isinstance(bound, bool) or not isinstance(bound, int) or bound < 0:
        raise ValueError("bound must be a nonnegative integer")
    return sum(
        (
            Fraction(beta(common * left) * beta(common * right), common)
            for common in range(1, bound + 1)
        ),
        Fraction(0),
    )


def closed_radial_coefficient(left: int, right: int, bound: int) -> Fraction:
    """Return the exact positive-amplitude exceptional profile on one ray."""
    validate_primitive_pair(left, right)
    if isinstance(bound, bool) or not isinstance(bound, int) or bound < 0:
        raise ValueError("bound must be a nonnegative integer")
    primitive_product = beta(left) * beta(right)
    if primitive_product == 0 or bound == 0:
        return Fraction(0)
    exceptional_exponent = exceptional_valuation(left * right)
    if exceptional_exponent not in EXCEPTIONAL_RADIAL_PROFILES:
        return Fraction(0)
    forbidden = EXCEPTIONAL_PRIME * left * right
    amplitude = sum(
        (
            Fraction(coefficient, EXCEPTIONAL_PRIME**exponent)
            * squarefree_harmonic(bound // (EXCEPTIONAL_PRIME**exponent), forbidden)
            for exponent, coefficient in enumerate(
                EXCEPTIONAL_RADIAL_PROFILES[exceptional_exponent]
            )
        ),
        Fraction(0),
    )
    return primitive_product * amplitude


def inverse_square_root_basis(value: int) -> tuple[int, Fraction]:
    """Return k,q such that 1/sqrt(value)=q/sqrt(k), with k squarefree."""
    validate_positive_integer(value)
    remaining = value
    square = 1
    squarefree = 1
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        square *= prime ** (exponent // 2)
        if exponent % 2:
            squarefree *= prime
        prime += 1
    if remaining > 1:
        squarefree *= remaining
    return squarefree, Fraction(1, square)


def scale_invariant_toy_kernel(left: int, right: int) -> Fraction:
    """An exact signed compact-ratio toy; not the physical kernel."""
    validate_positive_integer(left)
    validate_positive_integer(right)
    common = math.gcd(left, right)
    reduced_left = left // common
    reduced_right = right // common
    low = min(reduced_left, reduced_right)
    high = max(reduced_left, reduced_right)
    if high > 4 * low:
        return Fraction(0)
    magnitude = Fraction(1, reduced_left + reduced_right)
    return 2 * magnitude if 2 * high <= 3 * low else -magnitude


def _add_radical_term(
    accumulator: dict[int, Fraction], radicand: int, coefficient: Fraction
) -> None:
    accumulator[radicand] = accumulator.get(radicand, Fraction(0)) + coefficient
    if accumulator[radicand] == 0:
        del accumulator[radicand]


def direct_toy_prefix(cap: int = REPLAY_SOURCE_CAP) -> dict[int, Fraction]:
    """Evaluate the source pair sum in an exact square-root basis."""
    validate_positive_integer(cap)
    result: dict[int, Fraction] = {}
    for left in range(1, cap + 1):
        left_beta = beta(left)
        if left_beta == 0:
            continue
        for right in range(1, cap + 1):
            right_beta = beta(right)
            if right_beta == 0:
                continue
            kernel = scale_invariant_toy_kernel(left, right)
            if kernel == 0:
                continue
            radicand, scale = inverse_square_root_basis(left * right)
            _add_radical_term(
                result,
                radicand,
                Fraction(left_beta * right_beta) * kernel * scale,
            )
    return result


def primitive_toy_prefix(cap: int = REPLAY_SOURCE_CAP) -> dict[int, Fraction]:
    """Evaluate the same toy sum through primitive rays and radial sums."""
    validate_positive_integer(cap)
    result: dict[int, Fraction] = {}
    for left in range(1, cap + 1):
        for right in range(1, cap + 1):
            if math.gcd(left, right) != 1:
                continue
            radial_bound = cap // max(left, right)
            radial = closed_radial_coefficient(left, right, radial_bound)
            if radial == 0:
                continue
            kernel = scale_invariant_toy_kernel(left, right)
            if kernel == 0:
                continue
            radicand, scale = inverse_square_root_basis(left * right)
            _add_radical_term(result, radicand, radial * kernel * scale)
    return result


def mass() -> float:
    return 4.0 * math.sinh(0.5) ** 2


def physical_correlation(shift: float) -> float:
    """Display evaluation of the pinned exact first-rung formula."""
    if isinstance(shift, bool) or not isinstance(shift, (int, float)):
        raise TypeError("shift must be a finite real number")
    value = float(shift)
    if not math.isfinite(value):
        raise ValueError("shift must be a finite real number")
    radius = abs(value)
    if radius <= 1.0:
        raw = 0.25 * (
            (math.exp(2.0) + 4.0 - (math.exp(2.0) + 2.0) * radius) * math.exp(-radius)
            - (2.0 * radius + math.exp(-2.0) * (radius + 1.0)) * math.exp(radius)
        )
    elif radius <= 2.0:
        tail = 2.0 - radius
        raw = -0.5 * (math.sinh(tail) + tail * math.cosh(tail))
    else:
        return 0.0
    return raw / mass() ** 2


def witness_row(
    pair: tuple[int, int],
    expected_annulus: str,
    expected_beta_phase: int,
    expected_contribution_sign: int,
) -> dict[str, object]:
    left, right = pair
    validate_primitive_pair(left, right)
    radius = abs(math.log(left / right))
    kernel_value = physical_correlation(radius)
    annulus = "central" if kernel_value > 0 else "outer"
    beta_product = beta(left) * beta(right)
    beta_phase = 1 if beta_product > 0 else -1
    contribution_sign = 1 if beta_product * kernel_value > 0 else -1
    if (
        annulus != expected_annulus
        or beta_phase != expected_beta_phase
        or contribution_sign != expected_contribution_sign
    ):
        raise ArithmeticError("primitive annular witness drifted")
    return {
        "pair": [left, right],
        "ratio": f"{max(left, right)}/{min(left, right)}",
        "log_radius_display": radius,
        "annulus": annulus,
        "beta_product": beta_product,
        "kernel_sign": 1 if kernel_value > 0 else -1,
        "ray_contribution_sign": contribution_sign,
    }


def direct_physical_energy(cap: int) -> float:
    """Bounded display evaluation of the literal physical prefix energy."""
    validate_positive_integer(cap)
    total = 0.0
    for left in range(1, cap + 1):
        left_beta = beta(left)
        if left_beta == 0:
            continue
        for right in range(1, cap + 1):
            right_beta = beta(right)
            if right_beta == 0:
                continue
            total += (
                left_beta
                * right_beta
                * physical_correlation(math.log(left / right))
                / math.sqrt(left * right)
            )
    return total


def physical_channel_totals(cap: int) -> dict[str, float]:
    """Bounded display evaluation of D,C+/-,O+/- in primitive coordinates."""
    validate_positive_integer(cap)
    channels = {
        "D": physical_correlation(0.0) * float(closed_radial_coefficient(1, 1, cap)),
        "C_plus": 0.0,
        "C_minus": 0.0,
        "O_plus": 0.0,
        "O_minus": 0.0,
    }
    for left in range(1, cap + 1):
        for right in range(left + 1, cap + 1):
            if math.gcd(left, right) != 1:
                continue
            beta_product = beta(left) * beta(right)
            if beta_product == 0:
                continue
            radial = closed_radial_coefficient(left, right, cap // right)
            kernel = physical_correlation(math.log(right / left))
            if kernel == 0.0:
                continue
            magnitude = abs(float(radial) * kernel / math.sqrt(left * right))
            phase = "plus" if beta_product > 0 else "minus"
            annulus = "C" if kernel > 0 else "O"
            channels[f"{annulus}_{phase}"] += magnitude
    channels["assembled"] = channels["D"] + 2.0 * (
        channels["C_plus"]
        - channels["C_minus"]
        - channels["O_plus"]
        + channels["O_minus"]
    )
    return channels


def off_diagonal_eigenvalues(value: Fraction) -> tuple[Fraction, Fraction]:
    if isinstance(value, bool) or not isinstance(value, Fraction):
        raise TypeError("off-diagonal value must be a Fraction")
    if value == 0:
        raise ValueError("off-diagonal value must be nonzero")
    magnitude = abs(value)
    return -magnitude, magnitude


def _simpson_piece(power: int, start: float, end: float, panels: int) -> float:
    width = (end - start) / panels

    def integrand(point: float) -> float:
        return point**power * physical_correlation(point)

    total = integrand(start) + integrand(end)
    total += 4.0 * sum(
        integrand(start + index * width) for index in range(1, panels, 2)
    )
    total += 2.0 * sum(
        integrand(start + index * width) for index in range(2, panels, 2)
    )
    return width * total / 3.0


def half_moment(power: int, panels: int = SIMPSON_PANELS_PER_PIECE) -> float:
    if isinstance(power, bool) or not isinstance(power, int) or not 0 <= power <= 2:
        raise ValueError("power must lie in [0,2]")
    if (
        isinstance(panels, bool)
        or not isinstance(panels, int)
        or panels < 2
        or panels > MAX_SIMPSON_PANELS_PER_PIECE
        or panels % 2
    ):
        raise ValueError("panels must be even and lie in [2,1024]")
    return _simpson_piece(power, 0.0, 1.0, panels) + _simpson_piece(
        power, 1.0, 2.0, panels
    )


def canonical_digest(vector: dict[int, Fraction]) -> str:
    payload = "|".join(
        f"{radicand}:{coefficient.numerator}/{coefficient.denominator}"
        for radicand, coefficient in sorted(vector.items())
    )
    return hashlib.sha256(payload.encode()).hexdigest()


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    if tuple(beta(EXCEPTIONAL_PRIME**exponent) for exponent in range(5)) != (
        1,
        -2,
        1,
        0,
        0,
    ):
        raise ArithmeticError("exceptional beta profile drifted")

    radial_checks = 0
    bounds = (0, 1, 5, 70, 140)
    for left in range(1, REPLAY_PRIMITIVE_CAP + 1):
        for right in range(1, REPLAY_PRIMITIVE_CAP + 1):
            if math.gcd(left, right) != 1:
                continue
            for bound in bounds:
                if direct_radial_coefficient(
                    left, right, bound
                ) != closed_radial_coefficient(left, right, bound):
                    raise ArithmeticError("primitive radial formula failed")
                radial_checks += 1
    for left, right in (
        (EXCEPTIONAL_PRIME, 1),
        (EXCEPTIONAL_PRIME**2, 1),
        (EXCEPTIONAL_PRIME, 2),
    ):
        for bound in bounds:
            if direct_radial_coefficient(
                left, right, bound
            ) != closed_radial_coefficient(left, right, bound):
                raise ArithmeticError("exceptional primitive radial formula failed")
            radial_checks += 1

    direct_vector = direct_toy_prefix()
    primitive_vector = primitive_toy_prefix()
    if direct_vector != primitive_vector:
        raise ArithmeticError("primitive-ray normal form failed exact toy replay")

    witness_rows = [witness_row(*row) for row in WITNESS_PAIRS]
    physical_channels = physical_channel_totals(PHYSICAL_CHANNEL_CAP)
    direct_physical = direct_physical_energy(PHYSICAL_CHANNEL_CAP)
    physical_residual = abs(physical_channels["assembled"] - direct_physical)
    if physical_residual > 2e-12:
        raise ArithmeticError("physical four-channel assembly drifted")
    negative_eigenvalue, positive_eigenvalue = off_diagonal_eigenvalues(Fraction(3, 5))

    half_zero = half_moment(0)
    half_first = half_moment(1)
    half_second = half_moment(2)
    exact_half_first = (2.0 - math.sinh(2.0)) / (32.0 * math.sinh(0.5) ** 4)
    if abs(half_zero) > 2e-12:
        raise ArithmeticError("half zeroth moment drifted")
    if not math.isclose(half_first, exact_half_first, rel_tol=0.0, abs_tol=4e-11):
        raise ArithmeticError("half first moment drifted")
    if not math.isclose(half_second, -1.0, rel_tol=0.0, abs_tol=2e-12):
        raise ArithmeticError("half second moment drifted")

    return {
        "source_contract": {
            "frozen_base_commit": BASE_SOURCE_COMMIT,
            "frozen_base_blobs": BASE_SOURCE_BLOBS,
            "frozen_geometry_commit": GEOMETRY_SOURCE_COMMIT,
            "frozen_geometry_blobs": GEOMETRY_SOURCE_BLOBS,
        },
        "primitive_normal_form": {
            "source": "beta(n)=mu(n)-1_(67|n)mu(n/67)",
            "ray_coordinates": "m=gr, n=gs, gcd(r,s)=1",
            "radial_coefficient": ("A_(r,s)(Y)=sum_(g<=Y) beta(gr)beta(gs)/g"),
            "energy": (
                "E_1(X)=sum_(gcd(r,s)=1) R(log(r/s))/sqrt(rs) "
                "A_(r,s)(floor(X/max(r,s)))"
            ),
            "exceptional_profiles": {
                "alpha_0": [1, 4, 1],
                "alpha_1": [1, 1],
                "alpha_2": [1],
            },
            "ray_sign": (
                "for every active ray and Y>=1, sign A_(r,s)(Y)=sign(beta(r)beta(s))"
            ),
            "diagonal": ("D(X)=R(0)A_(1,1)(X), the unique primitive diagonal ray"),
        },
        "four_channel_annular_form": {
            "central": "1<rho=max(r/s,s/r)<e^xi, R(log rho)>0",
            "outer": "e^xi<rho<e^2, R(log rho)<0",
            "channels": {
                "C_plus": "central rays with beta(r)beta(s)>0",
                "C_minus": "central rays with beta(r)beta(s)<0",
                "O_plus": "outer rays with beta(r)beta(s)>0",
                "O_minus": "outer rays with beta(r)beta(s)<0",
            },
            "identity": "E_1=D+2(C_+-C_--O_++O_-)",
            "positive_mass": "P=C_++O_-",
            "negative_mass": "N=C_-+O_+",
            "assembled_identity": "E_1=D+2(P-N)",
            "unconditional_gram_inequality": "N<P+D/2 for every integer X>=1",
            "trivial_absolute_cap": "P+N<=4e R(0)X",
            "rh_equivalent_open_gate": "RH iff |P(X)-N(X)|=X^o(1)",
        },
        "continuous_shell_constraints": {
            "log_Haar_balance": (
                "integral_1^e R(log rho)drho/rho=sinh(1)/(2M^2), "
                "integral_e^(e^2)=-sinh(1)/(2M^2)"
            ),
            "central_outer_mass_balance": (
                "integral_1^(e^xi) R(log rho)drho/rho="
                "-integral_(e^xi)^(e^2) R(log rho)drho/rho>0"
            ),
            "log_first_moment": (
                "integral_1^(e^2) log(rho)R(log rho)drho/rho="
                "(2-sinh(2))/(32sinh^4(1/2))"
            ),
            "log_second_moment": ("integral_1^(e^2) log(rho)^2R(log rho)drho/rho=-1"),
            "arithmetic_firewall": (
                "these are log-Haar identities; the primitive energy pairs R "
                "with a signed atomic arithmetic measure, so no discrete "
                "annular cancellation follows"
            ),
        },
        "positivity_no_go": {
            "off_diagonal_two_point_spectrum": [
                str(negative_eigenvalue),
                str(positive_eigenvalue),
            ],
            "conclusion": (
                "every nonzero isolated annular edge gives an indefinite "
                "off-diagonal quadratic form"
            ),
            "actual_beta_ray_witnesses": witness_rows,
            "scope": (
                "refutes termwise and geometry-only annular positivity; does not "
                "decide the sign or size of either complete beta prefix annulus"
            ),
        },
        "bounded_replay": {
            "radial_formula_checks": radial_checks,
            "toy_source_cap": REPLAY_SOURCE_CAP,
            "toy_radical_coordinates": len(direct_vector),
            "toy_normal_form_digest": canonical_digest(direct_vector),
            "physical_witness_pairs": len(witness_rows),
            "physical_channel_cap": PHYSICAL_CHANNEL_CAP,
            "physical_channel_displays": {
                key: format(value, ".12e") for key, value in physical_channels.items()
            },
            "physical_direct_energy_display": format(direct_physical, ".12e"),
            "physical_channel_residual": format(physical_residual, ".3e"),
            "simpson_panels_per_piece": SIMPSON_PANELS_PER_PIECE,
            "display_half_moments": {
                "zeroth": format(half_zero, ".12e"),
                "first": format(half_first, ".12e"),
                "second": format(half_second, ".12e"),
            },
        },
        "proof_ledger": {
            "primitive_gcd_ray_reindexing": "PROVED EXACT",
            "exceptional_radial_profiles_and_fixed_ray_sign": "PROVED EXACT",
            "four_channel_annular_identity": "PROVED EXACT",
            "continuous_shell_and_moment_constraints": "PROVED EXACT",
            "assembled_gram_inequality": "PROVED EXACT",
            "termwise_or_geometry_only_annular_positivity": "REFUTED EXACTLY",
            "rh_equivalent_annular_cancellation_gate": (
                "PROVED EQUIVALENT / ESTIMATE OPEN"
            ),
            "central_or_outer_complete_prefix_sign": "NOT DETERMINED",
            "any_subpower_annular_cancellation": "NOT PROVED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "radial_primitive_coordinate_cap": REPLAY_PRIMITIVE_CAP,
            "radial_bound_samples": len(bounds),
            "exact_toy_source_cap": REPLAY_SOURCE_CAP,
            "physical_channel_cap": PHYSICAL_CHANNEL_CAP,
            "physical_witness_pairs": len(witness_rows),
            "simpson_panels_per_piece": SIMPSON_PANELS_PER_PIECE,
            "zeta_zeros": 0,
            "prime_interval_queries": 0,
            "curves": 0,
            "random_samples": 0,
        },
    }


def canonical_text(result: dict[str, object]) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = canonical_text(run(check_sources=not args.no_source_check))
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    elif args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            raise RuntimeError("canonical JSON drift")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
