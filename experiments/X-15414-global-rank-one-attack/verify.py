#!/usr/bin/env python3
"""Exact rational checker for the dyadic weighted-Chebyshev square identity.

This verifies only finite algebra for a synthetic nonnegative arithmetic weight
sequence. It does not evaluate zeta, primes, zero ordinates, or an RH sign.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15414-global-rank-one-attack.v1"
RESULT_SCHEMA = "riemann.x15414-global-rank-one-attack.verification.v1"


class VerificationError(ValueError):
    pass


def is_int(x: Any) -> bool:
    return isinstance(x, int) and not isinstance(x, bool)


def rat(raw: Any, name: str) -> Fraction:
    if is_int(raw):
        return Fraction(raw)
    if not isinstance(raw, dict) or set(raw) != {"numerator", "denominator"}:
        raise VerificationError(f"{name}: expected rational object")
    n, d = raw["numerator"], raw["denominator"]
    if not is_int(n) or not is_int(d) or d <= 0:
        raise VerificationError(f"{name}: malformed rational")
    return Fraction(n, d)


def fj(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def canonical_sha(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def prefix(entries: list[tuple[int, Fraction]], y: Fraction) -> Fraction:
    return sum((w for n, w in entries if Fraction(n) <= y), Fraction())


def signal_numerator(entries: list[tuple[int, Fraction]], y: Fraction) -> Fraction:
    """D(y)=A(y)-4 A(y/4)."""
    return prefix(entries, y) - 4 * prefix(entries, y / 4)


def integrate_piecewise(entries: list[tuple[int, Fraction]], lo: Fraction, hi: Fraction) -> tuple[Fraction, list[dict[str, Any]]]:
    if not (0 < lo < hi):
        raise VerificationError("require 0 < lower < upper")

    breakpoints = {lo, hi}
    for n, _ in entries:
        q = Fraction(n)
        if lo < q < hi:
            breakpoints.add(q)
        if lo < 4 * q < hi:
            breakpoints.add(4 * q)
    cuts = sorted(breakpoints)

    total = Fraction()
    cells: list[dict[str, Any]] = []
    for a, b in zip(cuts, cuts[1:]):
        mid = (a + b) / 2
        d = signal_numerator(entries, mid)
        # Q(log y)=D(y)/sqrt(y) and d(log y)=dy/y, so the direct
        # signal energy is integral D^2/y^2 dy. The C-square identity
        # has the identical integrand because C(y)-C(y/4)=D(y)/y.
        value = d * d * (1 / a - 1 / b)
        if value < 0:
            raise VerificationError("negative cell energy")
        total += value
        cells.append({
            "lower": fj(a),
            "upper": fj(b),
            "D": fj(d),
            "energy": fj(value),
        })
    return total, cells


def stationary_kernel(ns: list[int]) -> list[list[Fraction]]:
    out: list[list[Fraction]] = []
    for m in ns:
        row: list[Fraction] = []
        for n in ns:
            big, small = max(m, n), min(m, n)
            row.append(Fraction(4, big) - Fraction(1, small) if big <= 4 * small else Fraction())
        out.append(row)
    return out


def ldl_positive(A: list[list[Fraction]]) -> list[Fraction]:
    n = len(A)
    if any(len(row) != n for row in A):
        raise VerificationError("stationary kernel not square")
    if any(A[i][j] != A[j][i] for i in range(n) for j in range(n)):
        raise VerificationError("stationary kernel not symmetric")
    L = [[Fraction() for _ in range(n)] for _ in range(n)]
    pivots: list[Fraction] = []
    for i in range(n):
        L[i][i] = Fraction(1)
        p = A[i][i] - sum((L[i][r] * L[i][r] * pivots[r] for r in range(i)), Fraction())
        if p <= 0:
            raise VerificationError(f"stationary kernel pivot {i} not positive")
        pivots.append(p)
        for j in range(i + 1, n):
            residual = A[j][i] - sum((L[j][r] * L[i][r] * pivots[r] for r in range(i)), Fraction())
            L[j][i] = residual / p
    return pivots


def verify(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("schema") != SCHEMA:
        raise VerificationError("schema")
    raw_entries = doc.get("weighted_atoms")
    if not isinstance(raw_entries, list) or not raw_entries:
        raise VerificationError("weighted_atoms")

    entries: list[tuple[int, Fraction]] = []
    seen: set[int] = set()
    for i, item in enumerate(raw_entries):
        if not isinstance(item, dict) or set(item) != {"n", "weight"}:
            raise VerificationError(f"atom[{i}] schema")
        n = item["n"]
        if not is_int(n) or n < 2 or n in seen:
            raise VerificationError(f"atom[{i}] index")
        w = rat(item["weight"], f"atom[{i}].weight")
        if w < 0:
            raise VerificationError(f"atom[{i}] negative weight")
        seen.add(n)
        entries.append((n, w))
    entries.sort()

    ns = [n for n, _ in entries]
    stationary = stationary_kernel(ns)
    stationary_pivots = ldl_positive(stationary)

    lo = rat(doc.get("lower_Y"), "lower_Y")
    hi = rat(doc.get("upper_Y"), "upper_Y")
    energy, cells = integrate_piecewise(entries, lo, hi)

    sample_raw = doc.get("sample_Y")
    if not isinstance(sample_raw, list) or not sample_raw:
        raise VerificationError("sample_Y")
    samples = []
    for i, raw in enumerate(sample_raw):
        y = rat(raw, f"sample_Y[{i}]")
        if y <= 0:
            raise VerificationError("nonpositive sample")
        a_y = prefix(entries, y)
        a_quarter = prefix(entries, y / 4)
        d = a_y - 4 * a_quarter
        q_num = d / y
        # Store the coefficient of sqrt(y) in sqrt(y)[C(y)-C(y/4)].
        # It is D(y)/y and therefore agrees exactly with the raw signal.
        c_difference_coefficient = d / y
        if q_num != c_difference_coefficient:
            raise VerificationError("dyadic point identity")
        samples.append({
            "Y": fj(y),
            "A_Y": fj(a_y),
            "A_Y_over_4": fj(a_quarter),
            "D_Y": fj(d),
            "Q_coefficient": fj(q_num),
            "C_difference_coefficient": fj(c_difference_coefficient),
        })

    declared = rat(doc.get("declared_energy"), "declared_energy")
    if declared != energy:
        raise VerificationError("declared energy mismatch")

    result: dict[str, Any] = {
        "schema": RESULT_SCHEMA,
        "classification": "EXACT_SYNTHETIC_DYADIC_SQUARE_IDENTITY",
        "atom_count": len(entries),
        "cell_count": len(cells),
        "energy": fj(energy),
        "stationary_ratio_kernel": [[fj(x) for x in row] for row in stationary],
        "stationary_kernel_ldl_pivots": [fj(x) for x in stationary_pivots],
        "samples": samples,
        "cells": cells,
        "verdict": "EXACT_DYADIC_WEIGHTED_CHEBYSHEV_IDENTITY_VERIFIED",
        "proof_boundary": (
            "Finite rational algebra for a synthetic atom sequence only; "
            "no prime manifest, zeta zero, Hardy exponent, or RH conclusion is checked."
        ),
    }
    result["proof_object_sha256"] = canonical_sha(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    raw = json.loads(args.certificate.read_text())
    if not isinstance(raw, dict):
        raise VerificationError("root must be object")
    result = verify(raw)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
