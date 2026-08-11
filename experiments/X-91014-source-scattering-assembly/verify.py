#!/usr/bin/env python3
"""Finite checks for L-91014 through L-91018.

The replay checks exact finite coefficient identities and high-precision
analytic controls.  It does not prove the critical-boundary intertwiner, the
dyadic gate, or RH.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp

mp.mp.dps = 70


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n: int) -> list[int]:
    ds = [1]
    for p, e in factor(n).items():
        ds = [d * p**j for d in ds for j in range(e + 1)]
    return sorted(ds)


def q_fraction(A: int, n: int) -> Fraction:
    """q_a(n), with A=2a a positive integer."""
    ans = Fraction(1)
    for p in factor(n):
        ans *= 1 - Fraction(1, p**A)
    return ans


def q_mp(a: mp.mpf, n: int) -> mp.mpf:
    ans = mp.mpf(1)
    for p in factor(n):
        ans *= 1 - mp.power(p, -2 * a)
    return ans


def Q(a: mp.mpf, s: mp.mpc) -> mp.mpc:
    return mp.zeta(s) / mp.zeta(s + 2 * a)


def kappa(a: mp.mpf) -> mp.mpf:
    return 1 / mp.zeta(1 + 2 * a)


def H(a: mp.mpf, s: mp.mpc) -> mp.mpc:
    return Q(a, s) - kappa(a) / (s - 1)


def allpass_matrix(v: mp.mpc) -> mp.matrix:
    c = mp.sqrt(mp.mpf(5) / 8)
    s = mp.sqrt(mp.mpf(3) / 8)
    K = mp.matrix([[0, -s, 0], [s, 0, -c], [0, c, 0]])
    I = mp.eye(3)
    return (I + v * K) * (I - v * K) ** -1


def allpass_first_column(v: mp.mpc) -> mp.matrix:
    den = 4 * (1 + v * v)
    return mp.matrix(
        [(4 + v * v) / den, 2 * mp.sqrt(6) * v / den, mp.sqrt(15) * v * v / den]
    )


def phi(a: mp.mpf, t: mp.mpf, x: mp.mpf) -> mp.matrix:
    phase = mp.e ** (-1j * x * t)
    p1 = 1j * mp.sqrt(6) * a / 3 * (mp.e ** (-a * t) - mp.e ** (-2 * a * t))
    p2 = mp.sqrt(15) * a / 6 * (-mp.e ** (-a * t) + 2 * mp.e ** (-2 * a * t))
    return phase * mp.matrix([p1, p2])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    checks = 0
    max_cocycle_error = Fraction(0)
    max_allpass_error = mp.mpf(0)
    max_signature_error = mp.mpf(0)
    max_recurrence_error = mp.mpf(0)
    max_tail_error = mp.mpf(0)

    # Exact coefficient cocycle and divisor probabilities.
    for A, B in [(1, 1), (1, 2), (2, 3), (3, 1)]:
        for n in range(1, 321):
            lhs = q_fraction(A + B, n)
            rhs = sum(
                q_fraction(A, d) * q_fraction(B, n // d) / Fraction((n // d) ** A)
                for d in divisors(n)
            )
            err = abs(lhs - rhs)
            max_cocycle_error = max(max_cocycle_error, err)
            assert err == 0
            if lhs:
                probs = [
                    q_fraction(A, d)
                    * q_fraction(B, n // d)
                    / Fraction((n // d) ** A)
                    / lhs
                    for d in divisors(n)
                ]
                assert all(p >= 0 for p in probs) and sum(probs) == 1
            checks += 2

    # Logarithmic coproduct on every factorisation.
    for n in range(1, 250):
        for d in divisors(n):
            e = n // d
            assert mp.almosteq(mp.log(n), mp.log(d) + mp.log(e))
            checks += 1

    # SO(3) first column, complex orthogonality, trace excess and scalar eigenchannel.
    for v in [mp.mpf("0.1"), mp.mpf("0.7"), mp.mpf("2.3"), mp.mpc("0.4", "-0.2")]:
        R = allpass_matrix(v)
        col = R[:, 0]
        expected = allpass_first_column(v)
        err = mp.norm(col - expected)
        max_allpass_error = max(max_allpass_error, err)
        assert err < mp.mpf("1e-60")
        ortho = R.T * R - mp.eye(3)
        err = mp.norm(ortho)
        max_allpass_error = max(max_allpass_error, err)
        assert err < mp.mpf("1e-60")
        assert abs(mp.det(R) - 1) < mp.mpf("1e-60")
        checks += 3

    signature_samples: list[dict[str, str]] = []
    for a, d, r in [
        (mp.mpf("0.7"), mp.mpf("0.2"), mp.mpf("0.0")),
        (mp.mpf("0.7"), mp.mpf("0.4"), mp.mpf("0.9")),
        (mp.mpf("1.3"), mp.mpf("0.49"), mp.mpf("2.1")),
    ]:
        z = mp.mpc(d, r)
        v = -1j * z / a
        R = allpass_matrix(v)
        gram = R.transpose_conj() * R
        trace_excess = mp.re(mp.trace(gram) - 3)
        closed = 16 * a * a * d * d / (((a - d) ** 2 + r * r) * ((a + d) ** 2 + r * r))
        err = abs(trace_excess - closed)
        max_signature_error = max(max_signature_error, err)
        assert err < mp.mpf("1e-55")
        beta = mp.sqrt(((a + d) ** 2 + r * r) / ((a - d) ** 2 + r * r))
        b = (a + z) / (a - z)
        assert abs(abs(b) - beta) < mp.mpf("1e-60")
        signature_samples.append(
            {"a": mp.nstr(a, 8), "d": mp.nstr(d, 8), "r": mp.nstr(r, 8), "beta": mp.nstr(beta, 20)}
        )
        checks += 2

    # Lyapunov depth integral.
    lyapunov_samples: list[dict[str, str]] = []
    for a, d in [(mp.mpf("0.3"), mp.mpf("0.1")), (mp.mpf("0.3"), mp.mpf("0.7")), (mp.mpf("1.1"), mp.mpf("0.4"))]:
        integral = mp.quad(
            lambda r: mp.mpf("0.5")
            * mp.log((r * r + (a + d) ** 2) / (r * r + (a - d) ** 2)),
            [-mp.inf, mp.inf],
        )
        expected = 2 * mp.pi * min(a, d)
        assert abs(integral - expected) < mp.mpf("1e-45")
        lyapunov_samples.append(
            {"a": mp.nstr(a, 8), "d": mp.nstr(d, 8), "integral": mp.nstr(integral, 22)}
        )
        checks += 1

    # Pole residue and pole-subtracted cocycle recurrence.
    for a, b in [(mp.mpf("0.21"), mp.mpf("0.34")), (mp.mpf("0.5"), mp.mpf("0.5"))]:
        residue_identity = kappa(a) * Q(b, 1 + 2 * a) - kappa(a + b)
        assert abs(residue_identity) < mp.mpf("1e-60")
        checks += 1
        for s in [mp.mpc("0.73", "0.41"), mp.mpc("1.27", "1.3"), mp.mpc("1.8", "0.2")]:
            D = (Q(b, s + 2 * a) - Q(b, 1 + 2 * a)) / (s - 1)
            rhs = H(a, s) * Q(b, s + 2 * a) + kappa(a) * D
            err = abs(H(a + b, s) - rhs) / max(mp.mpf(1), abs(rhs))
            max_recurrence_error = max(max_recurrence_error, err)
            assert err < mp.mpf("1e-55")
            checks += 1

    # Finite positive-tail identity.
    N = 160
    a = mp.mpf("0.37")
    b = mp.mpf("0.5")
    s = mp.mpc("0.68", "0.9")
    qvals = [mp.mpf(0)] + [q_mp(b, n) for n in range(1, N + 1)]
    Q_shift = mp.fsum(qvals[n] * n ** (-(s + 2 * a)) for n in range(1, N + 1))
    Q_anchor = mp.fsum(qvals[n] * n ** (-(1 + 2 * a)) for n in range(1, N + 1))
    lhs = (Q_shift - Q_anchor) / (s - 1)
    rhs = -mp.fsum(
        qvals[n]
        * n ** (-(1 + 2 * a))
        * (1 - mp.e ** (-(s - 1) * mp.log(n)))
        / (s - 1)
        for n in range(1, N + 1)
    )
    err = abs(lhs - rhs)
    max_tail_error = max(max_tail_error, err)
    assert err < mp.mpf("1e-60")
    checks += 1

    # Detail pointwise square identity and a finite positive carrier Gram.
    a = mp.mpf("0.43")
    for t in [mp.mpf("0.0"), mp.mpf("0.4"), mp.mpf("2.3"), mp.mpf("7.1")]:
        p = phi(a, t, mp.mpf("0.0"))
        lhs = mp.re((p.transpose_conj() * p)[0])
        rhs = a * a * (
            mp.mpf(13) / 12 * mp.e ** (-2 * a * t)
            - 3 * mp.e ** (-3 * a * t)
            + mp.mpf(7) / 3 * mp.e ** (-4 * a * t)
        )
        assert abs(lhs - rhs) < mp.mpf("1e-60")
        checks += 1

    atoms = [(mp.mpf("0.2"), mp.mpf("1.1")), (mp.mpf("0.9"), mp.mpf("0.7")), (mp.mpf("2.4"), mp.mpf("2.0"))]
    carriers = [mp.mpf("-0.8"), mp.mpf("0.1"), mp.mpf("1.7")]
    gram = mp.matrix(len(carriers))
    for i, x in enumerate(carriers):
        for j, y in enumerate(carriers):
            gram[i, j] = mp.fsum(
                weight * (phi(a, t, x).transpose_conj() * phi(a, t, y))[0]
                for t, weight in atoms
            )
    eigvals = mp.eigsy((gram + gram.transpose_conj()) / 2, eigvals_only=True)
    min_gram_eigenvalue = min(eigvals)
    assert min_gram_eigenvalue > -mp.mpf("1e-55")
    checks += len(carriers) ** 2

    result: dict[str, Any] = {
        "classification": "PASS_SOURCE_SCATTERING_COEFFICIENT_ONE_ASSEMBLY",
        "checks": checks,
        "max_exact_cocycle_error": str(max_cocycle_error),
        "max_allpass_error": mp.nstr(max_allpass_error, 12),
        "max_signature_error": mp.nstr(max_signature_error, 12),
        "max_pole_subtracted_recurrence_error": mp.nstr(max_recurrence_error, 12),
        "max_finite_tail_error": mp.nstr(max_tail_error, 12),
        "minimum_detail_gram_eigenvalue": mp.nstr(min_gram_eigenvalue, 12),
        "signature_samples": signature_samples,
        "lyapunov_samples": lyapunov_samples,
        "scope": "finite algebra and high-precision controls only; no critical-boundary intertwiner and no RH claim",
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print("PASS_SOURCE_SCATTERING_COEFFICIENT_ONE_ASSEMBLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
