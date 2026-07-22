#!/usr/bin/env python3
"""Prime-power edge search for the cutoff-free finite Weil matrix.

STATUS: exploratory arbitrary-precision computation, not an interval proof.

The exact part of this module is the algebraic description of the contribution
that enters when c crosses a prime power q=p^a. The full cutoff-free matrix is
computed independently with mpmath from the closed forms recorded in D-0001.
Any negative output remains EMPIRICAL until every entry is enclosed by directed
interval arithmetic and the dyadic checker accepts a strict negative bound.
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

EXPERIMENT_ID = "X-0601"
IMPLEMENTATION_VERSION = "0.1.0"


@dataclass(frozen=True)
class PrimePower:
    q: int
    p: int
    exponent: int

    @property
    def weight(self) -> mp.mpf:
        return mp.log(self.p) / mp.sqrt(self.q)


def primes_up_to(limit: int) -> list[int]:
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_powers_up_to(c: int | str | mp.mpf) -> list[PrimePower]:
    value = mp.mpf(c)
    if not mp.isfinite(value) or value <= 1:
        raise ValueError("c must be finite and greater than 1")
    bound = int(mp.floor(value))
    out: list[PrimePower] = []
    for p in primes_up_to(bound):
        q = p
        exponent = 1
        while q <= value:
            out.append(PrimePower(q=q, p=p, exponent=exponent))
            if q > bound // p:
                break
            q *= p
            exponent += 1
    out.sort(key=lambda item: item.q)
    return out


def identify_prime_power(q: int) -> PrimePower:
    if not isinstance(q, int) or isinstance(q, bool) or q < 2:
        raise ValueError("q must be an integer at least 2")
    for item in prime_powers_up_to(q):
        if item.q == q:
            return item
    raise ValueError(f"{q} is not a prime power")


def even_projector(N: int) -> mp.matrix:
    if not isinstance(N, int) or isinstance(N, bool) or N < 1:
        raise ValueError("N must be an integer at least 1")
    V = mp.matrix(2 * N + 1, N + 1)
    V[N, 0] = 1
    factor = 1 / mp.sqrt(2)
    for k in range(1, N + 1):
        V[N - k, k] = factor
        V[N + k, k] = factor
    return V


def endpoint_vector(N: int) -> mp.matrix:
    return mp.matrix([1] + [mp.sqrt(2)] * N)


def even_moment(v: mp.matrix, order: int) -> mp.mpf:
    """Return M_order for even coordinates v=(v_0,...,v_N).

    M_0 = v_0 + sqrt(2) sum_{k>=1} v_k and, for order>=1,
    M_order = sqrt(2) sum k^(2*order) v_k.
    """
    if v.cols != 1 or order < 0:
        raise ValueError("v must be a column vector and order nonnegative")
    N = v.rows - 1
    if order == 0:
        return v[0] + mp.sqrt(2) * sum(v[k] for k in range(1, N + 1))
    return mp.sqrt(2) * sum(mp.mpf(k) ** (2 * order) * v[k] for k in range(1, N + 1))


def edge_epsilon(c: int | str | mp.mpf, q: int) -> mp.mpf:
    c_value = mp.mpf(c)
    if c_value < q:
        raise ValueError("the q contribution is not present when c<q")
    return 1 - mp.log(q) / mp.log(c_value)


def prime_power_full_block(c: int | str | mp.mpf, item: PrimePower, N: int) -> mp.matrix:
    """Exact-form q contribution to Q_N(c) in full indices -N,...,N.

    Arithmetic is mpmath, so returned numerical entries are not interval balls.
    At c=q every entry is exactly zero in symbolic real arithmetic.
    """
    eps = edge_epsilon(c, item.q)
    weight = item.weight
    indices = list(range(-N, N + 1))
    block = mp.matrix(2 * N + 1)
    for i, n in enumerate(indices):
        for j in range(i, 2 * N + 1):
            m = indices[j]
            if n == m:
                value = -2 * weight * eps * mp.cos(2 * mp.pi * n * eps)
            else:
                value = -weight * (
                    mp.sin(2 * mp.pi * n * eps) - mp.sin(2 * mp.pi * m * eps)
                ) / (mp.pi * (n - m))
            block[i, j] = value
            block[j, i] = value
    return block


def prime_power_even_block(c: int | str | mp.mpf, item: PrimePower, N: int) -> mp.matrix:
    V = even_projector(N)
    return V.T * prime_power_full_block(c, item, N) * V


def edge_derivative_jump_even(item: PrimePower, N: int) -> mp.matrix:
    """Right-minus-left u=log(c) derivative jump at c=q."""
    r = endpoint_vector(N)
    return -(mp.mpf(2) / (item.exponent * mp.sqrt(item.q))) * (r * r.T)


def leading_moment_edge_term(
    v: mp.matrix, item: PrimePower, epsilon: mp.mpf, vanished_through: int
) -> mp.mpf:
    """Leading q-Rayleigh term after M_0,...,M_s vanish.

    For s=vanished_through, the first retained moment is M_{s+1}; the q
    contribution is negative and has order epsilon^(4s+5).
    """
    s = vanished_through
    if s < 0:
        raise ValueError("vanished_through must be nonnegative")
    moment = even_moment(v, s + 1)
    coefficient = (
        -item.weight
        * 2
        * (2 * mp.pi) ** (4 * s + 4)
        * moment**2
        / mp.factorial(4 * s + 5)
    )
    return coefficient * epsilon ** (4 * s + 5)


def _geometric_sums(n: int, L: mp.mpf, target: mp.mpf) -> tuple[mp.mpf, ...]:
    w = 2 * mp.pi * n / L
    w2 = w * w
    ratio = mp.exp(-2 * L)
    g_s = g_cc = g_x1 = g_x2 = mp.mpf(0)
    for k in range(1_000_000):
        c_k = mp.mpf(2 * k) + mp.mpf("0.5")
        e_k = mp.exp(-c_k * L)
        denominator = c_k * c_k + w2
        g_s += e_k / denominator
        if n:
            g_cc += e_k * w2 / (c_k * denominator)
        g_x1 += e_k * c_k / denominator
        g_x2 += e_k * (c_k * c_k - w2) / denominator**2
        c_next = c_k + 2
        envelope = mp.exp(-c_next * L) / (1 - ratio)
        if max(envelope / c_next, envelope / c_next**2) <= target:
            return g_s, g_cc, g_x1, g_x2
    raise RuntimeError("geometric correction sums did not converge")


def _closed_form_sequences(c: mp.mpf, N: int, dps: int) -> tuple[list[mp.mpf], ...]:
    L = mp.log(c)
    quarter = mp.mpf("0.25")
    psi_quarter = mp.digamma(quarter)
    target = mp.power(10, -(dps - 15))
    S: list[mp.mpf] = []
    CC: list[mp.mpf] = []
    XC: list[mp.mpf] = []
    for n in range(N + 1):
        w = 2 * mp.pi * n / L
        g_s, g_cc, g_x1, g_x2 = _geometric_sums(n, L, target)
        z = mp.mpc(quarter, mp.pi * n / L)
        psi = mp.digamma(z)
        psi1 = mp.polygamma(1, z)
        S.append(mp.mpf(0) if n == 0 else mp.im(psi) / 2 - w * g_s)
        CC.append(mp.mpf(0) if n == 0 else -(mp.re(psi) - psi_quarter) / 2 + g_cc)
        XC.append(mp.re(psi1) / 4 - L * g_x1 - g_x2)
    return S, CC, XC, L


def build_cutoff_free_even_matrix(
    c: int | str | mp.mpf, N: int, *, dps: int = 80
) -> mp.matrix:
    """Independent mpmath construction of the cutoff-free even block."""
    if N < 1 or dps < 30:
        raise ValueError("require N>=1 and dps>=30")
    with mp.workdps(dps):
        c_value = mp.mpf(c)
        if not mp.isfinite(c_value) or c_value <= 1:
            raise ValueError("c must be finite and greater than 1")
        S, CC, XC, L = _closed_form_sequences(c_value, N, dps)
        indices = list(range(-N, N + 1))
        signed_S = [S[n] if n >= 0 else -S[-n] for n in indices]
        L2 = L * L
        sixteen_pi_sq = 16 * mp.pi**2
        prefactor = 32 * L * mp.sinh(L / 4) ** 2
        U = mp.exp(L / 2)
        J = -2 * mp.log(U + 1) + mp.log(U * U + 1) + 2 * mp.atan(U) + mp.log(2) - mp.pi / 2
        kappa = mp.log(4 * mp.pi * (mp.exp(L) - 1) / (mp.exp(L) + 1)) + mp.euler

        source = [mp.mpf(0)] * (2 * N + 1)
        source_derivative = [mp.mpf(0)] * (2 * N + 1)
        for item in prime_powers_up_to(c_value):
            y = mp.log(item.q)
            t = y / L
            weight = item.weight
            for i, n in enumerate(indices):
                source[i] += weight * mp.sin(2 * mp.pi * n * t)
                source_derivative[i] += 2 * weight * (1 - t) * mp.cos(2 * mp.pi * n * t)

        full = mp.matrix(2 * N + 1)
        for i, n in enumerate(indices):
            for j in range(i, 2 * N + 1):
                m = indices[j]
                w_02 = prefactor * (L2 - sixteen_pi_sq * n * m) / (
                    (L2 + sixteen_pi_sq * n * n) * (L2 + sixteen_pi_sq * m * m)
                )
                if n == m:
                    w_r = kappa + 2 * CC[abs(n)] + J - (2 / L) * XC[abs(n)]
                    w_p = source_derivative[i]
                else:
                    denominator = mp.pi * (m - n)
                    w_r = (signed_S[i] - signed_S[j]) / denominator
                    w_p = (source[i] - source[j]) / denominator
                full[i, j] = w_02 - w_r - w_p
                full[j, i] = full[i, j]
        V = even_projector(N)
        return +(V.T * full * V)


def smallest_even_eigenpair(c: int | str | mp.mpf, N: int, *, dps: int) -> tuple[mp.mpf, mp.matrix]:
    with mp.workdps(dps):
        matrix = build_cutoff_free_even_matrix(c, N, dps=dps)
        eigenvalues, eigenvectors = mp.eigsy(matrix)
        return +eigenvalues[0], +eigenvectors[:, 0]


def prime_power_values(limit: int) -> list[int]:
    return sorted({item.q for item in prime_powers_up_to(limit)})


def scan_edges(
    *, limit: int, bands: Iterable[int], fractions: Iterable[str], dps: int
) -> dict:
    values = prime_power_values(limit)
    extended = prime_power_values(2 * limit + 100)
    fraction_values = [mp.mpf(value) for value in fractions]
    cells: list[dict] = []
    for q in values:
        q_next = next(value for value in extended if value > q)
        gap = mp.log(mp.mpf(q_next) / q)
        for N in bands:
            for fraction in fraction_values:
                delta = fraction * gap
                c = mp.mpf(q) * mp.exp(delta)
                lam, v = smallest_even_eigenpair(c, N, dps=dps)
                cells.append(
                    {
                        "q": q,
                        "next_prime_power": q_next,
                        "fraction": mp.nstr(fraction, 20),
                        "delta_log_c": mp.nstr(delta, 30),
                        "c": mp.nstr(c, 40),
                        "N": N,
                        "minimum_even_eigenvalue": mp.nstr(lam, dps),
                        "endpoint_moment_M0": mp.nstr(even_moment(v, 0), min(dps, 50)),
                        "classification": "EMPIRICAL_NEGATIVE" if lam < 0 else "EMPIRICAL_NONNEGATIVE",
                    }
                )
    negatives = [cell for cell in cells if cell["classification"] == "EMPIRICAL_NEGATIVE"]
    return {
        "experiment_id": EXPERIMENT_ID,
        "implementation_version": IMPLEMENTATION_VERSION,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "parameters": {
            "limit": limit,
            "bands": list(bands),
            "fractions": [str(value) for value in fractions],
            "dps": dps,
        },
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "mpmath": mp.__version__,
        },
        "summary": {
            "cells": len(cells),
            "empirical_negative_cells": len(negatives),
        },
        "cells": cells,
        "warning": "Ordinary mpmath signs are discovery output, not proof certificates.",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--bands", nargs="+", type=int, default=[4, 8, 12])
    parser.add_argument(
        "--fractions",
        nargs="+",
        default=["0", "0.02", "0.05", "0.1", "0.2", "0.35", "0.5", "0.65", "0.8", "0.92", "0.98"],
    )
    parser.add_argument("--dps", type=int, default=85)
    parser.add_argument("--output", type=Path, default=None)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.limit < 2:
        raise SystemExit("--limit must be at least 2")
    result = scan_edges(limit=args.limit, bands=args.bands, fractions=args.fractions, dps=args.dps)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
