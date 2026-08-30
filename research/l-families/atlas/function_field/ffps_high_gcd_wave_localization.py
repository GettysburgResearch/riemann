#!/usr/bin/env python3
"""Bounded exact replay for high balanced gcd-wave localization."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_HIGH_GCD_WAVE_LOCALIZATION.md"
SOURCE_COMMIT = "0855a61a2c719b4f93ad02d5aa8390ddff1b7765"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_PRIMITIVE_CORE_GCD_GRAM_CLOSURE.md"
    ): "d3b5a372b554f48fda50fc5d4b8de9a37b1ba036",
    (
        "research/l-families/atlas/function_field/"
        "ffps_primitive_core_gcd_gram_closure.py"
    ): "73a3f0a6fb05b02a5a469e1f34a7448a6c326fae",
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
        "genuinely high, balanced, coprime bilinear",
        "HIGHGCDWAVE",
        "Type-II region",
        "prescribed subpower reduced-height region",
        "No HIGHGCDWAVE, OFFGCDWAVE",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing: {marker}")


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be positive")
    factors: list[tuple[int, int]] = []
    remaining = n
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            exponent = 0
            while remaining % p == 0:
                remaining //= p
                exponent += 1
            factors.append((p, exponent))
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def is_squarefree(n: int) -> bool:
    return all(exponent == 1 for _, exponent in factorization(n))


def divisor_count_k(n: int, k: int) -> int:
    result = 1
    for _, exponent in factorization(n):
        numerator = 1
        denominator = 1
        for j in range(1, exponent + 1):
            numerator *= k - 1 + j
            denominator *= j
        result *= numerator // denominator
    return result


def harmonic_number(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction())


def product_shell(alpha: int, h: int) -> tuple[Fraction, Fraction]:
    if alpha not in (0, 1, 2) or h < 1:
        raise ValueError("invalid shell input")
    scale = 67**alpha
    return Fraction(h * h, 16 * scale), Fraction(4 * h * h, scale)


def ratio_localization_panel() -> dict[str, object]:
    rows = []
    for alpha in (0, 1, 2):
        for h in (4, 6, 8):
            lower, upper = product_shell(alpha, h)
            integers = [n for n in range(1, int(upper) + 1) if lower < n <= upper]
            checked = 0
            for n in integers:
                if not is_squarefree(n):
                    continue
                for m in integers:
                    if not is_squarefree(m):
                        continue
                    ratio = Fraction(n, m)
                    if not Fraction(1, 64) < ratio < 64:
                        raise ArithmeticError("factor-64 ratio localization failed")
                    checked += 1
            rows.append(
                {
                    "alpha": alpha,
                    "H": h,
                    "lower": str(lower),
                    "upper": str(upper),
                    "checked_squarefree_pairs": checked,
                }
            )
    return {"rows": rows, "ratio_window": "1/64 < a/b < 64"}


def divisor_harmonic_panel() -> dict[str, object]:
    rows = []
    for cap in (4, 8, 12):
        left = sum(
            (Fraction(divisor_count_k(n, 8), n) for n in range(1, cap + 1)),
            Fraction(),
        )
        right = harmonic_number(cap) ** 8
        if left > right:
            raise ArithmeticError("eight-fold harmonic divisor bound failed")
        rows.append({"cap": cap, "left": str(left), "right": str(right)})
    return {"rows": rows, "theorem": "sum_(n<=X) d_8(n)/n <= H_X^8"}


def synthetic_term(g: int, a: int, b: int) -> Fraction:
    """A deterministic signed finite surrogate with the exact gcd geometry."""
    if not (is_squarefree(g) and is_squarefree(a) and is_squarefree(b)):
        return Fraction()
    if gcd(a, b) != 1 or gcd(g, a * b) != 1 or (a, b) == (1, 1):
        return Fraction()
    sign = (-1) ** (len(factorization(a)) + len(factorization(b)))
    return Fraction(sign * ((3 * g + 5 * a + 7 * b) % 17 - 8), g * a * b)


def high_low_partition_panel() -> dict[str, object]:
    rows = []
    cap = 30
    for cutoff in (1, 2, 4, 6):
        full = low = high = Fraction()
        low_pairs = 0
        high_pairs = 0
        for g in range(1, cap + 1):
            for a in range(1, cap + 1):
                for b in range(1, cap + 1):
                    if not Fraction(1, 64) < Fraction(a, b) < 64:
                        continue
                    value = synthetic_term(g, a, b)
                    full += value
                    if min(a, b) <= cutoff:
                        low += value
                        low_pairs += int(bool(value))
                    else:
                        high += value
                        high_pairs += int(bool(value))
        if full != low + high:
            raise ArithmeticError("high/low partition failed")
        rows.append(
            {
                "cutoff": cutoff,
                "full": str(full),
                "low": str(low),
                "high": str(high),
                "low_nonzero_terms": low_pairs,
                "high_nonzero_terms": high_pairs,
            }
        )
    return {"rows": rows, "partition_exact": True}


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "A: direct beta/primitive-pair route",
        "ratio_localization": ratio_localization_panel(),
        "divisor_harmonic_majorant": divisor_harmonic_panel(),
        "high_low_partition": high_low_partition_panel(),
        "exact_theorems": {
            "factor_64_reduced_ratio": True,
            "subpower_low_reduced_sector": True,
            "highgcdwave_equivalent_to_offgcdwave": True,
        },
        "bounds": {
            "low_sector": (
                "|O_low(H;B)| <<_R L_H B^2 "
                "(1+log(4H^2+2))^8"
            )
        },
        "scope_firewall": {
            "highgcdwave_proved": False,
            "offgcdwave_proved": False,
            "primcar_proved": False,
            "rh_or_grh_proved": False,
        },
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "resource_caps": {"largest_H": 8, "synthetic_cap": 30},
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
