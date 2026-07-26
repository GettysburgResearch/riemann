#!/usr/bin/env python3
"""Exact verifier for witness-adapted total-zero count dual certificates.

The checker uses only Python integers and fractions.Fraction. It evaluates no
special function. Direct completed-xi rectangles enter only through intervals
for H_T(u)=|xi(1/2+sqrt(u)+iT)|^2.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.xi-witness-adapted-count-dual.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
COUNT_GATE = "UNCONDITIONAL_TOTAL_ZERO_COUNT_EXACT"


class CertificateError(ValueError):
    pass


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("reversed interval")

    def sub(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def scale(self, value: Fraction) -> "Interval":
        if value >= 0:
            return Interval(self.lower * value, self.upper * value)
        return Interval(self.upper * value, self.lower * value)


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    n = exact_int(raw.get("numerator"), f"{name}.numerator")
    d = exact_int(raw.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Interval(rational(raw.get("lower"), f"{name}.lower"), rational(raw.get("upper"), f"{name}.upper"))


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def ij(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fj(value.lower), "upper": fj(value.upper)}


def canonical_sha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")).hexdigest()


def require_sha(value: Any, name: str) -> str:
    if not isinstance(value, str) or len(value) != 64:
        raise CertificateError(f"{name} must be a 64-character SHA-256")
    try:
        int(value, 16)
    except ValueError as exc:
        raise CertificateError(f"{name} is not hexadecimal") from exc
    return value.lower()


def atanh_log_unit_interval(x: Fraction, terms: int) -> Interval:
    """Enclose log(x) for 1 <= x < 2 by the positive atanh series."""
    if not (Fraction(1) <= x <= Fraction(2)):
        raise CertificateError("internal log reduction failed")
    if terms < 8:
        raise CertificateError("log_terms must be at least 8")
    z = (x - 1) / (x + 1)
    total = Fraction(0)
    power = z
    z2 = z * z
    for j in range(terms):
        total += power / (2 * j + 1)
        power *= z2
    lower = 2 * total
    tail = Fraction(0) if z == 0 else 2 * power / ((2 * terms + 1) * (1 - z2))
    return Interval(lower, lower + tail)


def log_fraction(x: Fraction, terms: int) -> Interval:
    if x <= 0:
        raise CertificateError("log argument must be positive")
    r = x
    k = 0
    while r >= 2:
        r /= 2
        k += 1
    while r < 1:
        r *= 2
        k -= 1
    unit = atanh_log_unit_interval(r, terms)
    log2 = atanh_log_unit_interval(Fraction(2), terms)
    return unit.sub(log2.scale(-k)) if k < 0 else Interval(unit.lower + k * log2.lower, unit.upper + k * log2.upper)


def log_ratio_interval(numerator: Interval, denominator: Interval, terms: int) -> Interval:
    if numerator.lower <= 0 or denominator.lower <= 0:
        raise CertificateError("modulus-square interval must be strictly positive")
    lo = log_fraction(numerator.lower / denominator.upper, terms)
    hi = log_fraction(numerator.upper / denominator.lower, terms)
    return Interval(lo.lower, hi.upper)


def parse_atoms(raw: Any) -> list[dict[str, Any]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError("atoms must be a nonempty list")
    atoms: list[dict[str, Any]] = []
    seen: set[str] = set()
    previous_upper: Fraction | None = None
    for i, item in enumerate(raw):
        if not isinstance(item, dict):
            raise CertificateError(f"atoms[{i}] must be an object")
        atom_id = item.get("id")
        if not isinstance(atom_id, str) or not atom_id or atom_id in seen:
            raise CertificateError("invalid or duplicate atom id")
        lower = rational(item.get("lower_offset"), f"atoms[{i}].lower_offset")
        upper = rational(item.get("upper_offset"), f"atoms[{i}].upper_offset")
        if lower > upper:
            raise CertificateError("atom lower exceeds upper")
        if previous_upper is not None and lower < previous_upper:
            raise CertificateError("atoms overlap or are out of order")
        previous_upper = upper
        seen.add(atom_id)
        atoms.append({"id": atom_id, "lower": lower, "upper": upper})
    return atoms


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("bad schema")
    if data.get("normalization_id") != NORMALIZATION:
        raise CertificateError("normalization mismatch")
    classification = data.get("classification")
    if classification not in ("SYNTHETIC_MODEL", "RIEMANN_XI_DIRECTED"):
        raise CertificateError("unsupported classification")
    terms = exact_int(data.get("log_terms", 160), "log_terms")
    primitive_sha = require_sha(data.get("primitive_table_sha256"), "primitive_table_sha256")
    count_sha = require_sha(data.get("count_table_sha256"), "count_table_sha256")

    nodes = data.get("nodes")
    if not isinstance(nodes, dict):
        raise CertificateError("nodes missing")
    u = rational(nodes.get("u"), "nodes.u")
    v = rational(nodes.get("v"), "nodes.v")
    if not (0 < u < v):
        raise CertificateError("require 0<u<v")

    h = data.get("h_intervals")
    if not isinstance(h, dict):
        raise CertificateError("h_intervals missing")
    h_u = interval(h.get("u"), "h_intervals.u")
    h_v = interval(h.get("v"), "h_intervals.v")
    raw = log_ratio_interval(h_v, h_u, terms)

    atoms = parse_atoms(data.get("atoms"))
    atom_index = {atom["id"]: i for i, atom in enumerate(atoms)}

    windows_raw = data.get("count_windows")
    if not isinstance(windows_raw, list) or not windows_raw:
        raise CertificateError("count_windows must be nonempty")
    windows: list[dict[str, Any]] = []
    window_ids: set[str] = set()
    for i, item in enumerate(windows_raw):
        if not isinstance(item, dict):
            raise CertificateError("malformed count window")
        window_id = item.get("id")
        if not isinstance(window_id, str) or not window_id or window_id in window_ids:
            raise CertificateError("invalid or duplicate count window id")
        window_ids.add(window_id)
        if item.get("gate") != COUNT_GATE:
            raise CertificateError("count semantic gate mismatch")
        ids = item.get("atoms")
        if not isinstance(ids, list) or not ids or any(atom_id not in atom_index for atom_id in ids):
            raise CertificateError("bad count window atom list")
        indices = [atom_index[x] for x in ids]
        if indices != list(range(indices[0], indices[-1] + 1)):
            raise CertificateError("count windows must be consecutive in atom order")
        count = exact_int(item.get("count"), f"count_windows[{i}].count")
        if count < 0:
            raise CertificateError("negative count")
        digest = require_sha(item.get("proof_gate_sha256"), f"count_windows[{i}].proof_gate_sha256")
        windows.append({"id": window_id, "ids": ids, "indices": indices, "count": count, "digest": digest})

    declared_costs = data.get("cell_cost_lower_bounds")
    if not isinstance(declared_costs, list) or len(declared_costs) != len(atoms):
        raise CertificateError("wrong cell cost count")
    costs: list[Fraction] = []
    exact_cell_costs: list[Interval] = []
    for i, (atom, raw_cost) in enumerate(zip(atoms, declared_costs)):
        cost = rational(raw_cost, f"cell_cost_lower_bounds[{i}]")
        if cost < 0:
            raise CertificateError("cell cost must be nonnegative")
        B = max(atom["lower"] * atom["lower"], atom["upper"] * atom["upper"])
        exact_cost = log_fraction((v + B) / (u + B), terms)
        if cost > exact_cost.lower:
            raise CertificateError("declared cell cost is not a proved lower bound")
        costs.append(cost)
        exact_cell_costs.append(exact_cost)

    primal = data.get("primal")
    dual = data.get("dual")
    if not isinstance(primal, dict) or not isinstance(dual, dict):
        raise CertificateError("primal and dual certificates are required")
    counts_raw = primal.get("atom_counts")
    if not isinstance(counts_raw, list) or len(counts_raw) != len(atoms):
        raise CertificateError("bad primal atom counts")
    x = [exact_int(value, f"primal.atom_counts[{i}]") for i, value in enumerate(counts_raw)]
    if any(value < 0 for value in x):
        raise CertificateError("primal counts must be nonnegative")
    for window in windows:
        if sum(x[j] for j in window["indices"]) != window["count"]:
            raise CertificateError("primal count equation failed")
    primal_objective = sum(cost * count for cost, count in zip(costs, x))

    def verify_dual(raw_dual: Any, name: str) -> tuple[list[Fraction], Fraction]:
        if not isinstance(raw_dual, dict):
            raise CertificateError(f"{name} must be an object")
        raw_lambdas = raw_dual.get("lambdas")
        if not isinstance(raw_lambdas, list) or len(raw_lambdas) != len(windows):
            raise CertificateError(f"bad {name} lambda count")
        values = [rational(value, f"{name}.lambdas[{i}]") for i, value in enumerate(raw_lambdas)]
        for j in range(len(atoms)):
            load = sum(values[r] for r, window in enumerate(windows) if j in window["indices"])
            if load > costs[j]:
                raise CertificateError(f"{name} atom inequality failed")
        objective = sum(values[r] * window["count"] for r, window in enumerate(windows))
        return values, objective

    lambdas, dual_objective = verify_dual(dual, "dual")
    if primal_objective != dual_objective:
        raise CertificateError("primal and dual objectives differ")
    _, coarse = verify_dual(data.get("coarse_dual"), "coarse_dual")
    if coarse < 0 or coarse > dual_objective:
        raise CertificateError("coarse dual objective must lie between zero and the optimum")

    coarse_residual = raw.sub(Interval(coarse, coarse))
    adapted_residual = raw.sub(Interval(dual_objective, dual_objective))

    def status(value: Interval) -> str:
        if value.upper < 0:
            return "CERTIFIED_NEGATIVE"
        if value.lower >= 0:
            return "CERTIFIED_NONNEGATIVE"
        return "UNRESOLVED"

    rows = [
        {"id": "raw-log-monotonicity", "interval": ij(raw), "status": status(raw)},
        {"id": "coarse-count-deflation", "interval": ij(coarse_residual), "status": status(coarse_residual)},
        {"id": "witness-adapted-dual-deflation", "interval": ij(adapted_residual), "status": status(adapted_residual)},
    ]
    negative = sum(row["status"] == "CERTIFIED_NEGATIVE" for row in rows)
    if classification == "RIEMANN_XI_DIRECTED" and adapted_residual.upper < 0:
        verdict = "NEGATIVE_RIEMANN_XI_WITNESS_PENDING_REPRODUCTION_AND_REVIEW"
    elif classification == "SYNTHETIC_MODEL" and adapted_residual.upper < 0:
        verdict = "SYNTHETIC_STRICT_SEPARATION"
    elif any(row["status"] == "UNRESOLVED" for row in rows):
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_ADAPTED_ROW"

    return {
        "schema": SCHEMA,
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "primitive_table_sha256": primitive_sha,
        "count_table_sha256": count_sha,
        "raw_log_interval": ij(raw),
        "cell_exact_cost_intervals": [ij(value) for value in exact_cell_costs],
        "declared_cell_lower_costs": [fj(value) for value in costs],
        "primal_objective": fj(primal_objective),
        "dual_objective": fj(dual_objective),
        "coarse_safe_subtraction": fj(coarse),
        "rows": rows,
        "certified_negative_rows": negative,
        "verdict": verdict,
        "scope_warning": (
            "The checker proves exact finite contraction and LP duality only. A Riemann-xi negative "
            "requires directed completed-xi rectangles, unconditional exact total-zero count gates, "
            "and independent review of the analytic normalization and L-9305."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level certificate must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result["verdict"] != "UNRESOLVED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
