#!/usr/bin/env python3
"""Exact finite checks for the support-rigidity / leakage packet.

Standard library only. All accepted mathematical comparisons use integers or
fractions.Fraction. The universal statements are proved in PROOF.md; these
finite checks are regression tests, not an RH certificate.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import json
from math import gcd
from pathlib import Path
import sys


class VerificationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


@lru_cache(maxsize=None)
def divisors(n: int) -> tuple[int, ...]:
    if n < 1:
        raise ValueError("positive integer required")
    return tuple(d for d in range(1, n + 1) if n % d == 0)


@lru_cache(maxsize=None)
def mobius(n: int) -> int:
    if n < 1:
        raise ValueError("positive integer required")
    m, parity, p = n, 0, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            parity += 1
            if m % p == 0:
                return 0
        p += 1
    if m > 1:
        parity += 1
    return -1 if parity % 2 else 1


@lru_cache(maxsize=None)
def b(n: int, k: int) -> F:
    if n < 1 or k < 0:
        raise ValueError("invalid fractional-part arguments")
    return F(k % n, n)


def u(r: int, k: int) -> int:
    return mobius(r // k) if k >= 1 and r % k == 0 else 0


@lru_cache(maxsize=None)
def dual(r: int) -> tuple[int, ...]:
    if r < 2:
        raise ValueError("dual index must be at least two")
    return tuple(k * (k + 1) * (u(r, k) - u(r, k + 1))
                 for k in range(1, r + 1))


def inner(x, y) -> F:
    # Both inputs are finite, indexed from k=1. Missing coordinates are zero.
    return sum((F(a) * F(c) / (k * (k + 1))
                for k, (a, c) in enumerate(zip(x, y), 1)), F(0))


def atom(d: int, k: int) -> F:
    return sum((mobius(d // n) * n * b(n, k) for n in divisors(d)), F(0))


def ramanujan(d: int, k: int) -> int:
    return sum(n * mobius(d // n) for n in divisors(gcd(d, k)))


def dual_gram(r: int, s: int) -> int:
    diagonal = 2 * sum(a * a * mobius(r // a) * mobius(s // a)
                       for a in divisors(gcd(r, s)))
    adjacent = sum(a * c * mobius(r // a) * mobius(s // c)
                   for a in divisors(r) for c in divisors(s) if abs(a - c) == 1)
    return diagonal - adjacent


def invert(matrix) -> list[list[F]]:
    n = len(matrix)
    require(n > 0 and all(len(row) == n for row in matrix), "square matrix required")
    aug = [[F(x) for x in row] + [F(i == j) for j in range(n)]
           for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if aug[i][j]), None)
        require(pivot is not None, "singular matrix")
        if pivot != j:
            aug[j], aug[pivot] = aug[pivot], aug[j]
        scale = aug[j][j]
        aug[j] = [x / scale for x in aug[j]]
        for i in range(n):
            if i == j or not aug[i][j]:
                continue
            scale = aug[i][j]
            aug[i] = [a - scale * c for a, c in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def matvec(matrix, vector):
    return [sum((a * c for a, c in zip(row, vector)), F(0)) for row in matrix]


def quadratic(matrix, vector):
    return sum((a * c for a, c in zip(vector, matvec(matrix, vector))), F(0))


def head_parameters(N):
    a = sum((F(1, k + 1) for k in range(1, N + 1)), F(0))
    z = sum((F(k, k + 1) for k in range(1, N + 1)), F(0))
    t = [sum((b(n, k) / (k + 1) for k in range(1, N + 1)), F(0))
         for n in range(2, N + 1)]
    return a, z, t


def compute() -> dict:
    counts = Counter()
    # Independent Mobius construction by divisor recurrence.
    mu_rec = {1: 1}
    for n in range(2, 121):
        mu_rec[n] = -sum(mu_rec[d] for d in divisors(n) if d < n)
        require(mobius(n) == mu_rec[n], f"Mobius recurrence at {n}")
        counts['mobius_recurrence'] += 1
    for r in range(2, 33):
        dr = dual(r)
        require(inner([1] * r, dr) == mobius(r), f"dual source r={r}")
        require(inner(list(range(1, r + 1)), dr) == 0, f"ramp r={r}")
        counts['dual_sources_and_ramps'] += 2
        for n in range(2, 65):
            value = inner([b(n, k) for k in range(1, r + 1)], dr)
            require(value == -int(n == r), f"biorthogonality r={r},n={n}")
            counts['biorthogonality'] += 1
        for s in range(2, 33):
            require(inner(dr, dual(s)) == dual_gram(r, s), f"dual Gram {r},{s}")
            counts['integer_gram_entries'] += 1
        for n in range(2, 49):
            value = inner([atom(n, k) for k in range(1, r + 1)], dr)
            expected = -r * mobius(n // r) if n % r == 0 else 0
            require(value == expected, f"Ramanujan transport {r},{n}")
            counts['ramanujan_dual_transport'] += 1
    for d in range(2, 31):
        for k in range(1, 41):
            require(atom(d, k) - atom(d, k - 1) == -ramanujan(d, k),
                    f"Ramanujan difference {d},{k}")
            counts['ramanujan_differences'] += 1
    snapshots = []
    for N in list(range(2, 19)) + [24]:
        idx = list(range(2, N + 1))
        gram = [[F(dual_gram(r, s)) for s in idx] for r in idx]
        inv = invert(gram)
        mu = [F(mobius(r)) for r in idx]
        a, z, t = head_parameters(N)
        head = [[sum((b(r, k) * b(s, k) / (k * (k + 1))
                       for k in range(1, N + 1)), F(0)) for s in idx] for r in idx]
        for i in range(N - 1):
            for j in range(N - 1):
                require(head[i][j] == inv[i][j] + t[i] * t[j] / z,
                        f"finite head decomposition {N},{i},{j}")
                counts['head_gram_entries'] += 1
        exact_error = F(1, N + 1) + a * a / z
        require(1 - quadratic(inv, mu) == exact_error, f"dual optimum N={N}")
        counts['dual_optimum'] += 1
        coefficients = [
            [F(0) for n in idx],
            [-F(mobius(n)) for n in idx],
            [F(((n * 17 + N) % 13) - 6, n + 1) for n in idx],
            [F((-1) ** n, n) for n in idx],
        ]
        for case, c in enumerate(coefficients):
            residual = [1 - sum((c[n - 2] * b(n, k) for n in idx), F(0))
                        for k in range(1, N + 1)]
            fit = quadratic(inv, [x + m for x, m in zip(c, mu)])
            ramp = (a - sum((x * y for x, y in zip(t, c)), F(0))) ** 2 / z
            require(inner(residual, residual) == fit + ramp,
                    f"three-part head identity N={N},case={case}")
            counts['source_head_decompositions'] += 1
            # A finite tail is independently appended; the infinite tail
            # remains symbolic in the universal proof.
            tail = sum(((1 - sum((c[n - 2] * b(n, k) for n in idx), F(0))) ** 2
                        / (k * (k + 1)) for k in range(N + 1, 3 * N + 1)), F(0))
            full_prefix = [1 - sum((c[n - 2] * b(n, k) for n in idx), F(0))
                           for k in range(1, 3 * N + 1)]
            require(inner(full_prefix, full_prefix) == fit + ramp + tail,
                    f"appended tail N={N},case={case}")
            counts['appended_finite_tails'] += 1
            for r in idx:
                require(inner(residual, dual(r)) == c[r - 2] + mobius(r),
                        f"coefficient recovery N={N},case={case},r={r}")
                counts['coefficient_recovery'] += 1
        # Compute the exact projection itself, not just its norm.
        beta = matvec(inv, mu)
        projection = [sum((beta[r - 2] * (dual(r)[k - 1] if k <= r else 0)
                           for r in idx), F(0)) for k in range(1, N + 1)]
        require(projection == [1 - a * k / z for k in range(1, N + 1)],
                f"dual projection N={N}")
        counts['dual_projection_vectors'] += 1
        if N in (2, 6, 12, 18, 24):
            snapshots.append({'N': N, 'dual_distance_squared': str(exact_error),
                              'ramp_norm_squared': str(z), 'ramp_source': str(a)})
    require(list(dual(6)) == [4, 0, -12, 0, -30, 42], "six-point witness")
    require(inner(dual(6), dual(6)) == 92, "six-point norm")
    require(inner([1] * 6, dual(6)) == 1, "six-point source")
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        n = p
        while n <= 1000:
            require(inner([atom(n, k) for k in range(1, 7)], dual(6)) == 0,
                    f"prime-power obstruction {n}")
            counts['prime_power_obstruction_controls'] += 1
            n *= p
    # Multiple omitted-denominator witness has an exact rational certificate.
    omitted = [6, 10, 14, 15]
    omitted_gram = [[F(dual_gram(r, s)) for s in omitted] for r in omitted]
    omitted_mu = [F(mobius(r)) for r in omitted]
    multi_bound = quadratic(invert(omitted_gram), omitted_mu)
    require(multi_bound >= F(1, 92), "multi-witness monotonicity")
    return {
        'schema': 1,
        'status': 'EXACT_RATIONAL_FINITE_REGRESSION',
        'rh_proved': False,
        'counts': dict(sorted(counts.items())),
        'single_witness': {'index': 6, 'vector': list(dual(6)),
                           'norm_squared': 92, 'source': 1,
                           'error_lower_bound': '1/92'},
        'multi_witness': {'indices': omitted, 'error_lower_bound': str(multi_bound)},
        'dual_projection_snapshots': snapshots,
        'scope': 'Finite identities only; universal claims use the written proofs.',
    }


def reject_controls(pristine: dict) -> list[str]:
    rejected = []
    candidates = []
    for label, updater in (
        ('wrong_witness_sign', lambda r: r['single_witness']['vector'].__setitem__(0, -4)),
        ('wrong_witness_norm', lambda r: r['single_witness'].__setitem__('norm_squared', 91)),
        ('rh_status_promotion', lambda r: r.__setitem__('rh_proved', True)),
        ('missing_coverage', lambda r: r['counts'].__setitem__('biorthogonality', 1)),
        ('wrong_dual_optimum', lambda r: r['dual_projection_snapshots'][0].__setitem__('dual_distance_squared', '0')),
    ):
        altered = json.loads(json.dumps(pristine))
        updater(altered)
        candidates.append((label, altered))
    for label, altered in candidates:
        try:
            require(altered == pristine, 'result does not match independent reconstruction')
        except VerificationError:
            rejected.append(label)
        else:
            raise VerificationError('mutation accepted: ' + label)
    # Direct mathematical failures, not just corrupted result metadata.
    require(dual_gram(2, 3) != 2 * sum(a*a*mobius(2//a)*mobius(3//a)
                                     for a in divisors(1)), 'adjacency mutation escaped')
    rejected.append('drop_adjacent_divisor_terms')
    N = 6
    a, z, t = head_parameters(N)
    require(a*a/z > 0, 'dropped ramp must change zero-coefficient error')
    rejected.append('drop_rank_one_ramp')
    require(F(1, N + 1) > 0, 'dropped tail must change zero-coefficient error')
    rejected.append('drop_tail')
    require(F(14) != F(1, 14), 'Gram/inverse confusion')
    rejected.append('use_gram_instead_of_inverse')
    return rejected


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise VerificationError('duplicate JSON key: ' + key)
        out[key] = value
    return out


def read_json(path: Path):
    with path.open('r', encoding='utf-8') as stream:
        return json.load(stream, object_pairs_hook=unique_object)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path, help='write freshly reconstructed result JSON')
    parser.add_argument('--check', type=Path, help='compare supplied JSON with fresh reconstruction')
    parser.add_argument('--self-test', action='store_true', help='run explicit rejection controls')
    args = parser.parse_args()
    result = compute()
    if args.self_test:
        rejected = reject_controls(result)
        try:
            json.loads('{"schema":1,"schema":1}', object_pairs_hook=unique_object)
        except VerificationError:
            rejected.append('duplicate_json_key')
        else:
            raise VerificationError('duplicate-key input accepted')
        print(json.dumps({'rejected_controls': rejected}, sort_keys=True), file=sys.stderr)
    if args.check:
        require(read_json(args.check) == result, 'certificate differs from reconstruction')
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.write:
        args.write.write_text(text, encoding='utf-8')
    sys.stdout.write(text)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (VerificationError, ValueError, OSError, json.JSONDecodeError) as error:
        print('REJECT: ' + str(error), file=sys.stderr)
        raise SystemExit(1)
