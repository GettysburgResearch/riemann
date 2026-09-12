"""Exact finite LP-quantization obstruction. Python standard library only.

The input is the explicit synthetic source below, NOT theta or a gamma stage.
No numerical eigenvalue, floating-point, external moment or zero oracle is used.
"""
from fractions import Fraction as Q
from itertools import product
import argparse
import json
from pathlib import Path


def det(a):
    a = [list(row) for row in a]
    value = Q(1)
    for k in range(len(a)):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, len(a)) if a[j][k]), None)
            if j is None:
                return Q(0)
            a[k], a[j] = a[j], a[k]
            value = -value
        p = a[k][k]
        value *= p
        for i in range(k + 1, len(a)):
            t = a[i][k] / p
            for j in range(k + 1, len(a)):
                a[i][j] -= t * a[k][j]
    return value


def check(condition, label):
    if not condition:
        raise ValueError(label)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        check(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def authenticate(raw, expected):
    value = json.loads(raw, object_pairs_hook=unique_object)
    # Encoding preserves JSON types: false is not accepted in place of 0.
    canonical = lambda x: json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False)
    check(canonical(value) == canonical(expected), 'artifact mismatch')


def self_test(expected):
    bad = json.loads(json.dumps(expected))
    bad['primitive_moments_replayed'][0] = False
    modified = json.loads(json.dumps(expected))
    modified['q1_through_q4'][0] = '21/3'
    raw = json.dumps(expected)
    cases = [json.dumps(bad), json.dumps(modified), '{"status":"changed",' + raw[1:]]
    for case in cases:
        try:
            authenticate(case, expected)
        except ValueError:
            continue
        raise ValueError('mutation accepted')
    return len(cases)


def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def moments_from_powers(q):
    # Newton identities: k e_k = sum (-1)^(j-1) q_j e_(k-j).
    e = [Q(1)]
    factorial = 1
    moments = [Q(1)]
    for k in range(1, len(q)):
        e.append(sum((-1) ** (j - 1) * q[j] * e[k - j]
                     for j in range(1, k + 1)) / k)
        factorial *= (2 * k - 1) * (2 * k)
        moments.append(factorial * e[k])
    return moments


def closed_walk_moment(diag, off_squared, k):
    # Every edge of a closed walk on a path is traversed an even number
    # of times. Thus sqrt(b_i) factors can be evaluated using rationals.
    if k == 0:
        return Q(1)
    total = Q(0)
    for inside in product(range(3), repeat=k - 1):
        path = (0,) + inside + (0,)
        value = Q(1)
        counts = [0, 0]
        for i, j in zip(path, path[1:]):
            if i == j:
                value *= diag[i]
            elif abs(i - j) == 1:
                counts[min(i, j)] += 1
            else:
                value = Q(0)
                break
        if value:
            check(all(c % 2 == 0 for c in counts), 'closed-walk parity')
            for b, c in zip(off_squared, counts):
                value *= b ** (c // 2)
            total += value
    return total


def add_interval(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul_interval(a, b):
    values = [x * y for x in a for y in b]
    return min(values), max(values)


def scale_interval(a, c):
    return mul_interval(a, (c, c))


def produce():
    b, delta = Q(21, 2), Q(1, 10**6)
    q = [Q(0), b, b, b * (1 + delta), b * (1 + 3 * delta)]
    moments = moments_from_powers(q)
    ordinary = [[moments[i + j] for j in range(3)] for i in range(3)]
    shifted = [[moments[i + j + 1] for j in range(2)] for i in range(2)]
    gram = [[q[i + j + 1] for j in range(2)] for i in range(2)]
    hankel = [[q[i + j + 2] for j in range(2)] for i in range(2)]
    minors = {name: [det([row[:k] for row in matrix[:k]])
                     for k in range(1, len(matrix) + 1)]
              for name, matrix in [('ordinary', ordinary), ('shifted', shifted),
                                   ('CSI_G2', gram), ('CSI_J2', hankel)]}
    check(all(x > 0 for row in minors.values() for x in row), 'positive forms')

    # Primitive probability source: positive three-by-three Jacobi matrix.
    a0 = moments[1]
    b1 = moments[2] - a0 * a0
    a1 = (moments[3] - 2 * a0 * moments[2] + a0**2 * moments[1]) / b1
    p2 = [a0 * a1 - b1, -a0 - a1, Q(1)]
    h2 = sum(c * moments[i] for i, c in enumerate(mul(p2, p2)))
    b2 = h2 / b1
    d1 = a1 - b1 / a0
    a2 = 1 + b2 / d1
    check(a0 > 0 and b1 > 0 and b2 > 0 and d1 > 0, 'positive Jacobi data')
    check(a2 - b2 / d1 == 1, 'positive final Schur complement')
    for k in range(5):
        check(closed_walk_moment([a0, a1, a2], [b1, b2], k) == moments[k],
              'primitive Jacobi moment replay')

    # Exact obstruction with sqrt(delta)=1/1000.
    radius = b * (4 * delta + Q(2, 1000))
    check(b - radius > 10 and b + radius < 11, 'integer-occupancy obstruction')

    # Robust power-sum box, inclusive radius 1e-4 in each of q1,q2,q3.
    tol = Q(1, 10000)
    lo = [None] + [q[k] - tol for k in range(1, 4)]
    hi = [None] + [q[k] + tol for k in range(1, 4)]
    blo, bhi = lo[1]**2 / hi[2], hi[1]**2 / lo[2]
    delta_hi = hi[1] * hi[3] / lo[2]**2 - 1
    check(delta_hi < Q(1, 20000), 'robust variance ceiling')
    # sqrt(delta) < 1/100 is a deliberately coarse rational bound.
    robust_radius = bhi * (Q(4, 20000) + Q(2, 100))
    check(blo - robust_radius > 10 and bhi + robust_radius < 11,
          'robust integer-occupancy obstruction')

    # A box of raw even moment errors <=1e-7 maps inside that power-sum box.
    mtol = Q(1, 10**7)
    e1, e2, e3 = [(moments[k] / f - mtol / f, moments[k] / f + mtol / f)
                  for k, f in [(1, 2), (2, 24), (3, 720)]]
    qboxes = [e1, add_interval(mul_interval(e1, e1), scale_interval(e2, -2)),
              add_interval(add_interval(mul_interval(mul_interval(e1, e1), e1),
                                        scale_interval(mul_interval(e1, e2), -3)),
                           scale_interval(e3, 3))]
    for k, interval in enumerate(qboxes, 1):
        check(q[k] - tol < interval[0] <= interval[1] < q[k] + tol,
              'raw moment box maps inside excluded power-sum box')

    return {'status': 'exact synthetic finite obstruction; not a theta result',
            'arithmetic': 'Python Fraction exact rational; no external input',
            'q1_through_q4': list(map(str, q[1:])),
            'even_moments_0_through_8': list(map(str, moments)),
            'positive_leading_minors': {k: list(map(str, v)) for k, v in minors.items()},
            'jacobi_diagonal': list(map(str, [a0, a1, a2])),
            'jacobi_off_diagonal_squared': list(map(str, [b1, b2])),
            'primitive_moments_replayed': [0, 2, 4, 6, 8],
            'exact_occupancy_radius': str(radius),
            'robust_q_tolerance': str(tol), 'robust_raw_moment_tolerance': str(mtol),
            'robust_delta_upper': str(delta_hi),
            'robust_b_interval': list(map(str, [blo, bhi])),
            'robust_occupancy_radius': str(robust_radius)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path)
    parser.add_argument('--check', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    result = produce()
    if args.check:
        authenticate(args.check.read_text(encoding='utf-8'), result)
    if args.write:
        args.write.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'accepted': True, 'primitive_moments': 5,
                      'positive_forms': 4, 'robust_exclusion': True,
                      'mutations_rejected': self_test(result) if args.self_test else 0}))
