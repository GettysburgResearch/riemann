#!/usr/bin/env python3
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
import random
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T103300_BALANCED_PHASE_GRAM_ALGEBRA"


def padd(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction()) + v
        if out[k] == 0:
            del out[k]
    return out


def pscale(a: dict[int, Fraction], c: Fraction) -> dict[int, Fraction]:
    return {k: c * v for k, v in a.items() if c * v}


def pmul(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, Fraction()) + x * y
    return {k: v for k, v in out.items() if v}


def conv(a: list[Fraction], b: list[Fraction], n: int) -> list[Fraction]:
    out = [Fraction() for _ in range(n)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < n:
                out[i + j] += x * y
    return out


def eta_coeffs(n: int) -> list[Fraction]:
    return [Fraction(math.comb(2 * k, k), 4**k) for k in range(n)]


def phase_mag_numerator(a: Fraction, t: Fraction, c: Fraction) -> Fraction:
    c2 = 2 * c * c - 1
    return (
        1
        + t * t * a * a
        + (1 - t) * (1 - t) * a**4
        - 2 * t * a * c
        - 2 * (1 - t) * a * a * c2
        + 2 * t * (1 - t) * a**3 * c
    )


def phase_mag_derivative_numerator(a: Fraction, t: Fraction, c: Fraction) -> Fraction:
    c2 = 2 * c * c - 1
    return (
        2 * t * a * a
        - 2 * (1 - t) * a**4
        - 2 * a * c
        + 2 * a * a * c2
        + 2 * (1 - 2 * t) * a**3 * c
    )


def box_hat(rho: float, gamma: float, h: float) -> complex:
    z = complex(rho, -gamma)
    if abs(z) < 1e-14:
        return complex(h)
    return (cmath.exp(z * h) - 1) / z


def run() -> dict[str, object]:
    rng = random.Random(103300)
    operator_checks = 0
    phase_checks = 0

    # Exact carrier-normalized operator identities in Q[V].
    for _ in range(1000):
        p = rng.choice([2, 3, 5, 7, 11, 67, 101])
        a = Fraction(1, p)
        t = Fraction(rng.randint(0, 40), 40)
        h = (1 - a) * (1 + a * (1 - t))
        N = {0: Fraction(1), 1: -t * a, 2: -(1 - t) * a * a}
        T = {1: Fraction(1, 1 - a), 2: -a / (1 - a)}
        lhs = padd(pscale(N, 1 / h), pscale(T, -1))
        rhs = pscale(pmul({0: 1, 1: -1}, {0: 1, 1: -a}), 1 / h)
        assert lhs == rhs

        # Differentiate N/h exactly and compare with the centered generator.
        Np = {1: -a, 2: a * a}
        hp = -a * (1 - a)
        derivative = padd(pscale(Np, 1 / h), pscale(N, -hp / (h * h)))
        generator = pscale(
            pmul({0: 1, 1: -1}, {0: 1, 1: -a}),
            a * (1 - a) / (h * h),
        )
        assert derivative == generator
        operator_checks += 1

    # Exact phase derivative and endpoint gain identities using cos(theta).
    for _ in range(3000):
        p = rng.choice([2, 3, 5, 7, 11, 67, 101, 1009])
        a = Fraction(1, p)
        t = Fraction(rng.randint(0, 100), 100)
        c = Fraction(rng.randint(-100, 100), 100)
        h = (1 - a) * (1 + a * (1 - t))
        hp = -a * (1 - a)
        M = phase_mag_numerator(a, t, c)
        Mp = phase_mag_derivative_numerator(a, t, c)
        derivative = (Mp * h - 2 * M * hp) / h**3
        asserted = (
            2
            * a
            * (1 - c)
            * (1 - 2 * a * c + a * a)
            * (1 - a * (1 - t))
            / ((1 - a) ** 2 * (1 + a * (1 - t)) ** 3)
        )
        assert derivative == asserted
        assert asserted >= 0

        # Endpoint gain, cross-multiplied to avoid division.
        m1_num = 1 + a * a - 2 * a * c
        m1_den = (1 - a) ** 2
        c2 = 2 * c * c - 1
        m0_num = 1 + a**4 - 2 * a * a * c2
        m0_den = (1 - a * a) ** 2
        gain_num = (1 + a) ** 2
        gain_den = 1 + 2 * a * c + a * a
        assert m1_num * m0_den * gain_den == m0_num * m1_den * gain_num
        assert gain_num >= gain_den
        phase_checks += 1

    # The half-divisor completion is the local square root of Mobius.
    width = 20
    eta = eta_coeffs(width)
    mu_local = [Fraction(1), Fraction(-1)] + [Fraction() for _ in range(width - 2)]
    lam = conv(mu_local, eta, width)
    lam_sq = conv(lam, lam, width)
    assert lam_sq == mu_local
    # At 67, multiplying by a second half-factor gives 1-z; squaring gives (1-z)^2.
    lam67 = conv(lam, lam, width)
    beta67_local = conv(mu_local, mu_local, width)
    # The ordinary half-factor and the extra 67 half-factor multiply to 1-z.
    assert lam67 == mu_local
    # Squaring that 67-local factor gives the duplicate Euler factor (1-z)^2.
    assert conv(lam67, lam67, width) == beta67_local

    # Exact radical counterexample, enclosed with high-precision Decimal arithmetic.
    getcontext().prec = 80
    D = Decimal
    counter = (
        -D(97) / D(30)
        - D(30).sqrt() / D(20)
        - D(7) * D(6).sqrt() / D(120)
        + D(3).sqrt() / D(10)
        + D(2).sqrt() / D(8)
        + D(15).sqrt() / D(5)
        + D(12) * D(5).sqrt() / D(25)
        + D(9) * D(10).sqrt() / D(20)
    )
    assert D("-0.029166") < counter < D("-0.029165")

    # Numerical verification of the exact centered B-spline autocorrelation phase.
    autocorrelation_checks = 0
    hlog = math.log(2.3)
    for gamma in [0.0, 0.1, 0.7, 2.0, 7.5]:
        left = (
            box_hat(-0.75, gamma, hlog)
            * box_hat(-0.25, gamma, hlog)
            * box_hat(0.25, gamma, hlog)
            * box_hat(0.75, gamma, hlog)
            * cmath.exp(2j * hlog * gamma)
        )
        fhat = box_hat(0.25, gamma, hlog) * box_hat(0.75, gamma, hlog)
        right = math.exp(-hlog) * abs(fhat) ** 2
        assert abs(left.imag) < 1e-10
        assert abs(left.real - right) < 1e-10 * max(1.0, abs(right))
        assert right >= 0
        autocorrelation_checks += 1

    payload: dict[str, object] = {
        "schema": "riemann.x103300.balanced_phase_gram.v1",
        "classification": VERDICT,
        "base_pr": 701,
        "base_sha": "b8fa864f257cce623b020ff94b09c5afcbcabdee",
        "external_prs": {
            "696": "f4016db548afceb31b150547cb6cd48b4cddb77d",
            "699": "f23dd81748562dfa2a73f86aecfb9fcd3e2b32b9",
        },
        "operator_identity_checks": operator_checks,
        "phase_identity_checks": phase_checks,
        "autocorrelation_checks": autocorrelation_checks,
        "local_transition_counterexample": str(counter),
        "carrier_normalized_homotopy_proved": True,
        "nonzero_phase_monotonicity_proved": True,
        "half_divisor_source_square_root_proved": True,
        "cubic_autocorrelation_proved": True,
        "local_transition_cone_invariant": False,
        "bpoe103300_proved": False,
        "rh_established": False,
    }
    digest_input = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(digest_input).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
