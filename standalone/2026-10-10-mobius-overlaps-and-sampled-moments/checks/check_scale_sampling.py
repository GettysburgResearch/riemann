#!/usr/bin/env python3
"""Exact finite sampling guards; not a proof of the infinite sampling theorem."""

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from math import factorial
from pathlib import Path


COUNTS = Counter()
ZERO = (F(0), F(0))


def require(condition, category, detail=""):
    COUNTS[category] += 1
    if not condition:
        raise RuntimeError(category + ": " + detail)


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def zsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def zscale(a, r):
    return (a[0] * r, a[1] * r)


def znorm2(a):
    return a[0] * a[0] + a[1] * a[1]


def peval(coefficients, x):
    result = ZERO
    for coefficient in reversed(coefficients):
        result = zadd(zscale(result, x), coefficient)
    return result


def real_mul(a, b):
    result = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return result


def basis(nodes, j, x):
    numerator, denominator = F(1), F(1)
    for i, node in enumerate(nodes):
        if i != j:
            numerator *= x - node
            denominator *= nodes[j] - node
    return numerator / denominator


def interpolant(nodes, values):
    result = [ZERO] * len(nodes)
    for j, value in enumerate(values):
        numerator, denominator = [F(1)], F(1)
        for i, node in enumerate(nodes):
            if i != j:
                numerator = real_mul(numerator, [-node, F(1)])
                denominator *= nodes[j] - node
        for i, coefficient in enumerate(numerator):
            result[i] = zadd(result[i], zscale(value, coefficient / denominator))
    return result


def integrate_norm2(coefficients, intervals):
    answer = F(0)
    for left, right in intervals:
        for i, a in enumerate(coefficients):
            for j, b in enumerate(coefficients):
                exponent = i + j + 1
                real_inner = a[0] * b[0] + a[1] * b[1]
                answer += real_inner * (right ** exponent - left ** exponent) / exponent
    return answer


def measure(intervals):
    return sum((b - a for a, b in intervals), F(0))


def quantile_nodes(intervals, m):
    total = measure(intervals)
    nodes = []
    for j in range(m):
        target = F(2 * j + 1, 2 * m) * total
        used = F(0)
        for left, right in intervals:
            if target <= used + right - left:
                nodes.append(left + target - used)
                break
            used += right - left
        else:
            raise RuntimeError("quantile construction missed the retained set")
    return nodes


def complex_polynomial(degree):
    return [
        (F((-1) ** i * (i + 1), degree + 3),
         F(i * i + 2, 2 * degree + 5))
        for i in range(degree + 1)
    ]


def derivative_real(coefficients):
    return [i * coefficients[i] for i in range(1, len(coefficients))]


def real_eval(coefficients, x):
    answer = F(0)
    for coefficient in reversed(coefficients):
        answer = answer * x + coefficient
    return answer


def run(note_path):
    intervals_panels = [
        [(F(0), F(1))],
        [(F(0), F(1, 16)), (F(3, 16), F(5, 16)), (F(9, 16), F(7, 8))],
        [(F(1, 7), F(2, 7)), (F(5, 7), F(11, 14))],
        [(F(0), F(1, 1024)), (F(511, 1024), F(513, 1024)),
         (F(1023, 1024), F(1))],
    ]
    evaluation_points = [F(0), F(1, 17), F(1, 5), F(1, 2), F(4, 5), F(1)]
    retained_cases = 0

    for intervals in intervals_panels:
        gamma = measure(intervals)
        require(F(0) < gamma <= 1, "retained_set_measure")
        for m in range(1, 8):
            retained_cases += 1
            nodes = quantile_nodes(intervals, m)
            d = gamma / (4 * m)
            require(len(nodes) == m, "retained_node_count")
            for j, node in enumerate(nodes):
                require(any(a <= node <= b for a, b in intervals), "retained_node_membership")
                for i in range(j):
                    require(node - nodes[i] >= (j - i) * d, "retained_node_separation")
                denominator = F(1)
                for i, other in enumerate(nodes):
                    if i != j:
                        denominator *= abs(node - other)
                bound = d ** (m - 1) * factorial(j) * factorial(m - j - 1)
                require(denominator >= bound, "factorial_denominator_lower_bound")

            factorial_bound = (F(8 * m) / gamma) ** (m - 1) / factorial(m - 1)
            exponential_bound = (F(48) / gamma) ** (m - 1)
            require(factorial_bound <= exponential_bound, "factorial_exponential_absorption")
            for x in evaluation_points:
                require(sum(abs(basis(nodes, j, x)) for j in range(m)) <= factorial_bound,
                        "nonuniform_lagrange_basis_bound")

            coefficients = complex_polynomial(m - 1)
            values = [peval(coefficients, node) for node in nodes]
            recovered = interpolant(nodes, values)
            require(recovered == coefficients, "complex_polynomial_coefficient_recovery")
            for x in evaluation_points:
                value = ZERO
                for j in range(m):
                    value = zadd(value, zscale(values[j], basis(nodes, j, x)))
                require(value == peval(coefficients, x), "complex_polynomial_value_recovery")

            full_energy = integrate_norm2(coefficients, [(F(0), F(1))])
            retained_energy = integrate_norm2(coefficients, intervals)
            require(full_energy > 0 and retained_energy > 0, "positive_integrated_polynomial_energy")
            require(full_energy <= (F(96) / gamma) ** (2 * m) * retained_energy,
                    "integrated_retained_polynomial_bound")

            # Degree m: the complex remainder equals its leading coefficient
            # times the nodal product, with no real mean-value point invoked.
            leading = (F(2, 3), F(-5, 7))
            higher = coefficients + [leading]
            higher_interpolant = interpolant(nodes, [peval(higher, node) for node in nodes])
            derivative_norm_squared = factorial(m) ** 2 * znorm2(leading)
            for x in evaluation_points:
                product = F(1)
                for node in nodes:
                    product *= x - node
                difference = zsub(peval(higher, x), peval(higher_interpolant, x))
                require(difference == zscale(leading, product), "complex_remainder_identity")
                require(znorm2(difference) <= derivative_norm_squared / factorial(m) ** 2,
                        "factorial_remainder_bound")

    grid_panels = 0
    reused_final_blocks = 0
    maximum_reuse = 0
    for n in range(1, 17):
        delta = F(1, n)
        for m in range(1, min(n + 1, 8) + 1):
            grid_panels += 1
            counts = [0] * (n + 1)
            starts = []
            for output_cell in range(n):
                start = min(output_cell, n + 1 - m)
                starts.append(start)
                indices = list(range(start, start + m))
                nodes = [j * delta for j in indices]
                require(len(indices) == m and 0 <= indices[0] <= indices[-1] <= n,
                        "grid_stencil_coverage")
                for index in indices:
                    counts[index] += 1
                left, right = output_cell * delta, (output_cell + 1) * delta
                for node in nodes:
                    require(max(abs(left - node), abs(right - node)) <= m * delta,
                            "grid_endpoint_distance")
                for j, node in enumerate(nodes):
                    denominator = F(1)
                    for i, other in enumerate(nodes):
                        if i != j:
                            denominator *= abs(node - other)
                    exact = delta ** (m - 1) * factorial(j) * factorial(m - 1 - j)
                    require(denominator == exact, "grid_factorial_denominator")
                coefficients = complex_polynomial(min(m - 1, 3))
                values = [peval(coefficients, node) for node in nodes]
                for fraction in (F(0), F(1, 3), F(1, 2), F(2, 3), F(1)):
                    x = left + fraction * delta
                    lebesgue = sum(abs(basis(nodes, j, x)) for j in range(m))
                    exact_bound = F(2 * m) ** (m - 1) / factorial(m - 1)
                    require(lebesgue <= exact_bound <= F(16) ** m, "grid_basis_budget")
                    value = ZERO
                    for j in range(m):
                        value = zadd(value, zscale(values[j], basis(nodes, j, x)))
                    require(value == peval(coefficients, x), "grid_complex_endpoint_interpolation")
            require(max(counts) <= 2 * m, "grid_node_reuse_bound")
            maximum_reuse = max(maximum_reuse, max(counts))
            if m >= 2:
                require(starts[-1] == n + 1 - m, "final_grid_block")
                require(n in range(starts[-1], starts[-1] + m), "upper_endpoint_inclusion")
            if m >= 3 and starts.count(n + 1 - m) > 1:
                reused_final_blocks += 1

    # A real mean-value point need not exist for a complex-valued function:
    # f(t) = t^2 + i t^3 on [0,1] has secant 1+i.  Its real derivative
    # forces t=1/2, where the imaginary derivative is 3/4, not 1.
    candidate = F(1, 2)
    require(2 * candidate == 1 and 3 * candidate ** 2 != 1,
            "negative_complex_mean_value_point")

    # Arbitrarily clustered retained nodes have no uniform grid constant.
    tiny = F(1, 1024)
    clustered = [F(0), tiny, 2 * tiny]
    clustered_values = [node * (node - tiny) for node in clustered]
    ratio = (1 - tiny) / max(abs(v) for v in clustered_values)
    require(ratio > F(16) ** 3, "negative_unseparated_node_budget")

    # Total retained measure alone leaves a whole interval unobserved.
    # The compactly supported piecewise polynomial is C^3, because it
    # vanishes to order four at both endpoints of the missing interval.
    gap_left, gap_right = F(1, 3), F(2, 3)
    bump = [F(1)]
    for _ in range(4):
        bump = real_mul(bump, [-gap_left, F(1)])
        bump = real_mul(bump, [gap_right, F(-1)])
    derived = bump
    for _ in range(4):
        require(real_eval(derived, gap_left) == 0 and real_eval(derived, gap_right) == 0,
                "negative_gap_bump_boundary_jets")
        derived = derivative_real(derived)
    bump_coefficients = [(coefficient, F(0)) for coefficient in bump]
    gap_energy = integrate_norm2(bump_coefficients, [(gap_left, gap_right)])
    gap_retained = [(F(0), gap_left), (gap_right, F(1))]
    retained_intersections = [
        (max(a, gap_left), min(b, gap_right))
        for a, b in gap_retained
        if max(a, gap_left) < min(b, gap_right)
    ]
    gap_retained_energy = integrate_norm2(bump_coefficients, retained_intersections)
    retained_measure = measure(gap_retained)
    require(retained_measure == F(2, 3) and gap_energy > 0 and gap_retained_energy == 0,
            "negative_total_measure_only")

    # Multiplying a perfectly smooth constant row by its moving entry
    # indicator produces a discontinuous function.  Its interpolation
    # error cannot be bounded using the constant row's second derivative.
    entry = F(3, 4)
    step_nodes = [F(1, 2), F(1)]
    step_values = [(F(int(node >= entry)), F(0)) for node in step_nodes]
    step_polynomial = interpolant(step_nodes, step_values)
    test_point = F(5, 8)
    observed_step = (F(int(test_point >= entry)), F(0))
    require(peval(step_polynomial, test_point) != observed_step,
            "negative_moving_row_entry_interpolation")
    require(F(1) - entry > 0 and
            all(int(node >= entry) == 0 for node in (F(0), F(1, 4), F(1, 2))),
            "negative_unsampled_row_entry")

    return {
        "status": "PASS",
        "arithmetic": "EXACT_RATIONAL; complex numbers represented by pairs of Fractions",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "associated_math_note_sha256": hashlib.sha256(note_path.read_bytes()).hexdigest(),
        "retained_set_panels": [
            {"intervals": [[str(a), str(b)] for a, b in panel], "measure": str(measure(panel))}
            for panel in intervals_panels
        ],
        "retained_interpolation_cases": retained_cases,
        "retained_interpolation_orders": [1, 7],
        "grid_panels": grid_panels,
        "grid_intervals_range": [1, 16],
        "maximum_grid_order": 8,
        "reused_final_block_panels": reused_final_blocks,
        "maximum_observed_node_reuse": maximum_reuse,
        "negative_controls": {
            "clustered_nodes_ratio": str(ratio),
            "unobserved_gap_full_squared_norm": str(gap_energy),
            "unobserved_gap_retained_squared_norm": str(gap_retained_energy),
            "unobserved_gap_retained_measure": str(retained_measure),
            "moving_row_entry": str(entry),
            "moving_row_wrong_interpolated_value": [str(x) for x in peval(step_polynomial, test_point)],
            "moving_row_actual_value": [str(x) for x in observed_step],
        },
        "checks": dict(sorted(COUNTS.items())),
        "total_checks": sum(COUNTS.values()),
        "scope": (
            "Finite exact diagnostics for polynomial interpolation, separated nonuniform nodes, "
            "integrated retained polynomial values at p=2, endpoint grid reuse, and explicit "
            "countermodels to omitted hypotheses. The associated note hash binds a file, not "
            "its mathematical truth. No arbitrary-measurable-set theorem, infinite convolution, "
            "derivative asymptotic, native arithmetic moment, zero-free premise, or RH is tested. "
            "The gap and row-entry controls refute naive omission of local distribution or "
            "smooth fixed-row scope; they do not contradict the stated remainder-inclusive theorem."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--note", type=Path, default=Path(__file__).with_name("attack3_averaging.md"))
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = json.dumps(run(arguments.note), indent=2, sort_keys=True) + "\n"
    if arguments.output is None:
        print(result, end="")
    else:
        arguments.output.write_text(result)
