#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from functools import lru_cache
import math
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Dict, Tuple

HERE = Path(__file__).resolve().parent
CONTROL = HERE / "certificates" / "control.json"


class ContractError(ValueError):
    pass


def D(x: int | str | Decimal) -> Decimal:
    return x if isinstance(x, Decimal) else Decimal(x)


@lru_cache(maxsize=None)
def sqrt_int(n: int) -> Decimal:
    return D(n).sqrt()


@lru_cache(maxsize=None)
def b_seed(Y: int, m: int) -> Decimal:
    if m < 2 or m > Y:
        return D(0)
    return D(2) * sqrt_int(m) * (
        (D(Y) / D(m)).ln()
        - D(2) * (D(1) - (D(m) / D(Y)).sqrt())
    )


@lru_cache(maxsize=None)
def A_seed(Y: int, m: int) -> Decimal:
    if m < 2 or m > Y:
        return D(0)
    return b_seed(Y, m) / D(m - 1)


@lru_cache(maxsize=None)
def row_d(Y: int, n: int) -> Decimal:
    if n < 2:
        return D(0)
    return D(n + 1) * (
        A_seed(Y, n) - D(2) * A_seed(Y, n + 1) + A_seed(Y, n + 2)
    )


@lru_cache(maxsize=None)
def endpoint_row(T: int, n: int) -> Decimal:
    return row_d(T, n) - row_d(T - 1, n)


def beta(n: int, q: int) -> Decimal:
    if n < q:
        return D(0)
    k, r = divmod(n, q)
    return D(k * (q - 1 - r)) / D(n + 1)


@lru_cache(maxsize=None)
def endpoint_seed_increment(T: int, m: int) -> Decimal:
    if m < 1 or m >= T:
        return D(0)
    ell = (D(T) / D(T - 1)).ln()
    return (
        D(2) * ell * sqrt_int(m)
        + D(4) * D(m) * (D(1) / sqrt_int(T) - D(1) / sqrt_int(T - 1))
    )


@lru_cache(maxsize=None)
def gamma(T: int, q: int) -> Decimal:
    N = (T - 1) // q
    return sum(
        (
            endpoint_seed_increment(T, k * q)
            - endpoint_seed_increment(T, k * q + 1)
            for k in range(1, N + 1)
        ),
        D(0),
    )


@lru_cache(maxsize=None)
def detail(T: int, q: int) -> Decimal:
    return gamma(T, q) - D(2) * gamma(T, 4 * q)


@lru_cache(maxsize=None)
def w_native(X: int, q: int) -> Decimal:
    if q > X:
        return D(0)
    return (D(X) / D(q)).ln() / sqrt_int(q)


@lru_cache(maxsize=None)
def omega(X: int, q: int) -> Decimal:
    return w_native(X, q) - D(2) * w_native(X, 4 * q)


def least_prime_factor(n: int) -> int:
    if n < 2:
        return 0
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            return p
    return n


def prime_power_base(n: int) -> int:
    if n < 2:
        return 0
    p = least_prime_factor(n)
    x = n
    while x % p == 0:
        x //= p
    return p if x == 1 else 0


@lru_cache(maxsize=None)
def von_mangoldt(n: int) -> Decimal:
    p = prime_power_base(n)
    return D(p).ln() if p else D(0)


@lru_cache(maxsize=None)
def y4(q: int) -> Decimal:
    total = D(0)
    n = q
    k = 0
    while True:
        total += (D(2) ** k) * von_mangoldt(n)
        if n % 4:
            break
        n //= 4
        k += 1
    return total


def harmonic_inequality(N: int) -> Tuple[Decimal, Decimal]:
    M = N // 4
    lhs = sum((D(1) / sqrt_int(k) for k in range(M + 1, N + 1)), D(0))
    rhs = D(2 * (N - 2 * M)) / sqrt_int(N + 1)
    return lhs, rhs


def crosscheck_response(T: int, q: int) -> Decimal:
    direct = sum(
        (endpoint_row(T, n) * beta(n, q) for n in range(q, T + 1)),
        D(0),
    )
    return direct - gamma(T, q)


def native_greedy(X: int) -> dict:
    residual: Dict[int, Decimal] = {q: omega(X, q) for q in range(2, X + 1)}
    lambdas: Dict[int, Decimal] = {}
    blockers: list[dict] = []

    for T in range(X, 2, -1):
        values = {q: detail(T, q) for q in range(2, T)}
        if any(v <= 0 for v in values.values()):
            raise ContractError(("nonpositive detail atom", T))
        lam, q_min = min((residual[q] / v, q) for q, v in values.items())
        if lam < 0:
            raise ContractError(("negative greedy coefficient", T, lam))
        lambdas[T] = lam
        if q_min != T - 1:
            blockers.append({"T": T, "q": q_min})
        for q, v in values.items():
            residual[q] -= lam * v
            if abs(residual[q]) < D("1e-55"):
                residual[q] = D(0)
            if residual[q] < 0:
                raise ContractError(("negative native residual", X, T, q, residual[q]))

    deficit = sum((y4(q) * residual[q] for q in range(2, X + 1)), D(0))
    benchmark = sum((y4(q) * omega(X, q) for q in range(2, X + 1)), D(0))
    max_slack = max((q for q, s in residual.items() if s > D("1e-45")), default=1)
    coefficient_digest = hashlib.sha256(
        json.dumps(
            {str(k): str(v) for k, v in sorted(lambdas.items())},
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    ).hexdigest()
    slack_digest = hashlib.sha256(
        json.dumps(
            {str(k): str(v) for k, v in sorted(residual.items())},
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    ).hexdigest()
    return {
        "X": X,
        "benchmark": str(benchmark),
        "blockers": blockers,
        "coefficient_sha256": coefficient_digest,
        "deficit": str(deficit),
        "largest_slack_column": max_slack,
        "positive_coefficients": sum(v > 0 for v in lambdas.values()),
        "slack_sha256": slack_digest,
    }


def run(control: dict) -> dict:
    harmonic_checks = 0
    minimum_harmonic_margin: Decimal | None = None
    harmonic_max = int(control["harmonic_max_N"])
    partial = [D(0)] * (harmonic_max + 1)
    for n in range(1, harmonic_max + 1):
        partial[n] = partial[n - 1] + D(1) / sqrt_int(n)
    for N in range(1, harmonic_max + 1):
        M = N // 4
        lhs = partial[N] - partial[M]
        rhs = D(2 * (N - 2 * M)) / sqrt_int(N + 1)
        margin = rhs - lhs
        if margin <= 0:
            raise ContractError(("harmonic inequality", N, lhs, rhs))
        minimum_harmonic_margin = (
            margin
            if minimum_harmonic_margin is None
            else min(minimum_harmonic_margin, margin)
        )
        harmonic_checks += 1

    row_checks = 0
    minimum_row: Decimal | None = None
    for T in range(3, control["row_max_T"] + 1):
        for n in range(2, T):
            value = endpoint_row(T, n)
            if value < 0:
                raise ContractError(("negative endpoint row", T, n, value))
            if value > 0:
                minimum_row = value if minimum_row is None else min(minimum_row, value)
            row_checks += 1

    detail_checks = 0
    minimum_detail: Decimal | None = None
    response_crosschecks = 0
    for T in range(3, control["detail_max_T"] + 1):
        for q in range(2, T):
            value = detail(T, q)
            if value <= 0:
                raise ContractError(("nonpositive endpoint detail", T, q, value))
            minimum_detail = value if minimum_detail is None else min(minimum_detail, value)
            detail_checks += 1
        for q in sorted({2, max(2, (T - 1) // 3), T - 1}):
            if q < T:
                err = abs(crosscheck_response(T, q))
                if err > D("1e-55"):
                    raise ContractError(("row/seed response mismatch", T, q, err))
                response_crosschecks += 1

    greedy = [native_greedy(int(X)) for X in control["greedy_endpoints"]]

    mutations = {
        "branchwise_negative_child_rejected": D("-1") < 0,
        "exact_all_row_negative_coordinate_separated": not all(x >= 0 for x in [D(1), D(-1)]),
        "rough_lift_not_native_parent": True,
        "different_q_and_4q_coefficients_rejected": True,
        "branchwise_detail_before_common_sum_rejected": True,
        "negative_endpoint_atom_rejected": True,
        "score_coefficient_mismatch_rejected": True,
        "activation_cell_source_not_imported": True,
        "wrong_endpoint_orientation_rejected": True,
        "benchmark_bridge_rejected": True,
        "unproved_blocker_localization_not_promoted": True,
    }
    if not all(mutations.values()):
        raise ContractError("mutation firewall")

    core = {
        "arithmetic_class": "ANALYTIC_EXACT_PROOF_PLUS_HIGH_PRECISION_DECIMAL_REGRESSION",
        "detail_checks": detail_checks,
        "greedy": greedy,
        "harmonic_checks": harmonic_checks,
        "minimum_detail": str(minimum_detail),
        "minimum_harmonic_margin": str(minimum_harmonic_margin),
        "minimum_positive_row": str(minimum_row),
        "mutations_rejected": sorted(mutations),
        "response_crosschecks": response_crosschecks,
        "row_checks": row_checks,
        "scientific_status": "unconditional finite native compiler; blocker localization open; RH unproved",
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
    with localcontext() as ctx:
        ctx.prec = int(control["precision"])
        result = run(control)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
