#!/usr/bin/env python3
"""Exact finite controls for a source identity; the off-diagonal bound is OPEN."""
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def run():
    # The identity is local in squarefree prime ideals. Boolean valuation
    # controls suffice for ideal divisibility, including every higher positive
    # valuation of a dual frequency. No rational-prime model of K is assumed.
    controls = 0
    for size in range(11):
        primes = range(size)
        for divides_frequency in itertools.product((False, True), repeat=size):
            total = 0
            for selected in itertools.product((False, True), repeat=size):
                # f selects primes of g; all unselected primes must avoid k.
                if all(selected[p] or not divides_frequency[p] for p in primes):
                    total += (-1)**sum(selected)
            expected = (-1)**size if all(divides_frequency) else 0
            require(total == expected, 'full signed common-factor collapse')
            controls += 1
    h, kappa = Fraction(18, 23), Fraction(2, 5)
    normalized_target = h+kappa*(1-h)
    require(normalized_target == Fraction(20, 23), 'normalized S target')
    require(1+normalized_target == Fraction(43, 23), 'restore original factor D')
    require(2-(1+normalized_target) == Fraction(3, 23), 'unpaid source saving')
    require(1 < 1+normalized_target, 'D log D diagonal is below target')
    require(1-h > 0, 'dual gap reverses at the smallest block')
    return {
        'status': 'PASS_EXACT_SIGNED_SOURCE_CONTROLS',
        'local_squarefree_divisor_controls': controls,
        'source_commit': 'fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb',
        'source_tex_sha256': 'd9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d',
        'fixed_h': str(h), 'target_kappa': str(kappa),
        'normalized_off_diagonal_target': str(normalized_target),
        'original_row_target': str(1+normalized_target),
        'saving_over_D_squared': str(2-(1+normalized_target)),
        'arithmetic_scope': 'exact local ideal-divisor controls and rational exponent normalization',
        'imported_poisson_rebuilt': False,
        'off_diagonal_estimate_proved': False,
        'new_row_moment_proved': False,
        'new_zero_free_half_plane_proved': False,
        'rh_proved': False,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2)+'\n', end='')
