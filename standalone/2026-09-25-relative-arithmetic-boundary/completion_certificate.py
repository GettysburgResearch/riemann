#!/usr/bin/env python3
"""Reproduce the finite-prime-completion lower bound and native-prefix energy.

All acceptance decisions use exact integer/Fraction arithmetic. Decimal fields
are displays only. The analytic inequalities connecting these numbers with an
L2 energy are proved in RESEARCH.md, not numerically assumed here.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from math import isqrt
from pathlib import Path

BITS = 40
SCALE = 1 << BITS

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def primes_to(n: int) -> list[int]:
    marked = bytearray(b'\1')*(n+1)
    marked[:2] = b'\0\0'
    for p in range(2, isqrt(n)+1):
        if marked[p]:
            marked[p*p:n+1:p] = b'\0'*((n-p*p)//p+1)
    return [p for p in range(2, n+1) if marked[p]]

def exp_partial(x: Fraction, terms: int) -> Fraction:
    """For x>0 this is a rigorous lower bound for exp(x)."""
    term = total = Fraction(1)
    for k in range(1, terms+1):
        term *= x/k
        total += term
    return total

def resonance_bound(y: int, primes: list[int]) -> dict:
    require(y >= 128, 'energy-denominator proof requires y >= 128')
    y16, y64 = y**16, y**64
    total = small = middle = large = 0
    for p in primes:
        if p > y:
            break
        root = isqrt(p)
        if p**31 < y16:
            # -2/floor(sqrt(p)) <= -2/sqrt(p).
            total += (-2*SCALE)//root
            small += 1
        elif p**93 >= y64:
            # 1/(2*ceil(sqrt(p))) - 1/(4p) <= the analytic positive lower bound.
            ceil_root = root+1  # p is prime, hence not a square.
            numerator, denominator = 2*p-ceil_root, 4*p*ceil_root
            total += (SCALE*numerator)//denominator
            large += 1
        else:
            middle += 1
    return {'y': y, 'bits': BITS, 'log_amplitude_lower_numerator': total,
            'denominator': SCALE, 'small_primes': small,
            'middle_primes': middle, 'large_primes': large,
            'display_lower': total/SCALE}

def native_energy(y: int, primes: list[int]) -> dict:
    mu = [1]*(y+1); mu[0] = 0
    for p in primes:
        if p > y:
            break
        for n in range(p, y+1, p):
            mu[n] = -mu[n]
        for n in range(p*p, y+1, p*p):
            mu[n] = 0
    # Independently authenticate every coefficient by mu * 1 = delta.
    convolution = [0]*(y+1)
    for d in range(1, y+1):
        if mu[d]:
            for n in range(d, y+1, d):
                convolution[n] += mu[d]
    require(convolution[1] == 1 and all(x == 0 for x in convolution[2:]),
            'native inverse identity failed')
    m = lo = hi = 0
    for k in range(1, y+1):
        m += mu[k]
        den, num = k*(k+1), m*m*SCALE
        lo += num//den
        hi += (num+den-1)//den
    return {'y': y, 'mertens': m, 'lower_numerator': lo, 'upper_numerator': hi,
            'denominator': SCALE, 'display_interval': [lo/SCALE, hi/SCALE],
            'independent_dirichlet_inverse_identity_verified_through': y}

def exact_small_completions(primes: list[int], number: int = 20) -> list[dict]:
    divisors, primorial, rows = [(1, 1)], 1, []
    for p in primes[:number]:
        divisors += [(p*d, -m) for d, m in divisors]
        primorial *= p
        numerator = prefix = 0
        for d, mu in sorted(divisors):
            numerator += (1+2*mu*prefix)*(primorial//d)
            prefix += mu
        require(prefix == 0, 'finite Euler sum must vanish')
        energy = Fraction(numerator, primorial)
        rows.append({'y': p, 'divisors': len(divisors),
                     'energy_numerator': energy.numerator,
                     'energy_denominator': energy.denominator,
                     'display_energy': float(energy)})
    return rows

def run(include_small: bool = True) -> dict:
    y = 1_000_000
    primes = primes_to(y)
    rows = [resonance_bound(z, primes) for z in (1000, 10000, 100000, y)]
    last = rows[-1]
    # L > 207/5 = 41.4. No rounded logarithm is used in these decisions.
    require(5*last['log_amplitude_lower_numerator'] > 207*SCALE, 'L > 41.4 failed')
    require(exp_partial(Fraction(14), 80) > y, 'log(y) < 14 certificate failed')
    # E >= exp(2L)/(40 log y) > exp(414/5)/560 > 10^33.
    require(exp_partial(Fraction(414, 5), 220) > 560*10**33,
            'energy > 10^33 certificate failed')
    head = native_energy(y, primes)
    require(head['upper_numerator'] < 2*SCALE, 'native energy < 2 failed')
    require(head['lower_numerator'] <= head['upper_numerator'], 'bad enclosure')
    return {
        'status': 'exact finite certificate plus an analytic argument in RESEARCH.md',
        'prime_count': len(primes), 'dyadic_bits': BITS,
        'resonance_interval': '[31*pi/(32*log(y)), 33*pi/(32*log(y))]',
        'uniform_energy_lower_formula': 'exp(2*L)/(40*log(y))',
        'resonance_bounds': rows, 'native_energy': head,
        'certified_comparison': {'y': y, 'full_prime_completion_energy_greater_than': str(10**33),
                                'native_prefix_energy_less_than': 2,
                                'therefore_artificial_tail_energy_greater_than': str(10**33-2)},
        'rational_exponential_checks': [
            {'x': '14', 'terms': 80, 'partial_sum_greater_than': str(y)},
            {'x': '414/5', 'terms': 220, 'partial_sum_greater_than': str(560*10**33)}],
        'small_full_completion_energies': exact_small_completions(primes) if include_small else [],
        'limits': ['not a counterexample to RH', 'not an estimate for balanced Newton covariance',
                   'no all-scale source-bound theorem', 'no independent formal proof audit'],
    }

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--check', type=Path, help='recompute and compare to an existing receipt')
    ap.add_argument('--skip-small', action='store_true', help='omit the up-to-2^20-divisor scout')
    args = ap.parse_args()
    result = run(not args.skip_small)
    if args.check:
        expected = json.loads(args.check.read_text(encoding='utf-8'))
        require(result == expected, 'receipt does not match exact recomputation')
    text = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')
if __name__ == '__main__':
    main()
