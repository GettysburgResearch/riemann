#!/usr/bin/env python3
"""BUB26: bounded exact checks only; no zeta evaluator or zero census.

The all-height analytic statements and Conrey's theorem are paper/imported
inputs. This program does not certify their truth by generating a JSON file.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'README.md', 'PROOF.md', 'SOURCES.json', 'VALIDATION.md',
         'check.py', 'test_check.py', 'result.json', 'SHA256SUMS'}
PARENT = 'ee7f76736c235714496526f999e028d181302b56'
RHO = F(31, 80)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def int_arg(value: int, minimum: int, name: str) -> None:
    require(type(value) is int and value >= minimum, f'invalid {name}')


def ceil_log2_int(value: int) -> int:
    int_arg(value, 1, 'log argument')
    return (value - 1).bit_length()


def ceil_log2_fraction(value: F) -> int:
    require(isinstance(value, F) and value >= 1, 'invalid rational log argument')
    k = max(0, value.numerator.bit_length() - value.denominator.bit_length())
    while value.denominator * (1 << k) < value.numerator:
        k += 1
    return k


def schedule(height: int, resolution_bits: int) -> dict:
    int_arg(height, 1, 'height')
    int_arg(resolution_bits, 0, 'resolution bits')
    L = 1 + 6 * ceil_log2_int(height + 10)
    B = (8 * height + 6) // 7 + 5 + (8 * resolution_bits + 28) * L
    C = F(6, 175) * (2 * (height + 5) ** 3 + 3)
    m = ceil_log2_fraction(C)
    blocks = (B + m + 15) // 15
    depth = 11 * blocks
    # These test the finite arithmetic in the written threshold, not xi.
    require(2 * (height + 10) ** 6 <= (1 << L), 'source disk ceiling')
    require(C <= 1 << m and C > F(1 << m, 2), 'rational ceil log')
    require(15 * blocks >= B + m + 1, 'error exponent budget')
    require(depth >= 1, 'depth positivity')
    return {'R': height, 'a': resolution_bits, 'L': L, 'B': B,
            'C_R': str(C), 'm': m, 'depth': depth}


def ordinate(multiplicity: int, pair_multiplicity: int) -> dict:
    int_arg(multiplicity, 0, 'central multiplicity')
    int_arg(pair_multiplicity, 0, 'off-central pair multiplicity')
    N = multiplicity + 2 * pair_multiplicity
    S = int(multiplicity == 1)
    G = int(multiplicity == 1 and pair_multiplicity == 0)
    require(2 * G >= 3 * S - N, 'ordinate pairing inequality')
    return {'central': multiplicity, 'pairs': pair_multiplicity,
            'N': N, 'S': S, 'G': G, 'slack': 2*G-3*S+N}


def poly_mul(a: list[F], b: list[F]) -> list[F]:
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def cmul(a: tuple[F, F], b: tuple[F, F]) -> tuple[F, F]:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def poly_eval(a: list[F], z: tuple[F, F]) -> tuple[F, F]:
    v = (F(0), F(0))
    for coefficient in reversed(a):
        v = cmul(v, z)
        v = v[0]+coefficient, v[1]
    return v


def sharp_synthetic() -> dict:
    """w=s-1/2. This polynomial is NOT an actual zeta source."""
    p = [F(1)]
    positive_roots = [(F(0), F(1))]
    for t in (2, 3, 4):
        positive_roots.extend((x, F(t)) for x in (F(0), F(1, 4), F(-1, 4)))
    for x, t in positive_roots:
        p = poly_mul(p, [x*x+t*t, -2*x, F(1)])
    derivative = [F(j)*p[j] for j in range(1, len(p))]
    for x, t in positive_roots:
        for sign in (-1, 1):
            root = (x, sign*t)
            require(poly_eval(p, root) == (0, 0), 'synthetic root identity')
            require(poly_eval(derivative, root) != (0, 0), 'synthetic root simple')
    require(all(p[j] == 0 for j in range(1, len(p), 2)), 'reflection symmetry')
    N, S, G = 10, 4, 1
    require(2*G == 3*S-N and F(G, N) == F(1, 10), 'sharp count')
    return {'kind': 'synthetic_not_zeta', 'degree': len(p)-1,
            'coefficients_in_s_minus_half': [str(x) for x in p],
            'positive_height_N': N, 'simple_central_S': S, 'clean_G': G}


def source_moments() -> list[dict]:
    # Two independent reconstructions: raw branching recurrence vs closed m3.
    m = [F(1)]
    for j in range(1, 4):
        m.append(m[-1] * (F(5, 2)+j-1)/F(5, 2))
    rows = []
    for depth in range(9):
        closed = F(93, 35) - F(24, 175)*RHO**depth
        require(m[:3] == [1, 1, F(7, 5)] and m[3] == closed,
                'literal branching moments')
        rows.append({'depth': depth, 'm3': str(m[3]),
                     'peano_mass': str((F(93, 35)-m[3])/6)})
        old = m
        # j=3 binomial coefficients explicitly, independent of a lookup table.
        m = [F(1)]
        for j in range(1, 4):
            a_j = (1-F(2)**(1-2*j))/(2*j-1)
            choose = 1
            total = F(0)
            for i in range(j+1):
                total += choose * old[i] * old[j-i]
                if i < j:
                    choose = choose * (j-i)//(i+1)
            m.append(a_j*total)
    require(F(127, 7)*F(125, 192) == F(15875, 1344) < 12,
            'complete first inverse moment')
    return rows


def reconstruct() -> dict:
    ln2_lower = F(2, 3)+F(2, 81)+F(2, 1215)
    require(ln2_lower > F(11, 16), 'log2 bound')
    require(RHO**11 < F(1, 1 << 15), 'rho block contraction')
    U = F(10)
    em = (1+U/2+U**2/12+U**4/720+U**6/40)/U**6
    require(em < 1, 'Euler Maclaurin constant')
    pairs = [(30,7), (100,7), (1000,10), (10**6,20), (2**20,20)]
    schedules = [schedule(R, a) for R, a in pairs]
    grid = []
    for j in range(4, 33):
        R = 1 << j
        n = 2*R + 64*(j+4)**2
        exact = schedule(R, j)['depth']
        require(n >= exact, 'simple cofinal shadow schedule')
        require(16*j*j+285*j+822 > 0, 'symbolic schedule excess')
        grid.append({'j': j, 'R': R, 'comparison_depth': n,
                     'sharper_depth': exact})
    counts = [ordinate(m, p) for m in range(5) for p in range(4)]
    return {'schema': 'BUB26-v1', 'parent': PARENT,
            'status': {'rh_proved': False, 'gap_free_cover_proved': False,
                       'new_actual_zero_computation': False,
                       'bounded_exact_checks_only': True},
            'constants': {'rho': str(RHO), 'rho11_times_2pow15': str(RHO**11*2**15),
                          'log2_lower': str(ln2_lower), 'em_ratio_at_10': str(em)},
            'schedules': schedules, 'dyadic_schedules': grid,
            'ordinate_panels': counts, 'source_moments': source_moments(),
            'sharp_count_example': sharp_synthetic()}


def reject_duplicates(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate JSON key {key}')
        result[key] = value
    return result


def strict_load(path: Path) -> object:
    return json.loads(path.read_text(encoding='utf-8'),
                      object_pairs_hook=reject_duplicates,
                      parse_float=lambda s: (_ for _ in ()).throw(ValueError('floats forbidden')),
                      parse_constant=lambda s: (_ for _ in ()).throw(ValueError('nonfinite forbidden')))


def same_typed(actual: object, expected: object, path: str = '$') -> None:
    require(type(actual) is type(expected), f'type mismatch at {path}')
    if isinstance(expected, dict):
        require(actual.keys() == expected.keys(), f'keys at {path}')
        for key in expected:
            same_typed(actual[key], expected[key], path+'.'+key)
    elif isinstance(expected, list):
        require(len(actual) == len(expected), f'length at {path}')
        for j, (a, e) in enumerate(zip(actual, expected)):
            same_typed(a, e, f'{path}[{j}]')
    else:
        require(actual == expected, f'value at {path}')


def inventory() -> None:
    # Internal integrity is not authentication against an adversary replacing all files.
    require({p.name for p in ROOT.iterdir()} == FILES, 'inventory differs')
    for name in FILES:
        p = ROOT/name
        require(not p.is_symlink() and p.is_file(), 'nonregular packet member')
    entries = {}
    for line in (ROOT/'SHA256SUMS').read_text(encoding='ascii').splitlines():
        digest, name = line.split('  ')
        require(name in FILES-{'SHA256SUMS'} and name not in entries, 'bad manifest')
        require(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest),
                'bad hash format')
        entries[name] = digest
    require(set(entries) == FILES-{'SHA256SUMS'}, 'manifest coverage')
    for name, digest in entries.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                'hash mismatch: '+name)
    sources = strict_load(ROOT/'SOURCES.json')
    require(sources['parent']['sha'] == PARENT, 'wrong source parent')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit', type=Path, help='producer-only; not a validation receipt')
    group.add_argument('--check', type=Path)
    args = parser.parse_args()
    try:
        expected = reconstruct()
        if args.emit is not None:
            args.emit.write_text(json.dumps(expected, indent=2, sort_keys=True)+'\n', encoding='utf-8')
            print('EMITTED_ONLY')
        else:
            inventory()
            same_typed(strict_load(args.check), expected)
            print('PASS_BUB26_BOUNDED_EXACT_CHECKS_ONLY')
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print('REJECT: '+str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
