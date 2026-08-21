#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
CONTROL_SCHEMA = "riemann.x94000.standalone-reset-candidate.v1"
RESULT_SCHEMA = "riemann.x94000.standalone-reset-candidate.result.v1"


def frac(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"unsupported rational value: {value!r}")


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


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


def add_interval(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg_interval(a):
    return -a[1], -a[0]


def scale_interval(c: Fraction, a):
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def mul_interval(a, b):
    vals = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(vals), max(vals)


def reciprocal_interval(a):
    if a[0] <= 0:
        raise ValueError("reciprocal interval crosses zero")
    return Fraction(1, a[1]), Fraction(1, a[0])


def divide_interval(a, b):
    return mul_interval(a, reciprocal_interval(b))


def g_interval(s: int, n: int):
    if n > s:
        return Fraction(0), Fraction(0)
    return add_interval(sqrt_interval(n), neg_interval(scale_interval(Fraction(n), reciprocal_interval(sqrt_interval(s)))))


def p_interval(s: int, j: int):
    if j < 2:
        raise ValueError("row index must be >=2")
    out = scale_interval(Fraction(1, j - 1), g_interval(s, j))
    out = add_interval(out, scale_interval(Fraction(-2, j), g_interval(s, j + 1)))
    out = add_interval(out, scale_interval(Fraction(1, j + 1), g_interval(s, j + 2)))
    return scale_interval(Fraction(j + 1), out)


def witness_interval():
    parent = p_interval(1005, 14)
    child = p_interval(15, 14)
    return add_interval(parent, neg_interval(divide_interval(child, sqrt_interval(67))))


def parse_vector(values):
    return [frac(v) for v in values]


def dot(a, b):
    if len(a) != len(b):
        raise ValueError("vector length mismatch")
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def validate_control(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != CONTROL_SCHEMA:
        raise ValueError("unexpected control schema")

    expected_genealogy = {
        "base_main_sha": "9c7538559d7f56c2914b39aed5a1fb3fbf7ce131",
        "pr495_sha": "50f45b46cbe3c471d6e702c41c7ef178b530e1ab",
        "review503_sha": "db77e5792966edf080604fd4b69fb00f07739681",
        "pr508_sha": "4ae97dffd1f76ed3244b8f3028560ffa80663caf",
        "pr352_sha": "906b5a477a1ed7c88a40db7569924f15f3d54b72",
        "pr353_sha": "ed566f3198e236c54ba18049181016536f56d456",
        "pr509_sha": "e01daee9cdfea35d2a7d2591f1df6c8080084119",
    }
    if data.get("genealogy") != expected_genealogy:
        raise ValueError("genealogy mismatch")

    affine = data["affine"]
    u_a, u_b, u_bar = (frac(affine[k]) for k in ("u_a", "u_b", "u_bar"))
    A, B = parse_vector(affine["A"]), parse_vector(affine["B"])
    if not (u_b < u_bar < u_a):
        raise ValueError("affine mean is outside endpoint interval")
    theta = (u_bar - u_b) / (u_a - u_b)
    p_a = [a - u_a * b for a, b in zip(A, B)]
    p_b = [a - u_b * b for a, b in zip(A, B)]
    p_bar = [a - u_bar * b for a, b in zip(A, B)]
    compressed = [theta * x + (1 - theta) * y for x, y in zip(p_a, p_b)]
    if p_bar != compressed:
        raise ValueError("affine two-node compression failed")
    if min(p_a + p_b) < 0:
        raise ValueError("endpoint row lost positivity")

    hybrid = data["hybrid"]
    anchored = parse_vector(hybrid["anchored"])
    bulk = parse_vector(hybrid["bulk"])
    defect = parse_vector(hybrid["defect"])
    native = parse_vector(hybrid["native"])
    if [anchored[i] + bulk[i] + defect[i] for i in range(len(native))] != native:
        raise ValueError("hybrid native identity failed")
    actual_row = [anchored[i] + bulk[i] for i in range(len(native))]
    if min(actual_row) < 0:
        raise ValueError("actual row is not nonnegative")

    obs = data["observations"]
    q = parse_vector(obs["q"])
    q4 = parse_vector(obs["q4"])
    q_value = dot(actual_row, q)
    q4_value = dot(actual_row, q4)
    detail = q_value - 2 * q4_value
    if detail != frac(obs["detail"]):
        raise ValueError("ordinary q/4q detail identity failed")

    witness = witness_interval()
    if not (Fraction(-184291, 10**9) < witness[0] <= witness[1] < Fraction(-184290, 10**9) < 0):
        raise ValueError("review #503 witness no longer fails closed")

    capacity = data["capacity"]
    X0 = int(capacity["minimum_X"])
    K = int(capacity["K"])
    if K != X0 // 67 + 1:
        raise ValueError("K is not floor(X/67)+1")
    floor_sqrt_k = isqrt(K)
    ceil_sqrt_k = floor_sqrt_k if floor_sqrt_k * floor_sqrt_k == K else floor_sqrt_k + 1
    W = 6 * ceil_sqrt_k + 4
    if not K + 2 <= X0 - W - 3:
        raise ValueError("bulk interval empty at minimum X")

    thinning_cost = Fraction(384) * Fraction(7, 10) * Fraction(83, 10)
    if thinning_cost != Fraction(55776, 25):
        raise AssertionError("thinning cost arithmetic drift")
    L = 29
    mismatch_cost = Fraction(171, 4 * floor_sqrt_k) * (3 + 2 * L + 2 * L * L)
    if mismatch_cost != Fraction(99351, 162892):
        raise AssertionError("mismatch cost arithmetic drift")
    total_cost = thinning_cost + mismatch_cost
    if not total_cost < 3457:
        raise ValueError("native cost is not below 3457")

    firewalls = data["firewalls"]
    required_zero = (
        "derivative_causal_calls",
        "rough_lift_parent_uses",
        "bulk_quantizers",
        "exported_children",
        "auxiliary_ports",
        "imports_L91763",
        "imports_T92910",
    )
    if any(int(firewalls[name]) != 0 for name in required_zero):
        raise ValueError("forbidden route operation enabled")
    if firewalls["pr509_dependency"] is not False:
        raise ValueError("PR #509 was promoted from comparison to dependency")
    if firewalls["ordinary_q_and_4q_same_row"] is not True:
        raise ValueError("q and 4q are not observations of one row")
    if firewalls["small_q_included"] is not True:
        raise ValueError("small q columns were dropped")
    if firewalls["benchmark_bridge_used"] is not False:
        raise ValueError("forbidden benchmark bridge enabled")
    if firewalls["finite_dual_orientation"] != "F_Lambda<=native_deficit":
        raise ValueError("wrong endpoint orientation")

    result = {
        "schema": RESULT_SCHEMA,
        "verdict": "PASS_T94000_STANDALONE_RESET_CANDIDATE_ALGEBRA",
        "genealogy": expected_genealogy,
        "mandatory_negative_witness": {
            "tuple": [67, 15, 1005, 14],
            "lower": fstr(witness[0]),
            "upper": fstr(witness[1]),
            "coarse": "-184291/10^9 < D < -184290/10^9 < 0",
        },
        "affine_cell": {
            "theta": fstr(theta),
            "endpoint_a": [fstr(v) for v in p_a],
            "endpoint_b": [fstr(v) for v in p_b],
            "mean_row": [fstr(v) for v in p_bar],
        },
        "hybrid": {
            "actual_row": [fstr(v) for v in actual_row],
            "native_row": [fstr(v) for v in native],
            "q_value": fstr(q_value),
            "q4_value": fstr(q4_value),
            "detail": fstr(detail),
        },
        "capacity": {
            "minimum_X": X0,
            "K": K,
            "floor_sqrt_K": floor_sqrt_k,
            "ceil_sqrt_K": ceil_sqrt_k,
            "top_anchor": W,
            "relative_reserve": "23/sqrt(K)",
            "thinning": "sqrt(K)/(sqrt(K)+24)",
        },
        "native_cost": {
            "thinning": fstr(thinning_cost),
            "signed_mismatch": fstr(mismatch_cost),
            "total": fstr(total_cost),
            "bound": "<3457",
        },
        "route_firewalls": {
            "derivative_causal_calls": 0,
            "rough_lift_parent_uses": 0,
            "bulk_quantizers": 0,
            "exported_children": 0,
            "auxiliary_ports": 0,
            "pr509_dependency": False,
        },
        "proof_boundary": (
            "Exact regression for the PR #503 witness, affine-cell compression, one actual hybrid row, "
            "same-row q/4q detail, reserve constants, genealogy and native-cost arithmetic. It does not replay "
            "the directed Target-Lorenz sweep, the retained-cell analytic estimate, or the Mellin-Landau consumer and does not establish RH."
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
    result = validate_control(json.loads(args.certificate.read_text()))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
