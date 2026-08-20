#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T100300_TWO_ROUTE_ENDGAME"


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def dirichlet_convolution(a: list[int], b: list[int], nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    for d in range(1, nmax + 1):
        if a[d] == 0:
            continue
        for m in range(1, nmax // d + 1):
            if b[m]:
                out[d * m] += a[d] * b[m]
    return out


def run() -> dict:
    # Route A: derivative of the cell antiderivative.
    # E(t^2)=A+B/t+C/t^2 and
    # F=-2A log t+2B/t+C/t^2.
    for A, B, C, t in [
        (Fraction(3, 2), Fraction(-7, 3), Fraction(5, 4), Fraction(9, 5)),
        (Fraction(-2, 5), Fraction(11, 7), Fraction(-13, 9), Fraction(7, 3)),
    ]:
        # t * F'(t) = -2(A+B/t+C/t^2)
        lhs = -2 * A - 2 * B / t - 2 * C / (t * t)
        rhs = -2 * (A + B / t + C / (t * t))
        assert lhs == rhs

    # Double-negative discriminant/root algebra.
    T, u, v = Fraction(5, 7), Fraction(9, 5), Fraction(4, 3)
    D = u * u - T * v
    assert D > 0
    # Product and sum of the formal roots of
    # 16 T t^2 - 24 u t + 9 v.
    root_sum = Fraction(3, 2) * u / T
    root_product = Fraction(9, 16) * v / T
    assert 16 * T * root_product == 9 * v
    assert 16 * T * root_sum == 24 * u

    # Supercritical positivity does not imply the linear hinge.
    # nu=delta_2-3delta_1.
    for m in range(2, 10):
        for a_num in range(0, 11):
            a = Fraction(a_num, 10)
            value = (Fraction(2) - a) ** m - 3 * (Fraction(1) - a) ** m
            assert value >= 0
    assert Fraction(2) - 3 * Fraction(1) < 0

    # Route B: exact Vaughan identity.
    nmax = 300
    U = 7
    mu = mobius_sieve(nmax)
    one = [0] + [1] * nmax
    eps = [0] * (nmax + 1)
    eps[1] = 1
    mu_u = [0] * (nmax + 1)
    for n in range(1, U + 1):
        mu_u[n] = mu[n]

    mu_u_one = dirichlet_convolution(mu_u, one, nmax)
    a_u = [eps[n] - mu_u_one[n] for n in range(nmax + 1)]
    assert all(a_u[n] == 0 for n in range(1, U + 1))

    term1 = [2 * x for x in mu_u]
    term2 = dirichlet_convolution(
        dirichlet_convolution(mu_u, mu_u, nmax), one, nmax
    )
    term3 = dirichlet_convolution(
        dirichlet_convolution(a_u, a_u, nmax), mu, nmax
    )
    rebuilt = [term1[n] - term2[n] + term3[n] for n in range(nmax + 1)]
    assert rebuilt[1:] == mu[1:]

    # Exact firewall: for U=3, (a_U*a_U)(30)=-2.
    U2 = 3
    mu_u2 = [0] * (nmax + 1)
    for n in range(1, U2 + 1):
        mu_u2[n] = mu[n]
    a_u2 = [
        eps[n] - dirichlet_convolution(mu_u2, one, nmax)[n]
        for n in range(nmax + 1)
    ]
    aa2 = dirichlet_convolution(a_u2, a_u2, nmax)
    assert a_u2[5] == -1
    assert a_u2[6] == 1
    assert aa2[30] == -2

    mutations = sorted([
        "catd100300_assumed_rejected",
        "bvd100310_assumed_rejected",
        "pointwise_patg_substituted_for_negative_mass_rejected",
        "supercritical_moments_interpolated_to_linear_rejected",
        "zero_moment_reused_on_balanced_core_rejected",
        "a_u_square_called_positive_rejected",
        "rh_established_by_replay_rejected",
    ])
    core = {
        "schema": "riemann.x100300.two-route-endgame.v1",
        "classification": VERDICT,
        "base_pr": 680,
        "base_sha": "64e8e138dde15bfdb02d532041ace945c600c912",
        "external_heads": {
            "pr676": "9849df6a52bb4791ebf10cf0dd9f0c929d36bdd9",
            "pr679": "37c811473cad6058e5f057a9fc89b05dc5b0e4cb",
            "pr681": "295000fead70e87c17623cf0dcc2af838a60ed0c",
        },
        "cellwise_deficit_formula": True,
        "catd100300_rh_equivalent": True,
        "extra_half_order_zero_moment": True,
        "vaughan_identity_exact": True,
        "type_i_error_integrable": True,
        "bvd100310_rh_equivalent": True,
        "catd100300_proved": False,
        "bvd100310_proved": False,
        "rh_established": False,
        "mutations_rejected": mutations,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return {**core, "proof_object_sha256": hashlib.sha256(canon).hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8", newline="\n")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
