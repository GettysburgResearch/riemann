#!/usr/bin/env python3
"""Bounded exact replay for the high-gcd principal-frequency identity."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_HIGH_GCD_PRINCIPAL_FREQUENCY_IDENTITY.md"
SOURCE_COMMIT = "5122e939df2fa322b5a3185cf1d78d4b402f3d5f"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md"
    ): "bf4d1baa231086ba7e8eafaecd39730d83c9201a",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_HIGH_GCD_FAR_GAP_LOCALIZATION.md"
    ): "72a4dbf21f452041c939c2c308716abfd49195a9",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_DIVISOR_WAVE_SHIFTED_ZETA_FACTORIZATION.md"
    ): "21ef6a6e0078beb85f81fc880e5f161fc6288a8f",
}
REPLAY_CAP = 42


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        frozen = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if frozen != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def check_scope_markers() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "nonzero boundary mean",
        "principal additive frequency",
        "exactly the one-block `COREAGG`",
        "minor-arc-only",
        "No HIGHFARGCDWAVE, COREAGG",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing: {marker}")


@dataclass(frozen=True)
class Q2:
    """An exact element a+b*sqrt(2)."""

    rational: Fraction
    root2: Fraction = Fraction()

    def __add__(self, other: Q2) -> Q2:
        return Q2(self.rational + other.rational, self.root2 + other.root2)

    def __sub__(self, other: Q2) -> Q2:
        return Q2(self.rational - other.rational, self.root2 - other.root2)

    def __mul__(self, other: Q2) -> Q2:
        return Q2(
            self.rational * other.rational + 2 * self.root2 * other.root2,
            self.rational * other.root2 + self.root2 * other.rational,
        )

    def scale(self, scalar: Fraction | int) -> Q2:
        scalar = Fraction(scalar)
        return Q2(scalar * self.rational, scalar * self.root2)

    def positive_by_squaring(self) -> bool:
        if self.rational <= 0:
            return False
        if self.root2 >= 0:
            return True
        return self.rational * self.rational > 2 * self.root2 * self.root2

    def render(self) -> str:
        return f"{self.rational}+({self.root2})*sqrt(2)"


@dataclass
class Radical:
    """A finite exact sum of coefficients times sqrt(squarefree radicands)."""

    terms: dict[int, Fraction]

    @staticmethod
    def zero() -> Radical:
        return Radical({})

    @staticmethod
    def rational(value: Fraction | int) -> Radical:
        value = Fraction(value)
        return Radical({1: value} if value else {})

    @staticmethod
    def root(radicand: int, coefficient: Fraction | int = 1) -> Radical:
        coefficient = Fraction(coefficient)
        return Radical({radicand: coefficient} if coefficient else {})

    def normalized(self) -> Radical:
        return Radical({r: c for r, c in self.terms.items() if c})

    def __add__(self, other: Radical) -> Radical:
        result = dict(self.terms)
        for radicand, coefficient in other.terms.items():
            result[radicand] = result.get(radicand, Fraction()) + coefficient
        return Radical(result).normalized()

    def __sub__(self, other: Radical) -> Radical:
        return self + other.scale(-1)

    def scale(self, scalar: Fraction | int) -> Radical:
        scalar = Fraction(scalar)
        return Radical(
            {radicand: scalar * coefficient for radicand, coefficient in self.terms.items()}
        ).normalized()

    def __mul__(self, other: Radical) -> Radical:
        result: dict[int, Fraction] = {}
        for left_rad, left_coefficient in self.terms.items():
            for right_rad, right_coefficient in other.terms.items():
                common = gcd(left_rad, right_rad)
                radicand = (left_rad // common) * (right_rad // common)
                coefficient = left_coefficient * right_coefficient * common
                result[radicand] = result.get(radicand, Fraction()) + coefficient
        return Radical(result).normalized()

    def square(self) -> Radical:
        return self * self

    def render(self) -> dict[str, str]:
        return {
            str(radicand): str(coefficient)
            for radicand, coefficient in sorted(self.terms.items())
        }

    def summary(self) -> dict[str, object]:
        payload = json.dumps(self.render(), separators=(",", ":"), sort_keys=True)
        return {
            "term_count": len(self.terms),
            "sha256": hashlib.sha256(payload.encode("ascii")).hexdigest(),
            "rational_component": str(self.terms.get(1, Fraction())),
        }


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    factors: list[tuple[int, int]] = []
    remaining = n
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def mobius(n: int) -> int:
    sign = 1
    for _, exponent in factorization(n):
        if exponent > 1:
            return 0
        sign = -sign
    return sign


def is_squarefree(n: int) -> bool:
    return mobius(n) != 0


def tau(n: int) -> int:
    result = 1
    for _, exponent in factorization(n):
        result *= exponent + 1
    return result


def kappa2(n: int) -> Fraction:
    if not is_squarefree(n):
        raise ValueError("kappa2 replay is restricted to squarefree n")
    result = Fraction(1)
    for prime, _ in factorization(n):
        result *= Fraction(prime + 2, prime)
    return result


def synthetic_wave(product_shell: int) -> Fraction:
    """A finite rational surrogate for one fixed I, alpha divisor wavelet."""
    if product_shell > REPLAY_CAP:
        return Fraction()
    return Fraction((product_shell**3 + 5 * product_shell + 7) % 23 - 11, 3)


def half_weighted_coefficient(n: int) -> Radical:
    """mu(n)/sqrt(n) = mu(n)*sqrt(n)/n on squarefree support."""
    sign = mobius(n)
    if sign == 0:
        return Radical.zero()
    return Radical.root(n, Fraction(sign, n))


def z_coordinate(core: int) -> Radical:
    total = Radical.zero()
    if not is_squarefree(core):
        return total
    for cofactor in range(1, REPLAY_CAP // core + 1):
        if not is_squarefree(cofactor) or gcd(core, cofactor) != 1:
            continue
        total = total + half_weighted_coefficient(cofactor).scale(
            synthetic_wave(core * cofactor)
        )
    return total


def additive_autocorrelation_panel(core: int = 6, near_gap: int = 2) -> dict[str, object]:
    sequence: dict[int, Radical] = {}
    for cofactor in range(1, REPLAY_CAP // core + 1):
        if is_squarefree(cofactor) and gcd(core, cofactor) == 1:
            sequence[cofactor] = half_weighted_coefficient(cofactor).scale(
                synthetic_wave(core * cofactor)
            )
    correlations: dict[int, Radical] = {}
    indices = sorted(sequence)
    for left in indices:
        for right in indices:
            shift = right - left
            correlations[shift] = correlations.get(shift, Radical.zero()) + (
                sequence[left] * sequence[right]
            )
    total_frequency = Radical.zero()
    near = Radical.zero()
    far = Radical.zero()
    for shift, value in correlations.items():
        total_frequency = total_frequency + value
        if abs(shift) <= near_gap:
            near = near + value
        else:
            far = far + value
    z_value = z_coordinate(core)
    if total_frequency.terms != z_value.square().terms:
        raise ArithmeticError("principal additive-frequency identity failed")
    if total_frequency.terms != (near + far).terms:
        raise ArithmeticError("near/far additive partition failed")
    return {
        "core": core,
        "sequence_coordinates": len(sequence),
        "shifts": len(correlations),
        "near_gap": near_gap,
        "principal_frequency": total_frequency.summary(),
        "z_squared": z_value.square().summary(),
        "near": near.summary(),
        "far": far.summary(),
        "identity": "sum_h C_g,I(h)=|Z_I,g|^2",
    }


def coprime_frequency(core: int) -> Radical:
    total = Radical.zero()
    for left in range(1, REPLAY_CAP // core + 1):
        if not is_squarefree(left) or gcd(left, core) != 1:
            continue
        left_value = half_weighted_coefficient(left).scale(
            synthetic_wave(core * left)
        )
        for right in range(1, REPLAY_CAP // core + 1):
            if (
                not is_squarefree(right)
                or gcd(right, core) != 1
                or gcd(left, right) != 1
            ):
                continue
            right_value = half_weighted_coefficient(right).scale(
                synthetic_wave(core * right)
            )
            total = total + left_value * right_value
    return total


def coprimality_inversion_panel() -> dict[str, object]:
    rows = []
    for core in (1, 2, 3, 6, 10):
        direct = coprime_frequency(core)
        via_divisors = Radical.zero()
        for divisor in range(1, REPLAY_CAP // core + 1):
            if (
                not is_squarefree(divisor)
                or gcd(divisor, core) != 1
                or mobius(divisor) == 0
            ):
                continue
            via_divisors = via_divisors + z_coordinate(core * divisor).square().scale(
                Fraction(mobius(divisor), divisor)
            )
        if direct.terms != via_divisors.terms:
            raise ArithmeticError(f"coprimality inversion failed at core={core}")
        rows.append(
            {
                "core": core,
                "direct": direct.summary(),
                "divisor_inversion": via_divisors.summary(),
            }
        )
    return {
        "rows": rows,
        "identity": (
            "C_cop(g,I)=sum_((d,g)=1) mu(d)/d |Z_(I,gd)|^2"
        ),
    }


def global_coreagg_panel() -> dict[str, object]:
    left = Radical.zero()
    right = Radical.zero()
    for core in range(1, REPLAY_CAP + 1):
        if not is_squarefree(core):
            continue
        left = left + coprime_frequency(core).scale(Fraction(kappa2(core), core))
        right = right + z_coordinate(core).square().scale(
            Fraction(tau(core), core * core)
        )
    if left.terms != right.terms:
        raise ArithmeticError("global principal frequency did not reassemble COREAGG")
    local_rows = []
    for prime in (2, 3, 5, 7, 11):
        convolution = kappa2(prime) - 1
        expected = Fraction(2, prime)
        if convolution != expected:
            raise ArithmeticError("local kappa2-mobius convolution failed")
        local_rows.append(
            {
                "prime": prime,
                "kappa2_minus_one": str(convolution),
                "tau_over_prime": str(expected),
            }
        )
    return {
        "left_coprime_frequency_assembly": left.summary(),
        "right_coreagg": right.summary(),
        "local_rows": local_rows,
        "identity": (
            "sum_g kappa2(g)/g C_cop(g,I)"
            "=sum_r tau(r)/r^2 |Z_(I,r)|^2"
        ),
    }


def kernel_mean_panel() -> dict[str, object]:
    q_zero = Q2(Fraction(1), Fraction(-1))
    q_zero_squared = q_zero * q_zero
    boundary_coefficient = q_zero_squared.scale(3)
    autocorrelation_coefficient = boundary_coefficient * boundary_coefficient
    if q_zero_squared != Q2(Fraction(3), Fraction(-2)):
        raise ArithmeticError("(1-sqrt(2))^2 identity failed")
    if boundary_coefficient != Q2(Fraction(9), Fraction(-6)):
        raise ArithmeticError("boundary mean coefficient failed")
    if autocorrelation_coefficient != Q2(Fraction(153), Fraction(-108)):
        raise ArithmeticError("autocorrelation zero-frequency coefficient failed")
    if not boundary_coefficient.positive_by_squaring():
        raise ArithmeticError("boundary mean coefficient is not positive")
    if not autocorrelation_coefficient.positive_by_squaring():
        raise ArithmeticError("autocorrelation coefficient is not positive")
    return {
        "q_zero": q_zero.render(),
        "q_zero_squared": q_zero_squared.render(),
        "boundary_mean": (
            "(9-6*sqrt(2))*(log(2))^2"
        ),
        "boundary_mean_nonzero": True,
        "boundary_positivity_margin": str(
            boundary_coefficient.rational**2
            - 2 * boundary_coefficient.root2**2
        ),
        "autocorrelation_zero_frequency": (
            "(153-108*sqrt(2))*(log(2))^4"
        ),
        "autocorrelation_zero_frequency_positive": True,
        "autocorrelation_positivity_margin": str(
            autocorrelation_coefficient.rational**2
            - 2 * autocorrelation_coefficient.root2**2
        ),
        "limit_inputs": [
            "lim_(s->0) (1-2^(-s))/s=log(2)",
            "lim_(s->0) (s-1)*(5s+3/2)/(s-1/2)=3",
        ],
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "A: direct beta/primitive-pair route",
        "kernel_mean": kernel_mean_panel(),
        "additive_autocorrelation": additive_autocorrelation_panel(),
        "coprimality_inversion": coprimality_inversion_panel(),
        "global_coreagg_frequency": global_coreagg_panel(),
        "exact_theorems": {
            "boundary_kernel_mean_nonzero": True,
            "autocorrelation_zero_frequency_positive": True,
            "principal_additive_frequency_equals_z_squared": True,
            "coprimality_inversion_exact": True,
            "global_frequency_assembly_equals_coreagg": True,
        },
        "scope_firewall": {
            "hidden_vanishing_moment_exists": False,
            "minor_arc_only_estimate_sufficient": False,
            "near_shift_estimate_sufficient": False,
            "highfargcdwave_proved": False,
            "coreagg_proved": False,
            "rh_or_grh_proved": False,
        },
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "resource_caps": {
            "radical_replay_product_shell_cap": REPLAY_CAP,
            "finite_fields": 0,
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-lock", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(
        run(check_sources=not args.no_source_lock), indent=2, sort_keys=True
    ) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
