#!/usr/bin/env python3
"""Exact finite controls; no asymptotic trace bound is certified."""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import permutations
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path


def need(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def pmul(a, b, degree):
    out = Counter()
    for x, cx in a.items():
        for y, cy in b.items():
            z = tuple(i + j for i, j in zip(x, y))
            if sum(z) <= degree:
                out[z] += cx * cy
    return {z: c for z, c in out.items() if c}


def formal_control(r, degree=6):
    zero = (0,) * r
    numerator = {zero: 1}
    factors = []
    for i in range(r):
        e = tuple(int(j == i) for j in range(r))
        numerator[e] = -1
        factors.append(e)
    pairs = []
    for i in range(r):
        for j in range(i + 1, r):
            e = tuple(int(l == i) + int(l == j) for l in range(r))
            pairs.append(e)
    remainder = numerator
    for e in factors + pairs:
        geometric = {tuple(n * c for c in e): 1
                     for n in range(degree // sum(e) + 1)}
        remainder = pmul(remainder, geometric, degree)
    need(all(sum(e) not in (1, 2) for e in remainder),
         f'all degree-one/two terms cancel at r={r}')
    cubic = {}
    for i in range(r):
        for j in range(r):
            if i != j:
                cubic[tuple(2 * int(l == i) + int(l == j)
                            for l in range(r))] = -1
    for i in range(r):
        for j in range(i + 1, r):
            for l in range(j + 1, r):
                cubic[tuple(int(h in (i, j, l)) for h in range(r))] = -2
    need({e: c for e, c in remainder.items() if sum(e) == 3} == cubic,
         f'complete ordered cubic remainder at r={r}')
    reconstructed = remainder
    for e in factors + pairs:
        reconstructed = pmul(reconstructed, {zero: 1, e: -1}, degree)
    need(reconstructed == numerator, f'all reciprocal pair signs at r={r}')
    no_pairs = numerator
    for e in factors:
        no_pairs = pmul(no_pairs, {tuple(n * c for c in e): 1
                         for n in range(degree + 1)}, degree)
    need(any(sum(e) == 2 for e in no_pairs), 'omitted-pair negative control')
    return {'slots': r, 'degree': degree, 'all_pairs': len(pairs),
            'checked_nonzero_remainder_coefficients': len(remainder),
            'complete_cubic_terms': len(cubic),
            'omitted_pair_control_rejected': True}


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[0], x[1] - y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def scale(x, c):
    return x[0] * c, x[1] * c


def conj(x):
    return x[0] - x[1], -x[1]


def norm(x):
    return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]


def divide(x, y):
    need(norm(y) != 0, 'nonzero exact Euler denominator')
    return scale(mul(x, conj(y)), Fraction(1, norm(y)))


UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
ONE = (Fraction(1), Fraction(0))


def native_control():
    H = 40
    rows = []
    amax = isqrt(4 * H // 3)
    for a in range(-amax, amax + 1):
        t = isqrt(4 * H - 3 * a * a)
        for b in range(-(-(a - t) // 2), (a + t) // 2 + 1):
            if (a, b) != (0, 0):
                need(0 < norm((a, b)) <= H, 'complete norm-ball inequalities')
                rows.append((a, b))
    need(len(rows) == 150 and len(set(rows)) == 150, 'complete 150 native rows')
    lookup = {row: i for i, row in enumerate(rows)}
    primes, characters, charges = [], [], []
    for q in (7, 13, 19, 31):
        roots = [r for r in range(q) if (r * r + r + 1) % q == 0]
        need(len(roots) == 2, 'both conjugate prime-ideal residue fields')
        for root in roots:
            generator = next(g for g in range(2, q)
                             if len({pow(g, j, q) for j in range(q - 1)}) == q - 1)
            logs = {pow(generator, j, q): j for j in range(q - 1)}
            beta = (1 + root) % q
            c = logs[beta] // ((q - 1) // 6)
            need(logs[beta] % ((q - 1) // 6) == 0 and gcd(c, 6) == 1,
                 'exact native sixth-unit embedding')
            inverse = pow(c, -1, 6)
            table = []
            for a, b in rows:
                value = (a + b * root) % q
                table.append(None if value == 0 else logs[value] * inverse % 6)
            primes.append((q, root))
            characters.append(table)
            charges.append(((q - 1) // 6) % 6)
    need(len(set(primes)) == 8, 'eight distinct actual prime ideals')
    orbit_checks = 0
    for j, table in enumerate(characters):
        for i, row in enumerate(rows):
            rotated = lookup[mul(row, UNITS[1])]
            expect = None if table[i] is None else (table[i] + charges[j]) % 6
            need(table[rotated] == expect, 'literal zero-preserving sixth-unit orbit')
            orbit_checks += 1

    distinct = list(permutations(range(8), 4))
    need(len(distinct) == 1680, 'all ordered fully distinct prime slots')
    row_direct = [(0, 0) for _ in rows]
    killed = surviving = nonzero_surviving = 0
    charge_census = Counter()
    total = (0, 0)
    for p, q, r, s in distinct:
        charge = (charges[p] + charges[q] - charges[r] - charges[s]) % 6
        charge_census[charge] += 1
        kernel = (0, 0)
        for i in range(len(rows)):
            phases = [characters[j][i] for j in (p, q, r, s)]
            if None in phases:
                continue
            value = UNITS[(phases[0] + phases[1] - phases[2] - phases[3]) % 6]
            kernel = add(kernel, value)
            row_direct[i] = add(row_direct[i], value)
        if charge:
            need(kernel == (0, 0), 'every nonzero-charge native kernel vanishes')
            killed += 1
        else:
            surviving += 1
            nonzero_surviving += kernel != (0, 0)
        total = add(total, kernel)
    need(total == (456, 0), 'actual surviving leading signed kernel 456')
    quartic_total = 0
    full = 0
    mask_zeros = 0
    for i in range(len(rows)):
        F = P2 = Q1 = (0, 0)
        V = E4 = 0
        for table in characters:
            e = table[i]
            if e is None:
                mask_zeros += 1
                sixth_power = (1, 0)
                for _ in range(6):
                    sixth_power = mul(sixth_power, (0, 0))
                need(sixth_power == (0, 0) and sixth_power != (1, 0),
                     'positive sixth power retains zero; dropping mask rejected')
                continue
            z = scale(UNITS[e], -1)  # actual prime Mobius coefficient
            F = add(F, z)
            P2 = add(P2, mul(z, z))
            Q1 = add(Q1, scale(z, norm(z)))
            V += norm(z)
            E4 += norm(z) ** 2
        FQ = mul(F, conj(Q1))
        rhs = (norm(sub(mul(F, F), P2)) - 4 * V * norm(F)
               + 4 * (2 * FQ[0] - FQ[1]) + 2 * V * V - 6 * E4)
        need(row_direct[i] == (rhs, 0), 'each exact balanced quartic row identity')
        quartic_total += rhs
        full += norm(F) ** 2
    need((quartic_total, full) == (456, 16752), 'full and collision-subtracted totals')
    need(mask_zeros > 0, 'nonunit zeros actually exercised')

    # Exact finite Euler factorization with unequal integral exponents and moving masks.
    factor_checks = 0
    for i in range(len(rows)):
        for deleted in ((), (0,), (0, 3), (1, 4, 7)):
            C = single_product = pair_product = remainder_product = ONE
            for j, (q, root) in enumerate(primes):
                if j in deleted:
                    continue
                phase = characters[j][i]
                eta = (0, 0) if phase is None else UNITS[phase]
                z = [scale(eta, Fraction(1, q)), scale(eta, Fraction(1, q*q)),
                     scale(conj(eta), Fraction(1, q)),
                     scale(conj(eta), Fraction(1, q*q))]
                numerator = sub(ONE, tuple(map(sum, zip(*z))))
                singles = pairs = ONE
                for zi in z:
                    singles = mul(singles, sub(ONE, zi))
                for a in range(4):
                    for b in range(a + 1, 4):
                        pairs = mul(pairs, sub(ONE, mul(z[a], z[b])))
                E = divide(numerator, mul(singles, pairs))
                need(mul(mul(singles, pairs), E) == numerator,
                     'exact unequal finite local all-pair identity')
                C = mul(C, numerator)
                single_product = mul(single_product, singles)
                pair_product = mul(pair_product, pairs)
                remainder_product = mul(remainder_product, E)
                factor_checks += 1
            need(mul(mul(single_product, pair_product), remainder_product) == C,
                 'exact moving-row/moving-Q finite Euler product')

    pair_bounds = 0
    for q in (7, 13, 19, 31):
        for e in range(6):
            eta2 = mul(UNITS[e], UNITS[e])
            absolute_square = norm(sub(ONE, scale(eta2, Fraction(1, q))))
            for k in range(1, 9):
                lhs_square = (absolute_square ** (k * (k - 1))
                              * Fraction(q - 1, q) ** (2 * k * k))
                rhs_square = Fraction(q - 1, q) ** (2 * k)
                need(lhs_square <= rhs_square, 'actual sixth-phase paired critical bound')
                pair_bounds += 1
        off_slice = Fraction(q, q - 1) ** 2
        need(off_slice > 1, 'independent-frequency local growth negative control')
    return {'native_rows': len(rows), 'actual_prime_ideals': primes,
            'unit_orbit_symbol_checks': orbit_checks,
            'fully_distinct_ordered_tuples': len(distinct),
            'unit_charge_census': dict(sorted(charge_census.items())),
            'exactly_unit_killed_tuples': killed,
            'unit_surviving_tuples': surviving,
            'nonzero_surviving_tuple_kernels': nonzero_surviving,
            'leading_signed_kernel': total,
            'full_fourth_moment': full,
            'quartic_row_identities': len(rows),
            'nonunit_symbol_zeros_exercised': mask_zeros,
            'unequal_local_factorization_checks': factor_checks,
            'moving_mask_product_checks': len(rows) * 4,
            'paired_critical_rational_inequalities': pair_bounds,
            'off_slice_growth_controls': 4}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    source_root = Path('/workspace/.riemann-research/moment-sources')
    sources = {
        Path('/workspace/.riemann-research/sources/qrh11-12.tex'):
        'd9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d',
        source_root / '914/standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md':
        'c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983',
        source_root / '914/standalone/2026-10-10-sextic-moment-conductor-core/INTERACTION_GRAPH.md':
        '46ac022dcbeee727689d1f2bc247ec22eae54850dd7e010ff2de35d42e1405c5',
        source_root / '915/standalone/2026-10-10-sextic-critical-core/REFLECTION_SCALAR_AUDIT.md':
        '17bdce731735412cc463c50c944df9240736e5797282f2c5a4eed5a07b2e21e2',
        source_root / '916/standalone/2026-10-10-all-order-collision-removal/PROOF.md':
        'c67f2469e2d2dfce91cdf2b70220fa53978091c0756ffac9a676737e00792a3f',
        Path('/workspace/riemann/research/exploratory/2026-10-10-four-hour-wave/arithmetic/MASK_DENSITY_REFINEMENT.md'):
        'ecddc2ee84fac81d6905663e3f08c7fbff62d54c08f2a01aa402f9e640b98d2c',
        Path('/workspace/riemann/research/exploratory/2026-10-10-four-hour-wave/literature/GENERALIZED_MOMENT_ATTACK.md'):
        '923fac6659314cff53319a80207d1aca7b58d90a154efec4f6de31844f21e94e',
        source_root / '915/standalone/2026-10-10-sextic-critical-core/LOG_FREE_REPLICATED_SPIKES.md':
        'b59978c1c5d3b5cb904c7f22d675a67bb71b2af512db9f0577e568a04565a86b'}
    for path, expected in sources.items():
        need(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
             f'frozen source binding: {path}')
    here = Path(__file__).resolve()
    record = {'status': 'PASS_EXACT_PRIME_SLOT_CANCELLATION_CONTROLS',
              'proof_sha256': hashlib.sha256(here.with_name('PRIME_SLOT_CANCELLATION.md').read_bytes()).hexdigest(),
              'checker_sha256': hashlib.sha256(here.read_bytes()).hexdigest(),
              'sources': {str(path): digest for path, digest in sources.items()},
              'formal_controls': [formal_control(r) for r in (2, 4, 6, 8)],
              'native_controls': native_control(),
              'asymptotic_trace_contract_proved': False,
              'power_saving_proved': False,
              'generalized_moment_proved': False,
              'rh_proved': False}
    payload = json.dumps(record, sort_keys=True, indent=2) + '\n'
    if args.output:
        args.output.write_text(payload)
    print(payload, end='')


if __name__ == '__main__':
    main()
