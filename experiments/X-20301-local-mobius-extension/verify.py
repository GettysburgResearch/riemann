#!/usr/bin/env python3
"""Exact verifier for X-20301: local Möbius radical extension.

Standard library only. All arithmetic is fractions.Fraction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


class VerificationError(ValueError):
    """Fail-closed certificate rejection."""


def reject(condition: bool, message: str) -> None:
    if condition:
        raise VerificationError(message)


def parse_fraction(value: Any) -> Fraction:
    reject(isinstance(value, bool), "booleans are not rational numbers")
    if isinstance(value, int):
        return Fraction(value)
    reject(not isinstance(value, str), f"expected rational string, got {type(value).__name__}")
    text = value.strip()
    reject(not text, "empty rational string")
    try:
        return Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise VerificationError(f"invalid rational {value!r}") from exc


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_json_bytes(data: Any) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def mobius(n: int) -> int:
    reject(isinstance(n, bool) or not isinstance(n, int) or n < 1, "Möbius input must be a positive integer")
    x = n
    prime_count = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            prime_count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def parse_intervals(raw: Any, *, label: str) -> list[tuple[Fraction, Fraction, Fraction]]:
    reject(not isinstance(raw, list) or not raw, f"{label} must be a nonempty interval list")
    intervals: list[tuple[Fraction, Fraction, Fraction]] = []
    previous_right: Fraction | None = None
    for idx, row in enumerate(raw):
        reject(not isinstance(row, dict), f"{label}[{idx}] must be an object")
        reject(set(row) != {"left", "right", "value"}, f"{label}[{idx}] has unexpected fields")
        left = parse_fraction(row["left"])
        right = parse_fraction(row["right"])
        value = parse_fraction(row["value"])
        reject(left < 0 or right <= left, f"{label}[{idx}] has invalid endpoints")
        if previous_right is not None:
            reject(left < previous_right, f"{label} intervals overlap or are unordered")
        previous_right = right
        intervals.append((left, right, value))
    return intervals


def eval_piecewise(intervals: Iterable[tuple[Fraction, Fraction, Fraction]], x: Fraction) -> Fraction:
    for left, right, value in intervals:
        if left <= x < right:
            return value
    return Fraction(0)


def integral_piecewise(intervals: Iterable[tuple[Fraction, Fraction, Fraction]]) -> Fraction:
    return sum((right - left) * value for left, right, value in intervals)


def merge_breakpoints(intervals: Iterable[tuple[Fraction, Fraction, Fraction]]) -> set[Fraction]:
    points: set[Fraction] = set()
    for left, right, _ in intervals:
        points.add(left)
        points.add(right)
    return points


def ldl_pivots_symmetric(matrix: list[list[Fraction]]) -> list[Fraction]:
    n = len(matrix)
    reject(any(len(row) != n for row in matrix), "matrix must be square")
    reject(any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)), "matrix must be symmetric")
    work = [row[:] for row in matrix]
    pivots: list[Fraction] = []
    for k in range(n):
        pivot = work[k][k]
        reject(pivot <= 0, f"nonpositive LDL pivot at {k}")
        pivots.append(pivot)
        for i in range(k + 1, n):
            lik = work[i][k] / pivot
            for j in range(i, n):
                work[j][i] -= lik * work[j][k]
                work[i][j] = work[j][i]
    return pivots


def verify(certificate: dict[str, Any]) -> dict[str, Any]:
    expected_top = {
        "schema",
        "a",
        "b",
        "N",
        "g_intervals",
        "psi_intervals",
        "tail_samples",
        "graph_control",
        "formal_zero_control",
    }
    reject(set(certificate) != expected_top, "certificate top-level fields do not match schema")
    reject(certificate["schema"] != "riemann.x20301-local-mobius-extension.v1", "unsupported schema")

    a = parse_fraction(certificate["a"])
    b = parse_fraction(certificate["b"])
    reject(a <= 0 or b <= a, "require 0<a<b")

    N_raw = certificate["N"]
    reject(isinstance(N_raw, bool) or not isinstance(N_raw, int) or N_raw < 1, "N must be a positive integer")
    N = N_raw
    reject(Fraction(N) * a <= b, "certificate must use the strong safe cutoff N*a>b")

    g_intervals = parse_intervals(certificate["g_intervals"], label="g_intervals")
    psi_intervals = parse_intervals(certificate["psi_intervals"], label="psi_intervals")

    for left, right, _ in g_intervals:
        reject(left < a or right > b, "g must be supported inside [a,b]")
    for left, right, _ in psi_intervals:
        reject(left <= 0 or right >= a, "psi must be supported strictly inside (0,a)")

    g_integral = integral_piecewise(g_intervals)
    psi_integral = integral_piecewise(psi_intervals)
    reject(psi_integral != 1, "psi integral must equal one")

    mu = [0] + [mobius(n) for n in range(1, N + 1)]
    p_at_one = sum(Fraction(mu[n], n) for n in range(1, N + 1))
    correction = p_at_one * g_integral

    def g(x: Fraction) -> Fraction:
        return eval_piecewise(g_intervals, x)

    def psi(x: Fraction) -> Fraction:
        return eval_piecewise(psi_intervals, x)

    def source(x: Fraction) -> Fraction:
        return sum(Fraction(mu[n]) * g(Fraction(n) * x) for n in range(1, N + 1)) - correction * psi(x)

    source_integral = p_at_one * g_integral - correction * psi_integral
    reject(source_integral != 0, "source integral correction failed")
    min_source_support = min(
        [left / n for left, _, _ in g_intervals for n in range(1, N + 1) if mu[n] != 0]
        + [left for left, _, _ in psi_intervals]
    )
    reject(min_source_support <= 0, "source must vanish in a neighborhood of zero")

    source_breakpoints: set[Fraction] = set()
    for left, right, _ in g_intervals:
        for n in range(1, N + 1):
            if mu[n]:
                source_breakpoints.add(left / n)
                source_breakpoints.add(right / n)
    source_breakpoints |= merge_breakpoints(psi_intervals)
    max_source_support = max(source_breakpoints)

    def e_sum(u: Fraction) -> Fraction:
        reject(u <= 0, "dilation evaluation requires u>0")
        max_m = int(max_source_support // u) + 2
        return sum(source(Fraction(m) * u) for m in range(1, max_m + 1))

    reconstruction_points = {a, b} | {x for x in merge_breakpoints(g_intervals) if a <= x <= b}
    max_m_on_target = int(max_source_support // a) + 2
    for breakpoint in source_breakpoints:
        for m in range(1, max_m_on_target + 1):
            point = breakpoint / m
            if a <= point <= b:
                reconstruction_points.add(point)
    ordered = sorted(reconstruction_points)
    reconstruction_cells = 0
    for left, right in zip(ordered, ordered[1:]):
        if left == right:
            continue
        midpoint = (left + right) / 2
        reject(e_sum(midpoint) != g(midpoint), f"local reconstruction failed on cell ({left},{right})")
        reconstruction_cells += 1
    reject(reconstruction_cells == 0, "no reconstruction cells were checked")

    coefficient_rows: list[dict[str, int]] = []
    for k in range(1, 4 * N + 1):
        value = sum(mu[d] for d in range(1, N + 1) if k % d == 0)
        coefficient_rows.append({"k": k, "value": value})
        if k == 1:
            reject(value != 1, "A_N(1) must be one")
        elif k <= N:
            reject(value != 0, f"A_N({k}) must vanish")

    raw_samples = certificate["tail_samples"]
    reject(not isinstance(raw_samples, list) or not raw_samples, "tail_samples must be a nonempty list")
    replayed_samples: list[dict[str, Any]] = []
    for idx, row in enumerate(raw_samples):
        reject(not isinstance(row, dict) or set(row) != {"u", "expected_tail"}, f"tail_samples[{idx}] malformed")
        u = parse_fraction(row["u"])
        expected = parse_fraction(row["expected_tail"])
        reject(u <= 0 or u >= a, "tail samples must lie strictly below a")
        actual = e_sum(u) - g(u)
        reject(actual != expected, f"tail sample {idx} mismatch")
        replayed_samples.append({"u": fraction_json(u), "tail": fraction_json(actual)})

    graph = certificate["graph_control"]
    reject(not isinstance(graph, dict), "graph_control must be an object")
    reject(set(graph) != {"metric", "evaluation_R", "evaluation_W", "expected_kernel_vector"}, "graph_control fields mismatch")
    metric_raw = graph["metric"]
    reject(not isinstance(metric_raw, list), "graph metric must be a matrix")
    metric = [[parse_fraction(x) for x in row] for row in metric_raw]
    pivots = ldl_pivots_symmetric(metric)
    reject(len(metric) != 2, "synthetic graph metric must be 2x2")

    v_r = parse_fraction(graph["evaluation_R"])
    v_w = parse_fraction(graph["evaluation_W"])
    reject(v_w == 0, "visible evaluation must be invertible")
    expected_vector_raw = graph["expected_kernel_vector"]
    reject(not isinstance(expected_vector_raw, list) or len(expected_vector_raw) != 2, "expected kernel vector malformed")
    expected_vector = [parse_fraction(x) for x in expected_vector_raw]
    kernel_vector = [Fraction(1), -v_r / v_w]
    reject(kernel_vector != expected_vector, "graph kernel vector mismatch")
    reject(v_r * kernel_vector[0] + v_w * kernel_vector[1] != 0, "graph vector is not evaluation-invisible")
    graph_metric_norm = sum(kernel_vector[i] * metric[i][j] * kernel_vector[j] for i in range(2) for j in range(2))

    zero_control = certificate["formal_zero_control"]
    reject(not isinstance(zero_control, dict), "formal_zero_control must be an object")
    reject(set(zero_control) != {"target_evaluation", "expected_tail_evaluation"}, "formal_zero_control fields mismatch")
    target_evaluation = parse_fraction(zero_control["target_evaluation"])
    expected_tail_evaluation = parse_fraction(zero_control["expected_tail_evaluation"])
    formal_tail_evaluation = -target_evaluation
    reject(formal_tail_evaluation != expected_tail_evaluation, "formal zero residual mismatch")

    proof_object_sha256 = hashlib.sha256(canonical_json_bytes(certificate)).hexdigest()
    return {
        "schema": "riemann.x20301-local-mobius-extension.result.v1",
        "verified": True,
        "verdict": "CERTIFIED_EXACT_LOCAL_MOBIUS_RADICAL_EXTENSION",
        "safe_cutoff_slack": fraction_json(Fraction(N) * a - b),
        "mobius_values": mu[1:],
        "p_N_at_one": fraction_json(p_at_one),
        "target_g_integral": fraction_json(g_integral),
        "source_correction": fraction_json(correction),
        "source_integral": fraction_json(source_integral),
        "minimum_source_support": fraction_json(min_source_support),
        "reconstruction_cells": reconstruction_cells,
        "divisor_coefficients": coefficient_rows,
        "tail_samples": replayed_samples,
        "graph_metric_ldl_pivots": [fraction_json(x) for x in pivots],
        "graph_kernel_vector": [fraction_json(x) for x in kernel_vector],
        "graph_kernel_metric_norm": fraction_json(graph_metric_norm),
        "formal_zero_target_evaluation": fraction_json(target_evaluation),
        "formal_zero_tail_evaluation": fraction_json(formal_tail_evaluation),
        "proof_object_sha256": proof_object_sha256,
        "proof_boundary": (
            "Exact finite Möbius/divisor convolution, source cancellation, local reconstruction, "
            "graph-kernel algebra, and formal zero-multiplier identity only. The Riemann application "
            "still requires the E-map/Weil normalization and a cofinal form-metric bound for the "
            "explicit lower-tail operator."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
        reject(not isinstance(certificate, dict), "certificate root must be an object")
        result = verify(certificate)
    except (OSError, json.JSONDecodeError, VerificationError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, sort_keys=True))
        return 1

    rendered = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
