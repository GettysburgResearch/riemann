#!/usr/bin/env python3
"""DSE27. Exact integer/divisor reconstruction and outward energy bounds.
The native all-scale gain is NOT established. Standard library only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import subprocess
from functools import lru_cache
from math import isqrt
from pathlib import Path

BITS = 112
SCALE = 1 << BITS


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def mobius(n: int) -> list[int]:
    require(type(n) is int and n >= 1, 'positive integer cutoff required')
    a = [1] * (n + 1)
    a[0] = 0
    prime = bytearray(b'\x01') * (n + 1)
    prime[:2] = b'\x00\x00'
    for p in range(2, n + 1):
        if prime[p]:
            for k in range(p, n + 1, p):
                a[k] = -a[k]
                if k > p:
                    prime[k] = 0
            for k in range(p * p, n + 1, p * p):
                a[k] = 0
    return a


def primitive_trial(n: int) -> int:
    if n == 0:
        return 0
    out, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            out = -out
            if n % p == 0:
                return 0
        p += 1
    return -out if n > 1 else out


def prefix(a: list[int]) -> list[int]:
    out = [0]
    for v in a[1:]:
        out.append(out[-1] + v)
    return out


def mertens_solver(y: int):
    seed = mobius(y)
    initial = prefix(seed)
    work = [0]

    @lru_cache(maxsize=None)
    def M(n: int) -> int:
        if n <= y:
            return initial[n]
        total, lo = 1, 2
        while lo <= n:
            q = n // lo
            hi = n // q
            total -= (hi - lo + 1) * M(q)
            lo = hi + 1
            work[0] += 1
        return total
    return M, seed, initial, work


def square_mesh(lo: int, last: int) -> list[int]:
    require(1 <= lo <= last, 'invalid observation interval')
    pts = {lo, last}
    for j in range(max(1, isqrt(16 * lo) - 1), isqrt(16 * last) + 2):
        v = j * j // 16
        if lo < v < last:
            pts.add(v)
    return sorted(pts)


def add_positive_fraction(acc: list[int], numerator: int, denominator: int) -> None:
    require(numerator >= 0 and denominator > 0, 'invalid positive fraction')
    q, r = divmod(numerator * SCALE, denominator)
    acc[0] += q
    acc[1] += q + (r != 0)


def sqrt_bounds(interval: list[int]) -> list[int]:
    lo, hi = interval
    require(0 <= lo <= hi, 'invalid nonnegative interval')
    a = isqrt(lo * SCALE)
    b = isqrt(hi * SCALE)
    return [a, b + (b * b != hi * SCALE)]


def energy_from_samples(points: list[int], values: list[int]) -> dict:
    require(len(points) == len(values) and len(points) >= 1, 'bad sample count')
    require(all(type(v) is int for v in points + values), 'integer samples required')
    require(points[0] >= 1, 'positive coordinates required')
    S, Z = [0, 0], [0, 0]
    covered = 1
    for a, b, u, v in zip(points, points[1:], values, values[1:]):
        h = b - a
        require(h > 0 and abs(v - u) <= h, 'unordered or non-Lipschitz samples')
        split = a + h // 2 + 1  # tie goes to the left endpoint
        add_positive_fraction(S, u * u * (split - a), a * split)
        add_positive_fraction(S, v * v * (b - split), split * b)
        add_positive_fraction(Z, (h // 2) ** 2 * h, a * b)
        covered += h
    n = points[-1]
    add_positive_fraction(S, values[-1] ** 2, n * (n + 1))
    rs, rz = sqrt_bounds(S), sqrt_bounds(Z)
    lower = max(0, rs[0] - rz[1]) ** 2 // SCALE
    upper_num = (rs[1] + rz[1]) ** 2
    upper = (upper_num + SCALE - 1) // SCALE
    return {'sample_energy': S, 'complete_error_budget': Z,
            'energy_enclosure': [lower, upper], 'covered_integer_cells': covered}


def prefix_energy(initial: list[int]) -> list[int]:
    acc = [0, 0]
    for k, m in enumerate(initial[1:], 1):
        add_positive_fraction(acc, m * m, k * (k + 1))
    return acc


def sample_digest(points: list[int], values: list[int]) -> str:
    payload = ''.join(f'{n} {v}\n' for n, v in zip(points, values)).encode('ascii')
    return hashlib.sha256(payload).hexdigest()


def run(y: int, engine: Path | None = None, full_check: bool = False) -> dict:
    require(type(y) is int and 1 <= y <= 4095, 'bounded checker cutoff 1..4095')
    b, last = y + 1, (y + 1) ** 2 - 1
    M, seed, initial, work = mertens_solver(y)
    points = square_mesh(b, last)
    if engine is None:
        require(not full_check, 'full comparison needs the compiled engine')
        vals = [M(n) for n in points]
        independent = None
    else:
        cmd = [str(engine.resolve())] + (['--full-check'] if full_check else [])
        data = f'{y} {len(points)}\n' + ' '.join(map(str, points)) + '\n'
        process = subprocess.run(cmd, input=data, text=True, capture_output=True, check=True)
        independent = json.loads(process.stdout, object_pairs_hook=reject_duplicates)
        vals = independent['samples']
        require(all(type(v) is int for v in vals), 'noninteger engine values')
    part = energy_from_samples(points, vals)
    e0 = prefix_energy(initial)
    total = [e0[i] + part['energy_enclosure'][i] for i in (0, 1)]
    # (1+E_B)^2 <= 4(1+E_Y)^3; sufficient finite p=3/2 E-gain.
    gain = (SCALE + total[1]) ** 2 * SCALE <= 4 * (SCALE + e0[0]) ** 3
    if full_check:
        require(independent['full_sieve_checked'] is True, 'missing independent reconstruction')
        exact = [int(v) << (BITS - 64) for v in independent['full_energy_enclosure']]
        require(total[0] <= exact[0] <= exact[1] <= total[1], 'sparse enclosure fails independent full energy')
        print('FULL_SIEVE_ENERGY ' + canonical(independent['full_energy_enclosure']), file=__import__('sys').stderr)
    return {'Y': y, 'B': last, 'arithmetic': 'integers; outward 112-bit binary intervals',
            'prefix_energy': e0, 'annulus': part, 'total_energy': total,
            'finite_E_gain_certified': gain,
            'sample_count': len(points), 'sample_sha256': sample_digest(points, vals),
            'sample_examples': [[points[i], vals[i]] for i in sorted({0, len(points)//2, len(points)-1})],
            'prefix_mu_sha256': hashlib.sha256(bytes(v+1 for v in seed[1:])).hexdigest(),
            'future_mobius_values_used_in_recurrence': 0}


def reject_duplicates(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--Y', type=int, default=1023)
    p.add_argument('--engine', type=Path)
    p.add_argument('--full-check', action='store_true')
    p.add_argument('--write', type=Path)
    p.add_argument('--check', type=Path)
    args = p.parse_args()
    value = {'packet': 'DSE27', 'schema': 1, 'bits': BITS,
             'RH_proved': False, 'native_unbounded_gain_proved': False, 'result': run(args.Y, args.engine, args.full_check)}
    if args.check:
        expected = json.loads(args.check.read_text(), object_pairs_hook=reject_duplicates)
        require(canonical(value) == canonical(expected), 'report does not match exact reconstruction')
    if args.write:
        args.write.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')
    print(canonical(value))

if __name__ == '__main__':
    main()
