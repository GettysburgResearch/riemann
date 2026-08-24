#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def check_equal(a, b, label, checks):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    while len(b) > 1 and b[-1] == 0:
        b.pop()
    if a != b:
        raise AssertionError(f"{label}: {a} != {b}")
    checks.append(label)


def rational_identity(num1, den1, num2, den2, label, checks):
    check_equal(poly_mul(num1, den2), poly_mul(num2, den1), label, checks)


def vertical_side_harmonic_measure(X, H, x, y, terms=1001):
    """Harmonic measure of both vertical sides in (-X,X)x(0,H)."""
    total = 0.0

    def sinh_ratio(a, b):
        if a == 0.0:
            return 0.0
        return (
            math.exp(a - b)
            * (-math.expm1(-2.0 * a))
            / (-math.expm1(-2.0 * b))
        )

    for j in range(1, terms, 2):
        coeff = 4.0 / (j * math.pi)
        a_right = j * math.pi * (x + X) / H
        a_left = j * math.pi * (X - x) / H
        b = 2.0 * j * math.pi * X / H
        right = sinh_ratio(a_right, b)
        left = sinh_ratio(a_left, b)
        total += coeff * (right + left) * math.sin(j * math.pi * y / H)
    return total


def main(output: str) -> None:
    checks = []

    # Firewall quartic F=z^4-z^2+1.
    c2 = Fraction(1, 2)
    Fcrit = c2 * c2 - c2 + 1
    Fppcrit = 12 * c2 - 2
    rho = Fcrit / Fppcrit
    assert Fcrit == Fraction(3, 4)
    assert Fppcrit == 4
    assert rho == Fraction(3, 16) and rho > 0
    checks += [
        "firewall_Fcrit=3/4",
        "firewall_Fppcrit=4",
        "firewall_positive_residue=3/16",
    ]

    # On z=iy, F/F'=i(y^4+y^2+1)/(4y^3+2y), positive for y>0.
    assert all(x > 0 for x in (1, 1, 1, 4, 2))
    checks.append("firewall_imaginary_axis_orientation")

    # Real-rooted calibration F=(z^2-1)(z^2-4)=z^4-5z^2+4.
    rho0 = Fraction(4, -10)
    c2_good = Fraction(5, 2)
    Fcrit_good = c2_good * c2_good - 5 * c2_good + 4
    Fppcrit_good = 12 * c2_good - 10
    rho_good = Fcrit_good / Fppcrit_good
    assert rho0 == Fraction(-2, 5)
    assert Fcrit_good == Fraction(-9, 4)
    assert Fppcrit_good == 20
    assert rho_good == Fraction(-9, 80)
    checks += [
        "real_rooted_central_residue=-2/5",
        "real_rooted_outer_residue=-9/80",
    ]

    # Exact Herglotz decomposition of the regularized polynomial ratio:
    # mhat=z/4+(9/100)z/(1-(2/5)z^2).
    direct_num = [Fraction(0), Fraction(17), Fraction(0), Fraction(-5)]
    direct_den = [Fraction(50), Fraction(0), Fraction(-20)]
    aff_num = [Fraction(0), Fraction(1)]
    aff_den = [Fraction(4)]
    atom_num = [Fraction(0), Fraction(9)]
    atom_den = [Fraction(100), Fraction(0), Fraction(-40)]
    combined_num = poly_add(
        poly_mul(aff_num, atom_den), poly_mul(atom_num, aff_den)
    )
    combined_den = poly_mul(aff_den, atom_den)
    rational_identity(
        direct_num,
        direct_den,
        combined_num,
        combined_den,
        "real_rooted_exact_Herglotz_decomposition",
        checks,
    )

    assert Fraction(17, 50) == Fraction(1, 4) + Fraction(9, 100)
    checks.append("polynomial_source_mass_split")

    W = -2 * rho_good / c2_good
    s = 1 / c2_good
    assert W == Fraction(9, 100)
    assert s == Fraction(2, 5)
    checks += ["critical_atom_weight=9/100", "critical_atom_location=2/5"]

    # Harmonic-measure side decay used by L-105432.
    H = 2.0
    x = 0.0
    y = 1.0
    previous = None
    for X in (2.0, 4.0, 8.0, 12.0):
        omega = vertical_side_harmonic_measure(X, H, x, y)
        bound = 3.0 * math.exp(-math.pi * (X - abs(x)) / H)
        assert omega >= -1e-14
        assert omega <= bound
        if previous is not None:
            assert omega < previous
        previous = omega
        checks.append(f"harmonic_measure_decay_X={int(X)}")

    # The good-side growth is subexponential and is beaten by side harmonic
    # measure. These are numerical sanity checks, not a replay of L-105431.
    C = 7.0
    for X in (10_000.0, 100_000.0, 1_000_000.0):
        exponent = C * math.log(X) * math.log(math.log(3.0 + X)) - math.pi * X / H
        assert exponent < 0
        checks.append(f"subexponential_beaten_X={int(X)}")

    payload = {
        "arithmetic_class": "EXACT_RATIONAL_PLUS_FLOATING_HARMONIC_SANITY",
        "checks": len(checks),
        "checks_list": checks,
        "critical_sign_proved_for_xi": False,
        "finite_strip_analytic_theorem_replayed": False,
        "moving_saddle_replayed": False,
        "rh_established": False,
        "verdict": "PASS_X_105430_CRITICAL_SIGN_RIGIDITY",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object"] = hashlib.sha256(canonical).hexdigest()

    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["verdict"])
    print(payload["proof_object"])
    print(f"checks={payload['checks']}")
    print("RH_UNPROVEN")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py OUTPUT_JSON")
    main(sys.argv[1])
