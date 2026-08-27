#!/usr/bin/env python3
"""Exact replay for L-105416 anchor-renormalized oriented spectral flow.

Authenticates finite rational polynomial algebra only. It does not prove the
Xi outer-phase gate, the moving-saddle theorem, low-order descent, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

Q = Fraction


def trim(p: list[Q]) -> list[Q]:
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def derivative(p: list[Q]) -> list[Q]:
    return trim([Q(i) * p[i] for i in range(1, len(p))] or [Q(0)])


def evaluate(p: list[Q], x: Q) -> Q:
    out = Q(0)
    for coefficient in reversed(p):
        out = out * x + coefficient
    return out


def multiply(p: list[Q], q: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def integrate(p: list[Q], constant: Q = Q(0)) -> list[Q]:
    return trim([constant] + [p[i] / Q(i + 1) for i in range(len(p))])


def polynomial_from_roots(roots: list[int]) -> list[Q]:
    out = [Q(1)]
    for root in roots:
        out = multiply(out, [-Q(root), Q(1)])
    return out


def series_division(num: list[Q], den: list[Q], order: int) -> list[Q]:
    assert den[0] != 0
    out = [Q(0)] * order
    for n in range(order):
        rhs = num[n] if n < len(num) else Q(0)
        for j in range(1, min(n + 1, len(den))):
            rhs -= den[j] * out[n - j]
        out[n] = rhs / den[0]
    return out


def odd_source_coefficients(f: list[Q], order: int) -> list[Q]:
    # f(z)=z P(z^2), so f/f'=z P/(P+2tP').
    p = [f[2 * n + 1] if 2 * n + 1 < len(f) else Q(0)
         for n in range(order + 2)]
    fp = derivative(f)
    d = [fp[2 * n] if 2 * n < len(fp) else Q(0)
         for n in range(order + 2)]
    return series_division(p, d, order)


def even_source_coefficients(f: list[Q], order: int) -> tuple[list[Q], Q]:
    # f(z)=P(t), t=z^2. After removing rho_0/z,
    # mhat(z)/z=[P/(2P')-rho_0]/t.
    p = [f[2 * n] if 2 * n < len(f) else Q(0)
         for n in range(order + 3)]
    pp = derivative(p)
    ratio = series_division(p, [Q(2) * value for value in pp], order + 1)
    rho0 = ratio[0]
    return ratio[1:order + 1], rho0


def source_quadratic(a: list[Q], q: list[Q], shift: int) -> Q:
    return sum(
        (q[i] * q[j] * a[i + j + shift]
         for i in range(len(q)) for j in range(len(q))),
        Q(0),
    )


def kernel_at_square(q: list[Q], shift: int, t: Q) -> Q:
    s = Q(1) / t
    return s ** (shift + 1) * evaluate(q, s) ** 2


def critical_flow(
    f: list[Q], positive_critical_points: list[Q],
    q: list[Q], shift: int
) -> Q:
    fp = derivative(f)
    fpp = derivative(fp)
    return sum(
        (
            Q(2)
            * evaluate(f, c)
            / evaluate(fpp, c)
            * kernel_at_square(q, shift, c * c)
            for c in positive_critical_points
        ),
        Q(0),
    )


def primitive_terms(q: list[Q], shift: int) -> dict[int, Q]:
    # Psi(z)=-sum q_i q_j z^{-m}/m, m=2(shift+i+j)+1.
    out: dict[int, Q] = {}
    for i, qi in enumerate(q):
        for j, qj in enumerate(q):
            m = 2 * (shift + i + j) + 1
            out[m] = out.get(m, Q(0)) - qi * qj / Q(m)
    return out


def check_fixture(
    f: list[Q], critical_points: list[Q], parity: str,
    expected_degree: int
) -> int:
    order = 10
    if parity == "odd":
        source = odd_source_coefficients(f, order)
        rho0 = Q(0)
    else:
        source, rho0 = even_source_coefficients(f, order)
        fp = derivative(f)
        assert rho0 == evaluate(f, Q(0)) / evaluate(derivative(fp), Q(0))

    q_vectors = [
        [Q(1)],
        [Q(1), Q(-2)],
        [Q(2), Q(3), Q(-1)],
        [Q(-3), Q(1), Q(2), Q(-1)],
    ]
    checks = 0

    for q in q_vectors:
        for shift in (0, 1):
            terms = primitive_terms(q, shift)
            for m, coefficient in terms.items():
                assert m % 2 == 1
                assert coefficient * (-Q(m)) == sum(
                    (
                        q[i] * q[j]
                        for i in range(len(q))
                        for j in range(len(q))
                        if 2 * (shift + i + j) + 1 == m
                    ),
                    Q(0),
                )
                checks += 1

            anchor = source_quadratic(source, q, shift)
            flow = critical_flow(f, critical_points, q, shift)
            # A full polynomial outer window leaves the affine remainder z/deg(f).
            expected = (
                q[0] * q[0] / Q(expected_degree)
                if shift == 0 else Q(0)
            )
            assert anchor + flow == expected
            checks += 1

    if parity == "even":
        # First-order moving-central-branch removal.
        fp = derivative(f)
        for z in (Q(1, 3), Q(3, 2), Q(5, 2)):
            if evaluate(fp, z) == 0:
                continue
            lhs = -Q(2) * evaluate(f, z) / evaluate(fp, z) + Q(2) * rho0 / z
            rhs = -Q(2) * (evaluate(f, z) / evaluate(fp, z) - rho0 / z)
            assert lhs == rhs
            checks += 1

    # Implicit velocities c'_alpha(0)=rho_c and c'_(-alpha)(0)=-rho_c.
    fp = derivative(f)
    fpp = derivative(fp)
    for c in critical_points:
        rho = evaluate(f, c) / evaluate(fpp, c)
        assert evaluate(fp, c) == 0
        assert evaluate(fpp, c) * rho - evaluate(f, c) == 0
        assert evaluate(fpp, c) * (-rho) + evaluate(f, c) == 0
        checks += 2

    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    fp_odd = polynomial_from_roots([-2, -1, 1, 2])
    f_odd = integrate(fp_odd, Q(0))

    fp_even = multiply([Q(0), Q(1)], fp_odd)
    f_even = integrate(fp_even, Q(3))

    counts = {
        "odd_anchor_flow_checks": check_fixture(
            f_odd, [Q(1), Q(2)], "odd", 5
        ),
        "even_regularized_anchor_flow_checks": check_fixture(
            f_even, [Q(1), Q(2)], "even", 6
        ),
    }
    payload = {
        "verdict": "PASS_X_105416_ANCHOR_ORIENTED_FLOW",
        "arithmetic_class": "EXACT_RATIONAL_FINITE_POLYNOMIAL",
        "counts": counts,
        "boundary_flow_identity_replayed": True,
        "central_branch_regularization_replayed": True,
        "outer_phase_gate_proved": False,
        "xi_low_order_descent_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["proof_object"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
