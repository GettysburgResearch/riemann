"""Infinite-Jacobi separation certificates for X-16206."""
from __future__ import annotations
from fractions import Fraction
from typing import Any
import numpy as np
from scipy.linalg import eigh_tridiagonal
from flint import ctx
from x16206_common import (GAMMA, MODES, BLOCK_INDICES, APPROX_DIM, STURM_DIM,
    STURM_RADIUS, exact_arb, fstr)

def diag_fraction(i: int, gamma: int = GAMMA) -> Fraction:
    ell = 2 * i
    xdiag = Fraction((ell + 1) ** 2, (2 * ell + 1) * (2 * ell + 3))
    if ell:
        xdiag += Fraction(ell * ell, (2 * ell + 1) * (2 * ell - 1))
    return Fraction(ell * (ell + 1)) + gamma * gamma * xdiag


def off_sq_fraction(i: int, gamma: int = GAMMA) -> Fraction:
    """Square of the Jacobi coupling between even indices i and i+1."""
    ell = 2 * i
    return Fraction(
        gamma**4 * (ell + 1) ** 2 * (ell + 2) ** 2 * (2 * ell + 1),
        ((2 * ell + 1) * (2 * ell + 3)) ** 2 * (2 * ell + 5),
    )


def tail_lower_bound(n: int = STURM_DIM, gamma: int = GAMMA) -> Fraction:
    # For ell>=2n, the kinetic diagonal is >=ell(ell+1), and each of the
    # two adjacent couplings is <=gamma^2/3. This is a deliberately coarse,
    # exact Gershgorin lower bound for the infinite Jacobi tail.
    ell = 2 * n
    return Fraction(ell * (ell + 1)) - Fraction(2 * gamma * gamma, 3)


def approximate_centers() -> np.ndarray:
    ell = np.arange(0, 2 * APPROX_DIM, 2, dtype=float)
    xdiag = (ell + 1) ** 2 / ((2 * ell + 1) * (2 * ell + 3))
    mask = ell > 0
    xdiag[mask] += ell[mask] ** 2 / ((2 * ell[mask] + 1) * (2 * ell[mask] - 1))
    diagonal = ell * (ell + 1) + GAMMA * GAMMA * xdiag
    l = ell[:-1]
    off = (
        GAMMA
        * GAMMA
        * (l + 1)
        * (l + 2)
        / ((2 * l + 1) * (2 * l + 3))
        * np.sqrt((2 * l + 1) / (2 * l + 5))
    )
    return eigh_tridiagonal(
        diagonal,
        off,
        select="i",
        select_range=(0, 12),
        eigvals_only=True,
        lapack_driver="stebz",
    )


def sturm_count_pair(energy: Fraction, precision: int = 192) -> tuple[int, int]:
    """Return lower/upper possible full-operator counts below energy.

    The lower count is the inertia of the principal block B-E. The upper count
    is the inertia after the maximal Schur correction b^2/(L-E) at its last
    coordinate. Equality certifies the exact infinite-Jacobi count.
    """
    ctx.prec = precision
    E = exact_arb(energy)
    L = tail_lower_bound()
    if not energy < L:
        raise RuntimeError("energy is not below the certified tail floor")

    pivot = exact_arb(diag_fraction(0)) - E
    if not (pivot > 0 or pivot < 0):
        raise RuntimeError("indeterminate first Sturm pivot")
    count = int(pivot < 0)
    for i in range(1, STURM_DIM):
        pivot = exact_arb(diag_fraction(i)) - E - exact_arb(off_sq_fraction(i - 1)) / pivot
        if not (pivot > 0 or pivot < 0):
            raise RuntimeError(f"indeterminate Sturm pivot {i}")
        if i == STURM_DIM - 1:
            lower_count = count + int(pivot < 0)
            correction = exact_arb(off_sq_fraction(i)) / (exact_arb(L) - E)
            corrected = pivot - correction
            if not (corrected > 0 or corrected < 0):
                raise RuntimeError("indeterminate Schur-corrected final pivot")
            upper_count = count + int(corrected < 0)
            return lower_count, upper_count
        count += int(pivot < 0)
    raise AssertionError("unreachable")


def certify_separations() -> list[dict[str, Any]]:
    centers = approximate_centers()
    rows: list[dict[str, Any]] = []
    L = tail_lower_bound()
    for mode, index in zip(MODES, BLOCK_INDICES, strict=True):
        center = Fraction.from_float(float(centers[index]))
        lo = center - STURM_RADIUS
        hi = center + STURM_RADIUS
        count_lo = sturm_count_pair(lo)
        count_hi = sturm_count_pair(hi)
        if count_lo != (index, index) or count_hi != (index + 1, index + 1):
            raise RuntimeError(
                f"failed infinite-Jacobi count for mode {mode}: {count_lo}, {count_hi}"
            )
        sigma_lo = lo / (GAMMA * GAMMA)
        sigma_hi = hi / (GAMMA * GAMMA)
        if sigma_lo <= 0 or sigma_hi >= Fraction(1, 8):
            raise RuntimeError("separation interval left the phase-safe range")
        rows.append(
            {
                "mode": mode,
                "even_block_index": index,
                "mu_interval": [fstr(lo), fstr(hi)],
                "sigma_sq_interval": [fstr(sigma_lo), fstr(sigma_hi)],
                "sturm_count_at_lower": list(count_lo),
                "sturm_count_at_upper": list(count_hi),
                "principal_dimension": STURM_DIM,
                "tail_lower_bound": fstr(L),
                "tail_schur_correction_rule": "b_N^2/(tail_lower-E)",
            }
        )
    return rows
