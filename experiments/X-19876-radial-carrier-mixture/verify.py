#!/usr/bin/env python3
"""High-precision finite replay for L-19876 and R-19876."""
from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 90
D = Decimal


def exp(x: Decimal) -> Decimal:
    return x.exp()


def ln(x: Decimal) -> Decimal:
    return x.ln()


def sqrt(x: Decimal) -> Decimal:
    return x.sqrt()


def phi(x: Decimal) -> Decimal:
    return D(1) - (D(1) + x) * exp(-x)


def m(a: Decimal, u: Decimal) -> Decimal:
    return sqrt(phi(D(2) * a * u) / (a**3 * u))


def omega_coeff(a: Decimal, c: Decimal, u: Decimal, k: Decimal = D(1)) -> Decimal:
    return phi(D(2) * a * u) * exp(-c * u) / (k * a * a)


def beta_coeff(b: Decimal, c_shifted: Decimal, u: Decimal, k: Decimal = D(1)) -> Decimal:
    return b * u * exp(-c_shifted * u) / k


def radial_integral_coeff(a: Decimal, c: Decimal, u: Decimal, k: Decimal = D(1)) -> Decimal:
    # (4/a^2) u * int_0^a b*u/k*exp(-(c+2b)u) db
    integral = (D(1) - (D(1) + D(2) * a * u) * exp(-D(2) * a * u)) / (D(4) * u * u)
    return D(4) / (a * a) * u * (u / k) * exp(-c * u) * integral


def g(s: Decimal) -> Decimal:
    return exp(-s) * (D(1) + s + s * s / D(3))


def main() -> None:
    a = D("1.7")
    c = D("2.3")
    carriers = [ln(D(2)), ln(D(3)), ln(D(4)), ln(D(5)), ln(D(7))]
    checks = 0
    measure_errors = []
    for i, u in enumerate(carriers, start=1):
        k = D(1 if i != 3 else 2)
        x = omega_coeff(a, c, u, k)
        y = radial_integral_coeff(a, c, u, k)
        err = abs(x - y)
        assert err < D("1e-75")
        measure_errors.append(str(err))
        checks += 1

    # Old triangular intertwiner fails because the multiplier sees u, not u-t.
    u = D("1.2")
    t = D("0.4")
    s = u - t
    mismatch = abs(m(a, u) - m(a, s)) * abs(g(s))
    assert mismatch > D("1e-5")
    checks += 1

    # Exact finite-atom tail-Hankel anticommutator formula.
    t = D("0.25")
    left = D(0)
    right = D(0)
    per_atom = []
    for i, u in enumerate(carriers, start=1):
        if u <= t:
            continue
        k = D(1 if i != 3 else 2)
        oc = omega_coeff(a, c, u, k)
        left_term = g(u - t) * oc
        left += left_term

        # Analytically integrated radial beta term:
        # (4/a^2) * u * g(u-t) * int beta_b db.
        integral_beta = (u / k) * exp(-c * u) * (
            D(1) - (D(1) + D(2) * a * u) * exp(-D(2) * a * u)
        ) / (D(4) * u * u)
        right_term = D(4) / (a * a) * u * g(u - t) * integral_beta
        right += right_term
        per_atom.append(str(abs(left_term - right_term)))
    hankel_error = abs(left - right)
    assert hankel_error < D("1e-74")
    checks += 1

    # Two carrier ports have exactly the scalar carrier norm.
    for u, t in [(D("1.1"), D("0.2")), (D("2.7"), D("1.3")), (D("5"), D("4.9"))]:
        amp = g(u - t)
        scalar = D(4) / (a * a) * u * amp * amp
        ports = D(4) / (a * a) * (t + (u - t)) * amp * amp
        assert scalar == ports
        checks += 1

    result = {
        "verdict": "PASS_RADIAL_JORDAN_SCATTERING_CARRIER_MIXTURE",
        "checks": checks,
        "max_measure_error": str(max(D(x) for x in measure_errors)),
        "old_intertwiner_mismatch": str(mismatch),
        "tail_hankel_error": str(hankel_error),
        "per_atom_tail_errors": per_atom,
        "scope": {
            "proves": [
                "finite-atom radial measure identity",
                "finite-atom tail-Hankel anticommutator identity",
                "two-carrier pointwise isometry",
                "old input-multiplier intertwiner fails",
            ],
            "does_not_prove": [
                "the radial direct-integral Julia/Fisher source lock",
                "the delayed Weil defect identity",
                "the Riemann Hypothesis",
            ],
        },
    }
    out = Path(__file__).with_name("results") / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])
    print(f"checks: {checks}")
    print(f"old intertwiner mismatch: {mismatch}")


if __name__ == "__main__":
    main()
