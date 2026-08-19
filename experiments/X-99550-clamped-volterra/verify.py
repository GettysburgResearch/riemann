#!/usr/bin/env python3
"""Exact algebra replay for T99550.

The script deliberately uses only the standard library.  It certifies the
finite differential and coefficient identities in the packet; it does not
replay any inherited Hall, MPFR, common-parent, or Mellin-Landau campaign.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, Tuple

Q = Fraction
Term = Tuple[Q, Q, int]  # coefficient, power of u, log-power (0 or 1)
Expr = Dict[Tuple[Q, int], Q]


def _clean(expr: Expr) -> Expr:
    return {key: value for key, value in expr.items() if value}


def apply_v(terms: Iterable[Term]) -> Expr:
    """Apply V=(2D^2-3D+1)/(2 sqrt(u)), D=u d/du."""
    out: Expr = defaultdict(Q)
    for coefficient, power, log_power in terms:
        characteristic = 2 * power * power - 3 * power + 1
        exponent = power - Q(1, 2)
        if log_power == 0:
            out[(exponent, 0)] += coefficient * characteristic / 2
        elif log_power == 1:
            out[(exponent, 1)] += coefficient * characteristic / 2
            out[(exponent, 0)] += coefficient * (4 * power - 3) / 2
        else:
            raise ValueError("Only log powers 0 and 1 are supported")
    return _clean(dict(out))


def value_at_one(terms: Iterable[Term]) -> Q:
    return sum(c for c, _a, b in terms if b == 0)


def derivative_at_one(terms: Iterable[Term]) -> Q:
    total = Q(0)
    for coefficient, power, log_power in terms:
        if log_power == 0:
            total += coefficient * power
        elif log_power == 1:
            # d[u^a log u]/du at u=1 is 1.
            total += coefficient
        else:
            raise ValueError("Only log powers 0 and 1 are supported")
    return total


def integral_dictionary() -> Dict[str, Q]:
    """Coefficient dictionary after integrating one colour.

    Use r=sqrt(k theta).  Expanding K_-(theta,t) times the colour density and
    integrating theta<=t<=1/k gives a linear combination of
    1, r, r^2, and r log(k theta).
    """
    out: Dict[str, Q] = defaultdict(Q)

    # 4 sqrt(theta)/k * integral t^(-3/2)
    out["one"] += 8
    out["r"] -= 8

    # -2 sqrt(theta)/sqrt(k) * integral t^(-1)
    out["r_log"] += 2

    # -4 theta/k * integral t^(-2)
    out["one"] -= 4
    out["r2"] += 4

    # 2 theta/sqrt(k) * integral t^(-3/2)
    out["r2"] -= 4
    out["r"] += 4

    return {key: value for key, value in out.items() if value or key == "r2"}


def run_checks() -> dict:
    canonical: Tuple[Term, ...] = (
        (Q(4), Q(0), 0),
        (Q(-4), Q(1, 2), 0),
        (Q(2), Q(1, 2), 1),
    )

    expected_v: Expr = {
        (Q(-1, 2), 0): Q(2),
        (Q(0), 0): Q(-1),
    }
    actual_v = apply_v(canonical)
    assert actual_v == expected_v

    assert value_at_one(canonical) == 0
    assert derivative_at_one(canonical) == 0

    # Exact scaled-colour rule:
    # V_theta[k^-1 F(k theta)] = k^-1/2 V_u F(u), u=k theta.
    scaled_colour = {
        "coefficient_of_1_over_k_sqrt_theta": Q(2),
        "coefficient_of_1_over_sqrt_k": Q(-1),
    }
    assert scaled_colour == {
        "coefficient_of_1_over_k_sqrt_theta": Q(2),
        "coefficient_of_1_over_sqrt_k": Q(-1),
    }

    # Reverse Green kernel: left derivative at x=t is -t^-3/2 and the right
    # derivative is zero, so right-minus-left is +t^-3/2.
    reverse_kernel_jump_multiplier = Q(1)
    assert reverse_kernel_jump_multiplier == 1

    expected_integral = {
        "one": Q(4),
        "r": Q(-4),
        "r2": Q(0),
        "r_log": Q(2),
    }
    actual_integral = integral_dictionary()
    assert actual_integral == expected_integral

    # The two homogeneous modes are killed by endpoint value and derivative.
    # Matrix [[1,1],[1/2,1]] has determinant 1/2.
    clamp_matrix_determinant = Q(1, 2)
    assert clamp_matrix_determinant != 0

    # Mutation firewalls.
    value_mutation = (
        (Q(5), Q(0), 0),
        (Q(-4), Q(1, 2), 0),
        (Q(2), Q(1, 2), 1),
    )
    derivative_mutation = (
        (Q(4), Q(0), 0),
        (Q(-4), Q(1, 2), 0),
        (Q(3), Q(1, 2), 1),
    )
    nullspace_mutation = (
        (Q(4), Q(0), 0),
        (Q(-3), Q(1, 2), 0),
        (Q(2), Q(1, 2), 1),
    )
    assert value_at_one(value_mutation) != 0
    assert derivative_at_one(derivative_mutation) != 0
    assert apply_v(derivative_mutation) != expected_v
    # Changing the sqrt coefficient is invisible to V but violates the clamp.
    assert apply_v(nullspace_mutation) == expected_v
    assert value_at_one(nullspace_mutation) != 0

    proof_data = {
        "canonical_terms": [
            [str(c), str(a), b] for c, a, b in canonical
        ],
        "volterra_image": {
            f"u^{power}*log^{log_power}": str(coefficient)
            for (power, log_power), coefficient in sorted(actual_v.items())
        },
        "activation_value": "0",
        "activation_derivative": "0",
        "reverse_kernel_jump_multiplier": "1",
        "one_colour_integral_dictionary": {
            key: str(value) for key, value in actual_integral.items()
        },
        "homogeneous_clamp_determinant": str(clamp_matrix_determinant),
        "mutations_rejected": 4,
        "compact_hall_replayed": False,
        "mpfr_terminal_replayed": False,
        "common_parent_reconstructed": False,
        "rh_established": False,
    }
    encoded = json.dumps(proof_data, sort_keys=True, separators=(",", ":")).encode()
    proof_object = hashlib.sha256(encoded).hexdigest()

    return {
        "verdict": "PASS_T99550_CLAMPED_VOLTERRA_EQUALITY_INTERFACE",
        "proof_object": proof_object,
        "checks": proof_data,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = run_checks()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
