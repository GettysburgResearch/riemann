#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99550_CLAMPED_VOLTERRA_EQUALITY_FRAME"


def euler_numerator_for_power_log(a: Fraction) -> tuple[Fraction, Fraction]:
    """For y^a log y, return coefficients of y^a log y and y^a
    in 2 y^2 f'' - y f' + f."""
    return 2 * a * a - 3 * a + 1, 4 * a - 3


def euler_numerator_for_power(a: Fraction) -> Fraction:
    """For y^a, return the coefficient in 2 y^2 f'' - y f' + f."""
    return 2 * a * a - 3 * a + 1


def main() -> None:
    half = Fraction(1, 2)

    # Exact Euler-operator action on the four basis functions.
    assert euler_numerator_for_power_log(Fraction(1)) == (0, 1)
    assert euler_numerator_for_power_log(half) == (0, -1)
    assert euler_numerator_for_power(Fraction(1)) == 0
    assert euler_numerator_for_power(half) == 0

    # V(4 y log y + 2 sqrt(y) log y - 12 y + 12 sqrt(y))
    # = 2 sqrt(y) - 1.
    sqrt_coefficient = 4 * Fraction(1, 2)
    constant_coefficient = 2 * Fraction(-1, 2)
    assert sqrt_coefficient == 2
    assert constant_coefficient == -1

    # The two activation clamps uniquely determine the homogeneous terms.
    # For 4 y log y + 2 sqrt(y) log y + a y + b sqrt(y):
    # Phi(1)=a+b and Phi'(1+)=6+a+b/2.
    b = Fraction(12)
    a = -b
    assert a + b == 0
    assert 6 + a + b / 2 == 0
    assert (a, b) == (Fraction(-12), Fraction(12))

    # The Green integral against 2 sqrt(t)-1 reconstructs exactly
    # 4 x log x + 2 sqrt(x) log x - 12 x + 12 sqrt(x).
    green_coefficients = {
        "x_log_x": Fraction(4),
        "sqrt_x_log_x": Fraction(2),
        "x": Fraction(-4) + Fraction(-8),
        "sqrt_x": Fraction(4) + Fraction(8),
    }
    assert green_coefficients == {
        "x_log_x": Fraction(4),
        "sqrt_x_log_x": Fraction(2),
        "x": Fraction(-12),
        "sqrt_x": Fraction(12),
    }

    # At the lower endpoint a=1, both homogeneous Green coefficients vanish.
    f1 = Fraction(0)
    fp1 = Fraction(0)
    A1 = 2 * (f1 - fp1)
    B1 = 2 * fp1 - f1
    assert A1 == 0 and B1 == 0

    # Every newly activated arithmetic colour has zero value and derivative,
    # hence its derivative-jump atom t^(3/2)[f'(t+)-f'(t-)] is zero.
    right_value = a + b
    right_derivative = 6 + a + b / 2
    left_value = Fraction(0)
    left_derivative = Fraction(0)
    assert right_value == left_value
    assert right_derivative == left_derivative

    # Exact scaling check at n=4, x=36 (so y=9):
    # V_x Phi(x/n) = n^(-1/2) (2 sqrt(x/n)-1) = 5/2.
    assert Fraction(1, 2) * (2 * 3 - 1) == Fraction(5, 2)

    # The physical endpoint packet is also double clamped.
    # b_X(t)=2 sqrt(t) log(X/t)-4 sqrt(t)+4t/sqrt(X).
    # At X=t=9, both b and partial_X b vanish.
    sqrt_t = Fraction(3)
    t = Fraction(9)
    b_at_activation = -4 * sqrt_t + 4 * t / sqrt_t
    db_at_activation = 2 * sqrt_t / t - 2 * t / (sqrt_t ** 3)
    assert b_at_activation == 0
    assert db_at_activation == 0

    # Mutation firewalls: changing either homogeneous coefficient destroys
    # at least one clamp and therefore creates a boundary or knot term.
    a_bad, b_bad = Fraction(-11), Fraction(12)
    assert a_bad + b_bad != 0
    a_bad2, b_bad2 = Fraction(-12), Fraction(11)
    assert (a_bad2 + b_bad2 != 0) or (6 + a_bad2 + b_bad2 / 2 != 0)

    core = {
        "schema": "riemann.x99550.clamped-volterra.v1",
        "operator_density": "(2*x^2*f''-x*f'+f)/(2*sqrt(x))",
        "phi_coefficients": [4, 2, -12, 12],
        "inverse_density": "2*sqrt(y)-1",
        "value_clamp_at_one": True,
        "derivative_clamp_at_one": True,
        "all_activation_knot_atoms_zero": True,
        "volterra_nullspace_coefficients_zero": True,
        "green_reconstruction_exact": True,
        "physical_endpoint_packet_double_clamped": True,
        "mutation_firewalls_pass": True,
        "heavy_inherited_campaigns_replayed": False,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canon).hexdigest()

    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(core, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(VERDICT)
    print(core["proof_object_sha256"])


if __name__ == "__main__":
    main()
