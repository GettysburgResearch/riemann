#!/usr/bin/env python3
"""Non-proof numerical reconnaissance for three LRPT closure routes.

This script intentionally uses binary64 arithmetic and a sparse parameter grid.
It must never be cited as a directed or exact certificate.
"""
from __future__ import annotations

import bisect
import json
import math
from collections import deque
from pathlib import Path

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
P_GRID = [67, 83, 101, 251, 1009]
Y_GRID = [1.0, 10.0, 30.0, 67.0]
J_GRID = [2, 10, 20, 40, 60, 66]


def divisors_with_mu():
    values = [(1, 1)]
    for prime in PRIMES:
        values += [(d * prime, -mu) for d, mu in list(values)]
    return sorted(values)


DIVISORS = divisors_with_mu()
DVALUES = [d for d, _ in DIVISORS]
MAX_N = max(int(p * y) for p in P_GRID for y in Y_GRID)
H = [0.0] * (MAX_N + 1)
L = [0.0] * (MAX_N + 1)
for n in range(1, MAX_N + 1):
    H[n] = H[n - 1] + n ** -0.5
    L[n] = L[n - 1] + math.log(n) * n ** -0.5


def component_q(endpoint, row):
    if endpoint < row:
        return 0.0
    n = int(math.floor(endpoint + 1e-12))
    log_endpoint = math.log(endpoint)

    def h(m):
        return 0.0 if m > endpoint else math.log(endpoint / m) / math.sqrt(m)

    h_row = h(row)
    h_next = h(row + 1)
    tail = 0.0
    if n >= row + 2:
        tail = log_endpoint * (H[n] - H[row + 1]) - (L[n] - L[row + 1])
    return (
        ((row + 1) / (row - 1)) * (h_row - h_next)
        + (2 * (row + 1) / (row * (row - 1))) * h_next
        + (2 / (row * (row - 1))) * tail
    )


def atoms(p, y, row):
    r = p ** -0.5
    x = p * y
    sqrt_x = math.sqrt(x)
    sqrt_y = math.sqrt(y)
    output = []
    for d, mu in DIVISORS[: bisect.bisect_right(DVALUES, x + 1e-12)]:
        score = 5 * sqrt_x / d - 3 / math.sqrt(d)
        if d <= y + 1e-12:
            score -= r * (5 * sqrt_y / d - 3 / math.sqrt(d))
        component = component_q(x / d, row) / math.sqrt(d)
        if d <= y + 1e-12:
            component -= r * component_q(y / d, row) / math.sqrt(d)
        output.append((d, mu, score, component))
    return output


def lorenz_metrics(p, y, row):
    data = atoms(p, y, row)
    odd_score = sum(score for _, mu, score, _ in data if mu == -1)
    remaining = odd_score
    removed = []
    cutoff = None
    for d, mu, score, component in data:
        if mu != 1:
            continue
        take = min(remaining, score)
        if take > 0:
            removed.append((take, component / score if score else 0.0))
            remaining -= take
            cutoff = d
        if remaining <= 1e-10:
            break

    signed_score = sum(mu * score for _, mu, score, _ in data)
    signed_row = sum(mu * component for _, mu, _, component in data)
    even_row = sum(component for _, mu, _, component in data if mu == 1)
    residual_row = even_row - sum(take * ratio for take, ratio in removed)
    cutoff_atom = next(atom for atom in data if atom[0] == cutoff)
    determinant = signed_row * cutoff_atom[2] - signed_score * cutoff_atom[3]

    even_score = sum(score for _, mu, score, _ in data if mu == 1)
    odd_row = sum(component for _, mu, _, component in data if mu == -1)
    full_determinant = even_row * odd_score - even_score * odd_row
    return data, cutoff, determinant, full_determinant, signed_row - residual_row


def inner_discrete_gap(data, y):
    evens = [(d, component / score) for d, mu, score, component in data if mu == 1 and d <= y and score > 0]
    odds = [(d, component / score) for d, mu, score, component in data if mu == -1 and d <= y and score > 0]
    best = float("inf")
    for e, q_e in evens:
        for o, q_o in odds:
            if e <= o:
                best = min(best, q_e - q_o)
    return best


def greedy_shift_eight_gain(data):
    evens = [
        {"d": d, "capacity": score, "ratio": component / score}
        for d, mu, score, component in data
        if mu == 1 and score > 0
    ]
    odds = [
        {"d": d, "demand": score, "ratio": component / score}
        for d, mu, score, component in data
        if mu == -1 and score > 0
    ]
    available = deque()
    even_index = 0
    gain = 0.0
    max_upward = 0
    for odd in odds:
        while even_index < len(evens) and evens[even_index]["d"] <= odd["d"] + 8:
            available.append(evens[even_index])
            even_index += 1
        remaining = odd["demand"]
        while remaining > 1e-9:
            while available and available[0]["capacity"] <= 1e-12:
                available.popleft()
            if not available:
                raise AssertionError("grid point failed shifted-eight Hall")
            even = available[0]
            take = min(remaining, even["capacity"])
            gain += take * (even["ratio"] - odd["ratio"])
            max_upward = max(max_upward, even["d"] - odd["d"])
            even["capacity"] -= take
            remaining -= take
    return gain, max_upward


def main():
    minima = {
        "cutoff_determinant": [float("inf"), None],
        "full_even_odd_determinant": [float("inf"), None],
        "literal_lorenz_row_gap": [float("inf"), None],
        "inner_discrete_order_gap": [float("inf"), None],
        "shift8_greedy_row_gain": [float("inf"), None],
    }
    largest_upward = 0
    cases = 0
    for p in P_GRID:
        for y in Y_GRID:
            for row in J_GRID:
                data, cutoff, determinant, full_determinant, row_gap = lorenz_metrics(p, y, row)
                inner_gap = inner_discrete_gap(data, y)
                flow_gain, upward = greedy_shift_eight_gain(data)
                largest_upward = max(largest_upward, upward)
                values = [
                    ("cutoff_determinant", determinant),
                    ("full_even_odd_determinant", full_determinant),
                    ("literal_lorenz_row_gap", row_gap),
                    ("inner_discrete_order_gap", inner_gap),
                    ("shift8_greedy_row_gain", flow_gain),
                ]
                for name, value in values:
                    if math.isfinite(value) and value < minima[name][0]:
                        minima[name] = [value, {"p": p, "y": y, "j": row, "cutoff": cutoff}]
                cases += 1

    result = {
        "classification": "EMPIRICAL_THREE_ROUTE_RECONNAISSANCE_ONLY",
        "proof_status": "NOT_A_PROOF_OBJECT",
        "cases": cases,
        "p_grid": P_GRID,
        "y_grid": Y_GRID,
        "j_grid": J_GRID,
        "minima": minima,
        "largest_upward_edge_used_by_left_greedy": largest_upward,
        "scope": "Binary64 sparse-grid reconnaissance. It supports route selection only and proves no all-parameter inequality or RH.",
    }
    output = Path(__file__).resolve().parent / "results" / "reconnaissance.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
