#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x93920.review503-hybrid-direct-row.result.v1"
HERE = Path(__file__).resolve().parent


def frac(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"unsupported rational value: {value!r}")


def sqrt_interval(n: int, digits: int = 30) -> tuple[Fraction, Fraction]:
    if n <= 0:
        raise ValueError("sqrt input must be positive")
    den = 10**digits
    target = n * den * den
    lo_num = isqrt(target)
    hi_num = lo_num if lo_num * lo_num == target else lo_num + 1
    lo, hi = Fraction(lo_num, den), Fraction(hi_num, den)
    if not (lo * lo <= n <= hi * hi):
        raise AssertionError("invalid sqrt enclosure")
    return lo, hi


def add(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return a[0] + b[0], a[1] + b[1]


def neg(a: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return -a[1], -a[0]


def scale(c: Fraction, a: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def mul(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    values = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(values), max(values)


def reciprocal(a: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    if a[0] <= 0:
        raise ValueError("reciprocal interval crosses zero")
    return Fraction(1, a[1]), Fraction(1, a[0])


def divide(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return mul(a, reciprocal(b))


def g_interval(s: int, n: int) -> tuple[Fraction, Fraction]:
    if n > s:
        return Fraction(0), Fraction(0)
    sn = sqrt_interval(n)
    ss = sqrt_interval(s)
    return add(sn, neg(scale(Fraction(n), reciprocal(ss))))


def p_interval(s: int, j: int) -> tuple[Fraction, Fraction]:
    if j < 2:
        raise ValueError("row index must be >=2")
    out = scale(Fraction(1, j - 1), g_interval(s, j))
    out = add(out, scale(Fraction(-2, j), g_interval(s, j + 1)))
    out = add(out, scale(Fraction(1, j + 1), g_interval(s, j + 2)))
    return scale(Fraction(j + 1), out)


def witness_interval() -> tuple[Fraction, Fraction]:
    parent = p_interval(1005, 14)
    child = p_interval(15, 14)
    return add(parent, neg(divide(child, sqrt_interval(67))))


def direct_bulk_interval() -> tuple[Fraction, Fraction]:
    # Actual positive direct fibre contribution at x=2:
    # (2 sqrt(2)-1) p_1005(14).
    density = add(scale(Fraction(2), sqrt_interval(2)), (Fraction(-1), Fraction(-1)))
    return mul(density, p_interval(1005, 14))


def ceil_sqrt(n: int) -> int:
    r = isqrt(n)
    return r if r * r == n else r + 1


def validate_control(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != "riemann.x93920.review503-hybrid-direct-row.control.v1":
        raise ValueError("unexpected control schema")

    genealogy = data["genealogy"]
    expected_genealogy = {
        "pr495_sha": "50f45b46cbe3c471d6e702c41c7ef178b530e1ab",
        "review503_sha": "db77e5792966edf080604fd4b69fb00f07739681",
        "pr508_sha": "4ae97dffd1f76ed3244b8f3028560ffa80663caf",
        "pr352_sha": "906b5a477a1ed7c88a40db7569924f15f3d54b72",
        "pr353_sha": "ed566f3198e236c54ba18049181016536f56d456",
        "pr509_sha": "e01daee9cdfea35d2a7d2591f1df6c8080084119",
    }
    if genealogy != expected_genealogy:
        raise ValueError("genealogy mismatch")

    route = data["route"]
    if route["preserved_claims"] != ["L-91760", "L-91761", "L-91762"]:
        raise ValueError("surviving Volterra claims changed")
    if set(route["forbidden_claims"]) != {"L-91763", "T-92910"}:
        raise ValueError("forbidden claim firewall changed")
    forbidden_true = (
        "uses_derivative_fibre_causal_generator",
        "uses_rough_lift_as_parent_marginal",
        "uses_bulk_quantizer",
        "uses_pr509_as_confirmation",
    )
    if any(route[name] for name in forbidden_true):
        raise ValueError("forbidden route operation enabled")
    required_true = (
        "anchored_target_lorenz_import",
        "ordinary_and_4q_share_one_row",
        "small_q_included",
        "forbidden_benchmark_bridge",
    )
    if not all(route[name] for name in required_true):
        raise ValueError("required route firewall disabled")
    if route["finite_dual_orientation"] != "F_Lambda<=native_deficit":
        raise ValueError("wrong finite-dual orientation")
    if route["exported_children"] != 0 or route["auxiliary_port"] != 0:
        raise ValueError("children or port unexpectedly exported")

    constants = data["constants"]
    if constants != {
        "minimum_X": 10**12,
        "top_anchor_sqrt_multiplier": 6,
        "top_anchor_additive": 4,
        "relative_mismatch_constant": 23,
        "thinning_shift": 24,
        "thinning_native_cost_bound": 3456,
        "mismatch_native_cost_bound": 1,
        "total_native_deficit_bound": 3457,
    }:
        raise ValueError("constant ledger mismatch")

    witness = data["mandatory_witness"]
    if (witness["p"], witness["child_endpoint"], witness["parent_endpoint"], witness["row"]) != (67, 15, 1005, 14):
        raise ValueError("mandatory witness changed")

    D = witness_interval()
    coarse_lo = Fraction(witness["coarse_lower_numerator"], witness["coarse_denominator"])
    coarse_hi = Fraction(witness["coarse_upper_numerator"], witness["coarse_denominator"])
    if not (coarse_lo < D[0] <= D[1] < coarse_hi < 0):
        raise ValueError("review #503 witness no longer fails closed")

    parent = p_interval(1005, 14)
    child = p_interval(15, 14)
    direct = direct_bulk_interval()
    if parent[0] <= 0 or child[0] <= 0 or direct[0] <= 0:
        raise ValueError("direct positive fibre regression failed")

    # Exact constant checks used in L-93921.
    if not 513 * 513 < 2 * (23 * 16) ** 2:
        raise AssertionError("nonterminal constant 23 invalid")
    if not Fraction(1) + Fraction(3, 8) + Fraction(1, 5) < Fraction(8, 5):
        raise AssertionError("terminal three-multiple bound invalid")
    if not Fraction(608, 5 * 6) < 23:
        raise AssertionError("moving-anchor terminal constant invalid")
    # Exact elementary certificate that log(2*10^12) < 29:
    # exp(29) exceeds the 29th partial sum, and that rational partial sum
    # already exceeds 2*10^12.
    exp_partial = Fraction(0)
    term = Fraction(1)
    for n in range(30):
        if n > 0:
            term *= Fraction(29, n)
        exp_partial += term
    if not exp_partial > 2_000_000_000_000:
        raise AssertionError("exp(29) lower certificate failed")
    if not Fraction(1539 * 1743, 4_000_000) < 1:
        raise AssertionError("native mismatch cost is not below one")
    if constants["thinning_native_cost_bound"] + constants["mismatch_native_cost_bound"] != constants["total_native_deficit_bound"]:
        raise AssertionError("native cost ledger does not sum")

    X0 = constants["minimum_X"]
    K0 = X0 // 67 + 1
    W0 = constants["top_anchor_sqrt_multiplier"] * ceil_sqrt(K0) + constants["top_anchor_additive"]
    if not K0 + 2 <= X0 - W0 - 3:
        raise ValueError("bulk interval empty at minimum X")

    result = {
        "schema": SCHEMA,
        "verdict": "PASS_REVIEW503_SAFE_ANCHORED_VOLTERRA_DIRECT_ROW",
        "freeze": expected_genealogy,
        "mandatory_negative_witness": {
            "tuple": [67, 15, 1005, 14],
            "lower": f"{D[0].numerator}/{D[0].denominator}",
            "upper": f"{D[1].numerator}/{D[1].denominator}",
            "coarse": "-184291/10^9 < D < -184290/10^9 < 0",
        },
        "actual_row_checks": {
            "p_1005_row14_lower": f"{parent[0].numerator}/{parent[0].denominator}",
            "p_15_row14_lower": f"{child[0].numerator}/{child[0].denominator}",
            "direct_x2_bulk_row14_lower": f"{direct[0].numerator}/{direct[0].denominator}",
        },
        "route_firewalls": {
            "derivative_causal_calls": 0,
            "rough_lift_parent_uses": 0,
            "bulk_quantizers": 0,
            "exported_children": 0,
            "auxiliary_port": 0,
            "pr509_dependency": False,
        },
        "all_column_constants": {
            "relative_mismatch": "23/sqrt(K)",
            "thinning": "sqrt(K)/(sqrt(K)+24)",
            "top_anchor": "6*ceil(sqrt(K))+4",
            "minimum_X": X0,
            "K_at_minimum_X": K0,
            "W_at_minimum_X": W0,
        },
        "native_cost": {
            "thinning": "<3456",
            "signed_mismatch": "<1",
            "total": "<3457",
        },
        "proof_boundary": (
            "Exact regression for the PR #503 negative witness, direct positive Volterra fibre, "
            "route firewalls, all-column constants, genealogy, and native-cost arithmetic. "
            "It does not replay the directed Target-Lorenz sweep or the frozen Mellin-Landau consumer and does not prove RH."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=HERE / "certificates" / "control.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    result = validate_control(data)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
