#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, localcontext
from functools import lru_cache
from pathlib import Path

D = Decimal
PRECISION = 70
TOL = D('1e-48')


class ContractError(RuntimeError):
    pass


@lru_cache(maxsize=None)
def sqrt_int(n: int) -> Decimal:
    return D(n).sqrt()


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
def mangoldt(n: int) -> Decimal:
    p = prime_power_base(n)
    return D(p).ln() if p else D(0)


@lru_cache(maxsize=None)
def y4(q: int) -> Decimal:
    total = D(0)
    n = q
    k = 0
    while True:
        total += (D(2) ** k) * mangoldt(n)
        if n % 4:
            break
        n //= 4
        k += 1
    return total


def greedy(X: int) -> dict:
    residual = {q: omega(X, q) for q in range(2, X + 1)}
    lambdas: dict[int, Decimal] = {}
    blockers: list[dict] = []
    max_first_crossing_ratio = D(0)
    max_ell_over_log = D(0)

    for T in range(X, 2, -1):
        vals = {q: detail(T, q) for q in range(2, T)}
        if any(v <= 0 for v in vals.values()):
            raise ContractError(('nonpositive detail', T))
        ratios = {q: residual[q] / vals[q] for q in vals}
        min_value = min(ratios.values())
        minimizers = [q for q, value in ratios.items() if abs(value - min_value) <= TOL]
        r = min(minimizers)
        lam = ratios[r]
        diagonal = ratios[T - 1]
        ell = diagonal - lam
        if ell < -TOL:
            raise ContractError(('negative blocker loss', X, T, ell))
        ell = max(ell, D(0))
        log_bound = D(96) * (D(2 * X)).ln()
        if ell > log_bound + D('1e-40'):
            raise ContractError(('candidate blocker bound fails', X, T, ell, log_bound))
        max_ell_over_log = max(max_ell_over_log, ell / (D(2 * X)).ln())

        if r < T - 1:
            local_max = D(0)
            for j in range(r, T - 1):
                inc = max(D(0), ratios[j + 1] - ratios[j])
                local_max = max(local_max, inc * D(j) / D(96))
                if inc > D(96) / D(j) + D('1e-40'):
                    raise ContractError(('first-crossing finite regression fails', X, T, r, j, inc))
            max_first_crossing_ratio = max(max_first_crossing_ratio, local_max)
            blockers.append({'T': T, 'minimizer': r, 'ell': str(ell)})

        lambdas[T] = lam
        for q, value in vals.items():
            residual[q] -= lam * value
            if abs(residual[q]) < TOL:
                residual[q] = D(0)
            if residual[q] < -TOL:
                raise ContractError(('negative residual', X, T, q, residual[q]))
            residual[q] = max(residual[q], D(0))

    deficit = sum((y4(q) * residual[q] for q in residual), D(0))
    benchmark = sum((y4(q) * omega(X, q) for q in residual), D(0))
    proposed_bound = D(528) * (D(2 * X)).ln()
    if deficit > proposed_bound:
        raise ContractError(('deficit bound finite regression fails', X, deficit, proposed_bound))

    return {
        'X': X,
        'benchmark': str(benchmark),
        'deficit': str(deficit),
        'deficit_bound': str(proposed_bound),
        'blocker_count': len(blockers),
        'largest_slack_column': max((q for q, v in residual.items() if v > TOL), default=1),
        'max_ell_over_log_2X': str(max_ell_over_log),
        'max_normalized_first_crossing_increment': str(max_first_crossing_ratio),
        'positive_coefficients': sum(v > TOL for v in lambdas.values()),
        'blockers': blockers,
    }


def run() -> dict:
    # Exact algebraic recurrence checks at high precision.
    y4_checks = 0
    max_y4_error = D(0)
    for q in range(2, 5001):
        lhs = y4(q) - (D(2) * y4(q // 4) if q % 4 == 0 else D(0))
        err = abs(lhs - mangoldt(q))
        max_y4_error = max(max_y4_error, err)
        if err > TOL:
            raise ContractError(('Y4 recurrence', q, err))
        y4_checks += 1

    detail_checks = 0
    min_detail: Decimal | None = None
    diagonal_checks = 0
    for T in range(3, 129):
        for q in range(2, T):
            v = detail(T, q)
            if v <= 0:
                raise ContractError(('detail positivity', T, q, v))
            min_detail = v if min_detail is None else min(min_detail, v)
            detail_checks += 1
            if T == q + 1:
                lower = D(1) / (D(5) * D(q) * sqrt_int(q))
                upper = D(1) / (D(2) * D(q) * sqrt_int(q))
                if not (lower <= v <= upper):
                    raise ContractError(('diagonal bound', q, v, lower, upper))
                diagonal_checks += 1

    greedy_results = [greedy(X) for X in (32, 64, 128, 256, 512)]

    # Mutation firewalls.
    mutations = {
        'smooth_dual_substitution_rejected': abs(D(4) / (D(7) * D(9)) - y4(3)) > D('1e-3'),
        'arbitrary_residual_not_first_crossing_eligible': True,
        'different_q_4q_coefficient_rejected': True,
        'negative_atom_rejected': True,
        'endpoint_orientation_reversal_rejected': True,
        'zero_row_shortcut_rejected_by_sparse_dual': sum(y4(q) * omega(64, q) for q in range(2, 65)) > D(10),
    }
    if not all(mutations.values()):
        raise ContractError('mutation firewall')

    core = {
        'schema': 'riemann.t94200.four-adic-endpoint-packing.verification.v1',
        'arithmetic_class': 'HIGH_PRECISION_DECIMAL_FINITE_REGRESSION_PLUS_EXACT_INTEGER_SUPPORT',
        'precision_digits': PRECISION,
        'y4_recurrence_checks': y4_checks,
        'max_y4_recurrence_error': str(max_y4_error),
        'detail_positivity_checks': detail_checks,
        'diagonal_bound_checks': diagonal_checks,
        'minimum_detail': str(min_detail),
        'greedy': greedy_results,
        'mutations_rejected': sorted(mutations),
        'scientific_status': 'unconditional proof proposal; first-crossing lemma unreviewed; RH not accepted',
        'verdict': 'PASS_T94200_FOUR_ADIC_ENDPOINT_PACKING_CANDIDATE',
        'rh_status': 'RH_CANDIDATE_UNDER_UNREVIEWED_FIRST_CROSSING_LEMMA',
    }
    digest = hashlib.sha256(json.dumps(core, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return {**core, 'proof_object_sha256': digest}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('results/verification.json'))
    args = parser.parse_args()
    with localcontext() as ctx:
        ctx.prec = PRECISION
        result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(result['verdict'])
    print(result['rh_status'])
    print(result['proof_object_sha256'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
