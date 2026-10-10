#!/usr/bin/env python3
"""Independent census/covariance controls for the finite CRT mechanism probe.

Uses the reviewed literal character routine for values; independently counts
squarefree ideals by rational prime factorization and computes the cumulant
through real covariance, without the probe's complex_square/summarize helpers.
This verifies finite experiments, not an infinite short-row estimate.
"""
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)


def squarefree_ideal_count(n):
    count = 1
    divisor = 2
    while divisor * divisor <= n:
        exponent = 0
        while n % divisor == 0:
            n //= divisor
            exponent += 1
        if exponent:
            if divisor in (2, 3):
                return 0
            if divisor % 3 == 1:
                if exponent > 2:
                    return 0
                count *= 2 if exponent == 1 else 1
            elif exponent != 2:
                return 0
        divisor += 1
    if n > 1:
        if n in (2, 3) or n % 3 == 2:
            return 0
        count *= 2
    return count


def run():
    source = Path(__file__).parent.parent / 'correlations' / 'probe_sextic_cumulants.py'
    spec = importlib.util.spec_from_file_location('reviewed_sextic_probe', source)
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    expected_cumulants = (
        F(348006807, 35153041),
        F(6875488331, 23088025),
        F(5440157328645, 9354951841),
    )
    records = []
    for D, expected in zip((128, 256, 512), expected_cumulants):
        ideal_count = sum(squarefree_ideal_count(n) for n in range(D // 2 + 1, D + 1))
        ideals = probe.prime_ideals(D)
        columns = probe.columns(ideals, D)
        need(ideal_count == len(columns), 'independent complete squarefree ideal count')
        values = []
        for row in probe.rows(D):
            local = [probe.symbol(prime, row) for prime in ideals]
            a = b = 0
            for _, mu, indices in columns:
                if any(local[index] < 0 for index in indices):
                    continue
                x, y = probe.ROOTS[sum(local[index] for index in indices) % 6]
                a += mu * x
                b += mu * y
            values.append((F(a), F(b)))
        count = len(values)
        ma = sum(value[0] for value in values) / count
        mb = sum(value[1] for value in values) / count
        centered = [(a - ma, b - mb) for a, b in values]
        # epsilon=1/2+i sqrt(3)/2: X=a+b/2, Y=sqrt(3)b/2.
        xx = sum((a + b / 2) ** 2 for a, b in centered) / count
        yy = F(3, 4) * sum(b * b for a, b in centered) / count
        xy_squared = F(3, 4) * (sum((a + b / 2) * b for a, b in centered) / count) ** 2
        fourth = sum(((a + b / 2) ** 2 + F(3, 4) * b * b) ** 2 for a, b in centered) / count
        cumulant = fourth - 3 * xx ** 2 - 2 * xx * yy - 3 * yy ** 2 - 4 * xy_squared
        need(cumulant == expected and cumulant > 0, 'independent real-covariance cumulant')
        records.append({'D': D, 'squarefree_columns': ideal_count,
                        'rows': count, 'positive_fourth_cumulant': str(cumulant)})
    return {'status': 'PASS_INDEPENDENT_FINITE_CRT_CENSUS_AND_REAL_CUMULANTS',
            'panels': records, 'short_row_moment_proved': False, 'rh_proved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
