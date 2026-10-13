#!/usr/bin/env python3
"""Exact principal-reference calibration, not a full native-moment computation.
All good squarefree ideal columns in D/2<Nn<=D are used. The independent
reference is enclosed in rational dyadic intervals, with every rounding
remainder paid. Sharp physical principal values are exact integers.
"""
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import math

HERE = Path(__file__).resolve().parent

def require(ok, message):
    if not ok:
        raise ValueError(message)


def ceil_root(n, r):
    low, high = 0, 1
    while high**r < n:
        high *= 2
    while high-low > 1:
        mid = (high+low)//2
        if mid**r < n:
            low = mid
        else:
            high = mid
    return high


def main():
    spec = importlib.util.spec_from_file_location('census_source', HERE/'census_source.py')
    c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
    bits = 96; scale = 1 << bits
    cases = []
    for D in (64, 128, 256, 512, 1024, 2048):
        primes = c.prime_ideals(D)
        all_ideals = c.ideals_through(D, primes)
        columns = [f for n, f, _ in all_ideals if D < 2*n and all(e == 1 for j, e in f)]
        profiles = c.product_counts(columns, 2)
        lo = hi = 0
        exact = Fraction(0)
        for fac, mult in profiles.items():
            numerator = mult*mult*math.prod(primes[j][0]-1 for j, e in fac)
            denominator = math.prod(primes[j][0] for j, e in fac)
            q, remainder = divmod(scale*numerator, denominator)
            lo += q; hi += q+(remainder != 0)
            if D <= 256:
                exact += Fraction(numerator, denominator)
        if D <= 256:
            require(Fraction(lo, scale) <= exact <= Fraction(hi, scale), 'dyadic enclosure')
        require(hi-lo <= len(profiles), 'complete rounding remainder')
        Hs = (D, ceil_root(D**21, 20))
        physical = []
        for H in Hs:
            rows = c.element_rows(H)
            prefix = c.row_count_prefix(rows, H)
            p = c.principal_reference(profiles, H, prefix, primes)
            require(p['sixth_alias_addition'] == 0, 'squarefree quartic has no aliases')
            # Different symbolic-product implementation from the pinned census.
            independent = c.principal_fourth(columns, H, prefix, primes)
            require(p['principal_total'] == independent['principal_total'], 'two product engines')
            physical.append({'H': H, 'rows': len(rows), 'principal_fourth': p['principal_total']})
        cases.append({'D': D, 'good_prime_ideals': len(primes), 'squarefree_columns': len(columns),
                      'distinct_pair_products': len(profiles),
                      'B4_lower_numerator': lo, 'B4_upper_numerator': hi,
                      'B4_denominator_power_of_two': bits,
                      'physical': physical})
    print(json.dumps({'status':'FINITE_EXACT_REFERENCE_CALIBRATION',
                      'scope':'Hard annular columns, all good ideals; exact sharp principal sums, not full physical moments. No asymptotic inference.',
                      'cases':cases}, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
