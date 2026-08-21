#!/usr/bin/env python3
"""Exploratory cutoff-free finite Weil-matrix scan.

STATUS: ordinary arbitrary-precision computation, NOT interval-certified.

This is an independent implementation of the closed-form finite
Connes--van Suijlekom / Guinand--Weil matrix used in the project route
M-0001.  It deliberately avoids a finite archimedean integration cutoff T:
finite-T negative eigenvalues can be truncation artifacts.  The formulas are
recorded in D-0001 and traced to the sources listed in the experiment README.

A negative value emitted by this program is only an EMPIRICAL candidate.  To
become a counterexample witness, the same rational/dyadic test vector must be
checked against rigorous interval enclosures for every matrix entry, with a
strict upper bound v^T Q v < 0.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

import mpmath as mp

EXPERIMENT_ID = "X-0001"
IMPLEMENTATION_VERSION = "0.1.0"


@dataclass(frozen=True)
class TailBounds:
    """Analytic upper bounds for omitted geometric-series tails.

    These inequalities are exact on real arithmetic.  Their numerical
    evaluation here is *not* directed-rounding interval arithmetic, so the
    reported values are diagnostics rather than proof certificates.
    """

    terms: int
    g_s: mp.mpf
    g_cc: mp.mpf
    g_x1: mp.mpf
    g_x2: mp.mpf

    @property
    def maximum(self) -> mp.mpf:
        return max(self.g_s, self.g_cc, self.g_x1, self.g_x2)


def _require_integer(name: str, value: int, minimum: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}; got {value!r}")
    return value


def primes_up_to(limit: int) -> list[int]:
    """Return all primes <= limit using an exact integer sieve."""

    limit = _require_integer("limit", limit, 2)
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_powers_up_to(c: int) -> list[tuple[int, int]]:
    """Return sorted pairs (q, p) for q=p^a <= integer bound c."""

    c = _require_integer("c", c, 2)
    out: list[tuple[int, int]] = []
    for p in primes_up_to(c):
        q = p
        while q <= c:
            out.append((q, p))
            if q > c // p:
                break
            q *= p
    out.sort()
    return out


def geometric_sums(
    n: int,
    L: mp.mpf,
    *,
    target: mp.mpf,
    max_terms: int = 1_000_000,
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf, TailBounds]:
    """Compute the four exponentially convergent correction sums.

    For c_k=2k+1/2, w=2*pi*n/L, and e_k=exp(-c_k L), this returns
    G_S, G_CC, G_X1, G_X2.  After K included terms, conservative absolute
    tail bounds follow from e_{k+1}/e_k=exp(-2L) and c_k monotonicity:

      |tail(G_S)|, |tail(G_X2)| <= E / c_next^2
      |tail(G_CC)|, |tail(G_X1)| <= E / c_next

    where E=e_next/(1-exp(-2L)).
    """

    if n < 0:
        raise ValueError("n must be nonnegative")
    if target <= 0:
        raise ValueError("target must be positive")

    w = 2 * mp.pi * n / L
    w2 = w * w
    ratio = mp.exp(-2 * L)
    one_minus_ratio = 1 - ratio

    g_s = mp.mpf("0")
    g_cc = mp.mpf("0")
    g_x1 = mp.mpf("0")
    g_x2 = mp.mpf("0")

    for k in range(max_terms):
        c_k = mp.mpf(2 * k) + mp.mpf("0.5")
        e_k = mp.exp(-c_k * L)
        den = c_k * c_k + w2
        g_s += e_k / den
        if n:
            g_cc += e_k * w2 / (c_k * den)
        g_x1 += e_k * c_k / den
        g_x2 += e_k * (c_k * c_k - w2) / (den * den)

        c_next = c_k + 2
        envelope = mp.exp(-c_next * L) / one_minus_ratio
        b_sq = envelope / (c_next * c_next)
        b_lin = envelope / c_next
        bounds = TailBounds(
            terms=k + 1,
            g_s=b_sq,
            g_cc=mp.mpf("0") if n == 0 else b_lin,
            g_x1=b_lin,
            g_x2=b_sq,
        )
        if bounds.maximum <= target:
            return g_s, g_cc, g_x1, g_x2, bounds

    raise RuntimeError(
        f"geometric series failed to reach target {target} in {max_terms} terms"
    )


def coerce_cutoff(c: int | str | mp.mpf) -> mp.mpf:
    """Parse c without silently introducing binary-float input error."""

    if isinstance(c, bool) or isinstance(c, float):
        raise TypeError("c must be an int, decimal string, or mp.mpf; binary float is rejected")
    value = mp.mpf(c)
    if not mp.isfinite(value) or value < 2:
        raise ValueError(f"c must be finite and >= 2; got {c!r}")
    return value


def canonical_cutoff(c: mp.mpf, digits: int) -> str:
    if c == mp.floor(c):
        return str(int(c))
    return mp.nstr(c, digits, strip_zeros=True)


def closed_form_sequences(
    c: int | str | mp.mpf,
    N: int,
    *,
    dps: int,
) -> tuple[list[mp.mpf], list[mp.mpf], list[mp.mpf], mp.mpf, dict]:
    """Build S(n), CC(n), XC(n), n=0,...,N, without a finite T cutoff."""

    c_value = coerce_cutoff(c)
    N = _require_integer("N", N, 1)
    dps = _require_integer("dps", dps, 30)

    L = mp.log(c_value)
    quarter = mp.mpf("0.25")
    psi_quarter = mp.digamma(quarter)
    target = mp.power(10, -(dps - 15))

    S: list[mp.mpf] = []
    CC: list[mp.mpf] = []
    XC: list[mp.mpf] = []
    tail_rows: list[dict] = []

    for n in range(N + 1):
        w = 2 * mp.pi * n / L
        z = mp.mpc(quarter, mp.pi * n / L)
        psi = mp.digamma(z)
        psi1 = mp.polygamma(1, z)
        g_s, g_cc, g_x1, g_x2, bounds = geometric_sums(
            n, L, target=target
        )

        if n == 0:
            S_n = mp.mpf("0")
            CC_n = mp.mpf("0")
        else:
            S_n = mp.im(psi) / 2 - w * g_s
            CC_n = -(mp.re(psi) - psi_quarter) / 2 + g_cc
        XC_n = mp.re(psi1) / 4 - L * g_x1 - g_x2

        S.append(S_n)
        CC.append(CC_n)
        XC.append(XC_n)
        tail_rows.append(
            {
                "n": n,
                "terms": bounds.terms,
                "max_analytic_tail_bound": mp.nstr(bounds.maximum, 12),
            }
        )

    metadata = {
        "target": mp.nstr(target, 12),
        "rows": tail_rows,
    }
    return S, CC, XC, L, metadata


def _signed_odd_sequence(values: Sequence[mp.mpf], n: int) -> mp.mpf:
    return values[n] if n >= 0 else -values[-n]


def _j_term(L: mp.mpf) -> mp.mpf:
    U = mp.exp(L / 2)
    return (
        -2 * mp.log(U + 1)
        + mp.log(U * U + 1)
        + 2 * mp.atan(U)
        + mp.log(2)
        - mp.pi / 2
    )


def _kappa(L: mp.mpf) -> mp.mpf:
    eL = mp.exp(L)
    return mp.log(4 * mp.pi * (eL - 1) / (eL + 1)) + mp.euler


def build_cutoff_free_matrix(
    c: int | str | mp.mpf,
    N: int,
    *,
    dps: int = 80,
) -> tuple[mp.matrix, dict]:
    """Construct the real symmetric (2N+1)-square cutoff-free matrix Q_N(c)."""

    N = _require_integer("N", N, 1)
    dps = _require_integer("dps", dps, 30)

    with mp.workdps(dps):
        c_value = coerce_cutoff(c)
        c_text = canonical_cutoff(c_value, dps)
        S, CC, XC, L, tail_metadata = closed_form_sequences(c_value, N, dps=dps)
        pi = mp.pi
        sixteen_pi_sq = 16 * pi * pi
        L2 = L * L
        prefactor = 32 * L * mp.sinh(L / 4) ** 2
        kappa = _kappa(L)
        J = _j_term(L)

        pp = prime_powers_up_to(int(mp.floor(c_value)))
        weights = [mp.log(p) / mp.sqrt(q) for q, p in pp]
        positions = [mp.log(q) for q, _ in pp]

        dim = 2 * N + 1
        A = mp.matrix(dim, dim)
        for i in range(dim):
            n = i - N
            for j in range(i, dim):
                m = j - N

                numerator = L2 - sixteen_pi_sq * m * n
                denominator = (
                    (L2 + sixteen_pi_sq * m * m)
                    * (L2 + sixteen_pi_sq * n * n)
                )
                w_02 = prefactor * numerator / denominator

                if n == m:
                    w_r = kappa + 2 * CC[abs(n)] + J - (2 / L) * XC[abs(n)]
                else:
                    w_r = (
                        _signed_odd_sequence(S, m)
                        - _signed_odd_sequence(S, n)
                    ) / (pi * (n - m))

                w_p = mp.mpf("0")
                for weight, y in zip(weights, positions):
                    if n == m:
                        kernel = 2 * (1 - y / L) * mp.cos(2 * pi * n * y / L)
                    else:
                        kernel = (
                            mp.sin(2 * pi * m * y / L)
                            - mp.sin(2 * pi * n * y / L)
                        ) / (pi * (n - m))
                    w_p += weight * kernel

                value = w_02 - w_r - w_p
                A[i, j] = value
                A[j, i] = value

        metadata = {
            "c": c_text,
            "N": N,
            "dimension": dim,
            "dps": dps,
            "L": mp.nstr(L, dps),
            "prime_powers": [{"q": q, "p": p} for q, p in pp],
            "geometric_tails": tail_metadata,
        }
        return +A, metadata


def even_projector(N: int) -> mp.matrix:
    """Orthonormal embedding of the even sector into indices -N,...,N."""

    N = _require_integer("N", N, 1)
    dim = 2 * N + 1
    V = mp.matrix(dim, N + 1)
    V[N, 0] = 1
    inv_sqrt_2 = 1 / mp.sqrt(2)
    for k in range(1, N + 1):
        V[N - k, k] = inv_sqrt_2
        V[N + k, k] = inv_sqrt_2
    return V


def matrix_max_abs(A: mp.matrix) -> mp.mpf:
    return max(abs(A[i, j]) for i in range(A.rows) for j in range(A.cols))


def symmetry_error(A: mp.matrix) -> mp.mpf:
    """Direct entrywise symmetry check (avoids mpmath transpose-expression quirks)."""

    if A.rows != A.cols:
        raise ValueError("A must be square")
    return max(abs(A[i, j] - A[j, i]) for i in range(A.rows) for j in range(A.cols))


def vector_inf_norm(v: mp.matrix) -> mp.mpf:
    return max(abs(v[i]) for i in range(v.rows))


def smallest_even_eigenpair(A: mp.matrix) -> tuple[mp.mpf, mp.matrix, mp.matrix]:
    """Return (lambda_min, even_coordinates, full_coordinates)."""

    if A.rows != A.cols or A.rows % 2 != 1:
        raise ValueError("A must be an odd-dimensional square matrix")
    N = (A.rows - 1) // 2
    V = even_projector(N)
    A_even = V.T * A * V
    eigvals, eigvecs = mp.eigsy(A_even)
    lam = eigvals[0]
    v_even = eigvecs[:, 0]
    v_full = V * v_even
    return lam, v_even, v_full


def empirical_inertia(A: mp.matrix) -> dict[str, int]:
    """Count numerical eigenvalue signs; zero means exactly zero at current precision."""

    eigvals, _ = mp.eigsy(A)
    positive = sum(1 for x in eigvals if x > 0)
    negative = sum(1 for x in eigvals if x < 0)
    return {
        "positive": positive,
        "negative": negative,
        "zero_at_working_precision": A.rows - positive - negative,
    }


def _sign(x: mp.mpf) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def _decimal(x: mp.mpf, digits: int) -> str:
    return mp.nstr(x, digits, strip_zeros=False)


def analyze_cell(c: int | str | mp.mpf, N: int, *, dps: int, guard_dps: int) -> dict:
    """Run a cell twice and report precision stability and residuals."""

    if guard_dps <= dps:
        raise ValueError("guard_dps must exceed dps")

    A_lo, meta_lo = build_cutoff_free_matrix(c, N, dps=dps)
    with mp.workdps(dps):
        lam_lo, _, _ = smallest_even_eigenpair(A_lo)
        inertia_lo = empirical_inertia(A_lo)
        symmetry_lo = symmetry_error(A_lo)

    A_hi, meta_hi = build_cutoff_free_matrix(c, N, dps=guard_dps)
    with mp.workdps(guard_dps):
        lam_hi, v_even, v_full = smallest_even_eigenpair(A_hi)
        residual = vector_inf_norm(A_hi * v_full - lam_hi * v_full)
        rayleigh = (v_full.T * A_hi * v_full)[0]
        inertia_hi = empirical_inertia(A_hi)
        symmetry_hi = symmetry_error(A_hi)
        delta = abs(lam_hi - lam_lo)
        scale = max(abs(lam_hi), abs(lam_lo), mp.power(10, -(dps - 5)))
        relative_delta = delta / scale

        status = "EMPIRICAL_NEGATIVE" if lam_hi < 0 else "EMPIRICAL_NONNEGATIVE"
        if _sign(lam_hi) != _sign(lam_lo):
            status = "PRECISION_UNSTABLE"

        candidate = None
        if lam_hi < 0:
            candidate = {
                "status": "EMPIRICAL_ONLY",
                "even_sector_coefficients": [
                    _decimal(v_even[i], guard_dps) for i in range(v_even.rows)
                ],
                "full_coefficients_indexed_minus_N_to_N": [
                    _decimal(v_full[i], guard_dps) for i in range(v_full.rows)
                ],
                "rayleigh_quotient": _decimal(rayleigh, guard_dps),
                "required_next_step": (
                    "Round to an explicit rational/dyadic vector and prove a strict "
                    "negative upper bound using Arb interval entries; this JSON is not a proof."
                ),
            }

        return {
            "c": meta_hi["c"],
            "N": N,
            "dimension": 2 * N + 1,
            "classification": status,
            "minimum_even_eigenvalue": {
                "dps": dps,
                "value": _decimal(lam_lo, dps),
                "sign": _sign(lam_lo),
                "guard_dps": guard_dps,
                "guard_value": _decimal(lam_hi, guard_dps),
                "guard_sign": _sign(lam_hi),
                "absolute_change": _decimal(delta, min(guard_dps, 40)),
                "relative_change": _decimal(relative_delta, min(guard_dps, 40)),
            },
            "guard_residual_inf_norm": _decimal(residual, min(guard_dps, 40)),
            "guard_rayleigh_minus_eigenvalue": _decimal(
                abs(rayleigh - lam_hi), min(guard_dps, 40)
            ),
            "symmetry_error": {
                "dps": _decimal(symmetry_lo, 10),
                "guard_dps": _decimal(symmetry_hi, 10),
            },
            "empirical_full_inertia": {
                "dps": inertia_lo,
                "guard_dps": inertia_hi,
            },
            "candidate_vector": candidate,
            "metadata": meta_hi,
            "warning": (
                "All signs are ordinary mpmath observations. No directed rounding, "
                "entrywise interval enclosure, or certified inertia is provided."
            ),
        }


def scan(
    cutoffs: Iterable[int | str | mp.mpf],
    bands: Iterable[int],
    *,
    dps: int,
    guard_dps: int,
) -> dict:
    cutoff_list = list(cutoffs)
    band_list = list(bands)
    cells = []
    for c in cutoff_list:
        for N in band_list:
            print(f"[{EXPERIMENT_ID}] c={c} N={N} dps={dps}/{guard_dps}", file=sys.stderr)
            cells.append(analyze_cell(c, N, dps=dps, guard_dps=guard_dps))

    negatives = [
        {"c": cell["c"], "N": cell["N"]}
        for cell in cells
        if cell["classification"] == "EMPIRICAL_NEGATIVE"
    ]
    unstable = [
        {"c": cell["c"], "N": cell["N"]}
        for cell in cells
        if cell["classification"] == "PRECISION_UNSTABLE"
    ]
    return {
        "experiment_id": EXPERIMENT_ID,
        "implementation_version": IMPLEMENTATION_VERSION,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "research_question": (
            "Does the cutoff-free finite Weil matrix exhibit a reproducible negative "
            "quadratic direction at any scanned (c,N)?"
        ),
        "parameters": {
            "cutoffs": list(dict.fromkeys(cell["c"] for cell in cells)),
            "bands": band_list,
            "dps": dps,
            "guard_dps": guard_dps,
        },
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "mpmath": mp.__version__,
        },
        "summary": {
            "cells": len(cells),
            "empirical_negative_cells": negatives,
            "precision_unstable_cells": unstable,
        },
        "cells": cells,
    }


def parse_cutoff_list(values: Sequence[str]) -> list[str]:
    out: list[str] = []
    for value in values:
        # Validate now, preserve decimal text for deterministic reparsing at working precision.
        with mp.workdps(50):
            coerce_cutoff(value)
        if value not in out:
            out.append(value)
    return out


def parse_int_list(values: Sequence[str]) -> list[int]:
    out: list[int] = []
    for value in values:
        item = int(value)
        if item not in out:
            out.append(item)
    return out


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cutoffs",
        nargs="+",
        default=["2", "3", "5", "7", "11", "13"],
        help="decimal cutoffs c >= 2; use strings, not binary floats",
    )
    parser.add_argument(
        "--bands",
        nargs="+",
        default=["2", "4", "6", "8"],
        help="Galerkin half-bands N >= 1",
    )
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--guard-dps", type=int, default=90)
    parser.add_argument("--output", type=Path, default=None)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cutoffs = parse_cutoff_list(args.cutoffs)
    bands = parse_int_list(args.bands)
    result = scan(cutoffs, bands, dps=args.dps, guard_dps=args.guard_dps)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
