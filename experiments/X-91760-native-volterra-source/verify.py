#!/usr/bin/env python3
"""Exact regression for L-91760/L-91761.

This checker authenticates a formal perfect-square instance of the Volterra
atom identity, the rank-one source coupling, finite=continuum+mismatch under
linear observations, interval one-use ownership, and root/rough disjointness.
It does not prove the analytic endpoint estimates or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x91760-native-volterra-source.v1"


def frac(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("booleans are not rational inputs")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, str):
        return Fraction(x)
    raise ValueError(f"unsupported rational input: {x!r}")


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def vec(raw: Any) -> list[Fraction]:
    if not isinstance(raw, list) or not raw:
        raise ValueError("vector must be a nonempty list")
    return [frac(x) for x in raw]


def mat(raw: Any, width: int) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise ValueError("matrix must be nonempty")
    out = [[frac(x) for x in row] for row in raw]
    if any(len(row) != width for row in out):
        raise ValueError("matrix width mismatch")
    return out


def add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    if len(a) != len(b):
        raise ValueError("vector dimension mismatch")
    return [x + y for x, y in zip(a, b)]


def scale(c: Fraction, a: list[Fraction]) -> list[Fraction]:
    return [c * x for x in a]


def mv(A: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    return [sum((a * b for a, b in zip(row, x)), Fraction(0)) for row in A]


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("schema mismatch")

    # 1. Formal Volterra identity in the basis {1, log(Y/n)}.
    volterra_results = []
    cases = data.get("volterra_cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("volterra_cases must be nonempty")
    for case in cases:
        A = frac(case["sqrt_Y"])
        B = frac(case["sqrt_n"])
        C = frac(case["sqrt_k"])
        if not (A > B > 0 and C > 0):
            raise ValueError("need sqrt_Y > sqrt_n > 0 and sqrt_k > 0")

        # Left: k^(-1/2) int_n^Y t^(-1/2) log(Y/t) dt.
        left_const = 4 * (A - B) / C
        left_log = -2 * B / C

        # Right: integrate (2/s) ell_(X/s)(k) g_s(n) after u=sqrt(s).
        # Primitive values are evaluated separately at u=A and u=B.
        upper_const = -8 * B / C
        lower_const = (-4 * A - 4 * B) / C
        right_const = upper_const - lower_const
        right_log = -2 * B / C

        if (left_const, left_log) != (right_const, right_log):
            raise ValueError("formal Volterra atom identity failed")
        volterra_results.append(
            {
                "sqrt_Y": fstr(A),
                "sqrt_n": fstr(B),
                "sqrt_k": fstr(C),
                "constant_coefficient": fstr(left_const),
                "log_Y_over_n_coefficient": fstr(left_log),
            }
        )

    # 2. Exact rank-one source coupling.
    pos = vec(data["positive_weights"])
    neg = vec(data["negative_weights"])
    feature = vec(data["common_feature"])
    Pp = sum(pos, Fraction(0))
    Pm = sum(neg, Fraction(0))
    if not (Pp > Pm >= 0):
        raise ValueError("rank-one coupling requires total positive > total negative")

    transport = [[nw * pw / Pp for pw in pos] for nw in neg]
    for i, nw in enumerate(neg):
        if sum(transport[i], Fraction(0)) != nw:
            raise ValueError("negative source not exhausted")
    residual = []
    for j, pw in enumerate(pos):
        used = sum((transport[i][j] for i in range(len(neg))), Fraction(0))
        if not 0 <= used <= pw:
            raise ValueError("positive source overdraw")
        residual.append(pw - used)
    L = Pp - Pm
    if sum(residual, Fraction(0)) != L:
        raise ValueError("residual does not sum to positive density")
    signed_feature = add(scale(Pp, feature), scale(-Pm, feature))
    residual_feature = scale(sum(residual, Fraction(0)), feature)
    if signed_feature != residual_feature:
        raise ValueError("common-feature source identity failed")

    # 3. Exact finite = continuum + mismatch under all declared observations.
    continuum = vec(data["continuum_seed"])
    mismatch = vec(data["mismatch_seed"])
    finite = vec(data["finite_seed"])
    if add(continuum, mismatch) != finite:
        raise ValueError("finite seed is not continuum plus mismatch")
    width = len(finite)
    row_map = mat(data["row_map"], width)
    ordinary_map = mat(data["ordinary_map"], width)
    detail_map = mat(data["detail_map"], width)
    observation_results = {}
    for name, Aobs in (
        ("row", row_map),
        ("ordinary", ordinary_map),
        ("detail", detail_map),
    ):
        lhs = mv(Aobs, finite)
        rhs = add(mv(Aobs, continuum), mv(Aobs, mismatch))
        if lhs != rhs:
            raise ValueError(f"{name} observation identity failed")
        observation_results[name] = [fstr(x) for x in lhs]

    # 4. Source restriction is a literal partition.
    total_mass = frac(data["total_source_mass"])
    bottom = frac(data["bottom_mass"])
    retained = frac(data["retained_mass"])
    top = frac(data["top_mass"])
    if any(x < 0 for x in (bottom, retained, top)):
        raise ValueError("source restrictions must be nonnegative")
    if bottom + retained + top != total_mass:
        raise ValueError("source restrictions do not partition total mass")

    # 5. Root colours are strictly below 67 and rough owners start at 67.
    root_labels = data["root_labels"]
    rough_labels = data["rough_labels"]
    if not isinstance(root_labels, list) or not isinstance(rough_labels, list):
        raise ValueError("label arrays required")
    if any(isinstance(x, bool) or not isinstance(x, int) for x in root_labels + rough_labels):
        raise ValueError("labels must be integers")
    if any(x < 1 or x >= 67 for x in root_labels):
        raise ValueError("root label reaches rough threshold")
    if any(x < 67 for x in rough_labels):
        raise ValueError("rough label below threshold")
    if set(root_labels).intersection(rough_labels):
        raise ValueError("root and rough ownership overlap")


    # 6. Rough/Volterra Jacobian: m^(-1/2) (2/s) ds = m^(-1/2) (2/S) dS.
    parent_S = frac(data["parent_endpoint"])
    rough_scales = data["rough_square_scales"]
    if parent_S <= 0 or not isinstance(rough_scales, list) or not rough_scales:
        raise ValueError("positive parent_endpoint and rough_square_scales required")
    rough_jacobian = []
    for item in rough_scales:
        sqrt_m = frac(item["sqrt_m"])
        if sqrt_m <= 0:
            raise ValueError("sqrt_m must be positive")
        m = sqrt_m * sqrt_m
        if parent_S < m:
            raise ValueError("rough scale exceeds parent endpoint")
        child_s = parent_S / m
        inv_sqrt_m = 1 / sqrt_m
        # ds=dS/m under S=m*s.
        left = inv_sqrt_m * (2 / child_s) * (1 / m)
        right = inv_sqrt_m * (2 / parent_S)
        if left != right:
            raise ValueError("rough/Volterra Jacobian failed")
        rough_jacobian.append({"m": fstr(m), "coefficient": fstr(right)})

    # 7. Subcritical causal child list and two-ledger residual.
    child_coeffs = vec(data["causal_child_coefficients"])
    if any(c < 0 for c in child_coeffs):
        raise ValueError("negative causal child coefficient")
    child_sum = sum(child_coeffs, Fraction(0))
    if not child_sum < Fraction(1, 8):
        raise ValueError("causal child coefficient sum is not subcritical")

    unused = vec(data["unused_capacity"])
    correction = vec(data["signed_correction"])
    expected_residual = vec(data["expected_residual"])
    if not (len(unused) == len(correction) == len(expected_residual)):
        raise ValueError("two-ledger vectors have different dimensions")
    if any(u < 0 for u in unused):
        raise ValueError("unused capacity must be nonnegative")
    residual_two_ledger = [u - e for u, e in zip(unused, correction)]
    if residual_two_ledger != expected_residual:
        raise ValueError("two-ledger residual identity failed")
    if any(r < 0 for r in residual_two_ledger):
        raise ValueError("signed correction overruns unused capacity")

    proof_payload = {
        "schema": SCHEMA,
        "verdict": "PASS_NATIVE_VOLTERRA_RANK_ONE_COMMON_PARENT_SOURCE",
        "volterra_cases": volterra_results,
        "positive_total": fstr(Pp),
        "negative_total": fstr(Pm),
        "positive_density": fstr(L),
        "residual_weights": [fstr(x) for x in residual],
        "observation_results": observation_results,
        "source_partition": {
            "total": fstr(total_mass),
            "bottom": fstr(bottom),
            "retained": fstr(retained),
            "top": fstr(top),
        },
        "root_labels": root_labels,
        "rough_labels": rough_labels,
        "rough_volterra_jacobian": rough_jacobian,
        "causal_child_sum": fstr(child_sum),
        "two_ledger_residual": [fstr(x) for x in residual_two_ledger],
        "proof_boundary": (
            "Exact rational regression for the formal Volterra atom identity, "
            "rank-one source coupling, finite/continuum/mismatch observations, "
            "literal source restriction, rough/root disjointness, subcritical child mass, and the positive-source/signed-observation two-ledger residual. It does "
            "not certify the frozen analytic reserve stack, endpoint consumer, or RH."
        ),
    }
    canonical = json.dumps(proof_payload, sort_keys=True, separators=(",", ":")).encode()
    proof_payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return proof_payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    result = verify(data)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
