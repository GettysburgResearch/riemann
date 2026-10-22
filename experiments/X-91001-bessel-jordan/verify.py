#!/usr/bin/env python3
"""Finite exact/high-precision checks for the Bessel--Hausdorff--Jordan continuation.

This is a regression suite for algebraic identities and synthetic controls only.
It does not establish any Riemann-data sign or prove RH.
"""
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import mpmath as mp
import numpy as np

mp.mp.dps = 70


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_shift(a: list[Fraction], m: int = 1) -> list[Fraction]:
    return [Fraction(0)] * m + a


def poly_scale(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return [c * x for x in a]


def poly_deriv(a: list[Fraction]) -> list[Fraction]:
    return [Fraction(i) * a[i] for i in range(1, len(a))] or [Fraction(0)]


def poly_eval(a: Iterable[Fraction], x: mp.mpf) -> mp.mpf:
    y = mp.mpf("0")
    for c in reversed(list(a)):
        y = y * x + mp.mpf(c.numerator) / c.denominator
    return y


def q_rows(max_k: int) -> list[list[Fraction]]:
    rows = [[Fraction(1), Fraction(1), Fraction(-1)]]
    for k in range(max_k):
        old = rows[-1]
        # (t+2k+3)Q - t Q'
        term = poly_add(poly_shift(old), poly_scale(old, Fraction(2 * k + 3)))
        term = poly_add(term, poly_scale(poly_shift(poly_deriv(old)), Fraction(-1)))
        rows.append(term)
    return rows


def theta_row(n: int) -> list[Fraction]:
    out: list[Fraction] = []
    for j in range(n + 1):
        c = Fraction(math.factorial(2 * n - j), math.factorial(j) * math.factorial(n - j) * 2 ** (n - j))
        out.append(c)
    return out


def p_row(q: list[Fraction], k: int) -> list[Fraction]:
    return poly_scale(q, Fraction(1, 2 ** (k + 1)))


def theta_eval(n: int, x: mp.mpf) -> mp.mpf:
    return poly_eval(theta_row(n), x)


def p_eval(rows: list[list[Fraction]], k: int, x: mp.mpf) -> mp.mpf:
    return poly_eval(p_row(rows[k], k), x)


def von_mangoldt(n: int) -> float:
    # log p iff n is a prime power, else 0.
    if n < 2:
        return 0.0
    m = n
    p = None
    d = 2
    while d * d <= m:
        if m % d == 0:
            p = d
            while m % d == 0:
                m //= d
            break
        d += 1 if d == 2 else 2
    if p is None:
        return math.log(n)  # prime
    if m != 1:
        return 0.0
    # ensure original n has no other prime factor (already m==1)
    return math.log(p)


def prime_factors(n: int) -> list[int]:
    fs: list[int] = []
    d = 2
    m = n
    while d * d <= m:
        if m % d == 0:
            fs.append(d)
            while m % d == 0:
                m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        fs.append(m)
    return fs


def jordan_u(n: int, u: mp.mpf) -> mp.mpf:
    if n == 1:
        return mp.mpf(1)
    val = mp.power(n, u)
    for p in prime_factors(n):
        val *= 1 - mp.power(p, -u)
    return val


def xi(s: mp.mpc) -> mp.mpc:
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def min_hermitian_eig(a: mp.matrix) -> mp.mpf:
    arr = np.array([[complex(a[i, j]) for j in range(a.cols)] for i in range(a.rows)], dtype=np.complex128)
    arr = (arr + arr.conj().T) / 2
    vals = np.linalg.eigvalsh(arr)
    return mp.mpf(float(vals.min()))


def main() -> dict:
    max_k = 24
    rows = q_rows(max_k + 3)

    # 1. Exact reverse-Bessel identity.
    reverse_checks = 0
    for k in range(max_k + 1):
        rhs = poly_add(theta_row(k + 1), poly_scale(poly_shift(theta_row(k), 2), Fraction(-1)))
        assert rows[k] == rhs
        reverse_checks += len(rows[k])

    # 2. Closed EGF against direct finite sum.
    egf_samples = [(mp.mpf("0.07"), mp.mpf("0.4")), (mp.mpf("0.31"), mp.mpf("1.7")), (mp.mpf("0.62"), mp.mpf("3.1"))]
    egf_max_error = mp.mpf(0)
    egf_terms = 250
    rows_long = q_rows(egf_terms)
    for uu, tt in egf_samples:
        direct = mp.fsum(p_eval(rows_long, k, tt) * uu**k / mp.factorial(k) for k in range(egf_terms))
        r = mp.sqrt(1 - uu)
        closed = mp.mpf("0.5") / r * mp.e**(tt * (1 - r)) * (r**-2 + tt / r - tt**2)
        egf_max_error = max(egf_max_error, abs(direct - closed))
    assert egf_max_error < mp.mpf("1e-45")

    # 3. Golden-ratio Poissonized boundary.
    phi = (1 + mp.sqrt(5)) / 2
    boundary_error = mp.mpf(0)
    for uu in [mp.mpf("0.1"), mp.mpf("0.4"), mp.mpf("0.72")]:
        r = mp.sqrt(1 - uu)
        tt = phi / r
        boundary_error = max(boundary_error, abs(1 + r * tt - r**2 * tt**2))
    assert boundary_error < mp.mpf("1e-65")

    # 4. GIG moment and signed-moment identities.
    gig_max_error = mp.mpf(0)
    gig_samples = 0
    for tt in [mp.mpf("0.5"), mp.mpf("1.3"), mp.mpf("2.7")]:
        for k in range(5):
            density = lambda q: mp.pi**(-mp.mpf("0.5")) * q**(-mp.mpf("0.5")) * mp.e**(-q - tt**2 / (4 * q))
            mom = mp.quad(lambda q: q**k * density(q), [0, 1, mp.inf])
            expected = mp.e**(-tt) * theta_eval(k, tt) / 2**k
            signed = mp.quad(lambda q: q**k * (q - tt**2 / 2) * density(q), [0, 1, mp.inf])
            expected_signed = mp.e**(-tt) * p_eval(rows, k, tt)
            gig_max_error = max(gig_max_error, abs(mom - expected), abs(signed - expected_signed))
            gig_samples += 2
    assert gig_max_error < mp.mpf("1e-50")

    # 5. Strict positive localizer and its Hankel Gram matrices.
    localizer_min = mp.inf
    hankel_min = mp.inf
    for tt in [mp.mpf("0.2"), mp.mpf("0.9"), mp.mpf("2.0"), mp.mpf("4.5")]:
        a = tt**2 / 2
        loc = []
        for k in range(9):
            val = p_eval(rows, k + 1, tt) - a * p_eval(rows, k, tt)
            localizer_min = min(localizer_min, val)
            loc.append(mp.e**(-tt) * val)
        assert min(loc) > 0
        d = 4
        H = mp.matrix(d, d)
        for i in range(d):
            for j in range(d):
                H[i, j] = loc[i + j]
        hankel_min = min(hankel_min, min_hermitian_eig(H))
    assert localizer_min > 0 and hankel_min > -mp.mpf("1e-55")

    # 6. Borel zero-kernel identity.
    borel_max_error = mp.mpf(0)
    for zz in [mp.mpc("0.2", "0.1"), mp.mpc("0", "0.7"), mp.mpc("0.35", "-0.4")]:
        for uu in [mp.mpf("0.05"), mp.mpf("0.3")]:
            direct = mp.fsum(
                (-2 * mp.factorial(k + 2) * zz**2 / (1 - zz**2)**(k + 3)) * uu**k / mp.factorial(k)
                for k in range(80)
            )
            closed = -4 * zz**2 / (1 - zz**2 - uu)**3
            borel_max_error = max(borel_max_error, abs(direct - closed))
    assert borel_max_error < mp.mpf("1e-35")

    # 7. Synthetic Hausdorff and false-pole controls.
    gammas = [mp.mpf("-3.2"), mp.mpf("-0.7"), mp.mpf("1.1"), mp.mpf("4.0")]
    x0 = mp.mpf("0.2")
    ak = []
    for k in range(14):
        ak.append(mp.fsum(2 * (g - x0)**2 / (1 + (g - x0)**2)**(k + 3) for g in gammas))
    hausdorff_min = mp.inf
    cur = ak[:]
    for m in range(7):
        sign = (-1) ** m
        for v in cur:
            hausdorff_min = min(hausdorff_min, sign * v)
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
    assert hausdorff_min > -mp.mpf("1e-60")

    y = mp.mpf("0.2")
    u0 = 1 - y**2
    false_borel = -8 * y**2 / (1 - y**2 - (u0 - mp.mpf("1e-4")))**3
    assert false_borel < 0

    # 8. Prime cross-Gram block is PSD for a finite prime-power packet.
    orders = [0, 1, 2]
    centers = [mp.mpf("0"), mp.mpf("0.6")]
    idx = [(i, x) for i in orders for x in centers]
    msz = len(idx)
    M = mp.matrix(msz, msz)
    C = mp.matrix(msz, msz)
    N = mp.matrix(msz, msz)
    for aa, (i, x) in enumerate(idx):
        for bb, (j, yv) in enumerate(idx):
            mval = mp.mpc(0)
            cval = mp.mpc(0)
            nval = mp.mpc(0)
            for n in range(2, 121):
                lm = von_mangoldt(n)
                if lm == 0:
                    continue
                tt = mp.log(n)
                wt = mp.mpf(lm) / mp.sqrt(n)
                phase = mp.e**(1j * (x - yv) * tt)
                a = tt**2 / 2
                def base(moment: int) -> mp.mpf:
                    return mp.e**(-tt) * theta_eval(moment, tt) / 2**moment
                mval += wt * phase * base(i + j)
                cval += wt * phase * (base(i + j + 1) - a * base(i + j))
                nval += wt * phase * (base(i + j + 2) - 2 * a * base(i + j + 1) + a**2 * base(i + j))
            M[aa, bb] = mval
            C[aa, bb] = cval
            N[aa, bb] = nval
    Block = mp.matrix(2 * msz, 2 * msz)
    for i in range(msz):
        for j in range(msz):
            Block[i, j] = M[i, j]
            Block[i, msz + j] = C[i, j]
            Block[msz + i, j] = mp.conj(C[j, i])
            Block[msz + i, msz + j] = N[i, j]
    block_min_eig = min_hermitian_eig(Block)
    assert block_min_eig > -mp.mpf("1e-45")

    # 9. Jordan quotient and compound-Poisson identity for finite primes.
    primes = [2, 3, 5]
    sigma = mp.mpf("2.3")
    ju = mp.mpf("0.4")
    xx = mp.mpf("0.7")
    def finite_ratio(s: mp.mpc) -> mp.mpc:
        out = mp.mpc(1)
        for p in primes:
            out *= (1 - mp.power(p, -s)) / (1 - mp.power(p, ju - s))
        return out
    lhs = finite_ratio(sigma + 1j * xx) / finite_ratio(sigma)
    log_rhs = mp.mpc(0)
    for p in primes:
        for rr in range(1, 150):
            intensity = mp.power(p, -rr * sigma) * (mp.power(p, rr * ju) - 1) / rr
            log_rhs += intensity * (mp.e**(-1j * xx * rr * mp.log(p)) - 1)
    rhs = mp.e**log_rhs
    compound_error = abs(lhs - rhs)
    assert compound_error < mp.mpf("1e-55")

    # Direct Jordan Dirichlet sum against the full finite-prime Euler product.
    # Enumerate exponents 0..18; tail is far below target precision at sigma-u=1.9.
    jordan_sum = mp.mpf(0)
    def rec(pos: int, n: int) -> None:
        nonlocal jordan_sum
        if pos == len(primes):
            jordan_sum += jordan_u(n, ju) / mp.power(n, sigma)
            return
        p = primes[pos]
        pp = 1
        for _ in range(30):
            rec(pos + 1, n * pp)
            pp *= p
    rec(0, 1)
    jordan_product = finite_ratio(sigma)
    jordan_error = abs(jordan_sum - jordan_product)
    assert jordan_error < mp.mpf("1e-15")

    # 10. Completed cocycle and boundary unitarity.
    cu = mp.mpf("0.2")
    cv = mp.mpf("0.13")
    ss = mp.mpc("1.4", "2.1")
    theta = lambda uu, s: xi(s - uu) / xi(s)
    cocycle_error = abs(theta(cu + cv, ss) - theta(cu, ss) * theta(cv, ss - cu))
    sb = mp.mpc((1 + cu) / 2, mp.mpf("3.7"))
    boundary_error_xi = abs(abs(theta(cu, sb)) - 1)
    assert cocycle_error < mp.mpf("1e-60") and boundary_error_xi < mp.mpf("1e-60")

    return {
        "status": "PASS_X_91001_BESSEL_HAUSDORFF_JORDAN",
        "scope": "Finite exact/high-precision identities and synthetic controls only; no Riemann-data sign and no RH claim.",
        "gates": {
            "reverse_bessel_identity": True,
            "closed_order_egf": True,
            "golden_ratio_boundary": True,
            "gig_moment_identity": True,
            "positive_localizer": True,
            "localizer_hankel_psd": True,
            "borel_cubic_kernel": True,
            "synthetic_hausdorff": True,
            "synthetic_false_pole": True,
            "prime_cross_gram_block_psd": True,
            "jordan_dirichlet_product": True,
            "compound_poisson_identity": True,
            "completed_cocycle": True,
            "completed_boundary_unitarity": True,
        },
        "reverse_coefficient_checks": reverse_checks,
        "egf_terms": egf_terms,
        "egf_max_error": float(egf_max_error),
        "golden_boundary_error": float(boundary_error),
        "gig_sample_count": gig_samples,
        "gig_max_error": float(gig_max_error),
        "localizer_min": float(localizer_min),
        "localizer_hankel_min_eigenvalue": float(hankel_min),
        "borel_max_error": float(borel_max_error),
        "hausdorff_min_slack": float(hausdorff_min),
        "synthetic_false_borel_value": float(false_borel),
        "prime_block_min_eigenvalue": float(block_min_eig),
        "compound_poisson_error": float(compound_error),
        "jordan_product_truncation_error": float(jordan_error),
        "completed_cocycle_error": float(cocycle_error),
        "completed_boundary_unitarity_error": float(boundary_error_xi),
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--json", type=Path, default=None)
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    print(result["status"])
