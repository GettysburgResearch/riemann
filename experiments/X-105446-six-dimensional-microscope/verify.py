#!/usr/bin/env python3
"""Exact replay for T105446 six-dimensional microscope algebra.

This checker authenticates finite rational identities only. It does not replay
strong maximum principles, Xi asymptotics, zero-height escape exclusion, or RH.
"""

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1],
            z[0] * w[1] + z[1] * w[0])


def cdiv(z, w):
    d = w[0] * w[0] + w[1] * w[1]
    return ((z[0] * w[0] + z[1] * w[1]) / d,
            (z[1] * w[0] - z[0] * w[1]) / d)


def cpow(z, n):
    out = (Q(1), Q(0))
    for _ in range(n):
        out = cmul(out, z)
    return out


def cscale(a, z):
    return (a * z[0], a * z[1])


def main():
    checks = 0

    # C_aa + C_hh - 2 C_h/h = 0 after harmonicity of Im m.
    for I2 in [Q(-7, 3), Q(0), Q(5, 2)]:
        for R3 in [Q(-11, 4), Q(0), Q(9, 5)]:
            for h in [Q(1, 3), Q(2), Q(7, 4)]:
                Caa = (h * R3 - I2) / 2
                Ch = -h * I2 / 2
                Chh = -(I2 + h * R3) / 2
                assert Caa + Chh - Q(2) * Ch / h == 0
                checks += 1

    # C=h^3 W converts the drift equation to
    # W_aa+W_hh+4 W_h/h=0.
    for W in [Q(-2), Q(3, 5)]:
        for Wh in [Q(-7, 4), Q(9, 2)]:
            for Waa in [Q(-3), Q(5, 6)]:
                for h in [Q(1, 2), Q(3)]:
                    Whh = -Waa - Q(4) * Wh / h
                    Caa = h**3 * Waa
                    Ch = 3 * h * h * W + h**3 * Wh
                    Chh = 6 * h * W + 6 * h * h * Wh + h**3 * Whh
                    assert Caa + Chh - Q(2) * Ch / h == 0
                    checks += 1

    # One critical pole rho/(z-c) gives the six-dimensional Newton charge.
    for rho in [Q(-3, 2), Q(5, 7)]:
        for a, c, h in [
            (Q(2), Q(-1), Q(3, 2)),
            (Q(-4, 3), Q(5, 6), Q(2, 5)),
            (Q(0), Q(0), Q(7, 3)),
        ]:
            z = (a - c, h)
            m = cdiv((rho, Q(0)), z)
            mp = cscale(-rho, cdiv((Q(1), Q(0)), cpow(z, 2)))
            C = (h * mp[0] - m[1]) / 2
            expected = rho * h**3 / (((a - c)**2 + h**2)**2)
            assert C == expected
            checks += 1

    # The regular trace for m=z^3 is C/h^3=-m'''/6=-1.
    for a in [Q(-5, 2), Q(0), Q(7, 3)]:
        for h in [Q(1, 4), Q(2), Q(5, 3)]:
            z = (a, h)
            m = cpow(z, 3)
            mp = cscale(Q(3), cpow(z, 2))
            C = (h * mp[0] - m[1]) / 2
            assert C == -h**3
            assert C / h**3 == Q(-1)
            checks += 2

    # Dual extremal-line fixture:
    # F=z^2-1, m=F/F'=(z-z^{-1})/2 is Pick.
    for y in [Q(1, 3), Q(1), Q(5, 2), Q(7)]:
        U = (y + 1 / y) / 2
        zero_capacity = Q(2) * y / (1 + y * y)
        pole_capacity = Q(1, 2) / y
        assert zero_capacity == 1 / U
        assert pole_capacity <= U
        assert zero_capacity * pole_capacity <= 1
        checks += 3

    payload = {
        "arithmetic_class": "EXACT_RATIONAL_FINITE_ALGEBRA",
        "checks": checks,
        "elliptic_microscope_identity_replayed": True,
        "six_dimensional_lift_replayed": True,
        "newton_charge_calibration_replayed": True,
        "regular_boundary_trace_replayed": True,
        "dual_extremal_capacity_fixture_replayed": True,
        "strong_maximum_principle_replayed": False,
        "xi_zero_height_escape_excluded": False,
        "rh_established": False,
        "verdict": "PASS_X_105446_SIX_DIMENSIONAL_MICROSCOPE",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object"] = hashlib.sha256(canonical).hexdigest()

    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "experiments/X-105446-six-dimensional-microscope/results/verification.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["verdict"])
    print(payload["proof_object"])
    print("checks=", checks)


if __name__ == "__main__":
    main()
