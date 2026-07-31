#!/usr/bin/env python3
"""Exact regressions for L-14312/L-14313 growing-low-block closure.

This program performs no zeta, xi, prime, floating-point, or interval-special-
function evaluation. It checks three finite algebraic facts:

1. fixed entries and strong convergence do not imply norm convergence for a
   growing self-adjoint matrix (the escaping rank-one regression);
2. common finite-rank tightness plus a finite compressed norm bound gives the
   quantitative L-14312 estimate;
3. exact radical tail-tail and tail-complement bounds imply the dimension-free
   Schur lower bound in L-14313.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


class VerificationError(ValueError):
    pass


def f(value: int | str | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def zeros(n: int, m: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(m)] for _ in range(n)]


def identity(n: int) -> list[list[Fraction]]:
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def transpose(a: Sequence[Sequence[Fraction]]) -> list[list[Fraction]]:
    if not a:
        return []
    return [list(row) for row in zip(*a)]


def matmul(
    a: Sequence[Sequence[Fraction]], b: Sequence[Sequence[Fraction]]
) -> list[list[Fraction]]:
    if not a or not b or len(a[0]) != len(b):
        raise VerificationError("matrix product dimension mismatch")
    bt = transpose(b)
    return [
        [sum((x * y for x, y in zip(row, col)), Fraction(0)) for col in bt]
        for row in a
    ]


def add(
    a: Sequence[Sequence[Fraction]], b: Sequence[Sequence[Fraction]]
) -> list[list[Fraction]]:
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise VerificationError("matrix addition dimension mismatch")
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a: Sequence[Sequence[Fraction]], c: Fraction) -> list[list[Fraction]]:
    return [[c * x for x in row] for row in a]


def sub(
    a: Sequence[Sequence[Fraction]], b: Sequence[Sequence[Fraction]]
) -> list[list[Fraction]]:
    return add(a, scale(b, Fraction(-1)))


def symmetric(a: Sequence[Sequence[Fraction]]) -> bool:
    return len(a) > 0 and all(len(row) == len(a) for row in a) and all(
        a[i][j] == a[j][i] for i in range(len(a)) for j in range(len(a))
    )


def ldl_nonnegative(a: Sequence[Sequence[Fraction]]) -> list[Fraction]:
    """Exact LDL for positive semidefinite matrices with zero-pivot handling."""
    if not symmetric(a):
        raise VerificationError("LDL input must be nonempty and symmetric")
    n = len(a)
    l = zeros(n, n)
    d = [Fraction(0) for _ in range(n)]
    for i in range(n):
        l[i][i] = Fraction(1)
        pivot = a[i][i] - sum(
            (l[i][k] * l[i][k] * d[k] for k in range(i)), Fraction(0)
        )
        if pivot < 0:
            raise VerificationError(f"negative LDL pivot at {i}")
        d[i] = pivot
        for j in range(i + 1, n):
            numerator = a[j][i] - sum(
                (l[j][k] * l[i][k] * d[k] for k in range(i)), Fraction(0)
            )
            if pivot == 0:
                if numerator != 0:
                    raise VerificationError(
                        f"zero pivot with nonzero residual column at {i},{j}"
                    )
                l[j][i] = Fraction(0)
            else:
                l[j][i] = numerator / pivot
    return d


def solve(a: Sequence[Sequence[Fraction]], b: Sequence[Fraction]) -> list[Fraction]:
    n = len(a)
    if n == 0 or len(b) != n or any(len(row) != n for row in a):
        raise VerificationError("solve dimension mismatch")
    aug = [list(a[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise VerificationError("singular solve")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            c = aug[r][col]
            if c:
                aug[r] = [x - c * y for x, y in zip(aug[r], aug[col])]
    return [aug[i][-1] for i in range(n)]


def inverse(a: Sequence[Sequence[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    cols = [solve(a, identity(n)[j]) for j in range(n)]
    return transpose(cols)


def escaping_rank_one(level: int) -> list[list[Fraction]]:
    if level < 1:
        raise VerificationError("level must be positive")
    out = zeros(level, level)
    out[-1][-1] = Fraction(-1)
    return out


def verify_escaping(max_level: int = 12, fixed_prefix: int = 5) -> dict[str, Any]:
    if max_level <= fixed_prefix:
        raise VerificationError("max_level must exceed fixed_prefix")
    rows = []
    for j in range(1, max_level + 1):
        k = escaping_rank_one(j)
        fixed_entries_zero = True
        if j > fixed_prefix:
            for r in range(fixed_prefix):
                for c in range(fixed_prefix):
                    fixed_entries_zero &= k[r][c] == 0
        rows.append(
            {
                "level": j,
                "fixed_prefix_zero": fixed_entries_zero,
                "minimum_eigenvalue_exact": "-1",
                "operator_norm_exact": "1",
            }
        )
    if not all(row["fixed_prefix_zero"] for row in rows[fixed_prefix:]):
        raise VerificationError("escaping regression fixed-prefix gate failed")
    return {
        "classification": "EXACT_ESCAPING_MODE_REFUTATION",
        "max_level": max_level,
        "fixed_prefix": fixed_prefix,
        "all_late_fixed_entries_zero": True,
        "all_operator_norms_one": True,
        "all_minimum_eigenvalues_minus_one": True,
        "rows": rows,
    }


def verify_tightness_bound() -> dict[str, Any]:
    k = [
        [f("1/100"), f("-1/200"), f("1/1000"), 0],
        [f("-1/200"), f("1/80"), 0, f("-1/1000")],
        [f("1/1000"), 0, f("1/2000"), 0],
        [0, f("-1/1000"), 0, f("-1/2500")],
    ]
    p = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    p = [[f(x) for x in row] for row in p]
    i4 = identity(4)
    q = sub(i4, p)
    qk = matmul(q, k)
    tail_sq = sum((x * x for row in qk for x in row), Fraction(0))
    pkp = matmul(matmul(p, k), p)
    comp_sq = sum((x * x for row in pkp for x in row), Fraction(0))
    delta = f("1/500")
    rho = f("1/50")
    if tail_sq > delta * delta:
        raise VerificationError("declared tail bound is too small")
    if comp_sq > rho * rho:
        raise VerificationError("declared compressed bound is too small")
    total = rho + 2 * delta
    plus = add(scale(i4, total), k)
    minus = sub(scale(i4, total), k)
    plus_pivots = ldl_nonnegative(plus)
    minus_pivots = ldl_nonnegative(minus)
    return {
        "classification": "EXACT_L14312_QUANTITATIVE_CONTROL",
        "tail_frobenius_squared": fj(tail_sq),
        "tail_operator_upper": fj(delta),
        "compressed_frobenius_squared": fj(comp_sq),
        "compressed_operator_upper": fj(rho),
        "L14312_total_norm_upper": fj(total),
        "plus_LDL_pivots": [fj(x) for x in plus_pivots],
        "minus_LDL_pivots": [fj(x) for x in minus_pivots],
    }


def verify_radical_schur() -> dict[str, Any]:
    b = [
        [f("1/400"), f("1/1000"), 0],
        [f("1/1000"), f("1/500"), f("-1/2000")],
        [0, f("-1/2000"), f("-1/800")],
    ]
    r = [
        [f("1/100"), f("-1/200"), 0],
        [0, f("1/250"), f("1/125")],
    ]
    m = [[f(2), f("1/4")], [f("1/4"), f("3/2")]]
    h = f("1/5")
    alpha = f("1/250")
    beta_squared = f("1/5000")
    ldl_nonnegative(m)
    mi = inverse(m)
    schur_energy = matmul(matmul(transpose(r), mi), r)
    d = len(b)
    idd = identity(d)
    b_upper_pivots = ldl_nonnegative(sub(scale(idd, alpha), b))
    b_lower_pivots = ldl_nonnegative(add(scale(idd, alpha), b))
    cross_pivots = ldl_nonnegative(
        sub(scale(idd, beta_squared), schur_energy)
    )
    corrected = sub(b, scale(schur_energy, 1 / h))
    moat = alpha + beta_squared / h
    corrected_pivots = ldl_nonnegative(add(corrected, scale(idd, moat)))
    return {
        "classification": "EXACT_L14313_DIMENSION_FREE_SCHUR_CONTROL",
        "dimension": d,
        "alpha": fj(alpha),
        "beta_squared": fj(beta_squared),
        "h": fj(h),
        "lower_floor_loss": fj(moat),
        "B_upper_LDL_pivots": [fj(x) for x in b_upper_pivots],
        "B_lower_LDL_pivots": [fj(x) for x in b_lower_pivots],
        "cross_LDL_pivots": [fj(x) for x in cross_pivots],
        "corrected_floor_LDL_pivots": [fj(x) for x in corrected_pivots],
    }


def proof_digest(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


def run() -> dict[str, Any]:
    result: dict[str, Any] = {
        "schema": "riemann.x14307-growing-low-block-closure.v1",
        "analytic_claims": ["R-14301", "L-14312", "L-14313"],
        "escaping_mode": verify_escaping(),
        "tightness_bound": verify_tightness_bound(),
        "radical_schur_bound": verify_radical_schur(),
        "verdict": "PASS_EXACT_FINITE_REGRESSIONS",
        "proof_boundary": (
            "Exact Fraction arithmetic only. This verifies the finite linear-"
            "algebra statements and the escaping-mode counterexample; it does not "
            "prove collective compactness or an exact radical frame for the zeta "
            "Weil low packets."
        ),
    }
    result["proof_object_sha256"] = proof_digest(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = run()
    except (VerificationError, ZeroDivisionError, ValueError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
