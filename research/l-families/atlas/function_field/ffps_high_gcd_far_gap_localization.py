#!/usr/bin/env python3
"""Bounded exact replay for high/far gcd-wave localization."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_HIGH_GCD_FAR_GAP_LOCALIZATION.md"
SOURCE_COMMIT = "680be76bd31acdd96925d0b73f1a469226a19c9f"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_HIGH_GCD_WAVE_LOCALIZATION.md"
    ): "1493a630000c211717339b8dd2e92244b624a6cd",
    (
        "research/l-families/atlas/function_field/"
        "ffps_high_gcd_wave_localization.py"
    ): "951ef7a801fa2691e9649403072d9469ea190d8d",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_DIVISOR_WAVE_SHIFTED_ZETA_FACTORIZATION.md"
    ): "21ef6a6e0078beb85f81fc880e5f161fc6288a8f",
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
        "reduced **product-shell** variables",
        "high in both reduced product-shell coordinates",
        "HIGHFARGCDWAVE",
        "density-saving averaged Chowla theorem",
        "No HIGHFARGCDWAVE, HIGHGCDWAVE",
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
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be positive")
    result = 1
    for _, exponent in factorization(n):
        numerator = 1
        denominator = 1
        for j in range(1, exponent + 1):
            numerator *= k - 1 + j
            denominator *= j
        result *= numerator // denominator
    return result


def tau(n: int) -> int:
    return divisor_count_k(n, 2)


def harmonic_number(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction())


def tau_square_panel(limit: int = 80) -> dict[str, object]:
    rows = []
    for n in range(1, limit + 1):
        left = tau(n) ** 2
        right = divisor_count_k(n, 4)
        if left > right:
            raise ArithmeticError("tau squared exceeds d_4")
        if n in (1, 2, 6, 12, 30, 60, 80):
            rows.append({"n": n, "tau_squared": left, "d4": right})
    return {"checked": limit, "rows": rows, "inequality": "tau(n)^2 <= d_4(n)"}


def divisor_harmonic_panel() -> dict[str, object]:
    rows = []
    for k in (4, 8):
        for cap in (6, 10, 16):
            left = sum(
                (Fraction(divisor_count_k(n, k), n) for n in range(1, cap + 1)),
                Fraction(),
            )
            right = harmonic_number(cap) ** k
            if left > right:
                raise ArithmeticError("divisor harmonic majorant failed")
            rows.append(
                {"k": k, "cap": cap, "left": str(left), "right": str(right)}
            )
    return {
        "rows": rows,
        "theorem": "sum_(n<=X) d_k(n)/n <= H_X^k for k=4,8",
    }


def shifted_cauchy_panel(cap: int = 48, gap: int = 7) -> dict[str, object]:
    global_bound = harmonic_number(cap + gap) ** 4
    max_first = Fraction()
    max_second = Fraction()
    checked = 0
    for h in range(-gap, gap + 1):
        # Fractions do not represent square roots.  Replay the two rational
        # L2 factors entering Cauchy instead.
        first = sum(
            (Fraction(tau(a) ** 2, a) for a in range(1, cap + 1) if a + h >= 1),
            Fraction(),
        )
        second = sum(
            (
                Fraction(tau(a + h) ** 2, a + h)
                for a in range(1, cap + 1)
                if 1 <= a + h <= cap + gap
            ),
            Fraction(),
        )
        if first > global_bound or second > global_bound:
            raise ArithmeticError("shifted Cauchy factor exceeds d4 bound")
        max_first = max(max_first, first)
        max_second = max(max_second, second)
        checked += 1
    return {
        "cap": cap,
        "gap": gap,
        "shifts_checked": checked,
        "max_first_l2_factor": str(max_first),
        "max_second_l2_factor": str(max_second),
        "common_bound": str(global_bound),
        "conclusion": "each shifted tau correlation is at most H_(X+G)^4",
    }

def synthetic_term(g: int, a: int, b: int) -> Fraction:
    if not (is_squarefree(g) and is_squarefree(a) and is_squarefree(b)):
        return Fraction()
    if gcd(a, b) != 1 or gcd(g, a * b) != 1 or (a, b) == (1, 1):
        return Fraction()
    if not Fraction(1, 64) < Fraction(a, b) < 64:
        return Fraction()
    parity = len(factorization(a)) + len(factorization(b))
    amplitude = (5 * g + 7 * a + 11 * b) % 19 - 9
    return Fraction(((-1) ** parity) * amplitude, g * a * b)


def three_way_partition_panel(cap: int = 32) -> dict[str, object]:
    rows = []
    for cutoff, gap in ((1, 0), (2, 1), (4, 2), (6, 4)):
        full = low = high_near = high_far = Fraction()
        counts = {"low": 0, "high_near": 0, "high_far": 0}
        for g in range(1, cap + 1):
            for a in range(1, cap + 1):
                for b in range(1, cap + 1):
                    value = synthetic_term(g, a, b)
                    full += value
                    if min(a, b) <= cutoff:
                        low += value
                        counts["low"] += int(bool(value))
                    elif abs(a - b) <= gap:
                        high_near += value
                        counts["high_near"] += int(bool(value))
                    else:
                        high_far += value
                        counts["high_far"] += int(bool(value))
        if full != low + high_near + high_far:
            raise ArithmeticError("three-way partition failed")
        rows.append(
            {
                "cutoff": cutoff,
                "gap": gap,
                "full": str(full),
                "low": str(low),
                "high_near": str(high_near),
                "high_far": str(high_far),
                "counts": counts,
            }
        )
    return {"cap": cap, "rows": rows, "partition_exact": True}


def shifted_coprimality_panel(limit: int = 30) -> dict[str, object]:
    checked = 0
    for a in range(1, limit + 1):
        for h in range(-a + 1, limit + 1):
            b = a + h
            if gcd(a, b) != gcd(a, h):
                raise ArithmeticError("shifted coprimality identity failed")
            checked += 1
    return {
        "checked": checked,
        "identity": "gcd(a,a+h)=gcd(a,h)",
        "limit": limit,
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "A: direct beta/primitive-pair route",
        "tau_square": tau_square_panel(),
        "divisor_harmonic": divisor_harmonic_panel(),
        "shifted_cauchy": shifted_cauchy_panel(),
        "three_way_partition": three_way_partition_panel(),
        "shifted_coprimality": shifted_coprimality_panel(),
        "exact_theorems": {
            "near_gap_absolute_subpower": True,
            "three_way_partition": True,
            "highfargcdwave_equivalent_to_highgcdwave": True,
            "shifted_coprimality_normal_form": True,
        },
        "bounds": {
            "near_gap": (
                "|O_near(H;G)| <<_R L_H (2G+1) "
                "(1+log(4H^2+G+2))^12"
            )
        },
        "scope_firewall": {
            "gap_is_in_reduced_product_shell_variables": True,
            "qualitative_averaged_chowla_imported": False,
            "highfargcdwave_proved": False,
            "highgcdwave_proved": False,
            "rh_or_grh_proved": False,
        },
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "resource_caps": {
            "partition_cap": 32,
            "shifted_cauchy_cap": 48,
            "tau_square_cap": 80,
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
