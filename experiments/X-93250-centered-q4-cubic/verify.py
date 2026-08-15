#!/usr/bin/env python3
"""Exact finite replay for L-93250--T-93255.

Uses only Python's standard library and Fraction arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


Q = Fraction


def poly_add(a: List[Q], b: List[Q]) -> List[Q]:
    n = max(len(a), len(b))
    out = [Q(0) for _ in range(n)]
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(a: List[Q], b: List[Q]) -> List[Q]:
    out = [Q(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(a: List[Q], c: Q) -> List[Q]:
    return [c * x for x in a]


def poly_eval(a: List[Q], x: Q) -> Q:
    ans = Q(0)
    for coefficient in reversed(a):
        ans = ans * x + coefficient
    return ans


def poly_integral(a: List[Q]) -> List[Q]:
    return [Q(0)] + [a[i] / Q(i + 1) for i in range(len(a))]


def poly_derivative(a: List[Q]) -> List[Q]:
    if len(a) <= 1:
        return [Q(0)]
    return [Q(i) * a[i] for i in range(1, len(a))]


def definite_integral(a: List[Q], left: Q = Q(0), right: Q = Q(1)) -> Q:
    antiderivative = poly_integral(a)
    return poly_eval(antiderivative, right) - poly_eval(antiderivative, left)


# w(x) = -1/6 + x - x^2
W = [Q(-1, 6), Q(1), Q(-1)]
# K(x) = -x/3 + x^2 - 2x^3/3
K = [Q(0), Q(-1, 3), Q(1), Q(-2, 3)]


def weight_cell(j: int, n: int, weight: List[Q] = W) -> Q:
    return definite_integral(weight, Q(j, n), Q(j + 1, n))


def prefix(values: List[Q]) -> List[Q]:
    out = [Q(0)]
    for value in values[1:]:
        out.append(out[-1] + value)
    return out


def row_from_source(values: List[Q], predecessor_shift: int = 1) -> List[Q]:
    """values is indexed 0..N; values[0] is ignored."""
    n = len(values) - 1
    csum = prefix(values)
    row: List[Q] = []
    for j in range(n):
        reflected = n - j - predecessor_shift
        if reflected < 0:
            reflected = 0
        row.append(csum[n] - csum[j] - csum[reflected])
    return row


def projection_from_cells(row: List[Q], weight: List[Q] = W) -> Q:
    n = len(row)
    return sum((weight_cell(j, n, weight) * row[j] for j in range(n)), Q(0))


def projection_from_kernel(values: List[Q], kernel: List[Q] = K) -> Q:
    n = len(values) - 1
    return sum(
        (values[m] * poly_eval(kernel, Q(m, n)) for m in range(1, n + 1)),
        Q(0),
    )


def centered_integral(row: List[Q]) -> Tuple[Q, Q]:
    n = len(row)
    mean = sum(row, Q(0)) / Q(n)
    integral = sum(((x - mean) ** 2 for x in row), Q(0)) / Q(n)
    return mean, integral


def primes_upto(n: int) -> List[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def formal_prime_weights(n: int) -> Dict[int, Q]:
    """Distinct positive rational stand-ins for log p; log 4 = 2 log 2."""
    return {p: Q((p % 17) + 3, (p % 11) + 5) for p in primes_upto(n)}


def q4_prime_components(n: int) -> Dict[int, List[Q]]:
    weights = formal_prime_weights(n)
    components: Dict[int, List[Q]] = {}
    for p, lp in weights.items():
        arr = [Q(0) for _ in range(n + 1)]
        power = p
        while power <= n:
            arr[power] += lp
            if 4 * power <= n:
                arr[4 * power] -= 4 * lp
            if power > n // p:
                break
            power *= p
        if p == 2:
            power4 = 4
            while power4 <= n:
                arr[power4] += 6 * lp  # 3 log 4 = 6 log 2
                if power4 > n // 4:
                    break
                power4 *= 4
        components[p] = arr
    return components


def source_sum(components: Dict[int, List[Q]], n: int) -> List[Q]:
    total = [Q(0) for _ in range(n + 1)]
    for arr in components.values():
        for m in range(1, n + 1):
            total[m] += arr[m]
    return total


def formal_von_mangoldt(m: int, weights: Dict[int, Q]) -> Q:
    """Formal Lambda(m): log p if m is a positive power of p, else zero."""
    if m < 2:
        return Q(0)
    for p, lp in weights.items():
        power = p
        while power < m and power <= m // p:
            power *= p
        if power == m:
            return lp
    return Q(0)


def q4_direct_source(n: int) -> List[Q]:
    """Independent direct evaluation of c_circ, not via prime components."""
    weights = formal_prime_weights(n)
    log2 = weights[2]
    out = [Q(0) for _ in range(n + 1)]
    powers4 = set()
    power4 = 4
    while power4 <= n:
        powers4.add(power4)
        if power4 > n // 4:
            break
        power4 *= 4
    for m in range(1, n + 1):
        value = formal_von_mangoldt(m, weights)
        if m % 4 == 0:
            value -= 4 * formal_von_mangoldt(m // 4, weights)
        if m in powers4:
            value += 6 * log2
        out[m] = value
    return out


def fraction_string(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    # 1. Weight and kernel algebra.
    assert definite_integral(W) == 0
    assert definite_integral(poly_mul(W, W)) == Q(1, 180)
    assert poly_derivative(K) == poly_scale(W, Q(2))
    assert poly_eval(K, Q(0)) == 0
    assert poly_eval(K, Q(1)) == 0

    # With y=2x-1 and t=y^2, K=y(1-y^2)/12.  The exact bound
    # 972 K^2 <= 1 is equivalent to
    # 4-27t(1-t)^2=(3t-1)^2(4-3t) >= 0 on 0<=t<=1.
    t = [Q(0), Q(1)]
    one_minus_t = [Q(1), Q(-1)]
    lhs_sup = poly_add([Q(4)], poly_scale(poly_mul(t, poly_mul(one_minus_t, one_minus_t)), Q(-27)))
    rhs_sup = poly_mul(poly_mul([Q(-1), Q(3)], [Q(-1), Q(3)]), [Q(4), Q(-3)])
    assert lhs_sup == rhs_sup
    kernel_sup_factorization_checks = 1

    symmetry_checks = 0
    kernel_sup_checks = 0
    for denominator in range(1, 97):
        for numerator in range(denominator + 1):
            x = Q(numerator, denominator)
            assert poly_eval(W, Q(1) - x) == poly_eval(W, x)
            assert poly_eval(K, Q(1) - x) == -poly_eval(K, x)
            assert 972 * poly_eval(K, x) ** 2 <= 1
            symmetry_checks += 2
            kernel_sup_checks += 1

    # 2. Mellin numerator:
    # Khat = -1/[3(s+1)] + 1/(s+2) - 2/[3(s+3)].
    factors = [[Q(1), Q(1)], [Q(2), Q(1)], [Q(3), Q(1)]]
    common = poly_mul(poly_mul(factors[0], factors[1]), factors[2])
    numerator = [Q(0)]
    mellin_terms = [(Q(-1, 3), 0), (Q(1), 1), (Q(-2, 3), 2)]
    for coefficient, omitted in mellin_terms:
        term = [Q(1)]
        for index, factor in enumerate(factors):
            if index != omitted:
                term = poly_mul(term, factor)
        numerator = poly_add(numerator, poly_scale(term, coefficient))
    assert poly_scale(numerator, Q(3)) == [Q(-1), Q(1)]
    mellin_checks = 1

    # 3. Arbitrary rational source fixtures.
    rng = random.Random(93250)
    projection_fixtures = 0
    cauchy_fixtures = 0
    endpoint_mutations_detected = 0
    kernel_mutations_detected = 0
    mean_mutations_detected = 0

    bad_kernel = K.copy()
    bad_kernel[2] += Q(1, 7)
    bad_weight = W.copy()
    bad_weight[0] += Q(1, 5)

    for n in range(2, 43):
        for _ in range(5):
            values = [Q(0)] + [
                Q(rng.randint(-9, 9), rng.randint(1, 9)) for _m in range(n)
            ]
            row = row_from_source(values)
            cell_value = projection_from_cells(row)
            kernel_value = projection_from_kernel(values)
            assert cell_value == kernel_value
            projection_fixtures += 1

            _mean, integral = centered_integral(row)
            assert 180 * cell_value * cell_value <= integral
            cauchy_fixtures += 1

            bad_row = row_from_source(values, predecessor_shift=0)
            if projection_from_cells(bad_row) != kernel_value:
                endpoint_mutations_detected += 1

            if projection_from_kernel(values, bad_kernel) != cell_value:
                kernel_mutations_detected += 1

            if projection_from_cells(row, bad_weight) != kernel_value:
                mean_mutations_detected += 1

    assert endpoint_mutations_detected > 0
    assert kernel_mutations_detected == projection_fixtures
    assert mean_mutations_detected > 0

    # 4. Formal Q4 prime-base fixtures.
    q4_endpoints = [8, 12, 16, 20, 24, 28, 32, 40, 48, 56, 64, 72, 80, 96]
    q4_source_coefficients = 0
    q4_row_checks = 0
    q4_centered_gram_checks = 0
    q4_scalar_checks = 0
    scalar_diagonal_checks = 0
    source_mutations_detected = 0
    source_mutation_opportunities = 0

    for n in q4_endpoints:
        components = q4_prime_components(n)
        total = source_sum(components, n)
        direct = q4_direct_source(n)
        assert total == direct
        q4_source_coefficients += n

        total_row = row_from_source(total)
        block_rows = {p: row_from_source(arr) for p, arr in components.items()}
        reconstructed = [
            sum((block_rows[p][j] for p in block_rows), Q(0)) for j in range(n)
        ]
        assert total_row == reconstructed
        q4_row_checks += n

        total_mean, _ = centered_integral(total_row)
        centered_total = [x - total_mean for x in total_row]
        centered_blocks: Dict[int, List[Q]] = {}
        for p, block in block_rows.items():
            block_mean, _ = centered_integral(block)
            centered_blocks[p] = [x - block_mean for x in block]
        reconstructed_centered = [
            sum((centered_blocks[p][j] for p in centered_blocks), Q(0))
            for j in range(n)
        ]
        assert centered_total == reconstructed_centered

        lhs = sum((x * x for x in centered_total), Q(0))
        diagonal = sum(
            (
                sum((x * x for x in centered_blocks[p]), Q(0))
                for p in centered_blocks
            ),
            Q(0),
        )
        plist = sorted(centered_blocks)
        cross = Q(0)
        for i, p in enumerate(plist):
            for r in plist[i + 1 :]:
                cross += 2 * sum(
                    (
                        centered_blocks[p][j] * centered_blocks[r][j]
                        for j in range(n)
                    ),
                    Q(0),
                )
        assert lhs == diagonal + cross
        q4_centered_gram_checks += 1

        scalar_total = projection_from_kernel(total)
        scalar_blocks = {
            p: projection_from_kernel(arr) for p, arr in components.items()
        }
        assert scalar_total == sum(scalar_blocks.values(), Q(0))
        assert scalar_total == projection_from_cells(total_row)
        q4_scalar_checks += 2

        for p, arr in components.items():
            amplitude = sum((abs(x) for x in arr[1:]), Q(0))
            assert 972 * scalar_blocks[p] * scalar_blocks[p] <= amplitude * amplitude
            scalar_diagonal_checks += 1

        # Drop the contracted term of the first available odd prime.
        odd_primes = [p for p in sorted(components) if p != 2]
        eligible = [p for p in odd_primes if 4 * p <= n]
        if eligible:
            source_mutation_opportunities += 1
            p = eligible[0]
            mutated = [x for x in components[p]]
            power = p
            while 4 * power <= n:
                mutated[4 * power] += 4 * formal_prime_weights(n)[p]
                if power > n // p:
                    break
                power *= p
            mutated_components = dict(components)
            mutated_components[p] = mutated
            mutated_total = source_sum(mutated_components, n)
            if mutated_total != total:
                source_mutations_detected += 1

    assert source_mutations_detected == source_mutation_opportunities

    # 5. Sharp synthetic coherence firewall.
    coherence_fixtures = 0
    cardinality_mutations_detected = 0
    for block_count in range(2, 81):
        energy = Q(block_count * block_count)
        diagonal = Q(block_count)
        positive_blocks = Q(block_count)
        cross = Q(block_count * (block_count - 1))
        assert positive_blocks == energy / diagonal
        assert cross == energy - diagonal
        coherence_fixtures += 1

        # The false shortcut "positive_blocks <= sqrt(E/D)" must fail.
        # Squaring avoids irrational arithmetic: M^2 > E/D = M for M>1.
        if positive_blocks * positive_blocks > energy / diagonal:
            cardinality_mutations_detected += 1
    assert cardinality_mutations_detected == coherence_fixtures

    result = {
        "arithmetic_class": "EXACT_RATIONAL",
        "bernoulli_weight": {
            "integral": fraction_string(definite_integral(W)),
            "l2_norm_squared": fraction_string(definite_integral(poly_mul(W, W))),
            "symmetry_checks": symmetry_checks,
        },
        "cubic_kernel": {
            "kernel_sup_squared": "1/972",
            "kernel_sup_factorization_checks": kernel_sup_factorization_checks,
            "kernel_sup_grid_checks": kernel_sup_checks,
            "mellin_numerator_checks": mellin_checks,
        },
        "finite_endpoint_fixtures": {
            "projection_identities": projection_fixtures,
            "centered_cauchy_inequalities": cauchy_fixtures,
        },
        "q4_prime_block_fixtures": {
            "endpoints": len(q4_endpoints),
            "source_coefficients": q4_source_coefficients,
            "row_reconstruction_checks": q4_row_checks,
            "centered_gram_checks": q4_centered_gram_checks,
            "scalar_projection_checks": q4_scalar_checks,
            "scalar_diagonal_checks": scalar_diagonal_checks,
        },
        "coherence_firewall": {
            "sharp_fixtures": coherence_fixtures,
        },
        "mutations": {
            "endpoint_predecessor_detected": endpoint_mutations_detected,
            "kernel_coefficient_detected": kernel_mutations_detected,
            "nonzero_mean_detected": mean_mutations_detected,
            "source_partition_detected": source_mutations_detected,
            "source_partition_opportunities": source_mutation_opportunities,
            "cardinality_shortcut_detected": cardinality_mutations_detected,
        },
        "verdict": "PASS_X_93250_CENTERED_Q4_CUBIC",
    }

    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
