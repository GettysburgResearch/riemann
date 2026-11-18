"""Certify signed bias excursions by reflected prime-tail evaluation."""
import argparse
import csv
import hashlib
import io
import json
import lzma
from decimal import Decimal, localcontext
from math import isqrt
from pathlib import Path

import numpy as np


SCALE = 2**40
DISCRIMINANT_LIMIT = 10_000
PHASE_LIMIT = 4096
PERIODS = 16


def factor_distinct(value):
    factors = []
    for p in range(2, isqrt(value) + 1):
        if value % p:
            continue
        factors.append(p)
        while value % p == 0:
            value //= p
    if value > 1:
        factors.append(value)
    return factors


def character(d):
    q = abs(d)
    squarefree_part = d if d % 4 == 1 else d // 4
    if d % 4 != 1 and (d % 4 != 0 or squarefree_part % 4 not in (2, 3)):
        return None
    primes = factor_distinct(abs(squarefree_part))
    if any(squarefree_part % (p*p) == 0 for p in primes):
        return None
    remainder = d
    n = np.arange(q)
    out = np.ones(q, dtype=np.int64)
    for p in primes:
        if p == 2:
            continue
        remainder //= p if p % 4 == 1 else -p
        residues = -np.ones(p, dtype=np.int64)
        a = np.arange(1, p)
        residues[a*a % p] = 1
        residues[0] = 0
        out *= residues[n % p]
    if remainder in (-4, -8, 8):
        out[n % 2 == 0] = 0
        if remainder < 0:
            out[n % 4 == 3] *= -1
        if abs(remainder) == 8:
            out[(n % 8 == 3) | (n % 8 == 5)] *= -1
    else:
        assert remainder == 1
    assert out.sum() == 0
    return out


def tables():
    # Floors of rational weights are exact. Decimal.ln is correctly rounded.
    end = PERIODS * DISCRIMINANT_LIMIT
    weights = np.zeros((end + 1, 4), dtype=np.int64)
    von_mangoldt = np.zeros(PHASE_LIMIT + 1, dtype=np.int64)
    with localcontext() as ctx:
        ctx.prec = 37
        for n in range(1, end + 1):
            log_n = Decimal(n).ln()
            weights[n] = (SCALE//n, int(SCALE*log_n/n),
                          SCALE//(n*n), int(SCALE*log_n/(n*n)))
            if 2 <= n <= PHASE_LIMIT and len(factor_distinct(n)) == 1:
                base = factor_distinct(n)[0]
                von_mangoldt[n] = int(SCALE*Decimal(base).ln()/(n*n))
    # Each approximate integer is within 2 units of its exact scaled value.
    return weights, von_mangoldt


def ratio_endpoints(numerator, denominator, num_radius, den_radius):
    assert denominator > den_radius
    candidates = [(SCALE * (numerator + a*num_radius), denominator + b*den_radius)
                  for a in (-1, 1) for b in (-1, 1)]
    return min(n//d for n, d in candidates), max(-(-n//d) for n, d in candidates)


def certificate(d, char, weights, vm, arch):
    q = len(char)
    end = q * PERIODS
    # Each full-period folded weight is exact signed int64, including final dot.
    # |sum| <= SCALE * sum_{n<=end}(1+log(n))/n < 100*SCALE.
    folded = weights[1:end+1].reshape(PERIODS, q, 4).sum(axis=0)
    rotated = np.roll(char, -1)
    sums = [int(v) for v in rotated @ folded]
    maximum = int(np.max(np.abs(np.cumsum(rotated))))
    radii = [2*end + maximum*(int(w)+2) for w in weights[end]]
    lo1, _ = ratio_endpoints(sums[1], sums[0], radii[1], radii[0])
    _, hi2 = ratio_endpoints(sums[3], sums[2], radii[3], radii[2])

    x = np.arange(len(vm), dtype=np.int64)
    v = char[x % q]*vm
    # Addition of X times the first finite sum minus the second one.
    # At worst 2 X^2 fixed-point units from errors in the von Mangoldt weights.
    # Every intermediate is bounded by O(X*SCALE*(1+sum log n/n^2)).
    assert max(abs(lo1), abs(hi2)) < 20*SCALE
    lower = lo1 - x*hi2 + x*np.cumsum(v) - np.cumsum(x*v) - 2*x*x
    lower += arch[0 if d > 0 else 1]
    # Fixed-point lower bound for sqrt(x)*lower/SCALE in thousandths.
    # Only positive lower entries may be certified this way.
    # This selection is heuristic alone; the strict inequality below is exact.
    best = int(np.argmax(np.sqrt(x[1:]) * lower[1:])) + 1
    score = int(lower[best])
    if score <= 0 or 9*best*score*score <= 4*SCALE*SCALE:
        return None
    milli = isqrt(best*(1000*score)**2)//SCALE
    return best, milli


def arch_table():
    # Archimedean contribution divided by sqrt(x); summands are all positive.
    tables = []
    for a in (0, 1):
        terms = [0]
        for x in range(1, PHASE_LIMIT + 1):
            value = 0
            for h in range(128):
                term = SCALE//(x**(a+1+2*h)*(a+1+2*h)*(a+2+2*h))
                if term == 0:
                    break
                value += term
            terms.append(value)
        tables.append(np.array(terms, dtype=np.int64))
    return tables


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='write compressed verified witnesses')
    args = parser.parse_args()
    weights, vm = tables()
    arch = arch_table()
    fundamental = [0, 0]
    found = [0, 0]
    rows = io.StringIO()
    writer = csv.writer(rows, delimiter='\t', lineterminator='\n')
    writer.writerow(('discriminant', 'phase_x', 'lower_milli'))
    for d in range(-DISCRIMINANT_LIMIT, DISCRIMINANT_LIMIT + 1):
        if abs(d) <= 1:
            continue
        char = character(d)
        if char is None:
            continue
        group = int(d > 0)
        fundamental[group] += 1
        result = certificate(d, char, weights, vm, arch)
        if result:
            found[group] += 1
            writer.writerow((d, *result))
    data = rows.getvalue().encode()
    if args.output:
        args.output.write_bytes(lzma.compress(data))
    print(json.dumps(dict(fundamental=fundamental, witnesses=found,
                          tsv_sha256=hashlib.sha256(data).hexdigest())))


if __name__ == '__main__':
    main()
