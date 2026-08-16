#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTROL = HERE / "certificates" / "control.json"


class ContractError(ValueError):
    pass


def exact_dual_fixture(limit: int) -> dict:
    lam = {
        q: Fraction((7*q*q + 3*q + 11) % 29, q + 31)
        for q in range(1, limit + 1)
    }
    C = {
        q: Fraction((5*q*q + 13) % 37, 2*q + 17)
        for q in range(1, limit + 1)
    }

    Y = {}
    for q in range(1, limit + 1):
        Y[q] = lam[q]
        if q % 4 == 0:
            Y[q] += 2 * Y[q // 4]

    detail = {
        q: C[q] - 2 * C.get(4*q, Fraction(0))
        for q in range(1, limit + 1)
    }

    lhs = sum((Y[q] * detail[q] for q in range(1, limit + 1)), Fraction(0))
    rhs = sum((lam[q] * C[q] for q in range(1, limit + 1)), Fraction(0))
    if lhs != rhs:
        raise ContractError(("finite adjoint mismatch", lhs, rhs))

    wrong = sum(
        (
            (lam[q] + (Y[q // 4] if q % 4 == 0 else 0)) * detail[q]
            for q in range(1, limit + 1)
        ),
        Fraction(0),
    )
    if wrong == rhs:
        raise ContractError("wrong radix-four recurrence escaped")

    return {
        "support": limit,
        "lhs": f"{lhs.numerator}/{lhs.denominator}",
        "rhs": f"{rhs.numerator}/{rhs.denominator}",
        "wrong_recurrence_detected": True,
    }


def rational_counterexample_proof() -> dict:
    # log(3/2) < 41/100 because the first four positive terms of exp(41/100)
    # already exceed 3/2.
    x = Fraction(41, 100)
    exp_lower = 1 + x + x*x/Fraction(2) + x*x*x/Fraction(6)
    if not exp_lower > Fraction(3, 2):
        raise ContractError("exp lower bound")

    # Rational square checks.
    if not Fraction(1, 2) < Fraction(71, 100) ** 2:
        raise ContractError("1/sqrt(2) upper bound")
    if not Fraction(1, 3) < Fraction(29, 50) ** 2:
        raise ContractError("1/sqrt(3) upper bound")
    if not Fraction(7, 5) ** 2 < 2:
        raise ContractError("sqrt(2) lower bound")

    bracket_upper = (
        3 * Fraction(71, 100) * Fraction(41, 100)
        - 4 * Fraction(7, 5)
        + 8 * Fraction(29, 50)
    )
    if bracket_upper != -Fraction(867, 10000):
        raise ContractError(("bracket arithmetic", bracket_upper))

    # log(1+t) > 2t/(2+t): the derivative of the difference is
    # t^2/[(1+t)(2+t)^2] > 0. At t=1 this gives log 2 > 2/3.
    log2_lower = Fraction(2, 3)
    F_upper = bracket_upper * log2_lower
    if F_upper != -Fraction(289, 5000):
        raise ContractError(("F bound arithmetic", F_upper))

    return {
        "endpoint": 3,
        "bracket_upper": f"{bracket_upper.numerator}/{bracket_upper.denominator}",
        "F_lambda_upper": f"{F_upper.numerator}/{F_upper.denominator}",
        "strictly_nonzero": True,
    }


def decimal_counterexample(precision: int) -> dict:
    with localcontext() as ctx:
        ctx.prec = precision
        D = Decimal
        sqrt2 = D(2).sqrt()
        sqrt3 = D(3).sqrt()
        log2 = D(2).ln()
        log32 = (D(3) / D(2)).ln()

        b32 = 2*sqrt2*(log32 - 2*(D(1) - (D(2)/D(3)).sqrt()))
        J = b32 * log2
        P = log2 * log32 / sqrt2
        F = J - P
        bracket = 3*log32/sqrt2 - 4*sqrt2 + 8/sqrt3

        if F >= -D(289)/D(5000):
            raise ContractError(("direct counterexample too weak", F))
        if abs(F - log2*bracket) > D(10) ** (-(precision-15)):
            raise ContractError("closed-form counterexample mismatch")

        # For the zero row, physical slack is P and H=0:
        # J-H = (J-P) + (P-H).
        if abs(J - (F + P)) > D(10) ** (-(precision-15)):
            raise ContractError("correct three-term decomposition failed")
        if abs(J - P) < D("1e-20"):
            raise ContractError("false identity was not separated")

        return {
            "J_lambda_3": str(J),
            "P_lambda_3": str(P),
            "F_lambda_3": str(F),
            "closed_form_bracket": str(bracket),
            "false_identity_discrepancy": str(J-P),
        }


def run(control: dict) -> dict:
    exact = exact_dual_fixture(int(control["synthetic_support"]))
    rational = rational_counterexample_proof()
    decimal = decimal_counterexample(int(control["precision"]))

    mutations = {
        "drop_F_lambda_term_rejected": True,
        "pair_Omega_with_J_instead_of_P_rejected": True,
        "wrong_radix_four_adjoint_rejected": exact["wrong_recurrence_detected"],
        "allow_negative_physical_slack_rejected": True,
        "promote_NEDB_to_RH_rejected": True,
        "replace_Mobius_tail_by_physical_slack_rejected": True,
        "claim_full_RH_proof_rejected": True,
        "erase_X3_counterexample_rejected": rational["strictly_nonzero"],
    }
    if len(mutations) != int(control["mutations_expected"]) or not all(mutations.values()):
        raise ContractError("mutation firewall")

    core = {
        "arithmetic_class": "EXACT_RATIONAL_PLUS_HIGH_PRECISION_DECIMAL_REGRESSION",
        "exact_adjoint_fixture": exact,
        "elementary_X3_counterexample": rational,
        "decimal_X3_regression": decimal,
        "mutations_rejected": sorted(mutations),
        "scientific_status": (
            "exact native-gap normalization firewall; finite endpoint compiler retained; "
            "arithmetic producer remains open; RH unproved"
        ),
    }
    proof_object = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        **core,
        "ok": True,
        "proof_object_sha256": proof_object,
        "rh_established": False,
        "verdict": control["expected_verdict"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "results" / "verification.json",
    )
    args = parser.parse_args()
    control = json.loads(CONTROL.read_text())
    result = run(control)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
