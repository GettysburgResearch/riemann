#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def shift(values: list[Fraction], dilation: int) -> list[Fraction]:
    return [values[x // dilation] for x in range(len(values))]


def add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return [x + y for x, y in zip(a, b)]


def subtract(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return [x - y for x, y in zip(a, b)]


def scale(c: Fraction, values: list[Fraction]) -> list[Fraction]:
    return [c * x for x in values]


def euler(values: list[Fraction], prime: int) -> list[Fraction]:
    return subtract(values, scale(Fraction(1, prime), shift(values, prime)))


def scale_filter_four(values: list[Fraction]) -> list[Fraction]:
    # Normalized form of A(X)-A(X/4): U(X)-1/2 U(X/4).
    return subtract(values, scale(Fraction(1, 2), shift(values, 4)))


def apply_euler(values: list[Fraction], primes: list[int]) -> list[Fraction]:
    result = values
    for prime in primes:
        result = euler(result, prime)
    return result


def product(values) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def full_omitted(
    low_state: list[Fraction],
    high_primes: list[int],
    omitted: set[int],
) -> list[Fraction]:
    return apply_euler(low_state, [p for p in high_primes if p not in omitted])


def exact_fixture() -> dict:
    limit = 840
    base = [Fraction(0)]
    base.extend(
        Fraction(((x * x + 3 * x + 7) % 23) - 11, 7)
        for x in range(1, limit + 1)
    )
    low_primes = [5, 7]
    high_primes = [11, 13, 17, 19]

    low = apply_euler(base, low_primes)
    full = apply_euler(low, high_primes)

    # The additional factor-four scale filter commutes with every Euler factor.
    assert apply_euler(scale_filter_four(base), low_primes + high_primes) == (
        scale_filter_four(apply_euler(base, low_primes + high_primes))
    )

    # Largest-prime Bellman telescoping.
    state = low
    budget = [Fraction(0)] * (limit + 1)
    for prime in high_primes:
        budget = add(
            budget,
            scale(Fraction(1, prime), shift(state, prime)),
        )
        state = euler(state, prime)
    assert state == full
    assert full == subtract(low, budget)

    # Exact top-history completion:
    # prod_{q>p}(E_q+q^{-1}T_q)=I.
    top_completion_checks = 0
    mutation_rejected = False
    for index, prime in enumerate(high_primes):
        before = apply_euler(low, high_primes[:index])
        larger = high_primes[index + 1 :]
        reconstructed = [Fraction(0)] * (limit + 1)
        wrong = [Fraction(0)] * (limit + 1)
        for size in range(len(larger) + 1):
            for selected in combinations(larger, size):
                q_selected = product(selected)
                omitted = set(selected) | {prime}
                term = shift(
                    full_omitted(low, high_primes, omitted),
                    q_selected,
                )
                reconstructed = add(
                    reconstructed,
                    scale(Fraction(1, q_selected), term),
                )
                # Hostile mutation: square one top-history coefficient.
                wrong = add(
                    wrong,
                    scale(Fraction(1, q_selected * q_selected), term),
                )
                top_completion_checks += 1
        assert reconstructed == before
        if wrong != before:
            mutation_rejected = True
    assert mutation_rejected

    # Summing owner p and its top set gives each nonempty high-prime subset once.
    subset_budget = [Fraction(0)] * (limit + 1)
    subset_count = 0
    seen: set[tuple[int, ...]] = set()
    for size in range(1, len(high_primes) + 1):
        for chosen in combinations(high_primes, size):
            assert chosen not in seen
            seen.add(chosen)
            q_chosen = product(chosen)
            term = shift(
                full_omitted(low, high_primes, set(chosen)),
                q_chosen,
            )
            subset_budget = add(
                subset_budget,
                scale(Fraction(1, q_chosen), term),
            )
            subset_count += 1
    assert subset_budget == budget
    assert subset_count == 2 ** len(high_primes) - 1

    # At a terminal endpoint below every omitted prime, omitted and full states
    # coincide literally.
    boundary_cutoff = 10
    assert min(high_primes) > boundary_cutoff
    for size in range(1, len(high_primes) + 1):
        for omitted_tuple in combinations(high_primes, size):
            omitted_state = full_omitted(
                low,
                high_primes,
                set(omitted_tuple),
            )
            for endpoint in range(boundary_cutoff + 1):
                assert omitted_state[endpoint] == full[endpoint]

    # Asymptotic coordinates: b(Y)=a sqrt(Y)+c+...
    # b(Y)-b(Y/4)=(a/2)sqrt(Y)+0+...
    a = Fraction(37, 11)
    c = Fraction(-19, 13)
    filtered_sqrt = a - Fraction(1, 2) * a
    filtered_constant = c - c
    assert filtered_sqrt == a / 2
    assert filtered_constant == 0

    root = 731
    low_root = low[root]
    corridor_primes = [11, 13]
    high_only_primes = [17, 19]
    state = low
    corridor_budget = Fraction(0)
    high_budget = Fraction(0)
    for prime in high_primes:
        term = Fraction(1, prime) * state[root // prime]
        if prime in corridor_primes:
            corridor_budget += term
        elif prime in high_only_primes:
            high_budget += term
        else:
            raise AssertionError("unclassified prime")
        state = euler(state, prime)
    assert state[root] == low_root - corridor_budget - high_budget

    return {
        "limit": limit,
        "low_primes": low_primes,
        "high_primes": high_primes,
        "scale_filter_commutes_with_euler": True,
        "largest_prime_bellman_exact": True,
        "top_history_completion_exact": True,
        "top_completion_checks": top_completion_checks,
        "nonempty_subset_owners": subset_count,
        "unique_subset_ownership": True,
        "boundary_omitted_factors_inactive": True,
        "constant_term_cancelled": True,
        "sqrt_main_retained_fraction": "1/2",
        "budget_partition_exact": True,
        "hostile_coefficient_mutation_rejected": mutation_rejected,
    }


def asymptotic_parameter_diagnostics() -> dict:
    ell = 20.0
    log_x = math.exp(ell)

    quadratic_z = log_x * log_x * ell
    half_weight_log_bound = 2.0 * math.sqrt(quadratic_z) / math.log(quadratic_z)

    k_subpower = ell * ell
    log_z_subpower = log_x / k_subpower
    log_l_subpower = k_subpower
    eta = math.log(k_subpower) / log_z_subpower
    rankin_exponent = eta * (log_x - log_l_subpower)

    log_h_quasipoly = ell ** 4
    log_l_quasipoly = ell ** 2

    assert half_weight_log_bound < 0.5 * log_x
    assert log_z_subpower > log_l_subpower
    assert 0.0 < eta < 0.5
    assert rankin_exponent > k_subpower
    assert log_h_quasipoly > log_l_quasipoly
    assert log_l_quasipoly / log_h_quasipoly == 1.0 / (ell * ell)

    return {
        "diagnostic_loglog_X": ell,
        "quadratic_log_cube_half_weight_below_sqrtX": True,
        "subpower_log_Z_gt_log_L": True,
        "rankin_eta_in_0_half": True,
        "rankin_exponent_gt_K": True,
        "quasipoly_boundary_ratio": "1/(loglog X)^2",
        "classification": "PARAMETER_HIERARCHY_DIAGNOSTIC_ONLY",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "results" / "verification.json",
    )
    args = parser.parse_args()

    payload = {
        "schema": "riemann.x97900.log-cube-boundary.v1",
        "exact_algebra": exact_fixture(),
        "parameter_diagnostics": asymptotic_parameter_diagnostics(),
        "analytic_theorems_replayed": False,
        "pnt_replayed": False,
        "upper_bound_sieve_replayed": False,
        "lscb67_proved": False,
        "fabp67_proved": False,
        "rh_established": False,
        "verdict": "PASS_X_97900_LOG_CUBE_AND_BOUNDARY_ALGEBRA",
    }
    canonical = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
