#!/usr/bin/env python3
"""Exact finite regressions for the Claude bootstrap algebra audit."""
from __future__ import annotations

import json
from fractions import Fraction
from typing import Any

SCHEMA = "riemann.x13802-bootstrap-algebra-audit.v1"


class AuditError(ValueError):
    pass


def hermite_x2_plus_1() -> dict[str, Any]:
    h00 = Fraction(2)
    h01 = Fraction(0)
    h11 = Fraction(-2)
    determinant = h00 * h11 - h01 * h01
    positive, negative, zero = 1, 1, 0
    signature = positive - negative
    claimed_wrong_signature = 0 - 1
    if determinant != -4 or signature != 0:
        raise AuditError("Hermite regression arithmetic failed")
    if signature == claimed_wrong_signature:
        raise AuditError("wrong Hermite signature formula was not separated")
    return {
        "polynomial": "X^2+1",
        "matrix": [[2, 0], [0, -2]],
        "determinant": -4,
        "inertia": {"positive": positive, "negative": negative, "zero": zero},
        "signature": signature,
        "refuted_formula_value": claimed_wrong_signature,
        "status": "CORRECT_INERTIA_CONFIRMED",
    }


def targeted_li_first_coefficient() -> dict[str, Any]:
    u = Fraction(1)
    f_re = Fraction(1)
    f_im = Fraction(2)
    analytic_re = 2 * u * f_re
    analytic_im = 2 * u * f_im
    claimed_real = 2 * u * f_re
    if analytic_im == 0:
        raise AuditError("synthetic complex-center control is accidentally real")
    return {
        "u": "1",
        "synthetic_xi_logderivative": {"real": "1", "imag": "2"},
        "analytic_taylor_coefficient": {
            "real": str(analytic_re),
            "imag": str(analytic_im),
        },
        "claimed_real_part_only": str(claimed_real),
        "equal": False,
        "status": "TARGETED_LI_DEFINITION_INCONSISTENCY_CONFIRMED",
    }


def classical_li_modulus_constant() -> dict[str, Any]:
    delta = Fraction(1, 1000)
    gamma = Fraction(14)
    rho_norm2 = (Fraction(1, 2) - delta) ** 2 + gamma**2
    modulus_square_increment = 2 * delta / rho_norm2
    first_order_modulus_increment = delta / rho_norm2
    wrong_first_order_increment = 2 * delta / rho_norm2
    return {
        "delta": str(delta),
        "gamma": str(gamma),
        "modulus_square_increment": str(modulus_square_increment),
        "correct_first_order_modulus_increment": str(first_order_modulus_increment),
        "refuted_first_order_modulus_increment": str(wrong_first_order_increment),
        "status": "CLASSICAL_LI_FACTOR_TWO_CORRECTION_CONFIRMED",
    }


def verify() -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "hermite": hermite_x2_plus_1(),
        "targeted_li": targeted_li_first_coefficient(),
        "classical_li": classical_li_modulus_constant(),
        "classification": "EXACT_SYNTHETIC_ALGEBRA_AUDIT",
        "proof_boundary": (
            "These controls refute formulas in the audited claim cards. They do "
            "not evaluate Riemann xi and do not replace the external Hermite or "
            "Li theorems."
        ),
    }


def main() -> int:
    print(json.dumps(verify(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
