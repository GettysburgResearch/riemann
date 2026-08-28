#!/usr/bin/env python3
"""Exact bounded replay for divisor-wave shifted-zeta factorization."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_DIVISOR_WAVE_SHIFTED_ZETA_FACTORIZATION.md"
SOURCE_COMMIT = "cf5cf6876dce5c8a969ad4636055215f7cec395d"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_HIGH_GCD_WAVE_LOCALIZATION.md"
    ): "1493a630000c211717339b8dd2e92244b624a6cd",
    (
        "research/l-families/atlas/function_field/"
        "ffps_high_gcd_wave_localization.py"
    ): "951ef7a801fa2691e9649403072d9469ea190d8d",
}


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
        "two shifted reciprocal-zeta factors",
        "double frequency integral",
        "finitely many omitted local factors",
        "additional cancellation mechanism",
        "No Fourier-mode bound, HIGHGCDWAVE",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing: {marker}")


def divisors(n: int) -> tuple[int, ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be positive")
    result = [d for d in range(1, n + 1) if n % d == 0]
    return tuple(result)


def interval_divisors(n: int, alpha: int, t: int) -> tuple[int, ...]:
    scale = 67**alpha
    return tuple(
        a
        for a in divisors(n)
        if max(scale * a, n // a) <= t
    )


def hyperbola_interval_panel() -> dict[str, object]:
    rows = []
    for n, alpha, t in ((30, 0, 10), (210, 0, 30), (30, 1, 70), (66, 0, 20)):
        direct = interval_divisors(n, alpha, t)
        lower_upper = tuple(
            a
            for a in divisors(n)
            if Fraction(n, t) <= a <= Fraction(t, 67**alpha)
        )
        if direct != lower_upper:
            raise ArithmeticError("hyperbola interval equivalence failed")
        rows.append(
            {
                "N": n,
                "alpha": alpha,
                "T": t,
                "divisors": list(direct),
                "interval_equal": True,
            }
        )
    return {"rows": rows}


def orientation_laurent_panel(number_of_primes: int = 4) -> dict[str, object]:
    """Compare divisor orientations with product of local z+z^-1 choices."""
    direct: dict[tuple[int, ...], int] = {}
    for bits in product((0, 1), repeat=number_of_primes):
        exponent = tuple(1 if bit else -1 for bit in bits)
        direct[exponent] = direct.get(exponent, 0) + 1
    tensor = {tuple(): 1}
    for _ in range(number_of_primes):
        enlarged: dict[tuple[int, ...], int] = {}
        for exponents, coefficient in tensor.items():
            for sign in (-1, 1):
                key = exponents + (sign,)
                enlarged[key] = enlarged.get(key, 0) + coefficient
        tensor = enlarged
    if direct != tensor:
        raise ArithmeticError("squarefree divisor Laurent product failed")
    return {
        "number_of_primes": number_of_primes,
        "orientation_count": len(direct),
        "product_equal": True,
        "local_factor": "z+z^-1",
    }


def correction_series(t: Fraction, order: int) -> tuple[Fraction, ...]:
    """Series of (1-t*x)/(1-t*x+x^2) through x^order."""
    q = [Fraction(1), -t, Fraction(1)]
    f = [Fraction(1), -t]
    e = [Fraction()] * (order + 1)
    for n in range(order + 1):
        rhs = f[n] if n < len(f) else Fraction()
        if n >= 1:
            rhs -= q[1] * e[n - 1]
        if n >= 2:
            rhs -= q[2] * e[n - 2]
        e[n] = rhs
    return tuple(e)


def local_euler_panel() -> dict[str, object]:
    rows = []
    for t in (Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)):
        e = correction_series(t, 8)
        q = (Fraction(1), -t, Fraction(1))
        product_coefficients = []
        for n in range(9):
            value = sum(
                (q[j] * e[n - j] for j in range(min(2, n) + 1)), Fraction()
            )
            product_coefficients.append(value)
        expected = [Fraction(1), -t] + [Fraction()] * 7
        if product_coefficients != expected:
            raise ArithmeticError("local shifted-zeta factorization failed")
        if e[0] != 1 or e[1] != 0 or e[2] != -1:
            raise ArithmeticError("Euler correction did not begin at x^2")
        rows.append(
            {
                "t": str(t),
                "correction_coefficients": [str(value) for value in e],
                "product_recovers_1_minus_t_x": True,
            }
        )
    return {
        "rows": rows,
        "identity": (
            "(1-t*x) = (1-t*x+x^2) * "
            "[(1-t*x)/(1-t*x+x^2)]"
        ),
    }


def finite_euler_product_panel() -> dict[str, object]:
    """Check squarefree coefficients from local factors on a finite prime set."""
    t_values = (Fraction(2), Fraction(-1), Fraction(0), Fraction(1))
    direct: dict[tuple[int, ...], Fraction] = {}
    for bits in product((0, 1), repeat=len(t_values)):
        coefficient = Fraction(1)
        for bit, t in zip(bits, t_values, strict=True):
            if bit:
                coefficient *= -t
        direct[bits] = coefficient
    expanded = {tuple(): Fraction(1)}
    for t in t_values:
        next_values: dict[tuple[int, ...], Fraction] = {}
        for key, coefficient in expanded.items():
            next_values[key + (0,)] = coefficient
            next_values[key + (1,)] = -t * coefficient
        expanded = next_values
    if direct != expanded:
        raise ArithmeticError("finite Euler product expansion failed")
    return {
        "local_t_values": [str(value) for value in t_values],
        "coefficient_count": len(direct),
        "squarefree_product_equal": True,
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "A: direct beta/primitive-pair route",
        "hyperbola_interval": hyperbola_interval_panel(),
        "divisor_laurent_product": orientation_laurent_panel(),
        "local_shifted_zeta_factor": local_euler_panel(),
        "finite_euler_product": finite_euler_product_panel(),
        "exact_theorems": {
            "prefix_fourier_hyperbola": True,
            "squarefree_divisor_product": True,
            "shifted_reciprocal_zeta_factorization": True,
            "zero_frequency_double_reciprocal_zeta": True,
        },
        "factorization": {
            "F_xi": (
                "E_xi(s)/[zeta^(67)(s-i*xi) zeta^(67)(s+i*xi)]"
            ),
            "E_local_minus_one": (
                "-p^(-2s)/[(1-p^(-(s-i*xi)))(1-p^(-(s+i*xi)))]"
            ),
        },
        "scope_firewall": {
            "fourier_mode_bound_proved": False,
            "highgcdwave_proved": False,
            "pole_survival_at_every_local_exception_proved": False,
            "rh_or_grh_proved": False,
        },
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "resource_caps": {
            "formal_orientation_primes": 4,
            "local_series_order": 8,
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
