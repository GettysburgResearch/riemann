#!/usr/bin/env python3
"""Exact finite native masked-translation and independent lattice ideal counts.

No asymptotic analytic hypothesis or infinite nonreturn is numerically tested.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import importlib.util
import json
from math import isqrt
from pathlib import Path

SOURCE = Path(__file__).resolve().parent.parent/'correlations/probe_sextic_cumulants.py'
spec = importlib.util.spec_from_file_location('native_sextic_source', SOURCE)
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)


def need(ok, message):
    if not ok:
        raise ArithmeticError(message)


def translator(ideals):
    rational_primes = sorted({p for _, p, _ in ideals})
    value = [0, 0]
    modulus = 1
    for p in rational_primes:
        local_ideals = [q for q in ideals if q[1] == p]
        if local_ideals[0][2] is None:
            residue = next((a, b) for a in range(p) for b in range(p)
                           if native.symbol(local_ideals[0], (a, b)) == 3)
        else:
            residue = (next(a for a in range(1, p)
                            if pow(a, (p-1)//6, p) == p-1), 0)
        for j in range(2):
            correction = ((residue[j]-value[j])*pow(modulus, -1, p)) % p
            value[j] += modulus*correction
        modulus *= p
    value = tuple(value)
    need(all(native.symbol(q, value) == 3 for q in ideals),
         'actual coherent local sextic signs including inert ideals')
    return value, modulus


def independent_prime_divides(prime, row):
    _, p, root = prime
    a, b = row
    return (a % p == 0 and b % p == 0) if root is None else (a+root*b) % p == 0


def square_prime_divides(prime, row):
    _, p, root = prime
    a, b = row
    if root is None:
        return a % (p*p) == 0 and b % (p*p) == 0
    # Independent Hensel lift of omega's split residue modulo p^2.
    correction = -((root*root+root+1)//p)*pow(2*root+1, -1, p) % p
    lift = root+p*correction
    need((lift*lift+lift+1) % (p*p) == 0, 'exact lifted split prime square')
    return (a+lift*b) % (p*p) == 0


def lattice_squarefree_band_count(scale, ideals, base):
    # Counts actual principal ideal generators independently of source columns.
    # Removing the six unit associates gives the ideal count.
    count = 0
    cap = isqrt(4*scale//3)+2
    relevant = [q for q in ideals if q[0]*q[0] <= scale]
    mask = [q for q in ideals if independent_prime_divides(q, base)]
    for a in range(-cap, cap+1):
        for b in range(-cap, cap+1):
            norm = a*a-a*b+b*b
            if not scale//2 < norm <= scale:
                continue
            # S consists of the prime over 3 and the inert prime over 2.
            if (a+b) % 3 == 0 or (a % 2 == 0 and b % 2 == 0):
                continue
            row = a, b
            if any(independent_prime_divides(q, row) for q in mask):
                continue
            if any(square_prime_divides(q, row) for q in relevant):
                continue
            count += 1
    need(count % 6 == 0, 'six unit associates per actual integral ideal')
    return count//6


def panel(scale):
    ideals = native.prime_ideals(scale)
    columns = native.columns(ideals, scale)
    t, modulus = translator(ideals)
    bases = [(1, 0), (7, 0), (5, 0), (3, 1), (2, 1)]
    records = []
    for base in bases:
        v = native.mul(t, base)
        w = native.mul(v, native.ring_power(base, 5))
        need(native.norm(w) == native.norm(v)*native.norm(base)**5,
             'exact norm multiplicativity')
        local = [native.symbol(q, w) for q in ideals]
        bmask = [independent_prime_divides(q, base) for q in ideals]
        need(all(j == (-1 if masked else 3) for j, masked in zip(local, bmask)),
             'literal masked vb^5 local source identity')
        expected = actual = 0
        for _, mu, indices in columns:
            coprime = not any(bmask[j] for j in indices)
            expected += coprime
            if any(local[j] < 0 for j in indices):
                signed = (0, 0)
            else:
                root = native.ROOTS[sum(local[j] for j in indices) % 6]
                signed = mu*root[0], mu*root[1]
            need(signed == ((1, 0) if coprime else (0, 0)),
                 'each actual squarefree source term retains its zero mask')
            actual += signed[0]
        lattice = lattice_squarefree_band_count(scale, ideals, base)
        need(actual == expected == lattice,
             'literal source count equals independent lattice squarefree ideal census')
        records.append({'base': list(base), 'base_norm': native.norm(base),
                        'masked_prime_ideal_count': sum(bmask),
                        'positive_masked_source_sum': actual,
                        'independent_lattice_ideal_count': lattice})
    if scale >= 32:
        need(records[1]['masked_prime_ideal_count'] == 2, 'both split ideals at 7 masked')
        need(records[2]['masked_prime_ideal_count'] == 1, 'inert prime of norm 25 masked')
        need(records[3]['masked_prime_ideal_count'] == 1, 'one split ideal of norm 7 masked')
        need(records[4]['masked_prime_ideal_count'] == 0, 'excluded ramified prime is not active')
    return {'D': scale, 'prime_ideal_count': len(ideals),
            'squarefree_sharp_band_column_count': len(columns),
            'translator_coordinate_modulus': str(modulus),
            'base_panels': records}


def exponent_controls():
    count = 0
    for bound in (Q(1, 2), Q(7, 8), Q(99, 100)):
        for power_a in (Q(1, 10), Q(1), Q(100)):
            gamma = delta = (1-bound)/4
            epsilon = min(gamma/(2*power_a), 1/(8*power_a))
            need(power_a*epsilon < gamma, 'main term lower exponent exceeds requested bound')
            need(1-power_a*epsilon > Q(1, 2)+power_a*epsilon,
                 'uniform masked counting error has a smaller exponent')
            need(1-gamma-(bound+delta) == (1-bound)/2 > 0,
                 'exact conditional contradiction exponent')
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    panels = [panel(d) for d in (32, 64, 128, 256, 512)]
    result = {'status': 'PASS_EXACT_MASKED_CRT_SOURCE_AND_INDEPENDENT_LATTICE_CONTROLS',
              'arithmetic': 'EXACT_INTEGER_RESIDUES_AND_RATIONAL_EXPONENT_GUARDS',
              'scale_panels': panels, 'nonzero_base_panels': sum(len(r['base_panels']) for r in panels),
              'exact_exponent_controls': exponent_controls(),
              'native_nu': 1, 'excluded_prime_ideals': 'all prime ideals over 6',
              'finite_profile': 'literal sharp band D/2<Nn<=D, not smooth W',
              'asymptotic_counting_numerically_certified': False,
              'uniform_full_twist_analytic_input_verified': False,
              'short_row_moment_upper_bound_proved': False, 'rh_proved': False,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'primitive_source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest()}
    text = json.dumps(result, sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
