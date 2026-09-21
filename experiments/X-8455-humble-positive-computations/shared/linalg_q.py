"""Tiny exact/rational linear algebra helpers.

These are convenience routines for reconnaissance. They are not a certified
interval-arithmetic library. Prefer independent reimplementation before using
any output as a proof object.
"""

from __future__ import annotations

from fractions import Fraction as F
from typing import Iterable


def _inertia_gaussian(M: list[list[F]]) -> tuple[int, int, int]:
    n = len(M)
    a = [[F(M[i][j]) for j in range(n)] for i in range(n)]
    pos = neg = zero = 0
    for k in range(n):
        # find pivot
        piv = None
        for i in range(k, n):
            if a[i][k] != 0:
                piv = i
                break
        if piv is None:
            zero += 1
            continue
        if piv != k:
            a[k], a[piv] = a[piv], a[k]
            for r in range(n):
                if r != k and r != piv:
                    a[r][k], a[r][piv] = a[r][piv], a[r][k]
        d = a[k][k]
        if d > 0:
            pos += 1
        elif d < 0:
            neg += 1
        else:
            zero += 1
        for i in range(k + 1, n):
            if a[i][k] == 0:
                continue
            factor = a[i][k] / d
            for j in range(k, n):
                a[i][j] -= factor * a[k][j]
            # keep symmetry roughly
            for j in range(k + 1, n):
                a[j][i] = a[i][j]
    return pos, neg, zero


def inertia_ldl(M: list[list[F]]) -> tuple[int, int, int]:
    """Return (n_pos, n_neg, n_zero) for a symmetric rational matrix.

    Uses sympy when available. Provisional — re-check before proof use.
    """
    try:
        import sympy as sp

        n = len(M)
        MS = sp.Matrix(n, n, lambda i, j: sp.Rational(M[i][j]))
        MS = (MS + MS.T) / 2
        if hasattr(MS, "inertia"):
            inn = MS.inertia()
            return int(inn[0]), int(inn[1]), int(inn[2])
        ev = MS.eigenvals()
        pos = neg = zero = 0
        for val, mult in ev.items():
            try:
                q = sp.together(sp.simplify(val))
                if q.is_real is False:
                    # numerical fallback
                    rv = float(sp.re(sp.N(val, 60)))
                    if rv > 1e-18:
                        pos += int(mult)
                    elif rv < -1e-18:
                        neg += int(mult)
                    else:
                        zero += int(mult)
                else:
                    if q > 0:
                        pos += int(mult)
                    elif q < 0:
                        neg += int(mult)
                    else:
                        zero += int(mult)
            except Exception:
                rv = float(sp.re(sp.N(val, 60)))
                if rv > 1e-18:
                    pos += int(mult)
                elif rv < -1e-18:
                    neg += int(mult)
                else:
                    zero += int(mult)
        return pos, neg, zero
    except Exception:
        return _inertia_gaussian(M)


def mat_add(A: list[list[F]], B: list[list[F]], c: F = F(1)) -> list[list[F]]:
    n = len(A)
    return [[A[i][j] + c * B[i][j] for j in range(n)] for i in range(n)]


def quadratic(M: list[list[F]], x: list[F]) -> F:
    n = len(x)
    return sum(x[i] * M[i][j] * x[j] for i in range(n) for j in range(n))


def normalize_sum(p: Iterable[F]) -> list[F]:
    vals = [F(v) for v in p]
    s = sum(vals)
    if s == 0:
        raise ValueError("cannot normalize a zero-sum vector")
    return [v / s for v in vals]
